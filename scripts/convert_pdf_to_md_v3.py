#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF → Markdown конвертер для RSL документации (v3).
Ключевые улучшения:
- Удаление строк оглавления (точки + номер страницы).
- Улучшенное определение границ оглавления.
- Разбиение BnRSL по разделам языка.
"""

import os
import re
import fitz

PDF_DIR = "/Users/lipanovav/rag/06_ToolsDoc"
OUT_DIR = "/Users/lipanovav/rag/knowledge"

os.makedirs(OUT_DIR, exist_ok=True)

# ── Утилиты чистки ─────────────────────────────────────────────────────────
COPYRIGHT_RE = re.compile(r'^\s*© АО Эр-Стайл Софтлаб,\s*\d+\s*–\s*\d+\s*$', re.MULTILINE)
MODULE_RE = re.compile(r'^\s*Модуль\s+\w+.*$', re.MULTILINE)
PAGE_NUM_RE = re.compile(r'^\s*\d+\s*$', re.MULTILINE)
TOC_LINE_RE = re.compile(r'\.{3,}.*\d+\s*$', re.MULTILINE)  # строки с точками и номером страницы
TOC_HEADER_RE = re.compile(r'^\s*Оглавление\s*\d*\s*$', re.MULTILINE)  # "Оглавление" или "Оглавление 3"

def clean_page(text: str) -> str:
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if not s:
            out.append(line)
            continue
        if COPYRIGHT_RE.match(s) or MODULE_RE.match(s) or PAGE_NUM_RE.match(s):
            continue
        out.append(line)
    return "\n".join(out)


def extract_raw(path: str) -> str:
    doc = fitz.open(path)
    parts = [clean_page(page.get_text()) for page in doc if page.get_text()]
    doc.close()
    return "\n".join(parts)


def remove_toc_lines(text: str) -> str:
    """Удаляет строки, которые являются элементами оглавления (точки + номер страницы)."""
    lines = text.splitlines()
    out = []
    for line in lines:
        if TOC_LINE_RE.search(line) or TOC_HEADER_RE.match(line.strip()):
            continue
        out.append(line)
    return "\n".join(out)


# ── Удаление оглавления ─────────────────────────────────────────────────────
TOC_STOP_PATTERNS = [
    re.compile(r'^\s*Введение\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*ПРЕДИСЛОВИЕ\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Introduction\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Особенности\s+реализации\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Технологическая\s+модель\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Общие\s+положения\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Работа\s+с\s+DLM\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Описание\s+инструмента\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Элементы\s+языка\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Инструмент\s+записи\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Редактор\s+ресурсов\b', re.MULTILINE | re.IGNORECASE),
]

def strip_toc(text: str) -> str:
    """Обрезает текст до первого значимого раздела (после оглавления)."""
    best_pos = -1
    for pat in TOC_STOP_PATTERNS:
        m = pat.search(text)
        if m:
            pos = m.start()
            # проверяем, что после найденного заголовка не идёт сразу оглавление (точки)
            tail = text[pos:pos+300]
            if not TOC_LINE_RE.search(tail):
                if best_pos == -1 or pos < best_pos:
                    best_pos = pos
    if best_pos != -1 and best_pos < len(text) * 0.35:
        return text[best_pos:]
    return text


# ── Вспомогательные функции форматирования ─────────────────────────────────
def convert_bullets(text: str) -> str:
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if s.startswith('·') or s.startswith('‐') or s.startswith('–') or s.startswith('-'):
            out.append('- ' + s[1:].strip())
        else:
            out.append(line)
    return "\n".join(out)


def looks_like_signature(s: str) -> bool:
    return '(' in s


def is_toc_entry(body: str) -> bool:
    cleaned = re.sub(r'\s+', '', body)
    return bool(re.fullmatch(r'[\.\d]+', cleaned))


def normalize_whitespace(text: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', text)


# ── Стратегия RSLprc ───────────────────────────────────────────────────────
RSLPROC_SPLIT_RE = re.compile(r'^(Процедура|Функция|Класс|Метод)\s+([A-Za-zА-Яа-я0-9_]+)', re.MULTILINE)

def process_rslprc(text: str, title: str) -> str:
    text = remove_toc_lines(text)
    text = strip_toc(text)
    matches = list(RSLPROC_SPLIT_RE.finditer(text))
    if not matches:
        return f"# {title}\n\n{normalize_whitespace(text.strip())}"

    meta = text[:matches[0].start()].strip()
    lines = [f"# {title}", ""]
    if meta:
        lines.append(normalize_whitespace(meta))
        lines.append("")

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        kind = m.group(1)
        name = m.group(2)
        body = text[start + len(m.group(0)):end].strip()

        if is_toc_entry(body):
            continue
        if kind in ('Процедура', 'Функция', 'Метод') and not looks_like_signature(body[:300]):
            continue

        lines.append(f"## {kind}: `{name}`")
        lines.append("")
        sig_lines = []
        idx = 0
        body_lines = body.splitlines()
        while idx < len(body_lines):
            l = body_lines[idx].strip()
            if not l:
                idx += 1
                continue
            if l.startswith('Параметры:') or l.startswith('Возвращаемое значение:') or l.startswith('Примечание.') or l.startswith('Пример.') or l.startswith('Свойства:') or l.startswith('Методы:'):
                break
            sig_lines.append(l)
            idx += 1
            if l.endswith(')'):
                break
        if sig_lines:
            sig = " ".join(sig_lines)
            lines.append(f"```rsl\n{sig}\n```")
            lines.append("")
        rest = "\n".join(body_lines[idx:]).strip()
        if rest:
            split_pat = re.compile(r'^(Параметры:|Возвращаемое значение:|Примечание\.|Пример\.|Свойства:|Методы:|Описание:)', re.MULTILINE)
            parts = list(split_pat.finditer(rest))
            if parts:
                desc = rest[:parts[0].start()].strip()
                if desc:
                    lines.append(desc)
                    lines.append("")
                for j, p in enumerate(parts):
                    sec_name = p.group(1).rstrip('.').rstrip(':')
                    sec_start = p.start()
                    sec_end = parts[j+1].start() if j+1 < len(parts) else len(rest)
                    sec_body = rest[sec_start + len(p.group(1)):sec_end].strip()
                    lines.append(f"**{sec_name}:**")
                    lines.append("")
                    lines.append(convert_bullets(sec_body))
                    lines.append("")
            else:
                lines.append(convert_bullets(rest))
                lines.append("")
    return "\n".join(lines)


# ── Стратегия SQL ──────────────────────────────────────────────────────────
SQL_PACKAGE_RE = re.compile(r'^Пакет\s+([A-Za-z0-9_]+)', re.MULTILINE)
SQL_PROC_RE = re.compile(r'^([A-Z][A-Za-z0-9_]*)\s*\(', re.MULTILINE)
SQL_CONST_RE = re.compile(r'^([A-Z][A-Z0-9_]*)\s+–', re.MULTILINE)

def process_sql(text: str, title: str) -> str:
    text = remove_toc_lines(text)
    text = strip_toc(text)
    lines = [f"# {title}", ""]
    pkg_matches = list(SQL_PACKAGE_RE.finditer(text))
    if not pkg_matches:
        lines.append(normalize_whitespace(text.strip()))
        return "\n".join(lines)

    for i, pm in enumerate(pkg_matches):
        pkg_start = pm.start()
        pkg_end = pkg_matches[i+1].start() if i+1 < len(pkg_matches) else len(text)
        pkg_name = pm.group(1)
        pkg_body = text[pkg_start + len(pm.group(0)):pkg_end]

        lines.append(f"## Пакет `{pkg_name}`")
        lines.append("")

        proc_matches = list(SQL_PROC_RE.finditer(pkg_body))
        if proc_matches:
            for j, pr in enumerate(proc_matches):
                pr_start = pr.start()
                pr_end = proc_matches[j+1].start() if j+1 < len(proc_matches) else len(pkg_body)
                if j == 0 and pr_start > 0:
                    preamble = pkg_body[:pr_start].strip()
                    if preamble:
                        lines.append(preamble)
                        lines.append("")
                proc_name = pr.group(1)
                proc_body = pkg_body[pr_start + len(pr.group(0)) - 1:pr_end]
                if is_toc_entry(proc_body):
                    continue
                lines.append(f"### `{proc_name}`")
                lines.append("")
                sig_lines = []
                idx = 0
                pb_lines = proc_body.splitlines()
                while idx < len(pb_lines):
                    l = pb_lines[idx].strip()
                    if not l:
                        idx += 1
                        continue
                    if l.startswith('Параметры:') or l.startswith('Возвращаемое значение:') or l.startswith('Примечание.') or l.startswith('Пример.'):
                        break
                    sig_lines.append(l)
                    idx += 1
                    if l.endswith(')'):
                        break
                if sig_lines:
                    sig = " ".join(sig_lines)
                    lines.append(f"```sql\n{sig}\n```")
                    lines.append("")
                rest = "\n".join(pb_lines[idx:]).strip()
                if rest:
                    split_pat = re.compile(r'^(Параметры:|Возвращаемое значение:|Примечание\.|Пример\.|Описание:)', re.MULTILINE)
                    parts = list(split_pat.finditer(rest))
                    if parts:
                        desc = rest[:parts[0].start()].strip()
                        if desc:
                            lines.append(desc)
                            lines.append("")
                        for k, p in enumerate(parts):
                            sec_name = p.group(1).rstrip('.').rstrip(':')
                            sec_start = p.start()
                            sec_end = parts[k+1].start() if k+1 < len(parts) else len(rest)
                            sec_body = rest[sec_start + len(p.group(1)):sec_end].strip()
                            lines.append(f"**{sec_name}:**")
                            lines.append("")
                            lines.append(convert_bullets(sec_body))
                            lines.append("")
                    else:
                        lines.append(convert_bullets(rest))
                        lines.append("")
            tail = pkg_body[proc_matches[-1].end():].strip()
            if tail and not is_toc_entry(tail):
                const_matches = list(SQL_CONST_RE.finditer(tail))
                if const_matches:
                    lines.append("### Константы")
                    lines.append("")
                    for cm in const_matches:
                        const_name = cm.group(1)
                        const_desc = tail[cm.end():].split('\n', 1)[0].strip()
                        lines.append(f"- `{const_name}` — {const_desc}")
                    lines.append("")
        else:
            pkg_body_clean = normalize_whitespace(pkg_body)
            lines.append(pkg_body_clean.strip())
            lines.append("")
    return "\n".join(lines)


# ── Стратегия DLM / RSL_Forms (Классы / Интерфейсы) ─────────────────────────
CLASS_SPLIT_RE = re.compile(r'^(Класс|Интерфейс)\s+([A-Za-z0-9_]+)', re.MULTILINE)

def process_classes(text: str, title: str) -> str:
    text = remove_toc_lines(text)
    text = strip_toc(text)
    matches = list(CLASS_SPLIT_RE.finditer(text))
    if not matches:
        return f"# {title}\n\n{normalize_whitespace(text.strip())}"
    meta = text[:matches[0].start()].strip()
    lines = [f"# {title}", ""]
    if meta:
        lines.append(normalize_whitespace(meta))
        lines.append("")
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        kind = m.group(1)
        name = m.group(2)
        body = text[start + len(m.group(0)):end].strip()
        if is_toc_entry(body):
            continue
        lines.append(f"## {kind}: `{name}`")
        lines.append("")
        sig_lines = []
        idx = 0
        bl = body.splitlines()
        while idx < len(bl):
            l = bl[idx].strip()
            if not l:
                idx += 1
                continue
            if l.startswith('Свойства:') or l.startswith('Методы:') or l.startswith('Примечание.'):
                break
            sig_lines.append(l)
            idx += 1
            if l.endswith(')'):
                break
        if sig_lines:
            lines.append(f"```rsl\n{' '.join(sig_lines)}\n```")
            lines.append("")
        rest = "\n".join(bl[idx:]).strip()
        if rest:
            lines.append(convert_bullets(rest))
            lines.append("")
    return "\n".join(lines)


# ── Стратегия Instruction (plain text) ──────────────────────────────────────
INSTRUCTION_SPLIT_RE = re.compile(
    r'^(Введение|Общие положения|Настройка|Описание|Технологическая модель|Виды событий|Элементы программирования|'
    r'Команды инструмента|Пример скрипта|Импорт скриптов|Синхронизация|Работа с|Приложение|'
    r'Создание ресурса|Параметры ресурса|Меню редактора ресурсов|Lib|Panel|New|Item|'
    r'Разработка печатных форм|Организация создания|Шаблон|Файл данных|Правила заполнения|'
    r'Вставка изображений|Печать в текстовые поля|Удаление таблицы|Обрамление таблицы|Высота строк|'
    r'Отчеты|Управляющий файл|Тестирование|Состав каталога|Управление трассировкой|'
    r'Трассировка операций|Трассировка изменения|Трассировка возникновения|Трассировка выполнения|'
    r'Элементы языка|Служебные слова|Имена|Область видимости|Комментарии|Объекты языка|'
    r'Типы данных|Переменные|Символические константы|Скалярные типы|Объектные типы|Константы|'
    r'Выражения|Синтаксис|Семантика|Структура RSL-программы|Загрузка и кэширование|Директива IMPORT|'
    r'Конструкции языка RSL|Пустая инструкция|Инструкция "выражение"|Условная инструкция IF|'
    r'Инструкция цикла WHILE|Оператор|Функция|Процедура|Класс)\b',
    re.MULTILINE | re.IGNORECASE
)

def process_instruction(text: str, title: str) -> str:
    text = remove_toc_lines(text)
    text = strip_toc(text)
    matches = list(INSTRUCTION_SPLIT_RE.finditer(text))
    if len(matches) < 2:
        return f"# {title}\n\n{normalize_whitespace(text.strip())}"
    lines = [f"# {title}", ""]
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        header = m.group(1).strip()
        body = text[start + len(m.group(0)):end].strip()
        if is_toc_entry(body):
            continue
        lines.append(f"## {header}")
        lines.append("")
        lines.append(convert_bullets(body))
        lines.append("")
    return "\n".join(lines)


# ── Главный диспетчер ──────────────────────────────────────────────────────
def classify(name: str) -> str:
    lname = name.lower()
    if lname.endswith('_rslprc.pdf'):
        return 'rslprc'
    if lname.endswith('_sql.pdf'):
        return 'sql'
    if lname == 'dlm.pdf':
        return 'dlm'
    if lname == 'rsl_forms.pdf':
        return 'rsl_forms'
    if lname == 'bnrsl.pdf':
        return 'instruction'  # BnRSL — это руководство по языку, разбиваем по разделам
    if lname == 'jasperreports.pdf':
        return 'instruction'
    if lname in ('atm.pdf', 'rce32.pdf', 'trace.pdf', 'reporttools.pdf', 'usercryptplugin.pdf', 'dbexp.pdf', 'reports_instrexp.pdf', 'retail_instrument.pdf'):
        return 'instruction'
    return 'instruction'


def process_file(path: str):
    name = os.path.basename(path)
    title = name.replace('.pdf', '').replace('_', ' ')
    print(f"Обработка: {name}")
    raw = extract_raw(path)
    doc_type = classify(name)

    if doc_type == 'rslprc':
        md = process_rslprc(raw, title)
    elif doc_type == 'sql':
        md = process_sql(raw, title)
    elif doc_type in ('dlm', 'rsl_forms'):
        md = process_classes(raw, title)
    else:
        md = process_instruction(raw, title)

    out_path = os.path.join(OUT_DIR, name.replace('.pdf', '.md'))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"  ✅ {out_path}")


def main():
    files = sorted([f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')])
    print(f"Всего PDF: {len(files)}")
    for f in files:
        process_file(os.path.join(PDF_DIR, f))
    print("Готово!")


if __name__ == '__main__':
    main()
