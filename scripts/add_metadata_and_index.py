import os
import re

# Словарь категорий по имени файла
CATEGORY_MAP = {
    'RSL_': 'RSL-справочник',
    'BnRSL.md': 'RSL-справочник',
    'RSL_Forms.md': 'RSL-формы',
    '_SQL.md': 'SQL-пакеты',
    '_RSLprc.md': 'RSL-процедуры',
    'DLM.md': 'DLM-SDK',
    'JasperReports.md': 'JasperReports',
    'ReportTools.md': 'Инструменты-отчётов',
    'RCE32.md': 'RCE32',
    'Trace.md': 'Trace',
    'ATM.md': 'ATM',
    'DBExp.md': 'DB-Explorer',
    'Retail_Instrument.md': 'Retail-инструменты',
    'UserCryptPlugin.md': 'Криптография',
    'Reports_InstrExp.md': 'Экспорт-отчётов',
    'db_schema_': 'Схема-БД',
}

DESCRIPTION_MAP = {
    'RSL_': 'Справочник по языку RSL (RS-Bank Scripting Language)',
    'BnRSL.md': 'Основной справочник по языку RSL — синтаксис, типы данных, конструкции, классы, методы',
    'RSL_Forms.md': 'Работа с формами, диалогами, отчётами в RSL',
    '_SQL.md': 'SQL-пакеты и процедуры базы данных RS-Bank',
    '_RSLprc.md': 'Процедуры и функции на языке RSL для модуля',
    'DLM.md': 'DLM SDK — средство разработки расширений для языка RSL',
    'JasperReports.md': 'JasperReports — генерация отчётов',
    'ReportTools.md': 'Инструменты для работы с отчётами',
    'RCE32.md': 'RCE32 — Remote Call Environment',
    'Trace.md': 'Trace — трассировка и отладка',
    'ATM.md': 'ATM — банкоматы и самообслуживание',
    'DBExp.md': 'DB Explorer — утилита для работы со структурами таблиц БД',
    'Retail_Instrument.md': 'Retail Instrument — инструментальные расширения RS-Retail',
    'UserCryptPlugin.md': 'User Crypt Plugin — криптографические плагины RS-Bank',
    'Reports_InstrExp.md': 'Reports Instrument Export — экспорт отчётов',
    'db_schema_': 'Структура базы данных RS-Bank',
}

def get_category(fname):
    for key, cat in CATEGORY_MAP.items():
        if key in fname:
            return cat
    return 'Документация'

def get_description(fname):
    for key, desc in DESCRIPTION_MAP.items():
        if key in fname:
            return desc
    return 'Документация RS-Bank'

def add_metadata(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fname = os.path.basename(filepath)
    
    # Проверяем, есть ли уже метаданные
    if content.startswith('---'):
        return  # Уже есть frontmatter
    
    category = get_category(fname)
    description = get_description(fname)
    
    # Считаем секции
    sections = content.count('\n## ')
    
    metadata = f"""---
title: {fname.replace('.md', '')}
description: {description}
category: {category}
source: PDF-документация RS-Bank V.6
sections: {sections}
generated: true
---

"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(metadata + content)
    
    print(f'Added metadata to {fname}')

def create_index():
    files = []
    for fname in sorted(os.listdir('/Users/lipanovav/rag/knowledge')):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join('/Users/lipanovav/rag/knowledge', fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Считаем секции
        sections = content.count('\n## ')
        lines = content.count('\n')
        
        category = get_category(fname)
        description = get_description(fname)
        
        files.append({
            'name': fname,
            'category': category,
            'description': description,
            'sections': sections,
            'lines': lines,
        })
    
    # Группируем по категориям
    from collections import defaultdict
    groups = defaultdict(list)
    for f in files:
        groups[f['category']].append(f)
    
    lines = ['# Индекс базы знаний RSL / RS-Bank\n']
    lines.append('Автоматически сгенерированный индекс всех документов базы знаний.\n')
    lines.append(f'**Всего файлов:** {len(files)}\n')
    lines.append('---\n\n')
    
    for category in sorted(groups.keys()):
        lines.append(f'## {category}\n\n')
        for f in sorted(groups[category], key=lambda x: x['name']):
            lines.append(f"- **[{f['name']}]({f['name']})** — {f['description']} ({f['sections']} секций, {f['lines']} строк)\n")
        lines.append('\n')
    
    with open('/Users/lipanovav/rag/knowledge/index.md', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print('Created index.md')

if __name__ == '__main__':
    for fname in os.listdir('/Users/lipanovav/rag/knowledge'):
        if fname.endswith('.md'):
            add_metadata(os.path.join('/Users/lipanovav/rag/knowledge', fname))
    
    create_index()
