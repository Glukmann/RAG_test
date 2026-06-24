#!/usr/bin/env python3
"""Удаление дублирующихся секций в DLM.md — объединение тела в одну секцию."""

IN_PATH = "/Users/lipanovav/rag/knowledge/DLM.md"
OUT_PATH = "/Users/lipanovav/rag/knowledge/DLM.md"

def main():
    with open(IN_PATH, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')

    # Разбиваем на секции
    sections = []
    current_heading = None
    current_body = []

    for line in lines:
        if line.startswith('## '):
            if current_heading is not None:
                sections.append((current_heading, current_body))
            current_heading = line
            current_body = []
        else:
            current_body.append(line)

    if current_heading is not None:
        sections.append((current_heading, current_body))

    # Объединяем дубли
    merged = {}
    for heading, body in sections:
        if heading not in merged:
            merged[heading] = []
        merged[heading].extend(body)

    # Перестраиваем файл
    out_lines = []
    # Мета-информация до первой ##
    if lines and not lines[0].startswith('## ') and not lines[0].startswith('# '):
        # Это не должно случиться, но на всякий случай
        pass

    # Находим # заголовок документа (если есть)
    doc_title = lines[0] if lines and lines[0].startswith('# ') else '# DLM'
    out_lines.append(doc_title)
    out_lines.append('')

    for heading, body in merged.items():
        out_lines.append(heading)
        out_lines.append('')
        # Удаляем дублирующиеся пустые строки в начале тела
        while body and body[0] == '':
            body.pop(0)
        # Удаляем дублирующиеся пустые строки в конце
        while body and body[-1] == '':
            body.pop()
        out_lines.extend(body)
        out_lines.append('')

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')

    print(f"Секций до: {len(sections)}")
    print(f"Секций после: {len(merged)}")
    print(f"Удалено дублей: {len(sections) - len(merged)}")

if __name__ == '__main__':
    main()
