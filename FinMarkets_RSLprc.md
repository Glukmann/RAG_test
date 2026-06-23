# FinMarkets RSLprc

Введение
Настоящее Руководство содержит описание переменных, классов, процедур и констант
языка интерпретатора RSL, которые используются при создании макромодулей, входящих в
состав АС RS-FinMarkets ИБС RS-Bank V.6, и при написании пользователем собственных
макропрограмм.
Информация об общесистемных интерфейсах RSL содержится в следующих Руководствах:
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 1" (файл Books\Tools\CoreRSLprc_1.pdf) – содержит описание общесистемных
спецпеременных 
и 
модулей 
BalanceInter, 
BankInter, 
BilFacturaInter, 
CarryDoc,
cryptdlm.d32, CTInter.
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 2" (файл Books\Tools\CoreRSLprc_2.pdf) – содержит описание модулей
CurrInter, FIInter, GateInter, InsCarryDoc, OprInter, PcRateInter, PTInter, RsbDataSet,
RsbObjFactory, RsSysLog, SFInter.
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 3" (файл Books\Tools\CoreRSLprc_3.pdf) – содержит описание модулей
PaymInter, Календарь, Проценты, Шлюз.
Описание интерфейсов языка RSL, используемых для взаимодействия с АС RS-Reporting
V.6, RS-Retail V.6, RS-Loans V.6, RS-Banking V.6 приведено в соответствующих Руководствах
к этим АС.
Интерфейсы языка RSL поставляются в виде стандартных RSL-модулей и становятся
доступными пользователю после подключения этих модулей к программам. Чтобы
подключить какой-либо модуль, необходимо воспользоваться командой Import.
Пример.
Import DealsInter;
Описание стандартных модулей сгруппировано по отдельным главам, название каждой из
которых соответствует названию соответствующего модуля. Каждая глава Руководства
содержит большое количество примеров, иллюстрирующих использование интерфейсов при
написании программ.
Внимание!
Перед изучением описания интерфейсов языка RSL ознакомьтесь с
разделом Руководства "Проблемно-ориентированный язык RSL" (файл
Books\Tools\BnRSL.pdf), 
который 
посвящен 
соглашению 
об
использовании имен и структур таблиц данных в прикладных
программах, разработанных специалистами компании R-Style Softlab.
При ссылке на информацию, расположенную в настоящем руководстве, указывается номер
страницы (в скругленном прямоугольнике 
), соответствующий нужному Вам разделу, или
гиперссылка. Ссылка на раздел другого руководства дается с указанием названия главы и
раздела, содержащего требуемую информацию.
RS-FinMarkets.
Классы

## Класс: `RsbPriceCondition`

```rsl
RsbPriceCondition ([LegKind:Integer], [DealID:Integer], [LegID:Integer]):Object
```

## Класс: `RsbDealTick`

```rsl
RsbDealTick ([DealID:Integer]):Object
```

## Класс: `RsbDealTick`

```rsl
предназначен для получения информации по сделке из таблицы ddl_tick_dbt. Создание объекта класса возможно двумя способами: · С использованием конструктора с параметрами (при этом в поля объекта загружается информация о сделке).
```

**Пример:**

var DealTick = RsbDealTick(DealID);
- С использованием конструктора по умолчанию (при этом информация о сделке не
загружается в поля объекта).

**Пример:**

var DealTick = RsbDealTick();

**Параметры:**

DealID – идентификатор записи таблицы как ddl_tick_dbt.

**Свойства:**

