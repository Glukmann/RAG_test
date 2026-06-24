---
title: Loans_RSLprc
description: Процедуры и функции на языке RSL для модуля
category: RSL-процедуры
source: PDF-документация RS-Bank V.6
sections: 201
generated: true
---

## Класс: `TLoansCalcPercent`

```rsl
TLoansCalcPercent
```

## Процедура: `getCardEndDate`

```rsl
getCardEndDate (cardBranch:Integer, cardContractID:Integer):Date
```

## Процедура: `KartaLimit`

```rsl
KartaLimit (ObjID:Integer, ObjNum:Integer, Date:Date):Moneyl
```

## Процедура: `ОткрытьКарту`

```rsl
ОткрытьКарту (RegDate:Date, EndDate:Date, КарточныйСчет:String, IDВидаКарты:Integer, IDСубъекта:Integer, ДатаОтчета:Integer, Лимит:Double, Doublel, Money, КатегорияКачества:Integer, 0 Качество обеспечения:Integer, СрокПогашения:Integer [, Филиал:Integer] [, Reference:Integer] [, RiskGroupRVP:Integer] [, KKSPerc:Double] [, RVPPerc:Double] [, Branch:Integer], [, RetailKarta:Integer]):IntegerОткрытьКарту (RegDate:Date, EndDate:Date, КарточныйСчет:String, IDВидаКарты:Integer, IDСубъекта:Integer, ДатаОтчета:Integer, Лимит:Double, Doublel, Money, КатегорияКачества:Integer, 0 Качество обеспечения:Integer, СрокПогашения:Integer [, Филиал:Integer] [, Reference:Integer] [, RiskGroupRVP:Integer] [, KKSPerc:Double] [, RVPPerc:Double] [, Branch:Integer], [, RetailKarta:Integer]):Integer
```

## Процедура: `УдалитьКарту`

```rsl
УдалитьКарту(IDКарты:Integer):Bool
```

## Процедура: `CalcDuty`

```rsl
CalcDuty (ObjN:Integer, OpDate:Date, TypeOp:Integer):Integer
```

## Процедура: `DeleteContract`

```rsl
DeleteContract(IDДоговора:Integer):Bool
```

## Процедура: `GetSynchMethod`

```rsl
GetSynchMethod(objectType:integer):String
```

## Процедура: `GetSynchState`

```rsl
GetSynchState():Bool
```

## Процедура: `GetSynchTimeout`

```rsl
GetSynchTimeout(objectType:integer):integer
```

## Процедура: `GetSynchUrl`

```rsl
GetSynchUrl(objectType:integer):String
```

## Процедура: `CarryNextOpStage`

```rsl
CarryNextOpStage (ID:Integer, Date:Date):Bool
```

## Процедура: `DeleteOperation`

```rsl
DeleteOperation(CreditNumber: Integer, OpType: Integer, OpDate: Date):Bool В зависимости от переданных параметров процедура удаляет последнюю операцию заданного видана дату по договору или удаляет операцию по указанному идентификатору OpType.
```

**Параметры:**

CreditNumber – идентификатор кредитного договора.
OpType – идентификатор вида операции (поле t_TypeOperNumber таблицы dtype_op_dbt).
OpDate – дата операции.

**Возвращаемое значение:**



## Процедура: `ExistsOperation`

```rsl
ExistsOperation (ObjectTypeID:Integer, ObjectID:Integer, SystOperationID:Integer):Bool
```

## Процедура: `ExistsOperationForCredNum`

```rsl
ExistsOperationForCredNum(CreditNumber:Integer [, SysopID:Integer] [, TypeOpID:Integer]):Integer
```

## Процедура: `GetCountDocTmp`

```rsl
GetCountDocTmp (IsDeleted:Integer, ДатаДокумента:Date): Integer
```

## Процедура: `GetExternDocument`

```rsl
GetExternDocument (IDОперации:Integer): Integer
```

## Процедура: `GetLastCrdOpID`

```rsl
GetLastCrdOpID (ObjectTypeID:Integer, ObjectNumber:Integer, SysOp:Integer, StageID:Integer)
```

## Процедура: `GetLastCredOperID_ForPlanPay`

```rsl
GetLastCredOperID_ForPlanPay (НомерОбъекта:Integer, [ВидОбъекта:Integer, ] Тип Графика:Integer):Integer
```

## Процедура: `GetLastGraphLimOpID`

```rsl
GetLastGraphLimOpID (ObjectTypeID:Integer, ObjectNumber:Integer, TypeGraphLim:Integer):Integer
```

## Процедура: `GetMO_OperID`

```rsl
GetMO_OperID():Integer
```

## Процедура: `ИзменитьРегистр`

