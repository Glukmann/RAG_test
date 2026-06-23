# Banking RSLprc

Введение
Настоящее Руководство содержит описание переменных, классов, процедур и констант
языка интерпретатора RSL, которые используются при создании макромодулей АС RS-
Banking V.6 ИБС RS-Bank V.6 и при написании пользователем собственных макропрограмм.
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
V.6, RS-Retail V.6, RS-Loans V.6, RS-FinMarkets, приведено в соответствующих Руководствах
к этим программным комплексам.
Описание стандартных модулей сгруппировано по отдельным главам, название каждой из
которых соответствует названию соответствующего модуля. Каждая глава Руководства
содержит большое количество примеров, иллюстрирующих использование спецпеременных
при написании программ.
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
В настоящем документе содержатся ссылки на Руководство "Настройки банка АС RS-
Banking V.6" (файл Books/Banking/Banking_BnNastr.pdf).
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
подсистемах "Расчетно-кассовое обслуживание юридических лиц" и "Бухгалтерия банка".
Процедуры

## Процедура: `CashgetString`

```rsl
CashgetString (str:String [, phead:String]):Bool
```

## Процедура: `GetCashSymb`

```rsl
GetCashSymb (cash:Record):TArray
```

## Процедура: `FindCERTforCheck`

```rsl
FindCERTforCheck ([FIID:Integer, ] [Department:Integer, ] [Series:String, ] [NumberFirst:String, ] [NumberLast:String, ] [Account:String, ] [AccountFIID:Integer, ] State:Integer [, buf:Record]):Integer
```

## Процедура: `IS_ChangeCertStatusForCheck`

```rsl
IS_ChangeCertStatusForCheck (Series:String, Number:String, Account:String, AccountFIID:Integer, PrevState:Integer, State:Integer):Integer
```

## Класс: `RsbFMOperation`

```rsl
RsbFMOperation ([OperationID:Integer])
```

## Класс: `RsbFMOprParty`

```rsl
описывает участника операции по легализации. Public-конструктор не предусмотрен. Все объекты класса RsbFMOprParty создаются через класс RsbFMOperation.
```

**Пример:**

var opcontr : RsbFMOperation;
var opcntrpt : RsbFMParty
...
opcntrpt = opcontr.OprParty(_FM_PARTY_PAYER);

**Свойства:**

Account – номер счета участника операции, используемый при проведении операции; тип
String.
BankCode – код банка; тип String:
- БИК – для банков-резидентов.
- S.W.I.F.T. BIC (или non-S.W.I.F.T. BIC) – для банков-нерезидентов.
BankCountry – страна регистрации банка; тип String.
BankID – идентификатор банка, в котором обслуживается участник операции; тип Integer.
BankName – наименование банка; тип String.
BankTerritory – код территории страны регистрации банка; тип String.
BeneficiarySign – признак наличия выгодоприобретателя. Используется только для
участников вида _FM_PARTY_PAYER и _FM_PARTY_RECEIVER. Для участников
всех остальных видов свойство равно пустой строке, и его изменение
игнорируется. Свойство принимает значения соответствующих констант
 и
имеет тип String.
Birthday – дата рождения участника операции, тип Date.
BirthPlace – место рождения участника операции. Для юридического лица изменение
данного свойства игнорируется. Свойство имеет тип String.
CardHolderSign – признак владельца банковской карты. Используется только для
участников вида _FM_PARTY_PAYER и _FM_PARTY_RECEIVER. Для участников
всех остальных видов свойство равно пустой строке, и его изменение
игнорируется. Свойство принимает значения соответствующих констант
 и
имеет тип String.
CardIssuerCode – код эмитента банковской карты; БИК для банков-резидентов; S.W.I.F.T.
BIC (или non-S.W.I.F.T. BIC) для банков-нерезидентов. Свойство имеет тип String.
CardIssuerID – идентификатор эмитента банковской карты. При изменении данного
свойства инициализируются все свойства, относящиеся к эмитенту банковской
карты CardIssuer. Свойство имеет тип Integer.
CardIssuerName – наименование эмитента банковской карты. Свойство имеет тип String.
CodeDocum – код документа, удостоверяющего личность участника операции; тип String.
CorrAccount – номер корреспондирующего счета, используемого при проведении
операции. Свойство имеет тип String.
CorrCode – код корреспондента; тип String.
CorrCountry – код страны регистрации корреспондента; тип String.
CorrID – идентификатор банка-корреспондента; тип Integer.
CorrName – наименование корреспондента; тип String.
CorrTerritory – код территории страны регистрации корреспондента; тип String.
FMPartyKind – вид участника операции. Свойство имеет тип Integer доступно только для
чтения.
ForeignPublicFunctionary – принадлежность к ИДПЛ. Для юридического лица данное
свойство 
игнорируется. 
Свойство 
принимает 
значения 
соответствующих
констант
 и имеет тип String.
INN – ИНН участника операции; тип String. Если передана строка в виде "ИНН/КПП", то
выделение 
ИНН 
производится 
автоматически. 
Для 
участника 
операции-
нерезидента – код иностранной организации (КИО).
IsSimpleIDClient – признак упрощенной идентификации участников операции; тип Bool.
KFMNumber – номер записи из справочника КФМ РФ лиц, причастных к террористической
деятельности, с которой совпадает участник операции. Свойство имеет тип
Integer.
MigratoryCardDateEnd – дата окончания действия миграционной карты. Для юридических
лиц и резидентов изменение данного свойства игнорируется. Свойство имеет тип
Date.
MigratoryCardDateStart – дата начала действия миграционной карты. Для юридических
лиц и резидентов изменение данного свойства игнорируется. Свойство имеет тип
Date.
MigratoryCardNumber – номер миграционной карты. Для юридических лиц и резидентов
изменение данного свойства игнорируется. Свойство имеет тип String.
Name – наименование участника операции; тип String.
OKPO – код ОКПО; тип String.
OperationID –идентификатор записи об операции, подлежащей контролю, участником
которой является объект, описываемым данным классом. Свойство имеет тип
Integer и доступно только для чтения.
OperationType – тип операции; тип Integer.
OrgFormForeign – организационная форма иностранной структуры без образования
юридического лица; тип String.
PaperIssuedDate – дата выдачи документа, удостоверяющего личность; тип Date.
PaperIssuer – наименование органа, который выдал документ, удостоверяющий личность;
тип String.
PaperName – наименование документа, удостоверяющего личность; тип String.
PaperNumber – номер документа, удостоверяющего личность; тип String.
PaperSeries – серия документа, удостоверяющего личность; тип String.
PartyID – идентификатор участника из справочника субъектов. При изменении этого
свойства, все остальные свойства объекта заполняются данными указанного
клиента. При создании объекта инициализируется значением ALLPARTY.
PartySign – признак участника операции. Для операций, у которых не установлены коды
групп 3000 или 7000, изменения свойства игнорируется. Возможные значения
свойства находятся в диапазоне 0 – 3. Свойство имеет тип Integer.
PartyType – тип участника операции. Свойство принимает значения соответствующих
констант
 и имеет тип String.
