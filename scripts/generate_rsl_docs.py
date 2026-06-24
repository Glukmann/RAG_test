import re, os, sys

OUTPUT_DIR = '/Users/lipanovav/rag/knowledge'
RAW_FILE = '/tmp/rsl_raw.txt'

def main():
    with open(RAW_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pages = content.split('---PAGE BREAK---')
    
    # Section definitions: (key, title, start_page, end_page)
    sections = [
        ('01_intro', 'Введение', 5, 6),
        ('02_elements', 'Элементы языка', 6, 8),
        ('03_data_types', 'Типы данных', 8, 9),
        ('04_constants', 'Константы', 9, 10),
        ('05_expressions', 'Выражения', 10, 12),
        ('06_program_structure', 'Структура программы', 12, 15),
        ('07_constructions', 'Конструкции языка RSL', 15, 35),
        ('08_io', 'Организация ввода/вывода', 35, 36),
        ('09_reports', 'Формирование отчетов', 36, 37),
        ('10_interactive', 'Интерактивный режим', 37, 45),
        ('11_files', 'Работа с файлами', 45, 56),
        ('12_builtins', 'Встроенные процедуры', 56, 76),
        ('13_classes_objects', 'Классы и объекты', 76, 87),
        ('14_dlm', 'DLM SDK', 87, 89),
        ('15_syntax', 'Сводка синтаксиса', 89, 93),
        ('20_ide', 'Интегрированная среда разработки', 93, 121),
        ('30_debugger', 'Отладчик макропрограмм', 121, 132),
        ('31_index', 'Алфавитный указатель', 132, len(pages)),
    ]
    
    for key, title, start, end in sections:
        section_pages = pages[start:end]
        md_text = process_section(title, section_pages, start)
        
        filename = f'RSL_{key}.md'
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_text)
        
        lines = md_text.count('\n')
        print(f'Created {filename} ({lines} lines, {len(md_text)} chars)')

def process_section(title, pages, start_page):
    """Convert pages to clean Markdown"""
    lines = []
    
    # Header
    lines.append(f'# {title}')
    lines.append('')
    lines.append('> RSL (R-Style Language) — Руководство программиста')
    lines.append('> Copyright © 1993-2001 R-Style Softlab')
    lines.append('')
    lines.append('---')
    lines.append('')
    
    for i, page in enumerate(pages):
        page_lines = page.strip().split('\n')
        
        for line in page_lines:
            stripped = line.strip()
            
            # Skip page numbers
            if stripped.isdigit() and len(stripped) <= 3:
                continue
            
            # Skip repeated page headers
            if stripped == 'Язык интерпретатора RSL':
                continue
            if stripped == 'Интегрированная среда разработки':
                continue
            if stripped == 'программ на языке RSL':
                continue
            if stripped == 'Отладчик макропрограмм':
                continue
            
            # Skip copyright
            if 'Copyright' in stripped or '©' in stripped:
                continue
            if 'R-Style Softlab' == stripped:
                continue
            if 'Все права защищены' in stripped:
                continue
            
            # Skip TOC references (lines with dots and page numbers)
            if re.match(r'^[\w\s]+\s+\.\.+\s+\d+$', stripped):
                continue
            
            # Detect section headers (all caps or title case, short)
            # Convert to markdown headers
            if is_section_header(stripped):
                level = get_header_level(stripped)
                prefix = '#' * level
                lines.append(f'{prefix} {stripped}')
                lines.append('')
                continue
            
            # Detect code examples (indented or special markers)
            if is_code_example(stripped):
                lines.append('```rsl')
                lines.append(line)
                lines.append('```')
                lines.append('')
                continue
            
            # Regular text
            lines.append(line)
    
    # Clean up consecutive empty lines
    result = '\n'.join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result