```rsl
ИзменитьРегистр (ВидОбъекта:Integer, НомерОбъекта:Integer, ВидРегистра:Integer, IDДокумента:Integer, Сумма: Money, MoneyL, ID операции:Integer [, ChangeDate:Date]):Integer
```

## Процедура: `СуммаДокументов`

```rsl
СуммаДокументов (CreditNumber:Integer, CurCode:Integer, FirstDate:Date, LastDate:Date, SysOpType:Integer)
```

## Процедура: `УстановитьНедоплаты`

```rsl
УстановитьНедоплаты (ВидОбъекта:Integer, НомерОбъекта:Integer, ВидРегистра:Integer, ВидНедоплаты:Integer, Сумма:MoneyL):Integer
```

## Процедура: `SQLCalcRezSum`

```rsl
SQLCalcRezSum (ObjID:Integer, ObjN:Integer, OpDate:Date, Rez_data:Record, recalc:Bool, ErrStr:String, checkval:Bool, reztype:Integer):Integer
```

## Процедура: `НомерПортфеляОбязательства`

```rsl
НомерПортфеляОбязательства (ВидОбъекта:Integer, НомерОбъекта:Integer [, Дата операции:Date] [, НомерПортфеля:Integer]):Bool
```

## Процедура: `СуммаПортфеля`

```rsl
СуммаПортфеля (НомерПортфеля:Integer [, ДатаРасчета:Date] [, НомерРегистра:Integer]): MoneyL
```

## Процедура: `ЭлементРасчетнойБазы`

```rsl
ЭлементРасчетнойБазы (ObjectTypeID:Integer, ObjectNumber:Integer, RestDate:Date, RegID:Integer, CaseType:Integer):MoneyL
```

## Процедура: `GetMO_ErrorID`

```rsl
GetMO_ErrorID ():Integer
```

## Процедура: `GetMO_LoansError`

```rsl
GetMO_LoansError ():String
```

## Процедура: `ОстатокОткрытыхСО`

```rsl
ОстатокОткрытыхСО (IDДоговора:Integer, ВидРегистра:Integer, ДатаОстатка:Date, [СтатусОбъекта:Integer, ] ТипОбязательства:Integer):Money
```

## Процедура: `ОстатокСО`

```rsl
ОстатокСО (DutyID:Integer, ВидРегистра:Integer, ДатаОстатка:Date):Money
```

## Процедура: `DeleteSPIAccount`

```rsl
DeleteSPIAccount(ObjID:Integer, ObjN:Integer, SetAccID:Integer):Integer
```

## Процедура: `InsertSPIAccount`

```rsl
InsertSPIAccount(ObjID:Integer, ObjN:Integer, IgCrdAcc:Record, IgSetAcc:Record):Integer
```

## Процедура: `UpdateSPIAccount`

```rsl
UpdateSPIAccount(ObjID:Integer, ObjN:Integer, IgCrdAcc:Record, IgSetAcc:Record):Integer
```

## Процедура: `КлючеватьСчет`

```rsl
КлючеватьСчет (НомерСчета:String [,Chapter:String] [,ObjectTypeID:String] [,ObjectNumber:String])
```

## Процедура: `КлючеватьСчетПоФилиалу`

```rsl
КлючеватьСчетПоФилиалу(НомерСчета:String [,Chapter:String] [,DprtID:Integer])
```

## Процедура: `НайтиСчет`

```rsl
НайтиСчет (ВидОбъектаШаг:Integer, КатегорияСчета:Integer, ВидОбъекта:Integer, НомерОбъекта:Integer, КодВалюты:Integer):String
```


```rsl
определяет номер счета указанного типа (категории) по объекту.
```

**Примечание:**



## Процедура: `ОстатокНаСчете`

```rsl
ОстатокНаСчете (ВидОбъекта:Integer, НомерОбъекта:Integer, КодВалюты:Integer, КатегорияСчета:Integer, ДатаОстатка:Date):Money
```

## Процедура: `СуммаДебетовыхОборотов`

```rsl
СуммаДебетовыхОборотов (НомерСчета:String, ВалютаСчета:Integer, ДатаНачала:Date, ДатаОкончания:Date):Money
```

## Процедура: `СуммаКредитовыхОборотов`

```rsl
СуммаКредитовыхОборотов (НомерСчета:String, ВалютаСчета:Integer, ДатаНачала:Date, ДатаОкончания:Date):Money
```

## Процедура: `ФильтрДокументаПоСчету`

```rsl
ФильтрДокументаПоСчету (DocAccID:Integer):Bool С помощью процедуры выполняется фильтрация документов по счету.
```

**Параметры:**

DocAccID – идентификатор документа по счету.

