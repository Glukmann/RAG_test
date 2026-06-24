---
title: RSL_15_syntax
description: Справочник по языку RSL (RS-Bank Scripting Language)
category: RSL-справочник
source: PDF-документация RS-Bank V.6
sections: 4
generated: true
---

# Сводка синтаксиса

> RSL (R-Style Language) — Руководство программиста
> Copyright © 1993-2001 R-Style Softlab

---

В данном приложении приведён формальный синтаксис языка RSL в форме Расширенной Бэкуса-Наура (РБНФ).

## Соглашения нотации

| Элемент | Значение |
|---------|----------|
| Терминалы | Набраны заглавными буквами |
| `NUMBER` | Константа типа `V_INTEGER`, `V_DOUBLE` или `V_MONEY` |
| `NAME` | Последовательность букв и цифр, начинающаяся с буквы. Символ подчёркивания `_` считается буквой |
| `SPNAME` | Последовательность любых символов, заключённая в фигурные скобки, например `{34-23-O}` |
| `STRING` | Строка символов, заключённая в кавычки |
| `[ ... ]` | Необязательная конструкция |
| `{ ... }` | Конструкция, которая может повторяться произвольное количество раз или отсутствовать |
| `\|` | Альтернатива |

### Esc-символы в строках

| Esc-последовательность | Значение |
|------------------------|----------|
| `\n` | Новая строка |
| `\r` | Возврат каретки |
| `\t` | Символ табуляции |
| `\f` | Перевод формата |
| `\xHH`, `\XHH` | Символ, заданный кодом `HH` (две шестнадцатеричные цифры) |

---

## Формальная грамматика RSL

```rbnf
unit := u_decl_list [ errhandler ] [ END ] .

u_decl_list := u_decl { ';' u_decl } .

errhandler := ONERROR [ '(' id ')' ] decl_list .

decl_list := decl { ';' decl } .

u_decl := import_def | decl .

import_def := IMPORT file_nm_lst .

file_nm_lst := file_name { ',' file_name } .

file_name := id | STRING .

id := NAME | SPNAME .

decl := macro_def | var_def | const_def | array_def | file_def |
        record_def | class_def | with_def | statement .

macro_def := [attr] MACRO id [ form_parm ] [ tpdecl ] decl_list
             [ errhandler ] END .

form_parm := '(' [ id_list ] ')' .

id_list := tpid { ',' tpid } .

tpid := id [ tpdecl ] .

tpdecl := ':' tpname .

tpname := id | VARIANT | INTEGER | MONEY | DOUBLE | MONEYL
          | DOUBLEL | STRING | BOOL | DATE | TIME | OBJECT |
          PROCREF | DATETIME | MEMADDR .

var_def := [attr] VAR init_id_list .

init_id_lst := init_var { ',' init_var } .

init_var := tpid [ '=' expression ] .

const_def := [attr] CONST const_lst .

const_lst := init_const { ',' init_const } .

init_const := tpid '=' expression .

array_def := [attr] ARRAY id_list .

file_def := [attr] FILE id '(' file_name [',' file_name ] ')' [ fparm_lst ] .

fparm_lst := fparm { fparm } .

fparm := NORMAL | KEY NUMBER | WRITE | MEM | TXT [NUMBER] | BTR |
         SORT NUMBER | DBF | DIALOG | BLOB .

record_def := [attr] RECORD id '(' file_name [',' file_name] ')' [fparm_lst] .

class_def := [attr] CLASS ['(' id ')' ] id [ form_parm ] decl_list
             [ errhandler ] END .

with_def := WITH '(' id ')' decl_list END .

attr := PRIVATE | LOCAL .

statement := [ loop | ifstmt | retstmt | outstmt | expstmt ] .

loop := WHILE condition stmt_list END .

ifstmt := IF condition stmt_list
          { ELIF condition stmt_list }
          [ ELSE stmt_list ] END .

condition := '(' expression ')' .

retstmt := RETURN [expression] .

outstmt := '[' control_str ']' [ '(' [ explist ] ')' ] .

control_str := print_ch | format_ch .

print_ch := любой символ, не равный format_ch .

format_ch := '#' .

expstmt := expression .

stmt_list := statement { ';' statement } .

expression := BoolExp { '=' BoolExp } .

BoolExp := SimplExpr [ relop SimplExpr ] .

SimplExpr := [ '+' | '-' ] Term { AddOp Term } .

Term := Factor { MulOp Factor } .

Factor := NUMBER | STRING | '(' expression ')' | NOT Factor
          | '@' Factor | qualId .

qualId := id { '.' id | '(' [ expList ] ')' } .

expList := exp_form { ',' exp_form } .

exp_form := expression [fmt_list] .

fmt_list := fmt_spec { fmt_spec } .

fmt_spec := ':' fmt_symbol .

fmt_symbol := NUMBER | 'l' | 'r' | 'c' | 'a' | 't' | 'd' | 'm' | 'w' | 'z' | 'f' | 'i' | 'iv' | 'v' .

relop := '==' | '!=' | '<' | '<=' | '>' | '>=' .

AddOp := '+' | '-' | OR .

MulOp := '*' | '/' | AND .
```

---

## Таблица операций

| Группа операций | Операторы | Ассоциативность | Приоритет |
|-------------------|-----------|-----------------|-----------|
| Унарные | `+`, `-`, `NOT`, `@` | Правая | Высокий |
| Мультипликативные | `*`, `/`, `AND` | Левая | Высокий |
| Аддитивные | `+`, `-`, `OR` | Левая | Средний |
| Сравнения | `==`, `!=`, `<`, `<=`, `>`, `>=` | Левая | Низкий |
| Присваивание | `=` | Правая | Самый низкий |

---

## Примечания

- Все операции, кроме операции присваивания, имеют **левую ассоциативность**; операция присваивания — **правоассоциативна**.
- Приоритет группы `relop` самый низкий, `MulOp` — самый высокий.
- Порядок вычисления операндов не определён для всех операций, кроме `OR` (логическое ИЛИ) и `AND` (логическое И). Для операций `OR` и `AND` сначала вычисляется левый операнд, далее, если необходимо, вычисляется правый операнд.
