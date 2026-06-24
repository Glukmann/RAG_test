import re

def split_large_sections_by_patterns(filepath, max_size=500):
    """
    Разбивает крупные секции (> max_size) по внутренним логическим разделителям.
    """
    # Паттерны для разделителей подсекций
    SPLIT_PATTERNS = [
        r'^Класс\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Процедура\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Функция\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Метод\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Свойство\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Конструктор\s+[A-ZА-Я][A-Za-zА-Яа-я0-9_]*\s*$',
        r'^Меню\s*$',
        r'^Вертикальное меню\s*$',
        r'^Горизонтальное меню\s*$',
        r'^Диалоговые окна\s*$',
        r'^Скроллинг\s*$',
        r'^Поддержка интерактивного режима\s*$',
        r'^Процедура обработки сообщений\s*$',
        r'^Свойства класса\s+[A-Za-z0-9_]+\s*$',
        r'^Методы класса\s+[A-Za-z0-9_]+\s*$',
        r'^Свойства объекта\s+[A-Za-z0-9_]+\s*$',
        r'^Методы объекта\s+[A-Za-z0-9_]+\s*$',
        r'^Организация ввода/вывода\s*$',
        r'^Использование стандартного класса\s*$',
        r'^Список обрабатываемых сообщений\s*$',
    ]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('## '):
            # Найти конец секции
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
                # Секция не крупная, оставляем как есть
                new_lines.extend(lines[start:end])
                i = end
                continue
            
            # Крупная секция, ищем разделители
            body = lines[start+1:end]
            split_indices = []
            for idx, body_line in enumerate(body):
                stripped = body_line.strip()
                for pattern in SPLIT_PATTERNS:
                    if re.match(pattern, stripped):
                        split_indices.append((idx, stripped))
                        break
            
            if len(split_indices) >= 3:
                # Есть разделители, разбиваем на подсекции
                new_lines.append(heading)
                last_idx = 0
                for split_pos, split_title in split_indices:
                    if split_pos > last_idx:
                        # Добавляем содержимое до разделителя
                        new_lines.extend(body[last_idx:split_pos])
                    # Добавляем разделитель как ###
                    new_lines.append(f'### {split_title}\n')
                    new_lines.append('\n')
                    last_idx = split_pos + 1
                
                # Добавляем остаток
                if last_idx < len(body):
                    new_lines.extend(body[last_idx:])
            else:
                # Разделителей мало, разбиваем на части по ~300 строк
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
        else:
            new_lines.append(line)
            i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Split large sections in {filepath}')

if __name__ == '__main__':
    split_large_sections_by_patterns('/Users/lipanovav/rag/knowledge/BnRSL.md')
