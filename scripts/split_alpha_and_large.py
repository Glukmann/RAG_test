import re
import os

def split_alpha_index(filepath):
    """Разбивает Алфавитный указатель на секции по буквам."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() == '## Алфавитный указатель':
            new_lines.append(line)
            i += 1
            continue
        
        heading = line
        start = i
        for j in range(i+1, len(lines)):
            if lines[j].startswith('##'):
                end = j
                break
        else:
            end = len(lines)
        
        body = lines[start+1:end]
        
        # Ищем разделители по буквам: '- A -', '- B -' и т.д.
        split_indices = []
        for idx, bline in enumerate(body):
            if re.match(r'^\s*-\s+[A-ZА-Я]\s+-\s*$', bline):
                split_indices.append((idx, bline.strip()))
        
        if len(split_indices) >= 2:
            new_lines.append(heading)
            last_idx = 0
            for split_pos, split_title in split_indices:
                if split_pos > last_idx:
                    new_lines.extend(body[last_idx:split_pos])
                new_lines.append(f'## Алфавитный указатель — {split_title}\n')
                last_idx = split_pos + 1
            
            if last_idx < len(body):
                new_lines.extend(body[last_idx:])
        else:
            # Не удалось разбить по буквам, разбиваем по ~300 строк
            new_lines.append(heading)
            part_size = 300
            num_parts = (len(body) + part_size - 1) // part_size
            for p in range(num_parts):
                p_start = p * part_size
                p_end = min((p + 1) * part_size, len(body))
                if num_parts > 1:
                    new_lines.append(f'## Алфавитный указатель — Часть {p+1}\n')
                new_lines.extend(body[p_start:p_end])
        
        i = end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split alphabetical index in {filepath}')

def split_large_sql_sections_by_size(filepath, max_size=500):
    """Разбивает оставшиеся крупные SQL-секции на части по ~300 строк."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith('##'):
            new_lines.append(line)
            i += 1
            continue
        
        heading = line
        start = i
        for j in range(i+1, len(lines)):
            if lines[j].startswith('##'):
                end = j
                break
        else:
            end = len(lines)
        
        size = end - start
        if size <= max_size:
            new_lines.extend(lines[start:end])
            i = end
            continue
        
        # Крупная секция, разбиваем на части
        body = lines[start+1:end]
        part_size = 300
        num_parts = (len(body) + part_size - 1) // part_size
        
        for p in range(num_parts):
            p_start = p * part_size
            p_end = min((p + 1) * part_size, len(body))
            if num_parts > 1:
                new_lines.append(f'{heading.rstrip()} (часть {p+1})\n')
            else:
                new_lines.append(heading)
            new_lines.extend(body[p_start:p_end])
            new_lines.append('\n')
        
        i = end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split large SQL sections by size in {filepath}')

if __name__ == '__main__':
    for fname in os.listdir('/Users/lipanovav/rag/knowledge'):
        if fname.endswith('_SQL.md'):
            fpath = os.path.join('/Users/lipanovav/rag/knowledge', fname)
            split_alpha_index(fpath)
            split_large_sql_sections_by_size(fpath)
