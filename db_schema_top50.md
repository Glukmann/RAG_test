---
title: db_schema_top50
description: Структура базы данных RS-Bank
category: Схема-БД
source: PDF-документация RS-Bank V.6
sections: 50
generated: true
---

# Структура данных RS-Bank (извлечена из макросов)

Данный документ содержит информацию о таблицах, полях и SQL-запросах, извлечённых из реальных макросов RS-Bank.

## Таблица: `dl_tick`

**Бизнес-контекст:** DLNG Макрос: vab150.mac

**Поля (74):**

- `Agent`
- `AutoClose`
- `AvoirKind`
- `BONUSDATE`
- `BOfficeKind`
- `Blocked`
- `BofficeKind`
- `Bonus`
- `BonusDate`
- `BonusFIID`
- `BrokerContrID`
- `BrokerID`
- `CarryWrt`
- `ChangeDate`
- `Client`
- `ClientContr`
- `ClientContrID`
- `ClientID`
- `Code`
- `CommDate`
- `Comment`
- `Contractor`
- `Country`
- `CurDeal`
- `CurGet`
- `CurPay`
- `Date`
- `DealCode`
- `DealCodePS`
- `DealCodeTS`


## Таблица: `dl_order`

**Бизнес-контекст:** DLNG Макрос: vsb150st.mac

**Поля (53):**

- `AutoKey`
- `AutoProlongation`
- `AutuProlongation`
- `Beneficiary`
- `CloseAtEndDate`
- `ContractID`
- `ContractKind`
- `Contractor`
- `ContractorAccount`
- `ContractorAddress`
- `ContractorBankCode`
- `ContractorBankCorrAcc`
- `ContractorBankName`
- `ContractorName`
- `ContractorTaxCode`
- `CorrespBankCode`
- `CorrespBankName`
- `DateReceived`
- `DocKind`
- `HandOver`
- `HandingDate`
- `ID`
- `IsInverse`
- `Kind`
- `KindBnNode`
- `KindDwNode`
- `Kind_Operation`
- `NPT_LINKCALCDATE`
- `NPT_TAXCALCDATE`
- `OFBU`


## Таблица: `dl_leg`

**Бизнес-контекст:** DLNG Макрос: sp_imp.mac

**Поля (46):**

- `Base`
- `Basis`
- `BitMask`
- `CFI`
- `Cost`
- `D1`
- `D2`
- `DealID`
- `DeliveringFIID`
- `DepositID`
- `Diff`
- `Duration`
- `Expiry`
- `Formula`
- `ID`
- `IncomeRate`
- `LegID`
- `LegKind`
- `LegNumber`
- `Maturity`
- `MaturityIsPrincipal`
- `MoveDate`
- `NKD`
- `NKDFIID`
- `OperState`
- `PFI`
- `PayFIID`
- `PayRegTax`
- `Point`
- `Price`


## Таблица: `dl_comm`

**Бизнес-контекст:** Ядро Securities Массовое выполнение действий над операциями перенумерации сделок

**Поля (35):**

- `AddCur`
- `AvoirKind`
- `ClientID`
- `CommCode`
- `CommDate`
- `CommStatus`
- `ContractID`
- `ContractKind`
- `CreateReport`
- `Currency`
- `Deal1`
- `DestBuyGoal`
- `Division`
- `DocKind`
- `DocumentID`
- `FIID`
- `Flag1`
- `Flag2`
- `Flag3`
- `Flag4`
- `Flag5`
- `FlagSecur`
- `FlagSecurOwn`
- `IssuerID`
- `MarketSchemeID`
- `MarketSchemeID_2`
- `NewFIID`
- `Oper`
- `OperSubKind`
- `OperationKind`


## Таблица: `sbdepdoc`

**Бизнес-контекст:** RS-Retail ФНС: Выполнение операции

**Поля (29):**

- `Account`
- `Action`
- `ApplicationKey`
- `ArDate`
- `CodClient`
- `Code_Currency`
- `Date_Document`
- `FNCash`
- `FNcash`
- `FlagRezid`
- `FlagStorn`
- `Ground`
- `InSum`
- `IsCur`
- `IsSuspended`
- `KNFCode`
- `KindOp`
- `NotConfirm`
- `NumDayDoc`
- `NumSession`
- `Oper`
- `OutSum`
- `PercOprSum`
- `Referenc`
- `Rest`
- `TypeComplexOper`
- `TypeOper`
- `VidDoc`
- `iApplicationKind`