**Возвращаемое значение:**



## Процедура: `CloseLoansCommonFiles`

```rsl
CloseLoansCommonFiles ()
```

## Процедура: `CloseLoansFilesAll`

```rsl
CloseLoansFilesAll ()
```

## Процедура: `OpenLoansCommonFiles`

```rsl
OpenLoansCommonFiles ()
```

## Процедура: `ПроверкаВыполненностиЭтапа`

```rsl
ПроверкаВыполненностиЭтапа (): Bool
```

## Процедура: `CalcAvailableLimitFromMacro`

```rsl
CalcAvailableLimitFromMacro (ObjNum:Integer, OpDate:Integer, SysOpType:Integer, OpType:Integer, Rest:Moneyl):Money
```

## Процедура: `CalcDischSum`

```rsl
CalcDischSum (ObjID:Integer, ObjN:Integer, TypeOperID:Integer, OptNopID:Integer, PrmTSumID: Integer, DateOp:Date, BegDate:Date, EndDate:Date, ContextType:Integer, ResSum:Money):Integer
```

## Процедура: `CalcDischType`

```rsl
CalcDischType (ObjID:Integer, ObjN:Integer, DateOp:Date, TypeOp:Integer, OptNopID:Integer, BegDate:Date, EndDate:Date, ContextType:Integer, S_np_treb:Moneyl, S_treb:Moneyl, S_tek:Moneyl, S_r:Moneyl, S_n:Moneyl, S_np:Moneyl):Integer
```

## Процедура: `CheckDisch`

```rsl
CheckDisch (ObjID:Integer, ObjN:Integer, OptNopID:Integer, PrmTSumID:Integer, DateOp:Date, BegDate:Date, EndDate:Date, ContextType:Integer, bool_res:Integer):Integer
```

## Процедура: `GetAccountBuffer`

```rsl
GetAccountBuffer ():Bool
```

## Процедура: `GetCNum`

```rsl
GetCNum ():Integer
```

## Процедура: `GetEnsObjSum`

```rsl
GetEnsObjSum (objid:Integer, ensobjid:Integer, OperDate:Date, Sum1:MoneyL, Sum2:MoneyL, Sum3:MoneyL):MoneyL
```

## Процедура: `GetMarkRate`

```rsl
GetMarkRate (CurCode:Integer, DateRate:Date): Double С помощью процедуры определяется основной курс валюты из базовой подсистемы ИБС RS-Bank на указанную дату.
```

**Параметры:**

CurCode – идентификатор вида валюты в справочнике валют.
DateRate – дата, на которую определяется курс.

**Возвращаемое значение:**



## Процедура: `GetNameAlg`

```rsl
GetNameAlg(Kind:Integer, Item:Integer):String
```

## Процедура: `GetOperBrigade`

```rsl
GetOperBrigade ():Integer
```

## Процедура: `GetTrffRateStr`

```rsl
GetTrffRateStr (ObjID:Integer, ObjN:Integer, TypeRateID:Integer, CalcDate:DATE):String
```

## Процедура: `InsertClaimStatus`

```rsl
InsertClaimStatus (ClaimID:Integer, StatusID:Integer):Integer
```

## Процедура: `IsDilCondExec`

```rsl
IsDilCondExec (ObjectID:Integer, ObjectNumber:Integer, GraphID:Integer, CredOperID:Integer, AllExec:Integer):Integer
```

## Процедура: `Loans_UserTypeCredit`

```rsl
Loans_UserTypeCredit (ВидыКредитов:String): String
```

## Процедура: `ListDepart`

```rsl
ListDepart ():Bool
```

## Процедура: `LoansError`

```rsl
LoansError (Сообщение:Integer, String [, TypeObj:Integer])
```

## Процедура: `NumFNCash`

```rsl
NumFNCash (): Integer
```

## Процедура: `RetailApplicationKey`

```rsl
RetailApplicationKey (TypeDoc:Integer):String
```

## Процедура: `RSL_GetRegRest_Date`

```rsl
RSL_GetRegRest_Date (RegID:Integer, ДатаОстатка:Date):Money
```

## Процедура: `по`

```rsl
уникальному идентификатору экземпляра регистра возвращает его остаток на дату.
```

**Параметры:**

RegID – идентификатор экземпляра регистра (поле t_ID таблицы dlcusreg_dbt).
ДатаОстатка – дата, на которую требуется получить остаток.

**Возвращаемое значение:**



## Процедура: `RSL_GetRegRest_Date_`

```rsl
RSL_GetRegRest_Date_ ():MoneyL
```

## Процедура: `SendBki`

```rsl
SendBki (BkiID:Integer, CreditNumber:Integer, SendKind:Integer, SendDate:Date [, Patch:String] [, FName:String])
```

