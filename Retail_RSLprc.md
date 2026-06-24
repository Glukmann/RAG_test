---
title: Retail_RSLprc
description: Процедуры и функции на языке RSL для модуля
category: RSL-процедуры
source: PDF-документация RS-Bank V.6
sections: 475
generated: true
---

## Класс: `TAcqAccount`

```rsl
TAcqAccount()
```

## Класс: `TAcqAccountList`

```rsl
TAcqAccountList()
```

## Класс: `TAcqClient`

```rsl
TAcqClient()
```

## Класс: `TAcqClientList`

```rsl
TAcqClientList()
```

## Класс: `TAcqCompTerm`

```rsl
TAcqCompTerm()
```

## Класс: `TAcqCompTermList`

```rsl
TAcqCompTermList()
```

## Класс: `TAcqDocList`

```rsl
TAcqDocList()
```

## Класс: `TAcqDocType`

```rsl
TAcqDocType()
```

## Класс: `TAcqDocTypeList`

```rsl
TAcqDocTypeList()
```

## Класс: `TAcqDocument`

```rsl
TAcqDocument()
```

## Класс: `TAcqOperation`

```rsl
TAcqOperation()
```

## Класс: `TAcqPaymentSystem`

```rsl
TAcqPaymentSystem()
```

## Класс: `TAcqPointOfSale`

```rsl
TAcqPointOfSale()
```

## Класс: `TAcqPosCurr`

```rsl
TAcqPosCurr()
```

## Класс: `TAcqPosCurrList`

```rsl
TAcqPosCurrList()
```

## Класс: `TAcqPosList`

```rsl
TAcqPosList()
```

## Класс: `TAcqPsList`

```rsl
TAcqPsList()
```

## Класс: `TAcqSlip`

```rsl
TAcqSlip()
```

## Класс: `TAcqSlipList`

```rsl
TAcqSlipList()
```

## Класс: `TAcqTerminal`

```rsl
TAcqTerminal()
```

## Класс: `TAcqTermList`

```rsl
TAcqTermList()
```

## Класс: `TAcqTranList`

```rsl
TAcqTranList()
```

## Класс: `TAcqTransaction`

```rsl
TAcqTransaction()
```

## Класс: `TList`

```rsl
TList()
```


```rsl
TList ()
```

## Класс: `TPersistRecord`

```rsl
TPersistRecord()
```

## Класс: `TPersistVarRecord`

```rsl
TPersistVarRecord()
```

## Класс: `TRecHandler`

```rsl
TRecHandler()
```

Стандартный RSL-класс для работы с записями.
Свойство:
rec – свойство обеспечивает доступ к полям записи; тип TRec.

## Класс: `TVarRecord`

```rsl
TVarRecord()
```

## Процедура: `CloseAcqFiles`

```rsl
CloseAcqFiles()
```

## Процедура: `OpenAcqFiles`

```rsl
OpenAcqFiles(): Bool
```

## Процедура: `ExportAccountingDocuments`

```rsl
ExportAccountingDocuments (RefDocs:Tarray):Tarray
```

## Процедура: `ExportAccountingDocumentsExt`

```rsl
ExportAccountingDocumentsExt (ObjDocs:Tarray [, IdentProg:Integer]):Tarray
```


```rsl
предназначена для выгрузки расчетно- денежных документов во внешнюю систему.
```

**Параметры:**

ObjDocs – массив документов в виде объектов, например в виде Java-объектов расчетно-
денежных документов, выгружаемых во внешнюю систему.
IdentProg – числовой идентификатор подсистемы. При незаданном параметре по
умолчанию используется подсистема "АРМ Бухгалтера".

**Возвращаемое значение:**



## Процедура: `RollBackAccountingDocument`

```rsl
RollBackAccountingDocument (AccDocID:String [, IdentProg:Integer]):Object
```

## Процедура: `RtCarryIncomeDoc`

```rsl
RtCarryIncomeDoc (DocID: Long): Integer
```

## Процедура: `RtDeleteIncomeDoc`

```rsl
RtDeleteIncomeDoc (ApplicationKind: Long, ApplicationKey: Syring, [Srorn: Bool], [stat: Long]): Bool
```

## Процедура: `RtRejectIncomeDoc`

```rsl
RtRejectIncomeDoc (DocID: Long) : Inter
```

## Процедура: `RtExportDocument`

```rsl
RtExportDocument (DocID: Long) : Integer
```

## Процедура: `UniteAccountingDocuments`

```rsl
UniteAccountingDocuments(RefDocs:TArray):Integer
```

## Процедура: `RollBackConsolidatedDocument`

```rsl
RollBackConsolidatedDocument(AccDocID:Integer):Integer
```

## Класс: `TClientList`

```rsl
TClientList ([ReadOnlyFlag:Bool], [FillAddress:Bool], [FillPaper:Bool])
```

## Класс: `TDepClient`

```rsl
TDepClient С помощью класса TDepClient осуществляется доступ к данным по конкретному клиенту. Поля, соответствующие классу TDepClient, описаны в структуре commclnt.rec. Доступ к полям структуры commclnt.rec осуществляется через атрибут rec.
```

**Пример:**

Var cl = TDepClient;   /*Объявление переменной*/
cl.Clear();                     /*Очистка структуры*/
/*Заполнение структуры данных по клиенту (переменной cl),
например, с помощью метода GetRecord*/
var CodClient = cl.rec.CodClient;         /*Получение кода
клиента (поле CodClient)*/
var FullName = cl. ConvertFIOFull ();  /*Получение фамилии,
имени и отчества в одной строке (вызов метода)*/
var  Name = cl.rec.Name1;    /*Фамилия (поле Name1)*/
Свойства класса TDepClient
Для класса TDepClient
 заданы следующие свойства:
AdressType – тип загруженного адреса для текущего клиента-физического лица; тип
Integer. Свойство может принимать следующие значения:
- 1 – юридический (адрес регистрации);
- 2 – фактический (адрес места жительства);
- 3 – почтовый (адрес временной регистрации).
При изменении значения свойства загружается адрес указанного типа. Если
адрес не задан, то результат загрузки зависит от значения свойства
MayMakeNewTypeAdress:
- TRUE – создается новая строка адреса с заданным типом. Сохранить вновь
созданный адрес можно с помощью метода SaveRecAdress
.
- FALSE (по умолчанию) – тип адреса становится неопределенным.
MayMakeNewPaperKind – признак создания новой строки при изменении значения
свойства PaperKind, если вид документа для текущего клиента отсутствует; тип
Bool. Свойство может принимать значения:
- TRUE – создается новая строка.
- FALSE (по умолчанию) – документ клиента становится неопределенным.
MayMakeNewTypeAdress – признак создания новой строки при изменении значения
свойства AdressType, если тип адреса для текущего клиента отсутствует; тип
Bool. Свойство может принимать значения:
- TRUE – новая строка создается.
- FALSE (по умолчанию) – адрес клиента становится неопределенным.
PaperKind – вид документа, удостоверяющего личность клиента; тип Integer. При
изменении свойства загружается документ указанного вида. Если документ не
задан, то результат загрузки зависит от свойства MayMakeNewPaperKind:
- TRUE – создается новая строка документа с заданным видом. Сохранить в
файле вновь созданный документ можно с помощью метода SaveRecPaper
.
- FALSE (по умолчанию) – вид документа становится неопределенным.
PrimaryClientCode – основной код клиента; тип Integer. В качестве значения параметра
устанавливается код, по которому в базе заведены ИНН, адреса, удостоверения
личности.

**Пример:**

var clntL = TClientList;
 if (clntL.GetRecord(210000004))
    MsgBox(clntL.CurRec.PrimaryClientCode);
Методы класса TDepClient
Для класса TDepClient реализованы следующие методы:
Clear():Bool

## Метод: `Clear`

```rsl
выполняет очистку записи (структуры).
```

**Возвращаемое значение:**



## Метод: `MakeDocStr`

```rsl
возвращает строку с информацией по документу, удостоверяющему личность клиента.
```

**Возвращаемое значение:**



## Класс: `TActionRSL`

```rsl
TActionRSL(ApplicationKind:Integer, ApplicationKey:String)
```

## Класс: `TActionList_RSL`

```rsl
TActionList_RSL(Branch:Integer, ContractID:Integer)
```

С помощью класса TActionList_RSL осуществляется доступ к выборке записей по
конкретному договору из таблицы действий над договорами.
Конструктор класса создает список действий для договора, определенного указанными
параметрами.

**Параметры:**

Branch – идентификатор подразделения.
ContractID – идентификатор договора.
Методы класса TActionList_RSL
Для класса TActionList_RSL
 реализованы следующие методы:
ApplyFilter():Bool

## Класс: `TContractRSL`

```rsl
TContractRSL(Branch:Integer, ID:Integer)
```


```rsl
представляет абстрактный договор. Объекту класса соответствует запись в таблице drt_contract_dbt. Конструктор класса создает объект, соответствующий договору по вкладу. При передаче ненулевого значения параметра ID объект заполняется данными договора с указанными Branch и ID; при передаче нулевого значения ID создается новый объект.
```

**Параметры:**

Branch – идентификатор подразделения.
ID – идентификатор договора.
Свойства класса TContractRSL
Для класса TContractRSL
 реализованы следующие свойства:
Action – вид действия над записью о договоре; тип Integer. Параметр может принимать
одно из значений:
- 0 – не определено;
- 1 – открытие;
- 2 – закрытие;
- 3 – блокирование;
- 4 – разблокирование;
- 5 – пролонгация.
BlockDate – дата блокирования договора; тип Date.
BlockType – вид блокирования договора; тип Integer. Параметр может принимать одно из
значений:
- 0 – не блокирован;
- 1 – блокирован по заявлению клиента;
- 2 – блокирован банком.
Branch – идентификатор подразделения, к которому относится договор; тип Integer.
Brigade – идентификатор смены, к которой относится операционист, зарегистрировавший
договор; тип Integer.
ClientCode – код клиента, являющегося владельцем счета, к которому относится договор;
тип Integer.
CloseDate – дата закрытия договора; тип Date.
EndDate – дата окончания срока действия договора; тип Date.
ID – идентификатор договора; тип Integer.
MaxProlNum – максимальное количество оставшихся пролонгаций; тип Integer. Значение
"-1" свидетельствует, что количество пролонгаций не ограничено.
Number – номер договора; тип Char.
OpenDate – дата регистрации договора в системе; тип Date.
Oper – идентификатор операциониста, зарегистрировавшего договор; тип Integer.
SessionNum – номер сессии репликации данных; тип Integer.
StartDate – дата начала срока действия договора; тип Date.
State – состояние договора; тип Integer. Параметр может принимать одно из значений:
- 0 – не обработан;
- 10 – открыт;
- 20 – подготовлен к закрытию;
- 30 – закрыт.
TermExtraDays – количество дней для сроков типа "3 месяца и 1 день"; тип Integer.
TermType – тип срока договора (день, месяц, год и т.п.); тип Integer.
TermValue – срок договора; тип Integer.
Методы класса TContractRSL
Для класса TContractRSL
 реализованы следующие методы:
Block():Bool

## Класс: `TContractList_RSL`

```rsl
TContractList_RSL()
```

С помощью класса TContractList_RSL осуществляется доступ к выборке записей таблицы
договоров.
Конструктор класса создает список договоров.
Методы класса TContractList_RSL
Для класса TContractList_RSL
 реализованы следующие методы:
ApplyFilter():Bool

## Класс: `TDepContractRSL`

```rsl
TDepContractRSL(Branch:Integer, ID:Integer)
```


```rsl
представляет договор по вкладу и является наследником класса TContractRSL . Конструктор класса создает объект, соответствующий договору по вкладу. При передаче ненулевого значения параметра ID объект заполняется данными договора с указанными Branch и ID; при передаче нулевого значения ID создается новый объект.
```

**Параметры:**

Branch – идентификатор подразделения.
ID – идентификатор договора.
Свойства класса TDepContractRSL
Для класса TDepContractRSL
 реализованы следующие свойства:
AccountType – вид вклада, по которому открывается договор; тип String.
BookGiven – признак выдачи сберегательной книжки по счету; тип String.
ContractPrinted – признак печати договора; тип String.
CurrCode – код валюты договора; тип Integer.
Flags – код типа счета; тип String.
NumPatternRef – идентификатор шаблона номера для вида вклада; тип Integer.
SessionNum – номер сессии репликации данных; тип Integer.
ShortNumber – номер договора в рамках группы по шаблону; тип Integer.
Методы класса TDepContractRSL
Для класса TDepContractRSL
 реализованы следующие методы:
Choose_DepReferenc(manuallySelectSingleAccount:Bool):Integer

## Класс: `RSL_LoansCarryDoc`

```rsl
RSL_LoansCarryDoc
```

## Класс: `RSL_LoansCarryList`

```rsl
RSL_LoansCarryList(CredOperID:Integer)
```

## Класс: `RslTDocList`

```rsl
RslTDocList()
```

## Класс: `RslTDocument`

```rsl
RslTDocument()
```


```rsl
RslTDocument()
```

## Класс: `RslTPanel`

```rsl
RslTPanel()
```

## Класс: `TAcqContractRSL`

```rsl
TAcqContractRSL()
```

## Класс: `TCardActionRSL`

```rsl
TCardActionRSL()
```

## Класс: `действия`