## Таблица: `sbdepdoc.dbt`

**Бизнес-контекст:** DEPOSITR Макрос: delaudit.mac

**Поля (26):**

- `AccTrnID`
- `Account`
- `Account_Payer`
- `Account_Receiver`
- `Action`
- `ApplType`
- `ApplicationKey`
- `Author`
- `CodClient`
- `Code_Currency`
- `Date_Document`
- `DepDate_document`
- `FNCash`
- `FlagRezid`
- `FlagStorn`
- `InSum`
- `IsCur`
- `NotConfirm`
- `NumDayDoc`
- `OutSum`
- `Referenc`
- `Rest`
- `TypeComplexOper`
- `TypeOper`
- `Type_Account`
- `iApplicationKind`


## Таблица: `exoperat.dbt`

**Бизнес-контекст:** RS-Retail Проверка в реестре контролируемых лиц

**Поля (26):**

- `Action`
- `ApplicationKey`
- `ApplicationKind`
- `ClientAddress`
- `ClientCode`
- `ClientCountry`
- `ClientDocInfo`
- `ClientDocNumber`
- `ClientDocSeria`
- `ClientDocType`
- `ClntIdentType`
- `CurDate`
- `IncomeAmount`
- `IncomeRefVal`
- `IncomeTypeValue`
- `IsSuspended`
- `Kind_Oper`
- `Kurs`
- `Name`
- `NotConfirmed`
- `OutAmount`
- `OutRefVal`
- `OutTypeValue`
- `Pname`
- `Sname`
- `Time`


## Таблица: `pay_doc.dbt`

**Бизнес-контекст:** RS-Retail Проверка в реестре контролируемых лиц

**Поля (23):**

- `Action`
- `ApplicationKey`
- `ClientAddress`
- `ClientCountry`
- `ClientFirstName`
- `ClientLastName`
- `ClientSecondName`
- `ClntIdentType`
- `CodClient`
- `CodCur`
- `Codcur`
- `Date_Document`
- `Ground`
- `GroupOpert`
- `InSum`
- `Insum`
- `IsSuspended`
- `NotConfirm`
- `PassportIssuer`
- `PassportNumb`
- `PassportSer`
- `PersIDType`
- `iApplicationKind`


## Таблица: `fininstr`

**Бизнес-контекст:** ББ и РКО Печать кассовых документов. Буферы и вспомогательные функции. Программист: Смирнов С.В. SMR PRN Создан: 30.09.02

**Поля (22):**

- `AvoirKind`
- `CCY`
- `Ccy`
- `DrawingDate`
- `FIID`
- `FI_Code`
- `FI_Kind`
- `FaceValue`
- `FaceValueFI`
- `FaceValueFi`
- `GeneralizedFIID`
- `ISO_NUMBER`
- `IsClosed`
- `IsGeneralized`
- `Issued`
- `Issuer`
- `Name`
- `ParentFI`
- `Point`
- `SumPrecision`
- `Version`
- `issuer`


## Таблица: `bilfactura.dbt`

**Бизнес-контекст:** Ядро ГКБО Реализация процедуры импорта СФ

**Поля (22):**

- `Assignment`
- `FIID`
- `FacturaID`
- `PaymantDate`
- `PaymentNumber`
- `Relcnt`
- `assignment`
- `correctionnum`
- `creationdate`
- `facturaid`
- `facturanumber`
- `isnonds`
- `numgoscontr`
- `receiverid`
- `receiverinn`
- `receivername`
- `supplierid`
- `supplierinn`
- `suppliername`
- `totalamount`
- `totalnds`
- `totalwithnds`


## Таблица: `party`

**Бизнес-контекст:** ББ и РКО Печать кассовых документов. Буферы и вспомогательные функции. Программист: Смирнов С.В. SMR PRN Создан: 30.09.02

**Поля (17):**

- `Address`
- `Born`
- `ClientID`
- `DocumentID`
- `DocumentIssueDate`
- `ExternalID`
- `Latname`
- `LegalForm`
- `NRCountry`
- `Name`
- `NotResident`
- `PartyID`
- `ShortName`
- `TaxInstitution`
- `name`
- `partyID`
- `partyid`