def is_section_header(text):
    """Detect if text is a section header"""
    if not text or len(text) > 80:
        return False
    
    # Known section headers
    headers = [
        'Введение', 'Элементы языка', 'Служебные слова', 'Имена',
        'Область видимости', 'Комментарии', 'Объекты языка',
        'Типы данных', 'Константы', 'Выражения', 'Синтаксис', 'Семантика',
        'Структура программы', 'Загрузка и кэширование',
        'Конструкции языка RSL', 'Пустая инструкция',
        'Инструкция', 'Условная инструкция', 'Инструкция цикла',
        'Инструкция возврата', 'Инструкция вывода',
        'Определение переменных', 'Определение классов',
        'Определение символических констант',
        'Определение процедуры', 'Процедуры языка RSL',
        'Передача параметров', 'Определение массивов',
        'Стандартный класс', 'Определения FILE',
        'Поддержка технологии ActiveX', 'Поддержка стандартных коллекций',
        'Обращение к свойствам', 'Доступ к объектам',
        'Обработка событий', 'Методы и свойства класса',
        'Обработка ошибок', 'Автоматическое создание',
        'Конструкция WITH', 'Организация ввода/вывода',
        'Спецификаторы форматирования', 'Формирование отчетов',
        'Поддержка интерактивного режима', 'Меню',
        'Вертикальное меню', 'Горизонтальное меню',
        'Диалоговые окна', 'Скроллинг', 'Работа с файлами',
        'Использование стандартного класса',
        'Методы и свойства класса',
        'Работа с Btrieve', 'Первый способ', 'Второй способ',
        'Обработка транзакций', 'Работа с текстовыми',
        'Работа с файлами в формате DBF',
        'Управление файлами', 'Встроенные процедуры',
        'Стандартные процедуры ввода', 'Стандартные процедуры вывода',
        'Типы и значения', 'Работа со строками',
        'Параметры процедур', 'Математические процедуры',
        'Внешние программы', 'Удаленный запуск',
        'Файлы и структуры', 'Классы и объекты',
        'Обработка меню', 'Обработка диалоговых окон',
        'Обработка скроллинга', 'Переменные',
        'Макропроцедуры', 'Другие процедуры',
        'Средство разработки расширений',
        'Создание и использование', 'Передача параметров и возврат',
        'Сводка синтаксиса', 'Интегрированная среда',
        'Словарь', 'Открытие', 'Создание', 'Закрытие',
        'Тестирование', 'Конвертирование', 'Директории',
        'Файлы', 'Структуры', 'Список полей',
        'Отчет о структуре', 'Список ключей',
        'Установка владельца', 'Снятие владельца',
        'Заимствование структур', 'Данные', 'Просмотр',
        'Содержимое полей', 'Выбор ключа',
        'Поиск записи', 'Редактирование', 'Изображение',
        'Экспорт', 'Импорт', 'Конвертирование',
        'Процедуры', 'Список макропроцедур',
        'Ввод новой', 'Описание RSL-программы',
        'Отладка макрофайла', 'Работа со встроенным',
        'Трансляция макрофайла', 'Режимы печати',
        'Редактирование ресурсов', 'Диалог',
        'Загрузить', 'Редактирование диалогов',
        'Сохранить', 'Сохранить как', 'Новый', 'Удалить',
        'Тестировать', 'Показать имена', 'Контрастный цвет',
        'Добавить', 'Рамка', 'Текст', 'Поле', 'Передвинуть',
        'Свойства', 'Меню', 'Редактирование меню',
        'Новое', 'Отладчик', 'Запуск отладчика',
        'Основное окно', 'Точки останова',
        'Список точек останова', 'Список импортируемых',
        'Окно проверки', 'Стек вызовов',
        'Окно переменных', 'Окно выражений',
        'Ввод выражения', 'Редактирование выражения',
        'Настройка отладчика', 'Список горячих клавиш',
        'Алфавитный указатель',
    ]
    
    for header in headers:
        if text.startswith(header):
            return True
    
    return False

def get_header_level(text):
    """Determine header level based on context"""
    # Main parts
    if text in ['Введение', 'Язык интерпретатора RSL', 
                'Интегрированная среда разработки программ на языке RSL',
                'Отладчик макропрограмм']:
        return 1
    
    # Major sections
    major = ['Элементы языка', 'Типы данных', 'Константы', 'Выражения',
             'Структура программы', 'Конструкции языка RSL',
             'Организация ввода/вывода', 'Формирование отчетов',
             'Поддержка интерактивного режима', 'Работа с файлами',
             'Встроенные процедуры', 'Классы и объекты',
             'Средство разработки расширений', 'Сводка синтаксиса',
             'Словарь', 'Директории', 'Файлы', 'Структуры', 'Данные',
             'Процедуры', 'Редактирование ресурсов', 'Отладчик']
    if any(text.startswith(m) for m in major):
        return 2
    
    return 3

def is_code_example(text):
    """Detect if line is a code example"""
    # Code markers
    code_markers = [
        'MACRO ', 'CLASS ', 'VAR ', 'CONST ', 'FILE ', 'RECORD ',
        'IF ', 'WHILE ', 'RETURN', 'END', 'PRINT(', 'INPUT(',
        'BEGIN', 'COMMIT', 'ROLLBACK',
    ]
    for marker in code_markers:
        if text.startswith(marker):
            return True
    return False

if __name__ == '__main__':
    main()
