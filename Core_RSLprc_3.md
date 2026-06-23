# Core RSLprc 3

Введение
Настоящее Руководство является частью Руководства программиста и содержит описание
переменных, классов, процедур и констант языка интерпретатора RSL, которые
используются при создании макромодулей PaymInter, Календарь, Проценты, Шлюз,
входящих в АС RS-Core V.6 ИБС RS-Bank V.6, и при написании пользователем собственных
макропрограмм. Кроме данного в состав Руководства программиста входят руководства,
содержащие описание других модулей языка RSL:
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 1" (файл Books\Tools\CoreRSLprc_1.pdf) – содержит описание модулей
BalanceInter, BankInter, BilFacturaInter, CarryDoc, cryptdlm.d32, CTInter.
· Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank
V.6. Часть 2" (файл Books\Tools\CoreRSLprc_2.pdf) – содержит описание модулей
CurrInter, FIInter, GateInter, InsCarryDoc, OprInter, PcRateInter, PTInter, RsbDataSet,
RsbObjFactory, RsSysLog, SFInter.
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
Классы

## Класс: `BatchMode`

```rsl
BatchMode (m:Integer, n:Integer):Object
```

## Класс: `PaymentFieldStringCache`

```rsl
PaymentFieldStringCache()
```

## Класс: `необходим`

```rsl
для преобразования строковых значений в идентификаторы базы данных.
```

**Методы:**

GetComissCharges(Code:String):Integer

## Класс: `PMScrolDateFltr`

```rsl
PMScrolDateFltr ()
```

## Класс: `RsbBackOfficePayment`

```rsl
RsbBackOfficePayment ()
```

## Класс: `RsbBankOrder`

```rsl
RsbBankOrder()
```

## Класс: `банковских`

```rsl
ордеров.
```

**Свойства:**

Kind_Operation – вид операции по документу (поле t_Kind_Operation таблицы
dpscshdoc_dbt); тип Integer.
LaunchOper – признак запуска дочерней операции по документу; тип Bool.
PrimDocNotes – объект класса RsbObjNotes, содержащий примечания первичного
документа.
RsbObjCategories – объект класса RsbObjCategories, содержащий категории первичного
документа.

**Методы:**

ConnectToOperation(ID_Operation:Integer, ID_Step:Integer):Bool

## Класс: `RsbBatchPaymTrn`

```rsl
RsbBatchPaymTrn()
```

## Класс: `RsbBBAddCashOrder`

```rsl
RsbBBAddCashOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbBBIncCashOrder`

```rsl
RsbBBIncCashOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbBBIncCashOrder`

```rsl
предназначен для описания первичного документа "Приходный кассовый ордер Бухгалтерии банка", является наследником класса RsbCashOrder наследует все его атрибуты. Конструктор класса RsbBBIncCashOrder ([DocumentID:Integer])
```

имеет 
параметр
DocumentID – идентификатор документа. Если параметр равен 0 или не указан,
создается новый документ.

## Класс: `RsbBBInOutCashOrder`

```rsl
RsbBBInOutCashOrder()
```

## Класс: `RsbBBOutCashOrder`

```rsl
RsbBBOutCashOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbBdTransfer`

```rsl
RsbBdTransfer()
```

## Класс: `RsbCashOrder`

```rsl
RsbCashOrder ()
```

Базовый класс первичного документа для кассовых ордеров РКО и ББ.

**Свойства:**

