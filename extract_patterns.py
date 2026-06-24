#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для извлечения примеров кода из .mac файлов и дополнения pattern-файлов.
"""

import os
import re
import random
from collections import defaultdict

random.seed(42)

# Директории
MAC_DIR = '/Users/lipanovav/rag/03_MacDir/Mac'
PRACTICE_DIR = '/Users/lipanovav/rag/knowledge/practice'

# Ключевые слова для каждого паттерна
PATTERN_KEYWORDS = {
    'pattern_file_operations.md': [
        'tbfile', 'trechandler', 'insert', 'update', 'delete', 'next', 'prev', 'rewind',
        'geteq', 'getge', 'getle', 'getgt', 'getlt', 'nrec', 'clear', 'packvarbuff',
        'setbuff', 'copy', 'fldnumber', 'fldname', 'fldoffset', 'recsize', 'varsize',
        'openmode', 'filename', 'lock', 'unlock', 'record ', 'record\t'
    ],
    'pattern_loops.md': [
        'while', 'for ', 'break', 'continue', 'end while', 'end for'
    ],
    'pattern_sql_queries.md': [
        'select', 'from', 'where', 'join', 'group by', 'order by', 'having', 'union',
        'rsdrecordset', 'rsdcommand', 'execute', 'query', 'dataset', 'execsqlselect',
        'execsql', 'rsdcommand', 'rsdrecordset'
    ],
    'pattern_dialogs.md': [
        'rundialog', 'addscroll', 'msgbox', 'setfocus', 'disablefields', 'enablefields',
        'settimer', 'trechandler', 'dialog', 'dlg_', 'cm_'
    ],
    'pattern_reports.md': [
        'jasper', 'report', 'reportform', 'repform', 'print', 'trepform', 'tpattfieldr',
        'tstreamdoc', 'saveas', 'printlm', 'template'
    ],
    'pattern_classes.md': [
        'class', 'object', 'this.', 'property', 'method', 'constructor', 'genobject'
    ],
    'pattern_string_processing.md': [
        'string', 'strlen', 'substr', 'pos', 'trim', 'upper', 'lower', 'replace', 'format',
        'concat', 'split', 'strcmp', 'strcat', 'strcpy'
    ],
    'pattern_date_money.md': [
        'date', 'time', 'datetime', 'curdate', 'curtime', 'money', 'moneyl', 'decimal',
        'numeric', 'valtype', 'double', 'integer'
    ],
    'pattern_arrays.md': [
        'array', 'tarray', 'size', 'value', 'add', 'remove', 'sort', 'find', 'index',
        'resize', 'asize'
    ],
    'pattern_error_handling.md': [
        'onerror', 'try', 'catch', 'except', 'finally', 'raise', 'error', 'btrerror'
    ],
    'pattern_collections_values.md': [
        'value', 'movenext', 'setparm', 'setattribute', 'setlinkedvalue', 'setfieldvalue',
        'getfieldvalue', 'setpanelvalue', 'getpanelvalue', 'getlinkedvalue', 'getattribute',
        'getregistryvalue', 'setregistryvalue'
    ],
    'pattern_type_conversion.md': [
        'int(', 'string(', 'double(', 'nvl', 'sql_convtypeinteger', 'sql_convtypedate',
        'sql_convtypedouble', 'sql_convtypemoney', 'sql_convtypestring', 'getsqldate',
        'todate', 'tostring', 'tomoney', 'tointeger', 'todouble', 'valtype', 'isnull', 'isempty'
    ],
    'pattern_math_aggregate.md': [
        'abs', 'round', 'sum', 'min', 'max', 'avg', 'iif', 'ifthenelse', 'sign', 'mod',
        'div', 'pow', 'sqrt', 'exp', 'ln', 'log'
    ],
    'pattern_business_api.md': [
        'executestep', 'runerror', 'записатьполелог', 'проводкапокатегориямучета',
        'isexistaccount', 'getaccount', 'openaccount', 'closeaccount', 'getclientname',
        'getclient', 'getfirolebyportfolio', 'getportfolio', 'getdeal', 'getdocument',
        'getoperation', 'checkpermission', 'setpermission', 'calcreserve', 'calcinterest',
        'calccommission', 'getrate', 'getcurrency', 'getbalance', 'getrest', 'setrest',
        'writelog', 'addlog', 'setlog', 'msg'
    ],
    'pattern_excel_reports.md': [
        'copyallsheetintotalbook', 'dp_addprintcell', 'addprintcell', 'addfieldproc',
        'addfield', 'setcellvalue', 'getcellvalue', 'addsheet', 'addpage', 'setpage',
        'printcell', 'printrow', 'printcolumn', 'printheader', 'printfooter', 'setprintparam',
        'getprintparam', 'exporttoexcel', 'exporttoword', 'exporttopdf', 'savetofile',
        'loadfromfile', 'createreport', 'buildreport', 'generatereport', 'fillreport',
        'filltemplate', 'addtemplate', 'settemplate', 'gettemplate', 'template'
    ],
    'pattern_sql_advanced.md': [
        'sqlparam', 'addparam', 'execsqlselect', 'execsql', 'execsqlupdate', 'execsqlinsert',
        'execsqldelete', 'dl_rsdcommand', 'dl_rsdrecordset', 'trsbdataset', 'getrq',
        'makearray', 'buildsql', 'preparesql', 'bindparam', 'executequery', 'executeupdate',
        'executebatch', 'transaction', 'commit', 'rollback', 'begintrans', 'savepoint',
        'cursor', 'fetch', 'opencursor', 'closecursor', 'getcursor', 'setcursor',
        'queryresult', 'resultset', 'recordcount', 'fieldcount', 'fieldname', 'fieldtype',
        'fieldsize', 'isnullfield', 'isemptyfield'
    ],
}

# Компилируем регулярки для скорости
PATTERN_REGEX = {}
for pattern_name, keywords in PATTERN_KEYWORDS.items():
    # Создаем regex для каждого ключевого слова
    compiled = []
    for kw in keywords:
        # Экранируем специальные символы
        escaped = re.escape(kw)
        if kw.endswith('(') or kw.endswith('_'):
            compiled.append(re.compile(r'\b' + escaped, re.IGNORECASE))
        else:
            compiled.append(re.compile(r'\b' + escaped + r'\b', re.IGNORECASE))
    PATTERN_REGEX[pattern_name] = compiled


def extract_macros(content):
    """Извлекает макросы из содержимого .mac файла."""
    lines = content.split('\n')
    macros = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Начало макроса: строка начинается с "macro " (без отступа или с минимальным)
        if stripped.lower().startswith('macro ') and len(line) - len(line.lstrip()) <= 2:
            start = i
            macro_name = stripped[6:].split('(')[0].split(';')[0].strip()
            i += 1
            while i < len(lines):
                end_line = lines[i]
                end_stripped = end_line.strip()
                if end_stripped.lower() == 'end;' and len(end_line) - len(end_line.lstrip()) <= 2:
                    macro_body = '\n'.join(lines[start:i+1])
                    macros.append((macro_name, macro_body))
                    i += 1
                    break
                i += 1
            else:
                # Дошли до конца файла без end;
                macro_body = '\n'.join(lines[start:])
                macros.append((macro_name, macro_body))
        else:
            i += 1
    return macros


def extract_script_blocks(content):
    """Для файлов без макросов извлекает значимые блоки кода."""
    lines = content.split('\n')
    # Убираем комментарии и пустые строки в начале
    start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith('/*') and not stripped.startswith('*/') and not stripped.startswith('*'):
            start = i
            break
    
    # Ищем блоки, разделенные пустыми строками
    blocks = []
    current = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped:
            current.append(line)
        elif current:
            block_body = '\n'.join(current)
            if len(block_body) > 200:  # Минимальный размер блока
                blocks.append(('', block_body))
            current = []
    if current:
        block_body = '\n'.join(current)
        if len(block_body) > 200:
            blocks.append(('', block_body))
    
    return blocks


def classify_block(block_body):
    """Классифицирует блок кода по паттернам."""
    scores = {}
    for pattern_name, regexes in PATTERN_REGEX.items():
        score = 0
        for regex in regexes:
            score += len(regex.findall(block_body))
        scores[pattern_name] = score
    
    if max(scores.values()) == 0:
        return None
    
    return max(scores, key=scores.get)


def get_existing_examples(pattern_file):
    """Получает количество существующих примеров в файле."""
    with open(pattern_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return len(re.findall(r'## Пример \d+:', content))


def get_existing_sources(pattern_file):
    """Получает уже использованные источники."""
    with open(pattern_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return set(re.findall(r'\*\*Источник:\*\* `([^`]+)`', content))


def add_examples_to_pattern(pattern_file, examples):
    """Добавляет примеры в конец pattern-файла."""
    with open(pattern_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    current_count = len(re.findall(r'## Пример \d+:', content))
    
    additions = []
    for i, (macro_name, block_body, source_path, block_type) in enumerate(examples):
        example_num = current_count + i + 1
        line_count = len(block_body.split('\n'))
        
        # Очищаем тело блока от лишних пробелов в конце
        block_body = block_body.rstrip()
        
        additions.append(f"""## Пример {example_num}: `{macro_name}`