## Процедура: `SetLoansGroupMode`

```rsl
SetLoansGroupMode (NewValue:Bool)
```

## Процедура: `SetOperDprt`

```rsl
SetOperDprt (НовоеЗначениеФилиала:Integer):Integer
```

## Процедура: `SQLRezFlagMacro`

```rsl
SQLRezFlagMacro (ObjID:Integer, ObjN:Integer, OpDate:Date):String
```

## Процедура: `ДеньВыносаНаПросрочку_2`

```rsl
ДеньВыносаНаПросрочку(ДеньПросрочки:Integer, Дата:Date):Integer
```

## Процедура: `ДобавитьПараметры`

```rsl
ДобавитьПараметры (Операция:Integer, Имя параметра:String, Значение:Variant)
```

## Процедура: `ДопровестиНедопроведенныйДокумент`

```rsl
ДопровестиНедопроведенныйДокумент (Reference:Integer):Integer
```

## Процедура: `ИзменитьНедоплаты`

```rsl
ИзменитьНедоплаты (ВидОбъекта:Integer, НомерОбъекта:Integer, ВидРегистра:Integer, ВидНедоплаты:Integer, Сумма:Money): Integer
```

## Процедура: `ОстатокРегистра`

```rsl
ОстатокРегистра (ВидОбъекта:Integer, НомерОбъекта:Integer, ВидРегистра:Integer, ДатаОстатка:Date): Money
```

## Процедура: `ПризнаниеДоходов`

```rsl
ПризнаниеДоходов ():Record
```

## Процедура: `ПроверитьГруппу`

```rsl
ПроверитьГруппу (НомерГруппы:Integer): Integer
```

## Процедура: `ПроверитьГруппуИФилиал`

```rsl
ПроверитьГруппуИФилиал (НомерГруппы:Integer, НомерФилиала:Integer): Integer
```

## Процедура: `РасчетЗадолженности`

```rsl
РасчетЗадолженности (ВидОбъекта:Integer, НомерОбъекта:Integer, ВидЗадолженности:Integer, ДатаРасчета:Date): Bool
```

## Процедура: `РезидентОффшорнойЗоны`

```rsl
РезидентОффшорнойЗоны (PartyID:Integer [, Дата:Date]): Bool
```

## Процедура: `СоздатьДокумент`

```rsl
СоздатьДокумент (Документ:Record, IDДокумента:Integer):Integer
```

## Процедура: `СоздатьСводныйДокумент`

```rsl
СоздатьСводныйДокумент (СводныйДокумент:Record): Bool
```

## Процедура: `Loans_FindAcCrd`

```rsl
Loans_FindAcCrd (iKeyNumber:Integer, [AccID:Integer, ] [ObjectNumber:Integer, ] [AccountNumber:String, ] [CreditAccountType:Integer, ] [CurCode:Integer, ] [Chapter:Integer, ] [RegDate:Date, ] acc_crd:Record):Bool
```

## Процедура: `Loans_FindAttrObject`

```rsl
Loans_FindAttrObject (KeyNum:Integer, AttrID:Integer, ObjID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindCASE`

```rsl
Loans_FindCASE (BriefcaseID:Integer, buff:Record):Bool
```

## Процедура: `обеспечивает`

```rsl
поиск портфеля в таблице dlbrfcase_dbt.
```

**Параметры:**

BriefcaseID – идентификатор искомого портфеля.
buff – буфер для найденной записи (TLoansCASE).

**Возвращаемое значение:**



## Процедура: `Loans_FindCatType`

```rsl
Loans_FindCatType (iKeyNumber:Integer, [AccCategID:Integer, ] [CreditTypeID_Ref:Integer, ] [AccCategType:Integer, ] [CurCode:Integer, ] cat_type:Record):Bool
```

## Процедура: `Loans_FindChangeLimit`

```rsl
Loans_FindChangeLimit (CreditNumber_Ref:Integer, Type:Integer, Date:Date, Buff:Record):Bool
```

## Процедура: `Loans_FindCopStage`

```rsl
Loans_FindCopStage (CredOperID:Integer, Date:Date, buff:Record):Bool
```

## Процедура: `Loans_FindCrdContract`

```rsl
Loans_FindCrdContract (CreditNumber:Integer, credit_c:Record):Bool
```

## Процедура: `Loans_FindCrdOp`

```rsl
Loans_FindCrdOp (CredOperID:Integer, crd_op:Record):Bool
```

## Процедура: `Loans_FindCredCom`

```rsl
Loans_FindCredCom (CredComID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindCreditClaim`