RegAddrBuilding – адрес регистрации: номер корпуса (строения). Свойство имеет тип
String.
RegAddress – место регистрации (для физического лица – место прописки); тип String.
RegAddrHouse – адрес регистрации: номер дома (владения). Свойство имеет тип String.
RegAddrOffice – адрес регистрации: номер офиса (квартиры). Свойство имеет тип String.
RegAddrOKATO – адрес регистрации: код региона по ОКАТО. Свойство имеет тип String.
RegAddrPlaceName – адрес регистрации: населенный пункт. Свойство имеет тип String.
RegAddrRegion – адрес регистрации: район (регион). Свойство имеет тип String.
RegAddrStreet – адрес регистрации: наименование улицы. Свойство имеет тип String.
RegCountry – код страны места регистрации (для физического лица – места прописки)
участника операции); тип String. Возможно указывать как цифровой, так и
трехбуквенный код страны.
RegDate – дата регистрации участника операции; тип Date.
RegNumber – регистрационный номер участника операции; тип String.
RegTerritory – код территории страны места регистрации (прописки); тип String.
RejectCode – основание отказа от заключения договора банковского счета; тип Integer.
RightVisitDocCode 
- 
код 
документа, 
подтверждающего 
право 
проживания 
для
нерезидента. Возможным значением свойства может быть пустая строка, а также
диапазон "1"-"4". Для юридических лиц и резидентов изменение данного свойства
игнорируется. Свойство имеет тип String.
RightVisitDocDateEnd – дата окончания действия документа, подтверждающего право
проживания для нерезидента. Для юридических лиц и резидентов изменение
данного свойства игнорируется. Свойство имеет тип Date.
RightVisitDocDateStart – дата начала действия документа, подтверждающего право
проживания для нерезидента. Для юридических лиц и резидентов изменение
данного свойства игнорируется. Свойство имеет тип Date.
RightVisitDocNumber – номер документа, подтверждающего право проживания для
нерезидента. Для юридических лиц и резидентов изменение данного свойства
игнорируется. Свойство имеет тип String.
RightVisitDocSeries – серия документа, подтверждающего право проживания для
нерезидента. Для юридических лиц и резидентов изменение данного свойства
игнорируется. Свойство имеет тип String.
StayAddrBuilding – адрес местонахождения: номер корпуса (строения). Свойство имеет
тип String.
StayAddress – место нахождения (пребывания); тип String.
StayAddrHouse – адрес местонахождения: номер дома (владения). Свойство имеет тип
String.
StayAddrOffice – адрес местонахождения: номер офиса (квартиры). Свойство имеет тип
String.
StayAddrOKATO – адрес местонахождения: код региона по ОКАТО. Свойство имеет тип
String.
StayAddrPlaceName – адрес местонахождения: населенный пункт. Свойство имеет тип
String.
StayAddrRegion – адрес местонахождения: район (регион). Свойство имеет тип String.
StayAddrStreet – адрес местонахождения: наименование улицы. Свойство имеет тип
String.
StayCountry – код страны места нахождения (для физического лица – страны
пребывания) участника операции; тип String.
StayTerritory – код территории страны места нахождения (пребывания); тип String.
SuperiorAddrBuilding – адрес регистрации вышестоящей организации: номер корпуса
(строения). Для физического лица и предпринимателя изменение данного
свойства игнорируется. Свойство имеет тип String.
SuperiorAddress – место регистрации вышестоящей организации; тип String.
SuperiorAddrHouse – адрес регистрации вышестоящей организации: номер дома
(владения). Для физического лица и предпринимателя изменение данного
свойства игнорируется. Свойство имеет тип String.
SuperiorAddrOffice – адрес регистрации вышестоящей организации: номер офиса
(квартиры). Для физического лица и предпринимателя изменение данного
свойства игнорируется. Свойство имеет тип String.
SuperiorAddrOKATO – адрес регистрации вышестоящей организации: код региона по
ОКАТО. Для физического лица и предпринимателя изменение данного свойства
игнорируется. Свойство имеет тип String.
SuperiorAddrPlaceName – адрес регистрации вышестоящей организации: населенный
пункт. Для физического лица и предпринимателя изменение данного свойства
игнорируется. Свойство имеет тип String.
SuperiorAddrRegion – адрес регистрации вышестоящей организации: район (регион). Для
физического лица и предпринимателя изменение данного свойства игнорируется.
Свойство имеет тип String.
SuperiorAddrStreet – адрес регистрации вышестоящей организации: наименование
улицы. Для физического лица и предпринимателя изменение данного свойства
игнорируется. Свойство имеет тип String.
SuperioirID – идентификатор вышестоящей организации из справочника субъектов; тип
Integer. При изменении этого свойства инициализируются все свойства,
относящиеся к данным о вышестоящей организации. В конструкторе класса
инициализируется константой UnknownParty.
SuperiorKFMNumber – номер записи из справочника КФМ РФ лиц, причастных к
террористической деятельности, с которой совпадает вышестоящая организация
участника операции. Для физического лица и предпринимателя изменение
данного свойства игнорируется. Свойство имеет тип Integer.
StayCountry – код страны места нахождения (для физического лица – страны
пребывания) участника операции; тип String.
SuperiorName – наименование вышестоящей организации; тип String.
SuperiorTerritory – код территории места регистрации вышестоящей организации; тип
String.
Метод:
CheckCountry ():Integer

## Процедура: `AddDescribe`

```rsl
AddDescribe (Descr:String):Bool
```

## Процедура: `CheckPartyOnTerror`

```rsl
CheckPartyOnTerror (PartyID:Integer [, TerrorBuff:TRecHandler]):Bool
```

## Процедура: `FM_CheckClientAddress`

```rsl
FM_CheckClientAddress(Country:String, Adress:Record, TerroristID:Integer):Bool
```

## Процедура: `FM_CheckPayment`

```rsl
FM_CheckPayment (PaymentID:Integer [, ID_Operation:Integer, ID_Step:Integer] [, HumBenCheckMode:integer]):Integer
```

## Процедура: `FM_CheckTerrorKFM`

```rsl
FM_CheckTerrorKFM (Str:String, Mode:Integer, Terrorist:Integer, Percent:Double):Bool
```

## Процедура: `FM_CheckTerrorOFAC`

```rsl
FM_CheckTerrorOFAC (Str:String, Mode:Integer, Terrorist:Integer, Percent:Double):Bool
```

## Процедура: `FM_CheckTerrorPersn`

```rsl
FM_CheckTerrorPersn(Name:String, Birthday:Date, PaperKind:Integer, PaperSeries:String, PaperNumber:String, PaperIssuedDate:Date, PaperIssuer:String, TerroristID:Integer, Percent:Double):Bool
```

## Процедура: `FM_GetActualPtRiskLevel`

```rsl
FM_GetActualPtRiskLevel(PartyID:Integer, RiskLevelNumber:Integer, RiskLevelName:String, RiskLevelGround:String):Integer
```

## Процедура: `FM_GetDirOrigUnloadFile`

```rsl
FM_GetDirOrigUnloadFile ():String
```

## Процедура: `FM_GetKTU`

```rsl
FM_GetKTU ([Department:Integer]):String
```

## Процедура: `FM_GetMinSumFrag`

```rsl
FM_GetMinSumFrag():Money
```

## Процедура: `FM_GetOfficialPart`

```rsl
FM_GetOfficialPart (FmReqAttach:Record):String
```

## Процедура: `FM_GetReqAttachName`

```rsl
FM_GetReqAttachName (FmReqAttach:Record, [Ext:String]):String
```

## Процедура: `FM_GetReqInfoFocusOnOperations`

```rsl
FM_GetReqInfoFocusOnOperations(PartyID:Integer, [RequestDate:Date], [RequestNumber:String]):Bool
```

## Процедура: `FM_GetSplitSumGroup`

```rsl
FM_GetSplitSumGroup():Integer
```

## Процедура: `FM_IsObjectFrozen`

```rsl
FM_IsObjectFrozen(PartyID:Integer, FrozenObjKind:Integer, FrozenObjNumber:String):Bool
```

## Процедура: `GetOpContrTypeName`

```rsl
GetOpContrTypeName(OprType:Integer):String
```

## Процедура: `MakeDocIDbyAppKind`

```rsl
MakeDocIDbyAppKind (iApplicationKind:Integer, ApplicationKey:String):String
```

## Процедура: `Nf_CalсIncidentState`

```rsl
Nf_CalсIncidentState(IncidentID:Integer, IncidentState:Integer):Integer
```

## Процедура: `ПолучитьДанныеРегистрации`

```rsl
ПолучитьДанныеРегистрации ([RegDate:Date, ] [RegNumber:String, ] PartyID:Integer [, RegDoc:Record]):Bool
```

## Процедура: `ПолучитьКодыОперации`

```rsl
ПолучитьКодыОперации (opcontr:File, Record [, CodeOC:String, TArray] [, CodeUO:String, TArray] [, MainCode:Bool]):Bool
```

## Класс: `RsbLCBigFld`

```rsl
RsbLCBigFld()
```

## Класс: `RsbLCCost`

```rsl
RsbLCCost()
```

## Класс: `RsbLCDemand`

```rsl
RsbLCDemand()
```

## Класс: `RsbLCDpHist`

```rsl
RsbLCDpHist()
```

## Класс: `RsbLCParty`

```rsl
RsbLCParty()
```

## Класс: `RsbLCPay`

```rsl
RsbLCPay()
```

## Класс: `RsbLCPay`

```rsl
описывает список выплат по аккредитиву.
```

**Свойства:**

Notes – примечания выплаты; тип RsbObjNotes. Для использования этого свойства
необходимо импортировать BankInter. Перед вызовом методов объекта
RsbObjNotes неообходимо в родительском сервисе ввода RsbLCPay встать на
нужную выплату (методами First, Next).
Parties – возвращает объект класса RsbLCParty; тип Object.
Size – количество записей в списке; тип Integer.
WlMesLnk – возвращает объект класса RsbWlMesLnk; тип Object. Для использования
этого свойства необходимо импортировать MesInter.

**Методы:**

Delete(LcpayID:Integer):Integer

## Класс: `RsbLCPmLnk`

```rsl
RsbLCPmLnk()
```

## Класс: `RsbLCPmLnk`

```rsl
описывает список связей аккредитива с платежами.
```

**Свойства:**

Size – количество записей в списке; тип Integer.

**Методы:**

AsTArray([stat:Integer]):TArray

## Класс: `RsbLetterOfCredit`

```rsl
RsbLetterOfCredit()
```

## Класс: `RsbLetterOfCredit`

```rsl
описывает документарный аккредитив.
```

**Свойства:**