## Таблица: `vsbanner`

**Бизнес-контекст:** DLNG Макрос: va4each.mac

**Поля (16):**

- `AccCode`
- `BCFormKind`
- `BCID`
- `BCNumber`
- `BCPresentationDate`
- `BCSeries`
- `BCTermFormula`
- `BackOffice`
- `FIID`
- `HolderName`
- `IssuePlace`
- `Issuer`
- `IssuerName`
- `OnCallRate`
- `OnCallRatePoint`
- `PortfolioID`


## Таблица: `pmpaym`

**Бизнес-контекст:** DLNG Макрос: va4each.mac

**Поля (16):**

- `Amount`
- `BaseAmount`
- `BaseFIID`
- `DocKind`
- `DocumentID`
- `FIID`
- `PayFIID`
- `PayerAccount`
- `PayerDpNode`
- `PaymentID`
- `Purpose`
- `ReceiverAccount`
- `ReceiverCode`
- `ReceiverCodeKind`
- `ReceiverDpNode`
- `ValueDate`


## Таблица: `wlacclnk.dbt`

**Бизнес-контекст:** МБ Расчеты Генерация сообщения по BVS_400 XML

**Поля (16):**

- `Account`
- `AccountID`
- `Chapter`
- `ClientID`
- `Department`
- `Description`
- `FIID`
- `LnkObjectID`
- `LnkObjectType`
- `ObjectID`
- `ObjectType`
- `Owner`
- `ResultCode`
- `State`
- `Type`
- `TypeAcc`


## Таблица: `sfdef.dbt`

**Бизнес-контекст:** VVV VVV

**Поля (15):**

- `CommNumber`
- `DateFee`
- `DatePeriodBegin`
- `DatePeriodEnd`
- `Department`
- `FIID_Sum`
- `FacturaID`
- `FeeType`
- `ID`
- `IsIncluded`
- `SfContrID`
- `Status`
- `Sum`
- `SumNDS`
- `commNumber`


## Таблица: `prccontract`

**Бизнес-контекст:** Главная книга Конвертация старых процентов

**Поля (14):**

- `Account`
- `Client`
- `ContractID`
- `EndDate`
- `FIID`
- `IsReckonAmoung`
- `Number`
- `ResKind`
- `UseOurAccount`
- `UseSPI`
- `account`
- `chapter`
- `fiid`
- `peraccount`


## Таблица: `acctrn`

**Бизнес-контекст:** VVV VVV

**Поля (13):**

- `Account`
- `ApplType`
- `ApplicationKey`
- `CodClient`
- `DepDate_Document`
- `FNCash`
- `InSum`
- `IsCur`
- `Referenc`
- `TypeComplexOper`
- `TypeOper`
- `Type_Account`
- `iApplicationKind`


## Таблица: `dpregstr.dbt`

**Бизнес-контекст:** Депозитарий Выгрузка инструкций по голосованию для web-кабинета НРД

**Поля (13):**

- `ApplicationKey`
- `ApplicationKind`
- `Branch`
- `Code113i`
- `CurDate`
- `Date`
- `Number`
- `Oper`
- `Rate_Ref`
- `SysTime`
- `curDate`
- `t_date`
- `t_rate_ref`


## Таблица: `pmrmprop`

**Бизнес-контекст:** Cb Макрос: boscmsco.mac

**Поля (12):**

- `CodePurpose`
- `Date`
- `Ground`
- `Number`
- `PayDate`
- `PayerChargeOffDate`
- `PaymentID`
- `PaymentKind`
- `Priority`
- `ResField`
- `ShifrOper`
- `UIN`


## Таблица: `dp_dep`

**Бизнес-контекст:** Ядро Securities Стандартные обработчики полей для форм отчетов (использование через DL_CPanel)

**Поля (11):**

- `Account`
- `CodClient`
- `Code_Currency`
- `End_DateDep`
- `IsCur`
- `Open_Close`
- `Open_Date`
- `Prol_DateDep`
- `Referenc`
- `SpecialAccess`
- `Start_DateDep`


## Таблица: `account.dbt`

**Бизнес-контекст:** ББ и РКО Печать кассовых документов. Буферы и вспомогательные функции. Программист: Смирнов С.В. SMR PRN Создан: 30.09.02

**Поля (10):**

