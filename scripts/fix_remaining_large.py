import re

def fix_reports_app(filepath):
    """Исправляет ложные ## приложение в Reports_InstrExp.md"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == '## приложение':
            # Убираем ##, оставляем просто текст
            new_lines.append('приложение\n')
            i += 1
            # Если следующая строка начинается с запятой или пробела, это продолжение
            if i < len(lines) and (lines[i].lstrip().startswith(',') or lines[i].lstrip().startswith('.')):
                # Объединяем с предыдущей строкой
                combined = new_lines[-1].rstrip() + ' ' + lines[i].lstrip()
                new_lines[-1] = combined
                i += 1
        else:
            new_lines.append(line)
            i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Fixed {filepath}')

def split_large_sections(filepath, max_size=500):
    """Разбивает крупные секции на подсекции по ### или по размеру."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith('## '):
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
        if size <= max_size:
            new_lines.extend(lines[start:end])
            i = end
            continue
        
        body = lines[start+1:end]
        
        # Ищем ### подсекции
        has_triples = any(l.startswith('### ') for l in body)
        
        if has_triples:
            # Превращаем ### в ##
            new_lines.append(heading)
            for bline in body:
                if bline.startswith('### '):
                    new_lines.append(f'## {heading.strip()[3:]} — {bline.strip()[4:]}\n')
                else:
                    new_lines.append(bline)
        else:
            # Разбиваем на части по ~300 строк
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
    
    print(f'Split large sections in {filepath}')

if __name__ == '__main__':
    fix_reports_app('/Users/lipanovav/rag/knowledge/Reports_InstrExp.md')
    split_large_sections('/Users/lipanovav/rag/knowledge/Reports_InstrExp.md')
    split_large_sections('/Users/lipanovav/rag/knowledge/Core_RSLprc_3.md')
    split_large_sections('/Users/lipanovav/rag/knowledge/RSL_13_classes_objects.md')