```rsl
Loans_FindCreditClaim (CreditNumber_Ref:Integer, ClaimKind:Integer, buff: Record):Bool
```

## Процедура: `Loans_FindCreditSum`

```rsl
Loans_FindCreditSum (FirstDate:Date, LastDate:Date, CurCode:Integer, AccountNumber:String):MoneyL
```

## Процедура: `Loans_FindDebetSum`

```rsl
Loans_FindDebetSum (FirstDate:Date, LastDate:Date, CurCode:Integer, AccountNumber:String):MoneyL
```

## Процедура: `Loans_FindDocAcc`

```rsl
Loans_FindDocAcc (iKeyNum:Integer [, ApplicationKey:String] [, ApplicationKind:Integer] [, DocAccID:Integer] [, doc_acc:Record]):Bool
```

## Процедура: `Loans_FindDocDuty`

```rsl
Loans_FindDocDuty (DutyOffDocID:Integer, CredOperID_Ref:Integer, buff:Record):Bool
```


```rsl
осуществляет поиск документа по погашению (ddoc_duty_dbt).
```

**Параметры:**

DutyOffDocID – идентификатор записи о виде кредита.
CredOperID – ссылка на операцию.
buff – буфер для записи результата (docduty).

**Возвращаемое значение:**



## Процедура: `Loans_FindDuty`

```rsl
Loans_FindDuty (DutyID_Ref:Integer, duty_crd:Record):Bool
```

## Процедура: `Loans_FindDutyOp`

```rsl
Loans_FindDutyOp (CredOperID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindDutyRest`

```rsl
Loans_FindDutyRest (DutyID_Ref:Integer, RestDate:Date, DUTYREST:Record):Bool
```

## Процедура: `Loans_FindEnsContract`

```rsl
Loans_FindEnsContract (EnsContractID:Integer, enscontr:Record):Bool
```

## Процедура: `Loans_FindEnsObject`

```rsl
Loans_FindEnsObject (EnsTypeID_Ref:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindEnsType`

```rsl
Loans_FindEnsType (EnsTypeID:Integer, buf:Record):Bool
```

## Процедура: `Loans_FindGPayOp`

```rsl
Loans_FindGPayOp (CredOperID:Integer, Type:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindHistAcc`

```rsl
Loans_FindHistAcc (KeyNum:Integer, ID:Integer, ObjectTypeID:Integer, ObjectNumber:Integer, CreditAccountType:Integer, CurCode:Integer, RegDate:Date, buff:Memaddr):Bool
```

## Процедура: `Loans_FindHistLim`

```rsl
Loans_FindHistLim (ВидОбъекта:Long, НомерОбъекта:Long, Дата:Date, Запись:Record):Bool
```

## Процедура: `Loans_FindKarta`

```rsl
Loans_FindKarta (CreditNumber:Integer, CREDIT:Record):Bool
```

## Процедура: `Loans_FindLAH`

```rsl
Loans_FindLAH (AlgID:Record, Date:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCA`

```rsl
Loans_FindLCA (AlgID:Record, buff:Record):Bool
```

## Процедура: `Loans_FindLCAO`

```rsl
Loans_FindLCAO (ObjectID:Integer, TypeAlgID:Integer, buff:Integer):Bool
```

## Процедура: `Loans_FindLCO`

```rsl
Loans_FindLCO (ObjectID:Integer, TypeAcCred:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCP`

```rsl
Loans_FindLCP (ObjectID:Integer, TypeRateID:Integer, buff:Integer):Bool
```

## Процедура: `Loans_FindLCR`

```rsl
Loans_FindLCR (RateID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCSR`

```rsl
Loans_FindLCSR (UsRegID:Integer, CredOperID:Integer, Number:Integer, Date:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCTA`

```rsl
Loans_FindLCTA (TypeAlgID:Integer, Buff:Integer):Bool
```

## Процедура: `Loans_FindLCTU`

```rsl
Loans_FindLCTU (TypeRateID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCUA`

```rsl
Loans_FindLCUA (ObjectID:Integer, CredObjID:Integer, TypeAlgID:Integer, AlgID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLCUR`

```rsl
Loans_FindLCUR (ObjectID:Integer, CredObjID:Integer, TypeRateID:Integer, RateID:Integer, buff:Record [, OnlyCurrObj:Bool]):Bool
```

## Процедура: `Loans_FindLCURG`

```rsl
Loans_FindLCURG (ObjectID:Integer, ObjectNumber:Integer, RegID:Integer, ID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindLRH`

```rsl
Loans_FindLRH (RateID:Integer, Date:Date, buff:Record):Bool
```

## Процедура: `Loans_FindLRO`

```rsl
Loans_FindLRO (ObjectID:Integer, RegID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindObject`