- `Account`
- `AccountID`
- `Balance`
- `Branch`
- `Chapter`
- `Code_Currency`
- `Department`
- `Kind_Account`
- `Open_Date`
- `Type_Account`


## Таблица: `dl_nett`

**Бизнес-контекст:** Неттинг макрос шага "Исполнение обязательств по сделке"

**Поля (10):**

- `ClientId`
- `DealNumber`
- `DocKind`
- `FI_Kind`
- `IdentProgram`
- `NettingID`
- `OverTransitAccount`
- `PayFIID`
- `SigningDate`
- `ValueDate`


## Таблица: `sfcontr`

**Бизнес-контекст:** Ценные бумаги Расчёт сумм для операций списания/зачисления денежных средств

**Поля (9):**

- `ContractorID`
- `DateConc`
- `FIID`
- `ID`
- `Number`
- `PartyID`
- `ServKind`
- `number`
- `partyID`


## Таблица: `avoiriss`

**Бизнес-контекст:** DLNG Макрос: NtgReg_Form.mac

**Поля (9):**

- `FIID`
- `IsVoting`
- `LSIN`
- `MetalRate`
- `NKDBase_Kind`
- `SPIsClosed`
- `TaxGroup`
- `Version`
- `metalnom`


## Таблица: `pc_drest`

**Бизнес-контекст:** RETAIL Перевод в другой вид вклада

**Поля (9):**

- `Action`
- `CodCur`
- `Date_Document`
- `FNCash`
- `GroupOpert`
- `InSum`
- `IsCur`
- `IsSuspended`
- `NotConfirm`


## Таблица: `sfdefcom`

**Бизнес-контекст:** DLNG Макрос: tsid140_OutCom.mac

**Поля (9):**

- `CommNumber`
- `CommSum`
- `ConID`
- `DateFee`
- `FIID_commSum`
- `FeeType`
- `ID`
- `NDSSum`
- `Status`


## Таблица: `vsordlnk`

**Бизнес-контекст:** DLNG Макрос: va4each.mac

**Поля (8):**

- `BCCFI`
- `BCCost`
- `DocKind`
- `InterestChargeDate`
- `IsPartycular`
- `LinkKind`
- `TaxBaseAmount`
- `taxbaseamount`


## Таблица: `pmprop`

**Бизнес-контекст:** Депозитарий Прием документарных ц/б на хранение. Снятие документарных ц/б с хранения. Шаг "Отражение операции по счетам"

**Поля (8):**

- `BankCode`
- `CodeKind`
- `CorSchem`
- `Corschem`
- `DebetCredit`
- `Group`
- `IsSender`
- `PaymentID`


## Таблица: `partyown.dbt`

**Бизнес-контекст:** БОЦБ Процедуры для репликации данных в БОЦБ из внешних систем

**Поля (8):**

- `PartyID`
- `PartyKind`
- `branch`
- `numsession`
- `partyid`
- `partykind`
- `subkind`
- `superior`


## Таблица: `depositr.dbt`

**Бизнес-контекст:** DEPOSITR Макрос: calccorr.mac

**Поля (8):**

- `Close_Date`
- `Code_Currency`
- `FNCash`
- `IsCur`
- `Open_Close`
- `Referenc`
- `Type_Account`
- `UseAlternate`


## Таблица: `dl_genagr`

**Бизнес-контекст:** Производные инструменты Классы для работы c категориями учета

**Поля (8):**

- `AccMode`
- `CodeInAccount`
- `Department`
- `DocKind`
- `Duration`
- `GenAgrID`
- `PartyID`
- `Start`


## Таблица: `objlink.dbt`

**Бизнес-контекст:** Cb Макрос: partycbdk.mac

**Поля (8):**

- `attrid`
- `attrtype`
- `groupid`
- `objectid`
- `objecttype`
- `oper`
- `validfromdate`
- `validtodate`


## Таблица: `sp_acts.tmp`

**Бизнес-контекст:** Ценные бумаги ОТЧЕТ: "АКТЫ СВЕРКИ Ц/Б"(БО)

**Поля (7):**

- `Account`
- `ClientID`
- `ContrID`
- `FIID`
- `Rest`
- `RestCB`
- `RestDep`


## Таблица: `settacc`

**Бизнес-контекст:** Ценные бумаги Операция списания и зачисления денежных средств/Шаг проводок

