import os
from collections import Counter

def merge_all_duplicates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Разбиваем на секции
    sections = []
    current_heading = None
    current_body = []
    
    for line in lines:
        if line.startswith('##'):
            if current_heading is not None:
                sections.append((current_heading, current_body))
            current_heading = line
            current_body = []
        else:
            current_body.append(line)
    if current_heading is not None:
        sections.append((current_heading, current_body))
    
    # Проверяем, есть ли дубли
    headings = [h for h, b in sections]
    counts = Counter(headings)
    dupes = {h: c for h, c in counts.items() if c > 1}
    
    if not dupes:
        return 0
    
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
        new_lines.append(heading)
        new_lines.extend(merged[heading])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    return len(dupes)

if __name__ == '__main__':
    total_dupes = 0
    for fname in os.listdir('/Users/lipanovav/rag/knowledge'):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        fpath = os.path.join('/Users/lipanovav/rag/knowledge', fname)
        dupes = merge_all_duplicates(fpath)
        if dupes > 0:
            print(f'Merged {dupes} duplicates in {fname}')
            total_dupes += dupes
    
    print(f'Total duplicates merged: {total_dupes}')
