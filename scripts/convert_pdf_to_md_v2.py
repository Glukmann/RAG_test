#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF → Markdown конвертер для RSL документации (v2).
Оптимизирован для RAG: удаление оглавления, точные границы чанков,
структурирование по процедурам/функциям/классам/пакетам.
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
TOC_DOTS_RE = re.compile(r'\.{3,}.*\d+\s*$', re.MULTILINE)

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


# ── Удаление оглавления ─────────────────────────────────────────────────────
# Оглавление обычно идёт до раздела "Введение" или до первого реального заголовка
TOC_STOP_PATTERNS = [
    re.compile(r'^\s*Введение\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*ПРЕДИСЛОВИЕ\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Introduction\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Особенности\s+реализации\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Технологическая\s+модель\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Общие\s+положения\b', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*Работа\s+с\s+DLM\b', re.MULTILINE | re.IGNORECASE),
]

def strip_toc(text: str) -> str:
    """Обрезает текст до первого значимого раздела (после оглавления)."""
    best_pos = -1
    for pat in TOC_STOP_PATTERNS:
        m = pat.search(text)
        if m:
            pos = m.start()
            if best_pos == -1 or pos < best_pos:
                best_pos = pos
    if best_pos != -1 and best_pos < len(text) * 0.35:
        return text[best_pos:]
    # fallback: если первые 20% текста состоят из строк с точками — это оглавление
    lines = text.splitlines()
    toc_lines = 0
    for i, line in enumerate(lines):
        if TOC_DOTS_RE.search(line):
            toc_lines = i
    if toc_lines > 0 and toc_lines < len(lines) * 0.4:
        return "\n".join(lines[toc_lines:])
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
    """Если тело секции состоит только из точек и номера страницы — это оглавление."""
    cleaned = re.sub(r'\s+', '', body)
    return bool(re.fullmatch(r'[\.\d]+', cleaned))


# ── Стратегия RSLprc ───────────────────────────────────────────────────────
RSLPROC_SPLIT_RE = re.compile(r'^(Процедура|Функция|Класс|Метод)\s+([A-Za-zА-Яа-я0-9_]+)', re.MULTILINE)

def process_rslprc(text: str, title: str) -> str:
    text = strip_toc(text)
    matches = list(RSLPROC_SPLIT_RE.finditer(text))
    if not matches:
        return f"# {title}\n\n{text.strip()}"

    meta = text[:matches[0].start()].strip()
    lines = [f"# {title}", ""]
    if meta:
        meta = re.sub(r'\n{3,}', '\n\n', meta)
        lines.append(meta)
        lines.append("")

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        kind = m.group(1)
        name = m.group(2)
        body = text[start + len(m.group(0)):end].strip()

        if is_toc_entry(body):
            continue
        # для Процедура/Функция/Метод проверяем, что в начале есть сигнатура со скобкой
        if kind in ('Процедура', 'Функция', 'Метод') and not looks_like_signature(body[:300]):
            continue

        lines.append(f"## {kind}: `{name}`")
        lines.append("")
        # выделение сигнатуры
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
            # Разбиваем по ключевым разделам
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
    text = strip_toc(text)
    lines = [f"# {title}", ""]
    # Ищем пакеты
    pkg_matches = list(SQL_PACKAGE_RE.finditer(text))
    if not pkg_matches:
        # fallback: просто текст
        lines.append(text.strip())
        return "\n".join(lines)

    for i, pm in enumerate(pkg_matches):
        pkg_start = pm.start()
        pkg_end = pkg_matches[i+1].start() if i+1 < len(pkg_matches) else len(text)
        pkg_name = pm.group(1)
        pkg_body = text[pkg_start + len(pm.group(0)):pkg_end]

        lines.append(f"## Пакет `{pkg_name}`")
        lines.append("")

        # Ищем процедуры/функции внутри пакета
        proc_matches = list(SQL_PROC_RE.finditer(pkg_body))
        if proc_matches:
            prev = 0
            for j, pr in enumerate(proc_matches):
                pr_start = pr.start()
                pr_end = proc_matches[j+1].start() if j+1 < len(proc_matches) else len(pkg_body)
                # текст до первой процедуры — описание пакета/константы
                if j == 0 and pr_start > 0:
                    preamble = pkg_body[prev:pr_start].strip()
                    if preamble:
                        lines.append(preamble)
                        lines.append("")
                proc_name = pr.group(1)
                proc_body = pkg_body[pr_start + len(pr.group(0)) - 1:pr_end]  # включаем (
                # убираем оглавление из тела
                if is_toc_entry(proc_body):
                    continue
                lines.append(f"### `{proc_name}`")
                lines.append("")
                # выделяем сигнатуру
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
            # Константы после процедур (если есть)
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
            # нет процедур — просто текст пакета
            pkg_body_clean = re.sub(r'\n{3,}', '\n\n', pkg_body)
            lines.append(pkg_body_clean.strip())
            lines.append("")
    return "\n".join(lines)


# ── Стратегия DLM / RSL_Forms (Классы / Интерфейсы) ─────────────────────────
CLASS_SPLIT_RE = re.compile(r'^(Класс|Интерфейс)\s+([A-Za-z0-9_]+)', re.MULTILINE)

def process_classes(text: str, title: str) -> str:
    text = strip_toc(text)
    matches = list(CLASS_SPLIT_RE.finditer(text))
    if not matches:
        return f"# {title}\n\n{text.strip()}"
    meta = text[:matches[0].start()].strip()
    lines = [f"# {title}", ""]
    if meta:
        meta = re.sub(r'\n{3,}', '\n\n', meta)
        lines.append(meta)
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
        # сигнатура (если есть)
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
            sig = " ".join(sig_lines)
            lines.append(f"```rsl\n{sig}\n```")
            lines.append("")
        rest = "\n".join(bl[idx:]).strip()
        if rest:
            lines.append(convert_bullets(rest))
            lines.append("")
    return "\n".join(lines)


# ── Стратегия Instruction (plain text) ──────────────────────────────────────
INSTRUCTION_SPLIT_RE = re.compile(r'^(Введение|Общие положения|Настройка|Описание|Технологическая модель|Виды событий|Элементы программирования|Команды инструмента|Пример скрипта|Импорт скриптов|Синхронизация|Работа с|Приложение|Создание ресурса|Параметры ресурса|Меню редактора ресурсов|Lib|Panel|New|Item|Разработка печатных форм|Организация создания|Шаблон|Файл данных|Правила заполнения|Вставка изображений|Печать в текстовые поля|Удаление таблицы|Обрамление таблицы|Высота строк|Отчеты|Управляющий файл|Тестирование|Состав каталога|Управление трассировкой|Трассировка операций|Трассировка изменения|Трассировка возникновения|Трассировка выполнения)\b', re.MULTILINE | re.IGNORECASE)

def process_instruction(text: str, title: str) -> str:
    text = strip_toc(text)
    matches = list(INSTRUCTION_SPLIT_RE.finditer(text))
    if len(matches) < 2:
        return f"# {title}\n\n{text.strip()}"
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
    if lname in ('atm.pdf', 'rce32.pdf', 'trace.pdf', 'reporttools.pdf', 'usercryptplugin.pdf', 'dbexp.pdf', 'reports_instrexp.pdf', 'retail_instrument.pdf'):
        return 'instruction'
    if lname == 'bnrsl.pdf':
        return 'rslprc'  # BnRSL — это руководство по RSL, похоже на rslprc
    if lname == 'jasperreports.pdf':
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
