import re

def merge_duplicate_sections(filepath):
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
    
    # Записываем результат
    new_lines = []
    for heading in order:
        new_lines.append(heading + '\n')
        new_lines.extend(merged[heading])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Merged duplicates in {filepath}: {len(sections)} -> {len(order)} sections')
    return len(order)

def split_large_sections(filepath, max_size=500):
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
    
    new_lines = []
    for heading, body in sections:
        if len(body) <= max_size:
            new_lines.append(heading + '\n')
            new_lines.extend(body)
            continue
        
        # Пытаемся разбить на подсекции
        # Для классов: ищем методы (строки с Name( или Name ()
        subsections = []
        current_subheading = None
        current_subbody = []
        
        for line in body:
            # Проверяем, является ли строка подзаголовком метода
            # Паттерны: MethodName (, MethodName(), PropertyName, и т.д.
            stripped = line.strip()
            if re.match(r'^[A-Za-zА-Яа-я][A-Za-zА-Яа-я0-9_]*\s*\(', stripped) and not stripped.startswith('//'):
                # Возможно, это начало метода
                if current_subheading is not None and len(current_subbody) > 0:
                    subsections.append((current_subheading, current_subbody))
                current_subheading = stripped.split('(')[0].strip()
                current_subbody = [line]
            elif stripped.endswith('()') and re.match(r'^[A-Za-zА-Яа-я][A-Za-zА-Яа-я0-9_]*\(\)$', stripped):
                if current_subheading is not None and len(current_subbody) > 0:
                    subsections.append((current_subheading, current_subbody))
                current_subheading = stripped[:-2]
                current_subbody = [line]
            else:
                current_subbody.append(line)
        
        if current_subheading is not None:
            subsections.append((current_subheading, current_subbody))
        
        if len(subsections) > 1:
            # Записываем оригинальный заголовок
            new_lines.append(heading + '\n')
            for subheading, subbody in subsections:
                new_lines.append(f'### {subheading}\n')
                new_lines.extend(subbody)
        else:
            # Не удалось разбить, оставляем как есть
            new_lines.append(heading + '\n')
            new_lines.extend(body)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split large sections in {filepath}')

if __name__ == '__main__':
    merge_duplicate_sections('/Users/lipanovav/rag/knowledge/BnRSL.md')
    split_large_sections('/Users/lipanovav/rag/knowledge/BnRSL.md')