DealID – идентификатор сделки. Свойство доступно только для чтения и имеет тип Long.
Attributes – атрибуты сделки (поле t_attributes таблицы ddl_tick_dbt); тип Long.
BofficeKind – вид сделки (поле t_bofficekind таблицы ddl_tick_dbt); тип Integer.
BrokerContrID – договор обслуживания контрагента (поле t_brokercontrid таблицы
ddl_tick_dbt); тип Long.
BrokerID – брокер (поле t_brokerid таблицы ddl_tick_dbt); тип Long.
Bundle – номер связки (поле t_bundle таблицы ddl_tick_dbt); тип Long.
CBRiskGroup – группа риска по ценным бумагам (поле t_cbriskgroup таблицы
ddl_tick_dbt); тип Integer.
ClientContrID – договор обслуживания клиента (поле t_clientcontrid таблицы ddl_tick_dbt);
тип Long.
ClientID – идентификатор клиента (поле t_clientid таблицы ddl_tick_dbt); тип Long.
CloseDate – дата завершения сделки (поле t_closedate таблицы ddl_tick_dbt); тип Date.
Collateral – тип обеспечения (поле t_collateral таблицы ddl_tick_dbt); тип Integer.
Comment – комментарий (поле t_comment таблицы ddl_tick_dbt); тип String.
ConfTpID – транспорт подтверждения (поле t_conftpid таблицы ddl_tick_dbt); тип Long.
DealCode – номер сделки в системе учета (поле t_dealcode таблицы ddl_tick_dbt); тип
String.
DealCodePS – код в системе подтверждений (поле t_dealcodeps таблицы ddl_tick_dbt); тип
String.
DealCodeTS – номер сделки в торговой системе (поле t_dealcodets таблицы ddl_tick_dbt);
тип String.
DealDate – дата заключения сделки (поле t_dealdate таблицы ddl_tick_dbt); тип Date.
DealTime – время заключения сделки (поле t_dealtime таблицы ddl_tick_dbt); тип Date.
Department – филиал (поле t_department таблицы ddl_tick_dbt); тип Long.
DepositID – депозитарий (поле t_depositid таблицы ddl_tick_dbt); тип Long.
ExternID – внешняя сделка (поле t_externid таблицы ddl_tick_dbt); тип String.
InDocCode – номер поручения на сделку (поле t_indoccode таблицы ddl_tick_dbt); тип
String.
IndocID – идентификатор поручения на сделку (поле t_indocid таблицы ddl_tick_dbt); тип
Long.
isPercent – признак указания цены в процентах от номинала (поле t_ispercent таблицы
ddl_tick_dbt); тип String.
LinkChannel – канал связи (поле t_linkchannel таблицы ddl_tick_dbt); тип Integer.
MarketID – торговая площадка (поле t_marketid таблицы ddl_tick_dbt); тип Long.
MarketOfficeID – сектор торговой площадки (поле t_marketofficeid таблицы ddl_tick_dbt);
тип Long.
Netting – режим неттинга (поле t_netting таблицы ddl_tick_dbt); тип Integer.
Number_Coupon – номер купона в операции погашения (поле t_number_coupon таблицы
ddl_tick_dbt); тип String.
NumberPack – номер пачки (поле t_numberpack таблицы ddl_tick_dbt); тип Integer.
Oper – операционист (поле t_oper таблицы ddl_tick_dbt); тип Long.
OriginID – происхождение сделки (поле t_originid таблицы ddl_tick_dbt); тип Integer.
PartyID – идентификатор контрагента (поле t_partyid таблицы ddl_tick_dbt); тип Long.
PortfolioID – портфель (поле t_portfolioid таблицы ddl_tick_dbt); тип Long.
PreOutlay – предварительные затраты (поле t_preoutlay таблицы ddl_tick_dbt); тип Double.
RegDate – дата регистрации сделки (поле t_regdate таблицы ddl_tick_dbt); тип Date.
RiskGroup – группа риска (поле t_riskgroup таблицы ddl_tick_dbt); тип Integer.
TraderID – трэйдер (поле t_traderid таблицы ddl_tick_dbt); тип Long.
TradeSystem – торговая система (поле t_tradesystem таблицы ddl_tick_dbt); тип Integer.
UserField1 – пользовательское поле №1 (поле t_userfield1 таблицы ddl_tick_dbt); тип
String.
UserField1 – пользовательское поле №2 (поле t_userfield2 таблицы ddl_tick_dbt); тип
String.
UserField1 – пользовательское поле №3 (поле t_userfield3 таблицы ddl_tick_dbt); тип
String.
UserField1 – пользовательское поле №4 (поле t_userfield4 таблицы ddl_tick_dbt); тип
String.
UserTypeDoc 
- 
пользовательский 
тип 
документа 
(поле 
t_usertypedoc 
таблицы
ddl_tick_dbt); тип String.
Константы
Вид документа, удостоверяющий
полномочия представителя стороны
договора
DL_SPG_REGUL – устав.
DL_SPG_TRUST – доверенность.
Виды договоров
KDL_ORDER_VSBARTER – мена векселей.
KDL_ORDER_VSDISC – дисконтный договор (договор купли-продажи дисконтного
векселя).
KDL_ORDER_VSDRAW – заявление на погашение.
KDL_ORDER_VSDRAW_EARLY – досрочное погашение векселя.
KDL_ORDER_VSEMIS – вексельный договор.
KDL_ORDER_VSINTERCHANGE – соглашение о зачете требований.
KDL_ORDER_VSPERC – процентный вексельный договор.
KDL_ORDER_VSSALE – договор продажи векселей.
Виды индоссаментов
IRCAG_ENDORSKIND_COMMIT – препоручительство.
IRCAG_ENDORSKIND_NOTBACK – безоборотный.
IRCAG_ENDORSKIND_NOTDEF – не определен.
IRCAG_ENDORSKIND_PAWN – залоговый.
IRCAG_ENDORSKIND_SIMPLE – простой.
Виды значений настройки "Ведение
депозитарного учета"
DL_CUSTODYACCOUNTING_CARRYDOC – депозитарный учет ведется в системе при
помощи проводок по лицевым счетам Депо.
DL_CUSTODYACCOUNTING_CUSTODY – депозитарный учет в системе ведется в рамках
подсистемы "Депозитарий".
DL_CUSTODYACCOUNTING_NO – депозитарный учет в системе не ведется.
DL_CUSTODYACCOUNTING_UNDEF – значение не определено.
Виды значений настройки "Вид связи с
депозитарием"
DL_KINDLINKCUSTODY_DOUBLE –двухсторонняя связь с депозитарием.
DL_KINDLINKCUSTODY_SINGLE – односторонняя связь с депозитарием.
DL_KINDLINKCUSTODY_UNDEF – значение не определено.
Виды значений признака установленности
"Депозитария" в системе
DL_INSTALLCUSTODY_UNDEF – значение не определено.
Виды операций
DL_MACOP_CORRECT – корректировка параметров графика погашения.
DL_MACOP_CREATEOPER – создание операции.
DL_MACOP_DELETE – удаление сделки.
DL_MACOP_DELETEOPER – удаление операции.
DL_MACOP_INSERT – ввод новой сделки.
DL_MACOP_UPDATE – обновление сделки.
Виды представителей
DLPROXY_CLIENT – сторона договора – клиент.
DLPROXY_CONTRACTOR – представитель контрагента.
DLPROXY_OURBANK – представитель нашего банка.
Виды связей между векселем и договором
VSORDLNK_K_ALL – все роли векселей по договору.
VSORDLNK_K_DRAW – погашение.
VSORDLNK_K_EMISSION – эмиссия.
VSORDLNK_K_PAWN – залог.
VSORDLNK_K_SALE – продажа.
VSORDLNK_K_STORAGE – хранение.
Виды сделок
DL_LEGID_BASE – прямая сделка.
DL_LEGID_REV – обратная сделка.
Виды статусов комиссии
DL_COMM_CLOSED – закрыта.
DL_COMM_PREPARING – на этапе подготовки.
DL_COMM_READIED – готова (создана операция).
Виды статусов сделок
DL_CLOSED – сделка закрыта.
DL_OPENCLOSED – открытые и закрытые.
DL_PREPARING – сделка на этапе подготовки.
DL_READIED – сделка готова (создана операция).
DL_UNDEFSTAT – неопределенный статус (статус не задан).
Виды сумм в поле t_kind таблицы
ddlsum_dbt
DLSUM_KIND_AGENT_ONCE – единовременная комиссия посреднику.
DLSUM_KIND_AGENT_ONCE_IMPORT – импортированная единовременная комиссия
посреднику в валюте начисления.
DLSUM_KIND_AGENT_PERIOD – периодическая комиссия посреднику.
DLSUM_KIND_BANK_ONCE – единовременная комиссия клиента банку.
DLSUM_KIND_BANK_ONCE_CONTR – единовременная комиссия контрагента банку.
DLSUM_KIND_BANK_ONCE_IMPORT – импортированная единовременная комиссия
банку в валюте начисления.
DLSUM_KIND_BANK_PERIOD – периодическая комиссия клиента банку.
DLSUM_KIND_BANK_PERIOD_CONTR – периодическая комиссия контрагента банку.
DLSUM_KIND_BEGBONUS – текущая начальная премия.
DLSUM_KIND_BEGDISCONTINCOME – начальный дисконт.
DLSUM_KIND_BONUS – начисленная премия.
DLSUM_KIND_BPP_SUM – количество ценных бумаг без первоначального признания
(БПП) для операции перемещения.
DLSUM_KIND_COMPDEL_SUMBACKKSU – сумма в портфеле ПВО_КСУ.
DLSUM_KIND_COMPDEL_SUMPKU – сумма в ПКУ.
DLSUM_KIND_COSTWRTTAX – стоимость покупки в налоговом учете.
DLSUM_KIND_DISCONTCORR – начисленный дисконтный доход, списанный при
переводе.
DLSUM_KIND_DISCONTINCOME – дисконтный доход.
DLSUM_KIND_DISCONTINCOMENOTCARRY – дисконтный доход, не отнесенный на
доходы.
DLSUM_KIND_INTERESTINCOME – процентный доход.
DLSUM_KIND_INTERESTINCOMENOTCARRY – процентный доход, не отнесенный на
доходы.
DLSUM_KIND_NKDWRTTAX – НКД в налоговом учете.
DLSUM_KIND_OLDBEGBONUS – начальная премия до перевода.
DLSUM_KIND_OLDBEGDISCONTINCOME – начальный дисконт до перевода.
DLSUM_KIND_OUTBAL_SUM1 – первое количество на внебалансе для операции
перемещения.
DLSUM_KIND_OUTBAL_SUM2 – второе количество на внебалансе для операции
перемещения.
DLSUM_KIND_OUTBAL_SUM3 – третье количество на внебалансе для операции
перемещения.
DLSUM_KIND_OUTLAY – затраты на приобретение.
DLSUM_KIND_OUTLAYWRTTAX – затраты в НУ.
DLSUM_KIND_OVERVALUE – переоценка.
DLSUM_KIND_PRICEWRTTAX – цена покупки в НУ.
DLSUM_KIND_REGISTAR_ONCE – единовременная комиссия регистратору.
DLSUM_KIND_REGISTAR_ONCE_CONTR 
- 
единовременная 
комиссия 
контрагента
регистратору.
DLSUM_KIND_RESERV_BACKREPO – сумма резерва по требованиям по второй части
сделок обратного репо (ОР).
DLSUM_KIND_RESERV_DELAY – сумма резерва по сделкам с отсрочкой платежа.
DLSUM_KIND_RESERV_OVERDUE – сумма резерва по просроченным требованиям.
DLSUM_KIND_RESERV_SALEREPO2_CONTR – сумма резерва по требованиям по 2
части сделок прямого РЕПО в ПКУ.
DLSUM_KIND_SUM_CLAIMS_LIABILITE – сумма требования/обязательства.
DLSUM_KIND_SUM_COUPON_INCOME_BACK – сумма купонного дохода, подлежащего
возврату.
DLSUM_KIND_SUM_DV_NKR– сумма НКР в операции с ПИ.
DLSUM_KIND_SUM_NOTCARRY_PERCENT 
- 
сумма 
начисленных 
процентов, 
не
отнесенная на доходы в валюте расчетов (ВР).
DLSUM_KIND_SUM_NOTCARRY_PERCENT_CFI – сумма начисленных процентов, не
отнесенная на доходы в валюте цены (ВЦ).
DLSUM_KIND_SUM_PARTIAL_INCOME_BACK – сумма дохода по частичному погашению
(ЧП), подлежащего возврату.
DLSUM_KIND_SUM_TO_PERCENT – сумма начисленных процентов в валюте расчетов.
DLSUM_KIND_SUM_TO_PERCENT_CFI – сумма начисленных процентов в валюте цены.
Значения настроек депозитарного учета
DL_CustodyAccounting – текущее значение настройки "Ведение депозитарного учета";
может принимать значения из группы "Виды значений настройки «Ведение
депозитарного учета»
".
DL_KindLinkCustody – текущее значение настройки "Вид связи с депозитарием"; может
принимать значения из группы "Виды значений настройки «Вид связи с
депозитарием»
".
DL_NdaysBeforeInsertDepoDraft – значение настройки "Срок от плановой даты поставки
ценных бумаг до формирования поручения ДЕПО".
Подвиды операций перевода ценных бумаг
DLCOMM_OPERSUBKIND_FROM_CONTROL – перемещение из портфеля контрольного
участия.
DLCOMM_OPERSUBKIND_RETIRE_TO_SALE 
- 
переклассификация 
ценных 
бумаг,
"удерживаемых до погашения", в ценные бумаги "для продажи".
DLCOMM_OPERSUBKIND_SALE_TO_RETIRE – переклассификация ценных бумаг "для
продажи" в "удерживаемые до погашения".
DLCOMM_OPERSUBKIND_SALE_TO_RETIRE_2129 
- 
перевод 
ценных 
бумаг 
"для
продажи" в "удерживаемые до погашения" (по 2129-У).
DLCOMM_OPERSUBKIND_TO_CONTROL – перемещение в портфель контрольного
участия.
DLCOMM_OPERSUBKIND_TRADE_TO_RETIRE_2129 – перевод ценных бумаг торгового
портфеля в "удерживаемые до погашения" (по 2129-У).
DLCOMM_OPERSUBKIND_TRADE_TO_SALE_2129 – перевод ценных бумаг торгового
портфеля в "ценные бумаги для продажи" (по 2129-У).
DLCOMM_OPERSUBKIND_UNRETIRE – перевод на счета долговых обязательств, не
погашенных в срок.
Подвиды операции расчета
налогооблагаемой базы для НДФЛ
DL_TXBASECALC_OPTYPE_ENDYEAR – окончание года.
DL_TXBASECALC_OPTYPE_LUCRE – материальная выгода.
DL_TXBASECALC_OPTYPE_NORMAL – обычный расчет.
Роли представителей
DL_PROXY_BOOK – главный бухгалтер.
DL_PROXY_BOSS – первое лицо.
DL_PROXY_INCASHER – инкассатор.
DL_PROXY_PAYEE – предъявитель векселя.
DL_PROXY_RECIPIENT – получатель.
Режимы поиска и/или ввода представителей
сторон договора
DL_MODE_PROXY_BUF – без панели из буфера.
DL_MODE_PROXY_PAN – с помощью панели.
DL_MODE_PROXY_PAN_BUF – с помощью панели из буфера.
Статусы договоров
ORDER_CONTRACT_STATUS_CLOSED – закрытый договор.
ORDER_CONTRACT_STATUS_OPENED – договор на стадии исполнения.
ORDER_CONTRACT_STATUS_PREP – отложенный договор.
Статусы лотов
DL_LEG_BALANCE – на балансе.
DL_LEG_FORM – поставлен.
DL_LEG_INITIAL – инициализирован.
DL_LEG_OUTBAL – внебаланс.
DL_LEG_PLANE – запланирован.
DL_LEG_PREPARING – отложен (лот в процессе заполнения).
DL_LEG_REMOVOUTBAL – снят с внебаланса.
DL_LEG_UNDEF – не задан.
Статусы операций по НДФЛ
DL_TXOP_Close – операция закрыта.
DL_TXOP_Open – операция открыта.
DL_TXOP_Prep – операция отвергнута.
Статусы учтенного векселя
VABANNER_STATUS_ACCOUNT– учтен.
VABANNER_STATUS_ALL– любой.
VABANNER_STATUS_ENDED – погашен.
VABANNER_STATUS_INPUT– введен.
Типы индоссамента
IRCAG_ENDORSTYPE_BLANK – бланковый.
IRCAG_ENDORSTYPE_NAME – именной.
IRCAG_ENDORSTYPE_NOTDEF – не определен.
Типы операции удержания НДФЛ
DL_TXHOLD_OPTYPE_CLOSE – закрытие договора.
DL_TXHOLD_OPTYPE_ENDYEAR – окончание года.
DL_TXHOLD_OPTYPE_LUCRE – материальная выгода.
DL_TXHOLD_OPTYPE_OUTAVOIR – вывод ценных бумаг.
DL_TXHOLD_OPTYPE_OUTMONEY – вывод денежных средств.
Флаги для задания битовой маски в поле
t_BitMask таблицы ddl_leg_dbt
DL_LEG_ADD_AGENT_ONCE – начислена единовременная комиссия посреднику.
DL_LEG_ADD_AGENT_PERIOD – начислена периодическая комиссия посреднику.
DL_LEG_ADD_BANK_INPAY_PERIOD – начислена периодическая комиссия банку в дату
оплаты сделки.
DL_LEG_ADD_BANK_ONCE – начислена единовременная комиссия банку.
DL_LEG_ADD_BANK_PERIOD – начислена периодическая комиссия банку.
DL_LEG_ALWAYS_DUE – по сделке изменялись сроки и она теперь всегда срочная.
DL_LEG_ANOTHER_DEPOSITARY – учет в другом депозитарии.
DL_LEG_CALC_AGENT_ONCE – рассчитана единовременная комиссия посреднику.
DL_LEG_CALC_AGENT_PERIOD – рассчитана периодическая комиссия посреднику.
DL_LEG_CALC_BANK_INPAY_PERIOD – рассчитана периодическая комиссия банку в
дату оплаты сделки.
DL_LEG_CALC_BANK_ONCE – рассчитана единовременная комиссия банку.
DL_LEG_CALC_BANK_PERIOD – рассчитана периодическая комиссия банку.
DL_LEG_COMMFULLPORTF – признак учета единовременной комиссии посреднику в
целом по портфелю.
DL_LEG_CONFIRM_DEAL – сделка подтверждена.
DL_LEG_EARLY_EXECUTE – исполнение не в срок.
DL_LEG_IMPORT_COMISS_AGENT – комиссия посреднику импортирована.
DL_LEG_IMPORT_COMISS_BANK – комиссия банку импортирована.
DL_LEG_LAST_EXECUTE – отложенное исполнение.
DL_LEG_NETTING_EXECUTE – признак выполненного неттинга.
DL_LEG_NOPART2 – отказ от исполнения второй части.
DL_LEG_PAY – лот оплачен.
DL_LEG_PAY_AGENT_ONCE – оплачена единовременная комиссия посреднику.
DL_LEG_PAY_AGENT_PERIOD – оплачена периодическая комиссия посреднику.
DL_LEG_PAY_AVANCE_DEPOSIT – аванс\задаток оплачен.
DL_LEG_PAY_BANK_INPAY_PERIOD – оплачена периодическая комиссия банку в дату
оплаты сделки.
DL_LEG_PAY_BANK_ONCE – оплачена единовременная комиссия банку.
DL_LEG_PAY_BANK_PERIOD – оплачена периодическая комиссия банку.
DL_LEG_PREPARE_CONTR – договор подготовлен.
DL_LEG_REPO_BLOCKING – блокированные ценные бумаги, полученные в сделках
РЕПО.
Процедуры
Процедуры поиска

