#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF → Markdown конвертер для RSL документации.
Оптимизирован для RAG (чёткие заголовки, чанки по процедурам/функциям).
"""

import os
import re
import fitz  # PyMuPDF

# Пути
PDF_DIR = "/Users/lipanovav/rag/06_ToolsDoc"
OUT_DIR = "/Users/lipanovav/rag/knowledge"

os.makedirs(OUT_DIR, exist_ok=True)

# Регулярки для чистки
PAGE_HEADER_RE = re.compile(
    r'^\s*Модуль\s+\w+.*$',
    re.MULTILINE
)
COPYRIGHT_RE = re.compile(
    r'^\s*© АО Эр-Стайл Софтлаб,\s*\d+\s*–\s*\d+\s*$',
    re.MULTILINE
)
PAGE_NUMBER_RE = re.compile(
    r'^\s*\d+\s*$',
    re.MULTILINE
)
# Убираем оглавление с точками
TOC_DOTS_RE = re.compile(r'\.{3,}.*\d+\s*$', re.MULTILINE)


def clean_page(text: str) -> str:
    """Убирает шапку/низ страницы, номера страниц, копирайт."""
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Пропускаем номер страницы (одна цифра)
        if re.fullmatch(r'\d+', stripped):
            continue
        # Пропускаем копирайт
        if COPYRIGHT_RE.match(stripped):
            continue
        # Пропускаем строку модуля (если она короткая и не содержит описания)
        if PAGE_HEADER_RE.match(stripped):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_pdf_text(path: str) -> str:
    """Извлекает текст из PDF через PyMuPDF, склеивает страницы."""
    doc = fitz.open(path)
    parts = []
    for page in doc:
        text = page.get_text()
        if text:
            parts.append(clean_page(text))
    doc.close()
    return "\n".join(parts)


def split_procedures(text: str):
    """
    Разбивает текст на секции:
    - meta (всё до первой процедуры/функции)
    - список (заголовок, тело)
    """
    # Ищем "Процедура ИМЯ" или "Функция ИМЯ" в начале строки
    pattern = re.compile(r'^(Процедура|Функция)\s+(\w+)', re.MULTILINE)
    matches = list(pattern.finditer(text))
    if not matches:
        return text, []

    meta = text[:matches[0].start()].strip()
    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        header = m.group(0)  # "Процедура Name"
        body = text[start + len(header):end].strip()
        sections.append((header, body))
    return meta, sections


def format_signature(body: str) -> tuple:
    """
    Пытается выделить сигнатуру из первой строки тела.
    Возвращает (signature, остальное_тело).
    """
    lines = body.splitlines()
    if not lines:
        return "", body
    # Сигнатура обычно: Name (params):ReturnType
    first = lines[0].strip()
    # Если первая строка похожа на сигнатуру (содержит скобки и/или двоеточие)
    if ('(' in first and ')' in first) or ':' in first:
        # Иногда сигнатура разбита на несколько строк (переносы параметров)
        # Собираем до пустой строки или до "Параметры:"
        sig_lines = [first]
        idx = 1
        while idx < len(lines):
            line = lines[idx].strip()
            # Если встретили ключевой разделитель — останавливаемся
            if line.startswith('Параметры:') or line.startswith('Возвращаемое значение:') or line.startswith('Примечание.'):
                break
            # Если строка пустая и уже набрали что-то вменяемое — останавливаемся
            if not line and len(sig_lines) > 1:
                break
            # Если следующая строка похожа на продолжение сигнатуры (начинается с параметра)
            if line:
                sig_lines.append(line)
            idx += 1
        signature = " ".join(sig_lines).strip()
        rest = "\n".join(lines[idx:]).strip()
        return signature, rest
    return "", body


def format_body(body: str) -> str:
    """Форматирует тело процедуры в Markdown."""
    signature, rest = format_signature(body)
    md_parts = []
    if signature:
        md_parts.append(f"```rsl\n{signature}\n```\n")

    # Разбиваем остальное на блоки по ключевым словам
    # Ключевые разделы: Параметры:, Возвращаемое значение:, Пример., Примечание.
    split_pattern = re.compile(
        r'^(Параметры:|Возвращаемое значение:|Пример\.|Примечание\.|Описание:)',
        re.MULTILINE
    )
    # Но в наших данных обычно нет явного "Описание:" — описание идёт перед Параметрами
    # Поэтому ищем первый из разделов
    parts = list(split_pattern.finditer(rest))
    if parts:
        # Всё до первого раздела — описание
        desc = rest[:parts[0].start()].strip()
        if desc:
            md_parts.append(desc)
            md_parts.append("")
        for i, m in enumerate(parts):
            section_name = m.group(1).rstrip('.').rstrip(':')
            start = m.start()
            end = parts[i + 1].start() if i + 1 < len(parts) else len(rest)
            section_body = rest[start + len(m.group(1)):end].strip()
            md_parts.append(f"**{section_name}:**\n")
            # Если внутри есть буллеты (·) или цифры, преобразуем в Markdown-списки
            section_body = convert_bullets(section_body)
            md_parts.append(section_body)
            md_parts.append("")
    else:
        # Нет разделов — просто текст
        md_parts.append(rest)

    return "\n".join(md_parts).strip()


def convert_bullets(text: str) -> str:
    """Преобразует буллеты (·) и тире в Markdown-списки."""
    lines = text.splitlines()
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('·'):
            result.append('- ' + stripped[1:].strip())
        elif stripped.startswith('‐') or stripped.startswith('–') or stripped.startswith('-'):
            result.append('- ' + stripped[1:].strip())
        else:
            result.append(line)
    return "\n".join(result)


def to_markdown(pdf_name: str, meta: str, sections: list) -> str:
    """Формирует полный Markdown документ."""
    # H1 из имени файла или первых строк
    title = pdf_name.replace('.pdf', '').replace('_', ' ')
    lines = [f"# {title}", ""]
    if meta:
        # Очистим meta от оглавлений с точками
        meta_clean = TOC_DOTS_RE.sub('', meta)
        # Убираем множественные пустые строки
        meta_clean = re.sub(r'\n{3,}', '\n\n', meta_clean)
        if meta_clean.strip():
            lines.append(meta_clean.strip())
            lines.append("")

    for header, body in sections:
        # header = "Процедура Name" или "Функция Name"
        parts = header.split(None, 1)
        kind = parts[0]  # Процедура/Функция
        name = parts[1] if len(parts) > 1 else "Unknown"
        lines.append(f"## {kind}: `{name}`")
        lines.append("")
        lines.append(format_body(body))
        lines.append("")
    return "\n".join(lines)


def process_pdf(pdf_path: str, out_dir: str):
    """Обрабатывает один PDF файл."""
    name = os.path.basename(pdf_path)
    print(f"Обработка: {name}")
    raw_text = extract_pdf_text(pdf_path)
    meta, sections = split_procedures(raw_text)
    if not sections:
        print(f"  ⚠️  Процедуры/функции не найдены, сохраняю как plain text.")
        md = f"# {name.replace('.pdf', '')}\n\n{raw_text}"
    else:
        md = to_markdown(name, meta, sections)
    out_name = name.replace('.pdf', '.md')
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"  ✅ Сохранено: {out_path} ({len(sections)} секций)")


def main():
    pdf_files = sorted([f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')])
    print(f"Найдено PDF файлов: {len(pdf_files)}")
    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        process_pdf(pdf_path, OUT_DIR)
    print("Готово!")


if __name__ == '__main__':
    main()