AddAmountCond – условия покрытия дополнительных сумм; тип String.
AddRlsFormID – дополнительный релиз; тип Integer.
Amount – сумма; тип Money.
AnyBankCond – признак рамбурса в пользу любого банка (dlcreimb_dbt.t_AnyBankCond).
Возможные значения: "X", "". Тип String.
AnyBen – признак рамбурса в пользу любого бенефициара (dlcreimb_dbt.t_AnyBen).
Возможные значения: "X", "". Тип String.
Authorisations – сервис ввода ответов на извещения о расхождениях; тип Object.
BankCond – признак рамбурса в пользу банка (dlcreimb_dbt.t_BankCond). Возможные
значения: "X", "". Тип String.
BankDate – операционный день последней смены статуса аккредитива; тип Date.
BigFields – список больших полей аккредитива. Объект класса RsbLCBigFld. Тип Object.
Branch – ВСП; тип Integer.
Categories – категории аккредитива. Объект типа RsbObjCategories. Для использорвания
этого свойства необходимо импортировать CTInter.
ChAcptRlsFormID – релиз для акцепта изменений; тип Integer.
ChAcptTpSchemID – транспортная схема для акцепта изменений; тип Integer.
Charges – оплата рамбурса (dlcreimb_dbt.t_Charges); тип String.
ChCancel – признак "Отмена аккредитива"; тип String.
ChCharges – расходы; тип String.
ChChargesNarrative – расходы. Пояснение; тип String.
ChDate – дата изменения; тип Date.
ChDetailsFollow – признак "Детали последуют"; тип String.
ChDirect – направление изменений; тип String.
ChHandAcpt – признак приема вручную; тип String.
ChHandTrans – признак передачи вручную; тип String.
ChInitiator – ссылка на участника - инициатора изменений; тип Integer.
ChNumber – номер изменения; тип Integer.
ChOutAddRlsFormID – дополнительный релиз для передачи изменений; тип Integer.
ChOutGenRlsFormID – основной релиз для передачи изменений; тип Integer.
ChOutTpSchemID – транспортная схема для передачи изменений; тип Integer.
ChPurpose – цель изменения; тип String.
ChReceiver – ссылка на участника - получателя изменений;  тип Integer.
ChReceiverInfo – информация получателю; тип String.
CloseDate – дата закрытия; тип Date.
Compensation – возмещение; тип Integer.
ContrID – идентификатор кредитного договора; тип Integer.
Costs – затраты по аккредитиву. Объект класса RsbLCCost.
CountMes – количество сообщений, которые будут сформированы по аккредитиву; тип
Integer.
Cover – покрытие; тип Integer.
CreationDate – дата создания; тип Date.
CreationOper – автор; тип Integer.
CreditAccount – счет для выдачи; тип String.
CreditDate – дата начала действия кредитного договора; тип Date.
CreditDateEnd – дата окончания действия кредитного договора; тип Date.
CreditFIID – валюта кредитного договора; тип Integer.
CreditNum – номер кредитного договора; тип String.
CreditStatus – статус кредитного договора; тип String.
CreditSum – сумма кредитного договора; тип Money.
CreditType – тип выдачи кредитного договора; тип String.
DealAccount – счет привлеченных средств; тип String.
DealDate – дата сделки МБК; тип Date.
DealFIID – валюта счета привлеченных средств в параметрах финансирования
аккредитива (поле t_DealFIID таблицы dlcdoc_dbt), тип Integer.
DealID – идентификатор сделки МБК; тип Integer.
DealNum – номер сделки МБК; тип String.
DeferPayDescr – описание отсроченного платежа; тип String.
Department – филиал; тип Integer.
DeparturePort – порт отправления; тип String.
DestinationPort – порт назначения; тип String.
DirectBill – направление векселя; тип String.
Discrepancys – сервис ввода извещений о расхождениях; тип Object.
DocsPeriod – период представления документов; тип Integer.
DocsPlace – место представления документов; тип String.
DpHist – сервис ввода для истории передачи в филиалы. Объект класса RsbLCDpHist.
EndPlace – конечный пункт; тип String.
ErrMinus – процент отклонения минус; тип Integer.
ErrPlus – процент отклонения плюс; тип Integer.
FIID – валюта; тип Integer.
Flag45 – признак необходимости заполнения поля 45A/B в создаваемом сообщении; тип
String.
Flag46 – признак необходимости заполнения поля 46A/B в создаваемом сообщении; тип
String. Возможные значения:"X" – заполнять поле, "" (пустая строка) – не
заполнять.
Flag47 – признак необходимости заполнения поля 47A/B в создаваемом сообщении; тип
String. Возможные значения:"X" – заполнять поле, "" (пустая строка) – не
заполнять.
Flag49GM – признак необходимости заполнения поля 49G/M в создаваемом сообщении;
тип String . Возможные значения:"X" - заполнять поле, "" (пустая строка) - не
заполнять.
Flag49HN – признак необходимости заполнения поля 49H/N в создаваемом сообщении;
тип String . Возможные значения:"X" - заполнять поле, "" (пустая строка) - не
заполнять.
Form – форма аккредитива; тип String.
GenRlsFormID – основной релиз; тип String.
KindDealMBK – вид сделки МБК; тип Integer.
LCaccount – счет учета; тип String.
LcChangeID – текущее значение идентификатора записи о расходах; тип Integer.
LcdocID – идентификатор аккредитива; тип Integer.
LcDiscrepID – текущее значение ID записи извещение о расхождениях; тип Integer.
LoanAccount – ссудный счет; тип String.
ManualTransferCond – признак ручной передачи аккредитива; тип String.
ManualTransferCond_LCREIMB – признак ручной передачи рамбурсного полномочия.
Возможные значения: "X" – сообщение МБР не формируется, "" (пустая строка) -
требуется выполнить выгрузку рамбурсного полномочия в МБР; тип String.
MisCalc – допуск суммы; тип Integer.
MixPayDescr – описание смешанного платежа; тип String.
Name_LCREIMB – наименование субъекта (dlcreimb_dbt.t_Name); тип String.
NegPayDescr – описание негоциации; тип String.
Notes – примечания аккредитива. Объект типа RsbObjNotes.
Number – номер аккредитива; тип String.
NumMes – номер сообщения, которое формируется по аккредитиву в текущий момент; тип
Integer.
ObligationID – идентификатор СО; тип Integer.
ObligationNum – номер СО; тип String.
ObligationSum – сумма СО; тип Money.
OpenDate – дата открытия аккредитива; тип Date.
OtherCharges – другие расходы (dlcreimb_dbt.t_OtherCharges); тип String.
OverShipping – перегрузки; тип String.
ParentLcdocID – идентификатор исходного аккредитива; тип Integer.
Parties – участники аккредитива. Объект типа RsbLCParty.
PartShipping – частичные отгрузки; тип String.
PayCond – способ оплаты; тип Integer.
PayerAccount – счет списания; тип String.
PayerAccount_LCREIMB – дебетуемый счет (dlcreimb_dbt.t_PayerAccount); тип String.
PayerFIID – валюта счета списания; тип Integer.
PaymLinks – cписок связей аккредитива с платежами. Объект класса RsbLCPmLnk.
Pays – выплаты по аккредитиву. Объект класса RsbLCPay.
ReqDate – дата заявки на кредит; тип Date.
ReqNum – номер заявки на кредит; тип String.
ReqStatus – статус заявки на кредит; тип String.
RlsFormID_LCREIMB – релиз для рамбурсирования (dlcreimb_dbt.t_RlsFormID); тип
Integer.
Rules – правила; тип String.
Rules_LCREIMB – правила для рамбурсирования (dlcreimb_dbt.t_Rules); тип String.
RulesDescr – описание правил; тип String.
ShippingDate – дата окончания отгрузки; тип Date.
ShippingDateCond – условие отгрузки до даты; тип String.
ShippingPeriod – период отгрузки; тип String.
ShippingPlace – место отгрузки; тип String.
State – статус аккредитива; тип Integer.
SysDate – системная дата последней смены статуса аккредитива; тип Date.
SysTime – системное время последнего изменения статуса аккредитива; тип Time.
TpSchemID – транспортная схема; тип Integer.
TpSchemID_LCREIMB 
- 
транспортная 
схема 
для 
рамбурсирования
(dlcreimb_dbt.t_TpSchemID); тип Integer.
UserID – пользователь, который последним менял статус аккредитива; тип Integer.
ValidDate – дата, до которой действует аккредитив; тип Date.
Wlhistor – история смены статусов аккредитива. Объект класса RsbWlHistor. Для
использования свойства необходимо импортировать PaymInter.

**Методы:**

ChangeState(State:Integer):Integer

## Процедура: `DefineRlsFormLCDOC_Add`

```rsl
DefineRlsFormLCDOC_Add(LCDocObj:Object, [TpID:Integer], [TpSchemID:Integer], [FormID:Integer], [RlsFormID:Integer], [ShowRlsPanel:Bool]):Integer
```

## Процедура: `DefineRlsFormLCDOC_Basic`

```rsl
DefineRlsFormLCDOC_Basic(LCDocObj:Object, [TpID:Integer], [TpSchemID:Integer], [FormID:Integer], [RlsFormID:Integer], [ShowRlsPanel:Bool]):Integer
```

## Процедура: `DefineRlsFormLCDOC_Reimburs`

```rsl
DefineRlsFormLCDOC_Reimburs(LCDocObj:Object, [TpID:Integer], [TpSchemID:Integer], [FormID:Integer], [RlsFormID:Integer], [ShowRlsPanel:Bool]):Integer
```

## Процедура: `CheckNewSumLcdoc`

```rsl
CheckNewSumLcdoc(Lcdoc:Trechandler, Lcdoc_ch:Trechandler, [Result:Integer], [Difference:Money]):Integer
```

## Процедура: `GenLcpayForCoverTransfer`

```rsl
GenLcpayForCoverTransfer (LcdocID:Integer, [CoverAmount:Money], [CoverType:Integer], [OnStep:Integer], [LcpayID:Integer]):Integer
```

## Процедура: `GetRlsParams_LcPmNotice`

