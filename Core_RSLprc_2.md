---
title: Core_RSLprc_2
description: Документация RS-Bank
category: Документация
source: PDF-документация RS-Bank V.6
sections: 350
generated: true
---

## Процедура: `ActivAC`

```rsl
ActivAC ([valacnt:Variant, ] [ valCurrency: Variant, ] [ valdateT:Date, ] [ valdateB:Date, ] [, valchapt:Variant]):Integer
```

## Процедура: `DebetAC`

```rsl
DebetAC ([valacnt: Variant, ] [, valCurrency: Variant, ] [, valdateT:Date, ] [, valdateB:Date, ] [, valchapt: Variant]):Integer
```

## Процедура: `KreditAC`

```rsl
KreditAC ([valacnt: Variant], [valCurrency: Variant, ] [, aldateT:Date, ] [, aldateB:Date, ] [, alchapt: Variant]):Integer
```

## Процедура: `PassivAC`

```rsl
PassivAC ([valacnt:Variant] [, valCurrency:Variant] [, valdateT:Date] [, valdateB:Date] [, valchapt:Variant]):Integer
```

## Процедура: `RestAC`

```rsl
RestAC ([valacnt:Variant, ] [valCurrency: Variant, ] [, valdateT:Date, ] [valdateB:Date, ] [ valchapt: Variant]):Integer
```

## Процедура: `ActivBC`

```rsl
ActivBC ():Integer
```

## Процедура: `DebetBC`

```rsl
DebetBC ():Integer
```

## Процедура: `KreditBC`

```rsl
KreditBC ():Integer
```

## Процедура: `PassivBC`

```rsl
PassivBC ():Integer
```

## Процедура: `RegPairedAccountsC`

```rsl
RegPairedAccountsC ([iAccChapter:Integer, ] [szAccount:String, ] [iCode_Currency:Integer, ] [szReportFile:String, ] [iKindReport:Integer]):Integer
```

## Процедура: `RestBC`

```rsl
RestBC ():Integer
```

## Процедура: `SumSymbC`

```rsl
SumSymbC ([account:String, ] [currency:Integer, ] [beg_d:Date, ] [end_d:Date]):String
```

## Процедура: `CreateEKDocC`

```rsl
CreateEKDocC (Maket:String [, Date:Date] [, Chapter:Integer]):String В результате работы формируется таблицы dvdockey_dbt (для рублей и валюты используется одна и та же временная таблица). Созданная таблица имеет нулевой ключ, значение которого соответствует заданному макету. Для получения отсортированных в нужном порядке документов необходимо перебирать записи таблицы по указанному ключу.
```

**Параметры:**

Maket – порядок сортировки полей таблицы, содержит не более семи цифровых
символов. Каждый символ строки обозначает позицию в строке макета. Позиции
определяют поля документа, расположенные слева направо:
- 0 – номер главы;
- 1 – опеpационист;
- 2 – номер пачки;
- 3 – номер документа;
- 4 – сумма документа;
- 5 – вид операции;
- 6 – код валюты.
В каждую позицию макета необходимо ввести цифру (от 0 до 6), которая
означает, на каком месте при создании ключа будет стоять данное поле. Если в
позиции установлен 0, поле, соответствующее данной позиции, в сортировке
участвовать не будет.
Date – дата проводки документов. Если параметр не задан, в качестве даты проводки
используется дата текущего операционного дня.
Chapter – целочисленное значение номера главы балансового учета. Если параметр не
задан, то используется глава номер 1.

**Пример:**