## Процедура: `DealsRestoreDocumentID`

```rsl
DealsRestoreDocumentID (Doc:Record, TbFile, DocumentID:String, DocKind:Integer):Bool
```

## Процедура: `DL_GetProxyName`

```rsl
DL_GetProxyName (Договор:Variant, СторонаДоговора:Integer, РольПреставителя:Integer [. представитель:Record] [, Документ:Record] [, Режим:Integer]):String
```

## Процедура: `FindDL_LEG`

```rsl
FindDL_LEG (LegKind:Integer, DealID:Integer, LegID:Integer, LegBuff:Record):Integer
```

## Процедура: `FindDLMARKET`

```rsl
FindDLMARKET (ID:Integer, Buff:Record):Integer
```

## Процедура: `FindDLMARKETbyMarket`

```rsl
FindDLMARKETbyMarket (MarketID:Integer, IsORCB:Bool, IsTrust:Bool, FI_Kind:Integer, DLMARKET_buff:TRecHandler):Bool
```

## Процедура: `FindDLSUM`

```rsl
FindDLSUM (DocKind:Integer, DocID:Integer, Kind:Integer, Date:Date, buff:Record):Integer
```

## Процедура: `DL_AddAccToDLCONTR`

```rsl
DL_AddAccToDLCONTR (DlContrID:int32, AccPrm:DLCONTRACCPRM[, ErrStr:String]):String
```

## Процедура: `DL_AddSubContrToDLCONTR`

```rsl
DLCONTRDL_AddSubContrToDLCONTR (DlContrID:int32, SubContrPrm:DLCONTRSUBPRM[, ErrStr:String]):String
```

## Процедура: `DL_CloseAccInDLCONTR`

```rsl
DL_CloseAccInDLCONTR (DlContrID:int32, FIID:int32, AccountID:int32, CloseDate:bdate[, ErrStr:String]):String
```

## Процедура: `DL_CloseDLCONTR`

```rsl
DL_CloseDLCONTR (DlContrID:int32, CloseDate:bdate, IisCloseByTransf:bool[, ErrStr:String]):String
```

## Процедура: `DL_CloseSubContrInDLCONTR`

```rsl
DL_CloseSubContrInDLCONTR (DlContrID:int32, SfContrID:int32, CloseDate:bdate[, ErrStr:String]):String
```

## Процедура: `DL_CreateDLCONTR`

```rsl
DL_CreateDLCONTR (DlContrPrm:DLCONTRPRM, AccPrmArr:DLCONTRACCPRM, SubContrPrmArr:DLCONTRSUBPRM[, ErrStr:String]):String
```

## Процедура: `DL_DeleteAccFromDLCONTR`

```rsl
DL_DeleteAccFromDLCONTR (DlContrID:int32, FIID:int32, AccountID:int32[, ErrStr:String]):String
```

## Процедура: `CreateNPTXOP`

```rsl
CreateNPTXOP (Rsl_parm_servkind:Integer, Rsl_parm_type:Integer, Rsl_parm_client:Integer, Rsl_parm_contract:Integer, Rsl_parm_account:Integer, Rsl_parm_sum:Numeric, Rsl_parm_client_account:String, Rsl_parm_client_bank:Integer, Rsl_parm_date:Date, Rsl_parm_time:Time, Rsl_parm_run:Integer, Rsl_parm_spground_id:Integer, Rsl_parm_spground_kind:Integer, Rsl_parm_spground_xld:String, Rsl_parm_spground_date:Date, Rsl_parm_kind_operation:Integer [, Rsl_parm_place:Integer] [, Rsl_parm_market_place:Integer] [, Rsl_parm_market_sector:Integer] [, Rsl_parm_place2:Integer] [, Rsl_parm_market_place2:Integer] [, Rsl_parm_market_sector2:Integer]):Integer
```

## Процедура: `DL_ChangeDLORDER`

```rsl
DL_ChangeDLORDER (ContractID:Integer, поле:String, значение:Variant):Bool
```

## Процедура: `DL_ChangeDLORDER`

```rsl
предназначена для изменения значений следующих полей договора, относящихся к векселю: · OnDeposit – фактическая дата сдачи векселя на хранение; · HandingDate – дата вручения векселя; · ContractStatus – статус договора. · DateOfPayment – фактическая дата оплаты договора.
```

## Процедура: `DL_CreateFiCert_Mortgage`

```rsl
DL_CreateFiCert_Mortgage (p_Mortgage:Trechandler, [p_MortObjArr:Tarray], [p_VsIrcAgArr:Tarray], [p_ErrStr:String]):Integer
```

## Процедура: `DL_CreateFiCert_Mortgage`

```rsl
предназначена для создания сертификата закладной. Процедура используется только вне контекста шагов операции.
```

**Параметры:**

p_Mortgage – рекорд записи таблицы dmortgage_dbt (Параметры закладной). После
успешного выполнения в поле t_MortgageID заносится идентификатор созданной
записи.
p_MortObjArr – рекорд или массив рекордов таблицы dmortobj_dbt (Предмет ипотеки
закладной).
p_VsIrcAgArr – рекорд или массив рекордов таблицы dvsircag_dbt (Агент обращения).
p_ErrStr – текст ошибки, если она возникла.

**Возвращаемое значение:**



## Процедура: `DL_CreatePmLinkByRQ`

```rsl
DL_CreatePmLinkByRQ (PARM_RQID:Integer, PaymID:Integer, Amount:Money, FIID:Integer):Integer
```

## Процедура: `DL_GetFicertAgents`

```rsl
DL_GetFicertAgents (CertID:Integer, AvoirKind:Integer, AgentRole:Integer, AgentsArray:TArray):Integer
```

## Процедура: `DL_InsertDLINACC`

```rsl
DL_InsertDLINACC (InnAcc:Record, DealCode:String):Bool
```

## Процедура: `DL_NPTX_InsertTaxObject`

```rsl
DL_NPTX_InsertTaxObject(Date:Date, Client:Number, Direction:Number, Level:Number, User:Char, Kind:Number, Sum:Money, Cur:Number, AnaliticKind1:Number, Analitic1:Number, AnaliticKind2:Number, Analitic2:Number, AnaliticKind3:Number, Analitic3:Number, AnaliticKind4:Number, Analitic4:Number, AnaliticKind5:Number, Analitic5:Number, AnaliticKind6:Number, Analitic6:Number, Comment:Varchar, DocID:Number, Step:Number)
```

## Процедура: `DL_NPTX_InsertTaxObjectWD`

```rsl
DL_NPTX_InsertTaxObjectWD(Date:Date, Client:Number, Direction:Number, Level:Number, User:Char, Kind:Number, Sum:Money, Cur:Number, AnaliticKind1:Number, Analitic1:Number, AnaliticKind2:Number, Analitic2:Number, AnaliticKind3:Number, Analitic3:Number, AnaliticKind4:Number, Analitic4:Number, AnaliticKind5:Number, Analitic5:Number, AnaliticKind6:Number, Analitic6:Number, Comment:Varchar, DocID:Number, Step:Number)
```

## Процедура: `DL_UpdAppDLINACC`

```rsl
DL_UpdAppDLINACC (ID:Integer, ApplicationKey:Integer, iApplicationKind:String):Bool
```

## Процедура: `List_GrTempl`

```rsl
List_GrTempl (DocLog:Integer, [DocKind:Integer, ] dlgrtBuff:Record):Integer
```

## Процедура: `ИзменитьУчтенныйВексель`

```rsl
ИзменитьУчтенныйВексель (BCID:Integer, поле:String, значение:Variant [, поле1:String] [, значение1:Variant]):Bool
```

## Класс: `TRsbDepoInfoMessage`

```rsl
TRsbDepoInfoMessage (ID: Integer): Integer
```