```rsl
Loans_FindObject (ID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindOpStage`

```rsl
Loans_FindOpStage (StageID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindParentDuty`

```rsl
Loans_FindParentDuty (DutyID_Ref:Integer, duty_crd:Record):Bool
```

## Процедура: `Loans_FindPayOp`

```rsl
Loans_FindPayOp (CredOperID:Integer, buff:Object):Bool
```

## Процедура: `Loans_FindPercDay`

```rsl
Loans_FindPercDay (ID_Ref:Integer, RateID:Integer, PercDate:Date, buff:Record):Bool
```

## Процедура: `Loans_FindPlanPay`

```rsl
Loans_FindPlanPay (ObjectTypeID_Ref:Integer, ObjectID_Ref:Integer, Type:Integer, CredOperID_Ref:Integer, DatePay:Date, DateExp:Date, buff:RECORD):Bool
```

## Процедура: `Loans_FindPNPReg`

```rsl
Loans_FindPNPReg (IDРегистра:Integer, ВидРегистраНедоплат:Integer, БуферДляЗаписиНайденного:Record):Bool
```

## Процедура: `поиска`

```rsl
записи по регистру недоплат (запись в таблице dpaynopay_dbt) для заданного экземпляра регистра по объекту.
```

**Параметры:**

IDРегистра – идентификатор экземпляра регистра по объекту (ссылка на поле t_ID
таблицы dlcusreg_dbt).
ВидРегистраНедоплат – вид регистра недоплат.
БуферДляЗаписиНайденного – структура для найденной записи, имеющая структуру,
аналогичную структуре таблицы dpaynopay_dbt.

**Возвращаемое значение:**



## Процедура: `Loans_FindPost`

```rsl
Loans_FindPost (PostID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindPostOper`

```rsl
Loans_FindPostOper (PostID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindRateVal`

```rsl
Loans_FindRateVal (ObjectID:Integer, CredObjID:Integer, RateUse:Integer, RateDate:Date [, OnlyCurrObject:Bool]):DoubleL
```

## Процедура: `Loans_FindRebillingMotive`

```rsl
Loans_FindRebillingMotive (ChangeID:Integer, buff:String):Bool
```

## Процедура: `Loans_FindRestAcc`

```rsl
Loans_FindRestAcc (Account:String, CurCode:Integer, Date:Date):MoneyL
```

## Процедура: `Loans_FindRestAccCrd`

```rsl
Loans_FindRestAccCrd (ObjectTypeID:Integer, ObjectNumber:Integer, Type:Integer, CurCode:Integer, Date:Date):MoneyL
```

## Процедура: `Loans_FindRezOp`

```rsl
Loans_FindRezOp (CredOperID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindRiskGroup`

```rsl
Loans_FindRiskGroup (NumberRiskGroup:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindSbAcc`

```rsl
Loans_FindSbAcc (CurCode:Integer, AccountNumber:String, sb_acc:Record):Bool
```

## Процедура: `Loans_FindSRG`

```rsl
Loans_FindSRG (ID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindStagePost`

```rsl
Loans_FindStagePost (TopStageID:Integer, PostID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindSysTypeOp`

```rsl
Loans_FindSysTypeOp (SystemOperationID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindTemplate`

```rsl
Loans_FindTemplate (ObjID:Integer, CrType:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindTopStage`

```rsl
Loans_FindTopStage (TopStageID:Integer, TypeOperID:Integer, StageID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindTypeAcCred`

```rsl
Loans_FindTypeAcCred (TypeAcCred:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindTypeCrd`

```rsl
Loans_FindTypeCrd (iKeyNumber:Integer, Kind:String, CurCode:Integer, CreditTypeID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindTypeOp`

```rsl
Loans_FindTypeOp (TypeOperNumber:Integer, TypeOperID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindTypeOpStep`

```rsl
Loans_FindTypeOpStep (TypeOperID_Ref:Integer, StepNumber:Integer, StepID:Integer, StepID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindUsField`

```rsl
Loans_FindUsField (UsFieldID:Integer, Buff:Record):Bool
```

## Процедура: `Loans_FindUsFieldVal`

```rsl
Loans_FindUsFieldVal (UsFObjTypeID:Integer, Date:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindUsFObjType`

```rsl
Loans_FindUsFObjType (UsFObjTypeID:Integer, buff:Record):Bool
```

## Процедура: `Loans_FindUsRateDate`

```rsl
Loans_FindUsRateDate (UsRateID:Integer, Date:Integer):Integer
```

## Процедура: `Loans_FindUsRegDate`

```rsl
Loans_FindUsRegDate (UsRegID:Integer, Date:Date):Integer
```

## Процедура: `Loans_GetAlgIDForRate`

