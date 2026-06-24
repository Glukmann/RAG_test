import re

def split_file_by_headings(filepath, headings, output_filepath=None):
    """
    Разбивает файл на секции по заданным заголовкам.
    headings: список строк-заголовков (без ##)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Найти позиции заголовков
    positions = []
    last_pos = 0
    for heading in headings:
        # Ищем строку, которая точно совпадает с заголовком (без пробелов в конце)
        found = False
        for i in range(last_pos, len(lines)):
            line_stripped = lines[i].strip()
            if line_stripped == heading:
                positions.append((heading, i))
                last_pos = i + 1
                found = True
                break
        if not found:
            print(f"WARNING: Heading '{heading}' not found in {filepath}")
            # Добавляем фиктивную позицию в конце
            positions.append((heading, len(lines)))
    
    # Генерируем новый контент
    new_lines = []
    # Добавляем заголовок H1
    new_lines.append(f"# {headings[0]}\n\n")
    
    for i in range(len(positions)):
        heading, start_line = positions[i]
        if i + 1 < len(positions):
            _, end_line = positions[i + 1]
        else:
            end_line = len(lines)
        
        # Добавляем заголовок H2
        new_lines.append(f"## {heading}\n\n")
        
        # Добавляем содержимое секции (пропускаем оригинальную строку заголовка)
        for j in range(start_line + 1, end_line):
            new_lines.append(lines[j])
        
        new_lines.append('\n')
    
    # Записываем результат
    out_path = output_filepath or filepath
    with open(out_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Split {filepath} into {len(positions)} sections -> {out_path}")
    return len(positions)


def main():
    # DBExp.md
    dbexp_headings = [
        "Введение",
        "Основное окно программы",
        "Файл",
        "Сервис",
        "Вид",
        "Окно",
        "Справка"
    ]
    split_file_by_headings('/Users/lipanovav/rag/knowledge/DBExp.md', dbexp_headings)
    
    # Retail_Instrument.md
    retail_headings = [
        "Введение",
        "Репликация данных в формате XML",
        "Репликация оперативных данных",
        "Выгрузка оперативных данных",
        "Загрузка оперативных данных",
        "Теги сессии репликации оперативных",
        "Репликация справочников",
        "Выгрузка справочников",
        "Загрузка справочников",
        "Теги сессии репликации справочников",
        "Сбор данных о времени выполнения операций"
    ]
    split_file_by_headings('/Users/lipanovav/rag/knowledge/Retail_Instrument.md', retail_headings)
    
    # UserCryptPlugin.md
    crypt_headings = [
        "Введение",
        "Криптоплагины ИБС RS-Bank V.6",
        "Класс TCryptoPlugin",
        "Методы наложения ЭЦП",
        "Методы проверки ЭЦП",
        "Методы кэширования пароля",
        "Методы для работы с хэшем",
        "Методы шифрования",
        "Рекомендации по созданию пользовательского криптоплагина"
    ]
    split_file_by_headings('/Users/lipanovav/rag/knowledge/UserCryptPlugin.md', crypt_headings)

if __name__ == '__main__':
    main()