## Процедура: `DP_CrpFindSettAcc`

```rsl
DP_CrpFindSettAcc (IsTemp:Bool, OnDate:Date, RegisterID:Integer, HolderAccID:Integer, Issuer:Integer, Currency:Integer, IsBrokerAcc:Bool, SettAccID:Integer):Integer
```

## Процедура: `FindBillAgent`

```rsl
FindBillAgent (ErrStr:String, Id:Integer, agentprm:Record):Integer
```

## Процедура: `FindDepoAcc`

```rsl
FindDepoAcc (ErrStr:String, Id:Integer, dpacntprm:Record):Integer
```

## Процедура: `FindDepoFaceAcc`

```rsl
FindDepoFaceAcc (ErrStr:String, Acc:String, accountprm:Record):Integer
```

## Процедура: `FindDepoKeepingPlace`

```rsl
FindDepoKeepingPlace (ErrStr:String, Id:Integer, spplaceprm:Record):Integer
```

## Процедура: `FindInventoryCard`

```rsl
FindInventoryCard (ErrStr:String, Xid:String, invcprm:Record):Integer
```

## Процедура: `FindSPGroundDocument`

```rsl
FindSPGroundDocument (ErrStr:String, SPGroundID:Integer, Parm:Record):Integer
```

## Процедура: `GetDEPOADMO_Contents`

```rsl
GetDEPOADMO_Contents (depoadmo:Record, name:TArray, from:TArray, to:TArray, idfrom:TArray, idto:TArray):Integer
```

## Процедура: `ПолучитьПамДокПриложения`

```rsl
ПолучитьПамДокПриложения (IsFirst:Bool, SourceDocKind:Integer, SourceDocID:Integer, IsShowError:Bool, spground:Record):Bool
```

## Процедура: `DPListDepoAcc`

```rsl
DPListDepoAcc (Kind:Integer, Owner:Integer, Department:Integer, Parent:String [, AccBuf:Record]):Integer
```

## Процедура: `GetAccountByDepoAcc`

```rsl
GetAccountByDepoAcc (depoacAutoKey:Integer, IsPayer:Integer, spdraftall:Memaddr, TypeOp:Integer [, error:Integer] [. AddPrm:String, Tbfile] [, IsOverdraft:Bool]):String
```

## Процедура: `GetDepoPartition`

```rsl
GetDepoPartition (IsPayer:Integer, spdraftall:Memaddr, TypeOp:Integer [, error:Integer] [, KindAccOperation:Integer] [, IsOverdraft:Bool]):Integer
```

## Процедура: `GL_GetAccountByDepoAcc`

```rsl
GL_GetAccountByDepoAcc (depoacAutoKey:Integer, IsPayer:Integer, corpop:Memaddr, error:Integer) String С помощью процедуры выполняется поиск/открытие лицевого счета для счета/раздела ДЕПО в глобальных операциях.
```

**Параметры:**

depoacAutoKey – ссылка на счет депо.
IsPayer – сторона проводки:
- 1 – плательщик (Д);
- 0 – получатель (К).
corpop – адрес первичного документа.
error – статус ошибки.

**Возвращаемое значение:**



## Процедура: `InsertDepoAcc`

```rsl
InsertDepoAcc (ErrStr:String, Id:Integer, dpacntprm:Record [, dpatvlprm:Array]):Integer
```

## Процедура: `InsertDepoFaceAcc`

```rsl
InsertDepoFaceAcc (ErrStr:String, accountprm:Record [, dpsubaccprm:Array]):Integer
```

## Процедура: `InsertDepoPartition`

```rsl
InsertDepoPartition (dpacntprm:Record [, dpatvlprm:Array]):Integer
```

## Процедура: `ПолучитьТипСчетаПоНазначению`

```rsl
ПолучитьТипСчетаПоНазначению (Идентификатор счета депо: Integer, Тип счета депо по назначению: Integer): Integer
```

## Процедура: `CreateAdmOperation`

```rsl
CreateAdmOperation (Item:Integer, OperKind:Integer, PartyID:Integer, DepoAcc:Integer, DepoPart:Integer, FIID:Integer, Account:String, FileName:String, recbuf:Record, sbuff:Record [, OperDate:Date] [, Oper:Integer] [, Initiator:Integer] [, InitiatorCode:String] [, InitiatorName:String] [, SpgroundBuf:Record] [, SpgroundAdd:Tarray], CertifID:Integer):Integer
```

## Процедура: `CreateInfOperation`

```rsl
CreateInfOperation (InfOp:Record):Integer
```

## Процедура: `DP_SelectKindOper`

```rsl
DP_SelectKindOper (DocKind:Integer, DocKindMin:Integer, DocKindMax:Integer, Kind_Operation:Integer [, AutoReturnIfOne:Bool]):Bool
```

## Процедура: `DP_ColletPattern`

```rsl
DP_ColletPattern (PatternID:Integer):String
```

## Процедура: `DP_GetPatternByMask`

```rsl
DP_GetPatternByMask (Pattern:String, Mask:String):String
```

## Процедура: `DP_GetSuitablePattern`

```rsl
DP_GetSuitablePattern (Object:Integer, Codekind:Integer, Obj:File, Memaddr, Record, TBFile, TRecHandler [, FIID:Integer] [, Indoor:Integer] [, Issuer:Integer]):Integer
```

## Процедура: `CertGetNumberType`

```rsl
CertGetNumberType (Num:String):Integer
```

## Процедура: `InsertInventoryCard`

```rsl
InsertInventoryCard (ErrStr:String, Xid:String, invcprm:Record [, MoveID:Integer] [, arrCatGroups:TArray] [, arrCatAttrs:TArray]):Integer
```

## Процедура: `InsertProxy`

```rsl
InsertProxy (proxyprm:Record):Bool С помощью процедуры выполняется добавление представителя по договору для инвентарной карточки.
```

**Параметры:**

proxyprm – структура, содержащая данные для добавления представителя. В параметрах
структуры необходимо указать номер инвентарной карточки, роль представителя,
идентификатор представителя, данные для документа представителя.

**Возвращаемое значение:**



## Процедура: `DP_CloseDPACAP`

```rsl
DP_CloseDPACAP(APID:Integer, ToDate:Date, ErrStr:String):Integer
```

## Процедура: `DP_DeleteDPACAPAU`

```rsl
DP_DeleteDPACAPAU(APID:Integer, APNodeID:Integer, AuthKind:Integer, ErrStr:String):Integer
```

## Процедура: `DP_DeleteDPACAPFI`

```rsl
DP_DeleteDPACAPFI(APID:Integer, AcapFIPrm:Record, ErrStr:String):Integer
```

## Процедура: `DP_InsertDPACAP`

```rsl
DP_InsertDPACAP(AcapPrm:Record, AuthKindArr:TArray, AcapFIPrmArr:TArray, APID:Integer, ErrStr:String):Integer
```

## Процедура: `DP_InsertDPACAPAU`

```rsl
DP_InsertDPACAPAU(APID:Integer, APNodeID:Integer, AuthKind:Integer, ErrStr:String):Integer
```

## Процедура: `DP_InsertDPACAPFI`

```rsl
DP_InsertDPACAPFI(APID:Integer, AcapFIPrm:Record, ErrStr:String):Integer
```

## Процедура: `BlockDobookField`

```rsl
BlockDobookField (Номер_Поля:Integer):Integer
```

## Процедура: `CheckExpSecurAble`

```rsl
CheckExpSecurAble (spdraft:Record, pm_paym:Record):Bool
```

## Процедура: `CheckExpSecurAble`

```rsl
предназначена для проверки возможности экспорта поручения депо в подсистему "Бэк-офис операций с ценными бумагами". Экспорт будет осуществляться в следующих случаях: · если установлена подсистема "Бэк-офис операций с ценными бумагами"; · если поручение не импортировано из подсистемы "Бэк-офис операций с ценными бумагами"; · если установлен признак в поручении; · для счета отправителя в междепозитарном списании; · для счета в зачислении бездокументарных ценных бумаг; · для тех пассивных счетов во внутридепозитарном переводе, у которых владелец является клиентом фондового дилинга и существует договор обслуживания клиента с банком.
```

**Параметры:**

spdraft – структура, соответствующая структуре таблицы базы данных dspdraft_dbt.
pm_paym – структура, соответствующая структуре таблицы базы данных dpmpaym_dbt.

**Возвращаемое значение:**



## Процедура: `DP_AddLoroOwnToRegline`

```rsl
DP_AddLoroOwnToRegline (IsTemp:Bool, ReglineID:Long, lo:Record):Integer
```

## Процедура: `DP_AddDPGRREP`

```rsl
DP_AddDPGRREP (Desc:Integer, Party:Integer, SourceDocKind:Integer, SourceDocID:Integer, DeliveryKind:Integer, AutoSendReport:Bool):Integer
```

## Процедура: `DP_ChangePMACCState`

```rsl
DP_ChangePMACCState (DocumentID:Integer, HolderAccID:Integer, NewState:Integer, NewStateDate:Date, EditDescription:Bool):Bool
```

## Процедура: `DpKvitOneMessage`

```rsl
DpKvitOneMessage (add_mes:Record, orig_mes:Record):Integer
```

## Процедура: `DpMessageConfirm`

```rsl
DpMessageConfirm (DraftID:Integer):Integer
```

## Процедура: `GL_GetDepoPartition`

```rsl
GL_GetDepoPartition (IsPayer:Integer, corpop:Memaddr, error:Integer):Integer С помощью процедуры выполняется поиск и открытие разделов по глобальным операциям.
```

**Параметры:**

IsPayer – сторона проводки:
- DP_OPRACC_PAYER – плательщик;
- DP_OPRACC_RECEIVER – получатель.
corpop – указатель на первичный документ.
error – статус ошибки.

**Возвращаемое значение:**



## Процедура: `InsertBillAgent`

```rsl
InsertBillAgent (ErrStr:String, agentprm:Record):Integer
```

## Процедура: `InsertCertMove`

```rsl
InsertCertMove (ErrStr:String, certprm:Record):Integer
```

## Процедура: `InsertDeferDraft`

```rsl
InsertDeferDraft (ErrStr:String, drafrprm:Record, pm_paym:Record):Integer
```

## Процедура: `InsertDepoKeepingPlace`

```rsl
InsertDepoKeepingPlace (ErrStr:String, Id:Integer, spplaceprm:Record):Integer
```