```rsl
Loans_GetAlgIDForRate (ObjID:Integer, ObjN:Integer, RateID:Integer [, OnlyCurrObject:Bool] [, ItsTypeRate:Integer]):Integer
```

## Процедура: `Loans_FreeGlobalData`

```rsl
Loans_FreeGlobalData (NameGlobalData:String):Bool
```

## Процедура: `Loans_ReadGlobalData`

```rsl
Loans_ReadGlobalData (NameGlobalData:String, ValGlobalData:Variant):Bool
```

## Процедура: `Loans_WriteGlobalData`

```rsl
Loans_WriteGlobalData (NameGlobalData:String, ValGlobalData:Variant):Bool
```

## Процедура: `ViewPanel`

```rsl
ViewPanel(ObjID: Integer, ObjN: Integer): Bool
```

## Процедура: `ВвестиПериодДат`

```rsl
ВвестиПериодДат (ДатаНачала:Date, ДатаОкончания:Date [, ЗаголовокПанели:String]):Bool
```

## Процедура: `УстановитьВидыКредитов`

```rsl
УстановитьВидыКредитов ([TypeCurCode:Integer, ] [CurCode:Integer, ] [Crd_Kind:Integer]) Integer
```

## Процедура: `УстановитьДоговора`

```rsl
УстановитьДоговора(WithDraft:Bool, CreditState:Integer):Bool
```

## Процедура: `УстановитьКлиентов`

```rsl
УстановитьКлиентов (Filter:Integer):Integer
```

## Процедура: `УстановитьТипыСчетов`

```rsl
УстановитьТипыСчетов ():Integer
```

## Процедура: `УстановитьФилиалы`

```rsl
УстановитьФилиалы ():Bool
```

## Процедура: `Loans_ListLCP`

```rsl
Loans_ListLCP (ObjectID:Integer, CredObjID:Integer, buff:Record):Bool С помощью процедуры осуществляется выбор из списка связи объектов и ставок.
```

**Параметры:**

ObjectID – идентификатор вида объекта.
CredObjID – идентификатор экземпляра объекта.
buff – буфер для записи результата (запись таблицы dlcusrate_dbt).

**Возвращаемое значение:**



## Процедура: `НазваниеНаселенногоПункта`

```rsl
НазваниеНаселенногоПункта (depclnt:Object):String
```

## Процедура: `СтажРаботы`

```rsl
СтажРаботы (ClientID_Ref:Integer, SeniorityDate:Date): Integer
```

## Процедура: `СтажРаботыВОрганизации`

```rsl
СтажРаботыВОрганизации (Client_Id:Integer, Дата:Date, PeriodType:String): Integer
```

## Процедура: `DutyInCases`

```rsl
DutyInCases (ObjectID, ObjectNumber, OperDate, Type): Integer
```

## Процедура: `GetAttrID`

```rsl
GetAttrID (ObjectType:Integer, ObjectID:Integer, GroupID:Integer, Дата:Date): Integer
```

## Процедура: `GetCalcGPay`

```rsl
GetCalcGPay (ObjectType:Integer, ObjectID:Integer, CurCode:Integer, calcgpay:Object): Bool
```

## Процедура: `GetClientSex`

```rsl
GetClientSex(CodClient:Integer): String
```

## Процедура: `GetHistoryClient`

```rsl
GetHistoryClient(CodClient:Integer, Hdate:Date):String
```

## Процедура: `GetPlanFirstDate`

```rsl
GetPlanFirstDate(ObjectType:Integer, ObjectID:Integer, CurCode:Integer, PayType:Integer): Date
```

## Процедура: `GetShortFIO`

```rsl
GetShortFIO (FullFIO:String): String
```

## Процедура: `GetUsFieldValue`

```rsl
GetUsFieldValue (ObjectType:Integer, ObjectID:Integer, FieldType:Integer, Дата:Date, GroupNum:Integer): Variant
```

## Процедура: `Int2Str`

```rsl
Int2Str (n:Integer, len:Integer): String
```

## Процедура: `IsInsider`

```rsl
IsInsider (CodClient:Integer): Bool
```

## Процедура: `LnGetRecordSet`

```rsl
LnGetRecordSet (Query:String, MsgPrint:Bool): Object
```

## Процедура: `MoneyToMString`

```rsl
MoneyToMString (Sum:moneyL, SumExtCurCode:Integer): String
```

## Процедура: `NextOpSystType`

```rsl
NextOpSystType (FirstSOp:Bool, ObjectNumber:Integer, Операции:TBFile, SystType:Integer, Направление:Bool, CurCode:Integer, ObjectType:Integer, StageOp:Integer, CredOperID:Integer, CURR_OBJ_ONLY:Bool): Bool
```

