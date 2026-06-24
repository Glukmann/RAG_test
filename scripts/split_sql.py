import re
import os

def split_sql_packages(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith('## Пакет '):
            new_lines.append(line)
            i += 1
            continue
        
        heading = line
        start = i
        for j in range(i+1, len(lines)):
            if lines[j].startswith('## '):
                end = j
                break
        else:
            end = len(lines)
        
        size = end - start
        if size <= 500:
            new_lines.extend(lines[start:end])
            i = end
            continue
        
        # Крупный пакет
        body = lines[start+1:end]
        
        # Ищем ### подсекции
        has_triples = any(l.startswith('### ') for l in body)
        
        if has_triples:
            # Превращаем ### в ##
            package_name = heading.strip().replace('## Пакет ', '')
            new_lines.append(heading)  # Оставляем заголовок пакета (краткий)
            new_lines.append('\n')
            
            for bline in body:
                if bline.startswith('### '):
                    sub_name = bline.strip()[4:]
                    new_lines.append(f'## {package_name} — {sub_name}\n')
                else:
                    new_lines.append(bline)
        else:
            # Нет ###, пытаемся разбить по "Процедура Name" или "Функция Name"
            # Ищем строки, которые начинаются с имени процедуры/функции, за которым следует описание
            split_pattern = re.compile(r'^(\w+)\s*\([^)]*\)')
            
            subsections = []
            current_heading = None
            current_body = []
            
            for idx, bline in enumerate(body):
                stripped = bline.strip()
                # Проверяем, является ли строка заголовком процедуры/функции
                if stripped and not stripped.startswith('·') and not stripped.startswith('-') and not stripped.startswith('Параметры') and not stripped.startswith('Возвращаемое'):
                    match = split_pattern.match(stripped)
                    if match and len(stripped) < 200 and '(' in stripped:
                        # Возможно, это заголовок
                        if current_heading is not None and len(current_body) > 0:
                            subsections.append((current_heading, current_body))
                        current_heading = stripped.split('(')[0].strip()
                        current_body = [bline]
                        continue
                
                if current_heading is not None:
                    current_body.append(bline)
            
            if current_heading is not None:
                subsections.append((current_heading, current_body))
            
            if len(subsections) >= 2:
                package_name = heading.strip().replace('## Пакет ', '')
                new_lines.append(heading)
                new_lines.append('\n')
                for sub_heading, sub_body in subsections:
                    new_lines.append(f'## {package_name} — {sub_heading}\n')
                    new_lines.extend(sub_body)
                    new_lines.append('\n')
            else:
                new_lines.extend(lines[start:end])
        
        i = end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split SQL packages in {filepath}')

if __name__ == '__main__':
    for fname in os.listdir('/Users/lipanovav/rag/knowledge'):
        if fname.endswith('_SQL.md'):
            split_sql_packages(os.path.join('/Users/lipanovav/rag/knowledge', fname))
