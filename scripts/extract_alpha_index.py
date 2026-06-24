import os

def extract_alphabetical_index(filepath):
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
        
        # Найти конец секции
        heading = line
        start = i
        for j in range(i+1, len(lines)):
            if lines[j].startswith('##'):
                end = j
                break
        else:
            end = len(lines)
        
        # Проверяем, есть ли 'Алфавитный указатель' внутри
        body = lines[start:end]
        idx_pos = None
        for k, bline in enumerate(body):
            if 'Алфавитный указатель' in bline:
                idx_pos = k
                break
        
        if idx_pos is not None and idx_pos < len(body) - 10:
            # Вынимаем алфавитный указатель
            new_lines.extend(body[:idx_pos])
            # Алфавитный указатель в отдельную секцию
            new_lines.append('## Алфавитный указатель\n')
            new_lines.extend(body[idx_pos:])
        else:
            new_lines.extend(body)
        
        i = end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Extracted alphabetical index from {filepath}')

if __name__ == '__main__':
    for fname in os.listdir('/Users/lipanovav/rag/knowledge'):
        if fname.endswith('_SQL.md'):
            extract_alphabetical_index(os.path.join('/Users/lipanovav/rag/knowledge', fname))
