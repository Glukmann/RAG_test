#!/usr/bin/env python3
"""
Извлечение структуры БД и бизнес-контекста из макросов RSL.
Анализирует .mac файлы, находит таблицы, поля, SQL-запросы и их контекст.
"""

import os, re, random, json
from collections import defaultdict

MAC_DIR = "/Users/lipanovav/rag/03_MacDir"
OUT_DIR = "/Users/lipanovav/rag/knowledge"

# --- Регулярки для поиска обращений к БД ---
FILE_RE = re.compile(r'\bfile\s+(\w+)\s*\(\s*"?([^"\)]+)"?\s*\)', re.I)
RECORD_RE = re.compile(r'\brecord\s+(\w+)\s*\(\s*"?([^"\)]+)"?\s*\)', re.I)
TBFILE_RE = re.compile(r'\bTbfile\s*\(\s*"([^"]+)"', re.I)
TRECH_RE = re.compile(r'\bTRecHandler\s*\(\s*"([^"]+)"', re.I)

# Поля вида: file.rec.Field или file.Field
FIELD_REC_RE = re.compile(r'\b(\w+)\.rec\.([A-Za-zА-Яа-я0-9_]+)', re.I)
FIELD_DIRECT_RE = re.compile(r'\b(\w+)\.([A-Za-zА-Яа-я0-9_]+)\b', re.I)

# SQL SELECT ... FROM
def extract_sql_queries(text):
    """Извлекает SQL-запросы из строковых конкатенаций."""
    queries = []
    # Собираем строки, заканчивающиеся на + (конкатенация SQL)
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Начало SQL-запроса в строке
        if re.search(r'"SELECT\s', line, re.I):
            query_lines = [line]
            j = i + 1
            while j < len(lines):
                l = lines[j].strip()
                if not l.endswith('"') and not l.endswith('+'):
                    query_lines.append(l)
                    break
                query_lines.append(l)
                if l.endswith('"') and not l.endswith('+'):
                    break
                j += 1
            query = ' '.join(query_lines)
            queries.append(query)
            i = j + 1
        else:
            i += 1
    return queries

# --- Класс для хранения инфы о таблице ---
class TableInfo:
    def __init__(self, name):
        self.name = name
        self.fields = set()
        self.aliases = set()  # имена переменных, которым присвоена эта таблица
        self.contexts = []  # (макрос, описание, процедура, путь)
        self.sql_queries = []  # SQL-запросы, использующие эту таблицу

    def to_dict(self):
        return {
            'name': self.name,
            'fields': sorted(self.fields),
            'aliases': sorted(self.aliases),
            'contexts': self.contexts[:5],  # топ-5 контекстов
            'sql_queries': self.sql_queries[:3],
        }


def extract_header_info(text):
    """Извлекает описание из шапки .mac файла."""
    info = {'name': '', 'module': '', 'description': ''}
    for line in text.split('\n')[:40]:
        line = line.strip()
        
        # Формат 1: $Name:, $Module:, $Description: (может быть без /*)
        m = re.match(r'\$Name:\s*(.+)', line, re.I)
        if m:
            info['name'] = m.group(1).strip()
        m = re.match(r'\$Module:\s*(.+)', line, re.I)
        if m:
            info['module'] = m.group(1).strip()
        m = re.match(r'\$Description:\s*(.+)', line, re.I)
        if m:
            info['description'] = m.group(1).strip()
            
        # Формат 2: русский блок (Имя файла : xxx)
        # Ищем .mac в строке с описанием
        m = re.search(r'[:：]\s*(\S+\.mac)', line, re.I)
        if m and not info['name']:
            info['name'] = m.group(1).strip()
        m = re.search(r'Описание\s*[:：]\s*(.+)', line, re.I)
        if m:
            info['description'] = m.group(1).strip()
            
    return info


