#!/usr/bin/env python3
"""Анализ 1000 макросов: находим самые частые API-вызовы, не попавшие в паттерны."""
import os, re, random

MAC_DIR = "/Users/lipanovav/rag/03_MacDir"

# Уже покрытые паттернами (примеры примерных regex)
COVERED = {
    'file': re.compile(r'\b(file|tbfile|next\s*\(|prev\s*\(|insert\s*\(|update\s*\(|delete\s*\(|geteq|getge|getle|getgt|getlt|rewind|lock|unlock|nrec|clear|packvarbuff|setbuff|copy\s*\(|fldnumber|fldname|fldoffset|recsize|varsize|openmode|filename)\b', re.I),
    'loop': re.compile(r'\b(while\s*\(|for\s*\(|break|continue)\b', re.I),
    'sql': re.compile(r'\b(select\s+|from\s+|where\s+|join\s+|group\s+by|order\s+by|having|union|rsdrecordset|rsdcommand|execute|query|dataset)\b', re.I),
    'dialog': re.compile(r'\b(rundialog|addscroll|msgbox|setfocus|disablefields|enablefields|settimer|t rechandler|dialog|dlg_|cm_)\b', re.I),
    'report': re.compile(r'\b(jasper|report|reportform|repform|print|excel|word|template|trepform|tpattfieldr|tstreamdoc|saveas)\b', re.I),
    'class': re.compile(r'\b(class\s+|object|this\.|property|method|constructor|genobject)\b', re.I),
    'string': re.compile(r'\b(string\s*\(|strlen|substr|pos|trim|upper|lower|replace|format|concat|split|strcmp|strcat)\b', re.I),
    'date_money': re.compile(r'\b(date|time|datetime|curdate|curtime|money|moneyl|decimal|numeric|valtype|double|integer)\b', re.I),
    'array': re.compile(r'\b(array|tarray|size\s*\(|value\s*\(|add\s*\(|remove|sort|find|index|resize)\b', re.I),
    'error': re.compile(r'\b(onerror|try|catch|except|finally|raise|error|btrerror)\b', re.I),
}

# Regex для поиска вызовов: ИмяПроцедуры( или ИмяКласса(
# Исключаем ключевые слова RSL
RSL_KEYWORDS = {
    'if', 'elif', 'else', 'while', 'for', 'break', 'continue', 'return',
    'macro', 'function', 'end', 'var', 'const', 'record', 'file', 'class',
    'import', 'export', 'private', 'local', 'with', 'this', 'true', 'false',
    'null', 'and', 'or', 'not', 'onerror', 'in', 'new', 'object', 'array',
    'string', 'integer', 'double', 'money', 'bool', 'date', 'time', 'datetime',
    'variant', 'proc', 'method', 'property', 'procedure', 'function'
}

CALL_RE = re.compile(r'\b([A-Za-zА-Яа-я_][A-Za-zА-Яа-я0-9_]*)\s*\(', re.I)

def is_covered(word):
    for pat in COVERED.values():
        if pat.search(word + '()'):
            return True
    return False

def main():
    files = []
    for root, _, names in os.walk(MAC_DIR):
        for n in names:
            if n.endswith('.mac'):
                p = os.path.join(root, n)
                if os.path.getsize(p) > 0:
                    files.append(p)

    random.seed(42)
    sample = random.sample(files, min(2000, len(files)))
    print(f"Анализ {len(sample)} файлов...")

    calls = {}
    for fpath in sample:
        try:
            with open(fpath, 'r', encoding='cp866', errors='ignore') as f:
                text = f.read()
        except:
            continue

        for m in CALL_RE.finditer(text):
            name = m.group(1)
            # Фильтруем
            if len(name) < 2:
                continue
            if name.lower() in RSL_KEYWORDS:
                continue
            if name.isdigit():
                continue
            if is_covered(name):
                continue
            calls[name] = calls.get(name, 0) + 1

    # Топ-100
    sorted_calls = sorted(calls.items(), key=lambda x: -x[1])

    print(f"\nВсего уникальных вызовов (не в паттернах): {len(sorted_calls)}")
    print(f"\nТоп-50 самых частых (потенциальные новые паттерны):\n")
    print(f"{'Название':<40} {'Вызовов':>10}")
    print("-" * 55)
    for name, count in sorted_calls[:50]:
        print(f"{name:<40} {count:>10}")

if __name__ == '__main__':
    main()