AutoKey – идентификатор документа (поле t_AutoKey таблицы dpscshdoc_dbt). Свойство
имеет тип Integer и доступно только для чтения.
Categories – категории документа. Свойство имеет тип Object, возвращает объект класса
RsbObjCategories (см. Руководство "Интерфейсы языка RSL для взаимодействия
с ИБС RS-Bank V.6. Часть 1") и доступно только для чтения.
ClientAccount – номер счета клиента (поле t_ClientAccount таблицы dpscshdoc_dbt); тип
String.
ConnectAppKey – поле ключа приложения балансового документа с разноской (поле
t_ConnectAppKey таблицы dpscshdoc_dbt). Свойство имеет тип String и доступно
только для чтения.
ConnectAppKind – вид приложения балансового документа с разноской (поле
t_ConnectAppKind таблицы dpscshdoc_dbt). Свойство имеет тип Integer и
доступно только для чтения.
ConnectToOper – признак "Привязывать создание документа к шагу операции"; тип Bool.
DocKind – вид документа (поле t_DocKind таблицы dpscshdoc_dbt). Свойство имеет тип
Integer и доступно только для чтения.
FIOClient – фамилия, имя и отчество клиента (поле t_FIOClient таблицы dpscshdoc_dbt);
тип String.
IsCurrency – признак валютного документа ("X" если документ валютный), поле
t_IsCurrency таблицы dpscshdoc_dbt; тип String.
Kind_Operation – вид операции по документу (поле t_Kind_Operation таблицы
dpscshdoc_dbt); тип Integer.
LaunchOper – признак "Автоматически запускать дочернюю операцию по документу"; тип
Bool.
NameIssuer – наименование чекодателя (поле t_NameIssuer таблицы dpscshdoc_dbt); тип
String.
Notes – примечания документа. Свойство имеет тип Object, возвращает объект класса
RsbObjNotes (см. Руководство "Интерфейсы языка RSL для взаимодействия с
ИБС RS-Bank V.6. Часть 1") и доступно только для чтения.
Oper – идентификатор операциониста, автора документа (поле t_Oper таблицы
dpscshdoc_dbt); тип Integer.
Origin – происхождение документа (поле t_Origin таблицы dpscshdoc_dbt); тип Integer.
PaperIssuedDate 
- 
дата 
выдачи 
документа, 
удостоверяющего 
личность 
(поле
t_PaperIssuedDate таблицы dpscshdoc_dbt); тип Date.
PaperIssuer – наименование организации, выдавшей документ, удостоверяющий
личность (поле t_PaperIssuer таблицы dpscshdoc_dbt); тип String.
PaperKind – вид документа, удостоверяющего личность (поле t_PaperKind таблицы
dpscshdoc_dbt); тип Integer.
PaperNumber – номер документа, удостоверяющего личность (поле t_PaperNumber
таблицы dpsschdoc_dbt); тип String.
PaperSeries – серия документа, удостоверяющего личность (поле t_PaperSeries таблицы
dpscshdoc_dbt); тип String.
Payment – платеж по первичному документу. Свойство имеет тип Object, возвращает
объект класса RsbCOPayment
 и доступно только для чтения.
Series – серия (поле t_Series таблицы dpscshdoc_dbt); тип String.
Status – статус документа (поле t_Status таблицы dpscshdoc_dbt); тип Integer.
UserField1 – пользовательское поле (поле t_UserField1 таблицы dpscshdoc_dbt); тип
String.
UserField2 – пользовательское поле (поле t_UserField2 таблицы dpscshdoc_dbt); тип
String.
UserField3 – пользовательское поле (поле t_UserField3 таблицы dpscshdoc_dbt); тип
String.
UserField4 – пользовательское поле (поле t_UserField4 таблицы dpscshdoc_dbt); тип
String.

**Методы:**

DestroyObjectWhenDestructionOfWrappers():

## Класс: `RsbCashSymbols`

```rsl
RsbCashSymbols(ObjectID:Integer, ObjectType:Integvgz
```

## Класс: `RsbClaimOrder`

```rsl
RsbClaimOrder()
```

## Класс: `RsbCOPayment`

```rsl
RsbCOPayment ()
```

## Класс: `RsbCrossRate`

```rsl
RsbCrossRate (FIID1:Integer, FIID2:Integer, RateDate:Date, Rate:Double| RateType:Integer [, Point:Intger, Scale:Intger, IsInverse:Bool]):Object Вспомогательный класс для хранения параметров курса конверсии двух валют. Объекты этого класса являются частью класса RsbPayment .
```

**Параметры:**

FIID1 – ссылка на базовый финансовый инструмент.
FIID2 – ссылка на котируемый финансовый инструмент.
RateDate – дата курса.
Rate – значение курса.
RateType – тип курса.
Point – точность курса (количество знаков после запятой).
Scale – масштаб курса.
IsInverse – признак обратной котировки курса.
Конструктор класса может быть вызван двумя способами:
- Инициализация объекта заданными параметрами курса на заданную дату:
RsbCrossRate( FIID1, FIID2, RateDate, Rate, Point, Scale, IsInverse );
- Определение способа задания параметров курса при определении курса на дату оплаты:
RsbCrossRate( FIID1, FIID2, RateDate, RateType );
где RateType равен, например, основному курсу банка.
Одновременно указывать тип курса и его параметры нельзя!

**Свойства:**

FIID1 – идентификатор базового финансового инструмента. Свойство имеет тип Integer и
доступно только для чтения.
FIID2 – идентификатор котируемого финансового инструмента. Свойство имеет тип
Integer и доступно только для чтения.
IsInverse – признак обратной котировки курса; тип Bool.
Point – точность курса (количество знаков после запятой); тип Integer.
Rate – значение курса; тип Date.
RateDate – дата курса, тип Date.
RateType – тип курса; тип Integer.
Scale – масштаб курса; тип Integer.

**Методы:**

Actuate (ActDate:Date, KeepRateDate:Bool)
Установка курса на заданную дату. Значение курса изменяется на заданное, если курс не
был установлен ранее.

**Параметры:**

ActDate – дата, на которую нужно установить курс.
KeepRateDate – признак установки курса на дату, заданную для объекта в
конструкторе класса. Возможны два значения данного параметра:
- Если параметр равен FALSE, то параметры курса определяются на дату,
заданную параметром ActDate. Если дата ActDate не задана, то курс
берется из класса на дату RateDate из объекта. Если дата RateDate не
задана, то курс берется на текущую операционную дату;
- Если параметр равен TRUE, то курс устанавливается из объекта на дату
RateDate. Если дата RateDate не задана, то курс устанавливается из класса
на дату, заданную параметром ActDate. Если дата ActDate не задана, то
курс устанавливается на текущую операционную дату.
Convert (Amount:MoneyL):MoneyL

## Класс: `RsbDeal550Payment`

```rsl
RsbDeal550Payment ()
```

## Класс: `RsbFnsDecision`

```rsl
RsbFnsDecision ()
```

## Класс: `RsbFnsInfo`

```rsl
RsbFnsInfo()
```

## Класс: `RsbFnsInfoNS`

```rsl
RsbFnsInfoNS ()
```

## Класс: `RsbFnsInfoOS`

```rsl
RsbFnsInfoOS ()
```

## Класс: `RsbFnsInfoVS`

```rsl
RsbFnsInfoVS ()
```

## Класс: `RsbInClaimOrder`

```rsl
RsbInClaimOrder ()
```

## Класс: `RsbMultyPayment`

```rsl
RsbMultyPayment ([DocumentID:Integer]):Object Базовый класс предназначен для описания первичного документа "Сводный платеж". Конструктор класса RsbMultyPayment ([DocumentID:Integer])
```

имеет 
параметр
DocumentID – идентификатор документа.

**Свойства:**

CorrPosType – тип позиционирования документа (поле t_CorrPosType таблицы
dpmprop_dbt для записи кредитового свойства платежа); тип Integer.
LaunchOper – признак "Автоматически запускать дочернюю операцию по документу"; тип
Bool.
PayerBankCorrID – идентификатор корреспондента депозитария отправителя (поле
t_CorrID таблицы dpmprop_dbt для записи дебетового свойства платежа); тип
Integer.
PayerCorschem – идентификатор корсхемы получателя (поле t_Corschem таблицы
dpmprop_dbt для записи дебетового свойства платежа); тип Integer.
PayerIsSender – признак "Плательщик является отправителем платежа" (поле t_IsSender
таблицы dpmprop_dbt для записи дебетового свойства платежа); тип Bool.
ReceiverBankCorrID – идентификатор корреспондента депозитария получателя (поле
t_CorrID таблицы dpmprop_dbt); тип Integer.
ReceiverCorschem – идентификатор корсхемы получателя (поле t_Corschem таблицы
dpmprop_dbt для записи кредитового свойства платежа); тип Integer.
ReceiverIsSender – признак "Получатель является отправителем платежа" (поле
t_IsSender таблицы dpmprop_dbt для записи кредитового свойства платежа); тип
Bool.

**Методы:**

AddOprState (StatusKindID:Integer, NumValue:Integer):Integer

## Класс: `RsbInCollectOrder`

```rsl
RsbInCollectOrder()
```

## Класс: `RsbObjCtrl`

```rsl
RsbObjCtrl ()
```

## Класс: `RsbOutClaimOrder`

```rsl
RsbOutClaimOrder ()
```

## Класс: `RsbOutCollectOrder`

```rsl
RsbInCollectOrder()
```

## Класс: `RsbPayment`

```rsl
RsbPayment ([id_платежа:Integer]):Object Конструктор класса создает объект, который представляет собой платеж.
```

**Параметры:**

id_платежа – идентификатор записи в таблице dpmpaym_dbt.

**Свойства:**

AdditionalInfo – дополнительная 
информация 
(поле 
t_AdditionalInfo 
таблицы
dpmrmprop_dbt). Свойство имеет тип String и доступно только для чтения.
AkkrAccRealReceiver – номер счета конечного получателя денежных средств (поле
t_AccRealReceiver таблицы dpmakkr_dbt); тип String.
AkkrAddCondition – дополнительные условия аккредитива (поле t_AddCondition таблицы
dpmakkr_dbt); тип String.
AkkrAddDocs – приложение к аккредитиву; тип String.
AkkrDate – дата окончания действия аккредитива (поле t_Date таблицы dpmakkr_dbt); тип
Date.
AkkrPayCondition – условие оплаты аккредитива (поле t_PayCondition таблицы
dpmakkr_dbt); тип Integer. Возможные значения:
- 0 – с акцептом;
- 1 – без акцепта.
AkkrRepresentation – документы, по предоставлению которых происходит оплата
аккредитива (поле t_Representation таблицы dpmakkr_dbt); тип String.
AkkrType – вид аккредитива (поле t_Type таблицы dpmakkr_dbt); тип String. Возможные
значения:
- "Н" – безотзывный непокрытый.
- "Б" – безотзывный покрытый.
- "П" – отзывный непокрытый.
- "О" – отзывный покрытый.
Attr7a – атрибут банковского ордера 7А, хранящийся в таблице dpmbnkord_dbt; тип String.
Attr25 – атрибут банковского ордера 25, хранящийся в таблице dpmbnkord_dbt; тип String.
Attr26 – атрибут банковского ордера 26, хранящийся в таблице dpmbnkord_dbt; тип String.
Attr27 – атрибут банковского ордера 27, хранящийся в таблице dpmbnkord_dbt; тип String.
Attr28 – атрибут банковского ордера 28, хранящийся в таблице dpmbnkord_dbt; тип String.
Attr29 – атрибут банковского ордера 29, хранящийся в таблице dpmbnkord_dbt; тип String.
BaseAmount – сумма базового актива (поле t_BaseAmount таблицы dpmpaym_dbt); тип
MoneyL.
BaseFIID – финансовый 
инструмент 
базового 
актива 
(поле 
t_BaseFIID 
таблицы
dpmpaym_dbt); тип Integer.
BaseRate – базовый курс. Объект класса RsbCrossRate
. Свойство доступно только
для чтения.
BttTICode – код 
бюджетной 
классификации 
(доходы, 
поле 
t_BttTICode 
таблицы
dpmrmprop_dbt); тип String.
CardFileDateIn – дата постановки учетного объекта на картотеку (поле t_CardFileIn
таблицы dwlpm_dbt); тип Date.
CardFileDateOut – дата снятия учетного объекта с картотеки (поле t_CardFileDateOut
таблицы dwlpm_dbt); тип Date.
CardFileKind – вид картотеки учетного объекта для сообщения (поле t_CardFileKind
таблицы dwlpm_dbt); тип Integer.
- 0 – не указана;
- 1 – картотека корсчета для исходящих;
- 2 – картотека корреспондента для исходящих.
CashSymbolCredit – расходный символ кредита (поле t_CashSymbolCredit таблицы
dpmrmprop_dbt); тип String.
CashSymbolDebet – приходный символ дебета (поле t_CashSymbolDebet таблицы
dpmrmprop_dbt); типа String.
CashSymbols – кассовые символы платежа. Свойство имеет тип Object и возвращает
объект класса RsbPaymentSymbols.
ChargesOfBank – расходы банка; тип Integer.
Chapter – глава счетов в платеже (поле t_Chapter таблицы dpmpaym_dbt). Свойство
имеет тип Integer и доступно только для чтения.
CheckTerror – параметр, определяющий, выполнялась ли проверка документа на
терроризм; тип Integer. Возможные значения:
- 0 – не проверен;
- 1 – проверен;
- 2 – проверка не требуется.
CheckTerrorOnUpdate – признак, указывающий на необходимость проверки документа на
терроризм при сохранении; тип Integer. Возможные значения:
- 0 – не проверять (значение по умолчанию);
- 1 – проверять.
ClaimID – идентификатор претензии (поле t_ClaimID таблицы dpmpaym_dbt); тип Integer.
ClientDate – дата приема от клиента (поле t_ClientDate таблицы dpmrmprop_dbt); тип Date.
CloseDate – дата закрытия операции по платежу (поле t_CloseDate таблицы
dpmpaym_dbt). Свойство имеет тип Date и доступно только для чтения.
CodePurpose – код назначения платежа; тип Integer.
ComissAccount – счет комиссии (поле t_ComissAccount таблицы dpmpaym_dbt). Свойство
имеет тип String и доступно только для чтения.
ComissCharges – комиссии и расходы (поле t_ComissCharges таблицы dpmrmprop_dbt);
тип Integer. Возможные значения:
- 1 – OUR.
- 2 – SHA.
- 3 – BEN.
ComissFIID – идентификатор 
валюты 
комиссии 
(поле 
t_ComissFIID 
таблицы
dpmpaym_dbt). Свойство имеет тип Integer и доступно только для чтения.
ContentOperation 
- 
содержание 
операции 
(поле 
t_ContentOperation 
таблицы
dpmpaym_dbt); типа String.
ContractDate – дата контракта валютной операции платежа (поле t_ContractDate таблицы
dpmco_dbt); тип Date.
ContractFIID – идентификатор валюты цены контракта валютной операции платежа (поле
t_ContractFIID таблицы dpmco_dbt); тип Integer.
ContractNumber – номер контракта валютной операции платежа (поле t_ContractNumber
таблицы dpmco_dbt); тип String.
CorrespondentCharges – расходы корреспондентов; тип Integer.
CoverAmmount – сумма по счету покрытия; тип Numeric.
CoverCalcMethod – метод пересчета суммы по счету покрытия; тип String. Свойство
может принимать следующие значения:
- "X" – из валюты счета плательщика.
- " X" – из валюты счета получателя.
- " X" – без пересчета суммы.
CoverRateDate – дата курса суммы по счету покрытия; тип Date.
CrCurEqID – идентификатор валюты-эквивалента счета получателя (поле t_CrCurEqID
таблицы dpmnvpi_dbt); тип Integer.
CreationIP – IP-адрес компьютера, на котором был создан платеж; тип String.
CreationMAC – MAC-адрес компьютера, на котором был создан платеж; тип String.
CrRecalcMethod – метод пересчета суммы по кредиту (поле t_CrRecalcMethod таблицы
dpmnvpi_dbt); тип String.
- "X " – из валюты счета;
- " X " – из валюты-эквивалента;
- " X" – без пересчета.
CrSumEq – сумма по кредиту в валюте-эквиваленте (поле t_CrSumEq таблицы
dpmnvpi_dbt); тип Money.
Date – дата (заполняется клиентом), поле t_Date таблицы dpmrmprop_dbt; тип Date.
DbCurEqID –идентификатор валюты-эквивалента счета плательщика (поле t_DbCurEqID
таблицы dpmnvpi_dbt); тип Integer.
DbFlag – признак дебетового платежа (поле t_DbFlag таблицы dpmpaym_dbt). Свойство
имеет тип String и доступно только для чтения.
DbRecalcMethod – метод пересчета суммы по дебету (поле t_DbRecalcMethod таблицы
dpmnvpi_dbt); тип String.
- "X " – из валюты счета;
- " X " – из валюты-эквивалента;
- " X" – без пересчета.
DbSumEq – сумма по дебету в валюте-эквиваленте (поле t_DbSumEq таблицы
dpmnvpi_dbt); тип Money.
DefComID 
- 
идентификатор 
удержанной 
комиссии 
(поле 
t_defComID 
таблицы
dpmpaym_dbt); тип Integer.
DemandAccept – текущее состояние акцепта для требований (поле t_Accept таблицы
dpmdemand_dbt); тип Integer.
- 0 – акцепт не требуется;
- 1 – ожидает акцепта;
- 2 – акцептовано;
- 3 – отказ от акцепта.
DemandAcceptDate – дата акцептования требования (поле t_AcceptDate таблицы
dpmdemand_dbt); тип Date.
DemandAcceptPeriod – срок акцепта в рабочих днях; тип Integer.
DemandAcceptTerm – условие акцепта для требований (поле t_AcceptTerm таблицы
dpmdemand_dbt); тип Integer.
- 0 – без акцепта;
- 1 – с акцептом.
DemandIndexExitDate – дата изъятия из картотеки требований (поле t_IndexExitDate
таблицы dpmdemand_dbt); тип Date.
DemandIndexPlaceDate – дата помещения в картотеку требований (поле t_IndexPlaceDate
таблицы dpmdemand_dbt); тип Date.
DemandIsESID – признак требования ЭСИД; тип String.
DemandPayCondition – условие оплаты; тип String.
DenialAmount – сумма документа на отказ от платежа (поле t_Amount таблицы
dpmdenial_dbt). Свойство имеет тип MoneyL и доступно только для чтения.
DenialGround – основание отказа от акцепта платежного требования (поле t_Ground
таблицы dpmdenial_dbt). Свойство имеет тип String и доступно только для чтения.
Department – номер филиала (поле t_Department таблицы dpmpaym_dbt); тип Integer.
DocDispatchDate – дата отсылки документов плательщику (поле t_DocDispatchDate
таблицы dpmrmprop_dbt); тип Date.
DocKind – вид первичного документа (поле t_DocKind таблицы dpmpaym_dbt); тип Integer.
DocumentID – идентификатор первичного документа (поле t_DocumentID таблицы
dpmpaym_dbt); тип String.
ECControl – контроль по перечню EC; тип String.
EndDepartment – ссылка на конечный узел территориальной структуры внутри ЦАБС
(поле t_EndDepartment таблицы dpmpaym_dbt); тип Integer.
Error – ошибка, значение всегда равно 0. Используется для категорий учета. Свойство
имеет тип Integer и доступно только для чтения.
FactRate – фактический курс. Объект класса RsbCrossRate
. Свойство имеет тип
Object и доступно только для чтения.
FeeType – тип взимания комиссии (поле t_feeType таблицы dpmpaym_dbt); тип Integer.
FPSTransactionID – идентификатор транзакции в СПБ; тип String.
FutureBaseAmount – реальная сумма платежа (поле t_FutureBaseAmount таблицы
dpmpaym_dbt); тип MoneyL.
FutureCRate – текущий курс кредита. Объект класса RsbCrossRate
. Свойство имеет
тип Object.
FutureDRate – текущий курс дебета. Объект класса RsbCrossRate
. Свойство имеет
тип Object.
FuturePayerAccount – счет, с которого будет списана следующая проводка (поле
t_FuturePayerAccount таблицы dpmpaym_dbt); тип String.
FuturePayerAmount – сумма будущего дебетования (поле t_FuturePayerAmount таблицы
dpmpaym_dbt). Свойство имеет тип MoneyL и доступно только для чтения.
FuturePayerFIID – идентификатор 
валюты 
счета 
FuturePayerAccount 
(поле
t_FIID_FuturePayAcc таблицы dpmpaym_dbt); тип Integer.
FutureRate – текущий курс. Объект класса RsbCrossRate
. Свойство имеет тип Object.
FutureReceiverAccount – счет, на который будет зачислена следующая проводка (поле
t_FutureReceiverAccount таблицы dpmpaym_dbt); тип String.
FutureReceiverAmount – сумма будущего кредитования (поле t_FutureReceiverAmount
таблицы dpmpaym_dbt). Свойство имеет тип MoneyL и доступно только для
чтения.
FutureReceiverFIID – идентификатор 
валюты 
счета 
FutureReceiverAccount 
(поле
t_FIID_FutureRecAcc таблицы dpmpaym_dbt); тип Integer.
Ground – основание платежа (поле t_Ground таблицы dpmrmprop_dbt); тип String.
GUID – GUID платежа; тип String.
HasReservedAmount 
- 
признак 
"Платеж 
имеет 
зарезервированные 
средства".
Возвращает TRUE, если в таблице dacclmdoc_dbt для заданного вида и
идентификатора документа есть запись. Свойство имеет тип Bool и доступно
только для чтения.
HCSAccount – счет в ГИС ЖКХ; тип String.
HCSDocID – идентификатор в ГИС ЖКХ; тип String.
HCSHouseGUID – ГУИД дома в реквизитах платежа ЖКХ; тип String.
HCSHouseNum – номер дома в реквизитах платежа ГИС ЖКХ; тип String.
HCSMonth – месяц в реквизитах платежа ГИС ЖКХ; тип Integer.
HCSPayerINN – ИНН/КПП плательщика в реквизитах платежа ЖКХ; тип String.
HCSPayerName – наименование плательщика в реквизитах платежа ЖКХ; тип String.
HCSPayerName1 – фамилия плательщика в реквизитах платежа ЖКХ; тип String.
HCSPayerName2 – имя плательщика в реквизитах платежа ЖКХ; тип String.
HCSPayerName3 – отчество плательщика в реквизитах платежа ЖКХ; тип String.
HCSPayerUID – уникальный идентификатор плательщика в реквизитах платежа; тип
String.
HCSPayment – платеж ЖКХ; тип String.
HCSRoomNum – номер комнаты в реквизитах платежа ЖКХ; тип String.
HCSServiceID – идентификатор ЖКУ; тип String.
HCSSupplierAccount – счет у поставщика ЖКУ; тип String.
HCSSupplierDocNum – номер документа у поставщика ЖКУ; тип String.
HCSSupplierID – идентификатор поставщика ЖКУ; тип Integer.
HCSSupplierINN – ИНН/КПП поставщика ЖКУ; тип String.
HCSSupplierName – наименование поставщика ЖКУ; тип String.
HCSSupplierName1 – фамилия поставщика ЖКУ; тип String.
HCSSupplierName2 – имя поставщика ЖКУ; тип String.
HCSSupplierName3 – отчество поставщика ЖКУ; тип String.
HCSYear – год в реквизитах платежа ЖКХ; тип Integer.
I2PlaceDate – дата помещения в картотеку 2 (поле t_I2PlaceDate таблицы dpmpaym_dbt);
тип Date.
InCorschem – идентификатор входящей схемы расчетов (поле t_Corschem таблицы
dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
InReferenceMes – референс входящего сообщения (поле t_TRN таблицы dwlmes_dbt).
Свойство имеет тип String и доступно только для чтения.
InSettlementSystemCode – номер документа во входящей системе расчетов (поле
t_SettlementSystemCode таблицы dpmprop_dbt). Свойство имеет тип String и
доступно только для чтения.
Instancy – срочность платежа (поле t_Instancy таблицы dpmrmprop_dbt); тип Integer.
InstructionCode – код инструкции (поле t_InstructionCode таблицы dpmrmprop_dbt).
Свойство имеет тип String и доступно только для чтения.
InTransferDate – дата перечисления платежа по входящей схеме расчетов (поле
t_TransferDate таблицы dpmprop_dbt). Свойство имеет тип Date и доступно только
для чтения.
InTransport – идентификатор транспорта входящей схемы расчетов (поле t_TpID таблицы
dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
InWlPmID – идентификатор учетного объекта входящего сообщения (поле t_WlPmID
таблицы dwlpm). Свойство имеет тип Integer и доступно только для чтения.
IsCredit – свойство определяет тип платежа (TRUE – кредитовый или FALSE –
дебетовый). Свойство имеет тип Bool и доступно только для чтения.
IsExternal – свойство определяет, является ли платеж внешним. Свойство имеет тип Bool
и доступно только для чтения. Возвращает TRUE, если хотя бы одно из полей
t_Group таблицы dpmprop_dbt имеет значение 1 (внешний).
IsExternalIncoming – определяет, является ли платеж входящим. Свойство имеет тип
Bool и доступно только для чтения.
IsFactPaym – признак фактического платежа (поле t_IsFactPaym таблицы dpmpaym_dbt).
Свойство доступно для изменения только до ввода платежа, имеет тип String.

**Пример:**

var Payment:RsbPayment = RsbPayment();
Payment.IsFactPaym = "X";
IsFixPayerAmount – свойство определяет, фиксирован ли актив дебетования (поле
t_IsFixAmount таблицы dpmpaym_dbt); тип Bool.
IsPaymentPropsChange – признак изменения реквизитов платежа; тип Bool.

**Пример:**

if( PaymentObj.IsPaymentPropsChange )
 MsgBox("Были изменения реквизитов");
end;
IsPlanPaym – признак планового платежа (поле t_IsPlanPaym таблицы dpmpaym_dbt).
Свойство доступно для изменения только до ввода платежа, имеет тип String.

**Пример:**

var Payment:RsbPayment = RsbPayment();
Payment.IsPlanPaym = "X";
IsPrinted – признак "Документ печатался" учетного объекта для сообщения (поле
t_IsPrinted таблицы dwlpm_dbt); тип String.
IsPurpose – признак движения целевых средств (поле t_IsPurpose таблицы dpmpaym_dbt);
тип String. Возможные значения:
- 'X' – целевые средства.
- 'A' – исполнение ареста.
IsUnknown – признак "Невыясненный" учетного объекта для сообщения (поле
t_IsUnknown таблицы dwlpm_dbt). Свойство имеет тип String и доступно только
для чтения.
Kind – тип объекта (всегда DLDOC_PAYMENT), используется для категорий учета.
Свойство имеет тип Integer и доступно только для чтения.
KZ_GroundCode – код назначения платежа (казахские реквизиты), поле t_GroundCode
таблицы dpmkz_dbt; тип Integer.
KZ_PayerCode – код отправителя денег (казахские реквизиты), поле t_PayerCode таблицы
dpmkz_dbt; тип String.
KZ_ReceiverCode – код бенефициара (казахские реквизиты), поле t_ReceiverCode
таблицы dpmkz_dbt; тип String.
KZ_ReceiverCountry 
- 
страна 
бенефициара 
(казахские 
реквизиты), 
поле
t_ReceiverCountry таблицы dpmkz_dbt; тип String.
MCMethodID – идентификатор метода мультивалютной проводки по платежу, поле
t_MCMethodID таблицы dpmpmaym_dbt; тип Integer.
MessageType – тип сообщения (поле t_MessageType таблицы dpmrmprop_dbt); тип String.
MinimizationTurn – признак минимизации оборотов; тип String.
NeedExecNotify – признак "Требуется уведомление" для платежа (значение констант
WLPM_EXECNOTIFY_FAIL, 
WLPM_EXECNOTIFY_NOTNEED 
или
WLPM_EXECNOTIFY_SUCCESS); тип Integer.
NeedNotify 
- 
признак 
"Требуется 
уведомление" 
(поле 
t_NeedNotify 
таблицы
dpmrmprop_dbt); тип String.

**Пример:**

if( PaymentObj.NeedNotify == "X" )
 MsgBox("Требуется уведомление");
end;
Netting – признак неттинга (поле t_Netting таблицы dpmpaym_dbt); тип String.
Notes – примечания платежа. Свойство имеет тип Object, возвращает объект класса
RsbObjNotes (см. Руководство "Интерфейсы языка RSL для взаимодействия с
ИБС RS-Bank V.6. Часть 1") и доступно только для чтения.
NotForBackOffice – признак "Не передавать в бэк-офис" (поле t_NotForBackOffice
таблицы dpmpaym_dbt); тип String.
Number – номер 
документа 
(заполняется 
клиентом), 
поле 
t_Number 
таблицы
dpmrmprop_dbt; тип String.

**Пример:**

var PaymentObj:RsbPayment;
PaymentObj.Number = "0001";
NumberPack – номер пачки (поле t_NumberPack таблицы dpmpaym_dbt); тип Integer.
OKATOCode – код ОКАТО (поле t_OKATOCode таблицы dpmrmprop_dbt); тип String.
OONControl – контроль по перечню ООН; тип String.
Oper – идентификатор операциониста, автора платежа (поле t_Oper таблицы
dpmpaym_dbt); тип Integer.
OperNode – узел операциониста-автора документа; тип Integer.
Origin – происхождение платежа, ссылка на значение справочника 1803 (поле t_Origin
таблицы dpmpaym_dbt); тип Integer (OBJTYPE_PAYMENT_ORIGIN).
OutCorschem – идентификатор исходящей схемы расчетов платежа (поле t_Corschem
таблицы dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
OutCorschemFIID – идентификатор валюты корсчета исходящей схемы расчетов (поле
t_PayFIID таблицы dpmprop_dbt). Свойство имеет тип Integer и доступно только
для чтения.
OutDateInProp – дата списания с картотеки (реальная) входящего невыясненного
платежа (поле t_OutDate таблицы drmpinprop_dbt); тип Date.
OutReferenceMes – референс исходящего сообщения (поле t_TRN таблицы dwlmes_dbt).
Свойство имеет тип String и доступно только для чтения.
OutRlsForm – идентификатор релиза исходящей схемы расчетов (поле t_RlsFormID
таблицы dpmprop_dbt); тип Integer.
OutSettlementSystemCode – код документа в исходящей системе расчетов (поле
t_SettlementSystemCode таблицы dpmprop_dbt). Свойство имеет тип String и
доступно только для чтения.
OutSubKindMessage – подвид сообщения; тип Integer.

**Примечание:**

Изменение 
свойства 
в 
уже 
созданном 
платеже 
не 
приводит 
к
переопределению релиза. Изменение релиза следует произвести с помощью
процедуры DefineRlsForm
.
OutTpSchem – идентификатор транспортной схемы исходящей схемы расчетов (поле
t_TpSchemID таблицы dpmprop_dbt); тип Integer.
OutTransferDate – дата перечисления платежа по исходящей схеме расчетов (поле
t_TransferDate таблицы dpmprop_dbt); тип Date.
OutTransport – транспорт 
исходящей 
схемы 
расчетов 
(поле 
t_TpID 
таблицы
dpmprop_dbt); тип Integer.
OutWlPmID – идентификатор учетного объекта исходящего сообщения (поле t_WlPmID
таблицы dwlpm_dbt). Свойство имеет тип Integer и доступно только для чтения.
PartPaymDateMain – дата 
основного 
документа 
(частичная 
оплата), 
поле
t_PartPaymDateMain таблицы dpmpaym_dbt; тип Date.
PartPaymNumber – порядковый номер частичного платежа (поле t_PartPaymNumber
таблицы dpmpaym_dbt); тип Integer.
PartPaymNumMain – номер 
основного 
документа 
(частичная 
оплата), 
поле
t_PartPaymNumMain таблицы dpmpaym_dbt; тип String.
PartPaymRestAmountMain – сумма 
остатка 
платежа 
(частичная 
оплата, 
поле
t_PartPaymRestAmountMain таблицы dpmpaym_dbt; тип Moneyl.
PartPaymShifrMain – шифр 
основного 
документа 
(частичная 
оплата), 
поле
t_PartPaymShifrMain таблицы dpmpaym_dbt; тип String.
PartyInfo – информация участнику (поле t_PartyInfo таблицы dpmrmprop_dbt); тип String.
PassportDate – дата паспорта сделки валютной операции платежа (поле t_PassportDate
таблицы dpmco_dbt); тип Date.
PassportNumber – номер паспорта сделки валютной операции платежа (поле
t_PassportNumber таблицы dpmco_dbt); тип String.
PayDate – срок платежа (поле t_PayDate таблицы dpmrmprop_dbt); тип Date.
Payer – идентификатор плательщика (поле t_Payer таблицы dpmpaym_dbt). Свойство
имеет тип Integer и доступно только для чтения.
PayerAccount – номер счета плательщика (поле t_PayerAccount таблицы dpmpaym_dbt).
Свойство имеет тип String и доступно только для чтения.
PayerAmount – сумма дебета (поле t_Amount таблицы dpmpaym_dbt); тип MoneyL.
PayerBankCode – код банка плательщика (поле t_BankCode таблицы dpmprop_dbt).
Свойство имеет тип String и доступно только для чтения.
PayerBankCodeKind – вид 
кода 
банка 
плательщика 
(поле 
t_CodeKind 
таблицы
dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
PayerBankCorrAcc – корсчет банка плательщика (поле t_CorrAcc таблицы dpmprop_dbt);
тип String.
PayerBankCorrCode – код корреспондента банка плательщика (поле t_CorrCode таблицы
dpmprop_dbt); тип String.
PayerBankCorrCodeKind – вид 
кода 
корреспондента 
банка 
плательщика 
(поле
t_CorrCodeKind таблицы dpmprop_dbt); тип Integer.
PayerBankCorrID – идентификатор корреспондента депозитария отправителя (поле
t_CorrID таблицы dpmprop_dbt). Свойство имеет тип Integer и доступно только
для чтения.
PayerBankCorrName – наименование 
корреспондента 
банка 
плательщика 
(поле
t_PayerCorrBankName таблицы dpmprop_dbt); тип String.
PayerBankEnterDate – дата 
поступления 
платежа 
в 
банк 
плательщика 
(поле
t_PayerBankEnterDate таблицы dpmpaym_dbt); тип Date.
PayerBankID – идентификатор 
банка 
плательщика 
(поле 
t_PayerBankID 
таблицы
dpmpaym_dbt). Свойство имеет тип Integer и доступно только для чтения.
PayerBankMarkDate – дата отметки банка плательщика (поле t_PayerBankMarkDate
таблицы dpmpaym_dbt); тип Date.
PayerBankName – наименование банка плательщика (поле t_PayerBankName таблицы
dpmrmprop_dbt); тип String 
PayerChargeOffDate 
- 
дата 
списания 
средств 
со 
счета 
плательщика 
(поле
t_PayerChargeOffDate таблицы dpmrmprop_dbt); тип Date.
PayerCode – код плательщика (поле t_PayerCode таблицы dpmpaym_dbt). Свойство имеет
тип String и доступно только для чтения.
PayerCodeKind – вид кода плательщика (поле t_PayerCodeKind таблицы dpmpaym_dbt).
Свойство имеет тип Integer и доступно только для чтения.
PayerCorrAccNostro – корреспондентский 
счет 
банка 
плательщика 
в 
РКЦ 
(поле
t_PayerCorrAccNostro таблицы dpmrmprop_dbt). Свойство имеет тип String и
доступно только для чтения.
PayerDpNode – раздел 
счета 
депо 
плательщика 
(поле 
t_PayerDpNode 
таблицы
dpmpaym_dbt); тип Integer.
PayerFIID – идентификатор валюты плательщика (поле t_FIID таблицы dpmpaym_dbt); тип
Integer.
PayerGroup – группа дебетового свойства платежа (поле t_Group таблицы dpmprop_dbt).
Свойство имеет тип Integer и доступно только для чтения.
PayerINN – ИНН плательщика (поле t_PayerINN таблицы dpmrmprop_dbt); тип String.
PayerInOurBalance – признак того, что корсчет исходящего корреспондента указан в
нашем балансе (поле t_InOurBalance таблицы dpmprop_dbt), тип Bool.
PayerIsSender – признак "Плательщик является отправителем платежа" (поле t_IsSender
таблицы dpmprop_dbt). Свойство имеет тип String и доступно только для чтения.
PayerMesBankID – участник отправитель (поле t_PayerMesBankID таблицы dpmpaym_dbt);
тип Integer.
PayerName – имя плательщика (поле t_PayerName таблицы dpmrmprop_dbt); тип String.
PayerOurCorrAcc – раздел корсчета депо отправителя (поле t_OurCorrAcc таблицы
dpmprop_dbt); тип String.
PayerOurCorrID 
- 
идентификатор 
внешнего 
исходящего 
корреспондента 
(поле
t_OurCorrID таблицы dpmprop_dbt); тип Integer.
PayerSPI_Ident – идентификатор СПИ плательщика (поле t_SPI_Ident 
таблицы
dpmprop_dbt); тип String.
PaymentByNoTaxReg – признак "Платеж за лицо без регистрации в налоговом органе";
тип String.
PaymentByOtherPerson – оплата налогов иным лицом; тип Integer.
PaymentID – идентификатор платежа. Свойство имеет тип Integer и доступно только для
чтения.
PaymentKind – вид платежа: "П" – почтой, "Т" – телеграммой, "Э" – электронно, "С" –
срочно (поле t_PaymentKind таблицы dpmrmprop_dbt.); тип Integer.
PaymStatus – статус платежа (поле t_PaymStatus таблицы dpmpaym_dbt); тип Integer.

**Пример:**

var PaymentObj:RsbPayment;
PaymentObj.PaymStatus = PM_PREPARING;
PlaceToIndex – признак "Помещать в картотеку" (поле t_PlaceToIndex таблицы
dpmpaym_dbt); тип String.
PmCO – объект RsbPmCO; тип Object.
Precedence – приоритет платежа; тип String.
PrimDocKind – вид документа, по которому создана операция по платежу (поле
t_PrimDocKind таблицы dpmpaym_dbt); тип Integer.
Priority – очередность платежа (поле t_Priority таблицы dpmrmprop_dbt); тип Integer.
Максимальное 
значение 
задается 
настройкой 
банка
CB\PAYMENTS\MAXPRIORITY.
ProcKind – обработка (поле t_ProcKind таблицы dpmpaym_dbt). Свойство имеет тип
Integer и доступно только для чтения.
PropStatus 
- 
системный 
статус 
свойств 
платежа 
(поле 
t_PropStatus 
таблицы
dpmprop_dbt); тип Integer. Используется в АРМ Позиционера, корсчетах.

**Пример:**

var PaymentObj.PropStatus = PM_PROP_UNKNOWN; // Невыясненный
платеж
Purpose – назначение платежа (поле t_Purpose таблицы dpmpaym_dbt); тип Integer.
Receiver – идентификатор получателя платежа (поле t_Receiver таблицы dpmpaym_dbt).
Свойство имеет тип Integer и доступно только для чтения.
ReceiverAccount – счет получателя (поле t_ReceiverAccount таблицы dpmpaym_dbt).
Свойство имеет тип String и доступно только для чтения.
ReceiverAmount – сумма перевода (поле t_PayAmount таблицы dpmpaym_dbt); тип String.
ReceiverBankCode – код банка получателя (поле t_BankCode таблицы dpmprop_dbt).
Свойство имеет тип String и доступно только для чтения.
ReceiverBankCodeKind – вид 
кода 
банка 
получателя 
(поле 
t_CodeKind 
таблицы
dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
ReceiverBankCorrAcc – код банка получателя (поле t_CorrAcc таблицы dpmprop_dbt); тип
String.
ReceiverBankCorrCode – код 
корреспондента 
банка 
получателя 
(поле 
t_CorrCode
таблицы dpmprop_dbt); тип String.
ReceiverBankCorrCodeKind – вид 
кода 
корреспондента 
банка 
получателя 
(поле
t_CorrCodeKind таблицы dpmprop_dbt); тип Integer.
ReceiverBankCorrID – идентификатор корреспондента депозитария получателя (поле
t_CorrID таблицы dpmprop_dbt). Свойство имеет тип Integer и доступно только
для чтения.
ReceiverBankCorrName – наименование 
корреспондента 
банка 
получателя 
(поле
t_ReceiverCorrBankName таблицы dpmrmprop_dbt); тип String.
ReceiverBankID – идентификатор банка получателя (поле t_ReceiverBankID таблицы
dpmpaym_dbt). Свойство имеет тип Integer и доступно только для чтения.
ReceiverBankMarkDate – дата отметки банка получателя (поле t_ReceiverBankMarkDate
таблицы dpmpaym_dbt); тип Date.
ReceiverBankName – наименование 
банка 
получателя 
(поле 
t_ReceiverBankName
таблицы dpmrmprop_dbt); тип String.
ReceiverChargeOffDate – дата 
списания 
средств 
со 
счета 
плательщика 
(поле
t_ReceiverChargeOffDate таблицы dpmrmprop_dbt); тип Date.
ReceiverCode – код получателя (поле t_ReceiverCode таблицы dpmpaym_dbt). Свойство
имеет тип String и доступно только для чтения.
ReceiverCodeKind – вид 
кода 
получателя 
(поле 
t_ReceiverCodeKind 
таблицы
dpmpaym_dbt). Свойство имеет тип Integer и доступно только для чтения.
ReceiverCorrAccNostro – корсчет банка получателя в РКЦ (поле t_ReceiverCorrAccNostro
таблицы dpmrmprop_dbt); тип String.
ReceiverDpNode – раздел счета депо получателя (поле t_ReceiverDpNode таблицы
dpmpaym_dbt); тип Integer.
ReceiverFIID – идентификатор 
валюты 
получателя 
(поле 
t_PayFIID 
таблицы
dpmpaym_dbt); тип Integer.
ReceiverGroup – группа кредитового свойства платежа (поле t_Group таблицы
dpmprop_dbt). Свойство имеет тип Integer и доступно только для чтения.
ReceiverINN – ИНН получателя (поле t_ReceiverINN таблицы dpmrmprop_dbt); тип String.
ReceiverInOurBalance – признак того, что корсчет входящего корреспондента указан в
нашем балансе (поле t_InOurBalance таблицы dpmprop_dbt); тип Bool.
ReceiverIsSender – признак "Получатель является отправителем платежа" (поле
t_IsSender таблицы dpmprop_dbt). Свойство имеет тип String и доступно только
для чтения.
ReceiverMesBankID – идентификатор участника получателя (поле t_ReceiverMesBankID
таблицы dpmpaym_dbt); тип Integer.
ReceiverName – наименование 
получателя 
(поле 
t_ReceiverName 
таблицы
dpmrmprop_dbt); тип String.
ReceiverOurCorrAcc – раздел корсчета депо получателя (поле t_OurCorrAcc таблицы
dpmprop_dbt); тип String.
ReceiverOurCorrID – идентификатор внешнего входящего корреспондента (поле
t_ReceiverOurCorrID таблицы dpmprop_dbt); тип Integer.
ReceiverSPI_Ident 
- идентификатор СПИ получателя (поле t_SPI_Ident
таблицы
dpmprop_dbt); тип String.
Reference – ссылка (поле t_Reference таблицы dpmrmprop_dbt). Свойство имеет тип
String и доступно только для чтения.
ReferenceMes – референс главного сообщения платежа (поле t_TRN таблицы
dwlmes_dbt). Свойство имеет тип String и доступно только для чтения.
ReplicationBO – символ бэк-офиса сессии репликации (поле t_BackOffice таблицы
dpmrepses_dbt); тип String.
ReplicationSession – номер сессии репликации платежа (поле t_Session таблицы
dpmrepses_dbt); тип Integer.
SEMUControl – контроль по СЭМУ; тип String.
SettleNotEarlier – исполнить в ПБР не ранее, чем; тип String.
SettleNotEarlierTime – исполнить в ПБР не ранее, чем, время; тип Time.
SettleNotEarlierSessID – исполнить в ПБР не ранее, чем рейс; тип Integer.
SettleNotLater – исполнить в ПБР не позднее, чем; тип String.
SettleNotLaterTime – Исполнить в ПБР не позднее, чем, время; тип Time.
SettlementTime – время исполнения в ПБР; тип Time.
ShifrOper – шифр операции (поле t_ShifrOper таблицы dpmrmprop_dbt); тип String.
Sort – порядок сортировки входящего невыясненного платежа (поле t_Sort таблицы
drminprop_dbt); тип String.
StartDepartment – ссылка на начальный узел территориальной структуры внутри ЦАБС
(поле t_StartDepartment таблицы dpmpaym_dbt); тип Integer.
StatusInfo – статус операции для ИКЮЛ, заданный пользователем; тип String.
StrDocumentID – строковый идентификатор платежа. Свойство имеет тип String и
доступно только для чтения.
SubKind – подвид платежа (поле t_SubKind таблицы dpmpaym_dbt). Свойство имеет тип
Integer и доступно только для чтения.
SubPurpose – подвид назначения платежа (поле t_SubPurpose таблицы dpmpaym_dbt);
тип Integer.
SymbNotBalCredit – забалансовый кассовый символ кредита (поле t_SymbNotBalCredit
таблицы dpmrmprop_dbt); тип String.
SymbNotBalDebet – забалансовый кассовый символ дебета (поле t_SymbNotBalDebet
таблицы dpmrmprop_dbt); тип String.
TaxAuthorState – статус 
составителя 
документа 
(поле 
t_TaxAuthorState 
таблицы
dpmrmprop_dbt); тип String.
TaxPmDate – дата налогового документа (поле t_TaxPmDate таблицы dpmrmprop_dbt); тип
Date.
TaxPmGround – основание 
налогового 
платежа 
(поле 
t_TaxPmGround 
таблицы
dpmrmprop_dbt); тип String.
TaxPmNumber – номер 
налогового 
документа 
(поле 
t_TaxPmNumber 
таблицы
dpmrmprop_dbt); тип String.
TaxPmPeriod – налоговый период (поле t_TaxPmPeriod таблицы dpmrmprop_dbt); тип
String.
TaxPmType – тип налогового платежа (поле t_TaxPmType таблицы dpmrmprop_dbt); тип
Integer.
TaxOperID – уникальный присваиваемый номер операции; тип String.
ToBackOffice – символ бэк-офиса получателя платежа (поле t_ToBackOffice таблицы
dpmpaym_dbt); тип String.
UIN – уникальный идентификатор начисления (поле t_UIN таблицы dpmrmprop_dbt); тип
String.
UnknownState – статус входящего невыясненного платежа (поле t_Closed таблицы
drminprop_dbt); тип String. Возможные значения:
- "X" – закрыт;
- "" – открыт.
ValueDate – дата валютирования платежа (поле t_Value таблицы dpmpaym_dbt); тип Date.
VO_Accept – состояние акцепта валютной операции; тип Integer.
VO_Code – код валютной операции (поле t_VO_Code таблицы dpmco_dbt), тип Integer.
VO_Description – описание ошибки валютного контроля dpmcurtr_dbt.t_description.
VO_Direct – направление платежа с точки зрения резидентности плательщика и
получателя; тип Integer.
VO_FIID – идентификатор валюты для валютной операции; тип Integer.
VO_LnkDocs – связанные документы; тип Integer.
VO_Oper – идентификатор валютного контролера; тип Integer.
VO_PayerBankCode – код банка плательщика в валютной операции; тип String.
VO_PayerBankCodeKind – вид кода банка плательщика в валютной операции; тип
Integer.
VO_PayerBankCountry – трехзначный цифровой код страны банка плательщика в
валютной операции; тип String.
VO_PayerBankID – идентификатор банка плательщика в валютной операции; тип Integer.
VO_ReceiverBankCode – код банка получателя в валютной операции; тип String.
VO_ReceiverBankCodeKind – вид кода банка получателя в валютной операции; тип
Integer.
VO_ReceiverBankCountry – трехзначный цифровой код страны банка получателя в
валютной операции; тип String.
VO_ReceiverBankID – идентификатор банка получателя в валютной операции; тип
Integer.
WlPmID – идентификатор учетного объекта сообщения МБР (поле t_WlPmID таблицы
dwlpm_dbt). Свойство имеет тип Integer и доступно только для чтения.

**Пример:**

Пример 1:
// автоматическое заполнение свойств класса RsbPayment
import PaymInter;
import BankInter;
import CTInter;
var MO = RSBMemorialOrder();// !!!
var Payment = MO.Payment;
Payment.PayerAmount = 777.77;
println("Payment.PayerAmount =", Payment.PayerAmount);
println("-----------------------------------");
println("Payment.FutureBaseAmount 
=",
Payment.FutureBaseAmount);
println("Payment.BaseAmount =", Payment.BaseAmount);
println("Payment.ReceiverAmount =", Payment.ReceiverAmount);
println("Payment.FuturePayerAmount 
=",
Payment.FuturePayerAmount);
println("Payment.FutureReceiverAmount 
=",
Payment.FutureReceiverAmount);
println("Payment.BaseAmount =", Payment.BaseAmount);
println("Payment.PayerAmount =", Payment.PayerAmount);
println("Payment.ReceiverAmount =", Payment.ReceiverAmount);
Результат:
Payment.PayerAmount = 777.77
- ---------------------------------------
Payment.FutureBaseAmount = 777.77
Payment.BaseAmount = 777.77
Payment.ReceiverAmount = 777.77
Payment.FuturePayerAmount = 777.77
Payment.FutureReceiverAmount = 777.77
Payment.BaseAmount = 777.77
Payment.PayerAmount = 777.77
Payment.ReceiverAmount = 777.77
Пример 2
import PaymInter;
import BankInter;
import CTInter;
var MD = RSBMultyDoc();// !!!
var Payment = MD.Payment;
Payment.PayerAmount = 777.77;
println("Payment.PayerAmount =", Payment.PayerAmount);
println("-----------------------------------");
println("Payment.FutureBaseAmount 
=",
Payment.FutureBaseAmount);
println("Payment.BaseAmount =", Payment.BaseAmount);
println("Payment.ReceiverAmount =", Payment.ReceiverAmount);
println("Payment.FuturePayerAmount 
=",
Payment.FuturePayerAmount);
println("Payment.FutureReceiverAmount 
=",
Payment.FutureReceiverAmount);
println("Payment.BaseAmount =", Payment.BaseAmount);
println("Payment.PayerAmount =", Payment.PayerAmount);
println("Payment.ReceiverAmount =", Payment.ReceiverAmount);
Результат:
Payment.PayerAmount = 777.77
- ---------------------------------------
Payment.FutureBaseAmount = 0.00
Payment.BaseAmount = 0.00
Payment.ReceiverAmount = 0.00
Payment.FuturePayerAmount = 777.77
Payment.FutureReceiverAmount = 0.00
Payment.BaseAmount = 0.00
Payment.PayerAmount = 777.77
Payment.ReceiverAmount = 0.00
См. описание методов класса
.
Методы класса RsbPayment
Среди методов класса RsbPayment выделяют:
- методы, которые могут возвращать и устанавливать значения одноименных полей
платежа
;
- методы поиска
;
- методы проверки дат перечисления платежа
;
- методы проверки наличия/отсутствия признаков платежа
;
- методы для работы с объектами
;
- методы для работы с платежными инструкциями
;
- методы для определения реквизитов плательщика и получателя
;
- прочие методы
.
Методы для работы с одноименными полями платежа
Для объектов класса RsbPayment реализованы методы, которые могут возвращать и
устанавливать значения одноименных полей платежа:
FIID ();
Amount ();
Payer ();
PaymStatus ();
PaymentID ();
PayerCodeKind ();
PayerCode ();
PayerName ();
PayerAccount ();
PayerBankID ();
PayerBankCodeKind ();
PayerBankCode ();
PayerBankName ();
PayerBankCorrAcc ();
PayerBankCorrCodeKind ();
PayerBankCorrCode ();
PayerBankCorrName ();
Receiver ();
ReceiverCodeKind ();
ReceiverCode ();
ReceiverName ();
ReceiverAccount();
ReceiverBankID ();
ReceiverBankCodeKind ();
ReceiverBankCode ();
ReceiverBankName ();
ReceiverBankCorrAcc ();
ReceiverBankCorrCodeKind ();
ReceiverBankCorrCode ();
ReceiverBankCorrName ();
ValueDate ();
Ground ();
PartyInfo ().

**Пример:**

Paym = RsbPayment ();
// Платежу присвоен статус "готов к отправке":
Paym.PaymStatus = PM_READY_TO_SEND
Методы поиска
Методы, предназначенные для поиска:
GetBasisFIRole ():Integer

## Класс: `RsbPaymTransaction`

```rsl
RsbPaymTransaction ():Object
```

## Класс: `RsbPIPayment`

```rsl
RsbPIPayment ()
```

## Класс: `RsbPmBfLnk`

```rsl
RsbPmBfLnk ()
```

## Класс: `RsbPmPartAt`

```rsl
RsbPmPartAt()
```

## Класс: `RsbPmptfm`

```rsl
RsbPmptfm()
```

## Класс: `RsbPSInCashOrder`

```rsl
RsbPSInCashOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbPSOutCashOrder`

```rsl
RsbPSOutCashOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbPSOutCashOrder`

```rsl
предназначен для описания первичного документа "Расходный кассовый ордер РКО", является наследником класса RsbCashOrder и наследует все его атрибуты. Конструктор класса RsbPSOutCashOrder ([DocumentID:Integer])
```

имеет 
параметр
DocumentID – идентификатор документа. Если параметр равен 0 или не указан,
создается новый документ.

## Класс: `RsbPSPayment`

```rsl
RsbPSPayment()
```

## Класс: `RsbPSPayOrder`

```rsl
RsbPSPayOrder ([DocumentID:Integer]):Object
```

## Метод: `созда`

```rsl
ёт частичную оплату по документу (отложенный клиентский чек на заданную сумму с заданными серией и номером). При этом создается связь между основным и частичным платежом вида PMLINK_KIND_KVITING. Если основной документ связан с требованием на оплату, для порожденного платежа также создается связка, при этом суммы связки основного платежа корректируются.
```

**Параметры:**

Amount – сумма документа. По умолчанию – сумма к оплате основного платежа.
Series – серия чека.
Number – номер чека.

**Возвращаемое значение:**



## Метод: `созда`

```rsl
ёт частичную оплату по документу (отложенный платёжный ордер на сумму – шифр документа "16"). При этом создается связь между основным и частичным платежом вида PMLINK_KIND_KVITING. Если основной документ связан с требованием на оплату, для порожденного платежа также создается связка, при этом суммы связки основного платежа корректируются. Параметр: Amount – сумма документа. По умолчанию – сумма к оплате основного платежа.
```

**Возвращаемое значение:**



## Класс: `RsbRegDec`

```rsl
RsbRegDec()
```

Базовый класс для объектов, хранящихся в таблице wlregdec.dbt (RsbFnsInfo,
RsbFnsDecision).

**Свойства:**

AccDateBegin – дата начала периода для поиска счетов; тип Date.
AccDateEnd – дата окончания периода для поиска счетов; тип Date.
AccLnk – список связанных счетов объекта; тип Object. Свойство имеет тип
RsbWlAccLnk.
AccTypePeriod – тип периода для поиска счетов; тип Integer. Свойство может принимать
следующие значения:
- 0 – за дату;
- 1 – за период.
AllAccounts – признак формирования по всем счетам; тип String.
Amount – сумма; тип Money.
BankDate – операционный день; тип Date.
BTTTICode – КБК; тип String.
ClientID – идентификатор клиента; тип Integer.
ClientINN – ИНН клиента; тип String.
ClientKPP – КПП клиента; тип String.
ClientName – наименование клиента; тип String.
ClientRegNum – номер свидетельства о постановке на учета; тип String.
ClientSubCode – код подчиненности клиента; тип String.
ClientType – тип клиента (юридическое/физическое лицо); тип Integer.
Date – дата; тип Date.
DecisionID – идентификатор объекта; тип Integer.
DeliveryDate – дата получения; тип Date.
Description – дополнительная информация; тип String.
Direct – направление; тип String.
EndDate – дата окончания периода; тип Date.
ExecuteDate – срок исполнения; тип Date.
Ground – основание; тип String.
Histor – история изменения статуса объекта; тип Object. Свойство имеет тип
RsbWlHistor.
InputDate – дата ввода; тип Date.
Kind – вид решения; тип Integer.
LnkDocDate – дата связанного документа; тип Date.
LnkDocExtID – внешний идентификатор связанного объекта; тип String.
LnkDocID – идентификатор связанного объекта; тип Integer.
LnkDocNumber – номер связанного документа; тип String.
LnkDocType – тип связанного документа; тип Integer.
LnkMesDate – дата связанного сообщения; тип Date.
LnkMesTRN – номер связанного сообщения; тип String.
LnkReqType – тип связанного запроса; тип String.
LnkTypeInfo – тип сведений в связанном объекте; тип Integer.
Notes – примечания объекта; тип Object. Свойство имеет тип RsbObjNotes.
Number – номер; тип String.
OKATOCode – код ОКАТО; тип String.
Origin – происхождение; тип String.
OriginatorCode – код создателя; тип String.
OriginatorCodeKind – вид кода создателя; тип Integer.
OriginatorID – идентификатор создателя; тип Integer.
OriginatorName – наименование создателя; тип String.
RecipientCode –код получателя; тип String.
RecipientCodeKind – вид кода получателя; тип Integer.
RecipientID – идентификатор получателя; тип Integer.
RecipientName – наименование получателя; тип String.
RegPartyKind – вид регистрационного органа; тип Integer.
RespPersonFIO – фамилия ответственного лица; тип String.
RespPersonPost – должность ответственного лица; тип String.
RespPersonTel – телефон ответственного лица; тип String.
StartDate – дата начала действия; тип Date.
State – текущий статус записи; тип Integer.
SysDate – системная дата; тип Date.
SysTime – системное время; тип Time.
Type – тип объекта (константа вида WLD_TYPE_REGDEC_*); тип Integer.
UserID – идентификатор пользователя; тип Integer.

**Методы:**

ChangeState (State:Integer):Integer

## Класс: `RsbRequestOrder`

```rsl
RsbRequestOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbRequestOrder`

```rsl
предназначен для описания первичного документа "Инкассовое поручение к валютному счету клиента". Конструктор класса RsbRequestOrder ([DocumentID:Integer])
```

имеет 
параметр
DocumentID – идентификатор документа. Если параметр равен 0 или не указан,
создается новый документ.

**Свойства:**

Categories – категории документа; тип Object. Свойство возвращает объект класса
RsbObjCategories (см. Руководство "Интерфейсы языка RSL для взаимодействия
с ИБС RS-Bank V.6. Часть 1") и доступно только для чтения.
ConnectToOper – признак "Привязывать создание документа к шагу операции"; тип Bool.
KindOperation – вид операции по документу; тип Integer.
LastPartPaymNumber – номер последней частичной оплаты по документу. Свойство
имеет тип Integer и доступно только для чтения.
LaunchOper – признак автоматического запуска дочерней операции по документу; тип
Bool.
MaketID – идентификатор макета ввода; тип Integer.
Notes – примечания документа; тип Object. Свойство возвращает объект класса
RsbObjNotes (см. Руководство "Интерфейсы языка RSL для взаимодействия с
ИБС RS-Bank V.6. Часть 1") и доступно только для чтения.
Oper – идентификатор операциониста (автора документа); тип Integer.
Origin – происхождение документа; тип Integer.
Payment – платеж по документу; тип Object. Свойство возвращает объект класса
RsbRequestPayment
 и доступно только для чтения.
PaymentID – идентификатор документа; тип Integer. Свойство доступно только для
чтения.
PSBCDate – дата заявки на продажу валюты, прилагаемой к ИПВС; тип Date.
PSBCNumber – номер заявки на продажу валюты, прилагаемой к ИПВС; тип String.
State – состояние документа; тип Integer.
Вид операции – дата закрытия операции по документу; тип Date. Свойство доступно
только для чтения.

**Методы:**

AddOprState(StatusKindID:Integer, NumValue:Integer):Integer

## Класс: `RsbRequestPayment`

```rsl
RsbRequestPayment()
```

## Класс: `RsbValuable`

```rsl
RsbValuable()
```

## Класс: `RsbValueTransOrder`

```rsl
RsbValueTransOrder()
```

## Класс: `RsbWlChAcc`

```rsl
RsbWlChAcc ()
```

## Класс: `списка`

```rsl
изменений счета, связанного с учетным объектом. Сервис ввода, содержит методы BankInter.TRsbRslTemplByWrap.
```

**Методы:**

Delete(ID:Integer):Integer

## Класс: `RsbWldConfirmation`

```rsl
RsbWldConfirmation ()
```

## Класс: `RsbWlPtLnk`

```rsl
RsbWlPtLnk()
```

## Класс: `списка`

```rsl
связей субъекта - сервис ввода, содержит методы BankInter.TRsbRslTemplByWrap.
```

**Методы:**

Delete(ID:Integer):Integer

## Класс: `BOBankClaimParm`

```rsl
BOBankClaimParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOBankOrderParm`

```rsl
BOBankOrderParm ():Object
```

## Класс: `BOBankPaymentParm`

```rsl
BOBankPaymentParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOBCOrderParm`

```rsl
BOBCOrderParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOCashOrderParm`

```rsl
BOCashOrderParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOCurrencyPaymentParm`

```rsl
BOCurrencyPaymentParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOInPaymentParm`

```rsl
BOInPaymentParm ():Object
```

## Класс: `BOMemorialOrderParm`

```rsl
BOMemorialOrderParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOMultyDocParm`

```rsl
BOMultyDocParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOPaymentParm`

```rsl
BOPaymentParm ()
```

## Класс: `BOPsPayOrderParm`

```rsl
BOPsPayOrderParm ():Object
```

## Метод: `переопределяет`

```rsl
свойства валютной операции документа переданным массивом записей таблицы dpmco_dbt (параметр arr). Реквизиты валютной операции, заданные в документе ранее, удаляются.
```

**Возвращаемое значение:**



## Класс: `BOTransferOrderParm`

```rsl
BOTransferOrderParm()
```

## Класс: `BOTransferParm`

```rsl
BOTransferParm()
```

## Класс: `RsbWlHistor`

```rsl
RsbWlHistor()
```

## Процедура: `needCheckPayerBankEnterDate`

```rsl
needCheckPayerBankEnterDate():Bool
```

## Процедура: `needCheckValueDate`

```rsl
needCheckValueDate():Bool
```

## Процедура: `PM_GetDate_Balance`

```rsl
PM_GetDate_Balance(Department:Integer):Date
```

## Процедура: `PM_GetDate_BankServiceBalance`

```rsl
PM_GetDate_BankServiceBalance(Department:Integer):Date
```

## Процедура: `PM_GetDate_RetailServiceBalance`

```rsl
PM_GetDate_RetailServiceBalance(Department:Integer):Date
```

## Процедура: `PM_GetDefaultClientDate`

```rsl
PM_GetDefaultClientDate(Department:Integer, DocKind:Integer):Date
```

## Процедура: `PM_GetDefaultDate`

```rsl
PM_GetDefaultDate(DocKind:Integer,ValueDate:Date):Date
```

## Процедура: `PM_GetDefaultPayDate`

```rsl
PM_GetDefaultPayDate(DocKind:Integer, ValueDate:Date, Demand:Integer):Date
```

## Процедура: `PM_GetDefaultPayerBankEnterDate`

```rsl
PM_GetDefaultPayerBankEnterDate(Department:Integer, DocKind:Integer):Date
```

## Процедура: `PM_GetDefaultTransferDate`

```rsl
PM_GetDefaultTransferDate(Department:Integer, DocKind:Integer):Date
```

## Процедура: `PM_GetOperDay_Balance`

```rsl
PM_GetOperDay_Balance(Department:Integer [, FromDate:Date]):Date
```

## Процедура: `PM_GetDefaultValueDate`

```rsl
PM_GetDefaultValueDate(Department:Integer, DocKind:Integer):Date
```

## Процедура: `PM_GetOperDay_BankServiceBalance`

```rsl
PM_GetOperDay_BankServiceBalance(Department:Integer):Date
```

## Процедура: `PM_GetOperDay_RetailServiceBalance`

```rsl
PM_GetOperDay_RetailServiceBalance(Department:Integer):Date
```

## Процедура: `DeleteBOBankClaim`

```rsl
DeleteBOBankClaim(PaymentID: Integer):Integer
```

## Процедура: `FindBOBankClaim`

```rsl
FindBOBankClaim(PaymentID:Integer):Object
```

## Процедура: `InsertBOBankClaim`

```rsl
InsertBOBankClaim(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

**Параметры:**

Obj – объект класса BOBankClaimParm
.
MinPhase – минимальная фаза операционного дня. По умолчанию параметр содержит
значение "0".
MaxPhase – максимальная фаза операционного дня. По умолчанию параметр содержит
значение "0".
CheckPhase – признак необходимости проверки фазы операционного дня. Возможные
значения параметра:
- true – проверять фазу операционного дня;
- false – не проверять фазу операционного дня.
ContextID – контекст для криптодействий. По умолчанию параметр содержит значение "".
CheckTerrorOnUpdate – признак выполнения проверки на терроризм при обновлении. По
умолчанию значение параметра равно константе CHTUPD_NO.

**Возвращаемое значение:**



## Процедура: `UpdateBOBankClaim`

```rsl
UpdateBOBankClaim(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOBankOrder`

```rsl
DeleteBOBankOrder(PaymentID:Integer):Integer
```

## Процедура: `FindBOBankOrder`

```rsl
FindBOBankOrder(PaymentID:Integer):Object
```

## Процедура: `InsertBOBankOrder`

```rsl
InsertBOBankOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String]):Integer
```

## Процедура: `UpdateBOBankOrder`

```rsl
UpdateBOBankOrder(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String]):Integer
```

## Процедура: `DeleteBOBankPayment`

```rsl
DeleteBOBankPayment(PaymentID:Integer):Integer
```

## Процедура: `FindBOBankPayment`

```rsl
FindBOBankPayment(PaymentID:Integer):Object
```

## Процедура: `InsertBOBankPayment`

```rsl
InsertBOBankPayment(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOBankPayment`

```rsl
UpdateBOBankPayment(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `InsertBOBCOrder`

```rsl
InsertBOBCOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String]):Integer
```

## Процедура: `DeleteBOCashOrder`

```rsl
DeleteBOCashOrder(PaymentID:Integer, DocKind:Integer):Integer
```

## Процедура: `FindBOCashOrder`

```rsl
FindBOCashOrder(PaymentID:Integer):Object
```

## Процедура: `InsertBOCashOrder`

```rsl
InsertBOCashOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOCashOrder`

```rsl
UpdateBOCashOrder(PaymentID:Integer , Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOCurrencyPayment`

```rsl
DeleteBOCurrencyPayment(PaymentID:Integer):Integer
```

## Процедура: `FindBOCurrencyPayment`

```rsl
FindBOCurrencyPayment(PaymentID:Integer):Object
```

## Процедура: `InsertBOCurrencyPayment`

```rsl
InsertBOCurrencyPayment(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOCurrencyPayment`

```rsl
UpdateBOCurrencyPayment(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOMemorialOrder`

```rsl
DeleteBOMemorialOrder(PaymentID:Integer):Integer
```

## Процедура: `FindBOMemorialOrder`

```rsl
FindBOMemorialOrder(PaymentID:Integer):Object
```

## Процедура: `InsertBOMemorialOrder`

```rsl
InsertBOMemorialOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOMemorialOrder`

```rsl
UpdateBOMemorialOrder(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOMultyDoc`

```rsl
DeleteBOMultyDoc(PaymentID:Integer):Integer
```

## Процедура: `FindBOMultyDoc`

```rsl
FindBOMultyDoc(PaymentID:Integer):Object
```

## Процедура: `InsertBOMultyDoc`

```rsl
InsertBOMultyDoc(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOMultyDoc`

```rsl
UpdateBOMultyDoc(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOPSPayOrder`

```rsl
DeleteBOPSPayOrder(PaymentID:Integer):Integer
```

## Процедура: `FindBOPSPayOrder`

```rsl
FindBOPSPayOrder(PaymentID:Integer):Object
```

## Процедура: `InsertBOPSPayOrder`

```rsl
InsertBOPSPayOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOPSPayOrder`

```rsl
UpdateBOPSPayOrder(PaymentID:Integer , Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Bool] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `DeleteBOTransferOrder`

```rsl
DeleteBOTransferOrder(PaymentID:Integer):Integer
```

## Процедура: `FindBOTransferOrder`

```rsl
FindBOTransferOrder(PaymentID:Integer):Object
```

## Процедура: `InsertBOTransferOrder`

```rsl
InsertBOTransferOrder(Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Integer] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `UpdateBOTransferOrder`

```rsl
UpdateBOTransferOrder(PaymentID:Integer, Obj:Object [, MinPhase:Integer] [, MaxPhase:Integer] [, CheckPhase:Integer] [, ContextID:String] [, CheckTerrorOnUpdate:Integer]):Integer
```

## Процедура: `PM_FillPropVOOnDefault`

```rsl
PM_FillPropVOOnDefault (PaymentID:Integer, Code:Integer):Integer
```

## Процедура: `PM_RollbackOperation`

```rsl
PM_RollbackOperation (PaymentID:Integer [, ident:String]):Integer
```

## Процедура: `PM_RollbackStep`

```rsl
PM_RollbackStep (PaymentID:Integer,  [OperationID:Integer, ] StepID| SymbolID:Integer|String [, ident:String]):Integer
```

## Процедура: `PM_GetRejectProcessKind`

```rsl
PM_GetRejectProcessKind ([AskIfUndef:Bool]):Integer
```

## Процедура: `PM_SetRejectProcessKind`

```rsl
PM_SetRejectProcessKind (ProcKind:Integer)
```

## Процедура: `CheckDeletePayment`

```rsl
CheckDeletePayment (PaymentID:Integer):Integer
```

## Процедура: `CheckPaymentWithScrollMacro`

```rsl
CheckPaymentWithScrollMacro(paymentID:Integer, operation:Integer):Integer
```

## Процедура: `FillPaymentAccounts`

```rsl
FillPaymentAccounts (Payer:Integer, Receiver:Integer, Kind_Operation:Integer, Paym: Record [, Debet: Record] [,Credit: Record] [,error:String]):Integer
```

## Процедура: `FillPaymentBySettAcc`

```rsl
FillPaymentBySettAcc (SettAccID:Integer, prop_type:Integer, paym:Record, prop:Record, [rm:Record], [ErrMsg:String, Variant]):Integer
```

## Процедура: `FindDupPayment`

```rsl
FindDupPayment ([PaymentID:Integer], [Purpose:Integer], [SubPurpose:Integer], [DocKind:Integer], [DocID:Integer], [FromDB:Bool], [paym:Record], [debet:Record], [credit:Record], [rm:Record]):Integer
```

## Процедура: `FindPayment`

```rsl
FindPayment ([PaumentID:Integer, ] [Purpose:Integer, ] [SubPurpose:Integer, ] [DocKind:Integer, ] [DocID:Integer, ] [FromDB:Bool, ] [pm:Record, ] [d:Record, ] [k:Record, ] [rm:Record, ] [cp:Record]):Integer
```

## Процедура: `FindPaymentFactValueDate`

```rsl
FindPaymentFactValueDate (PaymentID:Integer, Record):Date
```

## Процедура: `GetDocsByPaym`

```rsl
GetDocsByPaym (PaymentID:Integer, Purpose:Integer, SubPurpose:Integer, DocKind:Integer, DocID:Integer, Context:Memaddr, d:File, Record, TRecHandler):Bool
```

## Процедура: `GetDocsByPaym_Close`

```rsl
GetDocsByPaym_Close ([Context:Memaddr]):Bool
```

## Процедура: `GetFinResult`

```rsl
GetFinResult (Amount:MoneyL, PaymentID:Integer):Bool
```

## Процедура: `GetFirstReceipt`

```rsl
GetFirstReceipt (OriginalPayment:File, Record, SelectedPayment:File, Record):Integer
```

## Процедура: `GetMultiPayments`

```rsl
GetMultiPayments (Op:Integer, [Status:Integer] [,Paym:Memaddr] [,FIID:Integer] [,Corschem:Integer]):Bool
```

## Процедура: `GetPaymRestAfterMeetInd2`

```rsl
GetPaymRestAfterMeetInd2 (PaymentID:Integer, DocKind:Integer, DocumentID:Integer, Purpose: Integer, SubPurpose: Integer, Summa:Money, ErrMsg:String):Integer
```

## Процедура: `InitPM_PAYMPROP`

```rsl
InitPM_PAYMPROP (pmprop:TRecHandler): Bool
```

## Процедура: `IsNeedIncludeInMP`

```rsl
IsNeedIncludeInMP ():Integer
```

## Процедура: `MakeDocByPayment`

```rsl
MakeDocByPayment (Document: Record, Paym: Record, Debet: Record, Credit: Record, RM: Record):Integer
```

## Процедура: `MakeDocByPaymentID`

```rsl
MakeDocByPaymentID (PaymentID:Integer, Purpose:Integer, SubPurpose:Integer, DocKind:Integer, DocID:Integer, FromDB:Bool, doc:Record):Integer
```

## Процедура: `MakePartOrders`

```rsl
MakePartOrders(PaymentID:Integer, DocKind:Integer, Amount:Money [, ValueDate:Date]):Integer
```

## Процедура: `MFR_GetNextDepartment`

```rsl
MFR_GetNextDepartment (Department : Integer, EndDepartment : Integer) : Integer
```

## Процедура: `PaymInChangeDPP`

```rsl
PaymInChangeDPP (paym : Record [, debet : Record] [, credit : Record] [, ReadOnly : Integer] [, NewTransferDate : Date, Variant]) : Bool
```

## Процедура: `PaymOutChangeDPP`

```rsl
PaymOutChangeDPP (paym : Record [, debet : Record] [, credit : Record] [, ReadOnly : Integer] [, NewTransferDate : Date, Variant]) : Bool
```

## Процедура: `PM_CheckCommunalProp`

```rsl
PM_CheckCommunalProp(PaymentID:Integer):Bool
```

## Процедура: `PM_DenialPanel`

```rsl
PM_DenialPanel (Payment : Object, IndexNum : Integer, [LockAmount : BOOL]) : Bool
```

## Процедура: `PM_GenerateMessage`

```rsl
PM_GenerateMessage (PaymentID:Integer [, RlsFormID:Integer] [, TpSchemID:Integer]):Integer
```

## Процедура: `PM_GetDefaultPaymentKind`

```rsl
PM_GetDefaultPaymentKind (DocKind:Integer, [SubKind:Integer]):String
```

## Процедура: `PM_GetHaveCarry`

```rsl
PM_GetHaveCarry (PaymentID : Integer) : Bool
```

## Процедура: `PM_GetI2PlaceDate`

```rsl
PM_GetI2PlaceDate (PaymentID : Integer) : Date
```

## Процедура: `PM_GetPaymentExecutionDate`

```rsl
PM_GetPaymentExecutionDate (PaymentID:Integer, ExecutionDate:Date):Integer
```

## Процедура: `PM_ListPMPOPKND`

```rsl
PM_ListPMPOPKND():String
```

## Процедура: `PM_MassExecuteOperation`

```rsl
PM_MassExecuteOperation ([Silent:Bool], [Symbol:String]):Integer
```

## Процедура: `PM_ProcessPanel`

```rsl
PM_ProcessPanel(Payment:Object[, Enable:Integer] [, FlgPM:Array] [, FlgRM:Array] [, FlgCP:Array] [, FlgMBK:Array] [, FlgSecur:Array] [, FlgAkkr:Array] [, PreserveClientName:Bool] [, UserKey:Integer] [, UserMenuItem:String] [, MacroFile:String] [, MacroProc:String]):Integer
```

## Процедура: `PM_RatePanel`

```rsl
PM_RatePanel (PaymentID : Integer) : Integer
```

## Процедура: `PM_RollBackAndDeletePmDocument`

```rsl
PM_RollBackAndDeletePmDocument(PaymentID:Integer, CheckIsChild:Bool, SendReceiptForCLB:Bool, DeleteParmForCLB:Bool):Integer
```

## Процедура: `PmGetDefaultOutTransferDate`

```rsl
PmGetDefaultOutTransferDate (PaymentObj : Object) : Date
```

## Процедура: `SelectReceipt`

```rsl
SelectReceipt (OriginalPayment : File, Record, SelectedPayment : File, Record):Integer
```

## Процедура: `ShowPanelTimeExecInstancyPM`

```rsl
ShowPanelTimeExecInstancyPM (date : Date, time : Time, TypeTime : Integer) : Bool
```

## Процедура: `UpdatePayment`

```rsl
UpdatePayment (pm: TRecHandler, debet: TRecHandler, credit: TRecHandler, rm: TRecHandler, bttax: TRecHandler):Integer
```

## Процедура: `BindReserve`

```rsl
BindReserve (ClaimID:Integer, DocKind:Integer, DocID:Integer [, DocNumber:String] [, RebindRes:Bool]):Integer
```

## Процедура: `BindReserveEx`

```rsl
BindReserveEx (ClaimID:Integer, DocKind:Integer, DocID:Integer [, DocNumber:String] [, RebindRes:Bool]):Integer
```

## Процедура: `GetReserveAmount`

```rsl
GetReserveAmount ([Amount:MoneyL, ] [Date:Date, ] [FIID:Integer, ] [PaymentID:Integer]):Bool
```

## Процедура: `GetReserveChange`

```rsl
GetReserveChange ():Bool
```

## Процедура: `GetReserveInfo`

```rsl
GetReserveInfo (DocKind:Integer, DocumentID:Integer, OnDate:Date, ClaimID:Integer, AmountOnDate:Money, StateOnDate:Integer [, Account:String] [, Chapter:Integer] [, FIID:Integer]):Integer
```

## Процедура: `PM_IsMadeReserveOnStep`

```rsl
PM_IsMadeReserveOnStep():Bool
```

## Процедура: `WRTGetPortfolioAmount`

```rsl
WRTGetPortfolioAmount (Department:Integer, FIID:Integer, Party:Integer, Contract:Integer, Portfolio:Integer, Group:Integer, CalcDate:Date, Delivered:Bool, NotDelivered:Bool, WithAccept:Bool [, IsTrust:Bool]):Money
```

## Процедура: `WRTReserveLot`

```rsl
WRTReserveLot (OperDate : Date, SumID : Long, ID_Operation : Long, ID_Step : Integer, ReservAmount : Money, SetIncomeReserv : Bool, IncomeReserv : Money) : Bool
```

## Процедура: `WRT_Calc`

```rsl
WRT_Calc (Department:Integer, FIID:Integer, Party:Integer, Contract:Integer, pGroup:Integer, CalcDate:Date, Calc:Record, [Delivered:Bool, ] [WithAccept:Bool]):Bool
```

## Процедура: `WRT_ChoicePortofolio`

```rsl
WRT_ChoicePortofolio (ClientID:Integer, FIID:Integer, Type:Integer, Product:Integer, AvoirKind:Integer, Quoted:Integer, IssuerKind:Integer [, wrtgrp: Record] [, err:Integer]):Bool
```

## Процедура: `WRT_GetSaleFinResult`

```rsl
WRT_GetSaleFinResult (SaleID:Integer, Portfolio:Integer, ParentLot:Integer [, CostBuy:Money, BalanceCostBuy:Money, NKDBuy:Money, InterestIncomeBuy: Money, DiscountIncomeBuy:Money, NotCarryInterestBuy:Money, NotCarryDiscountBuy:Money, InterestIncomeAdd: Money, DiscountIncomeAdd:Money, NotCarryInterestAdd:Money, NotCarryDiscountAdd:Money, InterestIncomeSum:Money, DiscountIncomeSum: Money, NotCarryInterestSum:Money, NotCarryDiscountSum:Money, BalanceCostSum:Money, OutlayBuy:Money, OverAmountBuy:Money, ReservAmountBuy:Money, BalanceCostBD:Money, CostSale:Money, NKDSale:Money]):Bool
```

## Процедура: `WRT_TotalCalc`

```rsl
WRT_TotalCalc (Department : Integer, FIID : Integer, Party : Integer, Contract : Integer, TypePort : Integer, Date : Date, CalcTime : Time, StartDate : Date, CalcWrt : Record [, Delivered : Bool] [, WithAccept : Bool]) : Bool
```

## Процедура: `BalMoneySum`

```rsl
BalMoneySum ([Error:Integer, ] [Purpose:Integer, ] [SubPurpose:Integer, ] [DocKind:Integer, ] [DocumentID:Integer, ] [PartyID:Integer]):MoneyL
```

## Процедура: `BalMoneySumDate`

```rsl
BalMoneySumDate ([Amount: Integer, ] [Error:Integer, ] [FIID:Integer, ] [Dprt:Integer, ] [Delivery:Integer, ] [Date:Date, ] [PartyID:Integer]):MoneyL
```

## Процедура: `BalPrice`

```rsl
BalPrice ([Amount:MoneyL, ] [, Error:Integer, ] [, Purpose:Integer, ] [, SubPurpose:Integer, ] [, DocKind:Integer, ] [, DocumentID:Integer ] [, PartyID:Integer]):MoneyL
```

## Процедура: `BalPriceDate`

```rsl
BalPriceDate ([Amount:MoneyL, ] [Error:Integer, ]  [FIID:Integer, ] [Dprt:Integer, ] [Delivery:Integer, ] [Date:Date, ] [PartyID:Integer]):MoneyL
```

## Процедура: `BalSPSum`

```rsl
BalSPSum ([Error:Integer, ] [Purpose:Integer, ] [SubPurpose:Integer, ] [DocKind:Integer, ] [DocumentID:Integer, ] [PartyID:Integer]):MoneyL
```

## Процедура: `BalSPSumDate`

```rsl
BalSPSumDate (Error:Integer, FIID:Integer, Dprt:Integer, Delivery:Integer, Date:Date, PartyID:Integer):Money
```

## Процедура: `BB_COControlScrol`

```rsl
BB_COControlScrol(Symbol:String, SqlLink:String):Integer
```

## Процедура: `WriteOffSum`

```rsl
WriteOffSum ([Amount:MoneyL [, Error:Integer [, Purpose:Integer [, SubPurpose:Integer [, DocKind:Integer [, DocumentID:Integer [, PartyID:Integer]]]]]]]):Money
```

## Процедура: `WRTOverValue`

```rsl
WRTOverValue (OperDate:Date, FIID:Integer, Department:Integer, ID_Operation:Integer, ID_Step:Integer, Course :Money [G1, G2, G3, G4, G5:Integer, ] [BC1, BC2, BC3, BC4, BC5:Integer, ] [A1, A2, A3, A4, A5:Money, ] [OBC1, OBC2, OBC3, OBC4, OBC5:Integer, ] [O1, O2, O3, O4, O5:Integer]):Bool
```

## Процедура: `ПолучитьУзелОсновнойИнструкции`

```rsl
ПолучитьУзелОсновнойИнструкции (ObjKind:Integer, ObjID:Integer, Direct:Integer [, Route:Trechandler]):Bool
```

## Процедура: `ПолучитьБлижайшийУзел`

```rsl
ПолучитьБлижайшийУзел (ObjKind:Integer, ObjID:Integer, Direct:Integer [, Route:Trechandler]):Bool
```

## Процедура: `ПолучитьСамыйДальнийУзел`

```rsl
ПолучитьСамыйДальнийУзел (ObjKind:Integer, ObjID:Integer, Direct:Integer [, Route:Trechandler]):Bool
```

## Процедура: `ПерейтиНаБолееБлизкийУзел`

```rsl
ПерейтиНаБолееБлизкийУзел (Direct:Integer [, Route:Trechandler] ):Bool
```

## Процедура: `переходит`

```rsl
на более близкий узел.
```

**Параметры:**

Direct – вид ветки маршрута (RTDIR_IN или RTDIR_OUT).
Route – параметр куда будет записан буфер найденного узла маршрута.
Возвращаемые значения:

## Процедура: `ПерейтиНаБолееДальнийУзел`

```rsl
ПерейтиНаБолееДальнийУзел (Direct:Integer [, Route:Trechandler] ):Bool
```

## Процедура: `переходит`

```rsl
на более дальний узел.
```

**Параметры:**

Direct – вид ветки маршрута (RTDIR_IN или ).
Route – параметр куда будет записан буфер найденного узла маршрута.
Возвращаемые значения:

## Процедура: `AllowUseNonAcceptClaim`

```rsl
AllowUseNonAcceptClaim():Bool
```

## Процедура: `Bnk_GetCurrCode`

```rsl
Bnk_GetCurrCode(FIID:Integer):String
```

## Процедура: `Bnk_IsBatchMode`

```rsl
Bnk_IsBatchMode():Bool
```

## Процедура: `Bnk_ToRSTrace`

```rsl
Bnk_ToRSTrace (Categ:String[, Event:String], Message:String)
```

## Процедура: `CheckCorsLimits`

```rsl
CheckCorsLimits (PaymentObj:Object, [isOutCor:Bool]):Integer
```

## Процедура: `CheckExternalPaymentForRls`

```rsl
CheckExternalPaymentForRls (PaymentID:Integer, [err:String, Variant], [SendEmailErrMes:Bool]):Integer
```

## Процедура: `CopyParentRequisites`

```rsl
CopyParentRequisites (parentPaymID:Integer, childPaymID:Integer
```

## Процедура: `CreateNoticeEvent`

```rsl
CreateNoticeEvent(Code:String, [Description:String], [Param:String]):Integer
```

## Процедура: `Deal_ExecuteOperation`

```rsl
Deal_ExecuteOperation (DealID:Integer [, Symbol:String] [,PaymentList:Tarray] [, FinishDeal:Bool] [, AutoAction:Integer]):Integer
```

## Процедура: `DefineRlsForm`

```rsl
DefineRlsForm (PaymentObj:Object [, TpID Integer] [, TpShemID:Integer] [, FormID:Integer] [, RlsFormID:Integer]):Bool
```

## Процедура: `EraseCachedVar`

```rsl
EraseCachedVar(Context:String):Bool
```

## Процедура: `GetCachedVar`

```rsl
GetCachedVar ([context:String] [, macro:String]):Variant
```

## Процедура: `GetCurDateFlag`

```rsl
GetCurDateFlag(RealAttrVal:String):String
```

## Процедура: `GetLastDocumentID`

```rsl
GetLastDocumentID():Integer
```

## Процедура: `GetLastPaymentsNumber`

```rsl
GetLastPaymentsNumber ():String
```

## Процедура: `GetMaxDate`

```rsl
GetMaxDate(RealAttrVal:String):Date
```

## Процедура: `GetMinDate`

```rsl
GetMinDate(RealAttrVal:String):Date
```

## Процедура: `GetMultNoteReject`

```rsl
GetMultNoteReject (NoteStr:String):Bool
```

## Процедура: `GetOffSet`

```rsl
GetOffSet (RealAttrVal:String):Integer
```

## Процедура: `IsAccountNotInGKBOAllowed`

```rsl
IsAccountNotInGKBOAllowed(doc_kind:Integer, prim_doc_origin:Integer, paym_status:Integer, Group:Integer):Bool
```

## Процедура: `IsExistCallBack`

```rsl
IsExistCallBack(PaymentID:Integer, State:Integer [, wlreq:Record]):Bool
```

## Процедура: `IsManualInsertEditBO`

```rsl
IsManualInsertEditBO():Bool
```

## Процедура: `IsPSBRParticipate`

```rsl
IsPSBRParticipate(PartyID:Long, Role:String, Message:String):Integer
```

## Процедура: `IsReturnMFR`

```rsl
IsReturnMFR():Bool
```

## Процедура: `MakeAccountID`

```rsl
MakeAccountID(chapterID:Integer, currencyID:Integer, account:String, accountID:String, len_accID:Integer)
```

## Процедура: `MFR_BankInCABS`

```rsl
MFR_BankInCABS (BankID : Integer) : Bool
```

## Процедура: `MFR_IsOurBank`

```rsl
MFR_IsOurBank (BankID : Integer) : Bool
```

## Процедура: `PM_AccountIsMFR`

```rsl
PM_AccountIsMFR (Account : String, Chapter : Integer, FIID : Integer) : Bool
```

## Процедура: `PM_CallBackMFRPayment`

```rsl
PM_CallBackMFRPayment(PaymentID:Integer, AskBindDossier:Bool):Integer
```

## Процедура: `PM_ComplexOrderRevoke`

```rsl
PM_ComplexOrderRevoke(PaymentID:Integer, DocKind:Integer):Integer
```

## Процедура: `PM_DeleteBranch`

```rsl
PM_DeleteBranch(PaymentID:Integer, BranchSymbol:String, ident:String):Integer
```

## Процедура: `PM_ExecuteOperation`

```rsl
PM_ExecuteOperation (DocumentID:Integer, DocKind:Integer):Bool
```

## Процедура: `PM_FindBalanceInReg_117`

```rsl
PM_FindBalanceInReg_117 (KeyPath : String, Account : String [, mode : Integer]) : Bool
```

## Процедура: `PM_GetActionAddControlFM`

```rsl
PM_GetActionAddControlFM():Integer
```

## Процедура: `PM_GetCheckNameOption`

```rsl
PM_GetCheckNameOption (): Integer
```

## Процедура: `PM_GetPayerChargeOffDate`

```rsl
PM_GetPayerChargeOffDate (PaymentID : Integer) : Date
```

## Процедура: `PM_InsertAndExecuteBranch`

```rsl
PM_InsertAndExecuteBranch(PaymentID:Integer, StepSymbol:String, BranchSymbol:String, kind:String, ident:String):Bool
```

## Процедура: `PM_IsInternalPayerAccount`

```rsl
PM_IsInternalPayerAccount (paym : Record [, debet : Record]) : Bool
```

## Процедура: `PM_IsInternalReceiverAccount`

```rsl
PM_IsInternalReceiverAccount (paym : Record [, credit : Record]) : Bool
```

## Процедура: `PM_IsNeededStepReadyForExec`

```rsl
PM_IsNeededStepReadyForExec(PaymentID:Integer, Symbol:String):Bool
```

## Процедура: `PM_NeedDocumentRestart`

```rsl
PM_NeedDocumentRestart () : Bool
```

## Процедура: `PM_NeedRejectControl`

```rsl
PM_NeedRejectControl () : Bool
```

## Процедура: `PM_ReturnMFRPayment`

```rsl
PM_ReturnMFRPayment(pmpaym:Trechandler):Integer
```

## Процедура: `PM_RevokeOrder`

```rsl
PM_RevokeOrder (PaymentID:Integer, DocKind:Integer, CallSource:Integer, BuffDenial:Record,Trechandler):Integer
```

## Процедура: `PM_SetClientName`

```rsl
PM_SetClientName (paym : Record, rm : Record, debet : Record, credit : Record, side : Integer [, ClientName : String, Variant]) : Bool
```

## Процедура: `PM_SetClientNameGlobal`

```rsl
PM_SetClientNameGlobal (Account : Record [, NameClient : String, Variant] [, INNClient : String, Variant]) : Integer
```

## Процедура: `PrintEA`

```rsl
PrintEA(PrintEA:Bool, EDocKindID:Integer, EDocID:String, PrintType:Integer, Symbol:String):Integer
```

## Процедура: `SetCachedVar`

```rsl
SetCachedVar ([context : String] [, val : Variant]) : Bool
```

## Процедура: `SetNoteReject`

```rsl
SetNoteReject (NoteStr : String) : Bool
```

## Процедура: `SetReasonReject`

```rsl
SetReasonReject (Reason:String):Integer
```

## Процедура: `UFEBS_CheckDrawerStatus`

```rsl
UFEBS_CheckDrawerStatus(ReceiverBankID:Integer, Date:Date, EDDate:Date, [ReceiverBankAccount:String], [ReceiverAccount:String], [TaxAuthorState:String]):Integer
```

## Процедура: `WRTChargeIncomToLots`

```rsl
WRTChargeIncomToLots (OperDate:Date, EndDate : Date, FIID:Integer, Department:Integer, ID_Operation:Integer, ID_Step:Integer, Party : Integer, Contract : Integer, [, G1, G2, G3, G4, G5:Integer] [, CalcInterest : Bool] [, CalcDiscount : Bool]):Bool
```

## Процедура: `WRTGetGlobalMovingFinResult`

```rsl
WRTGetGlobalMovingFinResult (ID_Operation:Integer, ID_Step:Integer, Action:Integer, Source:Integer, Goal:Integer, State : Integer, DocKind : Integer, DocID : Integer [, Cost:Money] [, NKD:Money] [, BalanceCost:Money]  [, InterestIncome:Money] [, DiscountIncome:Money] [, NotCarryInterest:Money] [, NotCarryDiscount:Money] [, OverAmount : Money] [, ReservAmount : Money] [, IncomeReserv : Money]):Bool
```

## Процедура: `WRTOvervalueLot`

```rsl
WRTOvervalueLot (OperDate:Date, SumID:Integer, ID_Operation:Integer, ID_Step:Integer, BalanceCost:Money, OverAmount:Money, IsBD : Bool):Bool
```

## Процедура: `WRT_GetLotSumOnDate`

```rsl
WRT_GetLotSumOnDate (Lot: File, Record, Tbfile, Date:Date, Params: File, Record, Tbfile):Bool
```

## Процедура: `WRTCalcCouponIncome`

```rsl
WRTCalcCouponIncome (SumID:Long, Number:String, Date:Date, CurSum:Money, CurAmount:Money [, Portfolio:Long] [, IncomeSum:Money] [, NKD:Money] [, InterestIncomeSum:Money] [, InterestIncomeAdd:Money] [, NotCarryInterestSum:Money] [, NewBalanceCost:Money] [, BonusAdd:Money] [, NewBonus:Money] [, NewCost:Money]):Bool
```

## Процедура: `WRTCalcPartialIncome`

```rsl
WRTCalcPartialIncome (SumID:Long, Partly:String, CalcDate:Date, CurSum:Money, CurAmount:Money [, Portfolio:Long] [, IncomeSum:Money] [, DiscountIncomeSum:Money] [, DiscountIncomeAdd:Money] [, NotCarryDiscountSum:Money] [, NewCost:Money] [, NewBalanceCost:Money] [, NewOutlay:Money] [, NewDiscountIncome:Money] [, NewNotCarryDiscountIncome:Money]):Bool
```

## Процедура: `WRTGetRestoreLotOnDate`

```rsl
WRTGetRestoreLotOnDate (SumID : Long, LotDate : Date, Lot : Record) : Bool
```

## Процедура: `WRTRejectDeal`

```rsl
WRTRejectDeal (p_SumID : Integer, p_OperDate : Date, p_Portfolio : Integer, p_GroupID : Integer, p_Amount : Money, p_Sum : Money, p_Currency : Integer, p_Cost : Money, p_NKD : Money, p_BegDiscount : Money, p_ID_Operation : Integer, p_ID_Step : Integer) : Bool
```

## Процедура: `DateAfterCalenDays`

```rsl
DateAfterCalenDays (date:Date, days:Integer):Date
```

## Процедура: `DateAfterCalenMonths`

```rsl
DateAfterCalenMonths (date:Date, months:Integer):Date
```

## Процедура: `DateAfterWorkDays`

```rsl
DateAfterWorkDays (date:Date, days:Integer [, id_c:Integer]):Date
```

## Процедура: `DateAfterWorkDays`

```rsl
возвращает дату, которая находится через требуемое количество рабочих дней от указанной даты с учетом високосных лет.
```

**Параметры:**

date – дата типа V_DATE, от которой нужно отсчитать количество дней, заданное в
параметре days.
days – количество дней, через которое нужно вычислить дату. Параметр типа
V_INTEGER.
id_c – идентификатор календаря; необязательный параметр. Если параметр не задан,
используется календарь по умолчанию.

## Процедура: `DateAfterWorkMonths`

```rsl
DateAfterWorkMonths (date:Date, months:Integer [, id_c:Integer]):Date
```

## Процедура: `FindDate`

```rsl
FindDate(Date:Date [, Branch:Integer] [, ServiceKind:Integer] [, Balance:Integer] [, NextDays:Integer] [, NextDaysServiceKind:Integer] [, NextDaysBalance:Integer]):Date
```

## Процедура: `FloatMonths`

```rsl
FloatMonths (start:Date, end:Date):Double
```

## Процедура: `GetDateAfterMonthsWBranch`

```rsl
GetDateAfterMonthsWBranch(Date:Date, mon:Integer, monthLen:Integer [, Branch:Integer]):Date
```

## Процедура: `GetDateAfterWorkDays`

```rsl
GetDateAfterWorkDays ( date:Date, period:Date [, ID:Integer ] ):Date
```

## Процедура: `GetDateAttr`

```rsl
GetDateAttr(Date:Date, ServiceKind:Integer, Balance:Integer [, Branch:Integer]):Integer
```

## Процедура: `GetDateByCalendar`

```rsl
GetDateByCalendar([BaseDate:Date]): Date
```

## Процедура: `GetDaysInMonth`

```rsl
GetDaysInMonth (Date:Date) : Integer
```

## Процедура: `GetNextDate`

```rsl
GetNextDate(Date:Date [, Branch:Integer] [, ServiceKind:Integer] [, Balance:Integer]):Date
```

## Процедура: `GetNextDateAfterDays`

```rsl
GetNextDateAfterDays(Date:Date [, Branch:Integer] [, ServiceKind:Integer] [, Balance:Integer] [, Days:Integer]):Date
```

## Процедура: `GetNextWorkDate`

```rsl
GetNextWorkDate(Date:Date, WorkDays:Integer [, Branch:Integer]):Date
```

## Процедура: `GetWorkDaysNumBranch`

```rsl
GetWorkDaysNumBranch(firstDate:Date, lastDate:Date [, Branch:Integer]):Integer
```

## Процедура: `IsHoliday`

```rsl
IsHoliday ( Date:Date [, id_c:Integer]):Integer
```

## Процедура: `IsWorkday`

```rsl
IsWorkday ( Date:Date [, id_c:Integer]):Integer
```

## Процедура: `IsWorkDayBranch`

```rsl
IsWorkDayBranch(Date:Date [, Branch:Integer]):Integer
```

## Процедура: `NDays`

```rsl
NDays ( inval:Date, inval:Date):Integer
```

## Процедура: `NDays30`

```rsl
NDays30 (inval:Date, inval:Date):Integer
```

## Процедура: `NDays30Correct`

```rsl
NDays30Correct (DateBeg:Date, DateEnd:Date):Integer
```

## Процедура: `Workdays`

```rsl
Workdays (beg_d:Date, end_d:date [, id_c:Integer]):Integer
```

## Класс: `InterestDeal`

```rsl
InterestDeal():Object
```

## Класс: `InterestDeal`

```rsl
представляет собой процентный калькулятор.
```

**Свойства:**

Данный класс имеет следующие свойства, доступные для чтения и записи:
Principal – объем средств; тип Double.
Mode – режим включения в расчет границ периода расчета процентов. Возможные
значения:
- PCIDC_M_STARTEXCLUDED – исключать из расчета дату начала периода
расчета.
- PCIDC_M_MATURITYEXCLUDED – исключать из расчета дату окончания
периода расчета.
Basis – базис расчета процентов. Возможные значения:
- BASIS_ACTACT – число дней в месяце и в году по календарю.
- BASIS_30360 – в месяце 30 дней, в году 360 дней.
- BASIS_30ACT – в месяце 30 дней, число дней в году по календарю.
- BASIS_30360NOLEAP – в месяце 30 дней, в году 360 дней без учета
високосного года.
- BASIS_30ACTNOLEAP – в месяце 30 дней, число дней в году по календарю без
учета високосного года.
- BASIS_ACT360 – число дней в месяце по календарю, в году 360 дней.
- BASIS_ACT360NOLEAP – число дней в месяце по календарю, в году 360 дней
без учета високосного года.
- BASIS_ACT365 – число дней в месяце по календарю, в году 365 дней.
Pitch – единица продолжительности процентного периода. Возможные значения:
- PITCH_DAYS – дни.
- PITCH_WEEKS – недели.
- PITCH_MONTHS – месяцы.
- PITCH_YEARS – годы.
Start – дата размещения средств; тип Date.
Point – количество точек после запятой в ставке; тип Integer.
Scale – масштаб ставки, для процентов всегда равный 100; тип Integer.
Maturity – дата возврата средств; тип Date.
Duration – формальная продолжительность процентного периода; тип Double.
Rate – процентная ставка; целочисленное значение типа Double.

**Пример:**

Для ставки 123.4567% Rate=1234567, Point=4, Scale=100.
Interest – сумма процентов; тип MoneyL.
FValue – будущая стоимость, равная сумме свойств Interest и Principal; тип MoneyL.
Priority – приоритеты полей калькулятора. Строка вида "SFRIPDM", чем ближе код поля к
началу строки, тем больший приоритет у поля.

**Методы:**

Guess()
Расчет калькулятора на основании приоритетов.
Возвращаемое значение
Конструктор данного класса возвращает объект типа V_GENOBJ.

**Пример:**

var idc;
idc = InterestDeal();
idc.priority = "SFRIPDM";
idc.principal = $0;
idc.interest = $0;
idc.rate = 3650000; /*точность по умолчанию 4 знака*/
idc.fvalue = $1000;
idc.start = DATE(4,3,2002);
idc.maturity = DATE(4,4,2002);
msgbox("principal = ", idc.principal);
idc.Guess();
msgbox("principal = ", idc.principal);
Константы
Способ расчета процентов
PRC_CALC_MODE_ORDINARY – расчет за указанный период.
PRC_CALC_MODE_TOTAL – расчет нарастающим итогом, при этом учитываются суммы
процентов всех периодов, начиная с даты начала действия процентного
договора.
Тип объекта-владельца счета процентов
PRC_ACCOUNT – счета.
PRC_ACCOUNT_AOVR – счет процентов для овердрафтной части счета.
PRC_ACCOUNT_CUR – валютные счета.
PRC_ACCOUNT_DEP – счет (частный вклад).
PRC_ACCOUNT_RUB – рублевые счета.
PRC_ACCOUNT_TOVR – счет процентов для овердрафтной части типа вклада.
PRC_ACCOUNT_TYPE – тип вклада (частного).
PRC_DEAL_LOAN – по сделке займа.
PRC_IBC_CON – кредит МБК.
PRC_IBC_CON_EXP – просроченная задолженность по кредиту МБК.
PRC_IBC_CON_EXPPC – задолженность по оплате процентов по кредиту МБК.
PRC_OBACC_CUR – валютные внебалансовые счета.
PRC_OBACC_RUB – рублевые внебалансовые счета.
PRC_TYPE_NONE – не задан.
PRC_VEKSEL – по векселю.
PRC_VEKSEL_CALL – по векселю (до востребования).
PRC_WLD_CUR – валютные корсчета МБР.
PRC_WLD_RUB – рублевые корсчета МБР.
Процедуры

## Процедура: `PcAddSumToDate`

```rsl
PcAddSumToDate (autoPerc:Integer [, Date:Date] [, Sum:Moneyl]):Bool
```

## Процедура: `pcinsertsumlist`

```rsl
pcinsertsumlist (Date:Date):Integer
```

## Процедура: `Prc_CalcPeriodOnDate`

```rsl
Prc_CalcPeriodOnDate(ContractID:Integer, SchedKind:Integer, Date:Date, Mode:Integer, Sum:Money):Integer
```

## Процедура: `Prc_CalcPrcValues`

```rsl
Prc_CalcPrcValues(ContractID:Long, BeginDate:Date, EndDate:Date, PeriodSum:Money, [DailyCalc:Integer]):Integer
```

## Процедура: `Prc_CreateContractByObject`

```rsl
Prc_CreateContractByObject(PrcContract:Object, ContractID:Integer):Integer
```

## Процедура: `Prc_GenerateCalendarGraph`

```rsl
Prc_GenerateCalendarGraph(ContractID:Integer, ScheduleID:Integer):Integer
```

## Процедура: `Prc_RecalcPeriodOnDate`

```rsl
Prc_RecalcPeriodOnDate(ContractID:Integer, SchedKind:Integer, Date:Date, Mode:Integer, Sum:Money):Integer
```

## Процедура: `Prc_ReGenerateCalendarGraphEndDate`

```rsl
Prc_ReGenerateCalendarGraphEndDate(ContractID:Integer, SchedKind:Integer, OldEndDate:Date, NewEndDate:Date):Integer
```

## Процедура: `Prc_SetRateVal`

```rsl
Prc_SetRateVal(ContractID:Integer, Date:Date, Rate:Double, isPrognoz:Bool):Integer
```

## Процедура: `SelectRangeMarketRate`

```rsl
SelectRangeMarketRate(ServiseKind:Integer, BranchID:Integer, ProductKindId:Integer, ProductId:Integer, ContractYear:Integer, ContractMonths:Integer, ContractDays:Integer, ContractSum:Money, FiId:Integer, ClientType:Integer, Date:Date, MinValue:Money, MaxValue:Money, SourceDataLayer:Integer):Bool
```

## Процедура: `SelectRangeMarketRateEx`

```rsl
SelectRangeMarketRateEx(ServiseKind:Integer, BranchID:Integer, ProductKindId:Integer, ProductId:Integer, InterestFrequency:Integer, ContractYear:Integer, ContractMonths:Integer, ContractDays:Integer, ContractSum:Money, FiId:Integer, ClientType:Integer, Date:Date, MinValue:Money, MaxValue:Money, SourceDataLayer:Integer):Bool
```

## Процедура: `СтавкаРефинансированияЦБ`

```rsl
СтавкаРефинансированияЦБ (inval:Integer, inval:Date, outval:Doublel [, outval:Doublel]):Bool
```

## Процедура: `КлючеваяСтавкаЦБ`

```rsl
КлючеваяСтавкаЦБ(FIID:Integer, OnDate:Date, CBKeyRateBuff:Record):Integer
```

## Класс: `TgtLog`

```rsl
TgtLog (SeanceID:Integer): Memaddr
```

## Класс: `TGtRecord`

```rsl
TGtRecord (SeanceID:Integer, SeanceLog:Memaddr, ObjectKind:Integer, ObjectName:String, Mode:Integer, Action:Integer, Comment:String, iStatus:Integer): Memaddr
```

## Класс: `TGtRecord`

```rsl
предназначен для создания, просмотра и изменения записей репликации (ЗР) импорта шлюза. Класс может функционировать в трех режимах: · НепосредственнаяВставка – вызовы конструктора и методов класса отражаются в БД в момент вызова. · ВставкаЧерезКеш – данные ЗР аккумулируются в памяти, после чего вставляются в БД путем вызова метода Save. · Корректировка – данные ЗР загружаются из БД и после корректировки  сохраняются в БД с помощью метода Save. Для создания объекта класса необходимо вызвать конструктор TGtRecord() и одну из функций инициализации: · InitByID. · InitByCode. · LoadFromDB. Конструктор класса TGtRecord (SeanceID : Integer, SeanceLog : Memaddr, ObjectKind : Integer, ObjectName : String, Mode : Integer, Action : Integer, Comment : String, iStatus : Integer) содержит следующие параметры: SeanceID – идентификатор сеанса шлюза, в рамках которого создается запись репликации. SeanceLog – ссылка на лог сеанса (TgtLog), в рамках которого создается запись репликации. ObjectKind – вид объекта создаваемой записи репликации. ObjectName – наименование объекта создаваемой записи репликации. Mode – режим, в котором должен работать создаваемый объект. Возможные значения: · НепосредственнаяВставка (по умолчанию). · ВставкаЧерезКеш. Action – действие создаваемой записи репликации. Возможные значения: · Создать (по умолчанию). · Обновить. · Удалить. · Синхронизировать. Comment – комментарий, который необходимо добавить в лог сеанса при создании записи. По умолчанию – пустая строка. iStatus – статус, в котором должна быть создана запись репликации. По умолчанию – "готов к обработке" (идентификатор в таблице dgtsatus_dbt равен 2). Конструктор возвращает ссылку на созданный объект класса TgtRecord.
```

**Пример:**

var 
rec 
= 
TGtRecord(НепосредственнаяВставка, 
SeanceID,
SysLog).

**Методы:**

CheckClientIDByStatus(ClientID:Integer, 
StatusID:Integer 
[, 
ObjectKind:Integer] 
[,
SysDate:Date] [, CheckResult:Bool]):Bool

## Метод: `инициализации`

```rsl
объекта класса TgtRecord. Полный аналог InitByID() за исключением того, что принимает код объекта, код источника и код получателя. Параметры метода: CodeKind – вид кода объекта. ObjectCode – код объекта вида CodeKind, для которого создается запись репликации. SourceCode – код источника получения записи репликации (поле t_code таблицы dgtapp_dbt). TargetCode – код получателя записи репликации (поле t_code таблицы dgtapp_dbt).
```

**Возвращаемое значение:**



## Метод: `инициализации`

```rsl
параметров создаваемой записи репликации (ЗР)
```

с
использованием внутренних идентификаторов объекта ЗР, источника и получателя.
Параметры метода:
ObjectID – идентификатор объекта, для которого создается запись репликации.
SourceID – идентификатор источника записи репликации по таблице dgtapp_dbt.
TargetID – идентификатор получателя по таблице dgtapp_dbt. По умолчанию – "RS-
Bank получатель" (t_applicationid = 11).

**Возвращаемое значение:**



## Метод: `инициализации`

```rsl
объекта класса TgtRecord. Аналог метода InitByCode, только без проверки ЗР в DGTOBJECT_DBT. Параметры метода: CodeKind – вид кода объекта. ObjectCode – код объекта вида CodeKind, для которого создается запись репликации. SourceCode – код источника получения записи репликации (поле t_code таблицы dgtapp_dbt). TargetCode – код получателя записи репликации (поле t_code таблицы dgtapp_dbt).
```

**Возвращаемое значение:**



## Метод: `задает`

```rsl
клиента объекту записи репликации (таблица DGTSTATUS_DBT.T_CLIENTID). Параметры метода: ClientID – идентификатор клиента.
```

**Возвращаемое значение:**



## Метод: `задает`

```rsl
значение параметра вида объекта для записи репликации по идентификатору параметра. Параметры метода: ParamID – идентификатор параметра вида объекта (поле t_koprmid таблицы dgtkoprm_dbt)
```

Value – задаваемое значение параметра.

**Возвращаемое значение:**



## Метод: `задает`

```rsl
статус объекту записи репликации. Параметры метода: StatusID – идентификатор задаваемого статуса (поле t_statusid таблицы dgtstatus_dbt).
```

**Возвращаемое значение:**



## Класс: `TgtUserLog`

```rsl
TgtUserLog (): Memaddr
```

## Класс: `TgtUserLog`

```rsl
реализован для предоставления возможности ведения пользовательского лога сеанса шлюза. Конструктор класса TgtUserLog (SeanceID : Integer) содержит параметр SeanceID – идентификатор сеанса, для которого создается протокол. Конструктор возвращает ссылку на созданный объект пользовательского протокола сеанса.
```

**Методы:**

Add (Text : String) : Bool

## Процедура: `GetObjectCode`

```rsl
GetObjectCode (Application : Integer, ObjectID : Integer, ObjectCode : String [, ObjectKind:Integer]):Integer
```

## Процедура: `GetObjectID`

```rsl
GetObjectID (Application : Integer, ObjectKind : Integer, ObjectCode : String, ObjectID : Integer) : Integer
```

## Процедура: `GetRecordsForSeance`

```rsl
GetRecordsForSeance (rsbTarget:Integer, rsbSource:Integer, seanceId Integer):Object
```

## Процедура: `UpdateRecordStatus`

```rsl
UpdateRecordStatus (recordId:Integer, statusId:Integer [, connection:Object])t
```
