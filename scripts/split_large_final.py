import re

def split_large_sections_final(filepath, max_size=500):
    """
    Для крупных секций (> max_size) превращает внутренние ### подсекции в ## секции.
    Убирает артефактные ### (например, 'Организация ввода/вывода').
    """
    ARTIFACTS = {'Организация ввода/вывода', 'Организация ввода\\/вывода'}
    
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
        
        # Крупная секция, ищем ### подсекции
        body = lines[start+1:end]
        subsections = []
        current_subheading = None
        current_subbody = []
        
        for bline in body:
            if bline.startswith('### '):
                sub_title = bline.strip()[4:]
                if sub_title not in ARTIFACTS:
                    if current_subheading is not None:
                        subsections.append((current_subheading, current_subbody))
                    current_subheading = sub_title
                    current_subbody = []
                else:
                    # Артефакт, пропускаем заголовок
                    if current_subheading is not None:
                        current_subbody.append(bline)
            else:
                if current_subheading is not None:
                    current_subbody.append(bline)
        
        if current_subheading is not None:
            subsections.append((current_subheading, current_subbody))
        
        if len(subsections) >= 2:
            # Превращаем ### в ##
            # Текст до первого ### добавляем как отдельную секцию
            first_sub_pos = None
            for idx, bline in enumerate(body):
                if bline.startswith('### ') and bline.strip()[4:] not in ARTIFACTS:
                    first_sub_pos = idx
                    break
            
            if first_sub_pos and first_sub_pos > 0:
                # Создаём секцию с оригинальным заголовком + "(основное)"
                new_lines.append(heading)
                new_lines.extend(body[:first_sub_pos])
            
            for sub_title, sub_body in subsections:
                # Формируем новый заголовок
                if sub_title.startswith('Класс ') or sub_title.startswith('Процедура ') or sub_title.startswith('Функция ') or sub_title.startswith('Метод '):
                    new_heading = f'## {sub_title}\n'
                else:
                    # Наследуем контекст из оригинального заголовка
                    orig = heading.strip()[3:].strip()
                    new_heading = f'## {orig} — {sub_title}\n'
                new_lines.append(new_heading)
                new_lines.extend(sub_body)
        else:
            # Не удалось разбить, разбиваем на части
            new_lines.append(heading)
            part_size = 300
            num_parts = (len(body) + part_size - 1) // part_size
            for p in range(num_parts):
                p_start = p * part_size
                p_end = min((p + 1) * part_size, len(body))
                if num_parts > 1:
                    new_lines.append(f'### Часть {p+1}\n\n')
                new_lines.extend(body[p_start:p_end])
        
        i = end
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split large sections in {filepath}')

if __name__ == '__main__':
    split_large_sections_final('/Users/lipanovav/rag/knowledge/BnRSL.md')
