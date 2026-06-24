#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Извлечение паттернов из коллекции RSL-макросов (.mac) в knowledge/practice/

Цель: создать обучающую выборку реальных примеров кода для каждого типового паттерна.
"""

import os
import re
import random
import hashlib

MAC_DIR = "/Users/lipanovav/rag/03_MacDir"
OUT_DIR = "/Users/lipanovav/rag/knowledge/practice"

os.makedirs(OUT_DIR, exist_ok=True)

# ── Regex для извлечения процедур ───────────────────────────────────────────
MACRO_RE = re.compile(r'^(private\s+)?(macro|function)\s+(\w+)', re.IGNORECASE)
END_RE_INLINE = re.compile(r'end\s*;', re.IGNORECASE)
END_RE = re.compile(r'^end\s*;', re.IGNORECASE)

# Словарь паттернов: (название, regex для поиска в теле, описание, ссылка на теорию)
PATTERNS = {
    'file_operations': (
        re.compile(r'\b(file|tbfile|next\s*\(|prev\s*\(|insert\s*\(|update\s*\(|delete\s*\(|geteq|getge|getle|getgt|getlt|rewind|lock|unlock|nrec|clear|packvarbuff|setbuff|copy\s*\(|fldnumber|fldname|fldoffset|recsize|varsize|openmode|filename)\b', re.I),
        "Работа с таблицами базы данных (FILE, Tbfile, навигация, модификация записей)",
        "BnRSL.md## Объектные типы"
    ),
    'loops': (
        re.compile(r'\b(while\s*\(|for\s*\(|break|continue)\b', re.I),
        "Циклы (WHILE, FOR, BREAK, CONTINUE)",
        "BnRSL.md## Инструкция цикла WHILE"
    ),
    'sql_queries': (
        re.compile(r'\b(select\s+|from\s+|where\s+|join\s+|group\s+by|order\s+by|having|union|rsdrecordset|rsdcommand|execute|query|dataset)\b', re.I),
        "SQL-запросы и работа с наборами данных (RsdRecordSet, RsdCommand)",
        "BnRSL.md## Класс: `RsdRecordset`"
    ),
    'dialogs': (
        re.compile(r'\b(rundialog|addscroll|msgbox|setfocus|disablefields|enablefields|settimer|t rechandler|dialog|dlg_|cm_)\b', re.I),
        "Диалоговые окна и интерактивные элементы (RunDialog, TRecHandler, MsgBox)",
        "BnRSL.md## Процедура: `RunDialog`"
    ),
    'reports': (
        re.compile(r'\b(jasper|report|reportform|repform|print|excel|word|template|trepform|tpattfieldr|tstreamdoc|saveas)\b', re.I),
        "Печатные формы и отчёты (JasperReports, TRepForm, TStreamDoc)",
        "BnRSL.md## Класс: `TRepForm`"
    ),
    'classes': (
        re.compile(r'\b(class\s+|object|this\.|property|method|constructor|genobject)\b', re.I),
        "Объектно-ориентированное программирование (Class, Object, this, свойства, методы)",
        "BnRSL.md## Объектные типы"
    ),
    'string_processing': (
        re.compile(r'\b(string\s*\(|strlen|substr|pos|trim|upper|lower|replace|format|concat|split|strcmp|strcat)\b', re.I),
        "Обработка строк (string, strlen, substr, pos, trim)",
        "BnRSL.md## Скалярные типы"
    ),
    'date_money': (
        re.compile(r'\b(date|time|datetime|curdate|curtime|money|moneyl|decimal|numeric|valtype|double|integer)\b', re.I),
        "Работа с датами, временем и денежными типами (Date, Money, DateTime, CurDate)",
        "BnRSL.md## Скалярные типы"
    ),
    'arrays': (
        re.compile(r'\b(array|tarray|size\s*\(|value\s*\(|add\s*\(|remove|sort|find|index|resize)\b', re.I),
        "Массивы и динамические коллекции (Array, TArray, size, value)",
        "BnRSL.md## Класс: `TArray`"
    ),
    'error_handling': (
        re.compile(r'\b(onerror|try|catch|except|finally|raise|error|btrerror)\b', re.I),
        "Обработка ошибок и исключений (OnError, BtrError)",
        "BnRSL.md## Комментарии"
    ),
    'imports_modules': (
        re.compile(r'\b(import\s+|export\s+)\b', re.I),
        "Модульная архитектура (IMPORT, подключение библиотек)",
        "BnRSL.md## Директива IMPORT"
    ),
    'collections_values': (
        re.compile(r'\b(value\s*\(|moveNext|MoveNext|Next|SetParm|setAttribute|SetLinkedValue|SetFieldValue|GetFieldValue|SetPanelValue|GetPanelValue|GetLinkedValue|GetAttribute|GetRegistryValue|SetRegistryValue)\b', re.I),
        "Коллекции, навигация и доступ к полям (value, moveNext, SetParm, GetFieldValue, SetFieldValue)",
        "BnRSL.md## Класс: `TArray`"
    ),
    'type_conversion': (
        re.compile(r'\b(int\s*\(|Int\s*\(|string\s*\(|double\s*\(|NVL|nvl|SQL_ConvTypeInteger|SQL_ConvTypeDate|SQL_ConvTypeDouble|SQL_ConvTypeMoney|SQL_ConvTypeString|GetSQLDate|ToDate|ToString|ToMoney|ToInteger|ToDouble|ValType|IsNull|IsEmpty)\b', re.I),
        "Преобразование типов данных (int, string, NVL, SQL_ConvType, ValType)",
        "BnRSL.md## Скалярные типы"
    ),
    'math_aggregate': (
        re.compile(r'\b(abs\s*\(|round\s*\(|SUM|MIN|MAX|AVG|IIF\s*\(|IfThenElse|sign\s*\(|mod\s*\(|div\s*\(|pow\s*\(|sqrt\s*\(|exp\s*\(|ln\s*\(|log)\b', re.I),
        "Математические и агрегатные функции (abs, SUM, IIF, round, min, max)",
        "BnRSL.md## Выражения"
    ),
    'business_api': (
        re.compile(r'\b(ExecuteStep|RunError|ЗаписатьПолеЛог|ПроводкаПоКатегориямУчета|IsExistAccount|GetAccount|OpenAccount|CloseAccount|GetClientName|GetClient|GetFIRoleByPortfolio|GetPortfolio|GetDeal|GetDocument|GetOperation|CheckPermission|SetPermission|CalcReserve|CalcInterest|CalcCommission|GetRate|GetCurrency|GetBalance|GetRest|SetRest|WriteLog|AddLog|SetLog|msg\s*\()\b', re.I),
        "Банковская бизнес-логика (ExecuteStep, RunError, GetAccount, IsExistAccount, ПроводкаПоКатегориямУчета)",
        "BnRSL.md## Структура RSL-программы"
    ),
    'excel_reports': (
        re.compile(r'\b(CopyAllSheetInTotalBook|DP_AddPrintCell|AddPrintCell|AddFieldProc|AddField|SetPanelValue|SetCellValue|GetCellValue|AddSheet|AddPage|SetPage|PrintCell|PrintRow|PrintColumn|PrintHeader|PrintFooter|SetPrintParam|GetPrintParam|ExportToExcel|ExportToWord|ExportToPDF|SaveToFile|LoadFromFile|CreateReport|BuildReport|GenerateReport|FillReport|FillTemplate|AddTemplate|SetTemplate|GetTemplate|Template|Excel|Word|PDF|CSV|XML|HTML|RTF)\b', re.I),
        "Excel, печатные формы и шаблоны отчётов (AddPrintCell, CopyAllSheetInTotalBook, ExportToExcel, Template)",
        "BnRSL.md## Класс: `TRepForm`"
    ),
    'sql_advanced': (
        re.compile(r'\b(SQLParam|addParam|AddParam|execSQLselect|execSQL|execSQLupdate|execSQLinsert|execSQLdelete|DL_RSDCommand|DL_RSDRecordSet|TRsbDataSet|GetRQ|makeArray|BuildSQL|PrepareSQL|BindParam|ExecuteQuery|ExecuteUpdate|ExecuteBatch|Transaction|Commit|Rollback|BeginTrans|Savepoint|Cursor|Fetch|OpenCursor|CloseCursor|GetCursor|SetCursor|QueryResult|ResultSet|RecordCount|FieldCount|FieldName|FieldType|FieldSize|IsNullField|IsEmptyField)\b', re.I),
        "Продвинутая работа с SQL (SQLParam, addParam, execSQLselect, DL_RSDCommand, TRsbDataSet)",
        "BnRSL.md## Класс: `RsdRecordset`"
    ),
}


def extract_procedures(content: str):
    """Извлекает все процедуры/функции из текста .mac файла."""
    lines = content.split('\n')
    procs = []
    i = 0
    while i < len(lines):
        m = MACRO_RE.match(lines[i])
        if m:
            start = i
            depth = 1
            j = i + 1
            # Однострочный макрос: проверяем, нет ли end; на той же строке
            if END_RE_INLINE.search(lines[i][m.end():]):
                # Однострочный макрос
                j = i + 1
            else:
                while j < len(lines) and depth > 0:
                    line_stripped = lines[j].strip()
                    line_lower = line_stripped.lower()
                    # Вложенные macro/function увеличивают depth
                    nested = MACRO_RE.match(lines[j])
                    if nested:
                        # Если это однострочный вложенный макрос, не увеличиваем depth
                        if not END_RE.search(lines[j][nested.end():]):
                            depth += 1
                    elif line_lower.startswith('end') or line_lower == 'end':
                        depth -= 1
                    j += 1
            body_lines = lines[start:j]
            body = '\n'.join(body_lines)
            procs.append({
                'name': m.group(3),
                'kind': m.group(2).lower(),
                'private': m.group(1) is not None,
                'body': body,
                'line_count': j - start,
                'source': '',
            })
            i = j
        else:
            i += 1
    return procs


def classify_procedure(body: str):
    """Возвращает список паттернов, которые встречаются в теле процедуры."""
    matches = []
    for pat_name, (pat_re, _, _) in PATTERNS.items():
        if pat_re.search(body):
            matches.append(pat_name)
    return matches


def clean_body(body: str) -> str:
    """Очистка тела процедуры для вывода."""
    lines = body.split('\n')
    # Убираем пустые строки в начале и конце
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return '\n'.join(lines)


def score_procedure(body: str) -> int:
    """Оценка качества примера (чем выше, тем лучше для обучения)."""
    lines = body.split('\n')
    score = 0
    # Комментарии — хорошо
    score += sum(1 for l in lines if l.strip().startswith('//') or l.strip().startswith('/*')) * 2
    # Умеренная длина (не слишком короткая, не слишком длинная)
    if 5 <= len(lines) <= 60:
        score += 10
    elif 60 < len(lines) <= 100:
        score += 5
    # Наличие параметров — хорошо (показывает интерфейс)
    if '(' in lines[0] and ')' in lines[0]:
        score += 3
    # Несколько конструкций — показывает реальное использование
    score += len([l for l in lines if re.search(r'\b(if|while|for|macro|function|class|return|var)\b', l, re.I)]) * 1
    return score


def main():
    # 1. Собираем все .mac файлы
    all_files = []
    for root, _, filenames in os.walk(MAC_DIR):
        for f in filenames:
            if f.endswith('.mac'):
                fpath = os.path.join(root, f)
                if os.path.getsize(fpath) > 0:
                    all_files.append(fpath)

    print(f"Всего .mac файлов: {len(all_files)}")

    # 2. Случайная выборка для анализа (все 9000+ — слишком много, берём 2000)
    random.seed(42)
    sample_size = min(2000, len(all_files))
    sample = random.sample(all_files, sample_size)
    print(f"Анализируем выборку: {sample_size} файлов")

    # 3. Извлекаем процедуры и классифицируем
    examples = {k: [] for k in PATTERNS}
    total_procs = 0

    for fpath in sample:
        try:
            with open(fpath, 'r', encoding='cp866', errors='ignore') as f:
                content = f.read()
        except Exception:
            continue

        procs = extract_procedures(content)
        for proc in procs:
            total_procs += 1
            proc['source'] = os.path.relpath(fpath, MAC_DIR)
            patterns = classify_procedure(proc['body'])
            proc['patterns'] = patterns
            for pat in patterns:
                if pat in examples:
                    examples[pat].append(proc)

    print(f"Всего извлечено процедур: {total_procs}")
    for pat, procs in examples.items():
        print(f"  {pat}: {len(procs)} примеров")

    # 4. Для каждого паттерна выбираем лучшие 10-15 примеров и сохраняем в MD
    for pat_name, (pat_re, description, theory_link) in PATTERNS.items():
        procs = examples[pat_name]
        if not procs:
            print(f"  ⚠️ {pat_name}: нет примеров, пропускаем")
            continue

        # Сортируем по score, убираем дубликаты (по хешу тела)
        seen = set()
        unique_procs = []
        for p in sorted(procs, key=lambda x: score_procedure(x['body']), reverse=True):
            h = hashlib.md5(p['body'].encode('utf-8', errors='ignore')).hexdigest()[:16]
            if h not in seen and len(unique_procs) < 15:
                seen.add(h)
                unique_procs.append(p)

        # Формируем MD
        lines = [f"# Практика: {description}", ""]
        lines.append(f"**Теория:** [{theory_link}]")
        lines.append("")
        lines.append(f"Ниже приведены {len(unique_procs)} реальных примера из производственной кодовой базы RS-Bank.")
        lines.append("")

        for i, p in enumerate(unique_procs, 1):
            lines.append(f"## Пример {i}: `{p['name']}`")
            lines.append("")
            lines.append(f"**Источник:** `{p['source']}`  ")
            lines.append(f"**Тип:** `{'private ' if p['private'] else ''}{p['kind']}`  ")
            lines.append(f"**Размер:** {p['line_count']} строк")
            lines.append("")
            lines.append("```rsl")
            lines.append(clean_body(p['body']))
            lines.append("```")
            lines.append("")

            # Добавляем пояснение, если есть комментарии в начале
            body_lines = p['body'].split('\n')
            comment_lines = []
            for l in body_lines[1:]:  # пропускаем заголовок macro
                lstrip = l.strip()
                if lstrip.startswith('//') or lstrip.startswith('/*'):
                    comment_lines.append(lstrip.lstrip('/').lstrip('*').strip())
                elif lstrip:
                    break
            if comment_lines:
                lines.append("**Комментарий автора:**")
                lines.append(' '.join(comment_lines[:3]))
                lines.append("")
            lines.append("---")
            lines.append("")

        out_path = os.path.join(OUT_DIR, f"pattern_{pat_name}.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        print(f"  ✅ {out_path} ({len(unique_procs)} примеров)")

    print("Готово!")


if __name__ == '__main__':
    main()