```rsl
, выполняемого по договору карты.
```

**Свойства:**

Action – признак сторнирования/удаления действия; тип Integer. Параметр может
принимать одно из значений:
- 2 – действие удалено;
- 11 – действие сторнировано.
BlockCode – код причины блокировки карты (для действия "Блокировка карты"); тип
Integer.
BlockKind – способ блокировки карты; (для действия "Блокировка карты"); тип Integer.
CardActBranch – идентификатор подразделения банка; тип Integer.
CardActNumSession – номер сессии репликации; тип Integer.
DrivingLicLost – признак потери водительского удостоверения (для действия "Блокировка
карты"); тип String.
LossDate – дата потери карты (для действия "Блокировка карты"); тип Date.
LossPlace – место потери карты (для действия "Блокировка карты"); тип String.
LossTime – время потери карты (для действия "Блокировка карты"); тип Time.
PassportLoss – признак потери паспорта (для действия "Блокировка карты"); тип String.
PINLost – признак потери конверта с PIN-кодом карты (для действия "Блокировка карты");
тип String.
StopListInserted – признак помещения карты в стоп-лист (для действия "Блокировка
карты"); тип String.

## Класс: `TCardContractRSL`

```rsl
TCardContractRSL()
```

## Класс: `TCbRfRateList`

```rsl
TCbRfRateList()
```

## Класс: `TConvertCurrency`

```rsl
TConvertCurrency()
```

## Класс: `TdpDepList`

```rsl
TdpDepList()
```

## Метод: `восстанавливает`

```rsl
ранее сохраненную позицию курсора и параметры фильтра. rewind()
```

## Класс: `TJuridicalPerson`

```rsl
TJuridicalPerson()
```

## Процедура: `EDocInitParam`

```rsl
EDocInitParam(EDocKind:Integer, InPackage:Integer, IDData:String, [InternalData:String], [OperCreate:Integer]):Integer
```

## Процедура: `DeskLogDocName`

```rsl
DeskLogDocName(File:String, EDocKind:Integer, IDData:String, InPackage:Integer, [InternalData:String], [OperCreate:Integer]):Integer
```

## Процедура: `GenIDData`

```rsl
GenIDData(EDocKind:Integer, [Regim:Integer], [Info:String]):String
```

## Процедура: `GenInternalData`

```rsl
GenInternalData(EDocKind:Integer, [Regim:Integer], [Info:String]):String
```

## Процедура: `GetCounter`

```rsl
GetCounter (Number:Integer, Branch:Integer, Counter:Record):Bool
```

## Процедура: `GetCountValue`

```rsl
GetCountValue (Number: Integer, Branch: Integer, CountValue: DoubleL [, CountStep: DoubleL]): Bool
```

## Процедура: `SetCounter`

```rsl
SetCounter (Numbe:Integer, Branch:Integer, Counter:File, Record):Bool
```

## Процедура: `BC_CheckSign`

```rsl
BC_CheckSign (Path: String): Integer
```

## Процедура: `BC_FormSign`

```rsl
BC_FormSign (Path: String): Integer
```

## Процедура: `ChangeMainRate`

```rsl
ChangeMainRate (RateID: Integer): Bool
```

## Процедура: `ConvertSumEx`

```rsl
ConvertSumEx(FromCodCur:Integer, ToCodCur:Integer, AmountFrom:Money, ConvertDate:Date, RateKindID:Integer, RateChange:Integer, TypeCalcRate:Integer, CrossCalcType:Integer, flagCommission:Bool, data:Memaddr):Integer
```

## Процедура: `GetMainRateChangeNum`

```rsl
GetMainRateChangeNum (): Integer
```

## Процедура: `ListRateKind`

```rsl
ListRateKind(RateKindID:Integer, RateKindName:String):Integer
```

## Процедура: `PrepareDateTimeForRates`

```rsl
PrepareDateTimeForRates (isNewDocument:Bool [, inDate:Date] [, inTime:Time] [, outDate:Date] [, outTime:Time]):Bool
```

## Процедура: `всегда`

```rsl
возвращает TRUE.
```

**Пример:**

PrepareDateTimeForRates( 
true, 
dateOper, 
null, 
dtRate,
tmRate );
 if ( not FindCurrRate( CodeCurrency, exopset.RateKind,
dtRate, CBRate, BuyRate, SellRate, tmRate, ConvSum ) )
   MsgBox( "Не найден курс для валюты с кодом " +
String( CodeCurrency ) + 
           "|за дату " + String( dateOper ) + " по виду " +
String( exopset.RateKind ) );
   return 1;
 end;
Процедуры для работы с сообщениями об
ошибках


```rsl
возвращает TRUE.
```

**Пример:**

SetLinkedCashier(9999,1,true)

## Процедура: `DisplayErrorMessage`

```rsl
DisplayErrorMessage ([topMessage:String])
```

## Процедура: `выдает`

```rsl
пользователю сообщение об ошибке (из стека ошибок).
```

**Параметры:**

topMessage – сообщение, которое необходимо поместить на вершину стека. Указанное
сообщение будет отображено в диалоговом окне. Если сообщение не задано, в
диалоговое окно будет выводиться последнее добавленное в стек сообщение.

## Процедура: `PushErrorMessage`

```rsl
PushErrorMessage (message:String):Bool
```

## Процедура: `TopErrorMessage`

```rsl
TopErrorMessage (message:String):Integer
```

## Процедура: `CalculateTarifEx`

```rsl
CalculateTarifEx (NumTarif:Integer, CodCur:Integer, Date:Date, SumOper:Money, SumTarif:Money [, ForCloseAcc:Bool] [, RateKind:Integer] [, RateChange:Integer] [, TypeCalcRate:Integer] [, Time:Time] [, CrossCalcType:Integer]):Integer
```

## Процедура: `CalculateTariff`

```rsl
CalculateTariff (tariffId:Integer, currCode:Integer, date:Date, baseAmount:Money, tariffAmount:Money [, calcForCloseAcc:Bool, Integer] [, time:Time] [, typeRate:Integer] [, flagCur:Integer]):Integer
```

## Процедура: `ConvSum`

```rsl
ConvSum (Sum:Money, Rate:Double [, Scale:Integer] [, Point:Integer] [, IsInverse:Bool]):Money
```

## Процедура: `SumConv`

```rsl
SumConv (vSum:Money, vRate:Double [, vScale:Integer] [, vPoint:Integer] [, vIsInverse:Bool]):Money
```

## Процедура: `CarryGDDList`

```rsl
CarryGDDList ([docType:Integer]):Integer
```

## Процедура: `CreateGDDList`

```rsl
CreateGDDList ():Integer
```

## Процедура: `DeleteGDDList`

```rsl
DeleteGDDList ()
```

## Процедура: `FindExchDocInGDDList`

```rsl
FindExchDocInGDDList (TurnType:Integer, Doc:Record):Bool
```

## Процедура: `GetCountDocInGDDList`

```rsl
GetCountDocInGDDList ():Integer
```

## Процедура: `GetFirstDocFromGDDList`

```rsl
GetFirstDocFromGDDList (Addr:Memaddr)
```


```rsl
GetFirstDocFromGDDList (Addr:Memaddr, DocType:Integer):Bool
```

## Процедура: `GetNextDocFromGDDList`

```rsl
GetNextDocFromGDDList (Addr:Memaddr, DocType:Integer):Bool
```

## Процедура: `InsertExchDocToGDDList`

```rsl
InsertExchDocToGDDList (Doc:Record):Bool
```

## Процедура: `PopGDDList`

```rsl
PopGDDList ()
```

## Процедура: `PushGDDList`

```rsl
PushGDDList ()
```

## Процедура: `RemoveDocFromGDDList`

```rsl
RemoveDocFromGDDList ():Bool
```

## Процедура: `RemoveExchDocInGDDList`

```rsl
RemoveExchDocInGDDList (TurnType:Integer):Bool
```

## Процедура: `ConfirmSecondPerson`

```rsl
ConfirmSecondPerson(type:Integer, queryText:String):Bool
```

## Процедура: `CritWaitAcceptEx`

```rsl
CritWaitAcceptEx(type:Integer, desc:String, data:Record, [applKind:Integer], [applKey:String], [statusLine:String], [branch:Integer], [onlyInsert:Bool]):Bool
```

## Процедура: `DefDepBalAccount`

```rsl
DefDepBalAccount(Kind:String, CodCur:Integer, Rezid:String, NameAcc:String, Account:String [, Branch:Integer] [, GroupID:Integer]):Integer
```

## Процедура: `DefPcEstimAccountForDepositr`

```rsl
DefPcEstimAccountForDepositr (depAccount:File, Record, TRecHandler, doAccNameLookup:Bool):String
```

## Процедура: `GetAccountName`

```rsl
GetAccountName (Chapter:Integer, Account:String, CurrCode:Integer):String
```

## Процедура: `GetBookAccounts`

```rsl
GetBookAccounts (ApplDoc: Integer, TypeOper: Integer, Kind: String, FNCash: Integer, IsCur: Integer, CodCur: Integer, DebetAcc: String, CreditAcc: String [, LineNo: Integer]): Bool
```

## Процедура: `GetBookAccountsEx`

```rsl
GetBookAccountsEx (Parm:Record [, SvodVarPart:Record], [SvodVarPartLen:Integer] [, PrimaryDoc:File, Record]):Bool
```

## Процедура: `iFindBankAccount`

```rsl
iFindBankAccount (Account:String, [Currency:Integer, ] Struct:Record [, Chapter:Integer]):Bool С помощью процедуры осуществляется поиск записи о банковском счете в базе данных системы.
```

**Параметры:**

Key – номер искомого счета.
Currency – код валюты искомого счета. По умолчанию используется код национальной
валюты.
Struct (выходной параметр) – структура таблицы базы данных ddepositr_dbt, содержащей
информацию о найденном счете. В структуре заполнены поля t_Code_Currency
(код валюты), t_Account (номер счета), t_CodClient (клиент банка), t_SvodAccount
(балансовый счет), t_FNCash (номер подразделения банка), t_PrevAccount
(связанный счет), t_Open_Close (признак закрытого счета).
Chapter – глава балансового плана счетов, по которой открыт счет. По умолчанию поиск
производится по 1 главе.

**Возвращаемое значение:**



## Процедура: `iListBankAccount`

```rsl
iListBankAccount (Currency:Integer, Account:String [, Сlient:Integer] [, FNCash:Integer] [, Chapter:Integer]):Bool С помощью процедуры осуществляется выбор банковского счета.
```

**Параметры:**

Currency – код валюты счета. По умолчанию в качестве значения параметра
используется код национальной валюты.
Account – номер выбранного счета, выходной параметр.
Сlient – код клиента, являющегося владельцем счета. По умолчанию поиск производится
по всем клиентам.
FNCash – код подразделения, в котором обслуживается счет. По умолчанию поиск
производится без учета подразделения.
Chapter – глава балансового плана счетов, по которой открыт счет; выходной параметр.
По умолчанию поиск производится по 1 главе.

**Возвращаемое значение:**



## Процедура: `OpenSymbolsInAccount`

```rsl
OpenSymbolsInAccount (params:Record, TRecHandler):String
```

## Процедура: `RSB_GetKey`

```rsl
RSB_GetKey (account:String):String
```

## Процедура: `SetKeyDigitInAccount`

```rsl
SetKeyDigitInAccount (InputAccount:String [, BIK:String]): String
```

## Процедура: `findAddress`

```rsl
findAddress (partyId:Integer, addressType:Integer [, address:TRecHandler]):Bool
```

## Процедура: `findDprtPartyCode`

```rsl
findDprtPartyCode (depId:Integer, codeKind:Integer):String
```

## Процедура: `findPartyCode`

```rsl
findPartyCode (partyId:Integer, codeKind:Integer):String
```

## Процедура: `SelectCodeKind`

```rsl
SelectCodeKind (code:Integer, [name:String]):Bool
```

## Процедура: `Log_WriteChanges`

```rsl
Log_WriteChanges (operation:Integer, oper:Integer, ApplicationKind:Integer, [DirNo:Integer, ] NewRec:File, [NewRecVarSize:Integer, ] [OldRec:Record, ] [OldRecValSize:Integer]):Bool
```

## Процедура: `Log_WriteCheckpoint`

```rsl
Log_WriteCheckpoint (Operation: String [, Desc: String]): Bool
```

## Процедура: `LogProcStartEnd`

```rsl
LogProcStartEnd (Action:Integer, Comment:String):Bool
```

## Процедура: `TrnPayLog`

```rsl
TrnPayLog (Str: String): Integer
```

## Процедура: `WriteChangesToLog`

```rsl
WriteChangesToLog (params:Record [, newRec:File, Record, TRecHandler] [, oldRec:File, Record, TRecHandler]):Integer
```

## Процедура: `WriteChronologicalLog`

```rsl
WriteChronologicalLog (num_action:Integer, num_file:Integer, buf_new:File, Record, len_new:Integer, buf_old:File, Record, len_old:Integer):Integer
```

## Процедура: `AppKindToDocKind`

```rsl
AppKindToDocKind (AppKind:Integer):Integer
```

## Процедура: `по`

```rsl
типу документа АС RS-Retail возвращает тип документа RS-Bank V.6.
```

**Параметры:**

AppKind – тип документа (ApplicationKind) в RS-Retail V.6.

**Возвращаемое значение:**



## Процедура: `BC_Archive`

```rsl
BC_Archive (Path: String): Integer
```


```rsl
выполняет архивацию файлов загрузки платежных поручений по безналичным платежам. Архивация выполняется в директорию ..\ARCHLOAD, расположенную на одном уровне с директорией ..\OBJ, при этом исходный файл загрузки удаляется. О факте архивации производится запись в "Журнал аудита". Параметр: Path – путь к архивируемому файлу.
```

**Возвращаемое значение:**



## Процедура: `CashLink_AddRec`

```rsl
CashLink_AddRec (applicationKind:Integer, applicationKey:String)
```


```rsl
CashLink_AddRec(ApplicationKind:Integer, ApplicationKey:String):Bool
```

## Процедура: `CheckChargeID`

```rsl
CheckChargeID (chargeId:String, Account:String):Integer
```

## Процедура: `CheckKeyDigit`

```rsl
CheckKeyDigit (account:String, bankCode:String, codeKind:Integer):Integer
```

## Процедура: `CheckOnAddNewRecord`

```rsl
CheckOnAddNewRecord (PaperKind: Integer, Series: String, Number: String ): Bool
```

## Процедура: `CheckOnBancruptEnd`

```rsl
CheckOnBancruptEnd(isAllowOfManager:Integer, typeOperation:Integer, resolutionFMByBankrupt:Integer):Integer
```

## Процедура: `CheckOnBancruptStart`

```rsl
CheckOnBancruptStart(codClient:Integer, clientRole:String, typeOperation:Integer, dateDoc:Date, resolutionFMByBankrupt:Integer):Integer Проверка на банкротство клиента при проведении операции в RS-Retail.
```

**Параметры:**

codClient – код клиента, который проверяется на банкротство:
- для вкладов – владелец вклада;
- для разовых операций – клиент, для которого проводится операция.
clientRole – роль клиента, который выполняет операцию:
- V – владелец;
- D – доверенное лицо.
typeOperation – тип операции, который проверяется на банкротство:
- 10 – ВКЛАДЫ_ПРИХОД;
- 20 – ВКЛАДЫ_РАСХОД;
- 80 – ПЛАТЕЖ_НЕ_БЮДЖЕТ;
- 90 – ПЛАТЕЖ_В_БЮДЖЕТ;
- 100 – ПЕРЕВОДЫ_ПРИЕМ;
- 110 – ПЕРЕВОДЫ_ВЫДАЧА;
- 140 – ВОО.
dateDoc – дата операции.
resolutionFMByBankrupt – признак банкротства лица, проводящего операцию:
- 0 – банкрот;
- -1 – не банкрот;
- 1 – банкрот, но операция разрешена финансовым управляющим.

**Возвращаемое значение:**



## Процедура: `CheckStopListExt`

```rsl
CheckStopListExt(typeDoc:Integer, buffDoc:Variant, docKind:Integer, docSer:String, docNum:String [, chkBlockSList:bool]):Integer
```

## Процедура: `ClearAssocStorage`

```rsl
ClearAssocStorage()
```

## Процедура: `Client_Address`

```rsl
Client_Address (ClientCode:Integer):String
```

## Процедура: `CloseDepFiles`

```rsl
CloseDepFiles (): Bool
```

## Процедура: `CloseFilesForBook`

```rsl
CloseFilesForBook ():Integer
```

## Процедура: `ConfDlg`

```rsl
ConfDlg (Текст1: String, Текст2: String, ..., ТекстN :String, null: Variant, Кнопка1: String, Кнопка2: String, ..., КнопкаN: String): Integer
```

## Процедура: `CreateAccountingDocs`

```rsl
CreateAccountingDocs (appKind:Integer, operationReference:String [, passNumber:Integer]):Bool
```

## Процедура: `CreateCashOrderBBForRetail`

```rsl
CreateCashOrderBBForRetail (params:File, Record, TRecHandler):Integer
```

## Процедура: `CreateMemOrderBBForRetail`

```rsl
CreateMemOrderBBForRetail (params:File, Record, TRecHandler):Integer
```

## Процедура: `CreateMultyDocBBForRetail`

```rsl
CreateMultyDocBBForRetail (params:File, Record, TRecHandler):Integer
```

## Процедура: `CreatePaymentBBForRetail`

```rsl
CreatePaymentBBForRetail (params:File, Record, TRecHandler):Integer
```

## Процедура: `DeleteDocument`

```rsl
DeleteDocument (ApplicationKind:Integer, ApplicationKey:String [, Storn:Bool] [, ErrNumber:Integer]):Bool
```

## Процедура: `FileCommentRt`

```rsl
FileCommentRt (FileName: String): String
```

## Процедура: `findDepartment`

```rsl
findDepartment (id:Integer [, code:String] [, dpDepParams:Trechandler] [, partyParams:Trechandler]):Bool
```

## Процедура: `FldCommentRt`

```rsl
FldCommentRt (FileName: String, FieldNum: Integer): String
```

## Процедура: `FormApplicationKey`

```rsl
FormApplicationKey (ApplicationKind: Integer): String
```

## Процедура: `FormClientCode`

```rsl
FormClientCode():Integer
```

## Процедура: `FullPath`

```rsl
FullPath (relPath:String, fullPath:String):Bool
```

## Процедура: `Get_ALG_CARDCONTRACT`

```rsl
Get_ALG_CARDCONTRACT ():Object
```

## Процедура: `Get_ALG_COMDEPCLNT`

```rsl
Get_ALG_COMDEPCLNT ():Object
```

## Процедура: `Get_ALG_COMPAYER`

```rsl
Get_ALG_COMPAYER ():Object
```

## Процедура: `Get_ALG_DEPCONTRACT`

```rsl
Get_ALG_DEPCONTRACT ():Object
```

## Процедура: `Get_Currency`

```rsl
Get_Currency (code: Integer, shrt: String, name: String, cop: String): Bool
```

## Процедура: `getBankName`

```rsl
getBankName (): String
```

## Процедура: `GetBankStandart`

```rsl
GetBankStandart (): Integer
```

## Процедура: `GetBitFlag`

```rsl
GetBitFlag (val: Integer, off: Integer): Integer
```

## Процедура: `GetBranchStatus`

```rsl
GetBranchStatus (): Integer
```

## Процедура: `GetCashOrderForBB`

```rsl
GetCashOrderForBB (documentType:Integer, paymentId:Integer [, payerAccount:String] [, receiverAccount:String])
```

## Процедура: `GetChFlagCur`

```rsl
GetChFlagCur (): Integer
```

## Процедура: `GetCNum`

```rsl
GetCNum (): Integer
```

## Процедура: `GetCountUseSeq`

```rsl
GetCountUseSeq (seqId:Integer, value:Integer):Bool
```

## Процедура: `GetCountValueEx`

```rsl
GetCountValueEx (Syst: Integer, Num: Integer [, FNCash: Integer], CountValue: Integer [, CountStep: Integer]): Bool
```

## Процедура: `GetCurDate`

```rsl
GetCurDate (): Date
```

## Процедура: `GetCurrentMode`

```rsl
GetCurrentMode ():Integer
```

## Процедура: `GetDateOff`

```rsl
GetDateOff (startDate:Date, periodUnit:Integer, periodLen:Integer):Date
```

## Процедура: `GetDocUserAttrPool`

```rsl
GetDocUserAttrPool (): Object
```

## Процедура: `GetFactRecLenForFile`

```rsl
GetFactRecLenForFile (FileName: String [,MaxRecLen: Integer [, MaxRecKey: Integer [, nkeys: Integer]]]): Integer
```

## Процедура: `getFilialName`

```rsl
getFilialName ():String
```

## Процедура: `getFilialNum`

```rsl
getFilialName ():String
```

## Процедура: `GetGroupProc`

```rsl
GetGroupProc (linkFlag:Bool [, numLinkDoc:Integer] [, applicationKind:Integer] [, applicationKey:String])
```

## Процедура: `GetIniString`

```rsl
GetIniString (Key:String [, IniFile:String] [, IsPath:Bool]):String
```

## Процедура: `GetISOCur`

```rsl
GetISOCur (Cod:Integer):String
```


```rsl
GetISOCur(CurrCode:Integer):String
```

## Процедура: `GetLinkedKassir`

```rsl
GetLinkedKassir (ApplicationKind:Integer, Cashier:Integer [, IsCur:Integer] [, IsIncome:Bool]):Bool
```

## Процедура: `GetNameAlg`

```rsl
GetNameAlg (Kind: Integer, Item: Integer) String
```

## Процедура: `GetNameOfPAPRKIND`

```rsl
GetNameOfPAPRKIND (PaperKind: Integer): String
```

## Процедура: `GetNextBookAccountsLine`

```rsl
GetNextBookAccountsLine (parm:Record):Bool
```

## Процедура: `GetOper`

```rsl
GetOper (): Integer
```

## Процедура: `GetOperBrigade`

```rsl
GetOperBrigade (): Integer
```

## Процедура: `GetOperBrigadeCur`

```rsl
GetOperBrigadeCur ():Integer
```

## Процедура: `getOurBankOKATO`

```rsl
getOurBankOKATO ():String
```

## Процедура: `getOurBankOKPO`

```rsl
getOurBankOKPO ():String
```

## Процедура: `GetPrintPort`

```rsl
GetPrintPort (alias:String):Integer
```

## Процедура: `GetProgramID`

```rsl
GetProgramID (): Integer
```

## Процедура: `getRegNumOurBank`

```rsl
getRegNumOurBank (CodeKind:Integer):String
```

## Процедура: `GetRegVal`

```rsl
GetRegVal (Key: String [, IsDir: Bool]):Record С помощью процедуры определяется значение параметра c именем Key, заданное в справочнике настроек ИБС подсистемы "Сервис розничных услуг".
```

**Параметры:**

Key – параметр, определяющий имя параметра в справочнике настроек ИБС.
IsDir – признак добавления символа к возвращаемому значению:
- TRUE – к возвращаемому значению параметра Key будет добавлен символ "\",
если возвращаемое значение имеет тип String и последний символ отличен от
"\".
- FALSE – возвращаемое значение параметра Key не будет изменено.

**Возвращаемое значение:**



## Процедура: `GetRetailOpDescription`

```rsl
GetRetailOpDescription (rec:File, Record, Tbfile, TRecHandler):String
```

## Процедура: `GetRetailVersion`

```rsl
GetRetailVersion (): String
```

## Процедура: `GetShowSpecialAccessAccounts`

```rsl
GetShowSpecialAccessAccounts ():Bool
```

## Процедура: `GetSpecialAccess`

```rsl
GetSpecialAccess ():Integer
```

## Процедура: `GetStringM`

```rsl
GetStringM ([value:String] [, prompt:String] [, width:Integer] [, height:Integer]):String
```

## Процедура: `GetTransactionNumber`

```rsl
GetTransactionNumber ():Integer
```

## Процедура: `GKBO_FindFinInstrCurr`

```rsl
GKBO_FindFinInstrCurr (FIID:Integer):Integer
```

## Процедура: `GKBO_GetFICodeByISO`

```rsl
GKBO_GetFICodeByISO (CodIso: Integer): Integer
```

## Процедура: `GKBO_Reg`

```rsl
GKBO_Reg ([silent:Bool] [, connMode:Integer]):Integer
```

## Процедура: `GKBO_Unreg`

```rsl
GKBO_Unreg ([silent:Integer]):Integer
```

## Процедура: `IdentProgram`

```rsl
IdentProgram (): String
```

## Процедура: `iFindBank`

```rsl
iFindBank (codeKind:Integer, code:String, name:String, corrAccount:String):Bool
```

## Процедура: `iFindBankClnt`

```rsl
iFindBankClnt (Сlient:Integer, [Name:String, ] INN:String [, KPP:String]):Bool С помощью процедуры осуществляется поиск записи о клиенте в таблице базы данных dparty_dbt.
```

**Параметры:**

Сlient – код клиента.
Name – полное наименование клиента, выходной параметр.
INN – ИНН клиента, выходной параметр.
KPP – код причины постановки на учет, выходной параметр.

**Возвращаемое значение:**



## Процедура: `iListKBK`

```rsl
iListKBK (KBK: String) Bool С помощью процедуры осуществляется выбор записи о коде бюджетной классификации платежа из справочника КБК.
```

**Параметры:**

KBK (выходной параметр) – код КБК.

**Возвращаемое значение:**



## Процедура: `iListLLVALUES`

```rsl
iListLLVALUES (Name: String, Kod: String) Bool С помощью процедуры осуществляется выбор записи из пользовательского справочника.
```

**Параметры:**

Name – название выбранной записи, выходной параметр.
Kod – код выбранной записи, выходной параметр.

**Возвращаемое значение:**



## Процедура: `InterDesk_EndDocBunch`

```rsl
InterDesk_EndDocBunch():Bool
```

## Процедура: `InterDesk_GetBunchApplic`

```rsl
InterDesk_GetBunchApplic(ApplicationKind:Integer, ApplicationKey:String):Bool
```

## Процедура: `InterDesk_InitDocBunch`

```rsl
InterDesk_InitDocBunch(applicationKind:Integer, ApplicationKey:String, params:Record):Bool Внимание! Эта процедура должна быть обязательно вызвана перед использованием процедуры CashLink_AddRec, причем, если формирование связки документов производится в транзакции, то процедура InterDesk_InitDocBunch должна быть вызвана в рамках этой транзакции. С помощью процедуры открывается новая связка документов.
```

**Параметры:**

ApplicationKind – вид приложения.
ApplicationKey – идентификатор операции.
params – параметры операции, представленные в структуре op_parm.rec.
Ниже приведен список значимых для инициализации полей структуры op_parm.rec:
Имя поля
Тип
Длина
Примечание
ApplicationKind
INT
Идентификатор операции
ApplicationKey
STRING
Идентификатор операции
Date
DATE
Дата
Operation
LONG
Номер операции соответствующего
банковского продукта
SubOp
INT
Подвид операции
ObjectRef
STRING
Ссылка на "основной" объект
Oper
INT
Операционист
Cashier
INT
Кассир
iToken
LONG
Номер документа (жетона)
Имя поля
Тип
Длина
Примечание
sToken
STRING
Номер документа (жетона)
OnLineOtherBranch
CHR
Операция по чужому подразделению
CodCur
INT
Код валюты главного документа
Flags
LONG
Побитовые флаги

**Возвращаемое значение:**



## Процедура: `InterDesk_IsDocBunchActive`

```rsl
InterDesk_IsDocBunchActive():Bool С помощью процедуры определяется наличие в текущий момент времени активной связки документов по операции.
```

**Возвращаемое значение:**



## Процедура: `InterDesk_MakeDocBunchCurrent`

```rsl
InterDesk_MakeDocBunchCurrent (applicationKind:Integer, applicationKey:String [, searchHead:Bool]):Bool
```

## Процедура: `InTransaction`

```rsl
InTransaction ():Bool
```

## Процедура: `IsGKBOActive`

```rsl
IsGKBOActive ():Bool
```

## Процедура: `IsHoliday`

```rsl
IsHoliday (date:Date):Integer
```

## Процедура: `IsOpenDay`

```rsl
IsOpenDay ():Integer
```

## Процедура: `IsOutputAccumulated`

```rsl
IsOutputAccumulated (): Bool
```

## Процедура: `LastDayInMonth`

```rsl
LastDayInMonth (date:Date):Integer
```


```rsl
LastDayInMonth (d:Date):Integer
```

## Процедура: `LinkOpToObject`

```rsl
LinkOpToObject (params:Record):Bool
```

## Процедура: `list_alg`

```rsl
list_alg (type:Integer, name:String):Integer
```

## Процедура: `ListBranches`

```rsl
ListBranches (Branch: Integer, NameBranch: String): Bool
```

## Процедура: `ListValidCategory_117`

```rsl
ListValidCategory_117 ([codeAcc:String, ] direction:Integer, [parentNum:String, ] categ:String):Bool
```

## Процедура: `LP_Shield`

```rsl
LP_Shield ():Integer
```

## Процедура: `MakeGround`

```rsl
MakeGround (Template:String, AppKind:Integer, Case:Integer, PrimDoc:File, Record [, WrapDoc:File, Record] [, CcwDoc:File, Record]):String
```

## Процедура: `MakeUniKey`

```rsl
MakeUniKey (PaperKind:Integer, Series:String, Number:String):String
```

## Процедура: `MultySelectCurrency`

```rsl
MultySelectCurrency(AccountType:String, RubInList:Bool, CurrencyList:TArray):Integer
```

## Процедура: `MultySelectFDep`

```rsl
MultySelectFDep(BranchList:TArray):Integer
```

## Процедура: `NumFlagCur`

```rsl
NumFlagCur (): Integer С помощью процедуры определяется текущее значение глобального флага валютности.
```

**Возвращаемое значение:**



## Процедура: `NumFNCash`

```rsl
NumFNCash (): Integer
```

## Процедура: `NumRealFNCash`

```rsl
NumRealFNCash (): Integer
```

## Процедура: `OpenDepFiles`

```rsl
OpenDepFiles (): Bool С помощью процедуры выполняется открытие таблиц баз данных для проводок по всем банковским продуктам.
```

**Возвращаемое значение:**



## Процедура: `OpenFilesForBook`

```rsl
OpenFilesForBook ():Integer
```

## Процедура: `PaperTypeName`

```rsl
PaperTypeName (Code: Integer): String
```

## Процедура: `PmntPropBufInit`

```rsl
PmntPropBufInit ():Bool
```

## Процедура: `PrintReports`

```rsl
PrintReports (ApplicationKind: Integer, ApplicationKey: String [, Mode: Integer])
```

## Процедура: `RegNumToStr`

```rsl
RegNumToStr (series: String , number: Integer [, leaveBlanks: Bool]): String
```

## Процедура: `RetrieveValue`

```rsl
RetrieveValue (Key: String): Variant
```

## Процедура: `RtDocumentList`

```rsl
RtDocumentList(filter:Record, result:Record):Integer
```

## Процедура: `RTsessionActionEnd`

```rsl
RTsessionActionEnd()
```

## Процедура: `RTsessionActionMess`

```rsl
RTsessionActionMess(Message:String, [isDML:Bool])
```

## Процедура: `SelectBank`

```rsl
SelectBank ([BIC:String] [, CorrAcc:String] [, ClearingCode:String] [, Name:String]):Bool
```

## Процедура: `SelectBrigadeForBranch`

```rsl
SelectBrigadeForBranch (branch:Integer, date:Date, brigadeId:Integer):String
```

## Процедура: `SelectCurrency`

```rsl
SelectCurrency (CurrCode:Integer [, DontCheckCurrFlag:Bool] [, IncludeNatCur:Bool]):Bool С помощью процедуры осуществляется выбор валюты из справочника валют.
```

**Параметры:**

CurrCode – код выбранной валюты, выходной параметр.
DontCheckCurrFlag – признак отказа от проверки режима валютности. Если значение
параметра равно FALSE, процедура не выполняется в режиме национальной
валюты. По умолчанию используется значение TRUE.
IncludeNatCur – признак включения национальной валюты в список валют. По умолчанию
параметр принимает значение TRUE.

**Возвращаемое значение:**



## Процедура: `selectDepartment`

```rsl
selectDepartment (id:Integer, [name:String, ] mode:Integer, parentId:Integer [, dpDepParams:TRecHandler] [, partyParams:TRecHandler]):Bool
```

## Процедура: `SelectDepClient`

```rsl
SelectDepClient (x: Integer, y: Integer, l: Integer, fil: Integer): Integer
```

## Процедура: `SelectFMCodes`

```rsl
SelectFMCodes(Codes:String):Integer
```

## Процедура: `SelectFNCash`

```rsl
SelectFNCash (Branch:Integer):Bool
```

## Процедура: `SelectOFK`

```rsl
SelectOFK ([Code:String], [CorAcc:String], [Name:String], [partyId:Integer], [CodeKind:Integer]):Bool
```

## Процедура: `SelectRegNum`

```rsl
SelectRegNum (CashOper:String, ValueRef:Integer, Date:Date, Nominal:Money [, Series:String] [, Number:Integer] [, SubAccount:String])
```

## Процедура: `SetAllFNCash`

```rsl
SetAllFNCash (NewFNCash: Integer, NewRealFNCash: Integer): Integer
```

## Процедура: `SetBitFlag`

```rsl
SetBitFlag (val: Integer, off: Integer): Integer
```

## Процедура: `SetCurDate`

```rsl
SetCurDate (NewDate: Date): Bool С помощью процедуры устанавливается новая дата операционного дня.
```

**Параметры:**

NewDate – новая дата операционного дня.

**Возвращаемое значение:**



## Процедура: `SetDlgCaption`

```rsl
SetDlgCaption (dlg:Trechandler, caption:TRecHandler):Bool
```

## Процедура: `SetFlagCur`

```rsl
SetFlagCur (NewFlagCur:Integer [, CheckPerm:Integer]):Integer
```

## Процедура: `SetGroupProc_NDoc`

```rsl
SetGroupProc_NDoc (numLinkDoc:Integer):Bool
```

## Процедура: `SetFNCash`

```rsl
SetFNCash (NewFNCash: Integer): Integer
```

## Процедура: `SetKassir`

```rsl
SetKassir (AppKind:Integer, Kassir:Integer [, IsCur:Integer] [, IsIncome:Bool]):Bool
```

## Процедура: `SetLinkedCashier`

```rsl
SetLinkedCashier (Cashier:Integer [, IsCur:Integer] [, IsIncome:Bool]):Bool
```

## Процедура: `SetOperBrigade`

```rsl
SetOperBrigade(Brigade:Integer]):Integer
```


```rsl
SetOperBrigade(Date:Date [, oper:Integer]):Integer
```

## Процедура: `SetOperDprt`

```rsl
SetOperDprt (newOperDprt:Integer):Integer
```

## Процедура: `SetPrintPort`

```rsl
SetPrintPort (Port: String)
```

## Процедура: `SetProcessCarryForOtherBranch`

```rsl
SetProcessCarryForOtherBranch ([Branch:Integer] [, ProcessCarryForOtherBranc h: Integer]):Integer
```

## Процедура: `SetProgramID`

```rsl
SetProgramID (NewID: Integer): Integer
```

## Процедура: `SetRealFNCash`

```rsl
SetRealFNCash (NewRealFNCash: Integer): Integer
```

## Процедура: `SetTransactionNumber`

```rsl
SetTransactionNumber (number:Integer)
```

## Процедура: `SetRegValue`

```rsl
SetRegValue ():Bool
```

## Процедура: `Sign`

```rsl
Sign (PrimType:String, PrimRef:String, [SecType:String, ] [SecRef:Integer, ] Cmd:Integer, Name:String [, PicFile:String]):Integer
```

## Процедура: `SplitPersIDStr`

```rsl
SplitPersIDStr(Str:String, DepClient:Record):Bool
```

## Процедура: `StoreValue`

```rsl
StoreValue (Key: String, Value: Variant): Bool
```

## Процедура: `StrToValForProperty`

```rsl
StrToValForProperty (text:String, valType:Integer):String
```

## Процедура: `SwitchProgramModule`

```rsl
SwitchProgramModule([NewID:Integer] [, OldID:Integer]):Integer
```

## Процедура: `TransLiteration`

```rsl
TransLiteration (cyrSurname:String, cyrName:String, cyrPatronymic:String, latSurname:String, latName:String, latPatronymic:String):Integer
```

## Процедура: `ДатаРегистрацииКлиента`

```rsl
ДатаРегистрацииКлиента (account:String, fiid:Integer):Date
```

## Процедура: `DeleteCardContractFromAccessGroup`

```rsl
DeleteCardContractFromAccessGroup(ContractID:Integer, Branch:Integer, GroupID:Integer):Integer
```

## Процедура: `DeleteDepContractFromAccessGroup`

```rsl
DeleteDepContractFromAccessGroup(ContractID:Integer, Branch:Integer, GroupID:Integer):Integer
```

## Процедура: `InsertCardContractIntoAccessGroup`

```rsl
InsertCardContractIntoAccessGroup(ContractID:Integer, Branch:Integer, GroupID:Integer):Integer
```

## Процедура: `InsertDepContractIntoAccessGroup`

```rsl
InsertDepContractIntoAccessGroup(ContractID:Integer, Branch:Integer, GroupID:Integer):Integer
```

## Процедура: `TakeStringAccessibleGroups`

```rsl
TakeStringAccessibleGroups ():String
```

## Процедура: `AI_SBook_Num`

```rsl
AI_SBook_Num ([Reference: Integer,] Serial: String, Number: Integer):Integer
```

## Процедура: `CalcCommissionOnOper`

```rsl
CalcCommissionOnOper(BufdepDoc:Record, SummaOper:Money, Summa:Money, CashCh:String):Integer
```

## Процедура: `CalcCommissionOnCP`

```rsl
CalcCommissionOnOper(BufdepDoc:Record, SummaOper:Money, Summa:Money, CashCh:String):Integer
```

## Процедура: `CalcEffectiveInterestRate`

```rsl
CalcEffectiveInterestRate (ref:Integer, [depDate:Date], [eir:Numeric]):Integer
```

## Процедура: `CalcNDSforMetal`

```rsl
CalcNDSforMetal(Reference:Integer, ReqID:Integer):Money
```

## Процедура: `CalcPercentForecast`

```rsl
CalcPercentForecast (aPcCalc:TArray, vRef:Long, vDateCalculate:Date):Integer
```

## Процедура: `CalcTotalDepositCost`

```rsl
CalcTotalDepositCost(aPcCalc:TArray, vRef:Integer, vDateStart:Date, vDateEnd:Date):Integer
```

## Процедура: `CarryNFOp`

```rsl
CarryNFOp (Referenc:Integer, OpNumber:Integer)
```

## Процедура: `CarryPayDocument`

```rsl
CarryPayDocument (PayDoc:Record):Integer
```

## Процедура: `CheclAlgPoint`

```rsl
CheckAlgPoint(Document:File, Record, TRecHandler, StepNumber:Integer):Integer
```

## Процедура: `CheckIsPBR`

```rsl
CheckIsPBR(partyID:Integer):Bool
```

## Процедура: `ChoosePaySubOper`

```rsl
ChoosePaySubOper(OpGroup:Integer, OpNumber:Integer):Integer
```

## Процедура: `ConvertPartSum`

```rsl
ConvertPartSum (doc: Object, type_doc: Integer, what_do: Integer, ConvertSum: MoneyL): Integer
```

## Процедура: `CP_Carry`

```rsl
CP_Carry (pay_doc:Memaddr [, dep_doc:Memaddr])
```

## Процедура: `CP_CashCarry`

```rsl
CP_CashCarry (pay_doc:Memaddr, pay_doc_cp:Memaddr, pprop:Memaddr):Integer
```

## Процедура: `CreatePlanPay4AccEx`

```rsl
CreatePlanPay4AccEx (operation: Integer, operation2: Integer, planpay: Object): Bool
```

## Процедура: `DeleteDepAcc`

```rsl
DeleteDepAcc(Reference:Integer, DeletePhysically:Bool):Integer
```

## Процедура: `Dep_FindTemplateAndCreateDocs`

```rsl
Dep_FindTemplateAndCreateDocs(IsCur:Integer, Kind:String, typeOper:Integer, applType:Integer, Account:String, ApplKind:Integer, ApplKey:String):Integer
```

## Процедура: `DepSetGround`

```rsl
DepSetGround(depdoc: File, Record, Tbfile, TRecHandler): Integer
```

## Процедура: `EditDepositor`

```rsl
EditDepositor (Parm: Record): Integer
```

## Процедура: `EdRefWrite`

```rsl
EdRefWrite (ApplicationKind: Integer, ApplicationKey: String): Integer С помощью процедуры добавляется новая запись в таблицу dsb_edref_dbt для дальнейшей возможности выпуска ордеров.
```

**Параметры:**

ApplicationKind – вид идентификатора объекта.
ApplicationKey – идентификатор объекта.

**Возвращаемое значение:**



## Процедура: `FindBankDprtAccount`

```rsl
FindBankDprtAccount(bankCodeKind:Integer, codeKind:String, corrAcc:String):Integer
```

## Процедура: `FormAccountNumber`

```rsl
FormAccountNumber (CurrCode: Integer, DepType: Integer, Number: Integer, Citizenship: Integer [, GroupNumber:Integer]): String
```

## Процедура: `FormReference`

```rsl
FormReference(): Integer
```

## Процедура: `GetCommissionOnOper`

```rsl
GetCommissionOnOper(buf:Record, SumOper:MoneyL, Action:Integer, SumCom:MoneyL, TypeCom:String, NumOper:Integer [, ComlexOper:Integer]):Integer
```

## Процедура: `GetDepRate`

```rsl
GetDepRate(BufdepDoc:Record, ConvCur:Integer, Sum:Money, RateKind:Integer, isMCD:Bool, RateOper:Double, RateType:String):Integer
```

## Процедура: `GetIndebtRestforDate`

```rsl
GetIndebtRestForDate(Branch:Integer, IndebtID:Long [, Date:Date]):MoneyL
```

## Процедура: `GetPayDate`

```rsl
GetPayDate (PercDate:Date, recPcAlg:Record):Integer
```

## Процедура: `GetRealTermForDepositor`

```rsl
GetRealTermForDepositor(StartDate:Date, Term:Integer, KindTerm:String, Term_Min:Integer, KindTerm_Min:String, Term_Max:Integer, KindTerm_Max:String, TreatHolidays:String, ResTerm:Integer, ResKindTerm:String, EndDate:Date):Integer
```

## Процедура: `GetRestForDate`

```rsl
GetRestForDate (id_par:Integer, date_par:Date):Money
```

## Процедура: `GetRestLienAccount`

```rsl
GetRestLienAccount (Счет:String, ФинИнструмент:Integer, ПодразделениеСчета:Integer, [ВладелецСчета:Integer], [ТекстОшибки:String], [СуммаОстатка:Money], [ФинИнструментОстаток:Integer]):Integer
```

## Процедура: `InitIndebtDoc`

```rsl
InitIndebtDoc(Pindebt:Record, Indebtdoc:Record):Bool
```

## Процедура: `InitIndebtDocForNewIndebt`

```rsl
InitIndebtDocForNewIndebt(Deposit:Record, Indebtdoc:Record):Bool
```

## Процедура: `InitPayDoc`

```rsl
InitPayDoc (Buff: Object, CreateReport: Bool): Bool
```

## Процедура: `InsertDocToGDDList`

```rsl
InsertDocToGDDList (Doc:Record):Bool
```

## Процедура: `InsertIndebtDocToGDDList`

```rsl
InsertIndebtDocToGDDList(Indebtdoc:Record):Bool
```

## Процедура: `InsertPayDoc`

```rsl
InsertPayDoc(Buff:Record):Bool
```

## Процедура: `InsertPayDocToGDDList`

```rsl
InsertPayDocToGDDList(Doc:Record):Bool
```

## Процедура: `IsExistSalaryAcc`

```rsl
IsExistSalaryAcc(ClientID:Integer, retval:Integer):Bool
```

## Процедура: `ListCorrAccount`

```rsl
ListCorrAccount(bankCodeKind:Integer, bankCode:String, corrAcc:String)
```

## Процедура: `ListRegion`

```rsl
ListRegion():String
```

## Процедура: `LoadXmlAccounts`

```rsl
LoadXmlAccounts (dupkeyAct:Integer [, fileName:String]):Bool
```

## Процедура: `LoadXmlDepTyp`

```rsl
LoadXmlDepTyp (dupkeyAct:Integer [, fileName:String]):Bool
```

## Процедура: `ManageLienAccount`

```rsl
ManageLienAccount (ДоговорОбеспечения:Integer, Операция:Integer, ФлагСторнирования:Bool, ОперацияВид:Integer, ОперацияИД:String, ИДАреста:Integer, НомерСчета:Integer, Валюта:Integer, Подразделение:Integer, [Владалец:Integer], СуммаЗалога:Money, ВалютаЗалога:Integer, [КодСообщения:String]):Integer
```

## Процедура: `moveAccountIntoAnotherState`

```rsl
moveAccountIntoAnotherState (newState: String, referenc: Integer, startDate: Date, endDate: Date [, calcDate: Date[, opDate: Date [, CarryDate: Integer]]]): Integer
```

## Процедура: `MultySelectDeptypep`

```rsl
MultySelectDeptypep(DepType:TArray):Integer
```

## Процедура: `PanelAccountForSelect`

```rsl
PanelAccountForSelect ([Type_Account: String], [Code_Currency: Integer], [ListCode_Currency: Integer], [Open_Close: Integer], [CodClient: Integer], [ParamForChange: Integer], [OtherBranch: Integer], [InFNCash: Integer]): Integer, [typePodrForList : Integer])
```

## Процедура: `PanelClientForPayDoc`

```rsl
PanelClientForPayDoc()
```

## Процедура: `PaySetGround`

```rsl
PaySetGround(pay_doc:File, Record, Tbfile, TRecHandler):Integer
```

## Процедура: `PerformConversion`

```rsl
PerformConversion (Buff:Record): Bool
```

## Процедура: `PlayProcExAnSys`

```rsl
PlayProcExAnSys(ProgramID:Integer, String, ModuleNum:Integer, ViewReport:Bool):Bool
```

## Процедура: `PP_GetPaymentSum`

```rsl
PP_GetPaymentSum(ID:Integer, Sum:Money):Integer
```

## Процедура: `RtCloseDay`

```rsl
RtCloseDay([BatchMode:Bool], [newDate:Date]):Bool
```

## Процедура: `RtOpenDay`

```rsl
RtOpenDay ([BatchMode:Bool]):Bool
```

## Процедура: `RunClientRoleOperation`

```rsl
RunClientRoleOperation(NFONumber:Integer, ContractBranch:Integer, ContractId:Integer, [ClientRoleList:Array], [NoInterface:Bool]):Integer
```

## Процедура: `RunPayOperation`

```rsl
RunPayOperation(PayDoc:Record):Integer
```

## Процедура: `SelectAccount`

```rsl
SelectAccount(DepType:String [, CurrCode:Integer] [, ClientCode:Integer] , Reference:Integer [, OpenClose:Integer]):Bool
```

## Процедура: `SelectCPReceiver`

```rsl
SelectCPReceiver (recv:Record, payKind:Record):Bool
```

## Процедура: `SelectDepType`

```rsl
SelectDepType(DepType:String [, IsCur:Integer]):Bool
```

## Процедура: `SelectPayCorr`

```rsl
SelectPayCorr(Buff:File, Record, TRecHandler):Bool
```

## Процедура: `SetBatchMode`

```rsl
SetBatchMode(value:Bool):Bool
```

## Процедура: `SimpleCalcPcEstim`

```rsl
SimpleCalcPcEstim(PercDate:Date, Referenc:Integer, SummaPerc:Money):Integer
```

## Процедура: `StoreAddPayDoc`

```rsl
StoreAddPayDoc(AddPayDoc:Record):Bool
```

## Процедура: `TestErrorsDepAccount`

```rsl
TestErrorsDepAccount (refDepAcc:Long, beginDate:Date, correctionError:Bool, isErrorInDepAcc:Bool):Integer
```

## Процедура: `TreatOnePlanPayments`

```rsl
TreatOnePlanPayments (Referenc:Integer):Integer
```

## Процедура: `TypeIssueToKind`

```rsl
TypeIssueToKind(Type:Integer, Issue:Integer): String
```

## Процедура: `UpdateAlgRecords`

```rsl
UpdateAlgRecords(mask: Integer [, save:Bool]):Bool
```

## Процедура: `UpdateDepStats`

```rsl
UpdateDepStats(Parm:Object):Bool
```

## Процедура: `UpdateStatistics`

```rsl
UpdateStatistics([queryUser:Bool], [depType:String], [isCur:Integer], [branch:Integer])
```

## Процедура: `Выполнение_Операции`

```rsl
Выполнение_Операции(Parm:Record, [Doc:Record], [RecvAttr:Record], [IPSPaym:Record]):Integer
```

## Процедура: `Выполнить_Операцию`

```rsl
Выполнить_Операцию(Account:String, AccType:String, Code_Currency:Integer, Operation:Integer [, Document:ecord [, ShowPanel:Integer [, UseMaxDate:Integer]]], NoPrint:Integer [, CompexOperation:Integer [, DocumentAuthor:Integer [, AuthorCode:Integer]]], CorAcnt:String, CorType:String [, DepDate:Date [, ObjectPercExe:Integer [, CalcDate:Date [, NotMakePercentDocument:Integer]]]]):Integer
```

## Процедура: `НовыйСчетБезДокументов`

```rsl
НовыйСчетБезДокументов(InitDepRec:Object [, Op:Integer [, GroupID:Integer]]):Integer
```

## Процедура: `ОтнестиСчетКГруппе`

```rsl
ОтнестиСчетКГруппе(Счет:Integer, Группа:Integer):Integer
```

## Процедура: `РучнойВводВкладногоДокумента`

```rsl
РучнойВводВкладногоДокумента(SbDepDoc:Object [, LinkParam:Integer]):Integer
```

## Процедура: `РучнойВводИсторииОпераций`

```rsl
РучнойВводИсторииОпераций (Referenc: Integer [, LinkParam: Integer]): Integer
```

## Процедура: `СписокНаследниковВклада`

```rsl
СписокНаследниковВклада(Referenc:Integer):Integer
```

## Процедура: `Список_Получателей_КП`

```rsl
Список_Получателей_КП():Integer
```

## Процедура: `AutoConfirm`

```rsl
AutoConfirm([mode:Integer):Integer
```

## Процедура: `CashDocBunch`

```rsl
CashDocBunch (appKind:Integer, appKey:String):Bool
```

## Процедура: `CheckCashLink`

```rsl
CheckCashLink(type:Integer, valType:Integer, valCode:Integer, applicationKind:Integer, applicationKey:String):Bool
```

## Процедура: `CheckCashRes`

```rsl
CheckCashRes(Code:Integer):Bool
```

## Процедура: `DeleteCashAccForValue`

```rsl
DeleteCashAccForValue(ValueRef:Integer)
```

## Процедура: `FindCodCurByRefVal`

```rsl
FindCodCurByRefVal(valueRef:Integer):Integer
```

## Процедура: `GetBagClientName`

```rsl
GetBagClientName(applicationKind:Integer, applicationKey:String):String
```

## Процедура: `GetClientInfo`

```rsl
GetClientInfo(Type:Integer, ID:Integer, [Name:String], [BIC:String], [CorrAcc:String], [Address:String], [INN:String]):Bool
```

## Процедура: `InitCashDoc`

```rsl
InitCashDoc(Parm:Record, ImmediateProcessing:Bool, BalCost:Integer):Integer
```

## Процедура: `InputRegNum`

```rsl
InputRegNum(oper:Integer, [linkedCashier:Integer], valueType:Integer, valueCode:Integer, [prompt:String], Series:String, Number:Integer, [prefill:Bool], [valueState:Integer]):Bool
```

## Процедура: `предоставляет`

```rsl
окно для ввода (выбора) регистрационного номера ценности.
```

**Параметры:**

oper – номер операциониста.
linkedCashier – номер связанного кассира.
valueType – тип ценности.
valueCode – внешний код ценности.
prompt – строка с текстом подсказки.
Series – возвращаемое значение введенной серии.
Number – возвращаемое значение введенного номера.
prefill – признак автоматической подстановки первого доступного номера в панель.
valueState – состояние ценности (по умолчанию - платежеспособная).

**Возвращаемое значение:**



## Процедура: `L_RTCasSym`

```rsl
L_RTCasSym (mode:Integer, fullSum:Money, operation:Integer, applicationKind:Integer, applicationKey:String):Bool
```

## Процедура: `NextRegNum`

```rsl
NextRegNum(Subj:String, ValueRef:Integer, Series:String, Number:Integer):Bool
```

## Процедура: `SplitCurrBag`

```rsl
SplitCurrBag(Bag:Record):Bool
```

## Процедура: `UnconfirmCashDoc`

```rsl
UnconfirmCashDoc(ApplicationKind Integer, ApplicationKey String) Bool
```

## Процедура: `ChoiceEmployee`

```rsl
ChoiceEmployee():Integer
```

## Процедура: `CurrToStr`

```rsl
CurrToStr(Sum:MoneyL, CurrCode:Integer): String
```

## Процедура: `GetFIOEmployee`

```rsl
GetFIOEmployee(Number:Integer):String
```

## Процедура: `GetFullNameEmployee`

```rsl
GetFullNameEmployee(Number Integer) String
```

## Процедура: `GetNameCodif`

```rsl
GetNameCodif(ExtNumb:Integer, RootExtNumb:Integer):String
```

## Процедура: `GetNameCur`

```rsl
GetNameCur(CurrCode:Integer):String
```

## Процедура: `GetNamePayDoc`

```rsl
GetNamePayDoc(Ref:Integer):String
```

## Процедура: `GetNameReestr`

```rsl
GetNameReestr(Type:Integer):String
```

## Процедура: `GetNameValForm`

```rsl
GetNameValForm(Ref: Integer):String
```

## Процедура: `GetNumReestr`

```rsl
GetNumReestr(OperRef:Integer):Integer
```

## Процедура: `GetSumInRub`

```rsl
GetSumInRub(Sum:MoneyL, CurrCode:Integer):MoneyL
```

## Процедура: `MakeCodeCurr`

```rsl
MakeCodeCurr(ISO:Integer):String
```

## Процедура: `ЗаполнитьСменыКурсов`

```rsl
ЗаполнитьСменыКурсов(BeginDate:Date, EndDate:Date):Integer С помощью процедуры заполняется временная таблица смен курсов валют, созданных в течение заданного периода.
```

**Параметры:**

BeginDate – дата начала периода, за который были сформированы смены курсов валют.
EndDate – дата окончания периода, за который были сформированы смены курсов валют.

**Возвращаемое значение:**



## Класс: `RslTMtSystem`

```rsl
RslTMtSystem ()
```

## Класс: `TMtOperationBase`

```rsl
TMtOperationBase ()
```

## Класс: `TMtOpHistory`

```rsl
TMtOpHistory ()
```

## Класс: `TMtTransfer`

```rsl
TMtTransfer ()
```

## Процедура: `CNG_ChooseMethodForSelect`

```rsl
CNG_ChooseMethodForSelect(method:Integer):Bool
```

## Процедура: `CNG_SelectPersistClient`

```rsl
CNG_SelectPersistClient(clientId:Integer, [clientCode:String], [birthDate:Date]):Bool
```

## Процедура: `CNG_SelectRecPoint`

```rsl
CNG_SelectRecPoint(id:Integer, [currCode:Integer]):Bool
```

## Процедура: `CNG_SelectTemplate`

```rsl
CNG_SelectTemplate(clientId:Integer, transId:Integer, [PSTransId:Integer]):Bool
```

## Процедура: `CNG_ShowFeature`

```rsl
CNG_ShowFeatures(subjectType:Integer, subjectCode:Integer, [needSearch:Bool])
```

## Процедура: `getCurrentOpHistory`

```rsl
getCurrentOpHistory ():Object
```


```rsl
позволяет получить объект операции по денежному переводу, для которого запущена процедура печати отчета.
```

**Пример:**

private var opHistoryReport = getCurrentOpHistory( );
private var sb_casln = Tbfile( "sb_casln.dbt", "r", 0 );
...
 sb_casln.KeyNum = 1;
 sb_casln.Clear;
 sb_casln.rec.ApplicationKind2 =
opHistoryReport.rec.opApplicationKind;
 sb_casln.rec.ApplicationKey2  =
opHistoryReport.rec.opApplicationKey;
 sb_casln.rec.RefValue2 = 0;
 if ( sb_casln.GetEQ )
...

## Процедура: `getCurrentTransfer`

```rsl
getCurrentTransfer ():Object
```

## Процедура: `MT_OperationExecution`

```rsl
MT_OperationExecution ([psId:Integer] [, opNum:Integer] [, subOpNum:Integer] [, refDepAcc:Integer]):Integer
```

## Процедура: `SelectUniqClient`

```rsl
SelectUniqClient(id:Integer, f:String, i:String, [o:String], [birthDate:Date])
```

## Класс: `CRslPercent`

```rsl
С помощью объекта класса CRslPercent определяется, на каком этапе вызвана пользовательская макрофункция расчета процентов и налога. Объект класса CRslPercent содержит входные данные, необходимые для работы с: · Reference – референс счета. · ObjectType – условия расчета (2001, 2002, 2003, 2004). · BeginDate, EndDate – даты начала и конца периода расчета. · PcAlg – условия расчета процентов. Членами объекта класса CRslPercent являются списки: · RateList – список ставок, объект класса CRslPcList. · RestList – список остатков, объект класса CRslPcList. · PeriodList – список периодов, объект класса CRslPcList. · TaxList – список записей налоговой карточки, объект класса CRslPcList. Свойства класса CRslPercent Для класса CRslPercent реализованы следующие свойства: BeginDate – дата начала периода расчета процентов; тип Date. EndDate – дата окончания периода расчета процентов; тип Date. ListKind – тип обрабатываемого списка; тип Integer. Свойство может принимать следующие значения: · UPC_RateList – ставки. · UPC_RestList – остатки. · UPC_PeriodList – периоды расчета процентов (на этапе работы с периодами расчета процентов доступны списки периодов, ставок, остатков; в остальных случаях доступен только один соответствующий список). · UPC_TaxList – налоговая карточка. Mode – свойства определяет, до или после системных действий вызвана макрофункция. Свойство может принимать следующие значения: · UPC_Make – создание списка (до системных действий). · UPC_Correct – коррекция списка (после системных действий). ObjectType – условия расчета процентов; тип Integer. Свойство может принимать следующие значения: · 2001 – при выполнении условий договора (основные условия); · 2002 – при нарушении условий договора (альтернативные условия); · 2003 – при возникновении овердрафта; · 2004 – в случае дополнительных взносов. PeriodList – список периодов (объект класса CRslPcList ); тип Object. RateList – список ставок (объект класса CRslPcList); тип Object. Reference – референс счета; тип Integer. RestList – список остатков (объект класса CRslPcList); тип Object. TaxList – список записей налоговой карточки (объект класса CRslPcList); тип Object. Методы класса CRslPercent Для класса CRslPercent реализован метод: PcAlg():TRecHandler
```

## Класс: `CRslPcList`

```rsl
Объекты класса CRslPcList позволяют перемещаться по спискам ставок, остатков, периодов и записей налоговой карточки и корректировать их элементы. Свойства класса CRslPcList Для класса CRslPcList реализованы следующие свойства: ListKind – вид списка; тип Integer. Свойство может принимать следующие значения: · UPC_RateList – ставки. · UPC_RestList – остатки. · UPC_PeriodList – периоды расчета процентов (на этапе работы с периодами расчета процентов доступны списки периодов, ставок, остатков; в остальных случаях доступен только один соответствующий список). · UPC_TaxList – налоговая карточка. NumItems – число элементов в списке; тип Integer. Методы класса CRslPcList В классе CRslPcList реализованы следующие методы: First
```

## Процедура: `CreatePcObject`

```rsl
CreatePcObject():Objeсм
```

## Процедура: `GetCalcStrategy`

```rsl
GetCalcStrategy(Reference:Integer, Date:Date [, NextPeriodFlag:String], PeriodEndDate:Date):Integer
```

## Процедура: `GetProlongDateForCurDate`

```rsl
GetProlongDateForCurDate(Reference:Integer, Date:Date, ContractStartDate:Date)
```

## Процедура: `PcSetManualData`

```rsl
PcSetManualData(newCalcDataFlag:Bool, newPutDataFlag:Bool, nextPeriodFlag:Bool, manualData_dep:Record, TRecHandler [, manualData_alt:Record, TRecHandler], manualData_add:Record, TRecHandler):Bool
```

## Процедура: `PercRateAL`

```rsl
PercRateAL (Referenc: Integer, ObjectType: Integer, RateDate: Date [, Rest:MoneyL]):Double
```

## Процедура: `PercRateTL`

```rsl
PercRateTL(DepType:String [, CurrCode:Integer] [, Date:Date] [, Rest:MoneyL]):Double
```

## Процедура: `ВыполнитьРегламентныеФункции`

```rsl
ВыполнитьРегламентныеФункции (Referenc: Integer, LimitDate, NeedErrorMessage: Integer): Date
```


```rsl
предназначена для выполнения регламентных операций независимо от настройки параметра RS-RETAIL\ СЕРВИСНЫЕ\ ВКЛАДЫ\ ПРОЦЕНТЫ\ РЕГЛАМЕНТНЫЕ_ОПЕРАЦИИ, который определен в справочнике настроек ИБС подсистемы "Сервис розничных услуг". Под регламентными понимаются операции, которые должны автоматически выполняться в соответствии с определенным графиком (пролонгация/завершение договора, расчет/оплата процентов и пр.).
```

**Параметры:**

Referenc – референс счета.
LimitDate – дата окончания периода, в течение которого будут выполнены регламентные
операции. Дата окончания периода не включается в этот период. По умолчанию
значение параметра принимается равным текущей системной дате.
NeedErrorMessage – признак необходимости вывода на экран системного сообщения об
ошибке, которая возникла в результате выполнения регламентных операций:
- 0 – сообщение об ошибке не выводится;
- 1 – в случае обнаружения ошибки выводится соответствующее системное
сообщение.
Внимание!
Сообщение об ошибке выводится при ее обнаружении на этапе
выполнения конкретной регламентной операции. Поэтому возможна
ситуация, когда группа регламентных операций была корректно
выполнена до обнаружения ошибки.

**Возвращаемое значение:**



## Процедура: `ДатыРасчетовДляВидовВкладов`

```rsl
ДатыРасчетовДляВидовВкладов(Type_Account:String):Integer
```

## Процедура: `Начисление_Отчисление_Процентов`

```rsl
Начисление_Отчисление_Процентов (Referenc: Integer, DepDate_Document: Date, CorrectSum: Money, ObjectType: Integer): Integer
```

## Процедура: `Отменить_Выдачу_Процентов`

```rsl
Отменить_Выдачу_Процентов (Referenc: Integer, BeginDate: Date, EndDate: Date): Integer
```

## Процедура: `Отчисление_Процентов`

```rsl
Отчисление_Процентов (Account: String, AccType: String, Code_Currency: Integer, PercSum: MoneyL, Date: Date [, ObjectType: Integer]): Integer
```

## Процедура: `Отчислить_Проценты_За_Период`

```rsl
Отчислить_Проценты_За_Период (Referenc:Integer [, ObjectType:Integer [, BeginDate:Date [, EndDate:Date [, OnlyCalc:Bool]]]], SumDeductPercent:MoneyL, SumDeductTax:MoneyL [, DeductPcFromSourceIfOver:Bool]):Integer С помощью процедуры осуществляется отчисление процентов со счета вкладчика за заданный период. Период, за который будут отчислены проценты, определяется датами учета процентов, а не датами фактической проводки операции причисления.
```

**Параметры:**

Referenc – референс счета.
ObjectType – условия, по которым ранее были причислены проценты:
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов;
- 0 – все возможные условия (по умолчанию).
BeginDate – дата начала периода, за который ранее были причислены проценты по
вкладу. 
По 
умолчанию 
значение 
параметра 
принимается 
равным 
дате
пролонгации договора по счету. В случае если дата пролонгации договора равна
"00.00.0000", то значение параметра принимается равным дате начала договора
по счету. Если же и дата начала договора по счету равна "00.00.0000", то
значение параметра принимается равным дате начала периода начисления
процентов по счету. Возможно, что дата начала периода начисления процентов
меньше или равна критической дате, тогда значение параметра принимается
равным дате, следующей за критической.
EndDate – дата окончания периода, за который ранее были причислены проценты по
вкладу. По умолчанию значение параметра принимается равным дате окончания
периода начисления процентов.
Внимание!
Дата начала и дата окончания периода не должна быть меньше или
равна критической дате, до которой не проводились операции в
системе. В случае невыполнения этого условия заданные параметры
автоматически 
корректируются 
с 
учетом 
критической 
даты.
Критическая дата определяется переменной Limit_Date в таблице
ddepositr_dbt.
OnlyCalc – признак необходимости проводки суммы процентов, подлежащих отчислению:
- TRUE – в результате выполнения процедуры осуществляется только расчет
суммы отчисляемых процентов.
- FALSE (по умолчанию) – в результате выполнения процедуры осуществляется
расчет и проводка суммы процентов, подлежащих отчислению.
SumDeductPercent (выходной параметр) – сумма процентов, которая была отчислена в
результате выполнения процедуры.
SumDeductTax (выходной параметр) – сумма налога на материальную выгоду, которая
была возвращена в результате выполнения процедуры.

**Примечание:**

Тип всех сумм MoneyL, соответствующая константа – $0l.
DeductPcFromSourceIfOver – признак возможности списания процентов с исходного
счета, если счет получателя процентов отличен от исходного, причем после
списания процентов со счета получателя образуется отрицательный остаток.
Параметр может принимать следующие значения:
- TRUE – в результате выполнения процедуры осуществляется отчисление
процентов с исходного счета, если счет получателя процентов отличен от
заданного параметром Referenc и на счете получателя процентов после
списания образуется отрицательный остаток.
- FALSE (по умолчанию) – в случае возникновения овердрафта по счету
получателя процентов после списания процентов, отчисление процентов
выполнено не будет и процедура возвратит ненулевое значение.

**Возвращаемое значение:**



## Процедура: `Параметры_Выпуска_Налоговой_Карточки`

```rsl
Параметры_Выпуска_Налоговой_Карточки([Caption:String] [, ChangeClient:Bool] [, ChangeYear:Bool] [, ClientCode:Integer] [, Year:Integer]):Bool
```

## Процедура: `Перенос_Остатков`

```rsl
Перенос_Остатков (Account: String, AccType: String, Code_Currency: Integer, destType: Integer, sourceType: Integer, begDate: Date, endDate: Date [, Summa: MoneyL]): Integer
```

## Процедура: `Пересчет_Процентов_По_Ставке_Рефинанси`

```rsl
рования Пересчет_Процентов_По_Ставке_Рефинансирования (referenc:Integer, objectType:Integer [, beginDate:Date] [, endDate:Date]):MoneyL
```

## Процедура: `Прогноз_процентов`

```rsl
Прогноз_процентов (referenc:Integer [, endDate:Date] [, needDeductPercent:Bool] [, sumPercent:MoneyL] [, sumDeductPercent:MoneyL] [, sumDeductTax:MoneyL]):Integer
```

## Процедура: `Процентов_К_Выдаче`

```rsl
Процентов_К_Выдаче (Account: String, AccType: String, Code_Currency: Integer, PercOutSum: MoneyL): Integer
```

## Процедура: `Проценты_К_Оплате_По_Конвертору`

```rsl
Проценты_К_Оплате_По_Конвертору (Referenc:Integer [, ObjectType:Integer [, EndDate:Date]], SumPay:MoneyL, TaxSumForPay:MoneyL, SumForPay:MoneyL, FactEndDate:Date):Integer С помощью процедуры на основании записей, содержащихся в таблице dauxinfo_dbt, определяются суммы: · процентов, оплаченных за всю историю счета; · процентов к оплате; · налога к оплате. Эта процедура аналогична процедуре Проценты_Налог_К_Оплате , отличие заключается в обработке данных только за прошлые периоды, которые были получены в результате конвертации.
```

**Параметры:**

Referenc – референс счета.
ObjectType – условия расчета процентов:
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов;
- 0 – все возможные условия (по умолчанию).
EndDate – дату, по состоянию на которую будут определены суммы процентов и налога.
По умолчанию значение параметра принимается равным соответствующему
полю последней записи в таблице dpc__calc_dbt.
SumForPay (выходной параметр) – сумма процентов к оплате.
SumPay (выходной параметр) – сумма процентов, оплаченных за всю историю счета.
TaxSumForPay (выходной параметр) – сумма налога к оплате.

**Примечание:**

Тип всех сумм MoneyL, соответствующая константа – $0l.
FactEndDate (выходной параметр) – дата, по состоянию на которую были определены
суммы процентов и налога. Значение параметра определяется на основании
даты окончания периода, содержащейся в таблице dpc__calc_dbt. Если значение
параметра ObjectType равно "0", то в качестве значения параметра FactEndDate
возвращается максимальная из дат, рассчитанных по всем возможным условиям.
В случае успешного завершения процедуры значение параметра FactEndDate не
превышает значения параметра EndDate.

**Возвращаемое значение:**



## Процедура: `Проценты_На_Операцию`

```rsl
Проценты_На_Операцию (Account: String, AccType: String, Code_Currency: Integer, OperSum: MoneyL, PercSum: MoneyL, begDate: Date [, endDate: Date [, ObjectType: Integer [, Save: Integer]]]): Integer С помощью процедуры рассчитываются проценты на сумму операции по счету вкладчика.
```

**Параметры:**

Account – номер счета вкладчика.
AccType – вид вклада, к которому относится счет вкладчика.
Code_Currency – код валюты счета вкладчика.
OperSum – сумма операции, на которую будут рассчитаны проценты.
PercSum (выходной параметр) – сумма процентов, которая была рассчитана в результате
выполнения процедуры.
begDate – дата начала периода, за который будет выполнен расчет процентов.
endDate – дата окончания периода, за который будет выполнен расчет процентов. Если
параметр не задан, то его значение принимается равным переменной MAXDATE.
ObjectType – условия расчета процентов:
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов.
По умолчанию значение параметра принимается равным "2001".
Save – признак необходимости сохранения результатов расчета процентов в таблицу
базы данных dpc__calc_dbt. По умолчанию результаты расчета процентов не
сохраняются.

**Возвращаемое значение:**



## Процедура: `Проценты_Налог_К_Оплате`

```rsl
Проценты_Налог_К_Оплате (Referenc: Integer [, ObjectType: Integer [, EndDate: Date]], SumForPay: MoneyL, SumPay: MoneyL, TaxSumForPay: MoneyL, FactEndDate: Date): Integer С помощью процедуры на основании записей, содержащихся в таблице, описанной во внутреннем словаре как dpc__calc_dbt, определяются суммы: · процентов, оплаченных за всю историю счета; · процентов к оплате; · налога к оплате.
```

**Параметры:**

Referenc – референс счета.
ObjectType – условия расчета процентов: 
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов;
- 0 – все возможные условия (по умолчанию).
EndDate – дата, по состоянию на которую будут определены суммы процентов и налога.
По умолчанию значение параметра принимается равным соответствующему
полю последней записи в таблице, описанной во внутреннем словаре как
dpc__calc_dbt.
SumForPay (выходной параметр) – сумма процентов к оплате.
SumPay (выходной параметр) – сумма процентов, оплаченных за всю историю счета.
TaxSumForPay (выходной параметр) – сумма налога к оплате.

**Примечание:**

Тип всех сумм MoneyL, соответствующая константа – $0l.
FactEndDate (выходной параметр) – дата, по состоянию на которую были определены
суммы процентов и налога. Значение параметра определяется на основании
даты окончания периода, содержащейся в таблице, описанной во внутреннем
словаре как dpc__calc_dbt. Если значение параметра ObjectType равно "0", то в
качестве значения параметра FactEndDate возвращается максимальная из дат,
рассчитанных по всем возможным условиям. В случае успешного завершения
процедуры значение параметра FactEndDate не превышает значения параметра
EndDate.

**Возвращаемое значение:**



## Процедура: `Проценты_Налог_К_Оплате_Учет_Конв`

```rsl
Проценты_Налог_К_Оплате_Учет_Конв (Referenc: Integer [, ObjectType: Integer [, EndDate: Date]], SumForPay: MoneyL, SumPay: MoneyL, TaxSumForPay: MoneyL, FactEndDate: Date): Integer С помощью процедуры на основании записей, содержащихся в таблицах, описанных во внутреннем словаре как dpc__calc_dbt и dauxinfo_dbt, определяются суммы: · процентов, оплаченных за всю историю счета; · процентов к оплате; · налога к оплате. Эта процедура аналогична процедуре Проценты_Налог_К_Оплате , отличие заключается в обработке данных с учетом прошлых периодов, которые были получены в результате конвертации.
```

**Параметры:**

Referenc – референс счета.
ObjectType – условия расчета процентов:
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов;
- 0 – все возможные условия (по умолчанию).
EndDate – дата, по состоянию на которую будут определены суммы процентов и налога.
По умолчанию значение параметра принимается равным соответствующему
полю последней записи в таблице, описанной во внутреннем словаре как
dpc__calc_dbt.
SumForPay (выходной параметр) – сумма процентов к оплате.
SumPay (выходной параметр) – сумма процентов, оплаченных за всю историю счета.
TaxSumForPay (выходной параметр) – сумма налога к оплате.

**Примечание:**

Тип всех сумм MoneyL, соответствующая константа – $0l.
FactEndDate (выходной параметр) – дата, по состоянию на которую были определены
суммы процентов и налога. Значение параметра определяется на основании
даты окончания периода, содержащейся в таблице, описанной во внутреннем
словаре как dpc__calc_dbt. Если значение параметра ObjectType равно "0", то в
качестве значения параметра FactEndDate возвращается максимальная из дат,
рассчитанных по всем возможным условиям. В случае успешного завершения
процедуры значение параметра FactEndDate не превышает значения параметра
EndDate.

**Возвращаемое значение:**



## Процедура: `Расчет_Налога_По_Счету_Вкладчика`

```rsl
Расчет_Налога_По_Счету_Вкладчика (Referenc: Integer [, ObjectType: Integer], BeginDate: Date, EndDate: Date [, NeedWriteToFile: Bool [, ClearOldListTaxCard: Bool]], TaxSum: MoneyL [, BeginDateIsAbs: Bool [, EndDateIsAbs: Bool [, UseFollContrFileDoc: Bool [, TakeNoNoticeOfGlobalParam: Bool]]]]): Integer С помощью процедуры рассчитывается налог на материальную выгоду по счету. Материальная выгода по счету определяется на основании разности процентной ставки по вкладу и ставки рефинансирования. Также с помощью процедуры может таблица, описанная во внутреннем словаре как dpc_tax_dbt, в котором содержатся данные налоговой карточки вкладчика.
```

**Параметры:**

Referenc – референс счета.
ObjectType – условия расчета процентов:
- 2001 – при выполнении условий договора (основные условия);
- 2002 – при нарушении условий договора (альтернативные условия);
- 2003 – при возникновении овердрафта;
- 2004 – в случае дополнительных взносов;
- 0 – все возможные условия (по умолчанию).
BeginDate – дата начала периода, за который будет выполнен расчет налога на
материальную выгоду.
EndDate – дата окончания периода, за который будет выполнен расчет налога на
материальную выгоду.
Внимание!
Дата начала и дата окончания периода не должна быть меньше
критической даты, до которой не проводились операции в системе. В
случае 
невыполнения 
этого 
условия 
заданные 
параметры
автоматически 
корректируются 
с 
учетом 
критической 
даты.
Критическая дата определяется переменной Limit_Date в таблице,
описанной во внутреннем словаре как ddepositr_dbt.
NeedWriteToFile – 
признак 
необходимости 
заполнения 
таблицы, 
описанной 
во
внутреннем словаре как dpc_tax_dbt, в котором содержатся данные налоговой
карточки вкладчика. Параметр может принимать следующие значения:
- TRUE – результаты выполнения процедуры будут отражены в налоговой
карточке вкладчика.
- FALSE (по умолчанию) – результаты выполнения процедуры не будут
отражены в налоговой карточке вкладчика, т.е. будет выполнен прогноз расчета
налога без заполнения базы данных.
ClearOldListTaxCard – признак необходимости отражения в налоговой карточке данных о
расчете налога за определенный период без учета ранее выполненных расчетов
за этот же период. Параметр имеет смысл, только если значение параметра
NeedWriteToFile равно "True". Параметр может принимать следующие значения:
- TRUE – данные о расчете налога за заданный период будут отражены в
налоговой карточке вкладчика без учета ранее выполненных расчетов за этот
же период. В этом случае автоматически удаляются все прежние записи о
расчете налога за заданную дату, содержащиеся в таблице, описанной во
внутреннем словаре как dpc_tax_dbt. Фактически формируется новая налоговая
карточка за заданный период с определением новых периодов расчета налога.
- FALSE (по умолчанию) – данные о расчете налога будут отражены в налоговой
карточке вкладчика с учетом ранее сформированных периодов расчета.
TaxSum (выходной параметр) – сумма налога, рассчитанная в результате выполнения
процедуры; соответствующая константа – $0l. 
BeginDateIsAbs – признак необходимости корректировки даты начала периода расчета
налога. Параметр может принимать следующие значения:
- TRUE – заданная дата начала периода не корректируется с учетом ранее
выполненных расчетов налога и процентов. В этом случае дата начала периода
автоматически корректируется только с учетом критических параметров (не
меньше критической даты, даты окончания начисления процентов по счету и
пр.). 
Если 
параметр 
NeedWriteToFile 
принимает 
значение 
"True", 
то
правильность задания даты начала периода определяется только параметрами
процедуры.
- FALSE (по умолчанию) – заданная дата начала периода автоматически
корректируется с учетом ранее выполненных расчетов налога и процентов.
EndDateIsAbs – признак необходимости корректировки даты окончания периода расчета
налога:
- TRUE – заданная дата окончания периода не корректируется с учетом ранее
выполненных расчетов налога и процентов. В этом случае дата окончания
периода корректируется только с учетом критических параметров (не меньше
критической даты, не больше даты окончания начисления процентов по счету и
пр.).
- FALSE (по умолчанию) – заданная дата окончания периода автоматически
корректируется с учетом ранее выполненных расчетов налога и процентов.
UseFollContrFileDoc – признак необходимости расчета налога на основании проверочной
истории Последующего контроля, содержащейся в таблице, которая описана во
внутреннем словаре как dfcdepdoc_dbt. Параметр может принимать следующие
значения:
- TRUE
- 
налог 
рассчитывается 
на 
основании 
проверочной 
истории
Последующего контроля, содержащейся в таблице, которая описана во
внутреннем словаре как dfcdepdoc_dbt.
- FALSE (по умолчанию) – налог рассчитывается на основании рабочей истории
операций по вкладу, содержащейся в таблице, которая описана во внутреннем
словаре как dsbdepdoc_dbt.
TakeNoNoticeOfGlobalParam – признак необходимости учета параметра ФОРМИРОВАТЬ
НАЛОГОВУЮ КАРТОЧКУ, заданного в справочнике видов вкладов. Параметр
может принимать следующие значения:
- TRUE – процедура выполняется без учета параметра ФОРМИРОВАТЬ
НАЛОГОВУЮ КАРТОЧКУ (по умолчанию). В случае вызова этой процедуры из
макроса будет рассчитан налог и сформирована налоговая карточка
независимо от установленных в справочнике параметров вида вклада.
- FALSE (по умолчанию) – процедура выполняется с учетом параметра
ФОРМИРОВАТЬ НАЛОГОВУЮ КАРТОЧКУ. Расчет налога и формирование
налоговой карточки будет осуществлено только, если в справочнике для этого
вида вкладов действуют соответствующие признаки.

**Возвращаемое значение:**



## Процедура: `УстановитьДатыСменыСтавок`

```rsl
УстановитьДатыСменыСтавок(RateGroup:String [, LastChangeDate:Date]):Integer
```

## Процедура: `CalcTariffForTariffPlan`

```rsl
CalcTariffForTariffPlan(TPID:Integer, TariffKind:Integer, CurrCode:Integer, BaseAmount:Money [, LinkType:String] [, Branch:Integer] [, Date:Date]. TariffAmount:Money):Integer
```

## Процедура: `CloseFileSvdWrk`

```rsl
CloseFileSvdWrk()
```

## Процедура: `CNVPackPayedTran`

```rsl
CNVPackPayedTran(execID:Integer, packetID:Integer, [dateDoc:Integer], [flagEndDay:Bool], [flagUseBorrowedFunds:Bool]):Integer
```

## Процедура: `CreateNewCrdSubAccdoc`

```rsl
CreateNewCrdSubAccDoc(link:File, Record, TRecHandler, depdoc:File, Record, TRecHandler):Bool
```

## Процедура: `GetCardSubAccRest`

```rsl
GetCardSubAccRest(Branch:Integer, AccCardLinkRef:Long [, DocDate:Date]):MoneyL
```

## Процедура: `GetCardUndividedRest`

```rsl
GetCardUndividedRest(Reference:Long [, DateFind:Date]):MoneyL
```

## Процедура: `GetInSumUnconfDocSubAcc`

```rsl
GetInSumUnconfDocSubAcc(branch:Integer, linkRef:Integer):Money
```

## Процедура: `InitNewCrdSubAccDoc`

```rsl
InitNewCrdSubAccDoc(link:File, Record, TRecHandler):Bool
```

## Процедура: `MultySelectCardProduct`

```rsl
MultySelectCardProduct(сardProdList:Array, [psRef:Integer]):Integer
```

## Процедура: `OpenFileSvdWrk`

```rsl
OpenFileSvdWrk():Integer
```

## Процедура: `RetrieveSubAccForCarry`

```rsl
RetrieveSubAccForCarry(accReference:Integer):Integer
```

## Процедура: `RSL_InsertCrdSubAccDocToGDDList`

```rsl
RSL_InsertCrdSubAccDocToGDDList():Bool
```

## Процедура: `RunPlasticCardOperation`

```rsl
RunPlasticCardOperation(CardNFOParm:Record):Integer
```

## Процедура: `scDefReferCard`

```rsl
scDefReferCard (): Integer
```

## Процедура: `scDefReferGrProp`

```rsl
scDefReferGrProp (): Integer
```

## Процедура: `scDefReferLGrPr`

```rsl
scDefReferLGrPr (): Integer
```

## Процедура: `scDefReferLink`

```rsl
scDefReferLink (): Integer
```

## Процедура: `scDefReferMail`

```rsl
scDefReferMail (): Integer
```

## Процедура: `scDefReferMailIt`

```rsl
scDefReferMailIt (): Integer
```

## Процедура: `scDefReferProp`

```rsl
scDefReferProp (): Integer
```

## Процедура: `scDefReferTran`

```rsl
scDefReferTran (): Integer
```

## Процедура: `scEditCardCtr`

```rsl
scEditCardCtr (Branch:Integer, Id:Integer [, Allow:Integer]):Integer
```

## Процедура: `scGetCurrentMayWorkWithClose`

```rsl
scGetCurrentMayWorkWithClose (): Bool С помощью процедуры определяется возможность работы пользователя с закрытыми объектами (карточками, счетами и т.д.).
```

**Возвращаемое значение:**



## Процедура: `scGetCurrentPaymentSystem`

```rsl
scGetCurrentPaymentSystem (): Integer
```

## Процедура: `scGetCurrentSetOperLog`

```rsl
scGetCurrentSetOperLog (): Bool С помощью процедуры определяется признак необходимости записи в журнал аудита измененной информации при работе с карточной системой.
```

**Возвращаемое значение:**



## Процедура: `scGetLinkTypeCode`

```rsl
scGetLinkTypeCode(AcqCode:String):String
```

## Процедура: `scGetSumDocForTran`

```rsl
scGetSumDocForTran (RecTran: Object, SumTran: MoneyL, KindTran: Integer): Bool
```

## Процедура: `scGetTariffPlanID`

```rsl
scGetTariffPlanID (ApplicationKind:Integer, [WhereCond:String]):Integer
```

## Процедура: `scPackPayedTranForGZ`

```rsl
scPackPayedTranForGZ(isViewReport:Bool [, dateDoc:Date] [, numPack:Integer] [, printForm52:Bool] [, flagSettlementOverDebt:Bool] [, isEndDay:Bool] [, isEndDay:Bool]):Bool
```

## Процедура: `scStoreSubAccRef`

```rsl
scStoreSubAccRef(ApplicationKind:Integer, ApplicationKey:String, Branch:Integer, AccCardLinkRef:Integer)
```

## Процедура: `StoreSubAccForCarry`

```rsl
StoreSubAccForCarry(card AccReference:Integer, linkRef:Integer):Bool
```

## Процедура: `ПоискКарточки`

```rsl
ПоискКарточки (cardRef: Integer, Branch: Integer, [PsRef: Integer], [CardHolderCode: Integer], [PaySysId: Integer], [fieldsCloseFlag: Integer]): Bool
```

## Процедура: `DateAfterCalenDays`

```rsl
DateAfterCalenDays (d: Date, offset: Integer): Date
```

## Процедура: `DateAfterCalenMonths`

```rsl
DateAfterCalenMonths (d: Date, offset: Integer): Date
```

## Процедура: `DateAfterWorkDays`

```rsl
DateAfterWorkDays (d:Date, offset:Integer): Date
```

## Процедура: `DateAfterWorkMonths`

```rsl
DateAfterWorkMonths (d: Date, offset: Integer): Date
```

## Процедура: `IsHolyday`

```rsl
IsHoliday (d: Date): Integer
```

## Процедура: `IsWorkday`

```rsl
IsWorkday (d: Date): Integer
```

## Процедура: `NDays30`

```rsl
NDays30 (Date1: Date, [Date2: Date]): Integer
```

## Процедура: `Workdays`

```rsl
Workdays (startDate:Date, endDate:Date):Integer
```

## Класс: `TMdbRecordset`

```rsl
Для работы с менеджером записей памяти реализован класс TMdbRecordset. С помощью этого класса можно создавать наборы записей в памяти по описанию из внутреннего словаря системы и работать с ними, как с обычными таблицами базы данных. Работа с классом TMdbRecordset может быть осуществлена в программном коде, реализованном на языке RSL. Интерфейс класса TMdbRecordset аналогичен интерфейсу класса TBFile, за исключением следующих отличий: · Конструктор класса TMdbRecordset имеет другие параметры. TMdbRecordset (structName: String [, keyNum: Integer]) – метод создает незаполненную таблицу МЗП по структуре из словаря.
```

**Параметры:**

structName – имя структуры в словаре базы данных.
keyNum – номер ключа. По умолчанию значение параметра принимается равным 0.
- Метод getPos во всех случаях, в том числе и при работе на платформе Oracle,
возвращает значение типа Integer. Параметр метода getDirect всегда относится к типу
Integer.
- Методы packVarBuff/unpackVarBuff и readBlob/writeBlob не реализованы ввиду
отсутствия необходимости.
- Не поддерживается получение кода и описания последней ошибки операции с помощью
метода status.
- Вместо метода TRecHandler.setRecordAddr для наложения структуры на запись МЗП-
набора следует использовать метод класса TMdbRecordset.
overlayRecord (strName:String [, offset:Integer, isFixed:Bool]):TRecHandler

## Метод: `редназначен`

```rsl
для наложения структуры на запись МЗП-набора.
```

**Параметры:**

strName – имя накладываемой структуры в словаре.
offset – смещение относительно постоянной (для isFixed=true) или переменной (для
isFixed=false) части записи (по умолчанию – 0).
isFixed – вид записи, на которую накладывается структура:
- TRUE – структура накладывается на постоянную часть записи.
- FALSE (по умолчанию) – структура накладывается на переменную часть
записи.

**Возвращаемое значение:**



## Процедура: `вызывается`

```rsl
при перепозиционировании на другую запись списка. Параметр: rec/зап – адрес буфера новой записи. RecFilter (rec:Memaddr)
```

ФильтрЗаписей (rec:Memaddr)

## Класс: `RslDSAGRMNT`

```rsl
RslDSAGRMNT()
```

## Класс: `RslTBunch`

```rsl
RslTBunch()
```

## Класс: `RslTCellList`

```rsl
RslTCellList()
```

## Класс: `RslTContract`

```rsl
RslTContract ()
```

## Класс: `RslTContrClientList`

```rsl
RslTContrClientList ()
```

## Класс: `RslTOpClientList`

```rsl
RslTOpClientList ()
```

## Класс: `RslTOperation`

```rsl
RslTOperation ()
```

## Класс: `RslTOpFootprint`

```rsl
RslTOpFootprint ()
```

**Свойства:**

contractType – вид договора; тип Integer. Свойство доступно только для чтения.
opNumber – номер операции; тип Integer. Свойство доступно только для чтения.
oper – операционист (контролер), выполняющий операцию; тип Integer. Свойство
доступно только для чтения.
cashier – кассир; тип Integer.
status – состояние процесса отката операции; тип Bool:
- TRUE – успешно.
- FALSE – ошибка в процессе отката операции.
action – действие по операции (вид отката); тип Integer:
- D_STORN – сторнирование.
- D_DELETE – удаление.
contract – запись договора аренды; тип RslTContract.
Внимание!
Для операций, не требующих выбора договора, свойство доступно
только после вызова методов newContract, selectContract или
setContract.
bunch – список документов по операции; тип Object.

**Методы:**

Rollback (): Вool
Стандартные действия по откату операции:
- Вызывается процедура DeleteDocumentEx.
- При внешнем вызове транзакции автоматически организуется транзакция.

**Возвращаемое значение:**



## Класс: `RslTOpPenaltyList`

```rsl
RslTOpPenaltyList ()
```

## Класс: `RslTRollbackData`

```rsl
RslTRollbackData()
```

## Класс: `реализован`

```rsl
на языке С/С++ и не экспортируется в RSL. Этот класс представляет собой список элементов произвольного типа.
```

**Свойства:**

numItems – количество элементов в списке; тип Integer. Свойство класса доступно только
для чтения.
item – текущий элемент списка; тип Variant.

**Методы:**

first (): Bool
Указание первого элемента списка.

**Возвращаемое значение:**



## Процедура: `accessUI`

```rsl
accessUI (Operation:Object):Bool
```

## Процедура: `CreateObjectOfOperation`

```rsl
CreateObjectOfOperation ():Object
```

## Процедура: `CreateOpFootprintObject`

```rsl
CreateOpFootprintObject ():Object
```


```rsl
создает объект класса RslTOpFootprint , необходимый для печати.
```

**Возвращаемое значение:**



## Процедура: `CreateRollbackDataObject`

```rsl
CreateRollbackDataObject ():Object
```

## Процедура: `CheckClientsOnContrType`

```rsl
CheckClientsOnContrType(ContrTypeID: Integer, Branch: Integer, ContractID: Integer, clientList :OBJECT): Integer
```

## Процедура: `CheckRunOp`

```rsl
CheckRunOp(operationObj: OBJECT): Bool
```

## Процедура: `GetNumDaysBetwen2Dates`

```rsl
GetNumDaysBetwen2Dates (Date1:Date, Date2:Date):Integer
```

## Процедура: `GetNumOfKeys`

```rsl
GetNumOfKeys (Branch:Integer, SafeID:Integer, CellNumber:Integer):Integer
```

## Процедура: `GetSafeName`

```rsl
GetSafeName (Branch:Integer, SafeID:Integer):String
```

## Процедура: `PayrentPack`

```rsl
PayrentPack()
```