```rsl
GetRlsParams_LcPmNotice(LcObj:Object, Lcpay:Trechandler, ReiBankID:Integer, BenBankID:Integer, KindMes:Integer, SubKindMes:Integer, PartyID:Integer, Department:Integer):Integer
```

## Процедура: `LCAuthorisationPanel`

```rsl
LCAuthorisationPanel (LCDemandID:Integer, LCDiscrep:Trechandler, BenLCParty:Trechandler, LCDocID:Integer, IsReview:Bool):Integer
```

## Процедура: `LCDocPanel`

```rsl
LCDocPanel(LcObj:Object, [IsReview:Bool], [exitKey:Integer], [IsFromExecuteStep:Bool]):Integer
```

## Процедура: `LCCharges_Scroll`

```rsl
LCCharges_Scroll (isReview:Bool, Mode:Integer, CallType:Integer, PartyID:Integer, CostType:Integer, SaveToDB:Bool, LcdocID:Integer):Integer
```

## Процедура: `LC_LinkPmToLcdocAuto`

```rsl
LC_LinkPmToLcdocAuto (LcObj:Object, [LcpayID:IntegeR], PaymentID:Integer, LinkKind:Integer):Integer
```

## Процедура: `LcpayLinkPaymScrol`

```rsl
LcpayLinkPaymScrol(LCDoc:Object, LcpayIDs:Tarray, Mode:Integer)
```

## Процедура: `ListLCParties`

```rsl
ListLCParties(LcObj:Object, [EnableMultiSelect:Bool], [SelectedLcparties:TArray]):Integer
```

## Процедура: `PnReadAmount`

```rsl
PnReadAmount(LcdocID:Integer, [BlockDate:Bool], Amount:Money, [PostingDate:Date], [key:Integer]):Integer
```

## Процедура: `ReadTextForMesReceiver`

```rsl
ReadTextForMesReceiver(LcdocID:Integer, [NoteKind:Integer], [Text:String]):Bool
```

## Процедура: `ReadRejectReason`

```rsl
ReadRejectReason(LcdocID:Integer, [NoteKind:INTEGER], [Text:String]):Bool
```

## Класс: `RsbAddFld`

```rsl
RsbAddFld()
```

## Класс: `RsbMessage`

```rsl
RsbMessage (MesID:Integer):Object
```

## Класс: `сообщения`

```rsl
МБР, реализован только для работы с механизмом прикладного применения криптографии. Конструктор класса RsbMessage (MesID:Integer)
```

содержит 
параметр 
MesID 
–
идентификатор сообщения.

**Пример:**

var RsMes:RsbMessage = RsbMessage(MesID);

**Свойства:**

AgentID – идентификатор контрагента. Свойство имеет тип Integer и доступно только для
чтения.
DeliveryNotification – признак "Ожидать подтверждения о доставке". Свойство имеет тип
String и доступно только для чтения.
Department – филиал. Свойство имеет тип Integer и доступно только для чтения.
Direct – направление сообщения (начальное, ответное). Свойство имеет тип String и
доступно только для чтения.
Importance – важность (приоритет) сообщения. Свойство имеет тип Integer и доступно
только для чтения.
InsideAbonentID – идентификатор внутреннего абонента. Свойство имеет тип Integer и
доступно только для чтения.
Kind – вид сообщения. Свойство имеет тип Integer и доступно только для чтения.
MesID – уникальный идентификатор сообщения; тип Integer.
OutsideAbonentDate – дата сообщения у нашего абонента. Свойство имеет тип Date и
доступно только для чтения.
OutsideAbonentID – идентификатор внешнего абонента. Свойство имеет тип Integer и
доступно только для чтения.
OutsideAbonentTime – время сообщения у нашего абонента. Свойство имеет тип Time и
доступно только для чтения.
PIB – блок целевой информации; тип String.
RelatedRef – ссылка на сообщение. Свойство имеет тип String и доступно только для
чтения.
RespProcessingDescr – результат обработки сообщения респондентом или транспортной
системой. Свойство имеет тип String и доступно только для чтения.
RlsFormID – идентификатор релиза формы. Свойство имеет тип Integer и доступно
только для чтения.
SessionID – идентификатор сеанса загрузки/выгрузки. Свойство имеет тип Integer и
доступно только для чтения.
TpSchemID – идентификатор транспортной схемы. Свойство имеет тип Integer и доступно
только для чтения.
TRN – референс сообщения. Свойство имеет тип String и доступно только для чтения.

## Класс: `RsbRdPm`

```rsl
RsbRdPmRsbRdPm()
```

## Класс: `RsbWlMesLnk`

```rsl
RsbWlMesLnk(ObjType:Integer, ObjID:Integer):Object
```

## Класс: `списка`

```rsl
связей учетного объекта с сообщениями.
```

**Методы:**

Delete(recWlMesLnk:TRecHandler):Integer

## Процедура: `IsDealReverseMode`

```rsl
IsDealReverseMode ():Bool
```

## Процедура: `IsPmCoverMode`

```rsl
IsPmCoverMode ():Bool
```

## Процедура: `ЗаписатьПоле`

```rsl
ЗаписатьПоле (fieldName:String, value:Object):Bool
```

## Процедура: `УстановитьКонтекстБлока`

```rsl
УстановитьКонтекстБлока ([BlockName:String]):Bool
```

## Процедура: `ОбновитьПоле`

```rsl
ОбновитьПоле (Value:String):Integer
```

## Процедура: `СчитатьПоле`

```rsl
СчитатьПоле (field_name:String, field_value:String [, block_name:String]):Bool
```

## Процедура: `СчитатьУзелМаршрута`

```rsl
СчитатьУзелМаршрута (ObjID:Integer, ObjKind:Integer, RoleBranch:Integer, RoleName:Integer, RTDoc:Record):Bool
```

## Процедура: `УстановитьОбъект`

```rsl
УстановитьОбъект (obj:Object):Bool
```

## Процедура: `GetDlgFlag`

```rsl
GetDlgFlag ():Bool
```

## Процедура: `ПечатьСообщения`

```rsl
ПечатьСообщения (mes:Record, ncopy:Integer, file:String):Bool
```

## Процедура: `ПолучитьДействие`

```rsl
ПолучитьДействие (obj_id:Integer, obj_kind:Integer, type_action:Integer, Date:Date, macro_file:String, macro_proc:String):Bool
```

## Процедура: `ПолучитьПоле`

```rsl
ПолучитьПоле (mes_ID:Integer, field_name:String, field_value:String):Bool
```

## Процедура: `ПолучитьСообщение`

```rsl
ПолучитьСообщение (ObjID:Integer, ObjKind:Integer, Direct:Integer [, Mes:Record] [, Sess:Record] [, SubKindMes:Integer]):Bool
```

## Процедура: `Canonization2`

```rsl
Canonization2 (file:String, buff:String):Bool
```

## Процедура: `ChangeStatusMesOnStep`

```rsl
ChangeStatusMesOnStep (MesID:Integer, NewStatus:Integer):Integer
```

## Процедура: `DefSerialNum_FNS`

```rsl
DefSerialNum_FNS (ObjectID:Integer, ObjectType:Integer, ReqFileName:String, BranchNum:String, Date:Date):Integer
```

## Процедура: `GetAttachedText`

```rsl
GetAttachedTextGetAttachedText (ImageID:Integer):String
```

## Процедура: `GetSerialNum_FNS`

```rsl
GetSerialNum_FNS():Integer
```

## Процедура: `UFBSSignature`

```rsl
UFBSSignature (typeAction:Integer, context:String, file:String, signature:String):Bool
```

## Процедура: `WldChangeStatus`

```rsl
WldChangeStatus (ObjID:Integer, ObjKind:Integer, Status:Integer):Integer
```

## Процедура: `CalculatePSBCKivtSum`

```rsl
CalculatePSBCKivtSum (BCDocID:Integer):Moneyl
```

## Процедура: `PossiblePSBCPayCurrency`

```rsl
PossiblePSBCPayCurrency (BCDocID:Integer):Bool
```

## Процедура: `PSBC_AddMessageToLog`

```rsl
PSBC_AddMessageToLog (mes :String)
```

## Класс: `PSRepMap`

```rsl
PSRepMap ()
```

## Класс: `словаря`

```rsl
переменных RSL по ключу любого встроенного типа.
```

**Свойства:**

Size – размер словаря (количество элементов в словаре). Свойство имеет тип Integer и
доступно только для чтения.

**Методы:**

Add (key:Variant, value:Variant):Bool

## Метод: `позиционирования`

```rsl
на первом элементе словаря, возвращает TRUE в случае успешного выполнения. Key ():Variant
```

## Метод: `позиционирования`

```rsl
на последнем элементе словаря, возвращает TRUE в случае успешного выполнения. Next ():Bool
```

## Метод: `позиционирования`

```rsl
на следующем элементе словаря, возвращает TRUE в случае успешного выполнения. Prev ():Bool
```

## Метод: `позиционирования`

```rsl
на предыдущем элементе словаря, возвращает TRUE в случае успешного выполнения. Remove ([key:Variant]):Bool
```

## Класс: `RsbBCPayment`

```rsl
платежа по первичному документу "Поручение на покупку/продажу/конверсию валюты". Наследник класса RsbPayment (см. Руководство программиста "Интерфейсы языка RSL для взаимодействия с ИБС RS-Bank V.6. Часть 3").
```