def extract_procedure_comments(text, proc_name):
    """Извлекает комментарии перед процедурой."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if re.search(rf'\bmacro\s+{proc_name}\b', line, re.I):
            # Ищем комментарии до 5 строк назад
            comments = []
            for j in range(max(0, i-10), i):
                l = lines[j].strip()
                if l.startswith('//') or l.startswith('/*') or l.startswith('*'):
                    comments.append(l.lstrip('/').lstrip('*').strip())
            return ' '.join(comments[:5])
    return ''


def main():
    # Собираем все .mac файлы
    all_files = []
    for root, _, names in os.walk(MAC_DIR):
        for n in names:
            if n.endswith('.mac'):
                p = os.path.join(root, n)
                if os.path.getsize(p) > 0:
                    all_files.append(p)

    random.seed(42)
    sample = random.sample(all_files, min(2000, len(all_files)))
    print(f"Анализ {len(sample)} файлов...")

    tables = {}
    total_procs = 0

    for fpath in sample:
        try:
            with open(fpath, 'r', encoding='cp866', errors='ignore') as f:
                text = f.read()
        except:
            continue

        header = extract_header_info(text)
        rel_path = os.path.relpath(fpath, MAC_DIR)
        basename = os.path.basename(fpath)
        module_from_path = rel_path.split('/')[1] if len(rel_path.split('/')) > 1 else ''
        
        # Если description пустой, используем имя файла
        if not header['description']:
            header['description'] = f"Макрос: {basename}"
        if not header['module']:
            header['module'] = module_from_path
        if not header['name']:
            header['name'] = basename

        # --- Находим таблицы/файлы ---
        for m in FILE_RE.finditer(text):
            alias = m.group(1)
            table_name = m.group(2).strip().lower()
            if table_name not in tables:
                tables[table_name] = TableInfo(table_name)
            tables[table_name].aliases.add(alias)
            tables[table_name].contexts.append({
                'file': rel_path,
                'macro': header.get('name', ''),
                'description': header.get('description', ''),
                'module': header.get('module', ''),
            })

        for m in RECORD_RE.finditer(text):
            alias = m.group(1)
            table_name = m.group(2).strip().lower()
            if table_name not in tables:
                tables[table_name] = TableInfo(table_name)
            tables[table_name].aliases.add(alias)
            tables[table_name].contexts.append({
                'file': rel_path,
                'macro': header.get('name', ''),
                'description': header.get('description', ''),
                'module': header.get('module', ''),
            })

        for m in TBFILE_RE.finditer(text):
            table_name = m.group(1).strip().lower().replace('.dbt', '')
            if table_name not in tables:
                tables[table_name] = TableInfo(table_name)
            tables[table_name].aliases.add('Tbfile')
            tables[table_name].contexts.append({
                'file': rel_path,
                'macro': header.get('name', ''),
                'description': header.get('description', ''),
                'module': header.get('module', ''),
            })

        for m in TRECH_RE.finditer(text):
            table_name = m.group(1).strip().lower().replace('.dbt', '')
            if table_name not in tables:
                tables[table_name] = TableInfo(table_name)
            tables[table_name].aliases.add('TRecHandler')
            tables[table_name].contexts.append({
                'file': rel_path,
                'macro': header.get('name', ''),
                'description': header.get('description', ''),
                'module': header.get('module', ''),
            })

        # --- Находим поля ---
        for m in FIELD_REC_RE.finditer(text):
            alias = m.group(1)
            field = m.group(2)
            # Ищем таблицу по алиасу
            for t in tables.values():
                if alias in t.aliases:
                    t.fields.add(field)
                    break

        # --- Находим SQL-запросы ---
        queries = extract_sql_queries(text)
        for q in queries:
            # Ищем таблицы в SQL (FROM xxx)
            from_match = re.findall(r'FROM\s+(\w+)', q, re.I)
            for t_name in from_match:
                t_name_lower = t_name.lower()
                if t_name_lower not in tables:
                    tables[t_name_lower] = TableInfo(t_name_lower)
                tables[t_name_lower].sql_queries.append(q[:300])

    # --- Фильтруем мусор ---
    # Убираем таблицы без полей и без контекста
    real_tables = {k: v for k, v in tables.items() if v.fields or v.sql_queries or len(v.contexts) > 0}
    # Убираем слишком общие имена
    real_tables = {k: v for k, v in real_tables.items() if len(k) > 2}

    print(f"Найдено таблиц/структур: {len(real_tables)}")

    # --- Сохраняем в JSON ---
    out_json = os.path.join(OUT_DIR, 'db_schema_raw.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump({k: v.to_dict() for k, v in sorted(real_tables.items())}, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {out_json}")

    # --- Генерируем MD ---
    # Группируем по модулям (банковские, кредиты, депозиты и т.д.)
    md_lines = ["# Структура данных RS-Bank (извлечена из макросов)", ""]
    md_lines.append("Данный документ содержит информацию о таблицах, полях и SQL-запросах, извлечённых из реальных макросов RS-Bank.")
    md_lines.append("")

    # Топ-50 таблиц по количеству полей
    top_tables = sorted(real_tables.values(), key=lambda x: -len(x.fields))[:50]

    for t in top_tables:
        md_lines.append(f"## Таблица: `{t.name}`")
        md_lines.append("")

        # Контекст
        if t.contexts:
            ctx = t.contexts[0]
            desc = ctx.get('description', '')
            mod = ctx.get('module', '')
            if desc or mod:
                md_lines.append(f"**Бизнес-контекст:** {mod or ''} {desc or ''}".strip())
                md_lines.append("")

        # Поля
        if t.fields:
            md_lines.append(f"**Поля ({len(t.fields)}):**")
            md_lines.append("")
            for field in sorted(t.fields)[:30]:  # ограничиваем 30 полями
                md_lines.append(f"- `{field}`")
            md_lines.append("")

        # SQL-запросы
        if t.sql_queries:
            md_lines.append(f"**SQL-запросы ({len(t.sql_queries)}):**")
            md_lines.append("")
            for q in t.sql_queries[:2]:
                md_lines.append(f"```sql")
                md_lines.append(q.strip()[:300])
                md_lines.append(f"```")
                md_lines.append("")

        md_lines.append("")

    # Сохраняем MD
    out_md = os.path.join(OUT_DIR, 'db_schema_top50.md')
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines) + '\n')
    print(f"  MD: {out_md}")

    # Генерируем MD с SQL-запросами
    sql_tables = sorted(real_tables.values(), key=lambda x: -len(x.sql_queries))[:30]
    md_sql_lines = ["# SQL-запросы RS-Bank (извлечены из макросов)", ""]
    md_sql_lines.append("Данный документ содержит реальные SQL-запросы, извлечённые из производственных макросов RS-Bank, сгруппированные по таблицам.")
    md_sql_lines.append("")

    for t in sql_tables:
        if not t.sql_queries:
            continue
        md_sql_lines.append(f"## Таблица: `{t.name}`")
        md_sql_lines.append("")
        
        # Контекст
        if t.contexts:
            ctx = t.contexts[0]
            desc = ctx.get('description', '')
            mod = ctx.get('module', '')
            if desc or mod:
                md_sql_lines.append(f"**Бизнес-контекст:** {mod or ''} {desc or ''}".strip())
                md_sql_lines.append("")
        
        # SQL-запросы
        md_sql_lines.append(f"**SQL-запросы ({len(t.sql_queries)}):**")
        md_sql_lines.append("")
        for q in t.sql_queries[:3]:
            md_sql_lines.append(f"```sql")
            md_sql_lines.append(q.strip()[:500])
            md_sql_lines.append(f"```")
            md_sql_lines.append("")
        md_sql_lines.append("")

    out_md_sql = os.path.join(OUT_DIR, 'db_schema_sql.md')
    with open(out_md_sql, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_sql_lines) + '\n')
    print(f"  SQL MD: {out_md_sql}")

    print("Готово!")

if __name__ == '__main__':
    main()