## Процедура: `NumAndStr`

```rsl
NumAndStr (Num:DoubleL, prec:Integer): String
```

## Процедура: `SetUsFieldValue`

```rsl
SetUsFieldValue (ObjectType:Integer, ObjectID:Integer, FieldType:Integer, FieldValue:Variant, IsOperating:bool, Дата:Date): Bool
```

## Процедура: `ГруппаРиска`

```rsl
ГруппаРиска (ВидОбъекта:Integer, НомерОбъекта:Integer, Тип: Integer, Дата:Date, Flag:Bool): String
```

## Процедура: `КачествоОбеспечения`

```rsl
КачествоОбеспечения (CreditNumber:Integer, EnsureDate:Date): Integer
```

## Процедура: `КоличествоДнейПросрочки`

```rsl
КоличествоДнейПросрочки (CreditNumber:Integer, CurCode:Integer, IDate:Date, OutParm1:Integer, OutParm2:Integer, ExpRestDate:Date, ExpPercDate:Date)
```

## Процедура: `КоличествоМесяцев`

```rsl
КоличествоМесяцев (date1:Date, date2:Date): Integer
```

## Процедура: `КоличествоПереоформлений`

```rsl
КоличествоПереоформлений (CreditNumber:Integer, IDate:Date, OutParm1:Integer, OutParm2:Integer)
```

## Процедура: `НомерСчета`

```rsl
НомерСчета (ObjectNumber:Integer, CurCode:Integer, AccountType:Integer, ObjectTypeID:Integer): String
```

## Процедура: `ОстатокКД`

```rsl
ОстатокКД (CreditNumber:Integer, ТипОстатка:Integer, Дата:Date): Moneyl
```

## Процедура: `ОстатокНаРегистре`

```rsl
ОстатокНаРегистре (ВидОбъекта:Integer, НомерОбъекта:Integer, Тип:Integer, Дата:Date): Moneyl
```

## Процедура: `ПогашеннаяСуммаКредита`

```rsl
ПогашеннаяСуммаКредита (CreditNumber:Integer, CurCode:Integer, FirstDate:Date, LastDate:Date): Moneyl
```

## Процедура: `СуммаЕдиновременногоПлатежа`

```rsl
СуммаЕдиновременногоПлатежа (IDОбязательства:Integer): Moneyl
```

## Процедура: `СуммаВыданногоКредита`

```rsl
СуммаВыданногоКредита (CreditNumber:Integer, CurCode:Integer, FirstDate:Date, LastDate:Date): Moneyl
```

## Процедура: `СуммаОбеспечения`

```rsl
СуммаОбеспечения (НомерДоговора:Integer, СистемныйВидОбеспечения:Integer, Тип:Integer, Дата:Date): Moneyl
```

## Процедура: `СуммаПоследнегоПлатежа`

```rsl
СуммаПоследнегоПлатежа (IDОбязательства:Integer): Moneyl
```

## Процедура: `LoansCalcPercent`

```rsl
LoansCalcPercent (ObjID:Integer, ObjN:Integer, RateID:Integer, begDate:Date, endDate:Date [, DutyStageID:Integer] [, DateOp:Date] [, ContextType]): Moneyl
```

## Процедура: `LoansCalcPercentExt`

```rsl
LoansCalcPercentExt(ObjID:Integer, ObjN:Integer, TrffTypeID:Integer, BegDate:Date, EndDate:Date [, DutyStageID:Integer] [, DateOp:Date] [, ContextType:Integer]):MoneyL
```

## Процедура: `Интервалы_постоянства_остатка`

```rsl
Интервалы_постоянства_остатка (ObjectID:Integer, ObjectN:Integer, SpVariableID:Integer, begDate:Date, endDate:Date, TYPE:Integer):Integer
```

## Процедура: `Интервалы_постоянства_остатка_1`

```rsl
Интервалы_постоянства_остатка_1 (CreditNumber:Integer, begDate:Date, endDate:Date, DAYS:Integer, TYPE:Integer):Integer
```

## Процедура: `Интервалы_Постоянства_Ставки`

```rsl
Интервалы_Постоянства_Ставки(ObjectID:Integer, ObjectN:Integer, TrffTypeID:Integer, begDate:Date, endDate:Date):Integer
```

## Процедура: `РасчетГрафикаПроцентов`

```rsl
РасчетГрафикаПроцентов(RateID:Integer, BegDate:Date, EndDate:Date, Ставка:Double [, Прогноз:Bool] [, IDТипаОбъекта:Integer] [, IDОбъекта:Integer] [, IDАлгоритма] [IDРегистра:Integer]):MoneyL
```