CreateEKDocC ("012")
/* Пример сортировки по возрастанию номера опеpациониста
(символ "1" в позиции 1 – операционист). В пределах одного
операциониста – сортировка по возрастанию номера пачки
(символ "2" в 
позиции 
- пачка).
Остальные поля 
не
сортируются.
Для 
описанной 
сортировки 
можно 
также 
использовать
последовательность "023" или "034" (необходимо, чтобы в
позиции 1 символ был меньше, чем в позиции 2).

## Класс: `RsbRate`

```rsl
RsbRate ([asDouble:Double], [Point:Integer], [Scale:Integer]):Object
```

## Процедура: `ConvertSum`

```rsl
ConvertSum (Amount:MoneyL, Rate:Double, RateScale:Integer, RatePoint:Integer [, RateInv:Bool, String] [, FaceValue:MoneyL]):MoneyL
```

## Процедура: `ConvSum`

```rsl
ConvSum ([SumConv:MoneyL] [, Sum:MoneyL] [, Date:Date] [, FI_Code:Integer, String] [, FI_Code_Base:Integer, String] [, Type:Integer] [, MP:Integer] [, Section:Integer]):MoneyL
```

## Процедура: `ConvSumCross`

```rsl
ConvSumCross (SumConv:Moneyl, Sum:Moneyl, Date:Date, FIID_From:Integer, FIID_To:Integer):Bool
```

## Процедура: `ConvSumRate`

```rsl
ConvSumRate (BaseSum:MoneyL, ContrSum:MoneyL, Scale:Integer, Point:Integer, RevRate:String):Integer
```

## Процедура: `FI_CircInMarket`

```rsl
FI_CircInMarket (FI:Integer [, Date:Date]):Bool
```

## Процедура: `FI_DeleteAvoiriss`

```rsl
FI_DeleteAvoiriss(FIID:Integer):Integer
```

## Процедура: `FI_DeleteWarnt`

```rsl
FI_DeleteWarnt(FIID:Integer, Number:String, IsPartial:Bool):Integer
```

## Процедура: `FI_GetCouponOnDate`

```rsl
FI_GetCouponOnDate (fiid:Integer, date:Date, avoir:Record):Integer
```

## Процедура: `FI_GetNominal`

```rsl
FI_GetNominal (FIID:Integer, Nominal:Double, Money, NomFIID:Integer):Integer
```

## Процедура: `FI_GetStatus`

```rsl
FI_GetStatus (fiid:Integer, date:Date, err:Integer):Integer
```

## Процедура: `FI_InitAvoiriss`

```rsl
FI_InitAvoiriss(AvoirKind:Integer, FI:Fininstr, Iss:Avoiriss, Invst:Avrinvst):Integer
```

## Процедура: `FI_InitWarnt`

```rsl
FI_InitWarnt(IsPartial:Bool, FIID:Integer, warnt:FIWarnts):Integer
```

## Процедура: `FI_InsertAvoiriss`

```rsl
FI_InsertAvoiriss(FI:File, Record, Tbfile, Trechandler, Iss:File, Record, Tbfile, Trechandler, [Invst:File, Record, Tbfile, Trechandler,] DontSetDefaultNalogGroup:Bool, SetOnSrvDepo:Bool):Integer
```

## Процедура: `FI_InsertWarnt`

```rsl
FI_InsertWarnt(warnt:FIWarnts):Integer
```

## Процедура: `FI_IsAvoirissPartly`

```rsl
FI_IsAvoirissPartly ( FIID:Integer, rate:Double [, all_rate:Double]):Bool
```

## Процедура: `FI_IsAvrKindIndividual`

```rsl
FI_IsAvrKindIndividual (AvoirKind: Integer): Bool
```

## Процедура: `FI_IsBond`

```rsl
FI_IsBond (fiid:Integer, err:Integer):Bool
```

## Процедура: `FI_IsCouponPartly`

```rsl
FI_IsCouponPartly (FIID:Integer, Number_Coupon:String, rate:Double ):Bool
```

## Процедура: `FI_IsDeposReceipt`

```rsl
FI_IsDeposReceipt (FI:Integer, Record):Bool
```

## Процедура: `FI_IsISU`

```rsl
FI_IsISU (fiid:Integer, err:Integer):Bool
```

## Процедура: `FI_IsKSU`

```rsl
FI_IsKSU (fiid:Integer, err:Integer):Bool
```

## Процедура: `FI_IsOverValue`

```rsl
FI_IsOverValue (FI:Variant):Bool
```

## Процедура: `FI_IsQuoted`

```rsl
FI_IsQuoted (FI:Variant):Bool
```

## Процедура: `FI_IsReserve`

```rsl
FI_IsReserve (FI:Variant) [, Deprec:Bool]):Bool
```

## Процедура: `FI_IsShare`

```rsl
FI_IsShare ([fiid:Integer, ] [DeposReceiptAsShare:Bool, ] [err:Integer]):Bool
```

## Процедура: `FI_UpdateAvoiriss`

```rsl
FI_UpdateAvoiriss(FI:Fininstr, Iss:Avoiriss, Invst:Avrinvst):Integer
```

## Процедура: `FI_UpdateWarnt`

```rsl
FI_UpdateWarnt(warnt:FIWarnts):Integer
```

## Процедура: `GetNominalValuePaym`

```rsl
GetNominalValuePaym (PAYM:Record, Nominal:MoneyL, NomFIID:Integer):Integer
```

## Процедура: `ListAvoiriss`

```rsl
ListAvoiriss (AvoirKind:Integer [, fi_rec: Record, TRecHandler] [, av_rec:Record, TRecHandler] [, ViewOpenAndClose:Bool] [, AdditionalFromTable:String] [, AdditionalWhereCond:String] [, BO:Integer]):Bool
```

## Процедура: `ListAvrKindsTree`

```rsl
ListAvrKindsTree(FI_Kind:Integer [, AvrKinds_rec:Record, TRecHandler] [, WhereCond:String] [, AllowChoiceHeader:Bool]):Bool
```

## Процедура: `ListFI`

```rsl
ListFI (FI_Kind:Integer, Avoir_Kind:Integer, FinInstr:File, Record [, AvoirIss:File, Record], Article:File, Record):Integer
```

## Процедура: `ИндивидуальныйФинИн`

```rsl
ИндивидуальныйФинИн (code:Integer, String [, error: Integer]): Integer
```

## Процедура: `ПолучитьЗначениеКурса`

```rsl
ПолучитьЗначениеКурса ([RATEDEF:File, Record, ] [Date:Date]):Integer
```

## Процедура: `ПолучитьЗначениеКурсаЦб`

```rsl
ПолучитьЗначениеКурсаЦб (FIID:Integer, Rate:Double, OtherFIID:Integer, Type:Integer, MP:Integer, Section:Integer, Date:DateTime, M:Integer, C:Integer):Integer
```

## Процедура: `ПолучитьИмяФинИн`

```rsl
ПолучитьИмяФинИн ([Код:Integer, String,] [КодОшибки:Integer]):Integer
```

## Процедура: `ПолучитьКодФинИн`

```rsl
ПолучитьКодФинИн ([Код:Integer, String] [, КодОшибки:Integer]):Integer
```

## Процедура: `ПолучитьКодФинИнДляСчета`

```rsl
ПолучитьКодФинИнДляСчета ([Код:Integer, String] [, КодВНомереСчета:Integer]):Integer
```

## Процедура: `ПолучитьКурс`

```rsl
Существует три варианта вызова данной процедуры (в зависимости от количества передаваемых параметров): ПолучитьКурс ([RATEDEF: Integer] [, RateID:Integer]):Integer ПолучитьКурс ([RATEDEF: Integer] [, FIID: Integer, String] [, OtherFI: Integer, String] [, Type:Integer]):Integer ПолучитьКурс ([RATEDEF: Integer] [, FIID: Integer, String] [, OtherFI: Integer, String] [, Type:Integer] [, MP:Integer] [, Section:Integer]):Integer
```

## Процедура: `ПолучитьНеэмиссионныйФинИн`

```rsl
ПолучитьНеэмиссионныйФинИн (FI_Kind:Integer, AvoirKind:Integer [, fi/FIID:Record]):Bool
```

## Процедура: `ПолучитьСистемныйВыпускФинИн`

```rsl
ПолучитьСистемныйВыпускФинИн (FI_Kind:Integer, AvoirKind:Integer, fiid:Integer):Bool
```

## Процедура: `ПолучитьСтрокуЗначенияКурса`

```rsl
ПолучитьСтрокуЗначенияКурса ():Integer
```

## Процедура: `ПолучитьФинИн`

```rsl
ПолучитьФинИн (Код:Integer, String [, ФинИн:File, Record, TRecHandler] [, ЦеннаяБумага: File, Record, TRecHandler] [, ДрагМеталл:File, Record, TRecHandler] [, ТекущийКупон:File, Record, TRecHandler], ВидКода:Integer]):Integer
```

## Процедура: `ПолучитьФинИнПоISO`

```rsl
ПолучитьФинИнПоISO (Ccy:Variant, fininstr:Record):Bool
```

## Процедура: `СледующееЗначениеКурса`

```rsl
СледующееЗначениеКурса ():Integer
```


```rsl
СледующееЗначениеКурса (RATEDEF:Object):Integer
```

## Процедура: `УстановитьКурс`

```rsl
УстановитьКурс ([RateParm:Record]):Integer
```

## Класс: `RsbFsspAccequire`

```rsl
RsbFsspAccequire
```

## Метод: `подготовки`

```rsl
записи для вставки нового значения. SetStdPriority ()
```

## Метод: `установки`

```rsl
счетам приоритета. Update ():Integer
```

## Класс: `RsbFsspDoubler`

```rsl
RsbFsspDoubler
```

## Класс: `RsbFssRequire`

```rsl
RsbFssRequire
```

## Процедура: `FSSP_CheckExistsFssp`

```rsl
FSSP_CheckExistsFssp (PartyID:Integer, [ExistsClaim:Bool], [ExistsFssp:Bool])
```

## Процедура: `FSSPREQUIRE_DocTypeFromStr`

```rsl
FSSPREQUIRE_DocTypeFromStr ([Name:String]):Integer
```

## Процедура: `GtConvertObjectCode`

```rsl
GtConvertObjectCode(ToCode:String, ToAppID:Integer, FromCode:String, FromAppID:Integer, ObjectKind:Integer):Integer
```

## Процедура: `UnswitchReceiver`

```rsl
UnswitchReceiver(AppID:Integer [, ObjectCode:String])
```

## Класс: `ExternalSign`

```rsl
ExternalSign ()
```

## Процедура: `InsertBankPayment`

```rsl
InsertBankPayment (pm_paym: Record [, pmrmprop: Record] [, debet: Record] [, credit: Record] [, order: Record] [, AutoKey : Integer], [SignKind : Integer] [, SignParm:Object]):Bool
```

## Процедура: `InsertCPBankPayment`

```rsl
InsertCPBankPayment (pm_paym: Record, [ cpprop: Record, ] [credit: Record, ] order : Record, [AutoKey:Integer, ] [SignKind:Integer, ] [SignParm:Object]):Bool
```

## Процедура: `oprSetSignature`

```rsl
oprSetSignature (ContextID:String, CryptoObject:GenObj):Bool
```

## Процедура: `AddAccountClaim`

```rsl
AddAccountClaim (Account:String, Chapter:Integer, FIID:Integer, ClaimNum:String, Initiator:Integer, ClaimType:Integer, ClaimKind:Integer [, Sum:Money] [, Priority:Integer] [, Note:String] [, DocDate:Date] [, RegDate:Date] [, StartDate:Date] [, EndDate:Date] [, Incremental:Bool] [, Auto:Bool] [, SkipCheckFreeAmount:Bool]):Bool
```

## Процедура: `ChangeAccountClaim`

```rsl
ChangeAccountClaim (ClaimID:Integer, DocNum:String, Initiator:Integer, ChangeKind:Integer, Delta:Money, [ Priority:Integer, ] [Note:String, ] [DocDate:Date, ] [RegDate:Date, ] StartDate:Date [, EndDate:Date] [, Auto:Bool]):Bool
```

## Процедура: `ChangeReserve`

```rsl
ChangeReserve (ClaimID:Integer, Delta:Money):Integer
```

## Процедура: `RecallChangeAccountClaim`

```rsl
RecallChangeAccountClaim (ChangeDocID:Integer):Bool
```

## Процедура: `InsertCurNRubDocument`

```rsl
InsertCurNRubDocument (type_doc:Integer, paymentDtype:Integer, paymentID:Integer, DocID:Integer, Purpose:Integer, Subpurpose:Integer, UserData: Integer, ForceMove:Integer, [ArraySymb:Date, MoneyL, String, ]d_id : Integer):Bool
```

## Процедура: `InsertMultiCurDocument`

```rsl
InsertMultiCurDocument (DbCurr: Integer, String, KrCurr: Integer, String, OVP1:String, OVP2:String, type_doc:Integer, paymentID:Variant):Integer
```

## Процедура: `GetAccountType`

```rsl
GetAccountType () : Integer
```

## Процедура: `addComissFromConCom`

```rsl
addComissFromConCom (feeType:Integer, sfCommNumber:Integer, to_sfContrId:Integer, from_sfContrId:Integer):Integer
```

## Процедура: `BorrowAccountClaim`

```rsl
BorrowAccountClaim (Chapter:Integer, Code_Currency:Integer, AccountFrom:String, AccountTo:String):Bool
```

## Процедура: `BreakBlock`

```rsl
BreakBlock ():Bool
```

## Процедура: `BreakOperation`

```rsl
BreakOperation ():Bool
```

## Процедура: `ChangeAccountType`

```rsl
ChangeAccountType (Chapter:Integer, FIID:Integer, Account:String, ChangeMode:Integer, Types:String):Integer
```

## Процедура: `changeSfPlan`

```rsl
changeSfPlan (sfContrId:Integer, sfPlanId:Integer, fromDate:Date [, usedRenewable:Bool]):Integer
```

## Процедура: `ConnectCategory`

```rsl
ConnectCategory ([ObjectType:Integer, ] [GroupID:Integer, ] [ObjectID:Integer, ] [TmpFlag:Bool, ] [AttrID:Integer, ] [CodeList:String, ] [NumInList:String]):Bool
```

## Процедура: `GetMessageNumber`

```rsl
GetMessageNumber (PartyID:Integer, MesKind:Integer, Series:String, Number:String):Bool
```

## Процедура: `InsertAccount`

```rsl
InsertAccount ([acc:File, Record, Tbfile, Trechandler] [, ab:Record] [, autokey:Integer] [, NeedBackout:BOOL] [, Limit:Money]):Bool
```

## Процедура: `InsertChangeAccountMessage`

```rsl
InsertChangeAccountMessage (Reqchnga: record): Integer
```

## Процедура: `InsertCloseAccountMessage`

```rsl
InsertCloseAccountMessage (Reqclosa: Record [, AccType:Integer]): Integer
```


```rsl
предназначена для формирования сообщения по заявлению на закрытие номера счета, при этом созданное сообщение привязывается к шагу операции. В зависимости от значений параметров процедуры сообщение может быть сформировано как по основному счету заявления, так и по связанному.
```

**Параметры:**

Reqclosa – значение параметра соответствует записи таблицы dreqclosa_dbt.
AccType – тип счета, по которому будет создано сообщение. Если параметр имеет
значение -1, то сообщение формируется по основному счету заявления.

**Возвращаемое значение:**



## Процедура: `InsertMultyDoc`

```rsl
InsertMultyDoc (mcdoc : Trechandler, [SignKind : Integer], [SignParm : Object]) : Bool
```

## Процедура: `InsertOpenAccountMessage`

```rsl
InsertOpenAccountMessage (Reqopena: Record [, AccType: Integer]):Integer
```

## Процедура: `InsertOprStatus`

```rsl
InsertOprStatus(StatusKindID:Integer, NumValue:Integer):Bool
```

## Процедура: `InsertPayment`

```rsl
InsertPayment ([ID:Integer, ] Payment: File, Record, TBfile, TRecHandler, [Debet: Variant, ] [Credit: Variant, ] [RMaket: Variant]):Bool
```

## Процедура: `InsertPaymentStat`

```rsl
InsertPaymentStat ([PaymentID:Integer, ] [PaymentStatus:Integer, ] [, PaymentIDType:Integer] [, DocKind:Integer] [, DocID:Integer] [, Purpose:Integer] [, SubPurpose:Integer] [, ValueDate:Date]):Bool
```

## Процедура: `InsertSfContract`

```rsl
InsertSfContract (sfcontr:Struct [, GroupID:Integer] [, sfssidl:Struct] [, SfPlanID:Integer] [, ProductID:Integer]): Bool
```

## Процедура: `вставляет`

```rsl
договор обслуживания на шаге операции.
```

**Параметры:**

sfcontr – буфер договора обслуживания со структурой, соответствующей структуре
таблицы dsfcontr_dbt.
GroupID – группа комиссий, которая закрепляется за договором. Параметр не задается,
если указан номер тарифного плана (SfPlanID).
sfssidl – буфер с информацией для создания СПИ ПЗО плательщика со структурой,
соответствующей структуре sfssidl.str.
OldSfID – идентификатор существующего договора. Если этот параметр передан, и
договор с таким идентификатором существует, то при вставке нового договора
для него будет произведено копирование комиссий из старого.
SfPlanID – номер тарифного плана, устанавливаемого на создаваемый договор
обслуживания. Параметр не задается, если указана группа комиссий (GroupID).
ProductID – идентификатор банковского продукта. В случае, если значение параметра
задано, создается банковский продукт.

**Возвращаемое значение:**




```rsl
запись с данными о новом субъекте в таблицу dparty_dbt.
```

**Параметры:**

party – вставляемый буфер (таблица dparty_dbt). После завершения работы процедуры в
эту таблицу заносится идентификатор вставленной записи.

**Возвращаемое значение:**



## Процедура: `KvitPayments`

```rsl
KvitPayments ([ID1:Integer] [, ID2:Integer]):Bool
```

## Процедура: `OprReplanStepPlanDates`

```rsl
OprReplanStepPlanDates (DateKind : Integer, DateValue : Date [, OnlyStepDate : Bool]) : Bool
```


```rsl
OprReplanStepPlanDates (DateKind:Variant, DateValue:Date [, OnlyStepDate:Bool]):Bool
```

## Процедура: `Opr_ConnectStep`

```rsl
Opr_ConnectStep(OperationID:Integer, StepID:Integer):Bool
```

## Процедура: `Opr_DeleteCarry`

```rsl
Opr_DeleteCarry (AppKind:Integer, AppKey:String [, ID_Operation:Integer] [, ID_Step:Integer]):Bool
```

## Процедура: `Opr_InsertAccSub`

```rsl
Opr_InsertAccSub (AnaliticsID:Integer, Account:String, FIID:Integer, Chapter:Integer, Parent:String, SubAcc:File, Record):Bool
```

## Процедура: `Opr_InsertAccSubDocument`

```rsl
Opr_InsertAccSubDocument (TmpID:Variant, AnaliticsID:Integer, Account:String, FIID:Integer, Chapter:Integer, Payer: String, Variant, Receiver: String, Variant, Doc:Variant):Bool
```

## Процедура: `Opr_InsertBranch`

```rsl
Opr_InsertBranch (BranchSymb:String [, KindBranch:String] [, ExecStep:Bool]):Bool
```

## Процедура: `OprUpdateMCCONACC`

```rsl
OprUpdateMCCONACC (New: Record):Bool
```

## Процедура: `OverestimateAccount`

```rsl
OverestimateAccount (Chapter:Integer, Code_Currency:Integer, Account:String, RegDate:Date):Bool
```

## Процедура: `SetOprDate`

```rsl
SetOprDate (DateKindID:Integer, Date:Date):Bool
```

## Процедура: `UpdateSumRealPayment`

```rsl
UpdateSumRealPayment (PaymentID:Integer , NewPayAmount:MoneyL [, NewAmount:MoneyL])
```

## Процедура: `SfInsertLink`

```rsl
SfInsertLink(PaymentID:Integer, InvoiceID:Integer):Bool
```

## Процедура: `SfInvSetState`

```rsl
SfInvSetState (InvoiceID:Integer, Status:Integer [, IsUpdateComiss: Bool, Integer]): Bool
```

## Процедура: `AskCorrectAction`

```rsl
AskCorrectAction([FieldName:String]):Bool
```

## Процедура: `CarryPlanDocuments`

```rsl
CarryPlanDocuments ([PaymentID:Integer, ] [DateBefore:Date]):Bool
```

## Процедура: `CloseUnionContr`

```rsl
CloseUnionContr(uniContrID:Integer, closeDate:Date):Integer
```

## Процедура: `CreateBilBookEntry`

```rsl
CreateBilBookEntry (FacturaID:Integer, Record, regDate:Date [, docs:TArray] [, DocKind:Integer] [, DocID:Integer, String] [, FIID:Integer] [, Amount:Money]):Bool
```

## Процедура: `DefineOprDate`

```rsl
DefineOprDate ([NumberDate:Integer, String], [valDate:Date]):Bool
```

## Процедура: `InsertCashOrder`

```rsl
InsertCashOrder (pscshdoc : Trechandler, pmpaym : Trechandler, rm : Trechandler, [symbols : Tarray], [SignKind : Integer], [SignParm : Array]) : Bool
```

## Процедура: `InsertLCNoticeMessage`

```rsl
InsertLCNoticeMessage (Lcpay:Trechandler, [LcLinkKind:Integer]):Integer
```

## Процедура: `InsertLimitRestoreTry`

```rsl
InsertLimitRestoreTry(FIID:Integer, Chapter:Integer, Sum:Money, Date:Date, ExeFromProc:Bool):Bool
```

## Процедура: `InsertLCMessage`

```rsl
InsertLCMessage(LcdocID:Integer, RlsFormID Integer, TpShemID:Integer, lcparty:Trechandler):Integer
```

## Процедура: `InsertMemorder`

```rsl
InsertMemorder (cbdoc:TRecHandler, pm_paym:TRecHandler, rm:TRecHandler [, ContextID:String] [, SignParm:Object] [, MemID: Integer]):Bool
```

## Процедура: `InsertObjectLink`

```rsl
InsertObjectLink (ObjectType:Integer, GroupID:Integer, ObjectID: Integer, String, TmpFlag:Bool, Variant, AttrType:Integer, AttrID: Integer, String, AttrTmpFlag: Bool, Variant):Bool
```

## Процедура: `InsertPaymentPropStat`

```rsl
InsertPaymentPropStat ([PaymentID:Integer], [PaymentStatus:Integer]):Bool
```

## Процедура: `InsertPayOrder`

```rsl
InsertPayOrder (payord_val:Record, paym_val:Record, rmprop_val:Record, Variant, credit_val:Record, Variant, paydem_val:Record, Variant, dlc:Variant):Bool
```

## Процедура: `InsertPcAdd`

```rsl
InsertPcAdd ([autoPerc:Integer] [, endDate:Date] [, addDate:Date] [, toAddSum:Moneyl]):Integer
```

## Процедура: `InsertPcPay`

```rsl
InsertPcPay ([autoPerc:Integer, ] [planDate:Date, ] [carryDate:date,] [ sum:Money]):Bool
```

## Процедура: `InsertPmsend`

```rsl
InsertPmsend (PaymentID:Integer, Action:Integer):Integer
```

## Процедура: `InsertWldPaymentStat`

```rsl
InsertWldPaymentStat ([WlPmID : Integer], [PaymentID : Integer], [Direct : Integer], Status : Integer) : Bool
```

## Процедура: `MFR_GetNextDepartment`

```rsl
MFR_GetNextDepartment(Department:Integer, EndDepartment:Integer):Integer
```

## Процедура: `Opr_SetAccountDate`

```rsl
Opr_SetAccountDate(date:Date)
```

## Процедура: `OprSay`

```rsl
OprSay (err_text:String):Variant
```

## Процедура: `OprUpdatePMDPPROP`

```rsl
OprUpdatePMDPPROP (pmdprop_new:Record [, pmdprop_old:Record]):Bool
```

## Процедура: `PaymentsKvit`

```rsl
PaymentsKvit (ArrayID_IP:Object, ArrayID_IPtype:Object, ArrayID_PP:Object, ArrayID_PPtype:Object [, ArraySum:Object] [, LinkKind:Integer]):Bool
```

## Процедура: `PaymentsReduction`

```rsl
PaymentsReduction (ArrayID:TArray, ArrayIDtype:TArray, [ArraySum:TArray, ] maket_pm:Record, [maket_cr: Record, ] [maket_rm: Record, ] [RedID:Integer]):Bool
```

## Процедура: `PlaceReqToClose`

```rsl
PlaceReqToClose(ReqID:Integer, ID_Operation:Integer, ID_Step:Integer):Integer
```

## Процедура: `SfComSetState`

```rsl
SfComSetState(oprsfcom:Record, status:Integer):Integer
```

## Процедура: `StepMFR_CABS`

```rsl
StepMFR_CABS (pmpaym:Record, pmrmprop:Record, debet:Record, credit:Record):Integer
```

## Процедура: `UnvalidPaymentMessage`

```rsl
UnvalidPaymentMessage(PaymentID:Integer [, BindingFlag:Bool]):Bool
```

## Класс: `RsbDeferredOperation`

```rsl
RsbDeferredOperation()
```

## Процедура: `AddDocumentToStep`

```rsl
AddDocumentToStep (Parm1:File, Record, Parm2:Integer, Parm3:Integer, Parm4:Integer, Parm5:Integer):Bool
```

## Процедура: `GetDocsByOperStep`

```rsl
GetDocsByOperStep ([Document: File, Record, ] [OprID:Integer, ] [StepID:Integer, Variant]):Bool
```

## Процедура: `GetKindActionFNS`

```rsl
GetKinfActionFNS():Integer
```

## Процедура: `GetOldfnsMessageID`

```rsl
GetOldfnsMessageID():Integer
```

## Процедура: `DeleteOperation`

```rsl
DeleteOperation (DocKind:Integer, Document:File, Record):Bool
```

## Процедура: `GetOperationGroup`

```rsl
GetOperationGroup (Parm:Integer):Integer
```

## Процедура: `GetOperationState`

```rsl
GetOperationState ([OprStat:File, Record]):Bool
```

## Процедура: `IsBUY`

```rsl
IsBUY (Group:Integer):Bool
```

## Процедура: `IsCOMMITMENT`

```rsl
IsCOMMITMENT (Parm:Integer, Parm:Integer):Bool
```

## Процедура: `на`

```rsl
основании системного типа операции, полученного в результате работы процедуры GetOperationGroup , позволяет интерпретировать назначения платежей для операций с точки зрения их отнесения к требованиям ("нашего" банка или клиента банка к контрагенту) или обязательствам ("нашего" банка или клиента банка перед контрагентом).
```

**Параметры:**

Parm – код системного типа операции.
Parm – код системного назначения платежа. Если данный параметр не указан, то по
умолчанию используется значение "BAi" (поставка базового актива).

**Возвращаемое значение:**



## Процедура: `IsCONVERS`

```rsl
IsCONVERS (Parm:Integer):Bool
```

## Процедура: `IsCONVERT_SHARE`

```rsl
IsCONVERT_SHARE (OperGroup:Integer):Bool
```

## Процедура: `IsCONVERT_RECEIPT`

```rsl
IsCONVERT_RECEIPT (OperGroup:Integer):Bool
```

## Процедура: `IsDealKSU`

```rsl
IsDealKSU (Group:Integer):Bool
```

## Процедура: `IsDERIVATIVE`

```rsl
IsDERIVATIVE (Parm:Integer):Bool
```

## Процедура: `IsEXCHANGE`

```rsl
IsEXCHANGE (Parm:Integer):Bool
```

## Процедура: `IsFUTURES`

```rsl
IsFUTURES (Parm:Integer):Bool
```

## Процедура: `IsLOAN`

```rsl
IsLOAN (Group : Integer) : Bool
```

## Процедура: `IsMOVING`

```rsl
IsMOVING (Parm:Integer):Bool
```

## Процедура: `IsOPTION`

```rsl
IsOPTION (Parm:Integer):Bool
```

## Процедура: `IsPUT`

```rsl
IsPUT (Parm:Integer):Bool
```

## Процедура: `IsRET_COUPON`

```rsl
IsRET_COUPON (Group:Integer):Bool
```

## Процедура: `IsRET_ISSUE`

```rsl
IsRET_ISSUE (Group:Integer):Bool
```

## Процедура: `IsSALE`

```rsl
IsSALE (Parm:Integer):Bool
```

## Процедура: `IsSWAP`

```rsl
IsSWAP (Parm:Integer):Bool
```

## Процедура: `ListKindOper`

```rsl
ListKindOper (KOPERbuff:File, Object, Record, DocKind:Integer, Closed:Bool) :Bool
```

## Процедура: `OprSfComScrol`

```rsl
OprSfComScrol (ruledef:Memaddr, comlist:Object, scrol_type:Integer ):Integer
```

## Процедура: `IsOprMultiExec`

```rsl
IsOprMultiExec ():Bool
```

## Процедура: `Opr_AutoRunStep`

```rsl
Opr_AutoRunStep (DocKind:Integer, DocumentID:String, symb:String):Bool
```

## Процедура: `Opr_BackoutStep`

```rsl
Opr_BackoutStep (ID_Operation:Integer, [ID_Step:Integer], [IsBackToStep:Bool]):Integer
```

## Процедура: `Opr_ExecuteStep`

```rsl
Opr_ExecuteStep (ID_Operation:Integer, ID_Step:Integer):Integer
```

## Процедура: `Opr_InsertAndExecuteBranch`

```rsl
Opr_InsertAndExecuteBranch (ID_Operation:Integer, BranchSymbol:String, BranchKind:String, [ID_Step:Integer], [StepSymbol:String]):Integer
```

## Процедура: `Opr_UnConnectBranch`

```rsl
Opr_UnConnectBranch (ID_Operation:Integer, ID_Step:Integer):Integer
```

## Процедура: `StepInfo`

```rsl
StepInfo (Kind_action:Integer, rec:File, Record, DocKind:Integer, DocID:String):Bool
```

## Процедура: `StepInfoEx`

```rsl
StepInfoEx ([Number_step:Integer,] rec: Record [[[, DocKind:Integer], DocID: Integer], (OperationID: Variant)]):Bool
```

## Процедура: `Opr_GetLastExecStepBySymbol`

```rsl
Opr_GetLastExecStepBySymbol (DocKind:Integer, DocumentID:String, symb:String):Bool
```

## Процедура: `PrimaryForDoc`

```rsl
PrimaryForDoc (DocKind:Integer, DocID:String, ApplKind:Integer, ApplKey:String):Bool
```

## Процедура: `RunOperation`

```rsl
RunOperation (DocKind:Integer, Document:File, Record, IsF:Bool, KindOper:Integer [, NoShowSteps:Bool]):Bool
```

## Процедура: `GetCountPartMesFNS`

```rsl
GetCountPartMesFNS():Integer
```

## Процедура: `GetMessageNumber510`

```rsl
GetMessageNumber510 (PartyID:Integer, Account:String, [Account_New:String], [Chapter:Integer], FIID:Integer, ClientID:Integer, Series:String, Number:String, [OldMesID:Integer], [ChangeBankProps:Bool], [IsSFC:Bool]):Bool
```

## Процедура: `GetGenBVDwithBVS`

```rsl
GetGenBVDwithBVS ():Integer
```

## Процедура: `GetNumPartMesFNS`

```rsl
GetNumPartMesFNS():Integer
```

## Процедура: `GetOperDepartment`

```rsl
GetOperDepartment (Parm:Integer):Bool
```

## Процедура: `GetOprDate`

```rsl
GetOprDate (NumberKD:Integer [, odate:Date, ], DocKind:Integer, Variant, [DocID:String]):Bool
```

## Процедура: `InsertSingComisPayment`

```rsl
InsertSingComisPayment (DocKind:Integer, BufDoc:Record, oprsfcom:Record):Bool
```

## Процедура: `IsDVFXBNOTE`

```rsl
IsDVFXBNOTEIsDVFXBNOTE(Group:integer):bool
```

## Процедура: `Opr_SetMultiExec`

```rsl
Opr_SetMultiExec(newMode:Bool, Integer):Bool
```

## Процедура: `OprGetAccountRest`

```rsl
OprGetAccountRest (Chapter:Integer, Currency:Integer, Account:String, [DataRest:Date], [Rest:Money], [PlanRest:Money]):Bool
```

## Процедура: `OprGetChildDocs`

```rsl
OprGetChildDocs([ID_Operation:Integer [, ID_Step:Integer [, OnlyPrimary:Bool]]]):Object
```

## Процедура: `OprGetSFDocParam`

```rsl
OprGetSFDocParam (PrimKind:Integer, PrimBuffer:Memaddr, OprPDParam:Record):Bool
```

## Процедура: `RT_MakeFactDate`

```rsl
RT_MakeFactDate ([StartDate:Date [, Duration:Integer [, Pitch:Integer [, Basis:Integer]]]]): Date
```

## Процедура: `ПолучитьСтавку`

```rsl
ПолучитьСтавку (FI: Integer, Product: Integer, Fund: Integer, Informator: Integer, MarketPlace: Integer, Purpose: Integer, RiskType: Integer, RiskGroup: Integer, Basis: Integer, BalanceSide: Integer, ActionDate: Date, Forestall: Date, StartDate: Date, EndDate: Date, Volume: Moneyl, Rate: Variant): Integer
```

## Класс: `RsbBatchImageParm`

```rsl
RsbBatchImageParm()
```

## Класс: `RsbCBDKFindPartyFields`

```rsl
RsbCBDKFindPartyFields()
```

## Класс: `RsbCheckAddressError`

```rsl
RsbCheckAddressError()
```

## Класс: `RsbOfficer`

```rsl
RsbOfficer()
```

Объект класса служит для работы с информацией о сотрудниках субъекта. Объект этого
класса создается вместе с объектом класса RSBParty с помощью метода Officer.
Использование объекта отдельно от объекта RSBParty невозможно.

**Свойства:**

Person ID –идентификатор физического лица или сотрудника; тип Integer.
OfficeID – идентификатор отдела; тип Integer.
Post – должность сотрудника; тип String.
PhoneNumber – телефон сотрудника; тип String.
DateFrom – дата начала действия полномочий лица, временно пользующегося правом
подписи; тип Date.
DateTo – дата окончания действия полномочий лица, временно пользующегося правом
подписи; тип Date.
HasSignRigh– признак того, что сотрудник имеет право подписи зарплатного реестра; тип
Bool.
IsFirstPerson – признак наличия у сотрудника права первой подписи; тип Bool.
IsSecondPerson – признак наличия у сотрудника права второй подписи; тип Bool.
IsMatOtvPerson – признак материальной ответственности сотрудника; тип Bool.
IsFirstOfficePerson – признак, определяющий сотрудника, который является начальником
подразделения; тип Bool.
IsTempSignature – признак наличия у сотрудника временного права подписи; тип Bool.

**Методы:**

DeletePerson (PersonID:Integer):Bool
Удаление сотрудника субъекта по заданному идентификатору физического лица,
указанному в параметре PersonID. В случае успешного выполнения возвращает значение
TRUE, иначе – FALSE.
GetFirstOfAll ():Bool

## Класс: `RSBParty`

```rsl
RsbParty ([PartyID:Integer] [, Original:Bool])
```

Объект класса служит для работы с информацией о субъекте экономики.

**Параметры:**

PartyID – идентификатор существующего субъекта. Если параметр не задан, то создается
новый субъект, реальный идентификатор которого будет создан после вызова
метода Update.
Original – параметр, определяющий, что будет искать процедура FindPARTY, если
параметр PartyID не будет задан. Параметр может принимать следующие
значения:
- TRUE – создается новый субъект-оригинал, реальный идентификатор которого
будет создан после вызова метода Update.
- FALSE – подставляется идентификатор существующего объекта PartyID (по
умолчанию).

**Свойства:**




```rsl
имеет набор свойств, как простых, представляющих собой переменные, так и сложных, которые, в свою очередь, являются объектами. Простые свойства класса могут, в большинстве своем, возвращать и устанавливать значения одноименных полей субъекта. Исключение составляют свойства PartyID, Change_Date и Change_DatePrev, которые доступны только для чтения. Для данного класса предусмотрены: · основные свойства из числа простых ; · свойства, характеризующие субъект как физическое лицо ; · ряд простых свойств для определения устава субъекта (учреждения, предприятия, организации)
```

;
· свойства, характеризующие субъект как участник БЭСП
;
· сложные свойства
.

**Методы:**

AddOwn(PartyKind:Integer)

## Метод: `удаления`

```rsl
субъекта. Возвращает TRUE в случае успешного завершения. DeleteUnlocked ()
```

## Метод: `вставки`

```rsl
клиента физического лица для Розничного обслуживания для текущего подразделения. IsOwned (PartyKind:Integer):Bool
```

## Метод: `блокировки`

```rsl
обновления информации о субъекте в базе данных. Возвращает TRUE в случае успеха. Officer ():Object
```

## Класс: `RsbPartyAddress`

```rsl
RsbPartyAddress()
```

## Класс: `RsbPartyCheckECUPRID`

```rsl
RsbPartyCheckECUPRID()
```

Класс – обертка над сущностью "Проверки субъектов в ЕС УПРИД".

**Свойства:**

CheckDate – дата последнего вызова интерфейса RS-Connect; тип Date.
CheckTime – время вызова; тип Time.
MessageID – идентификатор первичного запроса к RS-Connect; тип String.
ObjectID – идентификатор учетного объекта в RS-Connect; тип String.
Oper – пользователь; тип Integer.
PersonID – системный идентификатор проверяемого субъекта; тип Integer.
RecID – идентификатор записи; тип Integer.
ReturnCode – код ошибки, полученный от ЕC УПРИД в результате выполнения запроса;
тип String.
StatusCode – код статуса обработки последнего выполненного запроса в RS-Connect; тип
String.

**Методы:**

Add():Integer

## Класс: `RsbPartyContact`

```rsl
RsbPartyContact()
```

## Класс: `RsbPartyPFPropRSL`

```rsl
RsbPartyPFPropRSL()
```

## Класс: `RsbPartyRegDoc`

```rsl
RsbPartyRegDoc ()
```

## Класс: `RsbPartyTaxExemp`

```rsl
RsbPartyTaxExemp()
```

## Класс: `RsbPersonCitizen`

```rsl
RsbPersonCitizen()
```

## Класс: `RsbPersonPaper`

```rsl
RsbPersonPaper()
```

## Класс: `RsbPersonPlaceWork`

```rsl
RsbPersonPlaceWork()
```

## Класс: `RsbPtCode`

```rsl
RsbPtCode()
```

Объект класса предоставляет доступ к кодам субъекта. Объект создается вместе с
объектом RsbParty при помощи его свойства Code, которое позволяет записывать и
считывать объект класса RsbPtCode. Использование объекта класса RsbPtCode
отдельно от RsbParty невозможно.

**Методы:**

CloseCode (CodeKind:Integer, CloseDate:Date):Bool

## Метод: `быстрого`

```rsl
доступа к значению кода субъекта. Для доступа необходимо указать вид кода CodeKind субъекта как индекс объекта RsbPtCode. Метод возвращает значение кода заданного вида.
```

**Пример:**

RsbParty Party(123);
var PartyINN: string;
PartyINN = party.Codes(PTCK_INN); // Получаем ИНН

## Класс: `RsbPtNote`

```rsl
RsbPtNote()
```

## Класс: `примечаний`

```rsl
субъекта. Объект этого класса создается вместе с объектом RsbParty , использование указанного объекта отдельно от RsbParty невозможно.
```

**Методы:**

AddNote (NoteKind:Integer, Note:Variant, Date:Date):Integer

## Класс: `RsbResidentHist`

```rsl
RsbResidentHist()
```

## Класс: `TRsbLegalProxyList`

```rsl
TRsbLegalProxyList()
```

## Процедура: `PDN_InsertPDNFINPROCPARTY`

```rsl
PDN_InsertPDNFINPROCPARTY(Rec:Record):Integer
```

## Процедура: `PDN_InsertPDNPARTYTARGET`

```rsl
PDN_InsertPDNPARTYTARGET(Rec:Record):Integer
```

## Процедура: `PDN_InsertPDNTYPEPARTY`

```rsl
PDN_InsertPDNTYPEPARTY(Rec:Record):Integer
```

## Процедура: `Batch_CBDK_SyncParty`

```rsl
Batch_CBDK_SyncParty([PartyList:String, ] UseSynch:Bool [, BeginDate:Date] [, BeginTime:Time] [, Enddate:Date] [, EndTime:Time]):Integer
```

## Процедура: `CB_CheckPersnIDCAllow`

```rsl
CB_CheckPersnIDCAllow(PaperKind:Integer, NotResident:Bool, IsStateless:Bool, Born:Date):Integer
```

## Процедура: `CB_DelPtProxy`

```rsl
CB_DelPtProxy(PartyID:Integer, ProxyID:Integer):Integer
```

## Процедура: `CB_GetListPtProxy`

```rsl
CB_GetListPtProxy(PartyID:Integer, PtPrxArray:TArray):Integer
```

## Процедура: `CB_ListPartyPtProxy`

```rsl
CB_ListPartyPtProxy(PartyID:Integer, UseProxyList:Bool, recptproxy:Record):Integer
```

## Процедура: `CB_ListPtProxy`

```rsl
CB_ListPtProxy(PartyID:Integer, recptproxy:Record):Integer
```

## Процедура: `CB_SetPtProxy`

```rsl
CB_SetPtProxy(recptproxy:Record):Integer
```

## Процедура: `CBDK_FindPartyPanel`

```rsl
CBDK_FindPartyPanel(Fields:Object, Party:Object, Result:Integer):Integer
```

## Процедура: `FindSETTACC_PMAUTO`

```rsl
FindSETTACC_PMAUTO (PartyID:Integer, FIKind:Integer, FIID:Integer, ServiceKind:Integer, KindOper:Integer, Purpose:Integer, BankID:Integer, settacc:Record):Integer
```

## Процедура: `GetNameClient`

```rsl
GetNameClient (regPath:String, Account: Record, Chapter:Integer [, CodeCurrency:Integer] [, IsPayer : Bool] [, IsAllowLegalForm : Bool]):String
```

## Процедура: `GetOriginParty`

```rsl
GetOriginParty (PartyID:Integer [, PARTY:Record]):Integer
```

## Процедура: `GetPartyNames`

```rsl
GetPartyNames (PartyID:Integer, NameTypeID:Integer [, UseHistory:Bool]):Array
```

## Процедура: `GetPartyOnDate`

```rsl
GetPartyOnDate (PartyID:Integer, pDate:Date, [Party:File| Record| Tbfile| Trechandler], [BankDprt:File| Record| Tbfile| Trechandler], [PtBicDir:File| Record| Tbfile| Trechandler], [Persn:File| Record| Tbfile| Trechandler]):Integer
```

## Процедура: `ListPT`

```rsl
ListPT(PARTY: File, Record, SelectCodeKind:Integer, SelectCode:Integer, PTLIST:Integer, PartyID:Integer, CodeKind:Integer, FromDate:Date, ToDate:Date):Bool
```

## Процедура: `ListPText`

```rsl
ListPText (PARTY:File, Record, PartyID:Integer, AddCond:String [, readOnly:Bool]):Bool С помощью процедуры формируется список, используемый для выбора субъекта из справочника субъектов экономики.
```

**Параметры:**

PARTY – структура или таблица dparty_dbt, заполняется при выборе субъекта из списка.
PartyID – код субъекта, который будет первым в списке. По умолчанию используется
значение 0.
AddCond – строка, содержащая условие отбора субъектов в список. Добавляется к
генерируемому стандартным механизмом SQL-запросу.
readOnly – признак, определяющий возможность чтения/записи содержимого списка.
Возможные значения параметра:
- TRUE – чтение.
- FALSE – запись.
Если привилегии операциониста не допускают чтение/запись, то значение
параметра не учитывается и содержимое списка открывается только для чтения.

**Возвращаемое значение:**

- TRUE – в случае выбора субъекта (нажатием клавиши [Enter]).
- FALSE – во всех остальных случаях.

**Пример:**

import PTInter;
record pt( party );
/*показать список оценщиков – физических лиц*/
ListPText( pt, 0, "t.t_legalform = 2 AND t.t_partyid IN
(SELECT t_partyid FROM dpartyown_dbt WHERE t_partykind =
44)" );

## Процедура: `PartyAliesList`

```rsl
PartyAliesList (PartyID:Integer):Array
```

## Процедура: `PartyNameAdd`

```rsl
PartyNameAdd (Name:String, PartyID:Integer):Integer
```

## Процедура: `PartyNameFreqIncr`

```rsl
PartyNameFreqIncr (Name:String, PartyID:Integer):Integer
```

## Процедура: `PT_BindClientWithBranch`

```rsl
PT_BindClientWithBranch (PartyID:Long, ServiceKind:Integer, Branch:Integer [, Oper:Integer] [, startDate:Date] [, ForcedSet:Bool]):Bool
```

## Процедура: `PT_CheckClientService`

```rsl
PT_CheckClientService (ClientID : Long, ServiceKind : Integer, CheckDate : Date, Department : Integer) : Integer
```

## Процедура: `PT_CheckPriostanAccounts`

```rsl
PT_CheckPriostanAccounts (PartyID:Integer, [UserResult:Record])
```

## Процедура: `PT_CheckProxySignAuthority`

```rsl
PT_CheckProxySignAuthority (Account:String, Code_Currency:Integer, Chapter:Integer, PartyID:Integer, ProxyIDArray:Array, WrongProxyID:Integer, Message:String):Integer
```

## Процедура: `PT_CloseClientService`

```rsl
PT_CloseClientService (ClientID:Long, ServiceKind:Integer, CloseDate:Date [, SilentMode:Bool]):Bool
```

## Процедура: `PT_CopyPartyParm`

```rsl
PT_CopyPartyParm (destPartyID: Integer, sourcePartyID: Integer): Integer
```

## Процедура: `PT_DefinePartyDoubler`

```rsl
PT_DefinePartyDoubler (PartyObj:Object, EditMode:Bool, PanelMode:Bool):Integer
```

## Процедура: `PT_DeleteClientService`

```rsl
PT_DeleteClientService (ClientID:Integer, ServiceKind:Integer):Integer
```

## Процедура: `PT_DeletePTBANKRUPTHIST`

```rsl
PT_DeletePTBANKRUPTHIST (RecID:Integer):Integer
```

## Процедура: `PT_DeletePTBENEOWNER`

```rsl
PT_DeletePTBENEOWNER(Id:Integer):Integer
```

## Процедура: `PT_FindADRESS`

```rsl
PT_FindADRESS (PartyID:Long, AdrType:Integer, [AdrBuff:Memeaddr], [AdrDate:Date], [AdrRHArray:Array], [ParentID:Long]):Integer
```

## Процедура: `PT_FindADRESSHist`

```rsl
PT_FindADRESSHist (PartyID:Long, AdrType:Integer, [AdrID:Long], Direction:Bool, AdrRHArray:Array):Integer
```

## Процедура: `PT_FormAddressStr`

```rsl
PT_FormAddressStr (AdrID:Integer, PartyID:Integer, [AddrType:Integer], [AddrMode:Integer], [SetUpper:Bool], AddrStr:String):Integer
```

## Процедура: `PT_FormAddressStrByGUID`

```rsl
PT_FormAddressStrByGUID (Guid:String, [AddrMode:Integer], [SetUpper:Bool], AddrStr:String):Integer
```

## Процедура: `PT_GetAddressByGUID`

```rsl
PT_GetAddressByGUID (Guid:String, Address:Record):Integer
```

## Процедура: `PT_GFias_GetAdressByObjectID`

```rsl
PT_GFias_GetAdressByObjectID(ObjectID:BigInt, adr:record):Integer
```

## Процедура: `PT_GFias_GetObjectIDByAdress`

```rsl
PT_GFias_GetObjectIDByAdress (adr:Record, ObjectID:BigInt):Integer
```

## Процедура: `PT_GetAddressGUID`

```rsl
PT_GetAddressGUID (PartyID:Integer, [AddrType:Integer], AddrGUID:String):Integer
```

## Процедура: `PT_GetFIASForAddress`

```rsl
PT_GetFIASForAddress (Address:Record, FiasGuid:String):Integer
```

## Процедура: `PT_GFias_GetObjectID`

```rsl
PT_GFias_GetObjectID(PartyID:Long, ObjectID:BigInt, [AddrType:Integer]):Integer
```

## Процедура: `PT_GetSimilarForParty`

```rsl
PT_GetSimilarForParty (PartyID:Integer, LegalForm:Integer, Name1:String, Name2:String, Name3:Integer, BirthDate:Date, ShortName:String, CodeINN:String, ExcludeDoublers:Bool, OriginalArray:Tarray):Integer
```

## Процедура: `PT_InsUpdPTBANKRUPTHIST`

```rsl
PT_InsUpdPTBANKRUPTHIST (PtBankruptHistRec:Record):Integer
```

## Процедура: `PT_InsUpdPTBENEOWNER`

```rsl
PT_InsUpdPTBENEOWNER(PTBeneownerBuff:Record):Integer
```

## Процедура: `PT_IsGenderNotIdent`

```rsl
PT_IsGenderNotIdent ([ps:Record, String]):Bool
```

## Процедура: `PT_ListPARTYNAME`

```rsl
PT_ListPARTYNAME (PartyID:Integer, [buff:Record], [kinds:Array, Integer]):Integer
```

## Процедура: `пролистывает`

```rsl
псевдонимы субъекта.
```

**Параметры:**

PartyID – идентификатор субъекта.
buff – буфер записи partyname.dbt
kinds – перечень видов наименований (для отображения в списке).

**Возвращаемое значение:**



## Процедура: `PT_SplitPersonIDC`

```rsl
PT_SplitPersonIDC (Source:String, PaperKind:Integer, CheckFormat:Bool, [PaperSeries:String], [PaperNumber:String], [ErrorMsg:String]):Integer
```

## Процедура: `PT_SearchOperationForClient`

```rsl
PT_SearchOperationForClient(Party:Object):Integer
```

## Процедура: `UploadFiasXMLFileIntoDBFile`

```rsl
UploadFiasXMLFileIntoDBFile (XMLFileName:String, DBFileType:Integer):Integer
```

## Процедура: `ВидСубъекта`

```rsl
ВидСубъекта (PartyID:Integer, PartyKind:Integer [, ErrCode:Integer]):Bool
```

## Процедура: `ВставитьСубъекта`

```rsl
ВставитьСубъекта (party: File, Record):Bool
```

## Процедура: `ОбслуживаетсяКлиент`

```rsl
ОбслуживаетсяКлиент (PartyID:Integer, ServiceKind:Integer [, StartDate:Date, Variant] [, FinishDate:Date, Variant] [, error:Integer]):Bool
```

## Процедура: `при`

```rsl
успешном завершении возвращает значение: · TRUE – в случае положительного ответа. · FALSE – в случае отрицательного ответа.
```

**Пример:**

import PTInter;
record Субъект (party);
var КодСубъекта = 1,
Дата = {curdate}
Error,
flag;
flag 
= 
ОбслуживаетсяКлиент(КодСубъекта, 
PTSK_PAY, 
Дата,
Дата, Error)
if(Error = 0)
if(flag)
ПринятьПлатежноеПоручение();
end;
end;

## Процедура: `ПолучитьКодСубъекта`

```rsl
Существует два варианта вызова процедуры в зависимости от типа первого передаваемого параметра. ПолучитьКодСубъекта (Code:String, CodeKind:Integer, error:Integer):Integer При таком вызове процедура возвращает внутренний идентификатор PartyID субъекта по его внешнему коду Code вида CodeKind. ПолучитьКодСубъекта (PartyID:Integer, CodeKind:Integer, error:Integer, recursive:Integer)
```

При таком вызове процедура возвращает внешний код субъекта Code вида CodeKind по
его внутреннему идентификатору PartyID.

## Процедура: `ПолучитьСубъекта`

```rsl
ПолучитьСубъекта (PartyID:Integer, PARTY: Record):Integer
```

## Процедура: `ПолучитьКодСубъектаДляСчета`

```rsl
ПолучитьКодСубъектаДляСчета (ИдСубъекта:Integer [, ВидКода:Integer] [, КодОшибки:Integer]):String
```

## Процедура: `СрокОбслуживанияКлиента`

```rsl
СрокОбслуживанияКлиента (PartyID:Integer, ServiceKind:Integer, StartDate:Date, FinishDate:Date):Integer
```

## Процедура: `GetKladrLevel1`

```rsl
GetKladrLevel1():Bool
```

## Процедура: `GetKladrLevel2`

```rsl
GetKladrLevel2():Bool
```

## Процедура: `GetKladrLevel3`

```rsl
GetKladrLevel3():Bool
```

## Процедура: `GetKladrLevel4`

```rsl
GetKladrLevel4():Bool
```

## Процедура: `GetKladrLevel5`

```rsl
GetKladrLevel5():Bool
```

## Процедура: `GetKladrLevel6`

```rsl
GetKladrLevel6():Bool
```

## Процедура: `CB_DeleteNotetextHist`

```rsl
CB_DeleteNotetextHist (ID:Integer):Integer
```

## Процедура: `CB_InsertNotetextHist`

```rsl
CB_InsertNotetextHist (ObjectType:Integer, DocumentID:String, NoteKind:Integer, Date:Date, ValidToDate:Date, NoteValue:Variant, ID:Integer):Integer
```

## Процедура: `CB_UpdateNotetextHist`

```rsl
CB_UpdateNotetextHist (ID:Integer, Date:Date, ValidToDate:Date[, NoteValue:Variant]):Integer
```

## Процедура: `FindAdressContactValue`

```rsl
FindAdressContactValue (Addr:Record, ContactField:Integer, Value:String, Provider:String):Integer
```

## Процедура: `FoundSPI`

```rsl
FoundSPI (FIID: Integer, Account: String, [settac: Record]):Bool
```

## Процедура: `GetCapital`

```rsl
GetCapital(onDate:Date, [SumOfCapital:Money], [BaseCapital:Money], [MainCapiltal:Money]):Integer
```

## Процедура: `GetCorAcc`

```rsl
GetCorAcc (FIID:Integer, Corschem:Integer, KindAcc: Integer, String, Variant [, Origin:Bool, Variant]):Integer
```

## Процедура: `GetFullBankName`

```rsl
GetFullBankName (PartyID:Integer):String С помощью процедуры формируется полное наименование банка. Параметр: PartyID  идентификатор банка как субъекта экономики.
```

**Возвращаемое значение:**



## Процедура: `GetPersnIDCOnDate`

```rsl
GetPersnIDCOnDate(PersonID:Integer, PaperKind:Integer, OnDate:Date, PersnIDC:Record):Integer
```

## Процедура: `GetPtOfficeState`

```rsl
GetPtOfficeState (PartyID:Integer, OrgDate:Date, Office:Integer|String [, officce_buff:TrecHandler] [, superior_buff:TrecHandler] [, Sort:Integer] [, DateBegin:Date] [, ErrMes:String]):Bool
```

## Процедура: `IsBankType`

```rsl
IsBankType (Party: File, Integer, Record Type:Integer):Bool
```

## Процедура: `ListCorschem`

```rsl
ListCorschem (Corschem:Record [, Header:String] [, Flag:Integer, String]):Integer
```

## Процедура: `ListOrgStructure`

```rsl
ListOrgStructure (PartyID:Integer, OrgDate:Date, officce_buff:TrecHandler [, superior_buff:TrecHandler] [, OnlyForSuperiorID:Integer] [, NoChangeDate:Bool] [, SelectDate:Date]):Bool
```

## Процедура: `ParseRSMailString`

```rsl
ParseRSMailString (Value:String, Country:Integer, Region:Integer, Node:Integer):Integer
```

## Процедура: `PT_SelectLegalProxyHist`

```rsl
PT_SelectLegalProxyHist([PartyID:Integer] [, Account:String] [, ProxyID:Integer] [, OnlyActive:Bool]):Object
```

## Процедура: `PtCertainCategory`

```rsl
PtCertainCategory(PartyID:Integer, Flags:Integer):Integer
```

## Процедура: `PtCertainCategoryWarning`

```rsl
PtCertainCategoryWarning(PartyID:Integer):String
```

## Процедура: `PTOfficeInsert`

```rsl
PTOfficeInsert (BuffPTOffice:TrecHandler [, BaseOffice:Integer|String] [, Position:Integer] [, ErrMes:String]):Bool
```

## Процедура: `PTOfficeTree`

```rsl
PTOfficeTree (PartyID:Integer, SuperiorOfficeID:Integer, OrgDate:Date, Level:Integer):Object
```

## Процедура: `SetCapital`

```rsl
SetCapital(onDate:Date, SumOfCapital:Money, [BaseCapital:Money], [MainCapiltal:Money]):Integer
```

## Процедура: `XCOMPL_MakePartyNoteText`

```rsl
XCOMPL_MakePartyNoteText(SystemId:Integer, UpDateAt:Date):String
```

## Процедура: `ВышестоящееПодразделение`

```rsl
ВышестоящееПодразделение (PartyID:Integer, OfficeID:Integer, ActualDate:Date [, FindingBuf:Memaddr]):Bool
```

## Процедура: `ПолучитьКорсхемуПоУмолчанию`

```rsl
ПолучитьКорсхемуПоУмолчанию ([BankID:Integer, ] [FIID:Integer, ] [TypeDc:Integer, ] [DKFlag:String, ] [IOPartyID:Integer, ] [MesBankID:Integer, ] [NumberPack:Integer, ] [CorrID:Integer, ] [OurCorrAcc:String, ] [OperatTime:Variant, ] [IsTaxPaym:Bool, ] [TpShemID:Integer, [InOurBalance:String, ] [OurCorrID:Integer]):Integer
```

## Класс: `TRsbDataSet`

```rsl
TRsbDataSet():Object
```

## Класс: `имеет`

```rsl
набор конструкторов, аналогичный набору конструкторов класса RsdRecordset: TRsbDataSet (Cmd:Object [, CursorLocation :Integer] [, CursorType :Integer]) :Object Конструктор выборки на основе объекта класса RsdCommand. TRsbDataSet (cmdText:String [, CursorLocation:Integer] [, CursorType :Integer]):Object Конструктор выборки на основе SQL запроса. TRsbDataSet (ConString :String, cmdText :String [, CursorLocation :Integer] [, CursorType :Integer]):Object Конструктор выборки на основе SQL запроса с указанием строки соединения с базой данных. Конструктор вызывается с параметрами: Cmd – объект класса RsdCommand. RsdCommand должен быть выполнен или готов к выполнению SQL запроса (инициализирован). cmdText – текст SQL запроса. ConString – строка соединения с базой данных. CursorLocation – местоположение курсора, которое задается одной из следующих констант: · RSDVAL_SERVER – курсор создается на сервере; · RSDVAL_CLIENT – курсор создается в памяти клиентского приложения; · RSDVAL_CLIENT_IF_NEEDED – если сервер поддерживает серверные курсоры, то курсор создается на сервере, если нет, то в памяти клиентского приложения. CursorType – тип курсора. Тип курсора задается одной из констант: · RSDVAL_STATIC – статический курсор, который загружает данные, полученные при выполнении команды, в область памяти целиком. · RSDVAL_DYNAMIC – динамический курсор, который загружает данные в область памяти постранично. Размер страницы устанавливается в свойстве BlockSize. Этот тип курсора рекомендуется использовать при работе с большими объемами данных. · RSDVAL_FORVARD_ONLY – курсор удерживает только одну запись и поддерживает перемещение вперед по набору данных. Этот тип курсора рекомендуется использовать, если запрос создается с целью простого чтения данных без необходимости их дальнейших изменений. · RSDVAL_KEYSET_DRIVEN – курсор, поддерживаемый MS SQL-сервером, который представляет собой разновидность динамического курсора. Такой курсор сохраняет ключ для набора данных и перемещается по нему динамически. Этот тип курсора рекомендуется использовать при работе с большими объемами данных для экономии серверных ресурсов.
```

## Метод: `имеет`

```rsl
параметр Obj – объект поля которого будут скопированы в текущую запись источника данных. Обязательный параметр.
```

**Пример:**

import RsbDataSet;
var party_rec = TRecHandler("dparty_dbt");
// Создание объекта на основе SQL запроса.
var DataSet = TRsbDataSet("select t_partyid, t_legalform,
t_shortname, t_name, t_addname"
" from dparty_dbt"
" where t_partyid < 3"
" order by t_partyid"
);
DataSet.MoveNext();
// присваиваем новое значение
party_rec.rec.name = "Test";
// кладем рекорд в датасет
DataSet.SetRecord( party_rec.rec );
// печатаем новое значение у датасета
println( DataSet.name );
SetFieldType (FieldName:String, NewType:Integer)
Устанавливает новый тип поля. После вызова функции для поля данные этого поля будут
преобразовываться к установленному типу. Метод имеет параметры:
- FieldName – имя столбца, тип которого нужно изменить.
- NewType – новый тип столбца.

**Пример:**

import RsbDataSet;
var dataSet = TRsbDataSet("SELECT * FROM dparty_dbt");
dataSet.SetFieldType("t_PartyID", V_DOUBLE);
dataSet.MoveNext();
println(dataSet.t_partyid);
Update ():Bool
Обновляет или вставляет новую запись в базу данных.

**Пример:**

import RsbDataSet;
// Создание объекта на основе SQL запроса.
var DataSet = TRsbDataSet("select t_partyid, t_legalform,
t_shortname, t_name, t_addname"
" from dparty_dbt"
" where t_legalform = 2"
" order by t_partyid"
);
// Распечатка свойств и методов объекта
printobject(DataSet);
while(DataSet.MoveNext())
// Нижеследующие свойства имеют равные значения.
println(DataSet.t_Name);
println(DataSet.Name);
println(DataSet.rec.t_Name);
println(DataSet.rec.Name);
end;
Классы

## Класс: `RsbObjFactory`

```rsl
RsbObjFactory ()
```

Класс "фабрики", служит для создания экземпляров объектов Rs-Vox.

**Методы:**

GetObject (ObjectName:String [, ObjectType:Integer]):Object

## Класс: `RsSysLogDescriptor`

```rsl
RsSysLogDescriptor()
```

## Процедура: `RsSyslogClose`

```rsl
RsSyslogClose(descriptor:Object, errmsg:String):Bool
```

## Процедура: `RsSyslogConnect`

```rsl
RsSyslogConnect(protocol:Integer, ip_address:String, port:Integer, certfile:String, descriptor:Object, errmsg:String):Bool Процедура предназначена для создания соединения с сервером Syslog.
```

**Параметры:**

Protocol – протокол соединения. Возможные значения:
- RSSYSLOG_TCP
- RSSYSLOG_UDP
- RSSYSLOG_DTLS
ip_address – IP-адрес сервера Syslog.
port – номер порта сервера Syslog.
Certfile – полный путь к файлу корневого сертификата (используется только  для только
для RSSYSLOG_DTLS
).
descriptor – дескриптор соединения (выходной параметр).
errmsg – текст ошибки.

**Возвращаемое значение:**



## Процедура: `RsSyslogWrite`

```rsl
RsSyslogWrite(descriptor:Object, msg:String, errmsg:String):Bool
```

## Класс: `RsbSfInv`

```rsl
RsbSfInv ()
```

## Процедура: `SfDeleteBasObj`

```rsl
SfDeleteBasObj (sfbasobj:Record, Tbfile, TRecHandler):Integer
```

## Процедура: `SfFindBasObj`

```rsl
SfFindBasObj (PeriodCommID:Integer, BaseObjectType:Integer, BaseObjectID:Integer, sfbasobj:Record, Tbfile, TRecHandler):Integer
```

## Процедура: `SfGetBasObj`

```rsl
SfGetBasObj ([PeriodCommID:Integer, ] [, BaseObjectType:Integer] [, BaseObjectID:Integer] [, SingCommID:Integer] sfbasobj:Record, Tbfile, TRecHandler):Integer
```

## Процедура: `SfInsertBasObj`

```rsl
SfInsertBasObj (sfbasobj:Record, Tbfile, Trechandler):Integer
```

## Процедура: `SfUpdateBasObj`

```rsl
SfUpdateBasObj (sfbasobj: Record, Tbfile, Trechandler):Integer
```

## Процедура: `SfFillPaymentBySI`

```rsl
SfFillPaymentBySI (si: Record, prop_type: Integer, pmpaym: Record, pmprop: Record, pmrmprop: Record):Integer
```

## Процедура: `SfGetSI`

```rsl
SfGetSI (ObjectType:Integer, com:File, Record, Tbfile, TRecHandlerVariant, sidebet:File, Record, Tbfile, TRecHandlerVariant, sicredit:File, Record, Tbfile, TRecHandlerVariant):Integer
```

## Процедура: `SfSelectSETTACC`

```rsl
SfSelectSETTACC (FIID:Integer, ObjectType:Integer, Object:Record, settacc: Record, found:Bool [, FeeType:Integer] [, FeeNumber:Integer] [, ForContractor:Bool] [, Branch:Integer]):Integer
```

## Процедура: `SfCalcOprSfCom`

```rsl
SfCalcOprSfCom (ContrID:Long, commNumber:Integer [, doc:Memaddr], docKind:Integer, docSum:Money, docFIID:Money [, beginDate:Date] [, endDate:Date], paySum:Money, taxSum:Money):Bool
```

## Процедура: `SfComCheckAttr`

```rsl
SfComCheckAttr (feeType:Integer, commNumber:Integer, numParm:Integer, strVal:String):Bool
```

## Процедура: `SfFindOperCommission`

```rsl
SfFindOperCommission (operID:Integer, stepID:Integer, feeType:Integer, commNumber:Integer [, commBuff:Record]):Bool
```

## Процедура: `SfFindSuperiorComiss`

```rsl
SfFindSuperiorComiss (FeeType:Integer, CommNumber:Integer, IncComm: Record):Bool
```

## Процедура: `SfGetCategoryAccountsByPmPaym`

```rsl
SfGetCategoryAccountsByPmPaym (FeeType:Integer, DefComID:Integer, AccTax: File, Record, Tbfile, Trechandler, AccTransit: File, Record, Tbfile, Trechandler, isTransitAcc:Integer, PayNDS:Integer, MultyCarryMetodID:Integer [, SfComiss: File, Record, Tbfile, Trechandler]): Integer
```

## Процедура: `SfGetComiss`

```rsl
SfGetComiss (FeeType:Integer, CommNumber:Integer, sfcomiss:Record):Bool
```

## Процедура: `SfGetConCom`

```rsl
SfGetConCom (contrID:Integer, FeeType:Integer, concom:Record):Bool
```

## Процедура: `SfGetDefCom`

```rsl
SfGetDefCom (ContrID:Integer, FeeType:Integer, CommNumber:Integer, DateFee:Date, sfdefcom:Record):Bool
```

## Процедура: `SfGetOperCommission`

```rsl
SfGetOperCommission (operID:Integer, Step_ID:Integer, commBuff: Record [, PayCommiss:Bool]):Bool
```

## Процедура: `SfIsExistPeriodCalcComiss`

```rsl
SfIsExistPeriodCalcComiss (ContrID : Integer, [Date : Date]) : Bool
```

## Процедура: `SfIsExistPeriodComiss`

```rsl
SfIsExistPeriodComiss (ID:Integer, CheckRetriment:Bool [, IsClient:Bool] [, IsAgent:Bool] [, IsClientInPay:Bool] [, IsClientInStart:Bool]):Bool
```

## Процедура: `SfPayPeriodCommission`

```rsl
SfPayPeriodCommission (p_Date:Date, p_ContrlD:Integer, p_CommNumber:Integer):Integer
```

## Процедура: `CreateSfSrvDoc`

```rsl
CreateSfSrvDoc(sfsrvdoc:Record [, curonly:Bool] [, dep:String] [, fi:String] [, account:String] [, Oper:String]):Integer
```

## Процедура: `ExecChangeSfContrPlan`

```rsl
ExecChangeSfContrPlan (SfContrID:Integer, SfPlanID:Integer, StartDate:Date):Integer
```

## Процедура: `GetBranchForContr`

```rsl
GetBranchForContr (ServKind:Integer, ObjectBuf:Record, Branch:Integer)
```

## Процедура: `GetInvoiceRest`

```rsl
GetInvoiceRest (InvoiceID:Long, ValueDate:Date, PayFIID:Long, Direction:Integer, arrayInvRests:Array):Integer
```

## Процедура: `InsertSumList`

```rsl
InsertSumList (sfbassum: Record):Integer
```

## Процедура: `RunSfSrvDoc`

```rsl
RunSfSrvDoc(sfSrvDocID:Integer [, RepFileName:String]):Integer
```

## Процедура: `SfCalcAlGetUserParm`

```rsl
SfCalcAlGetUserParm (sfcalcal:Record, name:String, type:Integer, value:Variant):Integer
```

## Процедура: `SfContrChangeSfPlan`

```rsl
SfContrChangeSfPlan(SfContrID:Integer, SfPlanID:Integer, FromDate:Date, UsedRenewable:Bool):Integer
```

## Процедура: `SfCreateSfContr`

```rsl
SfCreateSfContr(Contr:Record, SfPlanID:Integer, UnionContrID:Integer):Integer
```

## Процедура: `создания`

```rsl
договора обслуживания.
```

**Параметры:**

Contr – заполненная таблица sfcontr.dbt.
SfPlanID – идентификатор записи sfplan.dbt (может иметь нулевое значение).
UnionContrID – идентификатор сводного договора обслуживания (может иметь нулевое
значение).

**Возвращаемое значение:**



## Процедура: `SfCreateUnionContr`

```rsl
SfCreateUnionContr(UnionContr:Record):Integer
```

## Процедура: `SfDeleteDLSSI`

```rsl
SfDeleteDLSSI(DlSsiID:Integer):Integer
```

## Процедура: `SfDeleteSfContr`

```rsl
SfDeleteSfContr(SfContrID:Integer):Integer
```

## Процедура: `SfDeleteSfSSI`

```rsl
SfDeleteSfSSI(SfContrID:Integer, SettAccID:Integer):Integer
```

## Процедура: `SfDeleteSfUnionContr`

```rsl
SfDeleteSfUnionContr(UnionContrID:Integer):Integer
```

## Процедура: `поиска`

```rsl
и заполнения структуры sfspidlins.rec используемой в процедуре создания и обновления СПИ для начисления доходов по ценным бумагам (SFSaveDLSSI ).
```

**Параметры:**

DlSsiID – идентификатор записи dlssi.dbt.
Spidlins –  заполненная запись sfspidlins.rec
.

**Возвращаемое значение:**



## Процедура: `SfFindSFSPIINSREC`

```rsl
SfFindSFSPIINSREC(SfContrID:Integer, SettAccID:Integer, spiins:Record):Integer
```

## Процедура: `SfSaveDLSSI`

```rsl
SfSaveDLSSI(SfContrID:Integer, UnionContrID:Integer, spidlins:Record):Integer
```

## Процедура: `SfSaveSfSSI`

```rsl
SfSaveSfSSI(SfContrID:Integer, spiins:Record):Integer
```

## Процедура: `SfUnionContrChangeSfPlan`

```rsl
SfUnionContrChangeSfPlan(UnionContrID:Integer, SfPlanID:Integer, FromDate:Date):Integer
```

## Процедура: `SfUpdateSfContr`

```rsl
SfUpdateSfContr(Contr:Record):Integer
```

## Процедура: `SfUpdateSfUnionContr`

```rsl
SfUpdateSfUnionContr(UnionContr:Record):Integer
```
