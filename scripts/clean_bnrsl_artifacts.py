import re

def clean_bnrsl_artifacts(filepath):
    """
    Убирает ложные ### подзаголовки (артефакты реструктуризации) и объединяет их в блоки кода.
    """
    # Список артефактов (строки кода, операторы, частые ложные подзаголовки)
    ARTIFACTS = {
        'if', 'println', 'Println', 'class', 'elif', 'while', 'MsgBox', 'AddColumn',
        'copy', 'RunDialog', 'for', 'message', 'setparm', 'SetScroll', 'ReplaceMacro',
        'm', 'SetFocus', 'AddField', 'insert', 'getparm', 'First', 'asize', 'OnError',
        'onError', 'UpdateFields', 'InitTRecHandler', 'trace', 'FillDown', 'rewind',
        'InitBtrAdapterBase', 'TRecHandler', 'open', 'printlm', 'WeakRef', 'InitTBFile',
        'WHILE', 'Test', 'Demo', 'V_ARRAY', 'MyVar', 'aa', 'RslTimer', 'RemTimer',
        'InitTForm', 'setTemplate', 'InitBtrAdapter', 'InitBtrAdapterEx', 'Second',
        'ClrObj', 'TestEvent', 'OnTestEvent', 'OnTestEvent2'
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    in_code_block = False
    code_buffer = []
    
    for line in lines:
        if line.startswith('### '):
            subheading = line.strip()[4:]
            if subheading in ARTIFACTS:
                # Это артефакт, начинаем или продолжаем блок кода
                if not in_code_block:
                    if code_buffer:
                        new_lines.extend(code_buffer)
                        code_buffer = []
                    new_lines.append('```rsl\n')
                    in_code_block = True
                code_buffer.append(subheading + '\n')
            else:
                # Это реальный подзаголовок
                if in_code_block:
                    new_lines.append('```\n')
                    in_code_block = False
                    code_buffer = []
                new_lines.append(line)
        else:
            if in_code_block:
                code_buffer.append(line)
            else:
                new_lines.append(line)
    
    if in_code_block:
        new_lines.append('```\n')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'Cleaned artifacts in {filepath}')

if __name__ == '__main__':
    clean_bnrsl_artifacts('/Users/lipanovav/rag/knowledge/BnRSL.md')
