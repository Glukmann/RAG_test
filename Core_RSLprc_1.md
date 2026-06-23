# Core RSLprc 1

Введение
Настоящее Руководство является частью Руководства программиста и содержит описание
общесистемных спецпеременных, а также переменных, классов, процедур и констант языка
интерпретатора RSL, которые используются при создании макромодулей BalanceInter,
BankInter, BilFacturaInter, CarryDoc, cryptdlm.d32, CTInter, входящих в АС RS-Core V.6
ИБС RS-Bank V.6, и при написании пользователем собственных макропрограмм. Кроме
данного в состав Руководства программиста входят руководства, содержащие описание
других модулей языка RSL:
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 2" (файл Books\Tools\CoreRSLprc_2.pdf) – содержит описание модулей
CurrInter, FIInter, GateInter, InsCarryDoc, OprInter, PcRateInter, PTInter, RsbDataSet,
RsbObjFactory, RsSysLog, SFInter.
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 3" (файл Books\Tools\CoreRSLprc_3.pdf) – содержит описание модулей
PaymInter, Календарь, Проценты, Шлюз.
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
Интерфейсы языка RSL, за исключением общесистемных спецпеременных, поставляются
вместе с ИБС RS-Bank V.6 в виде стандартных RSL-модулей и становятся доступными
пользователю после подключения этих модулей к программам. Все интерфейсы,
определенные 
в 
этих 
модулях, 
доступны 
для 
использования 
во 
всех
подсистемах – процедуры выполнения проводок, формирование балансов, спецпеременные
сложных 
проводок 
и 
т.п. 
Чтобы 
подключить 
какой-либо 
модуль, 
необходимо
воспользоваться командой Import:
Пример.
Import BankInter;
Описание стандартных модулей сгруппировано по отдельным главам, название каждой из
которых соответствует названию соответствующего модуля.
Каждая глава Руководства содержит большое количество примеров, иллюстрирующих
использование этих средств при написании программ.
В настоящее Руководство не входит описание интерфейсов, используемых в:
· АС RS-Banking V.6;
· АС RS-Reporting V.6;
· АС RS-Loans V.6;
· АС RS-Retail V.6;
· АС RS-FinMarkets.
Для этих компонентов ИБС RS-Bank V.6 подготовлены отдельные Руководства.
В настоящем документе содержатся ссылки на Руководство пользователя "Механизм
прикладного применения криптографии" (файл Books/ABS_Security/Cryptography.pdf).
Информация о лицензиях на функциональность ИБС RS-Bank V.6 представлена в
руководстве 
"Лицензируемая 
функциональность 
ИБС 
RS-Bank 
V.6" 
(см. 
файл
Books\System\License_V6.pdf).
При ссылке на информацию, расположенную в настоящем руководстве, указывается номер
страницы (в скругленном прямоугольнике 
), соответствующий нужному Вам разделу, или
гиперссылка. Ссылка на раздел другого руководства дается с указанием названия главы и
раздела, содержащего требуемую информацию.
Общесистемные спецпеременные
Общесистемные спецпеременные
При работе макросов используются перечисленные ниже спецпеременные. Для того чтобы
работать с этими переменными, необходимо в макрос пользователя подключить файл
globals.mac, используя директиву import, после чего спецпеременные будут доступны в
любой из подсистем комплекса RS-Bank.
{BranchCurDate} 
– дата 
операционного 
дня, 
открытого 
последним 
в 
филиале
работающего пользователя.
{BPromUse} – признак работы ИБС RS-Bank в режиме промышленной эксплуатации.
{CCYNatCur} – буквенный ISO-код национальной валюты.
{CORAC_Bank} – корсчет банка в РЦ.
{cRealTypePerson} 
– 
наименование 
актуального 
уровня 
доступа 
пользователя,
работающего в системе.
{cTypePerson} – код уровня доступа работающего в системе пользователя.
{curdate} – дата текущего операционного дня.
{FIO_Book} – ФИО главного бухгалтера.
{FIO_Boss} – ФИО управляющего.
{GroupOperF} – нижняя граница диапазона номеров пользователей, подчиненных
работающему в системе пользователю.
{GroupOperL} – верхняя граница диапазона номеров пользователей, подчиненных
работающему в системе пользователю.
{INN_Bank} – ИНН банка.
{ISONatCur} – цифровой ISO-код национальной валюты.
{Legal_Addr} – юридический адрес банка.
{MFO_Bank} – БИК банка.
{MFO_RCC} – БИК РЦ банка.
{Name_Bank} – название банка.
{Name_Book} – должность главного бухгалтера.
{Name_Boss} – должность управляющего.
{NumDprt} – номер головного отделения банка.
{oper} – номер исполнителя, с которым пользователь зарегистрировался в системе.
{OperDprt} – идентификатор филиала текущего пользователя. Если пользователь
привязан к узлу ТС с типом "Филиал", то переменная равна идентификатору этого
Общесистемные спецпеременные
узла; если пользователь привязан к узлу ТС с типом "ВСП", то переменная равна
ближайшему вышестоящему узлу ТС с типом "Филиал".
{OperDprtNode} – идентификатор подразделения текущего пользователя (т.е. узла ТС, к
которому он привязан). Если пользователь привязан к узлу ТС с типом "Филиал",
то данная переменная и переменная {OperDprt} равны между собой.
{OurBank} – определение нашего банка. Значение переменной зависит от того, к какому
узлу ТС привязан текущий работающий в системе пользователь (т.е. это
идентификатор связанного субъекта филиала пользователя). Используется для
простановки в поля документов.
{Post_Addr} – почтовый адрес банка.
{Real_Addr} – фактический адрес банка.
{ResidentCountryCode} – трехбуквенный код страны резидентности.
{Version} – номер версии системы.
Все спецпеременные имеют тип String, за исключением переменных {NumDprt},
{OperDprt}, {OurBank} и {oper}, которые принадлежат к типу Integer, переменной
{BPromUse}, которая имеет тип Bool, и переменной {curdate} типа Date. Фигурные скобки
являются частью имени переменной.
При использовании спецпеременных в макропрограмме нет необходимости явно их
определять. Однако если пользователь декларирует переменные программы при помощи
оператора VAR, то ему также необходимо декларировать и переменные.
Пример.
VAR {Name_Bank}, {MFO_Bank}
При декларировании переменных с помощью оператора VAR в макрофайле пользователю
необходимо использовать это определение и для описания переменных во всех
макрофайлах, перечисленных в директиве import.
отчетов.
Процедуры
Структура bl_info
Информационная структура bl_info.rec типа Object имеет следующее содержание:
iReportNumber – номер отчета. Поле может принимать следующие значения:
· 1 – рублевый баланс;
· 2 – валютный баланс;
· 3 – рублевая оборотно-сальдовая ведомость;
· 4 – валютная оборотно-сальдовая ведомость;
· 5 – рублевая оборотно-сальдовая ведомость, полученная с использованием
процедур макроязыка RSL (регламентированная отчетность);
· 6 – рублевая сальдовая ведомость, полученная с использованием процедур
макроязыка RSL (регламентированная отчетность);
· 7 – валютный баланс на RSL;
· 8 – рублевая оборотно-сальдовая ведомость, полученная с использованием
процедур макроязыка RSL.
iChapter – номер главы счетов от 1 до 30, по которой необходимо выполнить расчет
баланса, может также принимать значение 0 для всех глав.
iKind – период выпуска баланса. Данное поле может принимать следующие значения:
· 1 – за день;
· 2 – за месяц;
· 3 – квартальный;
· 4 – годовой;
· 5 – накопительный;
· 6 – годовой заключительный;
· 7 – за прошлый день;
· 8 – за период;
· 9 – за период оптимизированный.
iUnit – размерность сумм для рублевого баланса. Для валютных балансов пересчет в
тысячи не производится. Данное поле может принимать следующие значения:
· 1 – без округления;
· 2 – в тысячах;
· 3 – в тысячах-2;
· 4 – в тысячах-3;
· 6 – в тысячах-5.
При его значении, большем 1, производится округление сумм до тысяч в
соответствии с выбранным алгоритмом.
iCurrency – для рублевых балансов параметр определяет учет счетов покрытия. Поле
может принимать следующие значения:
· 1 – все счета;
· 2 – только счета рублевого покрытия;
· 3 – без счетов рублевого покрытия.
iMonth – номер месяца, за который выпускается баланс. Данное поле используется в
случае формирования баланса за месяц.
iQuarter – номер квартала, за который выпускается баланс. Данное поле используется в
случае формирования баланса за квартал.
BdRepDate – дата, за которую выпускается баланс. Данное поле используется в случае
формирования баланса за архивный день.
BdBeginDate – дата начала периода формирования баланса. Данное поле используется в
случае формирования баланса за период.
BdEndDate – дата окончания периода формирования баланса. Данное поле используется
в случае формирования баланса за период.
iFirstMonth – номер первого месяца баланса.
iLastMonth – номер последнего месяца баланса.
iRestMonth – номер месяца исходящего остатка.
iOutYear – номер года исходящего остатка.
iPlanNumber1 – номер плана балансовых счетов главы 1.
iPlanNumber2 – номер плана балансовых счетов главы 2.
iPlanNumberN – номер плана балансовых счетов главы N.
NumDprt – номер филиала, по счетам которого выполняется расчет баланса; по
умолчанию значение равно номеру текущего филиала.
Oper – номер операциониста, по счетам которого рассчитывается баланс.
Client – код клиента, по счетам которого выпускается баланс.
Balance – номер балансового счета для лицевых счетов, относящихся к которому,
выполняется расчет баланса.
Type_Account – системный тип лицевых счетов, для которых следует рассчитать баланс.
UserTypeAccount – пользовательский тип лицевых счетов, для которых рассчитывается
баланс.
iIsCur – признак выпуска валютного отчета.
Code_Currency – внутренний цифровой код валюты в справочнике для расчета баланса
по валютным счетам.
iAlgorithm – номер алгоритма расчета баланса для валютных счетов, по умолчанию его
значение равно 1. Поле может принимать следующие значения:
· 0 – основной;
· 1 – оптимизированный.
iRecalcCurrency – код валюты для пересчета в валютных балансах, по умолчанию его
значение равно 0 (национальная валюта). Данное поле может принимать
значение любого кода валюты, которая есть в справочнике валют.
iRealRub – флаг реального покрытия для валютного баланса, по умолчанию его значение
равно 0. Флаг может принимать значения: 
· 0 – пересчет;
· 1 – реальное покрытие.
iOutForm – номер формы выпуска баланса (обороты/остатки). Возможные значения
данного поля хранятся в таблице dnamealg_dbt.
iGroup – вид группировки счетов при формировании таблицы баланса и итогов при печати
отчета. Возможные значения данного поля хранятся в таблице dnamealg_dbt. При
значении, равном 2, сканирование счетов при расчете баланса производится в
соответствии с разбиением на разделы и балансовые счета, в остальных случаях
– только по балансовым счетам.
CPrnZero – признак печати нулевых сумм:
· Y – строки с нулевыми суммами будут представлены в отчете;
· N – строки с нулевыми суммами будут исключены из отчета.
cSetA – признак печати с апострофами: 
· Y – все суммы в отчете будут разделены по разрядам апострофами;
· N – суммы в отчете не разделяются по разрядам.
szBaseFileName – имя таблицы баланса.

