#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Реструктуризация BnRSL.md по смыслу для RAG.
"""

import re

IN_PATH = "/Users/lipanovav/rag/knowledge/BnRSL.md"
OUT_PATH = "/Users/lipanovav/rag/knowledge/BnRSL_restructured.md"

with open(IN_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def looks_like_heading_continuation(line):
    s = line.strip()
    if not s:
        return False
    if s.startswith('##'):
        return False
    if s.startswith('```'):
        return False
    if s.startswith('Процедура ') and re.match(r'^Процедура\s+[A-Z]', s):
        return False
    if s.startswith('Функция ') and re.match(r'^Функция\s+[A-Z]', s):
        return False
    if s.startswith('Класс ') and re.match(r'^Класс\s+[A-Z]', s):
        return False
    if s.startswith('Метод ') and re.match(r'^Метод\s+[A-Z]', s):
        return False
    if s.startswith('Стандартный класс'):
        return False
    if s.startswith('Использование стандартного класса'):
        return False
    if s.startswith('Встроенные процедуры'):
        return False
    if s.startswith('Пример'):
        return False
    if s.startswith('Примечание'):
        return False
    if s.startswith('Внимание'):
        return False
    return True

def is_procedure_heading(lines, i):
    """Проверяет, что строка i — это заголовок процедуры/функции."""
    line = lines[i].strip()
    if not line.startswith('Процедура ') and not line.startswith('Функция '):
        return False
    parts = line.split()
    if len(parts) != 2:
        return False
    name = parts[1]
    if not re.match(r'^[A-Z][A-Za-z0-9_]*$', name):
        return False
    if i + 1 >= len(lines):
        return False
    next_line = lines[i + 1].strip()
    if next_line.startswith(name + ' ('):
        return True
    return False

def is_class_heading(lines, i):
    line = lines[i].strip()
    if line.startswith('Использование стандартного класса'):
        return True
    if line.startswith('Использование класса'):
        return True
    if line.startswith('Стандартный класс '):
        return True
    if re.match(r'^Класс\s+[A-Z][A-Za-z0-9_]*\b', line):
        return True
    return False

def extract_class_name(line):
    # "Использование стандартного класса Tbfile" -> Tbfile
    # "Использование класса TRcwHost" -> TRcwHost
    m = re.search(r'класса\s+([A-Z][A-Za-z0-9_]*)', line)
    if m:
        return m.group(1)
    # "Стандартный класс TArray" -> TArray
    m = re.match(r'^Стандартный класс\s+([A-Z][A-Za-z0-9_]*)', line)
    if m:
        return m.group(1)
    # "Класс RsdRecordset" -> RsdRecordset
    m = re.match(r'^Класс\s+([A-Z][A-Za-z0-9_]*)', line)
    if m:
        return m.group(1)
    return None

out_lines = []
i = 0
while i < len(lines):
    line = lines[i].rstrip('\n')
    stripped = line.strip()
    
    # Объединяем разорванные заголовки ##
    if stripped.startswith('## ') and not stripped.startswith('## Процедура') and not stripped.startswith('## Функция') and not stripped.startswith('## Класс') and not stripped.startswith('## Метод'):
        heading = stripped[3:].strip()
        # Check if this is a false heading for "Имена" or "Переменные"
        if heading in ('Имена', 'Переменные') and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            # Skip empty line
            if not next_line and i + 2 < len(lines):
                next_line = lines[i + 2].strip()
            if next_line and next_line[0].islower():
                # This is a false heading, output as plain text without ##
                out_lines.append(heading)
                i += 1
                continue
        j = i + 1
        while j < len(lines) and looks_like_heading_continuation(lines[j]):
            heading += ' ' + lines[j].strip()
            j += 1
        out_lines.append(f'## {heading}')
        i = j
        continue
    
    # Удаляем повторяющиеся "Встроенные процедуры"
    if stripped == 'Встроенные процедуры':
        # Проверяем, не является ли это началом группы с подзаголовком
        # Если следующая строка тоже "Встроенные процедуры" — пропускаем
        if i + 1 < len(lines) and lines[i + 1].strip() == 'Встроенные процедуры':
            i += 1
            continue
        # Если это просто разделитель внутри группы — пропускаем
        i += 1
        continue
    
    # Заголовки процедур/функций
    if is_procedure_heading(lines, i):
        kind = stripped.split()[0]  # Процедура или Функция
        name = stripped.split()[1]
        out_lines.append(f'## {kind}: `{name}`')
        out_lines.append('')
        out_lines.append(f'```rsl')
        out_lines.append(lines[i + 1].strip())
        out_lines.append('```')
        out_lines.append('')
        i += 2
        continue
    
    # Заголовки классов
    if is_class_heading(lines, i):
        name = extract_class_name(stripped)
        if name:
            out_lines.append(f'## Класс: `{name}`')
        else:
            out_lines.append(line)
        i += 1
        continue
    
    # Встроенные процедуры как раздел (начало группы)
    if stripped == 'Встроенные процедуры' and i > 0 and not lines[i-1].strip().startswith('## '):
        out_lines.append('## Встроенные процедуры')
        i += 1
        continue
    
    # Общие разделители разделов
    if re.match(r'^(Средство разработки|Встроенные процедуры|Стандартные процедуры)', stripped):
        out_lines.append(f'## {stripped}')
        i += 1
        continue
    
    out_lines.append(line)
    i += 1

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines) + '\n')

print(f"Сохранено: {OUT_PATH}")
print(f"Строк: {len(out_lines)}")

# Статистика
sections = [l for l in out_lines if l.startswith('## ')]
print(f"Секций ##: {len(sections)}")
from collections import Counter
cnt = Counter(l.split(':')[0] if ':' in l else l for l in sections)
for k, v in cnt.most_common(15):
    print(f"  {k}: {v}")
