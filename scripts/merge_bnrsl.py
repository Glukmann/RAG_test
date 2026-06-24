import re
from collections import Counter

def merge_bnrsl_duplicates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Разбиваем на секции
    sections = []
    current_heading = None
    current_body = []
    
    for line in lines:
        if line.startswith('## '):
            if current_heading is not None:
                sections.append((current_heading, current_body))
            current_heading = line.strip()
            current_body = []
        else:
            current_body.append(line)
    if current_heading is not None:
        sections.append((current_heading, current_body))
    
    # Объединяем дубли
    merged = {}
    order = []
    for heading, body in sections:
        if heading not in merged:
            merged[heading] = []
            order.append(heading)
        merged[heading].extend(body)
    
    # Записываем
    new_lines = []
    for heading in order:
        new_lines.append(heading + '\n')
        new_lines.extend(merged[heading])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Merged {len(sections)} -> {len(order)} sections')
    return len(order)

if __name__ == '__main__':
    merge_bnrsl_duplicates('/Users/lipanovav/rag/knowledge/BnRSL.md')