## Процедура: `ОкруглитьФайлБаланса`

```rsl
ОкруглитьФайлБаланса (bl_info:Record):Variant
```

## Процедура: `ПанельОтчет`

```rsl
ПанельОтчет (bl_info:Record):Integer
```

## Процедура: `РассчитатьБалансПоГлавеВал`

```rsl
РассчитатьБалансПоГлавеВал ():Integer
```

## Процедура: `СоздатьКлючевойФайлСчетов`

```rsl
СоздатьКлючевойФайлСчетов (bl_info:Record):Integer
```

## Класс: `RsbAccSubDocuments`

```rsl
RsbAccSubDocuments ():Object
```

## Класс: `RsbAccTransaction`

```rsl
RsbAccTransaction():Object
```

## Класс: `RsbAccTransactionData`

```rsl
RsbAccTransactionData ():Object
```

## Класс: `RSBankMsg`

```rsl
RSBankMsg()
```

Класс, описывающий сообщения, которые возникают в ИБС RS-Bank V.6.

**Свойства:**

Message – текст сообщения; тип String.
Stat – номер сообщения; тип Integer.

## Класс: `RsbBankPayment`

```rsl
RsbBankPayment ([DocumentID:Integer]):Object
```

## Класс: `RsbBankPaymentBase`

```rsl
RsbBankPaymentBase ():Object
```

## Класс: `RsbBankProduct`

```rsl
RsbBankProduct()
```

## Класс: `RsbBatchAccTrn`

```rsl
RsbBatchAccTrn()
```

## Класс: `RsbBbCpOrder`

```rsl
RsbBbCpOrder ([DocumentID:Integer]):Object
```

## Класс: `платежа`

```rsl
по первичным документам "Рублевый платеж банка" и "Рублевое требование банка". Наследник класса RsbPayment (см. Руководство "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank V.6. Часть 3").
```

## Класс: `RsbClientProduct`

```rsl
RsbClientProduct()
```

## Класс: `RsbContactMesPro`

```rsl
RsbContactMesPro()
```

## Класс: `RsbConveyerExec`

```rsl
RsbConveyerExec()
```

## Класс: `RsbCpOrder`

```rsl
RsbCpOrder ()
```

## Класс: `платежа`

```rsl
по первичным документам "Валютный клиентский платеж" и "Валютный банковский платеж". Наследник класса RsbPayment (см. Руководство "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank V.6. Часть 3").
```

## Класс: `RsbInt512`

```rsl
RsbInt512()
```

Класс-представление целого числа в диапазоне от -2512 + 1 до 2512 - 1.

**Свойства:**

StringVal – cтроковое представление числа RsbInt512; тип String.

**Пример:**