## Класс: `RsbBuyCurrencyOrder`

```rsl
RsbBuyCurrencyOrder ([DocumentID:Integer]):Object
```

## Класс: `RsbCheckIss`

```rsl
RsbCheckIss ([OrderID:Integer]):Object
```

## Класс: `RsbPreAccept`

```rsl
RsbPreAccept()
```

## Класс: `RsbReqOpenAcc`

```rsl
RsbReqOpenAcc ([RequestID:Integer]):Object
```

## Класс: `RsbReqChangeAcc`

```rsl
RsbReqChangeAcc ([RequestID:Integer]):Object
```

## Класс: `RsbReqCloseAcc`

```rsl
RsbReqCloseAcc ([RequestID:Integer]):Object
```

## Класс: `RsbReqCloseAccum`

```rsl
RsbReqCloseAccum ([RequestID:Integer]):Object
```

## Класс: `RsbReqOpenAccum`

```rsl
RsbReqOpenAccum ([RequestID:Integer]):Object
```

## Класс: `RsbSummaryMemorialOrder`

```rsl
RsbSummaryMemorialOrder ()
```

## Процедура: `AnnulMes`

```rsl
AnnulMes (MesID:Integer):Integer
```

## Процедура: `AskDemAccept`

```rsl
AskDemAccept (Sum:Money, DenialAmount:Money, DenialGround:String):Integer
```

## Процедура: `CheckSertif`

```rsl
CheckSertif (Series:String, NumberFirst:String, NumberLast:String, Account:String, FormKind:Integer):Integer
```

## Процедура: `CreateReqChngAOperation`

```rsl
CreateReqChngAOperation (RequestID:Integer):Integer
```

## Процедура: `CreateReqClosAOperation`

```rsl
CreateReqClosAOperation (RequestID:Integer):Integer
```

## Процедура: `CreateReqOpenAOperation`

```rsl
CreateReqOpenAOperation (RequestID:Integer):Integer
```

## Процедура: `DefineCoefficientDepos`

```rsl
DefineCoefficientDepos (Code:Integer [, Val:Double]):Bool
```

## Процедура: `FindInverFlag`

```rsl
FindInverFlag ([record ord:Record]):Integer
```

## Процедура: `Fns_AccLnkListRegDecProcess_v4_00`

```rsl
Fns_AccLnkListRegDecProcess_v4_00 (ClientList:TArray, RecipientID:Integer, Date:Date, ClientName:String, ClientINN:String, AccLnkList:Object, RegDecType:Integer):Integer
```

## Процедура: `Fns_GetAccRestsInfo_v4_00`

```rsl
Fns_GetAccRestsInfo_v4_00 (AccLnkList:Object, LnkObjectType:Integer, LnkTypeInfo:Integer, ClientList:TArray):Integer
```

## Процедура: `GetChoiceIWPorREJECT`

```rsl
GetChoiceIWPorREJECT (Account:String, FIID:Integer):Integer
```

## Процедура: `GetChoiceK2orREJECT`

```rsl
GetChoiceIWPorREJECT (Account:String, FIID:Integer):Integer
```

## Процедура: `GetInd2AccDocSum`

```rsl
GetInd2AccDocSum ([Account:String, ] [Summa:Moneyl]):Integer
```

## Процедура: `GetKindRegOrgan`

```rsl
GetKindRegOrgan ():Integer
```

## Процедура: `GetOrderSum`

```rsl
GetOrderSum ([DocKind:Integer] [, DocID:Integer] [, Purpose:Integer] [, Summa:Moneyl]):Integer
```

## Процедура: `GetSrvPayByPayOrderID`

```rsl
GetSrvPayByPayOrderID (OrderID:Integer, SvSrvPay:Variant, SvAcc:Variant):Bool
```

## Процедура: `IsLnkAccountPrcError`

```rsl
IsLnkAccountPrcError (wlacclnk:File|Record|Tbfile|Trechandler, InfoType:Integer): Bool
```

## Процедура: `IsLnkAccountPrcError_v4_00`

```rsl
IsLnkAccountPrcError_v4_00 (wlacclnk:Trechandler):Bool
```

## Процедура: `IsReservPayOrder`

```rsl
IsReservPayOrder ([ord:Record]):Integer
```

## Процедура: `IsUrgentPayOrder`

```rsl
IsUrgentPayOrder ([ord:Record]):Integer
```

## Процедура: `PS_CancelOrder`

```rsl
PS_CancelOrder (PaymentID:Integer, DocKind:Integer, [Reason:String]):Integer
```

## Процедура: `PS_PayorderPanel`

```rsl
PS_PayorderPanel (PaymentObj:Object, FieldNum:Integer):Bool
```

## Процедура: `PS_ShowPsPayOrder`

```rsl
PS_ShowPsPayOrder (PaymentID:Integer):Bool
```

## Процедура: `PS_ShowRequestPayOrder`

```rsl
PS_ShowRequestPayOrder (PaymentID:Integer):Bool
```

## Процедура: `PSAccLnkListRegDecProcess`

```rsl
PSAccLnkListRegDecProcess(ClientList:TArray, RecipientID:Integer, Date:Date, ClientName:String, AccLnkList:Object, ClientINN:String, RegDecType:Integer):Integer
```

## Процедура: `PSFNSCheckClientData`

```rsl
PSFNSCheckClientData (ClientINN:String, ClientKPP:String, ClientName:String, ClientAddress:String, ClientID:Integer, [ClientType:Integer], [IsMassMode:Bool]):Integer
```

## Процедура: `PSFNSCheckClientData_v4_00`

```rsl
PSFNSCheckClientData_v4_00 (Raclient:Trechandler, [ClientID:Integer], [ErrList:Object], [ClientList:TArray], [NewName:String], [IsMassMode:Bool], [ClientsByINN:Bool]):Integer
```

## Процедура: `PSRequestCashSeriesAndNumber`

```rsl
PSRequestCashSeriesAndNumber(Series:String, Number:String):Number
```

## Процедура: `ReqAcc_SetAccType`

```rsl
ReqAcc_SetAccType (AccountFIID:Integer, Account:String, Type:String, IsBackoutType:Integer):Integer
```

## Процедура: `ReqAccPrintMessage`

```rsl
ReqAccPrintMessage(RequestID:Integer, ObjType:Integer [CopyCount:Integer]):Integer
```

## Процедура: `ReqChangePrintMessage`

```rsl
ReqChangePrintMessage (RequestID:Integer, NewAccountFIID:Integer, NewAccount:String):Integer
```

## Процедура: `RunScMacroForChangeDoc`

```rsl
RunScMacroForChangeDoc ():Integer
```

## Процедура: `SetAccNoteNumber`

```rsl
SetAccNoteNumber (Account:String, Series:String, Number:String):Integer
```

## Процедура: `SetKindRegOrgan`

```rsl
SetKindRegOrgan (new_KindRegOrgan:Integer):Integer
```

## Процедура: `ShowFV`

```rsl
ShowFV(FilePath:String)
```

## Процедура: `GetPmSumToKvit`

```rsl
GetPmSumToKvit (PaymentID:Integer, Is_In:Integer, Sum:Money):Bool
```

## Процедура: `GetPmUnkvitSum`

```rsl
GetPmUnkvitSum (PaymentID:Integer, Is_In:Integer, Sum:Money):Bool
```

## Процедура: `IsAccOk`

```rsl
IsAccOk ():Bool
```

## Процедура: `IsForcePlaceInUnknown`

```rsl
IsForcePlaceInUnknown ():Bool
```

## Процедура: `IsPmKvitFull`

```rsl
IsPmKvitFull ():Bool
```

## Процедура: `ListMultyPayment`

```rsl
ListMultyPayment ([PaymentID:Integer] [, Number:String] [, FIID:Integer] [, BegDate:Date] [, EndDate:Date] [, SumBeg:Money] [, SumEnd:Money] [, Purpose:Integer] [, TpID:Integer] [, FormID:Integer] [, RlsID:Integer]):Integer
```

## Процедура: `ДобавитьПримечаниеПлатежа`

```rsl
ДобавитьПримечаниеПлатежа (notetext:Record, payment_id:Integer):Bool
```

## Процедура: `добавления`

```rsl
примечания для платежа.
```

**Параметры:**

notetext – буфер примечания платежа (dnotetext_dbt).
payment_id – идентификатор платежа.

**Возвращаемое значение:**



## Процедура: `ПолучитьПервоеПримечаниеПлатежа`

```rsl
ПолучитьПервоеПримечаниеПлатежа (pmpaym:Record, notetext:Record):Bool
```

## Процедура: `ПолучитьПервуюКатегориюПлатежа`

```rsl
ПолучитьПервуюКатегориюПлатежа (pmpaym:Record, objatcor:Record):Bool
```

## Процедура: `ПолучитьРасходыРеспондента`

```rsl
ПолучитьРасходыРеспондента (payment_id:Integer, pmsleeve:Record [, party_id:Integer]):Bool
```

## Процедура: `ПолучитьСледующееПримечаниеПлатежа`

```rsl
ПолучитьСледующееПримечаниеПлатежа (pmpaym:Record, notetext:Record):Bool
```

## Процедура: `ПолучитьСледующуюКатегориюПлатежа`

