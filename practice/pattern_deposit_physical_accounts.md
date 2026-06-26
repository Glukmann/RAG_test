# Паттерн: работа с открытыми депозитными счетами физических лиц

**Источники:**
- `Mac/DEPOSITR/ic_deposit.mac`
- `Mac/DEPOSITR/accexist.mac`
- `Mac/DEPOSITR/rt_lc.mac`
- `Mac/WebServices/ws_RetailDeposits.mac`
- `Mac/SBDESK/budgetcheck.mac`
- `Mac/BOOK/PFRRefund.mac`
- `Mac/CELLS/trmconls.mac`

## Используемые таблицы

Полная структура всех таблиц RS-Bank V.6 извлечена из PowerDesigner-модели в файл `knowledge/db_schema_from_pdm.md`.

| Таблица | Название | Назначение | Ключевые поля |
|---------|----------|------------|---------------|
| `ddepositr_dbt` | Счет вкладчика | Депозитные счета | `t_Referenc`, `t_Account`, `t_CodClient`, `t_FNCash`, `t_Code_Currency`, `t_Type_Account`, `t_Open_Date`, `t_Close_Date`, `t_Open_Close`, `t_Action` |
| `dparty_dbt` | Субъект экономики | Контрагенты / клиенты | `t_PartyID`, `t_Name`, `t_ShortName`, `t_LegalForm` |
| `dpersn_dbt` | Физическое лицо | Физические лица | `t_PersonID`, `t_Name1` (фамилия), `t_Name2` (имя), `t_Name3` (отчество) |

## Признаки открытого депозитного счета

- `t_Open_Close = chr(0)` — счет открыт.
- `t_Action NOT IN (2, 11)` — исключить удаленные (`2`) и сторнированные (`11`) записи.
- `t_Open_Date <= ОперационнаяДата` — счет уже открыт на дату.
- `t_Close_Date` обычно проверяется как `TO_DATE('01.01.0001','dd.mm.yyyy')` или `> ОперационнаяДата`.

## Признак физического лица

В `dparty_dbt` поле `t_LegalForm` определяет тип клиента:

- `t_LegalForm = 2` — физическое лицо (см. `SBDESK/budgetcheck.mac`, `IsClientPhysical`).
- `t_LegalForm = 1` — юридическое лицо.

Также в системе используется константа `PTLEGF_PERSN`, которая соответствует физическому лицу.

## Получение ФИО клиента

ФИО физического лица хранится в `dpersn_dbt`:

```sql
SELECT t_Name1, t_Name2, t_Name3
  FROM dpersn_dbt
 WHERE t_PersonID = :ClientID
```

Склейка в RSL:

```rsl
var fio = rs.value("Name1") + " " + rs.value("Name2") + " " + rs.value("Name3");
```

## Пример SQL-запроса: открытые депозиты физлиц

```sql
SELECT dr.t_Referenc,
       dr.t_Account,
       dr.t_FNCash,
       dr.t_Code_Currency,
       dr.t_Type_Account,
       dr.t_Open_Date,
       dr.t_Close_Date,
       dr.t_CodClient,
       pers.t_Name1,
       pers.t_Name2,
       pers.t_Name3
  FROM ddepositr_dbt dr
       INNER JOIN dparty_dbt party ON party.t_PartyID = dr.t_CodClient
       LEFT JOIN dpersn_dbt pers ON pers.t_PersonID = dr.t_CodClient
 WHERE dr.t_Open_Close = chr(0)
   AND dr.t_Action NOT IN (2, 11)
   AND party.t_LegalForm = 2
 ORDER BY pers.t_Name1, pers.t_Name2, pers.t_Name3, dr.t_Account
```

## Пример макроса

См. `new_macros/OpenDepPhysAccounts.mac`.

## Правила сохранения новых макросов

Новые макросы, созданные ИИ-агентом, сохраняются в `Mac/NEW_MACROS/`, чтобы не смешиваться с оригинальной кодовой базой системы.