Import BankInter;
var val =
RsbInt512("1340780792994259709957402499820584612747936582059
8186486050853753882811946569946433649006083096");
println(val.StringVal);
val.StringVal = "123";
println(val.StringVal);

**Методы:**

Add(arg:Object, String):Object

## Класс: `RsbMemorialOrder`

```rsl
RsbMemorialOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbMOPayment`

```rsl
RsbMOPayment ([id_платежа:Integer]):Object
```

## Класс: `объекта`

```rsl
платежа в составе мемориального ордера. Класс реализован как наследник класса RsbPayment (см. Руководство "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank V.6. Часть 3"), и имеет аналогичные свойства и методы. Отличием от класса RsbPayment является то, что часть атрибутов класса RsbMOPayment доступна только на чтение, к ним относятся следующие: · PayerBankID. · PayerBankCodeKind. · PayerBankCode. · PayerBankName. · PayerBankCorrAcc. · PayerBankCorrCodeKind. · PayerBankCorrCode. · PayerBankCorrName. · ReceiverBankID. · ReceiverBankCodeKind. · ReceiverBankCode. · ReceiverBankName. · ReceiverBankCorrAcc. · ReceiverBankCorrCodeKind. · ReceiverBankCorrCode. · ReceiverBankCorrName.
```

## Класс: `RsbMultyCarryMethod`

```rsl
RsbMultyCarryMethod ():Object
```

## Класс: `RsbMultyDoc`

```rsl
RsbMultyDoc ([DocumentID:Integer]):Object
```

## Класс: `объекта`

```rsl
"Мультивалютный документ". Конструктор класса RsbMultyDoc ([DocumentID:Integer]) имеет параметр DocumentID – идентификатор документа.
```

**Свойства:**

AutoKey – идентификатор первичного документа (поле t_AutoKey таблицы dmultydoc_dbt);
тип Integer. Свойство доступно только для чтения.
Categories – категории документа; тип Object. Свойство представляет собой объект
класса RsbObjCategories
 и доступно только для чтения.
Chapter – номер главы плана счетов (поле t_Chapter поле dmultydoc_dbt); тип Integer.
CloseDate – дата 
закрытия 
операции 
по 
документу 
(поле 
t_CloseDate 
таблицы
dmultydoc_dbt; тип Date.
Kind_Operation – вид 
операции 
по 
документу 
(поле 
t_Kind_Operation 
таблицы
dmultydoc_dbt); тип Integer.
LaunchOper – признак "Запускать дочернюю операцию по документу"; тип Bool.
Notes – примечания документа; тип Object. Свойство представляет собой объект класса
RsbObjNotes
 и доступно только для чтения.
Oper – номер операциониста, автора документа (поле t_Oper таблицы dmultydoc_dbt); тип
Integer.
Origin – происхождение 
мультивалютного 
документа 
(поле 
t_Origin 
таблицы
dmultydoc_dbt); тип Integer.
Payment – объект платежа, сформированного по документу; тип Object. Свойство
возвращает объект класса RsbMDPayment и доступно только для чтения.
Status – статус документа (поле t_Status таблицы dmultydoc_dbt); тип Integer.
Type_Document – тип мультивалютного документа (поле t_Type_Document таблицы
dmultydoc_dbt); тип String.
UserField1 – пользовательское поле 1 (поле t_UserField1 таблицы dmultydoc_dbt); тип
String.
UserField2 – пользовательское поле 2 (поле t_UserField2 таблицы dmultydoc_dbt); тип
String.
UserField3 – пользовательское поле 3 (поле t_UserField3 таблицы dmultydoc_dbt); тип
String.
UserField4 – пользовательское поле 4 (поле t_UserField4 таблицы dmultydoc_dbt); тип
String.

**Методы:**

Update ():Integer

## Класс: `RsbObjNotes`

```rsl
RsbObjNotes ()
```

## Класс: `RsbProductObject`

```rsl
RsbProductObject()
```

## Класс: `RsbPsCpOrder`

```rsl
RsbPsCpOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbSQLInsert`

```rsl
RsbSQLInsert()
```

## Класс: `RsbUserPanel`

```rsl
RsbUserPanel ()
```

## Класс: `RsbUserPanelField`

```rsl
RsbUserPanelField ()
```

Класс представляет собой описатель поля панели.

**Свойства:**

DownField – номер поля, в которое перемещается фокус ввода при нажатии клавиши
[Down]; тип Integer.
Enabled – признак доступности поля на редактирование; тип Bool.
LeftField – номер поля, в которое перемещается фокус ввода при нажатии клавиш [Left],
[Shift+Tab]; тип Integer.
Length – длина строкового поля или число знаков после запятой числового поля.
Свойство имеет тип Integer и доступно только для чтения.
Name – название поля в ресурсе. Свойство имеет тип String и доступно только для
чтения.
RightField – номер поля, в которое перемещается фокус ввода при нажатии клавиш
[Right], [Tab], [Enter]; тип Integer.
UpField – номер поля, в которое перемещается фокус ввода при нажатии клавиши [Up];
тип Integer.
Value – значение поля; тип Variant.
ValueType – тип значения поля. Свойство имеет тип Integer и доступно только для чтения.

## Класс: `RsbUserPanelFieldsCollection`

```rsl
RsbUserPanelFieldsCollection ()
```

## Класс: `RsbUserPanelMenuItemsCollection`

```rsl
RsbUserPanelMenuItemsCollection()
```

## Класс: `RslBinaryData`

```rsl
RslBinaryData():Object
```

## Класс: `TRsbRslTemplByWrap`

```rsl
RslBinaryData():Object
```

## Процедура: `CB_CancelCorrectDoc`

```rsl
CB_CancelCorrectDoc (CorrDocType:Integer, accispr:Trechandler)
```

## Процедура: `CB_CreateCorrectDoc`

```rsl
CB_CreateCorrectDoc (CorrDocType:Trechandler, acctrn:Trechandler, accispr:Trechandler, objattr:Trechandler):Integer
```

## Процедура: `CB_GetCorrDocNumbers`

```rsl
CB_GetCorrDocNumbers (CorrDocID:Array, CorrDocNumber:Array):Integer
```

## Процедура: `CB_GetDocKindCorrectDoc`

```rsl
CB_GetDocKindCorrectDoc (CorrDocType:Integer, acctrn:Trechandler, acctrn:Trechandler):Integer
```

## Процедура: `CB_InitCorrectDoc`

```rsl
CB_InitCorrectDoc (CorrDocType:Integer, AccTrnID:Integer, CorrDocID:Integer, CorrDocNumber:String, RateDate:Date, acctrn:Trechandler, accispr:Trechandler):Integer
```

## Процедура: `GetTxtFileName`

```rsl
GetTxtFileName ([File:String]):String
```

## Процедура: `GetWorkFileName`

```rsl
GetWorkFileName ([File:String]):String
```

## Процедура: `CashSymbSum`

```rsl
CashSymbSum ([DateBegin:Date] [, DateEnd:Date] [, Currency:Integer, String] [, NumDprt:Integer]):Integer
```

## Процедура: `CashSymbSumAcc`

```rsl
CashSymbSumAcc (Account:String, BegDate:Date, EndDate:Date, Currency:String, NumDprt:Integer):String
```

## Процедура: `SetRSTrace`

```rsl
SetRSTrace (param:Bool):Integer
```

## Процедура: `SetOraTrace`

```rsl
SetOraTrace (param:Bool):Integer
```

## Процедура: `CB_DeleteOprBlock`

```rsl
CB_DeleteOprBlock(BlockID:Long):Bool
```

## Процедура: `CB_DeleteOPROSTEP`

```rsl
CB_DeleteOPROSTEP(BLOCKID:Long, NUMBER_STEP:Long):Bool
```

## Процедура: `CB_DeleteOprSblck`

```rsl
CB_DeleteOprSblck(BlockID:Long, StatusKindID:Long, NumValue:Long):Bool
```

## Процедура: `CB_InsUpdOprSblck`

```rsl
CB_InsUpdOprSblck([saveoprsblck:Trechandler], oprsblck:Trechandler):Bool
```

## Процедура: `WEB_CB_InsertUpdateOprBlockPanel`

```rsl
WEB_CB_InsertUpdateOprBlockPanel(oprblockOld:Trechandler, oprinfoOld:Trechandler, oprblockNew:Trechandler, oprinfoNew:Trechandler, infoNew:String [, saveFirstStep:Integer] [, firstStep:Integer]):Bool
```

## Процедура: `AccClaimIncomplete`

```rsl
AccClaimIncomplete (Account:String, Chapter:Integer, FIID:Integer):Bool
```

## Процедура: `AccGetFreeAmount`

```rsl
AccGetFreeAmount (FreeAmount:Money, FreeLimitAmount:Money, Account:String, Chapter:Integer, FIID:Integer, BankDate:Date [, Priority:Integer] [, ClaimID:Integer] [, SkipArrest:Bool] [, ReasonClaim:Trechandler] [, PayType:Integer])
```

## Процедура: `CB_CheckDeleteAcClmCng`

```rsl
CB_CheckDeleteAcClmCng(ChangeDocID:Integer, CheckOnly:Bool):Bool
```

## Процедура: `CB_CheckInsUpdAcClmCng`

```rsl
CB_CheckInsUpdAcClmCng(AcClmCngOld:Record, AcClmCngNew:Record, CheckOnly:Bool, ChangeDocID:Integer):Bool
```

## Процедура: `CB_CloseAccount`

```rsl
CB_CloseAccount (Chapter:Integer, FIID:Integer, Account:String [, CloseDate:Date] [, ErrorDescription:String]):Integer
```

## Процедура: `CB_CloseChapter`

```rsl
CB_CloseChapter (Сhapter:Integer):Bool
```

## Процедура: `CB_DeleteAccblnc`

```rsl
CB_DeleteAccblnc(accblncRec:Record)
```

## Процедура: `CB_DeleteAcClaim`

```rsl
CB_DeleteAcClaim(ClaimID:Integer):Bool
```

## Процедура: `CB_DeleteACCTYPE`

```rsl
CB_DeleteACCTYPE(OldTypeAccount:String):Integer
```

## Процедура: `CB_DeleteChapter`

```rsl
CB_DeleteChapter (Сhapter:Integer):Bool
```

## Процедура: `CB_DeleteNamePlan_Chapter`

```rsl
CB_DeleteNamePlan_Chapter (PlanNum:Integer, Сhapter:Integer):Bool
```

## Процедура: `CB_GetAccAttribRestriction`

```rsl
CB_GetAccAttribRestriction():Array
```

## Процедура: `CB_GetFormattedAcnt`

```rsl
CB_CloseAccount (Chapter:Integer, FIID:Integer, Account:String [, ErrorDescription:String]):Integer
```

## Процедура: `CB_InsertChapter`

```rsl
CB_InsertChapter (ChapterObj:Record):Bool
```

## Процедура: `CB_InsertNamePlan_Chapter`

```rsl
CB_InsertNamePlan_Chapter (PlanNum:Integer, Сhapter:Integer):Bool
```

## Процедура: `CB_InsertUpdateACCTYPE`

```rsl
CB_InsertUpdateACCTYPE (OldTypeAccount:String, AccTypeRec:Tbfile, IsNewRec:Bool):Integer
```

## Процедура: `CB_InsUpdAccblnc`

```rsl
CB_InsUpdAccblnc(accblncRec:Record, iNumPlan:Integer, isInsert:Bool):Integer
```

## Процедура: `CB_InsUpdAcClaim`

```rsl
CB_InsUpdAcClaim(AcClaimOld:File, AcClaimNew:File, ClaimID:Integer):Bool
```

## Процедура: `CB_IsPairExpAccounts`

```rsl
CB_IsPairExpAccounts (IsPair:Bool, OBCHAPTER:Record):Bool
```

## Процедура: `CB_MakeAdditionalAccount`

```rsl
CB_MakeAdditionalAccount(accTrn:Object [, ExRateSum:Money] [, CodeCat:String] [, FIRole:Integer] [, FIID:Integer]):String
```

## Процедура: `CB_OpenChapter`

```rsl
CB_OpenChapter (Сhapter:Integer):Bool
```

## Процедура: `CB_OpenClosedAccount`

```rsl
CB_CloseAccount (Chapter:Integer, FIID:Integer, Account:String [, ErrorDescription:String]):Integer
```

## Процедура: `CB_OverEstimateAccount`

```rsl
CB_OverEstimateAccount ([RevalueAccParamID:Integer] [, RevalueAccRecID:Integer] RestKind:Integer, DprtID:Integer, Chapter:Integer, Account:String, Code_Currency:Integer, RegulateDate:Date, AccountKind:Integer [, RegCarry:Bool] [, ActuateAccOvervalue:Bool] [, PrintReport:Bool] [, PrintOrders:Bool] [, AllDays:Bool] [, FirstNumberDoc:Integer] [, Backout:Bool]):Integer
```

## Процедура: `CB_OverstimNVPIAccount`

```rsl
CB_OverstimNVPIAccount ([ReVNVPIAccParamID:Integer], [ReVNVPIAccRecID:Integer], DprtID:Integer, Chapter:Integer, Account:String, Code_Currency:Integer, RegulateDate:Date, AccountKind:Integer, [PrintReport:Bool], [Backout:Bool]):Integer
```

## Процедура: `CB_RegulatePairAccount`

```rsl
CB_RegulatePairAccount (RegulateDate:Date, Chapter:Integer, Code_Currency:Integer, Account:String, [FinishRegDate:Date], [Backout:Bool], [RegPairAccParamID:Integer], [RegPairAccRecID:Integer], [PrintRegistry:Bool], [NumberDoc:Integer], [NumberPack:Integer]):Integer
```

## Процедура: `CB_RestoreAcClaimState`

```rsl
CB_RestoreAcClaimState(ClaimID:Integer):Bool
```

## Процедура: `CB_SetAccountLimit`

```rsl
CB_SetAccountLimit(AccountID:Integer, Limit:Money [, OnDate:Date]):Integer
```

## Процедура: `CB_UpdateChapter`

```rsl
CB_UpdateChapter (ChapterObj:Record):Bool
```

## Процедура: `ChangeAccountClaimAuto`

```rsl
ChangeAccountClaimAuto (acclmcng:Record):Integer
```

## Процедура: `ClearAccountRecord`

```rsl
ClearAccountRecord(accountRec:File, Record, TbFile, TRecHandler, accblncRec:File, Record, TbFile, TRecHandler)
```

## Процедура: `Create_Account`

```rsl
Create_Account ([inac:Record [, inab:Record] [, ErrMsg: String] [, Limit: Money]):Integer
```

## Процедура: `CreateAccountStatement`

```rsl
CreateAccountStatement(AccountID:Integer, DateFrom:Date, DateTo:Date [, ReportFileName:String] [, ReportFormat:Integer]):Intege
```

## Процедура: `Delete_Account`

```rsl
Delete_Account(AccountID:Integer):Integer
```

## Процедура: `GetFreeAmount`

```rsl
GetFreeAmount (Account:String, Chapter:Integer, FIID:Integer, BankDate:Date [, Priority:Integer] [, ClaimID:Integer] [, SkipArrest:Bool] [, ReasonClaim:TRecHandler] [, PayType:Integer]):Money
```

## Процедура: `GetFreeAmountForOverdraft`

```rsl
GetFreeAmountForOverdraft (Account:String, Chapter:Integer, FIID:Integer, BankDay:Date):Money
```

## Процедура: `GetFreeAmountWithLimit`

```rsl
GetFreeAmountWithLimit (Account:String, Chapter:Integer, FIID:Integer, BankDate:Date [, Priority:Integer] [, ClaimID:Integer] [, SkipArrest:Bool] [, ReasonClaim:TRecHandler] [, PayType:Integer]):Money
```

## Процедура: `GetKeyPosition`

```rsl
GetKeyPosition ()
```

## Процедура: `GetLastCarryDate`

```rsl
GetLastCarryDate (Chapter:Integer, FIID:Integer, Account:String, LastCarryDate:Date [, EndPeriod:Date]):Bool
```

## Процедура: `GetOCPAccount`

```rsl
GetOCPAccount (OCPAccount:String, Chapter:Integer, FIID:Integer [, Department:Integer]):Bool
```

## Процедура: `InsertAccountClaim`

```rsl
InsertAccountClaim (acclaim:Record [, acclaimstate:Record]):Integer
```

## Процедура: `InsertArestClaimAuto`

```rsl
InsertArestClaimAuto (acclaim:Record [, acclaimstate:Record]):Integer
```

## Процедура: `ListAccClaim`

```rsl
ListAccClaim (ClaimID:Integer, Chapter:Integer, FIID:Integer, Account:String [, Date:Date] [, ClaimKind:Integer] [, ClaimType:Integer] [, Initiator:Integer] [, DocNumber:String] [, DocDate:Date] [, FiscOrgCode:String] [, Auto:String] [, WhereClause:String]):Integer
```

## Процедура: `MakeAccountIDEx`

```rsl
MakeAccountIDEx(account:Record):String
```

## Процедура: `OV_DefineLimitAccount`

```rsl
OV_DefineLimitAccount (PaymentID:Integer, SfContrID:Integer, ProcDate:Date, IsPayer:Bool [, Slim:Money] [, Slim_full:Money]):Integer
```

## Процедура: `OV_GetOverdraftProcMode`

```rsl
OV_GetOverdraftProcMode ():Integer
```

## Процедура: `OV_LimitSumContro`

```rsl
OV_LimitSumContro (accLimit:Money, SfContrID:Integer, PaymentID:Integer, ControlDate:Date, IsPayer:Bool):Integer
```

## Процедура: `OV_NeedRestoreLimit`

```rsl
OV_NeedRestoreLimit (PaymentID:Integer, IsPayer:Bool [, Result:Bool]):Integer
```

## Процедура: `OV_NeedRestoreLimitForAccount`

```rsl
OV_NeedRestoreLimitForAccount (PaymentID:Integer, Account:String, FIID:Integer, IsPayer:Bool [, Result:Bool]):Integer
```

## Процедура: `OverValueAccount`

```rsl
OverValueAccount (Account:String, FIID:Integer [, Chapter:Integer] [, ProcDate:Date] [, Incomming:Bool]):Bool
```

## Процедура: `RemoveChangeAccountClaim`

```rsl
RemoveChangeAccountClaim (ChangeDocID:Integer):Integer
```

## Процедура: `SetAccOverdaftLimit`

```rsl
SetAccOverdaftLimit (Account:String, Chapter:Integer, FIID:Integer, BankDay:Date, LimitDelta:Money [, ErrMessage:String]):Bool
```

## Процедура: `Update_Account`

```rsl
Update_Account (Chapter:Integer, FIID:Integer, Account:String [, Oper:Integer] [, NameAccount:String] [, UserTypeAccount:String] [, Limit:Money] [, Type_Account:String] [, OperationDate:Date]):Integer
```

## Процедура: `Update_AccountEx`

```rsl
Update_AccountEx(accountRec:File, Record, TbFile, TRecHandler, accblncRec:File, Record, TbFile, TRecHandler):Integer
```

## Процедура: `WEB_CB_CalcFreeAmount`

```rsl
WEB_CB_CalcFreeAmount(AccountID:Integer, BankDate:Date, Rest:Moneyl, MinRest:Moneyl, CalcPriority:Integer, CalcFreeAmount:Moneyl, CalcFreeLimitAmount:Moneyl)
```

## Процедура: `WEB_CB_FillAcClaimData`

```rsl
WEB_CB_FillAcClaimData(AccountID:Integer, BankDate:Date, Rest:Moneyl, ClaimSum:Moneyl, ClaimKindIDs:Integer, ClaimKindNames:String, ClaimSums:Moneyl, FreeAmounts:Moneyl, BeneficiaryName:String)
```

## Процедура: `CB_DeleteOPDPhaseGroup`

```rsl
CB_DeleteOPDPhaseGroup(GroupID:Integer):Bool
```

## Процедура: `CB_DeleteOperDayPhase`

```rsl
CB_DeleteOperDayPhase(Phase:Integer):Bool
```

## Процедура: `CB_InsertOperDayPhase`

```rsl
CB_InsertOperDayPhase(phaseRec:Record, opdPhaseOwnerArray:Tarray, phasesDpParmArray:Tarray):Bool
```

## Процедура: `CB_UpdateOperDayPhase`

```rsl
CB_UpdateOperDayPhase(InitPhase:Integer, phasesRec:Record, toDelPhaseOwnerArray:Tarray, newPhaseOwnerArray:Tarray, phasesDpParmArray:Tarray):Bool
```

## Процедура: `IsOperDayOpened`

```rsl
IsOperDayOpened(OperDay: Date):Bool
```

## Процедура: `OpenNewOperDay`

```rsl
OpenNewOperDay (OperDay: Date, [IsHidden: Bool]):Integer
```

## Процедура: `GetErrMsg`

```rsl
GetErrMsg ():String
```

## Процедура: `IsRslBatchMode`

```rsl
IsRslBatchMode ():Bool
```

## Процедура: `RegistryObject`

```rsl
RegistryObject ([ObjectKind:Integer] [, ActionKind:Integer] [, Application:Integer] [, Object:File, Record] [, ErrMsg:String]):Integer
```

## Процедура: `SetRslBatchMode`

```rsl
SetRslBatchMode (newVal:Bool):Bool
```

## Процедура: `AddNoteForObject`

```rsl
AddNoteForObject (ObjectType:Integer, ObjID:String, NoteKind:Integer, Note:Variant [, Date:Date] [, ID_Operation:Integer] [, ID_Step:Integer]):Integer
```

## Процедура: `fillNoteValue`

```rsl
fillNoteValue (nt:TRecHandler, val :Variant):Integer
```

## Процедура: `GetNoteValue`

```rsl
GetNoteValue (Note:Record):Variant
```

## Процедура: `по`

```rsl
переданному буферу возвращает значение примечания.
```

**Параметры:**

Note – примечание.

**Пример:**

Obj.Notes.GetFirst( {curdate}, note );
nvalue = GetNoteValue( note );

## Процедура: `ReadNoteForObject`

```rsl
ReadNoteForObject (ObjectType:Integer, ObjID:String, NoteKind:Integer [, Date:Date] [, Date2:Date], [Notes:Array]):Variant
```

## Процедура: `RemoveNoteForObject`

```rsl
RemoveNoteForObject(ObjectType:Integer, DocumentID:String, NoteKind:Integer):Bool
```

## Процедура: `CalcACCASERest`

```rsl
CalcACCASERest (accase:Record, accasscs:Record, DateOn:Date, Rest:Money):Bool
```

## Процедура: `GetACCASEPM_on_Date`

```rsl
GetACCASEPM_on_Date (CaseID : Long, DateOn : Date, buffACCASEPM : Record)
```

## Процедура: `GetAccountReserveForCase`

```rsl
GetAccountReserveForCase (accase:Record, accasscs:Record, DateOn:Date, RestReserveAccount:Money):String
```

## Процедура: `CB_GetRsvParmForAccount`

```rsl
CB_GetRsvParmForAccount (Date:Date, Account:String, Chapter:Integer, Parm:Record):Bool
```

## Процедура: `FreeReserveMass`

```rsl
FreeReserveMass ():Integer
```

## Процедура: `GetCaseOfAccount`

```rsl
GetCaseOfAccount (Chapter:Integer, FIID:Integer, Account:String, EntryDate:Date):Integer
```

## Процедура: `BP_ChangeProductClient`

```rsl
BP_ChangeProductClient(ClientProductID:Integer, PartyID:Integer):Integer
```

## Процедура: `BP_DeletePrdClntRole`

```rsl
BP_DeletePrdClntRole(ClientProductID:Integer, ClntProdObjID:Integer, Role:Integer, PartyID:Integer, Use:Integer):Integer
```

## Процедура: `BP_GetBankProductsList`

```rsl
BP_GetBankProductsList(productsList:TArray, [BankDate:Date], [Branch:Integer], [ProductKindID:Integer])
```

## Процедура: `BP_GetClientProductsList`

```rsl
BP_GetClientProductsList(productsList:TArray, ClientID:Integer, [ProductKindID:Integer], [BankDate:Date], [Branch:Integer])
```

## Процедура: `BP_GetProductClientList`

```rsl
BP_GetProductClientList(productsList:TArray, ProductID:Integer, [BankDate:Date], [Branch:Integer])
```

## Процедура: `CB_DeleteAccAnalitic`

```rsl
CB_DeleteAccAnalitic(AccanaliticsID:Integer):Integer
```

## Процедура: `CB_DeleteAccSubDC`

```rsl
CB_DeleteAccSubDC(SubCarryID:Integer):Bool
```

## Процедура: `CB_DeleteSubAcc`

```rsl
CB_DeleteSubAcc(Accsub:Tbfile):Integer
```

## Процедура: `CB_InsertAccSubDC`

```rsl
CB_DeleteSubAcc(Accsub:Tbfile):Integer
```

## Процедура: `CB_InsertSubAccount`

```rsl
CB_InsertSubAccount(Accvanl:Tbfile, Accsub:Tbfile, Rest:Moneyl, Debet:Moneyl, Credit:Moneyl):Integer
```

## Процедура: `CB_UpdateAccSubDC`

```rsl
CB_InsertSubAccount(Accvanl:Tbfile, Accsub:Tbfile, Rest:Moneyl, Debet:Moneyl, Credit:Moneyl):Integer
```

## Процедура: `CB_UpdateSubAccount`

```rsl
CB_UpdateSubAccount(rec:Tbfile, oldrec:Tbfile, Rest:Moneyl, Debet:Moneyl, Credit:Moneyl):Integer
```

## Процедура: `DebetSubAcc`

```rsl
DebetSubAcc (AccAnaliticsID:Integer, SubAccountID:Integer, [date:Date, Integer]):Moneyl
```

## Процедура: `GetAccAnaliticsID`

```rsl
GetAccAnaliticsID (AnaliticsID:Integer, Account:String, FIID:Integer, Chapter:Integer):Integer
```

## Процедура: `InsertSubAccDoc`

```rsl
InsertSubAccDoc (SubDoc:Variant):Integer
```

## Процедура: `InsertSubAccDocEx`

```rsl
InsertSubAccDocEx (AnaliticsID:Integer, Account:String [, SubAccountCode:String], subdoc:Record):Integer
```

## Процедура: `GetSubAccID`

```rsl
GetSubAccID (AnaliticsID:Integer, Account:String, FIID:Integer, Chapter:Integer, SubAccCode:String [, AccAnaliticsID:Integer]):Integer
```

## Процедура: `InsertSubAccount`

```rsl
Insertsubaccount (Analiticsid:Integer, Account:String, FIID:Integer, Chapter:Integer, Parent:String, Subacc:File, Record):Integer
```

## Процедура: `KreditSubAcc`

```rsl
KreditSubAcc (AccAnaliticsID:Integer, SubAccountID:Integer, [Date :Date, Integer]):Moneyl
```

## Процедура: `RestSubAcc`

```rsl
RestSubAcc (AccAnaliticsID:Integer, SubAccountID:Integer, [date:Date, Integer]):Moneyl
```

## Процедура: `GetCmdLineParm`

```rsl
GetCmdLineParm ([Label:String] [, RetVal:Bool, String] [, Type:Variant]):Bool
```

## Процедура: `CheckLogCRC`

```rsl
CheckLogCRC ([logtype:Integer]):Integer
```

## Процедура: `GetPartyINN`

```rsl
GetPartyINN ([ID:Integer] [, Flag:Integer]):String
```

## Процедура: `WriteFiscLog`

```rsl
WriteFiscLog (Operation:Integer, File_procedure: File, String [, Buffer1:File, Record] [, Buffer2: File, Record]):Bool
```

## Процедура: `WriteShedulerLog`

```rsl
WriteShedulerLog ([Str:String]):Integer
```

## Процедура: `CheckKey`

```rsl
CheckKey (Chapter:Integer, Account:String):Integer
```

## Процедура: `GetKey`

```rsl
GetKey (Account:String [, BIC:String]):String
```

## Процедура: `ActivA`

```rsl
ActivA (Account: Variant, [Date:Date], [Date2:Date], [Chapter:Variant], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `DebetA`

```rsl
DebetA (Account: Variant, [Date:Date], [Date2:Date], [Chapter:Variant], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `KreditA`

```rsl
KreditA(Account: Variant, [Date:Date], [Date2:Date], [Chapter:Variant], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `PassivA`

```rsl
PassivA(Account:String, [Date:Date], [Date2:Date], [Chapter:Variant], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `RestA`

```rsl
RestA(Account:String, [Date:Date], [Date2:Date], [Chapter:Integer], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `ActivB`

```rsl
ActivB ([Plan:Integer,] Balance:String [, Date:Date] [, Date2:Date [, Chapter:Integer] [, Filter:Object, String , Buffer:String], [Cur:Integer], [RestCur:Integer]]):MoneyL
```

## Процедура: `DebetB`

```rsl
DebetB ([Plan:Integer], Balance:String [, Date:Date] [, Date2:Date] [, Chapter:Integer] [, Filter:Object, String, Buffer:String], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `GetAverageBalanceRest`

```rsl
GetAverageBalanceRest (Chapter:Integer, Balance:String, NumPlan:Integer, FIID:Integer [, DateTop:Date] [, DateBot:Date] [, sqlFilter:String]):Money
```

## Процедура: `GetBalanceCredit`

```rsl
GetBalanceCredit (Chapter:Integer, Balance:String, NumPlan:Integer, FIID:Integer [, DateTop:Date] [, DateBot:Date] [, sqlFilter:String]):Money
```

## Процедура: `GetBalanceDebet`

```rsl
GetBalanceDebet (Chapter:Integer, Balance:String, NumPlan:Integer, FIID:Integer [, DateTop:Date] [, DateBot:Date] [, sqlFilter:String]):Money
```

## Процедура: `GetBalanceRest`

```rsl
GetBalanceRest (Chapter:Integer, Balance:String, NumPlan:Integer, FIID:Integer [, RestDate:Date] [, sqlFilter:String]):Money
```

## Процедура: `KreditB`

```rsl
KreditB (Plan:Integer, Balance:String, [Date:Date] [, Date2:Date] [, Chapter:Integer] [, Filter:Object, String [, Buffer:String]], [Cur:Integer], [RestCur:Integer]):MoneyL
```

## Процедура: `PassivB`

```rsl
PassivB (Plan:Integer, Balance:String, [Date:Date] [, Date2:Date] [, Chapter:Integer] [, Filter:Object, String [, Buffer:String]], [Cur:Integer], [RestCur:Integer]):Money
```

## Процедура: `RestB`

```rsl
RestB (Plan:Integer, Balance:String, [Date:Date] [, Date2:Date] [, Chapter:Integer] [, Filter:Object, String [, Buffer:String]], [Cur:Integer], [RestCur:Integer]):Money
```

## Процедура: `ACS_CheckAccessForObject`

```rsl
ACS_CheckAccessForObject (PrivID: Integer, [ObjectType: Integer], [ID: Integer, String], [Oper: Integer], [OnlyCheck: Bool]): Integer
```

## Процедура: `CheckAccountRestriction`

```rsl
CheckAccountRestriction(PrivID:Integer, Chapter:Integer, Code_Currency:Integer, Account:String [, bpoint:Integer] [, Mode:Integer] [, context:Integer] [, Oper:Integer]):Bool Базовая процедура для определения прав доступа пользователя в рамках привилегии к объекту доступа "Лицевой счет".
```

**Параметры:**

PrivID – идентификатор привилегии.
Chapter – номер главы лицевого счета.
Code_Currency – идентификатор валюты лицевого счета.
Account – номер лицевого счета.
bpoint – идентификатор точки доступа.
Mode – режим. Параметр принимает одно из значений:
- ACS_OnlyCheck – выполнять только проверку доступа к объекту.
- ACS_CreateError – в случае отказа в доступе будет выведено сообщение об
ошибке.
- ACS_PutInLog – вставлять запись в журнал аудита в случае отказа в доступе.
- ACS_OftenUsed – в случае отказа в доступе будет выведено сообщение об
ошибке и добавлена запись в журнал аудита.
context – контекст вызова ФПД, определяющий место (цель) проверки доступа к объекту.
Параметр принимает одно из значений:
- CNTX_None – пустое значение.
- CNTX_Admin – административная привилегия.
- CNTX_Input – устанавливается при вводе операциониста.
- CNTX_BilFactura – при проверке доступа к счетам-фактурам.
- CNTX_BilBookEntry – при проверке доступа к записям книги.
Oper – идентификатор пользователя.

**Возвращаемое значение:**



## Процедура: `CheckActionRestriction`

```rsl
CheckActionRestriction(PrivID:Integer [, bpoint:Integer] [, Object:String] [, Oper:Integer] [, Mode:Integer] [, context:Integer]):Bool Базовая процедура для определения прав доступа пользователя в рамках привилегии к объекту доступа "Действие".
```

**Параметры:**

PrivID – идентификатор привилегии.
bpoint – идентификатор точки доступа.
Object – идентификатор объекта доступа.
Oper – идентификатор пользователя.
Mode – режим. Параметр принимает одно из значений:
- ACS_OnlyCheck – выполнять только проверку доступа к объекту.
- ACS_CreateError – в случае отказа в доступе будет выведено сообщение об
ошибке.
- ACS_PutInLog – вставлять запись в журнал аудита в случае отказа в доступе.
- ACS_OftenUsed – в случае отказа в доступе будет выведено сообщение об
ошибке и добавлена запись в журнал аудита.
context – контекст вызова ФПД, определяющий место (цель) проверки доступа к объекту.
Параметр принимает одно из значений:
- CNTX_None – пустое значение.
- CNTX_Admin – административная привилегия.
- CNTX_Input – при вводе операциониста.
- CNTX_BilFactura – при проверке доступа к счетам-фактурам.
- CNTX_BilBookEntry – при проверке доступа к записям книги.

**Возвращаемое значение:**



## Процедура: `CheckObjectRestriction`

```rsl
CheckObjectRestriction (PrivID:Integer, Mode:Integer, bpoint:Integer, tableName:String, whereCond:String, Object:String, [context:Integer, ] Oper:Integer):Bool
```

## Процедура: `GetObjectRestriction`

```rsl
GetObjectRestriction(sql_query:String, PrivID:Integer, [Oper:Integer, ], [TableAlias:String, ] [context:Integer, ] FileName:String, str_from:String):Bool
```

## Процедура: `определения`

```rsl
прав доступа для выборки. Процедура по номеру привилегии возвращает условие доступа (в виде строки SQL-запроса) для заданного операциониста к таблице объекта.
```

**Параметры:**

sql_query – условие, которое нужно подставить в запрос после Where.
PrivID – идентификатор привилегии.
Oper – идентификатор пользователя.
TableAlias – псевдоним таблицы объекта доступа в SQL-запросе.
context – контекст вызова ФПД, определяющий место (цель) проверки доступа к объекту.
Параметр принимает одно из значений:
- CNTX_None – пустое значение.
- CNTX_Admin – административная привилегия.
- CNTX_Input – при вводе операциониста.
- CNTX_BilFactura – при проверке доступа к счетам-фактурам.
- CNTX_BilBookEntry – при проверке доступа к записям книги.
FileName – наименование таблицы объекта доступа.
str_from – строка, которую нужно подставить в SQL-запрос после From.

**Возвращаемое значение:**



## Процедура: `IsAccessToAc`

```rsl
IsAccessToAc (Account:String, FIID:Integer, Oper:Integer, Chapter:Integer):Integer
```

## Процедура: `IsAccessToAcAlt`

```rsl
IsAccessToAcAlt (Oper:Integer, Type:String):String
```

## Процедура: `IsAccessToCl`

```rsl
IsAccessToCl (val:Integer, val:Integer):String
```

## Процедура: `IsAccessToOperInf`

```rsl
IsAccessToOperInf (Oper1:Integer, Oper:Integer):String
```

## Процедура: `GenerateReference`

```rsl
GenerateReference(RefID:Integer, Reference:String, ObjKind:Integer, Variant, buff: Record [, Date:Date] [, RefBranch:Integer]  [, AtnmTrn:String]):Integer
```

## Процедура: `GetReferenceIDByType`

```rsl
GetReferenceIDByType (ObjectType:Integer, RefType:Integer, RefID:Integer):Integer
```

## Процедура: `RestoreReference`

```rsl
RestoreReference (RefID:Integer, Reference:String [, Date:Date] [, Time:Time]):Integer
```

## Процедура: `CalcEqSumAccountFromSum`

```rsl
CalcEqSumAccountFromSum (Chapter:Integer, Account:String, Currency:Long, Cldate:Date, Sum:Money, SumEq:Money):Bool
```

## Процедура: `CalcSumAccountFromEqSum`

```rsl
CalcSumAccountFromEqSum (Chapter:Integer, Account:String, Currency:Long, cldate:Date, SumEq:Money, Sum:Money):Bool
```

## Процедура: `DeleteRegistryValue`

```rsl
DeleteRegistryValue (KeyPath:String [, ObjectID:Integer] [, RegKind:Integer]):Bool
```

## Процедура: `GetIniString`

```rsl
GetIniString (Keyname:String, NameIni:String, Variant, DisableMes:Bool, Integer):String
```

## Процедура: `GetRegistryValue`

```rsl
GetRegistryValue (PathKeyVal:String, TypeValue:Integer , Param:Variant [, ErrCode:Integer] [, UseINI:Bool] [, OperNum:Integer]):Integer
```

## Процедура: `SetDefaultRegistryValue`

```rsl
SetDefaultRegistryValue (KeyPath:String, RegValue:Variant):Bool
```

## Процедура: `SetDprtRegistryValue`

```rsl
SetDprtRegistryValue (KeyPath:String, RegValue:Variant [, DprtID:Integer] [, BlockUserValue:Bool]):Bool
```

## Процедура: `SetRegistryValue`

```rsl
SetRegistryValue (Path:String, Value:Variant [, Oper:Integer] [, BlockUserValue:Bool]):Bool
```

## Процедура: `WorkMode_DepoCorAccPos`

```rsl
WorkMode_DepoCorAccPos ():Bool
```

## Процедура: `ClearOraSessionAction`

```rsl
ClearOraSessionAction()
```

## Процедура: `SetOraSessionAction`

```rsl
SetOraSessionAction(ActionName:String)
```

## Процедура: `IsShedulerRunning`

```rsl
IsShedulerRunning ():Bool
```

## Процедура: `RaiseUserEvent`

```rsl
RaiseUserEvent (UserEventCode:String):Integer;
```

## Процедура: `AL_GetErrorInfo`

```rsl
AL_GetErrorInfo([ClearErrLog:Bool]):Object
```

## Процедура: `CreateErrMsg`

```rsl
CreateErrMsg(stat:Integer [, FormatParam:Variant])
```

## Процедура: `CreateWarning`

```rsl
CreateWarning([WarnMode:Integer] stat:Integer [, FormatParam:Variant])
```

## Процедура: `DisplayError`

```rsl
DisplayError ()
```

## Процедура: `GetWarnings`

```rsl
GetWarnings([bInitWarnings:Bool]):TArray
```

## Процедура: `InitError`

```rsl
InitError ()
```

## Процедура: `MemoryError`

```rsl
MemoryError ([stat:Integer] [, errMsg:String])
```

## Процедура: `CPCheckSignature`

```rsl
CPCheckSignature (CryptoSysID : Integer, SignedStr : String, [SignID : Long], [PIB : String]) : Bool
```

## Процедура: `CPSetSignature`

```rsl
CPSetSignature (CryptoSysID : Integer, StrForSign : String, Signature : String, DocKind : Integer, DocumentID : Integer, String, SignatoryPartyID : Integer, PrimaryDocKind : Integer, SignKind : Integer, ErrorCode : Integer, [SignID : Long]) : Bool
```

## Процедура: `CPSetSignatureFile`

```rsl
CPSetSignatureFile (CryptoSysID:Integer, file:String [, file_dest:String]) : Bool
```

## Процедура: `EndKeyCashing`

```rsl
EndKeyCashing ()
```

## Процедура: `ListAccount`

```rsl
ListAccount (AccountBuf:File, Record, Chapter:Integer, FinInstr:Variant, Account:String [, ListInBranch:Bool] [, BalanceAccount:String] [, Department:Integer] [, ExclRub:Bool]):Bool
```

## Процедура: `ListChapter`

```rsl
ListChapter (ChapterBuff:Object):Bool
```

## Процедура: `ListDepartment`

```rsl
ListDepartment (DepartmentBuff:File, Record):Bool
```

## Процедура: `осуществляется`

```rsl
выбор филиала из предоставляемого системой списка филиалов.
```

**Параметры:**

DepartmentBuff – параметр (структура dp_dep), определяющий буфер, в который будет
помещена запись о выбранном филиале.

**Возвращаемое значение:**



## Процедура: `ListOper`

```rsl
ListOper (BuffOper:Record [, OnlyOpen:Integer] [, OperNum:Integer]):Bool
```

## Процедура: `CompareStringsSimilar`

```rsl
CalcSumAccountFromEqSum (Chapter:Integer, Account:String, Currency:Long, cldate:Date, SumEq:Money, Sum:Money, CmpRes:Bool):Bool
```

## Процедура: `CompareStrWithMasks`

```rsl
CompareStrWithMasks (masks:String, str:String [, mode:Integer]):Integer
```

## Процедура: `RegExMatch`

```rsl
RegExMatch (str:String, regexStr:String):Bool
```

## Процедура: `Unkn_GetAccountActive`

```rsl
Unkn_GetAccountActive ([Node:Integer, ] [FIID:Integer, ] [Mode:Integer], [NPS:Integer], [AccountID:String]):String
```

## Процедура: `Unkn_GetAccountPassive`

```rsl
Unkn_GetAccountPassive ([Node:Integer, ] [FIID:Integer, ] [Mode:Integer], [NPS:Integer], [AccountID:String]):String
```

## Процедура: `SetDialogFlag`

```rsl
SetDialogFlag (flag:Integer ):Integer
```

## Процедура: `GetDialogFlag`

```rsl
GetDialogFlag ():Integer
```

## Процедура: `SizeSum`

```rsl
SizeSum ([Val:Integer]):Integer
```

## Процедура: `CreateEKDoc`

```rsl
CreateEKDoc (Maket:String [, Date:Date [, Chapter:Integer]]):String
```

## Процедура: `AddCategForObject`

```rsl
AddCategForObject(ObjectType:Integer, ObjectID:Integer, GroupID:Integer, AttrID:Integer [, Date:Date] [, OperationID:Integer] [, ID_Step:Integer]):Integer
```

## Процедура: `AddMessageList`

```rsl
AddMessageList (message:String):Integer
```

## Процедура: `AL_GetHashValueFile_3411_2012`

```rsl
AL_GetHashValueFile_3411_2012 (FileName:String, HashValue:String):Integer
```

## Процедура: `CB_CarryPlanDocuments`

```rsl
CB_CarryPlanDocuments (PaymentID:Integer, DateBefore:Date, OperationID:Integer, StepID:Integer):Integer
```

## Процедура: `CB_CritWaitAccept`

```rsl
CB_CritWaitAccept(Type:Long, Desc:String, RoleID:Long, ObjectType:Integer, ObjectID:Long, ConFuncID:Long, RejFuncID:Long, Param:String):Integer
```

## Процедура: `CB_GetDprtPartyCode`

```rsl
CB_GetDprtPartyCode(DepartmentID:Integer, CodeKind:Integer [, Code:String]):Integer
```

## Процедура: `CB_InsertUpdateMarketRate`

```rsl
CB_InsertUpdateMarketRate(buf:File, Record, Tbfile, valintmarketrate:Tarray, error:String):Integer
```

## Процедура: `CB_ListCashOprKind`

```rsl
CB_ListCashOprKind([Code:String], [Desc:String]):Bool
```

## Процедура: `CB_Scrol_ImageData`

```rsl
CB_Scrol_ImageData (ObjectType:Integer, ObjectID:String, [Review:Bool], [Name:String], [FormatStr:String]):Integer
```

## Процедура: `CheckOperAndPswd`

```rsl
CheckOperAndPswd(Oper:Integer, Password:String):Integer
```

## Процедура: `CheckOperDayPermission`

```rsl
CheckOperDayPermission(CurDate:Date, Department:Integer):Bool
```

## Процедура: `ClientHasSalaryAccount`

```rsl
ClientHasSalaryAccount(ClientID:Integer):Bool
```

## Процедура: `ConfWin`

```rsl
ConfWin(Text:Array, Button:Array, NumButton:Integer):Integer
```

## Процедура: `CreateDemoModeLicAlert`

```rsl
CreateDemoModeLicAlert (RestrictionID:Integer):Integer
```

## Процедура: `Delay`

```rsl
Delay (ms:Integer)
```

## Процедура: `EAM_Def_Ident_Value`

```rsl
EAM_Def_Ident_Value(IdentName:String, ObjectType:Integer, ObjectID:String):String
```

## Процедура: `EAM_GenTextTemplate`

```rsl
EAM_GenTextTemplate(EventID:Integer, [HeaderT:String], TextT:String, [HeaderM:String], [TextM:STRING]):Integer
```

## Процедура: `EAM_InsertEvent`

```rsl
EAM_InsertEvent(Events:ARRAY):Integer
```

## Процедура: `GetDocInf`

```rsl
GetDocInf (document:Record, docinf:Record):Integer
```

## Процедура: `GetDprtTimeZone`

```rsl
GetDprtTimeZoneGetDprtTimeZone([DprtCode:Int] [, OnDateIn:Date] [, OnTimeIn:Time] [, OnDateOut:Date] [, On:Time]):Integer
```

## Процедура: `GetFioOper`

```rsl
GetFioOper(Num_oper:Integer, String, [Short:Bool]):String
```

## Процедура: `GetGlobalParameter`

```rsl
GetGlobalParameter (Name:String [, DelParam:Bool])
```

## Процедура: `GetIdentProgram`

```rsl
GetIdentProgram():Integer
```

## Процедура: `GetImage`

```rsl
GetImage (ObjectType:Integer, ObjectID:String, ImageType:Integer, ImageID:Long):Integer
```

## Процедура: `GetLastFinalDate`

```rsl
GetLastFinalDate ([Chapter:File, Integer, Record]):Date
```

## Процедура: `GetNDSRateByDate`

```rsl
GetNDSRateByDate (NDSRate:Double [, NDSRateID:Integer] [, date:Date]):Bool
```

## Процедура: `GetOperDprtTimeZone`

```rsl
GetOperDprtTimeZone([OperCode:Integer] [, OnDateIn:Date] [, OnTimeIn:Time] [, OnDateOut:Date] [, OnTimeOut:Time]):Integer
```

## Процедура: `GetPartyBankruptStatus`

```rsl
GetPartyBankruptStatus (PartyID:Integer, OnDate:Date, BankruptStatus:Integer):Integer
```

## Процедура: `GetPriorityArrestClaim`

```rsl
GetPriorityArrestClaim(Account:String, Chapter:Integer, FIID:Integer [BankDate:Date], Priority:Integer):Integer
```

## Процедура: `GetProgramInformation`

```rsl
GetProgramInformation([ProgramVersion:String] [, DatabaseVersion:String])
```

## Процедура: `GetRegValueChilds`

```rsl
GetRegValueChilds (KeyPath:String, Append:Bool, Array:Array):Integer
```

## Процедура: `GetSumArrestClaim`

```rsl
GetSumArrestClaim(Account:String, Chapter:Integer, FIID:Integer [BankDate:Date], Priority:Integer, Sum:Money):Integer
```

## Процедура: `GetSumSpecialClaim`

```rsl
GetSumSpecialClaim(Account:String, Chapter:Integer, FIID:Integer [BankDate:Date], Sum:Money):Integer
```

## Процедура: `GetUfebsControlDate`

```rsl
GetUfebsControlDate( ControlDate:Date, Err:String)
```

## Процедура: `iInsertEventLog`

```rsl
iInsertEventLog(EventType:Integer, ObjectType:Integer, Params:String):Integer
```

## Процедура: `iGetEventSourceInfo`

```rsl
iGetEventSourceInfo(Department:Integer, Branch:Integer, XML:String):Integer
```

## Процедура: `InsertAccountPhase`

```rsl
InsertAccountPhase(Account:String, Chapter:Integer, Code_Currency:Integer):Integer
```

## Процедура: `InsertAnaliticSubAcc`

```rsl
InsertAnaliticSubAcc (AnaliticsID:Integer, FIID:Integer, Chapter:Integer, Account:String):Integer
```

## Процедура: `InsertConsolidatedClaim`

```rsl
InsertConsolidatedClaim(ClaimID:Integer, AccountId:Integer, AnalyticalAccountId:Integer, EnterDate:Date, DocNumber:String, StartAmount:Money, Initiator:Integer, error:String, [ClaimKind:Integer], [RestKind:Integer], [Incremental:Bool], [FullArest:Bool], IsAuto:Bool):Integer
```

## Процедура: `IsAccountFullyArrested`

```rsl
IsAccountFullyArrested(Account:String, Chapter:Integer, FIID:Integer [BankDate:Date]):Integer
```

## Процедура: `isDLMRuning`

```rsl
isDLMRuning():bool
```

## Процедура: `Qsort`

```rsl
Qsort (p_array:Object, p_cmp_proc:Variant)
```

## Процедура: `IsIDENTPROGRAM`

```rsl
IsIDENTPROGRAM(cIdentProgram:String):Integer
```

## Процедура: `LoadImageObj`

```rsl
LoadImageObj (FileName:String, ObjectType:Integer, ObjectID:String, ImageType:Integer):Bool
```

## Процедура: `OemToUtf8`

```rsl
OemToUtf8(instr:String):String
```

## Процедура: `OraTrnRollbackToSavePoint`

```rsl
OraTrnRollbackToSavePoint(SavePoint:String):Integer
```

## Процедура: `OraTrnSavePoint`

```rsl
OraTrnSavePoint(SavePoint:String):Integer
```

## Процедура: `PathIsNetworkPath`

```rsl
PathIsNetworkPath([pszPath:String]):Bool
```

## Процедура: `PartyBankruptWarning`

```rsl
PartyBankruptWarning (PartyID:Integer, ExtendedNotify:Bool, NoDialog:Bool, BankruptStatus:Integer, Message:String):Integer
```

## Процедура: `PT_CreateSettAcc`

```rsl
PT_CreateSettAcc(settacc:Record):Integer
```

## Процедура: `PT_DeleteSettAcc`

```rsl
PT_DeleteSettAcc(settacc:Record):Integer
```

## Процедура: `PT_UpdateSettAcc`

```rsl
PT_UpdateSettAcc(settacc1:Record, settacc2:Record):Integer
```

## Процедура: `RebuildResultRestrict`

```rsl
RebuildResultRestrict (PrivID:Integer, OperID:Integer, IsExist:Bool, RestValue:String):Integer
```

## Процедура: `RsBeginAction`

```rsl
RsBeginAction(tm:Integer, msg:String, flags:Integer):Bool
```

## Процедура: `RsEndAction`

```rsl
RsEndAction():Bool
```

## Процедура: `RunProgramWait`

```rsl
RunProgramWait (ProgName:String, CmdArgs:String, [fRemote:Bool], [fDetached:Bool], [timeOut:Integer]):Integer
```

## Процедура: `RunVisual`

```rsl
RunVisual (RlibName:String, RepName:String):String
```

## Процедура: `SEIEM_WriteEvent`

```rsl
SEIEM_WriteEvent(Event:Integer, Param1:String, Param2:String, [IsTrn:Bool]):Integer
```

## Процедура: `SendFileToTerm`

```rsl
SendFileToTerm ([local_name:String] [, remote_name:String]):Bool
```

## Процедура: `SendNotice`

```rsl
SendNotice (Desc: String, Recepient: Integer):Bool
```

## Процедура: `SetCtgUserSyncEnable`

```rsl
SetCtgUserSyncEnable (param:Bool):Bool
```

## Процедура: `SetGlobalParameter`

```rsl
SetGlobalParameter (Name:String, Param:Variant): Bool
```

## Процедура: `SetNewPswdToUserGroup`

```rsl
SetNewPswdToUserGroup (GroupID:Integer, Password:String):Integer
```

## Процедура: `SetNewPswdToUserGroup`

```rsl
позволяет задать начальный пароль группе пользователей. Процедуру следует использовать только в интересах конкретного клиента, при этом следует иметь в виду, что в указанную процедуру не встроены меры безопасности, необходимые при смене пароля: · не выполняется проверка пароля на совпадение с предыдущими паролями – указанный пароль устанавливается и в случае совпадения; · в качестве пароля может выступать любая комбинация символов любой длины, за исключением пустой строки (в этом случае выполнение процедуры приводит к возникновению ошибки); · процедура не использует механизм подтверждения критичных действий, т.е. выполняется сразу после вызова, без дополнительных подтверждений и запросов; · права доступа пользователя, вызвавшего макрос с функцией, на управление пользователями, входящими в группу, также не проверяются: пароль устанавливается каждому пользователю группы. Таким образом, соблюдение мер безопасности возлагается на программиста, использующего процедуру. При запуске процедуры выполняются следующие действия: Внимание! Запуск процедуры может осуществить только пользователь с уровнем доступа "Администратор безопасности". · указанный пароль записывается в базу данных в зашифрованном виде; · установленное значение пароля фиксируется в истории смены паролей – для проверки того, что смена пароля была произведена при следующем входе в систему; · устанавливается признак необходимости смены пароля при следующем входе; · обнуляется счетчик попыток ввода пароля; · дата последнего входа пользователя в систему устанавливается равной текущей (с целью предотвращения блокировки пользователя, который длительное время не входил в систему).
```

**Параметры:**

GroupID – идентификатор группы пользователей.
Password – значение устанавливаемого пароля.

**Возвращаемое значение:**



## Процедура: `SetOperDay`

```rsl
SetOperDay ([OperDay:Date]):Bool
```

## Процедура: `SplitFullINN`

```rsl
SplitFullINN (FullINN:String, INN:String, KPP:String):Integer
```

## Процедура: `UOL_WEB_SEARCH_IDENT_CLIENT`

```rsl
UOL_WEB_SEARCH_IDENT_CLIENT:Integer
```

## Процедура: `Utf8ToOem`

```rsl
Utf8ToOem(instr:String):String
```

## Процедура: `WEB_CB_InsertUpdateOprKDoc`

```rsl
WEB_CB_InsertUpdateOprKDoc(Oprkdoc:Trechandler, OprkdateArray:Tarray, OprstkindArray:Tarray, OprstvalArray:Tarray):Bool
```

## Процедура: `WriteOperLog`

```rsl
WriteOperLog(operation:Integer, file_procedure:FILE, String [buffer1:FILE, Record] [buffer2:FILE, Record]):Bool
```

## Класс: `RslBilFacturaBatchCharger`

```rsl
RslBilFacturaBatchCharger()
```

Класс, используемый для выполнения пакетной операции создания счетов-фактур.

**Методы:**

add(factura:Record, 
facturaLineArray:TArray, 
operationId:Integer, 
stepId:Integer, 
[DocKind:Integer], DocID:String)

## Процедура: `BFAnnulBilFactura`

```rsl
BFAnnulBilFactura (FacturaID:Integer, AnulConnnectedBF:Bool):Bool
```

## Процедура: `BFCalcNDSAmount`

```rsl
BFCalcNDSAmount(FIID:Integer, Amount:Money, IsIncluded:Bool, Rate:Double, NDSAmount:Money):Bool
```

## Процедура: `BFCreateBilBookEntry`

```rsl
BFCreateBilBookEntry (FacturaID:Integer, docs:TArray, regDate:Date, BilBookEntryId:Integer):Bool
```

## Процедура: `BFCreateBilFactura`

```rsl
BFCreateBilFactura (Factura:Record, facturaLine:TArray, FacturaId:Long):Bool
```

## Процедура: `BFDeleteBilBookEntry`

```rsl
BFDeleteBilBookEntry (BookEntryID:Integer):Bool
```

## Процедура: `BFDeleteBilFactura`

```rsl
BFDeleteBilFactura (FacturaID:Integer, AnulConnnectedBF:Bool):Bool
```

## Процедура: `BFFindBilBookEntryList`

```rsl
BFFindBilBookEntryList (FacturaID:Integer, arrayId:TArray):Bool
```

## Процедура: `MoveAccount`

```rsl
MoveAccount ([Chapter:Integer, ] [OldAcc:String, ] [NewAcc:String [, Currency:Integer] [, Balance:String]):Integer
```

## Процедура: `RegPairedAccounts`

```rsl
RegPairedAccounts (prm0 : Integer, prm1 : Date, prm2 : String, prm3 : String, prm4 : Integer) : Integer
```

## Класс: `IRSCryptoObj`

```rsl
IRSCryptoObj ():Object Базовый класс для объектов, реализующих работу с ЭЦП. Любой объект, над которым требуется проводить криптодействия, должен являться наследником от этого класса. Использование методов ExecCryptoAction , InsertExternal возможно только с экземплярами объектов, являющихся наследниками от IRSCryptoObj (например, производные классы RsbPayment, RsbMessage). В макромодуле невозможно сконструировать объект данного класса, IRSCryptoObj используется только для операций динамического приведения типа.
```

## Метод: `начала`

```rsl
кэширования пароля/ключа. Метод рекомендуется использовать при обработке группы документов (или выполнении нескольких криптодействий над одним объектом). При запущенном методе запрос пароля/ключа выполняется один раз для всего пакета обрабатываемых документов, в противном случае, пароль/ключ запрашивается при начале каждого криптодействия (режим по умолчанию).
```

**Возвращаемое значение:**



## Метод: `обеспечивает`

```rsl
проверку ЭЦП буфера в памяти.
```

**Параметры:**

ContextID 
- 
идентификатор 
контекста 
вызова 
ответной 
точки 
применения
криптографии (ИКПОО).
Buffer – буфер памяти, содержащий подпись.

**Возвращаемое значение:**



## Метод: `получения`

```rsl
идентификатора ключа (ПИКК)
```

последнего 
выполненного
криптодействия.

**Возвращаемое значение:**



## Метод: `вставки`

```rsl
внешней подписи объекта в базу данных.
```

**Параметры:**

ContextID – идентификатор контекста вызова начальной точки применения
криптографии (ИКПОО).
CryptoObject – объект, для которого необходимо вставить внешнюю подпись. Объект,
описываемый этим параметром, должен быть наследником от класса
IRSCryptoObj
.
Sign – внешняя ЭЦП.
KeyCode – идентификатор ключа внешней подписи.
KeyOwnerPatryID – идентификатор субъекта-владельца ключа внешней подписи.

**Возвращаемое значение:**



## Метод: `обеспечивает`

```rsl
проверку необходимости выполнения криптодействия (наличие зарегистрированных настроек). Метод может вызываться перед выполнением метода ExecCryptoAction , это позволяет избежать необходимости конструирования экземпляра обрабатываемого объекта.
```

**Параметры:**

ContextID – идентификатор контекста вызова точки применения криптографии
(ИКПОО).
DocKind – вид первичного документа. Если значение параметра равно 0, процедура
проверяет необходимость выполнения криптодействий в указанном контексте
ContextID и отбирает такие ТПК, для криптонаправления которых в качестве
первичного документа задан 0.

**Возвращаемое значение:**



## Класс: `RsbAccCategory`

```rsl
RsbAccCategory ():Object Конструктор класса создает объект, обладающий свойствами, аналогичными параметрам функций открытия лицевого счета по категориям учета.
```

**Свойства:**

AccDoc – буфер для найденного/открытого счета; тип File.
ActionDate – дата действия; тип Date.
ActivateDate – дата актуализации счета; тип Date.
BackoutAccount – признак отката созданного счета при откате шага; тип Bool.
Branch – узел ТС; тип Integer.
ChangeOpenDate – признак переустановки даты открытия в случае, когда счет есть, но
дата начала меньше требуемой; тип Bool.
CurryCurrency – валюта счета; тип Integer.
EqvFIID – код валюты эквивалента для счета с НВПИ; тип Integer.
FIRole – роль финансового инструмента; тип Integer.
Initiator – операционист; тип Integer.
IsMass – признак режима массовой обработки; тип Bool.
IsNVPI – признак необходимости открытия счета с НВПИ; тип Bool.
NumberForAcc – номер существующего счета, который необходимо привязать к
документу; тип String.
OpenMode – режим открытия счета; тип Integer.
ORScheme – схема переоценки; тип Integer.
PairAccMode – режим выбора парного счета; тип Integer.
PeriodID – диапазон срочности (для срочной категории); тип Integer.
PrimaryDoc – первичный документ; тип Object.
RateOffs – величина смещения (в днях) даты курса для счета с НВПИ; тип Integer.
RealOpenMode – фактический режим открытия; тип Integer.
Template – номер шаблона; тип Integer.

**Методы:**

FindAndOpenAccount (CodeCat:String, OperationID:Integer, StepID:Integer):String

## Класс: `RsbObjAttrListData`

```rsl
RsbObjAttrListData()
```

## Класс: `RsbObjAttrPanData`

```rsl
RsbObjAttrPanData()
```

## Класс: `RsbObjCategories`

```rsl
RsbObjCategories (ObjectType:Integer, ObjectID:String):Object Конструктор класса создает объект, который представляет собой категорию для объекта системы с типом ObjectType и идентификатором ObjectID. Работа с категорией ведется в памяти. Чтобы сохранить информацию о ней в базе данных, необходимо вызвать метод Save(). Если необходимо создать категорию для объекта системы, который еще не существует в базе данных, то нужно действовать по следующему алгоритму: · При создании экземпляра класса RsbObjCategories в качестве параметра ObjectID указать временный идентификатор объекта системы, которого гарантированно нет в базе данных (например, отрицательное значение). · Создать объект системы и получить его реальный идентификатор. · После завершения работы с категорией сохранить ее в базе данных с помощью метода Save(), при этом в качестве параметра ObjectID  указать реальный идентификатор объекта системы.
```

**Методы:**

ConnectAttr 
(GroupID:Integer, 
AttrID: 
String, 
Variant, 
CodeList:String, 
Variant,
NumList:String, Variant, Date:Date):Integer

## Метод: `присоединяет`

```rsl
признак к объекту.
```

**Параметры:**

GroupID  группа признаков, к которой принадлежит объект;
AttrID  идентификатор признака;
CodeList  номер уровня признака;
NumList  номер признака в уровне;
Date – дата, на которую действительно значение категории. Эта дата может
использоваться для получения значения(ий) категории.
DisconnectAttr (GroupID:Integer, AttrID:Integer):Integer

## Класс: `RsbObjLinkData`

```rsl
RsbObjLinkData()
```

## Процедура: `ListObjAttr`

```rsl
ListObjAttr (ObjType:Integer, GroupID:Integer, ObjAttrBuf:File, Record, Tbfile, TRecHandler [, SelectParents:Bool]):Bool
```

## Процедура: `MC_BatchFindAndOpenAccount`

```rsl
MC_BatchFindAndOpenAccount(CatCode:String, FD:Object [, ActionDate:Date] [, Currency:Integer] [, ORScheme:Integer] [, FIRole:Integer] [, Branch:Integer] [, Initiator:Integer] [, ActivateDate:Integer] [, BackoutAccount:Integer] [, ChangeOpenDate:Bool] [, IsNVPI:Bool] [, EqvFIID:Integer] [, RateDate:Integer] [, ID_Operation:Integer] [, ID_Step:Integer]):Bool
```

## Процедура: `MC_CalcPeriodBound`

```rsl
MC_CalcPeriodBound (CalcDate:Date, Period:Record, IsLowBound:Bool):Date
```

## Процедура: `MC_ConvertIndexDateToDate`

```rsl
MC_ConvertIndexDateToDate (categ:Record, IndexDate:Integer):Date
```

## Процедура: `MC_FindAndCloseAccount`

```rsl
MC_FindAndCloseAccount (CodeCat:String, fd:Object [, ActionDate:Date] [, FIRole:Integer] [, CurryCurrency:Integer] [, CloseMode:Integer]):Integer
```

## Процедура: `MC_FindAndOpenAccount`

```rsl
MC_FindAndOpenAccount (CodeCat: String, FD:Variant [, ActionDate: Date] [, IsMass:Integer] [, IsOpen:Integer] [, AccBuf: TRecHandler] [, CurryCurrency:Integer] [, ORScheme:Integer] [, PairAccMode:Integer] [, NumberForAcc:String] [, FIRole:Integer] [, Результат:Integer] [, AccDoc:File, Record, TBFile, TRecHandler] [, DepartmentID:Integer] [, Инициатор:Integer] [, ActivateDate:Date] [, BackoutAccount:Bool, Integer] [, ChangeOpenDate:Bool] [, IsNVPI:Bool] [, EqvFIID:Integer] [, RateOffs:Integer]):):String
```

## Процедура: `MC_FindAndOpenCommonAcc`

```rsl
MC_FindAndOpenCommonAcc (категория:String [, Дата:Date] [, Режим:Integer], Шаблон:Integer, Характеристики:Record[, Диапазон:Integer] [, Валюта:Integer] [, Счет:String] [, Узел ТС:Integer] [, AccBuf:File, Record, Tbfile, Trechandler] [, Результат:Integer] [, Initiator:Integer] [, PairAccMode:Integer] [, BackOutAccount:Bool] [, ChangeOpenDate:Bool] [, IsNVPI:Bool] [, EqvFIID:Integer] [, RateOffs:Integer]):String
```

## Процедура: `MC_FindAndOpenCommonAccByFD`

```rsl
MC_FindAndOpenCommonAccByFD (CodeCat:String, FD:Variant [, ActionDate: Date] [, IsMass:Integer] [, IsOpen:Integer] [, AccBuf: Record] [, CurryCurrency:Integer] [, ORScheme:Integer] [, PairAccMode:Integer] [, NumberForAcc:String] [, FIRole:Integer] [, RealOpenMode:Integer] [, AccDoc:Integer] [, DepartmentID:Integer] [, Инициатор:Integer] [, ActivateDate:Date] [, BackOutAccount:Bool] [, ChangeOpenDate:Bool] [, IsNVPI:Bool] [, EqvFIID:Integer] [, RateOffs:Integer]):String
```

## Процедура: `MC_FindComMCACCDOC`

```rsl
MC_FindComMCACCDOC (CatID:Integer, Currency:Integer, PeriodID:Integer, TempNum:Integer, AccDoc:Record):Bool
```

## Процедура: `MC_FindMaxMCACCDOC`

```rsl
MC_FindMaxMCACCDOC (DocKind:Integer, DocID:Integer, CatID:Integer, Currency:Integer, ActionDate:Date, AccDoc:Record, FIRole:Integer, DepartmentID:Integer):Bool
```

## Процедура: `MC_FindMCCATEG`

```rsl
MC_FindMCCATEG (CodeCat:String [, categ:Record]):Bool
```

## Процедура: `MC_FindMCTEMPL`

```rsl
MC_FindMCTEMPL (CatID:Integer, TempleNum:Integer, Templ:Record):Bool
```

## Процедура: `MC_FindUseMCACCDOC`

```rsl
MC_FindUseMCACCDOC (DocKind:Integer, DocID:Integer, CatID:Integer, FIRole:Integer, Currency:Integer, AccDoc:Record [, DepartmentID:Integer]):Bool
```

## Процедура: `MC_GetAccountNumber`

```rsl
MC_GetAccountNumber (CodeCat:String, FD:Object [, ActionDate:Integer] [, IsMass :Integer] [, CurryCurrency:Integer] [, FIRole:Integer] [, Узел ТС:Integer]):String
```

## Процедура: `MC_GetBalance`

```rsl
MC_GetBalance (ACCDOC:Record, TEMPL:Record):String
```

## Процедура: `MC_GetBalanceCb`

```rsl
MC_GetBalanceCb (CodeCat:String, Chapter:Integer, FIID:Integer, Date:Date, Balance:MoneyL, Err:Integer):Bool
```

## Процедура: `MC_GetClient`

```rsl
MC_GetClient (ACCDOC:Record, Templ:Record):Integer
```

## Процедура: `MC_GetExistAccount`

```rsl
MC_GetExistAccount (CodeCat:String, DocKind:Integer, DocID:Integer, FIRole:Integer, CurryCurrency:Integer [, ActionDate:Date] [, DepartmentID:Integer]):String
```

## Процедура: `MC_GetPeriodForCurrAcc`

```rsl
MC_GetPeriodForCurrAcc (CodeCat:String, DocKind:Integer, DocID:Integer, FIRole:Integer, Curency:Integer, PeriodKind:Integer [, ShowError:Bool], Period:Trechandler [, DepartmentID:Integer]):Integer
```

## Процедура: `SetLinkedObject`

```rsl
SetLinkedObject ([rslRole:Integer, ] [rslObjectType:Integer, ] [rslObjectID:File, Record, String, ] [rslAttrType:Integer, ] [rslAttrID:String, ] [rslCanOverwrite:Bool]):Integer
```

## Процедура: `GetLinkedObject`

```rsl
GetLinkedObject (rslRole:Integer, rslObjectType:Integer, rslObjectID:File, Record, String, rslAttrType:Integer, rslAttrID: File, Record, String):Integer
```

## Процедура: `SetLinkedObjectPacket`

```rsl
SetLinkedObjectPacket(ObjLinkData:Array):Integer
```

## Процедура: `CB_GetRegistry`

```rsl
CB_GetRegistry (ObjectType:Integer, ObjectID:Integer, RegPartyKind:Integer, RegDocKind:Integer, Objrgdoc:Record, Number:String):Integer
```

## Процедура: `CB_GetRegistry_Hier`

```rsl
CB_GetRegistry_Hier (PartyID:Integer, RegParty:Integer, DocKind:Integer, Result:Integer, RegNum:String, RegDate:Date, buff:Record):Integer
```

## Процедура: `CheckObjAttrPresence`

```rsl
CheckObjAttrPresence ([return_value:Bool], ObjType:Integer [, ObjID:String] [, GroupID:Integer] [, AttrID:Integer] [, Code:String] [, Num:String] [, Chld:Bool]):Bool
```

## Процедура: `ConnectObjAttr`

```rsl
ConnectObjAttr ([return_value:Integer, ] ObjType:Integer, ObjID:String [, GroupID:Integer] [, AttrID:Integer] [, Code:String] [, Num:String] [, DateRSL:Date]):Bool
```

## Процедура: `GetListLinkedObjects`

```rsl
GetListLinkedObjects(objLinkData:Array, objType:Integer, objID:String [, BankDate:Date] [, getInverseLinks:Integer] [, GroupID:Integer] [, attrType:Integer]):Integer
```

## Процедура: `GetMainObjAttr`

```rsl
GetMainObjAttr ([return_value:Integer, ] ObjType:Integer, ObjID:String, GroupID:Integer [, AttrID:Integer] [, Code:String] [, Num:String])
```

## Процедура: `IsObjectLinked`

```rsl
IsObjectLinked (AttrType:Integer, Attr:File, Record, String, ObjectType:Integer, Role:Integer [, Object:File, Record]):Bool
```

## Процедура: `FindObjCodeForDate`

```rsl
FindObjCodeForDate (ObjectType:Integer, CodeKind:Integer, ObjectID:Long, BankDate:Date, buffOBJCODE:Record):Integer
```

## Процедура: `ObjAttr_FindClose`

```rsl
ObjAttr_FindClose ():Variant
```

## Процедура: `ObjAttr_FindFirst`

```rsl
ObjAttr_FindFirst ([mParm:File, Record, ] [ObjType:Integer, ] [ObjID:String, ] [GroupID:Integer]):Integer
```

## Процедура: `ObjAttr_FindNext`

```rsl
ObjAttr_FindNext ([mParm:File, Record]):Integer
```

## Процедура: `RestoreFromUniID`

```rsl
RestoreFromUniID ([UniCode:String, ] [Buffer:File, Record, ] [ObjType:Integer, ] [DocKind:Integer]):Bool
```

## Процедура: `UniID`

```rsl
UniID (Buffer:File, Record, TRecHandler, ObjType:Integer, DocKind:Integer):String
```