```rsl
ПолучитьСледующуюКатегориюПлатежа (pmpaym:Record, objatcor:Record):Bool
```

## Класс: `RsbDpBilLim`

```rsl
RsbDpBilLimсм
```

## Класс: `RsbDpLiqSet`

```rsl
RsbDpLiqSet()
```

## Класс: `RsbRAClient`

```rsl
RsbRAClient ()
```

## Класс: `RsbRqGround`

```rsl
RsbRqGround ()
```

## Класс: `RsbRqMesSBP`

```rsl
RsbRqMesSBP()
```

## Класс: `RsbWlAccLnk`

```rsl
RsbWlAccLnk(ID:Integer, ObjectType:Integer):Object
```

## Класс: `RsbWlError`

```rsl
RsbWlError()
```

## Класс: `списка`

```rsl
ошибок обработки сообщения.
```

**Свойства:**

Size – размер списка ошибок обработки сообщения; тип Integer.

**Пример:**

var ErrList = RsbWlError(123);
msgbox("Для квитанции с ID 123 введено ", ErrList.Size(), "
ошибок обработки");

**Методы:**

Delete(buf:TRecHandler):Integer

## Класс: `RsbWlNDLnk`

```rsl
RsbWlNDLnk()
```

## Класс: `списка`

```rsl
филиалов уведомления в ФНС.
```

**Свойства:**

Size – размер списка связанных филиалов; тип Integer.

**Пример:**

var DepList = RsbWlNDLnk(1);
msgbox("В списке уведомления ", DepList.Size, " филиалов");

**Методы:**

Delete(NDLnkID:Integer):Integer

## Класс: `RsbWlRequest`

```rsl
RsbWlRequest()
```

## Процедура: `ПолучитьВидСтраницыВыписки`

```rsl
ПолучитьВидСтраницыВыписки (type_page:Integer):Bool
```

## Процедура: `ПолучитьДокументВыписки`

```rsl
ПолучитьДокументВыписки (wlconf:Record):Bool
```

## Процедура: `ПрочитатьТекстЗапроса_Ответа`

```rsl
ПрочитатьТекстЗапроса_Ответа (wlreq:Record, narrative:String [, description:String] [, copy_fields:String]):Bool
```

## Процедура: `ПрочитатьТекстИнфСообщения`

```rsl
ПрочитатьТекстИнфСообщения ( wlinfo:Record):Bool
```

## Процедура: `СоздатьТелеграммуПоПлатежу`

```rsl
СоздатьТелеграммуПоПлатежу (PaymentID:Integer):Integer
```

## Процедура: `СчитатьСвязьЗапросаСУчетнымОбъектом`

```rsl
СчитатьСвязьЗапросаСУчетнымОбъектом (ReqID:Integer [, ObjKind:Integer] [, ObjID:Integer]):Bool
```

## Процедура: `УстановитьФильтрДокументовВыписки`

```rsl
УстановитьФильтрДокументовВыписки (HeadID:Integer):Bool
```

## Процедура: `CreateInfo`

```rsl
CreateInfo (wlinfo:Record, Narrative:String, [RslFormID:Integer] [, TpShemID:Integer] [, ConnectTo_Oper:Bool] [, ID_Operation:Integer] [, ID_Step:Integer]):Integer
```

## Процедура: `CreateQuery`

```rsl
CreateQuery (wlreq:Record [, Narrative:String] [, Description:String] [, RlsFormID:Integer] [, TpShemID:Integer] [, ConnectToOper:Bool] [, ID_Operation:Integer] [, StepID:Integer], TpID:Integer [, ObjID:Integer] [, ObjKind:Integer] [, ObjDirect:String]):Integer
```

## Процедура: `WldDefineRslForm`

```rsl
WldDefineRslForm (ObjKind:Integer, PartyID:Integer, KindMes:Integer, TpID:Integer, TpShemID:Integer, RslformID:Integer):Integer
```

## Процедура: `ВставитьДокументВыписки`

```rsl
ВставитьДокументВыписки (wlconf:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись документа выписки во временную таблицу. Процедура может быть вызвана только после вызова процедуры ВставитьЗаголовокВыписки .
```

**Параметры:**

wlconf – указатель на буфер документа выписки (таблица dwlconf_dbt).
Возвращаемые значения:

## Процедура: `ВставитьДокументУведомления`

```rsl
ВставитьДокументУведомления (wldocnot:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись документа уведомления во временную таблицу. Процедура может быть вызвана только после вызова процедуры ВставитьЗаголовокУведомления .
```

**Параметры:**

wldocconf – указатель на буфер документа уведомления (таблица dwlconf_dbt).
Возвращаемые значения:

## Процедура: `ВставитьЗаголовокВыписки`

```rsl
ВставитьЗаголовокВыписки (wlhead:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись заголовка выписки во временную таблицу.
```

**Параметры:**

wlhead – указатель на буфер заголовка выписки (таблица dwlhead_dbt).
Возвращаемые значения:

## Процедура: `ВставитьЗаголовокУведомления`

```rsl
ВставитьЗаголовокУведомления (wlnot:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись заголовка уведомления во временную таблицу.
```

**Параметры:**

wlnot – указатель на буфер заголовка уведомления (таблица dwlhead_dbt).
Возвращаемые значения:

## Процедура: `ВставитьЗапрос`

```rsl
ВставитьЗапрос (wlreq:Record [, narrative:String] [, description:String] [, copy_fields:String]):Bool
```

## Процедура: `вставляет`

```rsl
запись запроса во временную таблицу.
```

**Параметры:**

wlreq – указатель на буфер запроса (таблица dwlreq_dbt).
narrative – текст запроса.
description – описательная информация.
copy_fields – копия обязательных полей.
Возвращаемые значения:

## Процедура: `ВставитьЗапросНаПолучениеВыписки`

```rsl
ВставитьЗапросНаПолучениеВыписки (wlreq:Record [, narrative:String] [, description:String] [, copy_fields:String]):Bool
```

## Процедура: `ВставитьИзменениеПретензии`

```rsl
ВставитьИзменениеПретензии(acclmcng:Record [, AcclmcngID:Integer]):Integer
```

## Процедура: `вставляет`

```rsl
документ, изменяющий претензию к лицевому счету.
```

**Параметры:**

acclmcng – заполненный буфер документа (таблица acclmcng.dbt).
AcclmcngID – идентификатор созданного документа.

**Возвращаемое значение:**



## Процедура: `ВставитьИнфСообщение`

```rsl
ВставитьИнфСообщение (wlinfo:Record, text:String):Bool
```

## Процедура: `вставляет`

```rsl
запись об информационном сообщении во временную таблицу.
```

**Параметры:**

wlinfo – указатель на буфер записи об информационном сообщении (таблица dwlinfo_dbt).
text – текст информационного сообщения.
Возвращаемые значения:

## Процедура: `ВставитьОстаток`

```rsl
ВставитьОстаток (wlrest:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись о доступном остатке на корреспондентском счете на заданную дату валютирования.
```

**Параметры:**

wlrest – буфер записи о доступных средствах (таблица dwlrest_dbt).
Возвращаемые значения:

## Процедура: `ВставитьОтвет`

```rsl
ВставитьОтвет (wlreq:Record [, narrative:String] [, description:String] [, copy_fields:String]):Bool
```

## Процедура: `вставляет`

```rsl
запись ответа во временную таблицу dwlreq_dbt.
```

**Параметры:**

wlans – указатель на буфер ответа (таблица dwlreq_dbt).
narrative – текст ответа на запрос.
description – описательная информация.
copy_fields – копия обязательных полей исходного сообщения.
Возвращаемые значения:

## Процедура: `ВставитьОшибкуОбработкиСообщения`

```rsl
ВставитьОшибкуОбработкиСообщения(wlerror:Record):Bool
```

## Процедура: `ВставитьПлатеж`

```rsl
ВставитьПлатеж (payment:Record, debet:Record, credit:Record [, rmprop:Record] [, Credit_Flag:Integer] [, pmdemand:Record] [, pmakkr:Record] [, AddDocs:String] [, curtr:Record], CheckTerrorOnUpdate:Bool [, pmkz:Record]):Bool
```

## Процедура: `вставляет`

```rsl
запись внешнего платежа во временную таблицу. При использовании этой процедуры обязательно должно быть указано свойство дебета или свойств кредита (либо оба свойства).
```

**Параметры:**

pmpaym – указатель на буфер платежа (таблица dpmpaym_dbt).
debet – указатель на буфер дебетовых свойств платежа (таблица dpmprop_dbt). Если
дебетовые свойства не заданы, то значение параметра принимается равным 0.
credit – указатель на буфер кредитовых свойств платежа (таблица dpmprop_dbt). Если
кредитовые свойства не заданы, то значение параметра принимается равным 0.
rmprop – указатель на буфер рублевых свойств платежа (таблица dpmrmprop_dbt). 
Credit_Flag – тип внешнего платежа. Возможные значения параметра:
- 0 – дебетовый.
- 1 – кредитовый.
По умолчанию, если значение параметра не задано, тип платежа определяется
как кредитовый.
pmdemand – запись таблицы pmdemand.dbt.
pmakkr – запись платежа pmakkr.dbt.
AddDocs – приложение к аккредитиву.
curtr – запись платежа pmcurtr.dbt.
CheckTerrorOnUpdate – признак проверки причастности платежа к финансированию
терроризма. Возможные значения параметра:
- TRUE – проверять платеж на причастность к финансированию терроризма.
- FALSE – не проверять.
pmkz – запись платежа pmkz.dbt.
Возвращаемые значения:

## Процедура: `ВставитьПодпись`

```rsl
ВставитьПодпись (CryptoSysID:Integer, Sign:String):Bool
```

## Процедура: `вставляет`

```rsl
внешнюю подпись платежа. Роль подписи задается в качестве значения параметра РОЛЬ ЭЦП ОТВ ПЛАТЕЖЕЙ. Процедура используется только после процедуры ВставитьПлатеж .
```

**Параметры:**

CryptoSysID – идентификатор криптосистемы (поле t_cryptosysid таблицы dsgnsys_dbt).
Sign – подпись.
Возвращаемые значения:

## Процедура: `ВставитьПодтверждение`

```rsl
ВставитьПодтверждение (wlconf:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись о подтверждении во временную таблицу.
```

**Параметры:**

wlconf – указатель на буфер записи о подтверждении (таблица dwlconf_dbt).
Возвращаемые значения:

## Процедура: `ВставитьПодтверждениеБанкаФНС`

```rsl
ВставитьПодтверждениеБанкаФНС([mes:TBfile, TRecHandler] [, ErrCode:Integer] [, ErrDescription:String] [, ErrList:Object] [, FileName:String] [, OriginatorID:Integer] [. OriginatorCodeKind:Integer] [, OriginatorCode:String] [OriginatorName:String] [, RecipientID:Integer] [, RecipientCodeKind:Integer] [RecipientCode:String] [, RecipientName:String] [, ResultID:Integer], [Type:Integer], [ResultID:Integer], [ID_Operation:Integer], [ID_Step:Integer]):Bool
```

## Процедура: `ВставитьПодтверждениеМБК`

```rsl
ВставитьПодтверждениеМБК (wldlmm:Record):Bool
```

## Процедура: `вставляет`

```rsl
запись о подтверждении сделки межбанковского кредитования (МБК) во временную таблицу.
```

**Параметры:**

wldlmm – указатель 
на 
буфер 
записи 
о 
подтверждении 
сделки 
МБК 
(таблица
dwldlmm_dbt).
Возвращаемые значения:

## Процедура: `ВставитьПодтверждениеОДоставке`

```rsl
ВставитьПодтверждениеОДоставке (mes_id:Integer, NoChangeState:Bool [, DeliveryDate:Date] [, Description:String] [, CreateKvt:Bool]):Bool
```

## Процедура: `ВставитьПодтверждениеОДоставкеМНС`

```rsl
ВставитьПодтверждениеОДоставкеМНС (MesID:Integer):Bool
```

## Процедура: `ВставитьПретензию`

```rsl
ВставитьПретензию(acclaim:Record, acclaimstate:Record [, AcclaimID:Integer]):Integer
```

## Процедура: `вставляет`

```rsl
претензию к лицевому счету.
```

**Параметры:**

acclaim – заполненный буфер таблицы acclaim.dbt.
acclaimstate – статус создаваемой претензии (буфер таблицы acclaimstate.dbt).
AcclaimID – идентификатор созданной претензии.

**Возвращаемое значение:**



## Процедура: `ВставитьПримечание`

```rsl
ВставитьПримечание (note_kind:Integer, note_text:Integer, String):Bool
```

## Процедура: `ВставитьРасходыОтправителя`

```rsl
ВставитьРасходыОтправителя (fiid:Integer, String, amount:Moneyl [, party_id:Integer]):Bool
```

## Процедура: `вставляет`

```rsl
запись о расходах отправителя на заданную сумму (в таблицу dpmsleeve_dbt). Данная процедура используется только после процедуры ВставитьПлатеж.
```

**Параметры:**

fiid – идентификатор финансового инструмента (тип Integer) или код валюты расходов
(тип String).
amount – сумма расходов; параметр Money или MoneyL.
party_id – идентификатор субъекта, который несет расходы, возникающие в процессе
перевода денежных средств в соответствии с платежным документом.
Возвращаемые значения:

## Процедура: `ВставитьРешениеРегистрационногоОргана`

```rsl
ВставитьРешениеРегистрационногоОргана(regdec:Record [, DecisionID:Integer]):Integer
```

## Процедура: `ВставитьСвязанноеПоручениеДляРешенияФНС`

```rsl
ВставитьСвязанноеПоручениеДляРешенияФНС(wlrdpm: Record, Trechandler):Bool
```

## Процедура: `ВставитьТребованиеФНС`

```rsl
ВставитьТребованиеФНС(regdec:Record, [DecisionID:Integer]):Integer
```

## Процедура: `ОбновитьЗаголовокВыписки`

```rsl
ОбновитьЗаголовокВыписки (wlhead:Record):Bool
```

## Процедура: `ОбновитьЗаголовокУведомления`

```rsl
ОбновитьЗаголовокУведомления (wlhead:Record):Bool
```

## Процедура: `ОбновитьИнфСообщение`

```rsl
ОбновитьИнфСообщение (wlinfo:Record, Narrative:String):Bool
```

## Процедура: `ОбновитьОтвет`

```rsl
ОбновитьОтвет (wlreq:Record [, Narrative:String] [, Description:String] [, CopyFields:String]):Bool
```

## Процедура: `ОшибкаЛогическогоКонтроляСообщения`

```rsl
ОшибкаЛогическогоКонтроляСообщения (MesID:Integer ErrCode:Integer, ErrDescr:String [, State:Integer] [, AllowDefectClosed:Bool] [, ResultID:Integer] [, CreateMesLnk:Integer], CreateDate:Date, CreateTime:Time):Bool
```

## Процедура: `ПолучитьВыпискуПоИдентификатору`

```rsl
ПолучитьВыпискуПоИдентификатору(PartAggregateID:String, wlhead:Record):Bool
```

## Процедура: `ПоместитьВНезавершенные`

```rsl
ПоместитьВНезавершенные (wlpm_id:Integer): Bool
```

## Процедура: `ПривязатьОбъектДепоКСообщению`

```rsl
ПривязатьОбъектДепоКСообщению (msgInfID:Integer):Bool
```

## Процедура: `СквитоватьПлатеж`

```rsl
СквитоватьПлатеж (wlpm_id:Integer):Bool
```

## Процедура: `вставляет`

```rsl
запись о новой связи квитовки между указанным платежом и текущим подтверждением во временную таблицу dwlkvtlnk_tmp (MDB-файл).
```

## Процедура: `вызывается`

```rsl
из макроса генерации подтверждения (выписки) по входящему сообщению после вызова процедуры ВставитьПодтверждение или ВставитьДокументВыписки . Процедуру СквитоватьПлатеж для одного подтверждения можно вызывать несколько раз.
```

**Параметры:**

wlpm_id – идентификатор записи (dwlpm_dbt).

**Возвращаемое значение:**



## Процедура: `ImportFileDir`

```rsl
ImportFileDir (pathDir:String, TpID:Integer [, RaceNumber:Integer]):Bool
```

## Процедура: `ОбновитьЗапись`

```rsl
ОбновитьЗапись (message:Record):Bool
```

## Процедура: `ПерейтиВНачалоФайла`

```rsl
ПерейтиВНачалоФайла ():Bool
```

## Процедура: `СоздатьЗапись`

```rsl
СоздатьЗапись (message:Record):Bool
```

## Процедура: `СчитатьБлок`

```rsl
СчитатьБлок (length:Integer):Integer
```

## Процедура: `СчитатьСтроку`

```rsl
СчитатьСтроку (length:Integer):Integer
```

## Процедура: `ТекущаяСтрока`

```rsl
ТекущаяСтрока ():Integer
```

## Процедура: `УстановитьНомерРейса`

```rsl
УстановитьНомерРейса (NumberRace:Integer):Bool
```

## Процедура: `ПечатьСообщенийСеанса`

```rsl
ПечатьСообщенийСеанса (wlsess:Record, ncopy:Integer):Bool
```

## Процедура: `ПечатьУчетныхОбъектовСеанса`

```rsl
ПечатьУчетныхОбъектовСеанса (SessID:Integer):Bool
```

## Процедура: `ПолучитьКопиюФайлаСеансаСвязи`

```rsl
ПолучитьКопиюФайлаСеансаСвязи (SessID:Integer)
```

## Процедура: `WldCheckMesDouble`

```rsl
WldCheckMesDouble(wlmes:Record [, DoubleMesID:Integer] [, DoubleStateName: String]):Bool
```

## Процедура: `ЗаписатьБлок`

```rsl
ЗаписатьБлок (строка:String):Bool
```

## Процедура: `ЗаписатьСтроку`

```rsl
ЗаписатьСтроку (str:String):Bool
```

## Процедура: `СчитатьЗапись`

```rsl
СчитатьЗапись (wlmes:Record [, err:Integer] [, ignore_prev_mes:Bool]):Bool
```

## Процедура: `ТекущийРазмерФайла`

```rsl
ТекущийРазмерФайла ()
```

## Процедура: `AddErrExpRepInfo`

```rsl
AddErrExpRepInfoAddErrExpRepInfo(MessageID:Integer, [SeesionID:Integer], Error:String):Bool
```

## Процедура: `Bnk_decodeXML`

```rsl
Bnk_decodeXML(xmlString:String, [tagString:String]):Integer
```

## Процедура: `ConnectMessageToObject`

```rsl
ConnectMessageToObject(MesID:Integer, Direct:String, ObjectType:Integer, ObjectID:Integer):Integer
```

## Процедура: `FindCORSCHEMForReqLiq`

```rsl
FindCORSCHEMForReqLiq(Department:Integer, corschem:Record):Bool
```

## Процедура: `FnsScrolRgdOrders`

```rsl
FnsScrolRgdOrders(Wlregdec:Record, Trechandler, [Mode:Integer], [RdpmList:Object])
```

## Процедура: `GetExchangeType`

```rsl
GetExchangeType(Department:Integer):String
```

## Процедура: `GetGGPaymentRefer`

```rsl
GetGGPaymentRefer(RefID:Integer, Refer:String, ObjKind:Integer, ObjID:Integer):Integer
```

## Процедура: `GetLastProcessedGGPIRequest`

```rsl
GetLastProcessedGGPIRequest(ObjectID:Integer, ObjectType:Integer):Integer
```

## Процедура: `GetLastUnprocessedGGPIRequest`

```rsl
GetLastUnprocessedGGPIRequest(ObjectID:Integer, ObjectType:Integer):Integer
```

## Процедура: `GetLastUnprocGGPIRequestWOI`

```rsl
GetLastUnprocGGPIRequestWOI(ObjectID:Integer, ObjectType:Integer, InsertedID:Integer):Integer
```

## Процедура: `GetPreviousGGPIRequest`

```rsl
GetPreviousGGPIRequest(ObjectID:Integer, ObjectType:Integer):Integer
```

## Процедура: `GetRecipientName`

```rsl
GetRecipientName(Department:Integer):String
```

## Процедура: `GetSenderIdentifier`

```rsl
GetSenderIdentifier(Department:Integer):String
```

## Процедура: `GetStatus`

```rsl
GetStatus(Department:Integer):String
```

## Процедура: `GetTypeCode`

```rsl
GetTypeCode(Department:Integer):String
```

## Процедура: `GetFNSInfMassProcessWarning`

```rsl
GetFNSInfMassProcessWarning():String
```

## Процедура: `GGPICheckGisGmpProp`

```rsl
GGPICheckGisGmpProp(PaymentID:Integer, NoteText:String):Integer
```

## Процедура: `GisGmpMsgParmsDefinition`

```rsl
GisGmpMsgParmsDefinition(ggcp:Integer, gisgmpmsg:Array, PaymDepartment:Integer):Integer
```

## Процедура: `GISGMP_PaymentDate`

```rsl
GISGMP_PaymentDate(ObjKind:Integer, ObjID:Integer, [PaymentDate:Date], [PaymentTime:Time]):Integer
```

## Процедура: `GISGMP_CancelTransferPay`

```rsl
GISGMP_CancelTransferPay(PaymentID:Integer, OperationID:Integer, StepID:INTEGER, [ErrMessage:String]):Integer
```

## Процедура: `InsertGGPIPmSend`

```rsl
InsertGGPIPmSend(ObjectID:Integer, ObjectType:Integer, Action:Integer, Ground:String, ErrMessage:String, pStat:Integer):Integer
```

## Процедура: `InsertGGRepData`

```rsl
InsertGGRepData(ObjectID:Integer, ObjectType:Integer, Department:Integer, Branch:Integer, MesID:Integer, Message:String):Integer
```

## Процедура: `ListMessages`

```rsl
ListMessagesListMessages(Direct:String, MesKind:Integer, OnlySend:Bool, OutsideAbonentID:Integer, MesDate:Date, Reference:String, TpID:Integer, FormID:Integer, RlsFormID:Integer, InsideAbonentID:Integer, RespDateFrom:Date, RespDateTo:Date, AddCond:String, [MesID:Integer]):Integer
```

## Процедура: `RsbUsSPFS`

```rsl
RsbUsSPFSRsbUsSPFS(ObjectID:Integer, ObjectType: Integer):Object
```

## Процедура: `SelectExternPaymentFromScrol`

```rsl
SelectExternPaymentFromScrol(Direct:String [, SqlLink:String]):Integer
```

## Процедура: `TransferPaymentInUnclose`

```rsl
TransferPaymentInUnclose (PaymentID:Integer):Integer
```

## Процедура: `WL_GisGmpPaymInfoPanel`

```rsl
WL_GisGmpPaymInfoPanel():Integer
```

## Процедура: `WL_GisGmpPmSelParms_Scroll`

```rsl
WL_GisGmpPmSelParms_Scroll ([Department:Integer], [Mode:Integer], [gisgmpmsg_new:Trechandler], [selectedGisGmpMsgs:Array]):Integer
```

## Процедура: `WldCreateDirection`

```rsl
WldCreateDirection (path:String):Integer
```

## Процедура: `WldCreateReqLink`

```rsl
WldCreateReqLink (ReqID:Integer, ObjID:Integer, ObjKind:Integer, ObjDirect:String):Integer
```

## Процедура: `WldDelReq`

```rsl
WldDelReq (ReqID:Integer):Integer
```

## Процедура: `WldPrintMessage`

```rsl
WldPrintMessage (MesID:Integer):Integer
```

## Процедура: `WldSetInstancyMessage`

```rsl
WldSetInstancyMessage(ObjectKind:Integer, ObjectID:Integer, [Instancy:Integer]):Integer
```

## Процедура: `wlraclient_IsNeededFieldsFilled`

```rsl
wlraclient_IsNeededFieldsFilled (raclient:Trechandler):Bool
```

## Процедура: `WlExecuteReqEditPanel`

```rsl
WlExecuteReqEditPanel(wlreq: Record[,Narrative: String] [,Description: String] [,CopyFields: String] [,TpID: Integer] [,ViewOnly: Bool] [, ObjID:Integer] [, ObjKind:Integer] [, ObjDirect:String]):Integer
```

## Процедура: `WlGGSetRepError`

```rsl
WlGGSetRepError (Error:String):Integer
```

## Процедура: `WlVer_FormatVerDefinitionOnDate`

```rsl
WlVer_FormatVerDefinitionOnDate (TpID:Integer, Partition:String, Date:Date, VersionID:Integer, [Version:String], [ErrMessage:String]):Integer
```

## Процедура: `WlVer_FormatVerPeriodDefinition`

```rsl
WlVer_FormatVerPeriodDefinition(TpID:Integer, Partition:String, Version:String, [StartDate:Date], [FinishDate:Date], [ErrMessage:String]):Integer
```

## Процедура: `WlVer_VerParamDefinition`

```rsl
WlVer_VerParamDefinition(ObjeсtType:Integer, ObjectID:Integer, [TpID:Integer], [Partition:String]):Integer
```

## Процедура: `УстановитьИдентификаторСеанса`

```rsl
УстановитьИдентификаторСеанса (SessUID:String):Bool
```

## Процедура: `ВставитьТребованиеФНС`

```rsl
265 - О - ОбновитьЗаголовокВыписки     265 ОбновитьЗаголовокУведомления     266 ОбновитьЗапись     271 ОбновитьИнфСообщение     266 ОбновитьОтвет     267 ОбновитьПоле     140 ОшибкаЛогическогоКонтроляСообщения     267 Алфавитный указатель - П - ПерейтиВНачалоФайла     271 ПечатьСообщенийСеанса     273 ПечатьСообщения     142 ПечатьУчетныхОбъектовСеанса     274 ПолучитьВидСтраницыВыписки     247 ПолучитьВыпискуПоИдентификатору     268 ПолучитьДействие     143 ПолучитьДокументВыписки     248 ПолучитьКопиюФайлаСеансаСвязи     274 ПолучитьПервоеПримечаниеПлатежа     209 ПолучитьПервуюКатегориюПлатежа     210 ПолучитьПоле     143 ПолучитьРасходыРеспондента     210 ПолучитьСледующееПримечаниеПлатежа     211 ПолучитьСледующуюКатегориюПлатежа     211 ПолучитьСообщение     144 ПоместитьВНезавершенные     269 ПривязатьОбъектДепоКСообщению     269 ПрочитатьТекстЗапроса_Ответа     248 ПрочитатьТекстИнфСообщения     249 - С - СквитоватьПлатеж     270 СоздатьЗапись     271 СоздатьТелеграммуПоПлатежу     249 СчитатьБлок     272 СчитатьЗапись     276 СчитатьПоле     140 СчитатьСвязьЗапросаСУчетнымОбъектом СчитатьСтроку     272 СчитатьУзелМаршрута     141 - Т - ТекущаяСтрока     272 ТекущийРазмерФайла     276 - У - УстановитьИдентификаторСеанса     297 УстановитьКонтекстБлока     139 УстановитьНомерРейса     273 УстановитьОбъект     141 УстановитьФильтрДокументовВыписки     250 Контактная информация R-Style Softlab http://www.softlab.ru/ Фактический адрес 117647, г. Москва, ул. Профсоюзная, д. 125А, 6 этаж Связаться с нами можно по телефонам и электронной почте: Сопровождение т: (495) 796-9311; E-mail: support@softlab.ru Корпоративные продажи т: (495) 796-9310; E-mail: sales@softlab.ru
```