## Процедура: `InsertGroundDocument`

```rsl
InsertGroundDocument (ErrStr:String, Id:Integer, Parm:Record):Integer
```

## Процедура: `SendDepoMessage`

```rsl
SendDepoMessage (MessageID:Integer):Integer
```

## Процедура: `DV_FillPayments`

```rsl
DV_FillPayments (DocKind:Integer, DocumentID:Integer, Oper:Record, Paym:Record, [ptr_deb:Record, ] [ptr_crd:Record, ] [ptr_rm:Record, ] PMGround:String [, no_auto:Bool] [,error:String]):Integer
```

## Процедура: `DV_InitSPDeal`

```rsl
DV_InitSPDeal (tick:Record, KindDoc:Integer, KindOper:Integer [, FullInit:Bool]):Bool
```

## Процедура: `DV_TickCost`

```rsl
DV_TickCost (FIID:Integer, Date:Date):Double
```

## Процедура: `DVDealGateCreateNew`

```rsl
DVDealGateCreateNew (dvdeal:Record, SPGRDOCID:Integer, CALCOPKIND:Integer, CALCOPCODE:String, PARTYID:Integer):Integer
```

## Процедура: `вставляет`

```rsl
в подсистему "Бэк-офис операций с ценными бумагами" сделку и операцию расчетов с производными инструментами при импорте из Шлюза.
```

**Параметры:**

dvdeal – буфер сделки с производными инструментами (ddvdeal_dbt).
SPGRDOCID – идентификатор подтверждающего документа по сделке.
CALCOPKIND – вид операции расчетов по сделке с производными инструментами.
CALCOPCODE – код операции расчетов по производным инструментам.
PARTYID – идентификатор контрагента по сделке.

**Возвращаемое значение:**



## Процедура: `DVFiTurnGateCreateNew`

```rsl
DVFiTurnGateCreateNew (dvturn:Record, CALCOPKIND:Integer, CALCOPCODE:String, PARTYID:Integer):Integer
```

## Процедура: `ПолучитьПервичныйДокументСервОперПИ`

```rsl
ПолучитьПервичныйДокументСервОперПИ (OprOper:Record, FDoc1:File, Record, TRecHandler):Integer
```

## Класс: `RsbConvDeal`

```rsl
RsbConvDeal ([PaymentID: Integer]): Object
```

## Класс: `RsbForexDealsFilter`

```rsl
RsbForexDealsFilter (): Object
```

## Класс: `RsbSwapDeal`

```rsl
RsbSwapDeal ([PaymentID: Integer]): Object
```

## Процедура: `FX_InsertDLRESLNK`

```rsl
FX_InsertDLRESLNK (rlnk:Record):Bool
```

## Процедура: `MM_ChangeDealTerm`

```rsl
MM_ChangeDealTerm(tick, leg, operdate:Date)
```

## Процедура: `MM_ChangeUsed`

```rsl
MM_ChangeUsed (ContractID:Integer, FIIN:Integer, SecProp:Integer, Used:Integer):Bool
```

## Процедура: `MM_ChechCorrectRetSecur`

```rsl
MM_ChechCorrectRetSecur (ContractID:Integer):Bool
```

## Процедура: `MM_CheckCorrectHungSecur`

```rsl
MM_CheckCorrectHungSecur (ContractID:Integer):Bool
```

## Процедура: `MM_DealExecuteStep`

```rsl
MM_DealExecuteStep(DealID:Integer, StepSymb:String):Integer
```

## Процедура: `MM_DefineOriginalID`

```rsl
MM_DefineOriginalID (DealID:Integer):Integer
```

## Процедура: `MM_GetAutoPerc`

```rsl
MM_GetAutoPerc (DealID: Integer, LegID: Integer, ObjType: Integer):Integer
```

## Процедура: `MM_InsertDLRESLNK`

```rsl
MM_InsertDLRESLNK (rlnk:Record):Bool
```

## Процедура: `MM_InsertPayment`

```rsl
MM_InsertPayment (pm:Record, d:Record, k:Record, rm:Record):Bool
```

## Процедура: `MM_PcMakeUpRestListForAccount`

```rsl
MM_PcMakeUpRestListForAccount (pDB:Date, pDE:Date, accID:Integer, objType:Integer, Account:String):Record
```

## Процедура: `РассчитатьПроценты`

```rsl
РассчитатьПроценты (DealID: Integer, LegID: Integer [, DC: Date] [, DR: Date] [, mode: Integer]): Bool
```

## Процедура: `СоздатьСообщение`

```rsl
СоздатьСообщение (type:Integer, tick:Record, leg:Record):Bool
```

## Процедура: `AccountDepo_FindClose`

```rsl
AccountDepo_FindClose (): Integer
```

## Процедура: `AccountDepo_FindFirst`

```rsl
AccountDepo_FindFirst (Depoaccid:Integer, CodeL:String, NumL:String, Account$:Record)
```

## Процедура: `AccountDepo_FindNext`

```rsl
AccountDepo_FindNext (Account$:Record): Integer
```

## Процедура: `DepoAcc_FindClose`

```rsl
DepoAcc_FindClose ();
```

## Процедура: `DepoAcc_FindFirst`

```rsl
DepoAcc_FindFirst (Depoacnt:Record): Integer
```

## Процедура: `DepoAcc_FindNext`

```rsl
DepoAcc_FindNext (Depoacnt:Record): Integer
```

## Процедура: `GetDepoAcc`

```rsl
GetDepoAcc (Code:String, DepoAcnt:Record): Integer
```

## Процедура: `GetDepoByAccName`

```rsl
GetDepoByAccName (Acc:String, CodeCur:Integer, Chapter:Integer, DepoCode:String, DepoName:String)
```

## Процедура: `DepoSubAcc_FindClose`

```rsl
DepoSubAcc_FindClose ():Variant
```

## Процедура: `DepoSubAcc_FindFirst`

```rsl
DepoSubAcc_FindFirst (Depoacnt:Record, Account$:Record): Integer
```

## Процедура: `DepoSubAcc_FindNext`

```rsl
DepoSubAcc_FindNext (Account$:Record): Integer
```

## Процедура: `SP_BuyForPeriod`

```rsl
SP_BuyForPeriod (CalcWrt:Record, Department:Integer, Party:Integer, FIID:Integer, TypePort:Integer [, DateBegin:Date] [, DateEnd:Date] [, IsORCB:Bool] [, Delivered:Bool]):Bool
```

## Процедура: `SP_RestOnDate`

```rsl
SP_RestOnDate (CalcWrt:Record, Department:Integer, FIID:Integer, Party:Integer, TypePort:Integer, Date:Date [, IsORCB:Bool] [, Delivered:Bool]):Bool
```

## Процедура: `SP_SaleForPeriod`

```rsl
SP_SaleForPeriod (CalcWrt:Record, Department:Integer, Party:Integer, FIID:Integer, TypePort:Integer, DateBegin:Date, DateEnd:Date [, IsORCB:Bool]):Bool
```

## Процедура: `SP_SaleForPeriod`

```rsl
предназначена для поиска сумм лотов по проданным за период ценным бумагам. Выполнение процедуры производится по следующему алгоритму: · Осуществляется поиск лотов продажи по портфелю бумаг TypePort с заданным FIID для субъекта Party, дата поставки которых попадает в интервал DateBegin–DateEnd. · Для каждого лота отбираются ссылки pmwrtlink, связывающие их с лотами покупки, при этом сделка, по которой лот приобретался (по ссылке из лота) соответствует режиму IsORCB. · Суммы по pmwrtlink возвращаются в CalcWrt.
```

**Параметры:**

CalcWrt – структура pmwrtsum, в поля которой заносятся подсчитанные значения
(BalanceCost, Amount, NKD_Amount, Sum).
Department – номер филиала.
Party – идентификатор субъекта-клиента. Значение "-1" означает поиск по собственным
сделкам "Нашего Банка".
FIID – идентификатор финансового инструмента.
TypePort – вид портфеля. Возможные значения:
- KINDPORT_CLIENT – клиентский портфель.
- KINDPORT_TRADE – торговый портфель.
- KINDPORT_SALE – портфель ценных бумаг для продажи.
- KINDPORT_CONTR – портфель контрольного участия.
- KINDPORT_PROMISSORY – просроченные долговые обязательства.
- KINDPORT_RETIRE – портфель долговых обязательств, удерживаемых до
погашения.
- KINDPORT_BACK – портфель ценных бумаг, полученных на возвратной
основе.
- KINDPORT_TRUST – портфель доверительного управления.
- KINDPORT_BASICDEBT – основной долг.
- KINDPORT_UNDEF (-1) – по всем портфелям.
DateBegin – дата начала периода.
DateEnd – дата завершения периода.
IsORCB – признак фильтрации. Параметр может принимать следующие значения:
- TRUE – только сделки на ОРЦБ.
- FALSE – только сделки не на ОРЦБ.
- NULL – любые сделки.

**Возвращаемое значение:**



## Процедура: `SP_GetSfContrID`

```rsl
SP_GetSfContrID (deal:Record, ContrID:Integer):Bool
```

## Процедура: `SP_GetSfContrIDbyPartyID`

```rsl
SP_GetSfContrIDbyPartyID (CheckDate:Date, PartyID:Integer, ContrID:Integer):Bool
```

## Процедура: `FillPaymentsByDeal`

```rsl
FillPaymentsByDeal (dl_tick:Record, Paym:Record [, debet:Record] [, credit:Record] [, pmrmprop:Record] [, pmdpprop:Record] [, no_auto:Bool] [, error:String]):Integer
```

## Процедура: `FillPaymentsByDL_COMM`

```rsl
FillPaymentsByDL_COMM (DocKind:Integer, DocumentID:Integer, dl_comm:Record, Paym:Record, [debet:Record, ] [credit:Record, ] [pmrmprop:Record, ] Ground:String [, No_Auto:Bool] [, error:String]):Integer
```

## Процедура: `InitSPDeal`

```rsl
InitSPDeal (tick:Record, KindDoc:Integer, KindOper:Integer [, FullInit:Bool]):Bool
```

## Процедура: `SP_CreateDeal`

```rsl
SP_CreateDeal(dl_tick:Record, dl_leg:Record, dl_leg2:Record, AvanceSum:Record, DepositSum:Record, AvanceSum2:Record, DepositSum2:Record, stat:Number, RetireLnk:Record):Number
```

## Процедура: `SP_DealGateCreateNew`