**Источник:** `{source_path}`
**Тип:** `{block_type}`
**Размер:** {line_count} строк

```rsl
{block_body}
```

---
""")
    
    # Добавляем в конец файла
    if content.rstrip().endswith('---'):
        new_content = content.rstrip() + '\n\n' + '\n'.join(additions)
    else:
        new_content = content.rstrip() + '\n\n' + '\n'.join(additions)
    
    with open(pattern_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(examples)


def main():
    print("Сканирование .mac файлов...")
    
    # Собираем все .mac файлы среднего размера
    mac_files = []
    for root, dirs, filenames in os.walk(MAC_DIR):
        for f in filenames:
            if f.endswith('.mac'):
                p = os.path.join(root, f)
                s = os.path.getsize(p)
                if 500 < s < 50000:
                    mac_files.append(p)
    
    print(f"Найдено {len(mac_files)} файлов среднего размера")
    
    # Перемешиваем для случайности
    random.shuffle(mac_files)
    
    # Собираем все примеры, классифицированные по паттернам
    pattern_examples = defaultdict(list)
    used_sources = defaultdict(set)  # источники, уже использованные в каждом паттерне
    used_macros = defaultdict(set)   # макросы, уже использованные (по имени)
    
    # Загружаем уже использованные источники
    pattern_files = [f for f in os.listdir(PRACTICE_DIR) if f.startswith('pattern_') and f.endswith('.md')]
    for pf in pattern_files:
        full_path = os.path.join(PRACTICE_DIR, pf)
        used_sources[pf] = get_existing_sources(full_path)
    
    processed = 0
    for filepath in mac_files:
        rel_path = os.path.relpath(filepath, MAC_DIR)
        source_path = 'Mac/' + rel_path
        
        try:
            with open(filepath, 'rb') as f:
                content = f.read().decode('cp866', errors='replace').replace('\r', '')
        except Exception as e:
            continue
        
        # Извлекаем макросы
        macros = extract_macros(content)
        
        if macros:
            for macro_name, macro_body in macros:
                # Пропускаем слишком короткие или слишком длинные макросы
                line_count = len(macro_body.split('\n'))
                if line_count < 5 or line_count > 150:
                    continue
                
                # Классифицируем
                pattern = classify_block(macro_body)
                if pattern is None:
                    continue
                
                # Проверяем дубли
                macro_key = f"{macro_name}:{source_path}"
                if macro_key in used_macros[pattern]:
                    continue
                
                # Проверяем, что не использовали этот файл уже для этого паттерна (не более 2 макросов из одного файла)
                source_count = sum(1 for _, _, src, _ in pattern_examples[pattern] if src == source_path)
                if source_count >= 2:
                    continue
                
                pattern_examples[pattern].append((macro_name, macro_body, source_path, 'macro'))
                used_macros[pattern].add(macro_key)
        else:
            # Файлы без макросов - извлекаем как блок
            blocks = extract_script_blocks(content)
            for block_name, block_body in blocks:
                line_count = len(block_body.split('\n'))
                if line_count < 10 or line_count > 150:
                    continue
                
                pattern = classify_block(block_body)
                if pattern is None:
                    continue
                
                source_count = sum(1 for _, _, src, _ in pattern_examples[pattern] if src == source_path)
                if source_count >= 2:
                    continue
                
                pattern_examples[pattern].append((block_name or 'Блок', block_body, source_path, 'block'))
        
        processed += 1
        if processed % 500 == 0:
            total = sum(len(v) for v in pattern_examples.values())
            print(f"  Обработано {processed} файлов, собрано {total} примеров")
    
    print(f"\nСобрано примеров по паттернам:")
    for pattern in sorted(pattern_examples.keys()):
        print(f"  {pattern}: {len(pattern_examples[pattern])}")
    
    # Теперь дополняем pattern-файлы
    print("\nОбновление pattern-файлов...")
    added_counts = {}
    
    for pattern_file in sorted(pattern_files):
        full_path = os.path.join(PRACTICE_DIR, pattern_file)
        current = get_existing_examples(full_path)
        target = 40  # целевое количество
        needed = max(0, target - current)
        
        if needed > 0 and pattern_file in pattern_examples:
            available = pattern_examples[pattern_file]
            # Берем случайные примеры, но стабильно (seed фиксирован)
            random.seed(42)
            selected = random.sample(available, min(needed, len(available)))
            
            count = add_examples_to_pattern(full_path, selected)
            added_counts[pattern_file] = count
            print(f"  {pattern_file}: было {current}, добавлено {count}, стало {current + count}")
        else:
            added_counts[pattern_file] = 0
            print(f"  {pattern_file}: было {current}, добавлено 0 (недостаточно примеров или уже достаточно)")
    
    # Создаем отчет
    report_lines = ["# Отчет о дополнении pattern-файлов\n"]
    report_lines.append("| Pattern-файл | Было | Добавлено | Стало |")
    report_lines.append("|-------------|------|-----------|-------|")
    
    for pattern_file in sorted(pattern_files):
        full_path = os.path.join(PRACTICE_DIR, pattern_file)
        current = len(re.findall(r'## Пример \d+:', open(full_path, 'r', encoding='utf-8').read()))
        added = added_counts.get(pattern_file, 0)
        was = current - added
        report_lines.append(f"| {pattern_file} | {was} | {added} | {current} |")
    
    report_path = '/Users/lipanovav/rag/pattern_update_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"\nОтчет сохранен: {report_path}")
    print("Готово!")


if __name__ == '__main__':
    main()