**Поля (7):**

- `Account`
- `BankCorrCode`
- `BankCorrName`
- `BankID`
- `CorrAcc`
- `FIID`
- `PartyID`


## Таблица: `dlrq.dbt`

**Бизнес-контекст:** Ценные бумаги Шаг изменения условий сделки\отказа от сделки ВО

**Поля (7):**

- `DealPart`
- `DocID`
- `DocKind`
- `FIID`
- `ID`
- `State`
- `Type`


## Таблица: `person`

**Бизнес-контекст:** RS-Retail Приходный кассовый ордер

**Поля (6):**

- `Kind_Operation`
- `Name`
- `Oper`
- `SysTypes`
- `cTypePerson`
- `oper`


## Таблица: `sfaccrue.dbt`

**Бизнес-контекст:** VVV VVV

**Поля (6):**

- `Amount`
- `BeginDate`
- `EndDate`
- `ID`
- `SfDefComID`
- `TransactionDate`


## Таблица: `dpmsginf`

**Бизнес-контекст:** Mbr Макрос: raygm035.mac

**Поля (6):**

- `Contractor`
- `ID`
- `IdentProgram`
- `Kind_Operation`
- `Status`
- `ValueDate`


## Таблица: `sb_casdc.dbt`

**Бизнес-контекст:** DEPOSITR Макрос: ingrep2.mac

**Поля (6):**

- `ApplicationKey`
- `ApplicationKind`
- `Branch`
- `CashDateDoc`
- `NumOper`
- `RefValue`


## Таблица: `sb_dtyp.dbt`

**Бизнес-контекст:** DEPOSITR Макрос: passive2.mac

**Поля (6):**

- `BalAcc`
- `FlagCur`
- `Kind`
- `KindTerm`
- `Term`
- `UserTypeAccount`


## Таблица: `persn`

**Бизнес-контекст:** ББ и РКО Печать кассовых документов. Буферы и вспомогательные функции. Программист: Смирнов С.В. SMR PRN Создан: 30.09.02

**Поля (5):**

- `Born`
- `Name1`
- `Name2`
- `Name3`
- `PersonID`


## Таблица: `account`

**Бизнес-контекст:** ББ и РКО Печать кассовых документов. Буферы и вспомогательные функции. Программист: Смирнов С.В. SMR PRN Создан: 30.09.02

**Поля (5):**

- `Account`
- `Chapter`
- `Code_Currency`
- `NameAccount`
- `accountid`


## Таблица: `corschem`

**Бизнес-контекст:** Производные инструменты Функции

**Поля (5):**

- `CorrID`
- `FIID`
- `FI_Kind`
- `IsNostro`
- `Number`


## Таблица: `sfcomiss.dbt`

**Бизнес-контекст:** VVV VVV

**Поля (5):**

- `Code`
- `FeeType`
- `InstantPayment`
- `Number`
- `RateType`


## Таблица: `depoacnt`

**Бизнес-контекст:** Депозитарий Отчет "Проверочная ведомость остатков лицевых счетов ДЕПО"

**Поля (5):**

- `AutoKey`
- `BriefCode`
- `Code`
- `Owner`
- `kind`


## Таблица: `sb_casln`

**Бизнес-контекст:** RS-Retail Печать формы 36

**Поля (5):**

- `ApplicationKey1`
- `ApplicationKey2`
- `ApplicationKind1`
- `ApplicationKind2`
- `RefValue2`


## Таблица: `sfcontr.dbt`

**Бизнес-контекст:** Производные инструменты Функции

**Поля (4):**

- `DATECONC`
- `Department`
- `ID`
- `Number`


## Таблица: `spground`

**Бизнес-контекст:** DLNG Макрос: tsdocumentscn.mac

**Поля (4):**

- `Kind`
- `RegistrDate`
- `SPgroundID`
- `Xld`


## Таблица: `llvalues`

**Бизнес-контекст:** Mbr Макрос: raygm035.mac

**Поля (4):**

- `Code`
- `Element`
- `List`
- `Name`


## Таблица: `adress`

**Бизнес-контекст:** RS-Bank 6.0 Отчет "ИК депозитного/сберегательного сертииката"

**Поля (4):**

- `Adress`
- `ObjectID`
- `ObjectType`
- `Type`