```rsl
SP_DealGateCreateNew (tick:Record, dl_leg1:Record, dl_leg2:Record, spgr1:Record, spgr2:Record, paym_base1:Record, debet_base1:Record, credit_base1:Record, paym_contr1:Record, debet_contr1:Record, credit_contr1:Record, paym_avance1:Record, debet_avance1:Record, credit_avance1:Record, paym_base2:Record, debet_base2:Record, credit_base2:Record, paym_contr2:Record, debet_contr2:Record, credit_contr2:Record, paym_avance2:Record, debet_avance2:Record, credit_avance2:Record, paym_percent:Record, debet_percent:Record, credit_percent:Record, ClntRep:Record, outlay:Record, dlsumAgentCom:Record, dlsumBankCom:Record, spgrdoc:Record):Integer
```

## Процедура: `SP_DealNeedReserv`

```rsl
SP_DealNeedReserv (KindReserv:Integer, ServOpBuf:Record, TickBuf:Record):Bool
```

## Процедура: `SP_Deals_Edit_Record`

```rsl
SP_Deals_Edit_Record(Mode:Integer):Bool
```

## Процедура: `SP_DelDealWithLinks`

```rsl
SP_DelDealWithLinks (DealID:Integer [, ErrMes:Bool]):Integer
```

## Процедура: `SP_GetDealParmsByDate`

```rsl
SP_GetDealParmsByDate (Deal:Record, Date:Date, DealChange:Record)
```

## Процедура: `SP_InsertSPTKCHNG`

```rsl
SP_InsertSPTKCHNG (Date:Date, Kind:Integer, Tick:Record [, Leg1:Record] [, Leg2:Record] [, UpdateOnlyDeal:Bool]):Integer
```

## Процедура: `SP_NtgNeedReservReq`

```rsl
SP_NtgNeedReservReq (ServOpBuf:Record, TickBuf:Record):Integer
```

## Процедура: `SP_PaymIsSale`

```rsl
SP_PaymIsSale (Paym:Record, Deal:Record):Bool
```

## Процедура: `SP_RecalcNKDAndPrice`

```rsl
SP_RecalcNKDAndPrice (tick:Record, dl_leg:Record, ValueDate:Date, IsImport:Bool):Integer
```

## Процедура: `ПолучитьЦеновыеУсловияСделки`

```rsl
ПолучитьЦеновыеУсловияСделки (Tick:Record, Date:Date, ByPart2:Bool [, Price:DoubleL] [, Cost:MoneyL] [, NKD:MoneyL] [, TotalCost:MoneyL]):Bool
```

## Процедура: `НКД`

```rsl
НКД (FIID:Integer, amount:Moneyl, date:Date [, err:Integer] [, IsTrust:Bool] [, AskQuest:Bool], ConsiderCompulsorily:Bool [ExCourse:Bool] [, CorrectDate:Bool]):Moneyl
```

## Процедура: `НКД`

```rsl
предназначена для вычисления величины НКД (накопленного купонного дохода) по стандартной формуле для заданного количества заданной ценной бумаги на заданную дату. При этом учитывается то, что если момент расчета совпадает с датой погашения текущего купона, то НКД нулевой.
```

## Процедура: `ПолучитьНКДЗаПериод`

```rsl
ПолучитьНКДЗаПериод (FIID:Integer, amount:MoneyL, begdate:Date, enddate:Date [, OnlyWholeCoup:Bool] [, OnlyClosedCoup:Bool] [, err:Integer]):MoneyL
```

## Процедура: `СуммаКупона`

```rsl
СуммаКупона (FIID:Integer, amount:MoneyL, date:Date [, err:Integer]):MoneyL
```

## Процедура: `GetDocKind`

```rsl
GetDocKind (document:Record, err:Integer):Integer
```

## Процедура: `SC_NeedCalcCom`

```rsl
SC_NeedCalcCom (p_sfContrID:Integer, p_sfComNumber: Integer, p_dateCalc:Date, [p_GroupID:Integer], [p_NumInList:String]):Bool
```

## Процедура: `SP_AddReservForPaym`

```rsl
SP_AddReservForPaym (paym:Record, Reserv:MoneyL, Date:Date):Bool
```

## Процедура: `SP_CalcForREPO`

```rsl
SP_CalcForREPO (dl_leg:Record, dl_leg:Record, BaseDate1:Record, BaseDate2:Record):Variant
```

## Процедура: `SP_DealNeedOverValueNVPI`

```rsl
SP_DealNeedOverValueNVPI (Date:Date, tick:File, Record, Tbfile, Trechandler):Integer
```

## Процедура: `SP_FindDocument`

```rsl
SP_FindDocument (DocKind: Integer, DocCode: String[, Date: Date]): Integer
```

## Процедура: `SP_GetClientAccount`

```rsl
SP_GetClientAccount (ticket:Record, ClientID:Integer, FIIDAccount:Integer, paym:Record, prop:Record, Account:String):Integer
```

## Процедура: `SP_GetLotKind`

```rsl
SP_GetLotKind (Group:Long, IsBack:Bool):Integer
```

## Процедура: `SP_GetNominal`

```rsl
SP_GetNominal (FIID:Integer, [Date:Date, ] Nominal:Double):Bool
```

## Процедура: `SP_GetPercentAccount`

```rsl
SP_GetPercentAccount (Deal:Record):Long
```

## Процедура: `SP_GetPercentSum`

```rsl
SP_GetPercentSum ([PmAvance1:Record, ] PmMoney1:Record, [PmAvance2:Record, ] PmMoney2:Record, Dl_Leg1:Record, Dl_Leg2:Record, OperGroup:Long, CalcDate:Date [, OnlyFactPayms:Bool]):Money
```

## Процедура: `SP_InsertBoardLot`

```rsl
SP_InsertBoardLot (Data:Record, TRecHandler [, BoardID:Integer] [, ShowError:Bool]):Bool
```

## Процедура: `может`

```rsl
вызываться как на шагах, так и вне шагов операции. В случае вызова на шаге операции происходит автоматический откат вставленной операции зачисления/списания при откате шага.
```

**Параметры:**

Data – данные для вставки операции зачисления/списания (структура dboardprm.rec).
BoardID – идентификатор операции при успешном добавлении. Заполняется только при
вызове процедуры не на шаге операции.
ShowError – признак вывода на экран ошибок. По умолчанию параметр принимает
значение TRUE.

**Возвращаемое значение:**



## Процедура: `SP_ListSCTXDEAL`

```rsl
SP_ListSCTXDEAL ([Cond:String, ] [Type:Long, ] [AvoirKind:Long, ] [FIID:Long]):Long
```

## Процедура: `SP_NtgNeedOvervalueNVPI`

```rsl
SP_NtgNeedOvervalueNVPI (date:Date, deal:File, Record, Tbfile, Trechandler):Integer
```

## Процедура: `SP_RepCalcOpGateCreateNew`

```rsl
SP_RepCalcOpGateCreateNew (spgr:Record, oprid:Long):Integer
```

## Процедура: `SP_RepExchangeGateCreateNew`

```rsl
SP_RepExchangeGateCreateNew (spgr:Record):Integer
```

## Процедура: `SP_RepoNeedOverValueNVPI`

```rsl
SP_RepoNeedOverValueNVPI (Date :Date, tick:File, Record, Tbfile, Trechandler):Integer
```

## Процедура: `WRTRejectDeal`

```rsl
WRTRejectDeal (SumID:Long, OperDate:Date, Portfolio:Integer, GroupID:Integer, Amount:Money, Sum:Money, Currency:Long, Cost:Money, NKD:Money, BegDiscount:Money, BegBonus:Money, ID_Operation:Long, ID_Step:Integer):Bool
```

## Процедура: `ПолучитьПервичныйДокументСервОпер`

```rsl
ПолучитьПервичныйДокументСервОпер (oproper:Record, FDoc1:Record [, FDoc2:Record]):Integer
```

## Процедура: `TS_ChangeDemand`

```rsl
TS_ChangeDemand (PARM_CHANGED_REC:File, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_ChangeProfit`

```rsl
TS_ChangeProfit (PARM_CHANGED_REC:File, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_ChangeTotal`

```rsl
TS_ChangeTotal (PARM_CHANGED_REC:File, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_ChangeTotalHistory`

```rsl
TS_ChangeTotalHistory (PARM_CHANGED_REC:File, Record, TBFile, TRecHandler):Integer
```

## Процедура: `TS_ChangeValid`

```rsl
TS_ChangeValid (PARM_ORDER:File, Record, TBfile, TRecHandler, PARM_VALID:File, Record, TBfile, TRecHandler, PARM_SHOWEDITPANEL:Integer):Integer
```

## Процедура: `TS_CreateDemandFromOtherBO`

```rsl
TS_CreateDemandFromOtherBO (PARM_SFCONTRID:Integer, PARM_ACTIVECODE:String, PARM_ACTIVEFIID:Integer, PARM_DEPOSITORYID:Integer, PARM_CURID:Integer, PARM_ACTIVEACCOUNT:String, PARM_OPERID:Integer, PARM_RECDEMAND:File, Record, TBfile, TRecHandler, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется создание требования/обязательства из стороннего бэк-офиса.
```

**Параметры:**

PARM_SFCONTRID – идентификатор контрагента.
PARM_ACTIVECODE – код актива.
PARM_ACTIVEFIID – идентификатор финансового инструмента (поле t_FIID таблицы
dtsactive_dbt).
PARM_DEPOSITORYID – идентификатор хранилища (поле t_DepositoryID таблицы
dtsactive_dbt).
PARM_CURID – текущий идентификатор.
PARM_ACTIVEACCOUNT – счет актива.
PARM_OPERID – идентификатор операции.
PARM_RECDEMAND – определитель объекта (структура, соответствующая структуре
таблицы dtsdemand_dbt).
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_DiscardDemandByID`

```rsl
TS_DiscardDemandByID (PARM_ID:Integer, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется списание требования/обязательства, т.е. его закрытие без изменения остатка актива. В качестве идентификатора требования/обязательства в процедуре используется значение первичного ключа ADemandID.
```

**Параметры:**

PARM_ID – идентификатор требования/обязательства ADemandID.
PARM_DATE – дата списания ADiscardDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_DiscardDemandByMark`

```rsl
TS_DiscardDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:Integer, String, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется списание требования/обязательства, т.е. его закрытие без изменения остатка актива. В качестве идентификатора требования/обязательства в процедуре используется значение альтернативного ключа {ABOfficeKind, AID_Operation, AUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND – вид бэк-офиса ABOfficeKind.
PARM_ID_OPERATION – идентификатор операции AID_Operation.
PARM_USERMARK – метка AUserMark.
PARM_DATE – дата списания ADiscardDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_ExecuteDemandByID`

```rsl
TS_ExecuteDemandByID (PARM_ID:Integer, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется исполнение требования/обязательства, т.е. его закрытие с изменением остатка актива. В качестве идентификатора требования/обязательства в процедуре используется значение первичного ключа ADemandID.
```

**Параметры:**

PARM_ID – идентификатор требования/обязательства ADemandID.
PARM_DATE – дата исполнения требования/обязательства AExecDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_ExecuteDemandByMark`

```rsl
TS_ExecuteDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется исполнение требования/обязательства, т.е. его закрытие с изменением остатка актива. В качестве идентификатора требования/обязательства в процедуре используется значение альтернативного ключа {ABOfficeKind, AID_Operation, AUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND – вид бэк-офиса ABOfficeKind.
PARM_ID_OPERATION – идентификатор операции AID_Operation.
PARM_USERMARK – метка AUserMark.
PARM_DATE – дата исполнения требования/обязательства.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_GetActivePlanByCode`

```rsl
TS_GetActivePlanByCode (PARM_CODE:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetActivePlanByFI`

```rsl
TS_GetActivePlanByFI (PARM_FIID:Integer, PARM_PARTY_ID:Integer, PARM_ORDER_ID:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetActivePlanByID`

```rsl
TS_GetActivePlanByID (PARM_ID:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetActiveRestByCode`

```rsl
TS_GetActiveRestByCode (PARM_CODE:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetActiveRestByFI`

```rsl
TS_GetActiveRestByFI (PARM_FIID:Integer, PARM_PARTY_ID:Integer, PARM_ORDER_ID:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetActiveRestByID`

```rsl
TS_GetActiveRestByID (PARM_ID:Integer, PARM_DATE:Date, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_CancelDemandByID`

```rsl
TS_CancelDemandByID (PARM_ID:Integer, PARM_TYPE:Integer, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется откат всех действий, произведенных по требованию/обязательства, и перевод требования/обязательства в запланированное или незапланированное состояние.
```

## Процедура: `TS_CancelDemandByMark`

```rsl
TS_CancelDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_TYPE:Integer, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется откат всех действий, произведенных по требованию/обязательству, и требования/обязательства в запланированное или незапланированное состояние.
```

## Процедура: `TS_GetDemandExecutionByID`

```rsl
TS_GetDemandExecutionByID (PARM_ID:Integer, PARM_QUANTITY:MONEY, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_GetDemandExecutionByMark`

```rsl
TS_GetDemandExecutionByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_SHOWERROR:Integer):Integer
```

## Процедура: `TS_MutualPayOffDemandByID`

```rsl
TS_MutualPayOffDemandByID (PARM_ID:Integer, PARM_LIABILITYID:Integer, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется взаимное погашение требования и обязательства. В качестве идентификатора требования/обязательства в процедуре используется значение первичного ключа ADemandID и ALiabilityID.
```

**Параметры:**

PARM_ID – идентификатор погашаемого требования/обязательства ADemandID.
PARM_LIABILITYID – идентификатор гасящего требования/обязательства ALiabilityID.
PARM_QUANTITY – количество взаимного погашения AQuantity. Количество взаимного
погашения должно быть равно его сумме.
PARM_AMOUNT – сумма взаимного погашения AAmount. Валюта суммы должна
совпадать с валютой требования и обязательства.
PARM_DATE – дата исполнения AExecDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_MutualPayOffDemandByMark`

```rsl
TS_MutualPayOffDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_LIABILITY_BOFFICEKIND:Integer, PARM_LIABILITY_ID_OPERATION:Integer, PARM_LIABILITY_USERMARK:String, PARM_QUANTITY:Money, PARM_AMOUNT:Money, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется взаимное погашение требования и обязательства. В качестве идентификатора требования/обязательства в процедуре используется значение альтернативного ключа {ADemBOfficeKind, ADemID_Operation, ADemUserMark} и {ALiaBOfficeKind, ALiaID_Operation, ALiaUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND 
- 
идентификатор 
вида 
бэк-офиса 
погашаемого
требования/обязательства ADemBOfficeKind.
PARM_ID_OPERATION 
- 
идентификатор 
операции 
погашаемого
требования/обязательства ADemID_Operation.
PARM_USERMARK – метка погашаемого требования/обязательства ADemUserMark.
PARM_LIABILITY_BOFFICEKIND 
- 
идентификатор 
вида 
бэк-офиса 
гасящего
требования/обязательства ALiaBOfficeKind.
PARM_LIABILITY_ID_OPERATION 
- 
идентификатор 
операции 
гасящего
требования/обязательства ALiaID_Operation.
PARM_LIABILITY_USERMARK – метка гасящего требования/обязательства AliaMark.
PARM_QUANTITY – количество взаимного погашения AQuantity. Количество взаимного
погашения должно быть равно его сумме.
PARM_AMOUNT – сумма взаимного погашения AAmount. Валюта суммы должна
совпадать с валютой требования и обязательства.
PARM_DATE – дата исполнения AExecDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_PartlyDiscardDemandByID`

```rsl
TS_PartlyDiscardDemandByID(PARM_ID:Integer, PARM_DATE:Date, PARM_AMOUNT:Money, PARM_QUANTITY:Money [, PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_PartlyDiscardDemandByMark`

```rsl
TS_PartlyDiscardDemandByMark(PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:Integer, String, PARM_DATE:Date, PARM_AMOUNT:Money, PARM_QUANTITY:Money [PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_RemoveDemandByID`

```rsl
TS_RemoveDemandByID (PARM_ID:Integer, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется удаление требования/обязательства из базы данных. Использование процедуры возможно, если требование/обязательство еще не запланировано. В качестве идентификатора требования/обязательства использует значение первичного ключа ADemandID.
```

**Параметры:**

PARM_ID – идентификатор требования/обязательства ADemandID.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_RemoveDemandByMark`

```rsl
TS_RemoveDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется удаление требования/обязательства из базы данных. Использование процедуры возможно, если требование/обязательство еще не запланировано. В качестве идентификатора требования/обязательства в процедуре используется значение альтернативного ключа {ABOfficeKind, AID_Operation, AUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND – идентификатор вида бэк-офиса требования/обязательства
ABOfficeKind.
PARM_ID_OPERATION 
- 
идентификатор 
операции 
требования/обязательства
AID_Operation.
PARM_USERMARK – метка требования/обязательства AUserMark.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_TransferDemandByID`

```rsl
TS_TransferDemandByID (PARM_ID:Integer, PARM_TRANSFER_ID:Integer, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется перенесение требования/обязательства, т.е. закрытие текущего требования/обязательства путем увеличения объема и суммы уже существующего требования/обязательства на всю сумму переносимого. В качестве идентификатора требования/обязательства в процедуре используется значение первичного ключа ADemandID и ATransferDemandID.
```

**Параметры:**

PARM_ID – идентификатор погашаемого требования/обязательства ADemandID.
PARM_TRANSFER_ID 
- 
идентификатор 
гасящего 
требования/обязательства
ATransferDemandID.
PARM_DATE – дата исполнения AExecDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_TransferDemandByMark`

```rsl
TS_TransferDemandByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_TRANSFER_BOFFICEKIND:Integer, PARM_TRANSFER_ID_OPERATION:Integer, PARM_TRANSFER_USERMARK:String, PARM_DATE:Date, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется перенесение требования/обязательства, т.е. закрытие текущего требования/обязательства путем увеличения объема и суммы уже существующего на всю сумму переносимого. В качестве идентификатора требования/обязательства в процедуре используется значение альтернативного ключа {ABOfficeKind, AID_Operation, AUserMark} и {ATransferBOfficeKind, ATransferID_Operation, ATransferUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND 
- 
идентификатор 
вида 
бэк-офиса 
погашаемого
требования/обязательства ABOfficeKind.
PARM_ID_OPERATION 
- 
идентификатор 
операции 
погашаемого
требования/обязательства AID_Operation.
PARM_USERMARK – метка погашаемого требования/обязательства AUserMark.
PARM_TRANSFER_BOFFICEKIND 
- 
идентификатор 
вида 
бэк-офиса 
гасящего
требования/обязательства ATransferBOfficeKind.
PARM_TRANSFER_ID_OPERATION 
- 
идентификатор 
операции 
гасящего
требования/обязательства AOffsetID_Operation.
PARM_TRANSFER_USERMARK 
- 
метка 
гасящего 
требования/обязательства
ATransferMark.
PARM_DATE – дата исполнения AExecDate.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_ExecutePlanProfitByID`

```rsl
TS_ExecutePlanProfitByID (PARM_ID:Integer, PARM_DATE:Date [, PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_ExecutePlanProfitByMark`

```rsl
TS_ExecutePlanProfitByMark (PARM_BOFFICEKIND:Integer, String, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_DATE Date, [PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_RealizeProfitByID`

```rsl
TS_RealizeProfitByID (PARM_ID:Integer, PARM_DATE:Date, PARM_SUMMA:Money, PARM_QUANTITY:Money [, PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_RealizeProfitByMark`

```rsl
TS_RealizeProfitByMark (PARM_BOFFICEKIND:Integer, String, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_DATE:Date, PARM_SUMMA:Money, PARM_QUANTITY:Money [, PARM_SHOWERROR:Integer]):Integer
```

## Процедура: `TS_RemoveProfitByID`

```rsl
TS_RemoveProfitByID (PARM_ID:Integer, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется удаление дохода/расхода из базы данных. В качестве идентификатора дохода/расхода в процедуре используется значение первичного ключа AProfitID.
```

**Параметры:**

PARM_ID – идентификатор дохода/расхода AProfitID.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_RemoveProfitByMark`

```rsl
TS_RemoveProfitByMark (PARM_BOFFICEKIND:Integer, PARM_ID_OPERATION:Integer, PARM_USERMARK:String, PARM_SHOWERROR:Integer):Integer С помощью процедуры выполняется удаление дохода/расхода из базы данных. В качестве идентификатора дохода/расхода в процедуре используется значение альтернативного ключа {ABOfficeKind, AID_Operation, AUserMark}.
```

**Параметры:**

PARM_BOFFICEKIND – идентификатор вида бэк-офиса ABOfficeKind.
PARM_ID_OPERATION – идентификатор операции AID_Operation.
PARM_USERMARK – метка AUserMark.
PARM_SHOWERROR – признак вывода кода ошибки.

**Возвращаемое значение:**



## Процедура: `TS_CalculateCommiss`

```rsl
TS_CalculateCommiss (PARM_CONTR_ID:Integer, PARM_GROUP_KIND:String, PARM_CALC_DATE:Date, PARM_SUMMA:Money, PARM_NDS:Money, PARM_FIID:Integer):Integer
```

## Процедура: `TS_GenerateActiveCode`

```rsl
TS_GenerateActiveCode (PARM_TSACTIVE:File, Record, TBfile, TRecHandler, PARM_ACTIVECODE:String)
```

## Процедура: `TS_GetCurrentInvDec`

```rsl
TS_GetCurrentInvDec (PARM_ORDERID:Integer, PARM_DATE:Date, PARM_INVDECL:File, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_GetCurrentMngPlan`

```rsl
TS_GetCurrentMngPlan (PARM_ORDERID:Integer, PARM_DATE:Date, PARM_MNGPLN:File, Money, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_GetCurrentValid`

```rsl
TS_GetCurrentValid (PARM_ORDERID:Integer, PARM_DATE:Date, PARM_VALID:File, Record, TBfile, TRecHandler):Integer
```

## Процедура: `TS_GetDateAfterPeriod`

```rsl
TS_GetDateAfterPeriod (PARM_BEGINDATE:Date, PARM_PERIOD:Integer, PARM_PERIOD_KIND:Integer):Date С помощью процедуры рассчитывается дата, наступающая спустя заданный период от указанной даты.
```

**Параметры:**

PARM_BEGINDATE – начальная дата.
PARM_PERIOD – период.
PARM_PERIOD_KIND – вид периода.

**Возвращаемое значение:**



## Процедура: `TS_OvervaluePositionDV`

```rsl
TS_OvervaluePositionDV (PARM_OPERID:Integer, PARM_POSID:Integer, PARM_DATE:Date, PARM_OVERVALUESUM:Money, PARM_RATE:Double, PARM_NEWLONG:Money, PARM_NEWSHORT:Money):Integer
```

## Процедура: `TS_RunFromServiceOper`

```rsl
TS_RunFromServiceOper (PARM_SERVOP:File, Record, TBfile, TRecHandler):Bool
```

## Процедура: `TS_SetOrderCloseDate`

```rsl
TS_SetOrderCloseDate (PARM_ORDERID:Integer, PARM_CLOSEDATE:Date):Integer
```

## Процедура: `TS_SvOpInsertMessageToLog`

```rsl
TS_SvOpInsertMessageToLog (PARM_MESSAGE:String)
```

С помощью процедуры выполняется вставка сообщения в лог-файл сервисных операций.
Параметр:
PARM_MESSAGE – добавляемое сообщение.

## Процедура: `WRTAmortizeOvervalueSum`

```rsl
WRTAmortizeOvervalueSum (PARM_OperDate:Date, PARM_FIID:Integer, PARM_Department:Integer, PARM_ID_Operation:Integer, PARM_ID_Step:Integer, PARM_Portfolio:Integer, PARM_Contract:Integer, PARM_Client:Integer, PARM_CorrectBalanceCost:Bool, PARM_Action:Integer):Integer
```

## Процедура: `WRTOvervalueLotsTrust`

```rsl
WRTOvervalueLotsTrust (PARM_OperDate:Date, PARM_FIID:Integer, PARM_Department:Integer, PARM_ID_Operation:Integer, PARM_ID_Step:Integer, PARM_Course:Double, PARM_Portfolio:integer, PARM_Contract:Integer, PARM_Client:Integer, PARM_AccountCost:Integer, PARM_Amount:Money, PARM_OldAccountCost:Money, PARM_OverAmount Money):Integer
```

## Процедура: `VA_ChangeDLRESLNK`

```rsl
VA_ChangeDLRESLNK (ID: Integer, ChildID: Integer, ReserveKind: Integer, ReserveAmount:MoneyL, ReserveDate: Date): Bool
```

## Процедура: `VA_InsertDLRESLNK`

```rsl
VA_InsertDLRESLNK (DlResLnk: Record) :Bool
```

## Процедура: `VA_ChangeDL_LEG`

```rsl
VA_ChangeDL_LEG (ID: Integer, поле: String, значение: Variant, [поле1:String], [значение1:Variant]):Bool
```

## Процедура: `VA_InsertVSORDLNK`

```rsl
VA_InsertVSORDLNK (VsOrdLnks:TArray) : Bool
```

## Процедура: `VA_ChangeVSORDLNK`

```rsl
VA_ChangeVSORDLNK (BCID:Integer, LinkKind:Integer, DocKind:Integer, ContractID:Integer, Start:Date, поле1:String, значение1:Variant):Bool
```

## Процедура: `VA_GetABCStatusOnDate`

```rsl
VA_GetABCStatusOnDate (BCID:Integer, Date:Date, ABCStatus:Integer) : Bool
```

## Процедура: `НайтиОткрытьСчетПроцВекселя`

```rsl
НайтиОткрытьСчетПроцВекселя (pcacc:Record, BCID:Integer, BalanceDate:Date):Bool
```

## Процедура: `VA_GetProxyName`

```rsl
VA_GetProxyName (Сделка:Integer, СторонаДоговора:Integer, РольПреставителя:Integer [, представитель:Record] [, РегДокумент:Record] [, ВводИнкасс:Integer]):String
```

## Процедура: `VS_ChangeVSORDLNK`

```rsl
VS_ChangeVSORDLNK (BCID:Integer, LinkKind:Integer, DocKind:Integer, ContractID:Integer, Start:Date, поле1:String, значение1:Variant):Bool
```

## Процедура: `VS_GetCurrentHolder`

```rsl
VS_GetCurrentHolder (bnr / BCID:Integer [, HolderName:String]):Bool
```

## Процедура: `VS_GetNextBnr`

```rsl
VS_GetNextBnr (IsGetFirst:Integer, Banner:Record, Dlleg:Record):Integer
```

## Процедура: `VS_GetPayDeadline`

```rsl
VS_GetPayDeadline (BCID/leg: Object/Integer): Date
```

## Процедура: `VS_GetSeriesAndNumber`

```rsl
VS_GetSeriesAndNumber (Ser:String, Num:String):Bool
```

## Процедура: `VS_GetSetting`

```rsl
VS_GetSetting (путь: String): Variant
```

## Процедура: `VS_GetVekselNumberInOrder`

```rsl
VS_GetVekselNumberInOrder ([number: Integer] BCID: Integer [, LinkKind: Integer] [, ContractId: Integer]): Bool
```

## Процедура: `VS_InsertPawnOrder`

```rsl
VS_InsertPawnOrder (ord:Record, spg1:Record, spg2:Record, VsOrdLnks:Tarray):Bool
```

## Процедура: `VS_InsertVSORDLNK`

```rsl
VS_InsertVSORDLNK (VsOrdLnks:TArray):Booll
```

## Процедура: `VS_MakeStorContract`

```rsl
VS_MakeStorContract (ContractID: Integer, FIID: Integer, Account: String [, FIIDPayer: Integer]): Bool
```

## Процедура: `VS_SetStatusToBlanks`

```rsl
VS_SetStatusToBlanks ()
```

## Процедура: `может`

```rsl
вызываться в двух вариантах: VS_SetStatusToBlanks (ID:Integer, Status:Integer [, ResponsPerson:Integer] [, StatusDate:Date]):Bool
```

## Процедура: `VS_SetStartDateOnBanner`

```rsl
VS_SetStartDateOnBanner (BCID:Integer [, дата:Date]):Bool
```

## Процедура: `ДатаЗакрСчПрВекселя`

```rsl
ДатаЗакрСчПрВекселя ([BCD: Integer], дата: Date): Bool
```

## Процедура: `ДатаОкнчСчПрВекселя`

```rsl
ДатаОкнчСчПрВекселя ([BCID: Integer] дата: Date): Bool
```

## Процедура: `ИзменитьВексель`

```rsl
ИзменитьВексель (BCID:Integer, поле:String, значение:Variant [, поле1:String] [, значение1:Variant]):Bool
```

## Процедура: `НайтиСчетПроцВекселя`

```rsl
НайтиСчетПроцВекселя ([pcacc:Trechandler, ] BCID:Integer [, obj_type:Integer] [, mode:Integer]):Bool
```

## Процедура: `VS_AutoRunStep`

```rsl
VS_AutoRunStep (kind: Integer, ID: Integer, symb: String): Bool
```

## Процедура: `VS_FillPaymProp`

```rsl
VS_FillPaymProp (ptid: Integer, bankid: Integer [, name: String] [, inn: String] [, bankname: String] [, coracc: String]): Bool
```

## Процедура: `VS_FindOrder`

```rsl
VS_FindOrder (BCID:Integer [, LinkKind:Integer] [, order:TRecHandler] [, lnk:TRecHandler]):Bool
```

## Процедура: `VS_GetBlanksEnumStr`

```rsl
VS_GetBlanksEnumStr (ID:Integer [, Count:Integer, SerieDelimiters:String]):String
```

## Процедура: `VS_GetComBase`

```rsl
VS_GetComBase (ord / ContractID:Integer [, basis:Integer] [, maturity:Date] [, sum:MoneyL]):Bool
```

## Процедура: `VS_GetProxyName`

```rsl
VS_GetProxyName (ord:Integer, Side:Integer, Role:Integer [, ProxyBuf:Record] [, SpgroundBuf:Record] [, mode:Integer]):String
```

## Процедура: `VS_InsertSPGROUND`

```rsl
VS_InsertSPGROUND (spg:Record):Bool
```

## Процедура: `VS_MakeDocumentID`

```rsl
VS_MakeDocumentID (Doc:Record, [DocID:String, ] DocKind:Integer):String
```

## Процедура: `VS_PercentCalc`

```rsl
VS_PercentCalc (autoperc:Integer, [calcdate:Date], [sum:MoneyL]):Bool
```

## Процедура: `VS_RestoreDocumentID`

```rsl
VS_RestoreDocumentID (Doc:Record, DocumentID:String, DocKind:Integer):Bool
```
