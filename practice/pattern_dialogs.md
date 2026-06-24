# Практика: Диалоговые окна и интерактивные элементы (RunDialog, TRecHandler, MsgBox)

**Теория:** [BnRSL.md## Процедура: `RunDialog`]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `CalcDepoCommReserveByAcc`

**Источник:** `Mac/DLNG/DEPO/dpressrvopstart.mac`  
**Тип:** `private macro`  
**Размер:** 25 строк

```rsl
PRIVATE MACRO CalcDepoCommReserveByAcc(dl_comm, AccountID:integer)
  var cmd, query, DataSet;
  var prc, sz;
  var SumsArr = TArray();
  var BaseAcc = TRecHandler("account.dbt");
  var ReservAcc = TRecHandler("account.dbt");
  var RSAcc = TRecHandler("account.dbt");
  var RSCatCode = "";
  var delta = 0;
  var err = 0;
  var accTrn;
  var i = 0;
  var Rnew = 0.0, Rold = 0.0;
  var fd;
  var resbase = TRecHandler("dpresbase.dbt");
  var resbaseCache = RsbSQLInsert("dpresbase.dbt");
  var resobjArr = TArray();
  var resobjCache = RsbSQLInsert("dpresobj.dbt");
  var realIDs = TArray();
  var ResBaseID = 0;

  if(GetAccount(AccountID, BaseAcc) != 0)
    msgbox("Ошибка при поиске счета");
    return 1;
  end;
```

---

## Пример 2: `ExecuteStep`

**Источник:** `Mac/Cb/pm061_10.mac`  
**Тип:** `macro`  
**Размер:** 47 строк

```rsl
macro ExecuteStep( Kind_Operation, first, KindDoc, ID_Operation )

  var stat = 0;
  var ActionStep:integer = ACTION_STEP_UNDEF;
  var pmaddpi    = TRecHandler("pmaddpi.dbt");
  var DateNoChange   :date = date(0,0,0);
  var TypeAccount:string = "";
  var TransAccount:string = "";
  var TransChapter;
  var TransFIID;
  var DepID:integer = 0;
  var NameAccount:string = "";
  var rsacc:RsdRecordset;
  var IfNext, pi;
  
  ActionStep = ChooseActionStep();
  
  if( ActionStep == ACTION_STEP_TRANSACCOUNT )

    var AccountID:string = "";
    MakeAccountID( PaymentObj.Chapter, PaymentObj.PayerFIID, PaymentObj.ReceiverAccount, AccountID, SIZEOBJECTLEN );
    var query:string = "SELECT t_AttrID FROM dobjlink_dbt             " +
                       " WHERE t_ObjectType     = :OBJTYPE_ACCOUNT_OBJ  " +
                        "  AND t_GroupID        = :OBJROLE_ACC_TRANSIT  " +
                        "  AND t_AttrType       = :OBJTYPE_ACCOUNT_ATTR " +
                        "  AND t_ObjectID       = :AccountID            " +
                        "  AND t_ValidFromDate <= :VALID_TO_DATE_FROM   " +
                        "  AND t_ValidToDate   >= :VALID_TO_DATE_TO     ";

    var params:TArray = makeArray( SQLParam("OBJTYPE_ACCOUNT_OBJ", OBJTYPE_ACCOUNT    ), 
                                   SQLParam("OBJROLE_ACC_TRANSIT"  , OBJROLE_ACC_TRANSIT),
                                   SQLParam("OBJTYPE_ACCOUNT_ATTR" , OBJTYPE_ACCOUNT    ),
                                   SQLParam("AccountID"            , AccountID          ),
                                   SQLParam("VALID_TO_DATE_FROM"   , VALID_TO_DATE      ),
                                   SQLParam("VALID_TO_DATE_TO"     , VALID_TO_DATE      ) );

    var rs:RsdRecordset = execSQLselect( query, params, true );
  
    if( rs and rs.moveNext() )
      TransAccount = SubStr(rs.Value(0), 10);
      TransChapter = int(SubStr(rs.Value(0),1, 2));
      TransFIID = int(SubStr(rs.Value(0),3, 7));

      if( PaymentObj.FutureReceiverFIID != TransFIID )
        msgbox("Валюта счета получателя отличается от валюты транзитного счета");
        return 1;
      end;
```

---

## Пример 3: `ИзменитьСрокиИсполнения_ДляСделки`

**Источник:** `Mac/DLNG/SECUR/scchdate.mac`  
**Тип:** `private macro`  
**Размер:** 24 строк

```rsl
private macro ИзменитьСрокиИсполнения_ДляСделки( FD:SPFirstDoc, Action:Integer, doc:Variant, ID_Op:Integer, FactDate:Date, PlanDate:Date, ExecDate:Date )
  var DealType, Ground;
  var DebetAcc, CreditAcc, ChdAcc, FIRole, ForvAcc, ForvAccMinus, ForvAccPlus;
  var ExistLink = false, NeedInsertDepoDraft = false, err, stat, RegistrDate;
  var Sum, N = 0, MinDate = date(0,0,0);

  var FD1, FD2, save_BegDateM = null, save_FinDateM = null, save_BegDateP = null, save_FinDateP = null;
  var MnOD = TRecHandler("account");
  var PlOD = TRecHandler("account");
  var MnOD_2 = TRecHandler("account");
  var PlOD_2 = TRecHandler("account");
  var UpdateAcc = true, i = 0;
  var DateKind = 0;
  var ArrFIID, j:integer = 0;
  var ИспДругиеТО = false;
  var GrDate:date = date(31,12,9999);
  var NumInList = "";

  macro ДосрочнаяОплата():integer

     if( FD.GetRQ(DLRQ_TYPE_PAYMENT).rec.PlanDate <= FactDate )
        MsgBox("Запрещено выполнение операции. Плановая дата ТО по оплате должна быть больше даты досрочной оплаты.");
        return 1;
     end;
```

---

## Пример 4: `OpenTransFiles`

**Источник:** `Mac/DEPOSITR/merge_br.mac`  
**Тип:** `macro`  
**Размер:** 78 строк

```rsl
macro OpenTransFiles;

 var Stat = False;

  if    ( not(     Open( T_Dep,        SourceDir + "depositr.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  depositr.sen ");
          Return Stat;
  elif  ( not(  Open( T_DepHistr,  SourceDir + "dephistr.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  dephistr.sen ");
          Return Stat;
  elif  ( not(  Open( T_DepDoc,    SourceDir + "sbdepdoc.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  sbdepdoc.sen ");
          Return Stat;
  elif  ( not(  Open( T_CashLink,  SourceDir + "sb_casln.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  sb_casln.sen ");
          Return Stat;
  elif  ( not(  Open( T_DepRest,   SourceDir + "pc_drest.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  pc_drest.sen ");
          Return Stat;
  elif  ( not(  Open( T_TrWill,    SourceDir + "sbtrast.sen"  ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  sbtrast.sen ");
          Return Stat;
  elif  ( not(  Open( T_DepClient, SourceDir + "depclnt.sen"  ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  depclnt.sen ");
          Return Stat;
  elif  ( not(  Open( T_AuxInfo,   SourceDir + "auxinfo.sen"  ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  auxinfo.sen ");
          Return Stat;
  elif  ( not(  Open( T_ConGet,    SourceDir + "sb_congt.sen" ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  sb_congt.sen ");
          Return Stat;
  elif  ( not(  Open( T_PcEstim,   SourceDir + "pcestim.sen"    ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  pcestim.sen ");
          Return Stat;
  elif  ( not(  Open( T_PcCalc,    SourceDir + "pc__calc.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  pc__calc.sen ");
          Return Stat;
  elif  ( not(  Open( T_PcRDate,   SourceDir + "pc_rdate.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  pc_rdate.sen ");
          Return Stat;
  elif  ( not(  Open( T_Numbers,   SourceDir + "numbers.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  numbers.sen ");
          Return Stat;
  elif  ( not(  Open( T_AccReg,   SourceDir + "accreg.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  accreg.sen ");
          Return Stat;
  elif  ( not(  Open( T_TextInfo, SourceDir + "textinfo.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  textinfo.sen ");
          Return Stat;
  elif  ( not(  Open( T_ScAcc,    SourceDir + "scAcc.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  scAcc.sen ");
          Return Stat;
  elif  ( not(  Open( T_ScLink,   SourceDir + "scLink.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  scLink.sen ");
          Return Stat;
  elif  ( not(  Open( T_ScCard,   SourceDir + "scCard.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  scCard.sen ");
          Return Stat;
  elif  ( not(  Open( T_ScTran,   SourceDir + "scTran.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  scTran.sen ");
          Return Stat;
  elif  ( not(  Open( T_PcTax,    SourceDir + "pc_tax.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  pc_tax.sen ");
          Return Stat;
  elif  ( not(  Open( T_RetOp,    SourceDir + "ret_op.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  ret_op.sen ");
          Return Stat;
  elif  ( not(  Open( T_OpObject, SourceDir + "opobject.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  opobject.sen ");
          Return Stat;
  elif  ( not(  Open( T_Compens,  SourceDir + "compens.sen"   ) ) )
          MsgBox("Ошибка при открытии транспортного  файла  compens.sen ");
          Return Stat;
  else
          Stat = True;
          Message ("  Транспортные   файлы   успешно  открыты ");
          Return Stat;
  end;
```

---

## Пример 5: `SfCarryAccrue`

**Источник:** `Mac/Cb/sf_lib.mac`  
**Тип:** `macro`  
**Размер:** 30 строк

```rsl
macro SfCarryAccrue( SfDefComRec, SfAccrueRec, SfContrRec, SfConComRec, AccDebit: @string, AccCredit: @string) : integer

  /*var SfComPD : SfComPrimDoc;*/
  var SfConComPD : SfConComPrimDoc;

  var debetSI  = TRecHandler("sfsi.dbt");
  var creditSI = TRecHandler("sfsi.dbt");

  var PayerAccount:string, ReceiverAccount:string;
  var NDSPayerAccount : string, NDSReceiverAccount : string;

  var Ground:string, NDSGround:string;

  var stat = 0;

  var SumPayer = $0, NDSSumPayer = $0, EqSumPayer = $0;
    
  var PayerCatCode:string, NDSPayerCatCode:string, NDSReceiverCatCode:string;

  var TrnDate = SfAccrueRec.TransactionDate;

  var IsNVPI:bool;

  debetSI.Clear;
  creditSI.Clear;

  if( SfGetSI_Uni(OBJTYPE_SFDEFCOM, SfDefComRec, debetSI, creditSI) )
     MsgBox("Ошибка при взятии платежных инструкций УПК.");
     return 1;
  end;
```

**Комментарий автора:**
var SfComPD : SfComPrimDoc;*/

---

## Пример 6: `ОбновитьКомиссиюЗаДосрочныйВывод`

**Источник:** `Mac/DLNG/TRUST/tsprolong.mac`  
**Тип:** `private macro`  
**Размер:** 21 строк

```rsl
PRIVATE MACRO ОбновитьКомиссиюЗаДосрочныйВывод(Order:TS_OrderFD, Valid, ADate:date)

  var ret = 0;
  var select, ComNumber = -1;
  private var ConCom = TRecHandler( "sfconcom.dbt" );
  private var Comiss = TRecHandler( "sfcomiss.dbt" );

  /*проверим на коммисии "за досрочный вывод" значение категории "возобновляемая"*/
  ComNumber = ПолучитьНомерКомиссии(Order.SfContr.rec.ID, "TSP", ADate);
  if(ComNumber > 0)
     if( SfGetComiss( SF_FEE_TYPE_PERIOD, ComNumber, Comiss ) == true )
     if( ДУ_ПолучитьЗначениеКатегории(Comiss, 11, OBJTYPE_SFCOMISS) == 1 ) /*11 - "возобновляемая"*/
        /*найдём комиссию "за досрочный вывод" на договоре*/
        Order.SfContr();
              while( SfGetConCom( Order.SfContr.rec.ID, SF_FEE_TYPE_PERIOD, ConCom ) == true )
                if( ConCom.rec.CommNumber == ComNumber )
             /*обновим комиссию*/
             if( TS_ConComUpdateDate( ConCom.rec.ID, Valid.rec.BeginDate, Valid.rec.EndDate, ConCom.rec.DATEBEGIN, ConCom.rec.DATEEND ) != 0 )
                MsgBox( "Ошибка при изменении дат комиссии" );
                ret = 1;
             end;
```

---

## Пример 7: `ExecuteCaseStep`

**Источник:** `Mac/Mbr/w110_305.mac`  
**Тип:** `macro`  
**Размер:** 24 строк

```rsl
macro ExecuteCaseStep( Kind_Operation, Number_Step, first, KindDoc )  

  var SumKvit, Cancel:string, stat:integer = 0, menu_item, KvitType;
  Array MenuStr;
  Cancel = KVIT_NORMAL;
  if ( Cancel==KVIT_NORMAL )
     return string(НомерШагаИзъятиеИзКартотекиКорреспМБР);
  elif  ( Cancel==KVIT_CANCEL )
    MsgBox("Повторная квитовка отказом запрещена");
    return 1;
  else 
    /* При квитовке отзывом предлагаем пользователю поместить платеж*/
    /* в отвергнутые, вернуть из картотеки у корреспондента или оставить в картотеке */
    menu_item = Opr_MakeChoice(Menu1, Menu2, Menu3, FromCardCorr);

    if( menu_item == 0 )
      return string(НомерШагаПоместитьВОтвергнутые);
    elif ( menu_item == 1)
      /*Возврат не может быть осуществлён, если платёж является */
      /*частичной оплатой Картотеки №2*/
      if( PaymentObj.SubPurpose >0 )
        MsgBox("Невозможно сделать возврат частичной оплаты картотеки №2");
        return 1;
      end;
```

---

## Пример 8: `PT_ShowPTEditPanel_example`

**Источник:** `Mac/Cb/PT_ShowPTPanel.mac`  
**Тип:** `private macro`  
**Размер:** 21 строк

```rsl
private macro PT_ShowPTEditPanel_example()
   var isOk = true;
   var PartyID=NULL;

//   PartyID=0;
//   isOk=PT_ShowPTEditPanel(PartyID);

//   PartyID=12;
//   isOk=PT_ShowPTEditPanel(PartyID, true);

// Пример использования PanelMode и PanelModeSaveManual
/*
PartyID=4312;
var partyObj = RsbParty(PartyID);
isOk=PT_ShowPTEditPanel(PartyID, false, "юридического лица", PTLIST_ALLPARTY, 279/*K_ALTI*/, true);

if(partyObj.Update())
  MsgBox("Изменения сохранены");
else
  DisplayError();
end;
```

---

## Пример 9: `GetRatesDFS`

**Источник:** `Mac/DLNG/ws_md_GetRatesDFS.mac`  
**Тип:** `macro`  
**Размер:** 29 строк

```rsl
macro GetRatesDFS()
  var prm = Settings();
  ReplaceMacro( "msgbox", "MTE_WriteLog" );

  var errMsg = "";
  var stat = 0;
  var curPair = TRecHandler("rkrate.dbt");
  var curName;

  var Idx =  GetConnectIdxFromCache();  
  var Htable =  GetTableIdxFromCache();  

  if( (Idx >= MTE_OK) and (Htable >= MTE_OK) )
    var Query = RSDCommand( " SELECT *  FROM DRKCURPAIR_DBT " );
    Query.execute();
    var DataSet = TRsbDataSet(Query);
    while (DataSet.MoveNext())
      curName = "";
      curPair.rec.Id = 0;
      curPair.rec.CurPairId = SQL_ConvTypeInteger( DataSet.Id );
      curName = prm.curPairMap.GetNameInTradeSystem( ( (ПолучитьКодФинИн(DataSet.PFI, null, FICK_ISOSTRING) )+(ПолучитьКодФинИн(DataSet.CFI, null, FICK_ISOSTRING)) ) );
      /*В этом цикле выполняем только рефреш таблицы для каждой валютной пары*/
      stat = Web_MTEGetQuotes(Idx, Htable, prm.GetTableName(),  curName,  errMsg, curPair, DECIMALS);
      if(stat >= 0)
        SaveCurPair(curPair.rec);
/*        PrintDbgInfo(curPair.rec);*/
      else
        msgbox("Ошибка получения параметров валютной пары " + "CurPairName: " + errMsg);
      end;
```

---

## Пример 10: `SfCarryAccrueExtra`

**Источник:** `Mac/Cb/sf_lib.mac`  
**Тип:** `macro`  
**Размер:** 29 строк

```rsl
macro SfCarryAccrueExtra( SfDefComRec, SfAccrueRec, SfContrRec, SfConComRec, AccDebit: @string, AccCredit: @string) : integer
  var SfConComPD : SfConComPrimDoc;

  var debetSI  = TRecHandler("sfsi.dbt");
  var creditSI = TRecHandler("sfsi.dbt");

  var PayerAccount = "", ReceiverAccount = "";
  var NDSPayerAccount : string, NDSReceiverAccount : string;
  var Ground:string, NDSGround:string;

  var stat = 0;

  var SumPayer = $0, NDSSumPayer = $0, EqSumPayer = $0;
    
  var PayerCatCode:string, ReceiverCatCode:string, NDSPayerCatCode:string, NDSReceiverCatCode:string;
  var PayerFIID, ReceiverFIID;
  var NDSPayerKindSfSi, NDSReceiverKindSfSi;

  var IsNVPI:bool;

  var TrnDate = SfAccrueRec.TransactionDate;

  debetSI.Clear;
  creditSI.Clear;   
  
  if( SfGetSI_Uni(OBJTYPE_SFDEFCOM, SfDefComRec, debetSI, creditSI) )  
    MsgBox("Ошибка при взятии платежных инструкций");
    return 1;
  end; 
```

---

## Пример 11: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/scchdealown.mac`  
**Тип:** `private macro`  
**Размер:** 23 строк

```rsl
private macro ExecuteStep( Doc, FDoc, DocKind, ID_Op, ID_Step )

   record deal(dl_tick);
   var newtick = TRecHandler("dl_tick.dbt");
   var newleg  = TRecHandler("dl_leg.dbt");
   var addNum = 0;
   var FD, dat;
   var change_date = SpChangeDlTick.ChangeDate;      
   var reject_date = SpChangeDlLeg.RejectDate;      
   var reject_date2= SpChangeDlLegBack.RejectDate;      
   var i = 0, j = 0;
   var GUID = "";
   var query, cmd, DataSet;

   var ОбработатьТО = true;

   SetBuff( deal, FDoc );

   /* Если отказ от исполнения/изменение параметров сделки запущен из списка шагов - выводить ошибку */
   if( NOT( SC_IsFromScrollMode() ) )
      msgbox("Шаг \"Изменения условий\" \\ \"Отказ от исполнения сделки\" из списка шагов выполнять запрещено.");
      return 1;
   end; 
```

---

## Пример 12: `ВыполнитьПереводВ_ПКУ`

**Источник:** `Mac/DLNG/SECUR/mvcb30.mac`  
**Тип:** `private macro`  
**Размер:** 21 строк

```rsl
PRIVATE MACRO ВыполнитьПереводВ_ПКУ(FD, d, comm, opid)
  var accOld = TRecHandler("account.dbt");
  var accNew = TRecHandler("account.dbt");
  var CarrySum = $0;
  var CatCode = "";
  var query, cmd, DataSet;
  var AcCurSec = УЧЕТ_ВАЛЮТНЫХ_ДОЛЕВЫХ_ЦБ();
  var SumEquivalentCarry = null;
  var FD_Deal = NULL;
  var err = 0;
  var OptValue = 0;
  var Rest = $0, FiRole = 0;
                                                        
  GetRegistryValue( "SECUR\\РЕКЛАСС.В ПКУ. КОРРЕКТ.СТ-ТИ", V_INTEGER, OptValue, err );
  if( err != 0 )
     msgbox("Ошибка при получении значения настройки SECUR\\РЕКЛАСС.В ПКУ. КОРРЕКТ.СТ-ТИ");
     return 1;
  elif((OptValue != 1) and (OptValue != 2))
     msgbox("Неверное значения настройки SECUR\\РЕКЛАСС.В ПКУ. КОРРЕКТ.СТ-ТИ");
     return 1;
  end;
```

---

## Пример 13: `CheckCompensationType`

**Источник:** `Mac/DEPOSITR/clccmp04.mac`  
**Тип:** `macro`  
**Размер:** 26 строк

```rsl
MACRO CheckCompensationType (compens)

  var DestCodeClient = compens.rec.DestClientCode,
      CodeClient = compens.rec.CodClient,
      CompensType = compens.rec.Kind,
      ClientType = compens.rec.Appltype,
      panel_compenscoef = 0;
      
  var dDay, dMon, dYear; /* День, месяц, год смерти клиента */
  var bDay, bMon, bYear; /* День, месяц, год рождения клиента */
  var cDay, cMon, cYear; /* День, месяц, год закрыие счета */
  var cmd_1, rs_1, cmd_2, rs_2, temp_date;

      Check_compens_pay(compens);
      flag_NOrest = check_and_mount_Rest(compens);
      Client = ClientList.CurRec;      

// ****************************************
// * Инициализация предварительных данных *
// ****************************************
     if (  ( ClientType == AT81 )  OR  
           ( ClientType == AT83 )  )
           if ( NOT CommonBase )
               msgbox("Сумма на оплату ритуальных услуг определяется только по общей базе");
               return 1;
           end;
```

---

## Пример 14: `UpdateBonus`

**Источник:** `Mac/DLNG/DV/dvnop330.mac`  
**Тип:** `private macro`  
**Размер:** 23 строк

```rsl
private macro UpdateBonus(FD:DVFirstDocNDeal, DocKind, ДатаИсполненияШага ):INTEGER
  VAR OurAcc  = TRecHandler("account"),
      AccNalog = TRecHandler("account"),
      Payment:RsbPayment, PaymentNalog:RsbPayment,
      SubPurpose:integer = 0, TmpPaymentID:integer = -1;
  var Pm = Trechandler( "pmpaym.dbt" );
  var SumPaym:money = FD.Deal.rec.Bonus;
  var PayNalog = FD.IsPayNalog();
  var SumNalogRUR:money = $0.0;
  var SumNalog:money = $0.0;
  var SumTax:money = $0;
  var createPaym:bool = false;
  var createPaymTax:bool = false;
  var pm2 = TRecHandler ("pmpaym");

  var bonusDate = FD.Deal.rec.BonusDate;

   if( PayNalog )
      SumNalogRUR = FD.SumNalog(ДатаИсполненияШага);
      if( not DV_SmartConvertSumDbl(SumNalog, SumNalogRUR, ДатаИсполненияШага, NATCUR, FD.Deal.rec.BonusFIID) )
         MsgBox( "Ошибка при конвертации суммы из " + string(ПолучитьКодФинИн(NATCUR)) + " в " + string(ПолучитьКодФинИн(FD.Deal.rec.BonusFIID)) );
         return 1;
      end;
```

---

## Пример 15: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsv020rp.mac`  
**Тип:** `macro`  
**Размер:** 23 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

/* Пример использования внешнего массива с назначением платежей.
   Смотри ф. RPS() в файле vsprint.mac
  var PurposeExt=TArray;
      PurposeExt[0] = PM_PURP_VEKSELDRAW;
      PurposeExt[1] = PM_PURP_PAY_DEBT;
      PurposeExt[2] = PM_PURP_TAXINCOME_NJ;
*/
    /* распоряжение на открытие счетов */
    /* распоряжение на выполнение проводок */
    /* МО по выдаче */
    /* распоряжение на банковский валютный платеж */
    /* распоряжение на клиентский валютный платеж */
    /* распоряжение на перечисление средств */
    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПОБКS"))
      msgbox("Нет документов для печати");
      exit(1);
    end;
```

---

## Пример 16: `SEIEM_QRadarSend`

**Источник:** `Mac/Cb/siem_send.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro SEIEM_QRadarSend(pProtocol, pAdress, pPort, pCert, pMessage, oErrMsg)
    var stat = true;
    var ConnectParams;

    stat = RsSyslogConnect(pProtocol, pAdress, pPort, pCert, ConnectParams, oErrMsg);
    if (stat)
        stat = RsSyslogWrite(ConnectParams, pMessage);
        RsSyslogClose(ConnectParams);
    end;
    
    if (not stat)
        msgbox("SEIEM_ConnectParams.LastError: ", ConnectParams.LastError);
        msgbox("SEIEM_ConnectParams.LastDetailedError: ", ConnectParams.LastDetailedError);
    end;
    
    return stat;
end;
```

---

## Пример 17: `ExecuteStep`

**Источник:** `Mac/DLNG/VEKSEL/vstrsrok.mac`
**Тип:** `macro`
**Размер:** 110 строк

```rsl
MACRO ExecuteStep(Buffer, FirstDoc, DocKind, ID_Operation, ID_Step)
var
    fd, СчетДебет = "", СчетКредит = "", СуммаПр = 0, BankName = "", ok, КатегорияУчета = "";

    var СуммаНачисленныхПроцентов = 0.0, СуммаНачисленногоДисконта = 0.0;
    var Валюта_Проводки = -1, ВалютаУчета;
    var PrDsParm, IncGroup;

    SetBuff( bnr, FirstDoc );
    
    if( srvdoc.rec.ExecutionDate > {curdate} )
       MsgBox ("Преждевременное выполнение шага запрещено.");
       return 1;
    end;

    if(bnr.BCTermFormula != VS_TERMF_ATSIGHT)
        /* формулировка срока не "по предъявлении" */;
        return 0;
    elif(Index(bnr.BCState, "С") != 0)
        msgbox ("Вексель уже перенесли по сроку");
        return 1;
    elif(Index(bnr.BCState, "И") != 0)
        msgbox ("Вексель уже перенесли к исполнению");
        return 1;
    elif(not НайтиЦеновыеУсловия(leg, bnr.BCID))
        msgbox ("Не найдены ценовые условия векселя ", bnr.BCID,
                "|серия ", bnr.BCSeries, " номер ", trim(bnr.BCNumber)
        );
        return 1;
    end;
    
    fd = VSBannerFD (bnr, leg);
    ВалютаУчета = fd.ОпределитьВалютуУчета();


    if(not DL_IsOurBanner(bnr.Issuer))
      IncGroup = VACollectIncome(srvdoc.rec.ExecutionDate);
      PrDsParm = VAPrDsParm(@IncGroup, ID_Operation, ID_Step);
      
      if(ВалютаУчета != leg.rec.PFI) //ВУ != ВН
        if(ExecMacroFile("vaovernvpi.mac", "ПереоценкаНВПИВекселя", bnr.BCID, srvdoc.rec.ExecutionDate, IncGroup))
          return 1;
        end;
      end;

      if(ExecMacroFile("vaprdslib.mac", "ВыполнитьДоначислениеОднойЦБ", fd.GetBnr(), fd.GetLeg(), null, null, null, PrDsParm))
        return 1;
      end;
    end;

    if(DL_IsOurBanner(bnr.Issuer))
        КатегорияУчета = "Наш вексель";//Балансовая стоимость векселя
        СчетДебет = OpenBnrAccount(КатегорияУчета, fd, false);
        СчетКредит = OpenBnrAccount(КатегорияУчета, fd, true);
        Валюта_Проводки = fd.ОпределитьВалютуУчета();
        if(not ПолучитьОстаток(СуммаПр, СчетДебет, Валюта_Проводки, srvdoc.rec.ExecutionDate))
          return 1;
        end;
        BankName = НашБанк();
    else
        КатегорияУчета = "Учтенные векселя";
        СчетКредит = OpenBnrAccount(КатегорияУчета, fd, false);
        СчетДебет = OpenBnrAccount(КатегорияУчета, fd, true);
        if(not GetLastSum(bnr.BCID, srvdoc.rec.ExecutionDate, @СуммаПр, ВалютаУчета))
           return 1;
        end;
        BankName = GetBankName(bnr.Issuer);
        Валюта_Проводки = ВалютаУчета;
    end;
    
    if((СчетКредит == "") or (СчетДебет == ""))
        msgbox ("Ошибка при определении счета");
        return 1;
    elif(СчетДебет == СчетКредит)
        msgbox ("Вексель ", bnr.BCID,
                "|серия ", bnr.BCSeries, " номер ", trim(bnr.BCNumber),
                "|не надо переносить по сроку");
        return 1;
    elif(Проводка(СчетДебет, СчетКредит, СуммаПр,
                  String("Перенос балансовой стоимости векселя ", BankName,
                         " серия " , bnr.BCSeries, " № ", trim(bnr.BCNumber),
                         " на счет \"до востребования\""),
                  null, null,
                  Валюта_Проводки, null, null,                
                  srvdoc.rec.ExecutionDate))
        return 1;
    elif (MakeDiscCarry(fd))
        return 1;
    else
        if(DL_IsOurBanner(bnr.Issuer))
           ok = ИзменитьВексель(bnr.BCID,srvdoc.rec.ValueDate, "addbcstate", "С");
        else
           ok = ИзменитьУчтенныйВексель(bnr.BCID, srvdoc.rec.ValueDate, "addbcstate", "С");
        end;
        if(not ok)
           msgbox("Ошибка при установке для векселя ", bnr.BCID,
                  "|серия ", bnr.BCSeries, " номер ", trim(bnr.BCNumber),
                  "|признака переноса по срочности");
           return 1;
        end;
    end;

    if( not(DL_IsOurBanner(bnr.Issuer)) )
      if(ExecMacroFile("vaprdslib.mac", "ПереносНачисленныхПроцентовИДисконтаПоВекселю", bnr, leg.rec, srvdoc.rec.ExecutionDate, srvdoc.rec.ValueDate, IncGroup))
        return 1;
      end;
    end;

    return 0;
END;
```

---

## Пример 18: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsoverv.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  // Номер экземпляра операции 
                ID_Step,       // Номер шага операции 
                Kind_Operation,// Вид операции 
                KindStep)      // Вид шага операции 

    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СП")) // Счета, Проводки 
      msgbox("Нет документов для печати");
      exit(1);
    end;

    return 1;
END;
```

---

## Пример 19: `pcmt_Done`

**Источник:** `Mac/DLNG/MMARK/mmactx.mac`
**Тип:** `macro`
**Размер:** 39 строк

```rsl
MACRO pcmt_Done( p_filename )

var MM_WordApp, RTF_PATH, dot_filename,
    txtRegistryPath = "BANK_INI\\ОБЩИЕ ПАРАМЕТРЫ\\ДИРЕКТОРИИ\\TEXTDIR";

    if( p_filename == "" ) /* pcmt_Do отработал с ошибкой */
       /*  msgbox вряд ли нужен, сообщения выдает pcmt_Do */
       return FALSE;
    end;
   
    /* пакетный выпуск */
    if( isOprMultiExec() and (МассоваяПечатьПодтверждений == true) )
       MMCMT_WordFiles[ ASize(MMCMT_WordFiles) ] = p_filename;
   /*    MMCMT_WordFilesPtr = MMCMT_WordFilesPtr + 1;*/
       return TRUE;
    end;
   
    MM_WordApp = ActiveX( "Word.Application", null, TRUE );
   
    if (IsStandAlone) /*Двухзвенка*/    
       MM_WordApp.Visible = TRUE;
       MM_WordApp.Documents.Add( p_filename, FALSE );
    else /*Трехзвенка*/
       MM_WordApp.Quit;
       if (not CopyFile (p_filename,"$txtfile\\tmprep.rtf"))
           MsgBox ("Ошибка при передаче файла на терминал");
           return FALSE;
       else
           if(MM_SetRegistryPath(txtRegistryPath, RTF_PATH) == 0)
              // получит полный путь
              RTF_PATH = MMCMT_processPath(RTF_PATH);
              dot_filename = RTF_PATH + "\\tmprep.rtf";
              CallRemoteRsl ("mmshrp.mac" ,"ShowReport", dot_filename);
           end;
       end;
    end;
   
    return TRUE;
END;
```

---

## Пример 20: `ExecuteStep`

**Источник:** `Mac/LC/lc004_10.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
MACRO ExecuteStep()
  var stat : integer = 0;
  var ShowRlsPanel : bool = true;
  Array Text, Buttons;

  if(LCDocObj.IsEmptyLcreimb())
    msgbox("Не задан способ рамбурсирования");
    return 1;
  end;
```

---

## Пример 21: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsr020pm.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПО")) /* Счета, Проводки, мем.Ордера */
      msgbox("Нет документов для печати");
      exit(1);
    end;

    return 1;
END;
```

---

## Пример 22: `FrzChOutStart`

**Источник:** `Mac/Cb/fm_frzchkout.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro FrzChOutStart()
  /* определим код территориального учреждения по ОКАТО */
/*
  KTU = FM_GetKTU();
  if( Trim(KTU) == "" )
    msgbox( "Не определен код территории учреждения по ОКАТО" );
    return 1;
  end;
```

---

## Пример 23: `TreatBranch`

**Источник:** `Mac/DEPOSITR/upldstat.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro TreatBranch;

  if(OpenTrFiles(ddep.rec.Code))
    IsFirstForBranch = true;
    TreatStaticAccsForBranch(0, SA_STATIC);
    TreatStaticAccsForBranch(0, SA_UNITED);
    TreatStaticAccsForBranch(1, SA_STATIC);
    TreatStaticAccsForBranch(1, SA_UNITED);
    if(not ErrFlag)
      DeleteFiles;
    else
      MsgBox("Ошибки при загрузке неподвижных/объединенных счетов|для филиала №",
       ddep.rec.Name, " |Повторите процедуру еще раз");
    end;
  end;
```

---

## Пример 24: `ФункцияПользователя_ЗаявлениеПогашения`

**Источник:** `Mac/DLNG/VEKSEL/vsscp.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
MACRO ФункцияПользователя_ЗаявлениеПогашения(Режим)
    msgbox(String("Выполняется макрофункция с именем|",
                  "ФункцияПользователя,|",
                  "которая определена в файле|",
                  "vsscp.mac|",
                  "Заявление на погашение"));
    return 0;
END;
```

---

## Пример 25: `Crit_Main`

**Источник:** `Mac/DEPOSITR/critacpt.mac`
**Тип:** `macro`
**Размер:** 76 строк

```rsl
macro Crit_Main( _Type, _Prm, _rez, _trast, _income, _age, _sum, _Desc, _Spec, _AddrDoc, _AddrTrast )
    var accept = TRUE;
    var fMake  = FALSE;

    Message( " Ожидание разрешения на выполнение рискованного действия. ~Ctrl-Break~ - прервать" );

    if (StrFor(GetProgramID) == "П")
        return TRUE;
    end;

    /* Чтение записи о Филиале */
    fil.rec.FNCash = FNCash;
    if ( fil.GetEQ()  AND  fil.rec.FlagCritAdd )
        fAdd = TRUE;
    end;

    SetBuff( ro, _Prm );

    sDesc = _Desc;

    ClearRecord( depDoc );
    if ( _AddrDoc != NULL )
        SetBuff( depDoc, _AddrDoc );
    end;

    // Проверки для видов вызова макроса.
    if   ( _Type == CM_DEP )     // Вкладные операции, кроме закрытия и наследства.
        fMake = check_Dep( ro.IsCur, ro.Operation, _rez, _trast, _income, _sum );
    elif ( _Type == CM_CLOSE )   // Операции закрытия счета.
        fMake = check_Close( _trast, _rez, _sum, depDoc );
    elif ( _Type == CM_WILL )    // Выплаты наследникам ( операция 99 ).
        fMake = check_Will();
    elif ( _Type == CM_NOTFIN )  // Нефинансовые операции.
        if ( _AddrTrast != NULL )
            SetBuff( trast, _AddrTrast );
        end;
        fMake = check_NotFin( ro.Operation );
    elif ( _Type == CM_STORN_OP )  // Сторнирование операции.
        if ( check_Storn( _Desc, _Spec, ro.ApplicationKey, ro.ApplicationKind, _Type, depDoc ) )
            return TRUE;
        else
            msgBox( "Действие отклонено." );
            return FALSE;
        end;
    elif ( _Type == CM_DELETE_OP )  // Удаление операции.
        if ( check_Del( _Desc, _Spec, ro.ApplicationKey, ro.ApplicationKind, _Type, depDoc ) )
            return TRUE;
        else
            msgBox( "Действие отклонено." );
            return FALSE;
        end;
    end;

    // Несовершеннолетний клиент.
    if ( _age < 18 )
        fMake = TRUE;
    end;

    // Вызов процедуры контроля критических (рискованных) действий.
    if ( fMake )
        if (_Type == CM_DEP)
            accept = CritWaitAcceptEx( CM_DEP, sDesc, StrFor(0), depDoc.iApplicationKind, depDoc.ApplicationKey, null, null, null, depDoc );
        elif ((_Type == CM_CLOSE) or (_Type == CM_WILL))
            accept = CritWaitAcceptEx( CM_CLOSE, sDesc, depDoc, depDoc.iApplicationKind, depDoc.ApplicationKey, null, null, null, depDoc );
        else
            accept = CritWaitAcceptEx( 0, sDesc, StrFor(0));
        end;
    end;

    if ( NOT accept )
        msgBox( "Действие отклонено." );
    end;

    return accept;

end;
```

---

## Пример 26: `DL_FldProc_AvrKindFltr`

**Источник:** `Mac/DLNG/SECUR/ReservReg_Form.mac`
**Тип:** `macro`
**Размер:** 44 строк

```rsl
MACRO DL_FldProc_AvrKindFltr( pThis:DL_CPanel, Cmd:INTEGER, Key:INTEGER, FldShowValue:@VARIANT, FldRealValue:@VARIANT ):INTEGER
  VAR Fininstr, AvrID, IsEmiss, IsNotEmiss, RepSubKind;
  VAR WhereCond = " (( RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_SHARE+", t_AvoirKind) > 0 " +
                  "      OR RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_DEPOSITORY_RECEIPT+", t_AvoirKind) > 0 )" +
                  "      OR RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_BOND+", t_AvoirKind) > 0 )";
  RepSubKind = pThis.GetLinkedValue(H_PNFLD_SUBKIND);                  
  //pThis.GetFieldValue(PNFLD_RESERVREG_SUBKIND, @svSubkind, @rvSubkind); 

  if( Cmd == DLG_INIT )
     if( FldRealValue == null )
        FldRealValue = -1;
     end;
     if( FldRealValue <= 0 )
        FldShowValue = STR_ALLVALUE;
     else
        DL_GetAvrKindName( FIKIND_AVOIRISS, FldRealValue, null, @FldShowValue );
     end;
  elif( Cmd == DLG_CHANGEVALUE ) /*значение поля было изменено*/

     if( pThis.ExistField(DL_PNFLD_AVRCODE) )
        if( (FldRealValue == null) OR (FldRealValue < 0 ) )
           pThis.SetLinkedValue( DL_PNFLD_AVRCODE, -1 ); /*скинуть поле*/
        else
           AvrID = pThis.GetLinkedValue(DL_PNFLD_AVRCODE);
           if( (AvrID != null) AND (AvrID > 0) )
              Fininstr = TRecHandler( "fininstr.dbt" );
              if( ПолучитьФинИн( AvrID, Fininstr) OR (FldRealValue != Fininstr.rec.AvoirKind) )
                 pThis.SetLinkedValue( DL_PNFLD_AVRCODE, -1 ); /*скинуть поле*/
              end;
           end;
        end;
     end;
  elif( (Cmd == DLG_KEY) AND (Key == KEY_SPACE) ) 
     FldRealValue = -1;
     FldShowValue = STR_ALLVALUE;
  elif( (Cmd == DLG_KEY) AND (Key == KEY_F3)) /*Вызов листалки и заполнение FldShowValue и FldRealValue*/
     if(RepSubKind == RESERVREG_0801)
        WhereCond = " ( RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_SHARE+", t_AvoirKind) > 0 "
                          + "      OR RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_DEPOSITORY_RECEIPT+", t_AvoirKind) > 0 )";
     elif(RepSubKind == RESERVREG_0802)
        WhereCond = "  RSB_FIInstr.FI_AvrKindsEQ("+FIKIND_AVOIRISS+", "+AVOIRISSKIND_BOND+", t_AvoirKind) > 0 ";
     end;
     DL_ListAvrKinds( FIKIND_AVOIRISS, @FldShowValue, @FldRealValue, pThis.CurrentFldX(), pThis.CurrentFldY(), WhereCond );
  end;
```

---

## Пример 27: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsv024rp.mac`
**Тип:** `macro`
**Размер:** 26 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

/* Пример использования внешнего массива с назначением платежей.
   Смотри ф. RPS() в файле vsprint.mac
  var PurposeExt=TArray;
      PurposeExt[0] = PM_PURP_VEKSELDRAW;
      PurposeExt[1] = PM_PURP_PAY_DEBT;
      PurposeExt[2] = PM_PURP_TAXINCOME_NJ;
*/
    /* распоряжение на открытие счетов */
    /* распоряжение на выполнение проводок */
    /* МО по выдаче */
    /* распоряжение на банковский валютный платеж */
    /* распоряжение на клиентский валютный платеж */
    /* распоряжение на перечисление средств */
    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПОБКS"))
      msgbox("Нет документов для печати");
      exit(1);
    end;

    return 1;
END;
```

---

## Пример 28: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsv010in.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
MACRO PrintStepDocs(
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

   if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПО")) /* Счета, Проводки, мем.Ордера */
      msgbox("Нет документов для печати");
      exit(1);
   end;

   return 1;
END;
```

---

## Пример 29: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsi075.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СП")) /* Счета, Проводки */
      msgbox("Нет документов для печати");
      exit(1);
    end;

    return 1;
END;
```

---

## Пример 30: `OpScUserEventPan`

**Источник:** `Mac/Cb/opscuser.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro OpScUserEventPan(dlg, cmd, id, key)
    if(cmd == DLG_INIT)
        NewOper = false;
        
        StdInit(dlg, cmd, id, key);
        UpdateFields(dlg);
        DisableFields(dlg);
    end;
end;
```

---

## Пример 31: `printReportRSF`

**Источник:** `Mac/DLNG/MMARK/mmrprorl2.mac`
**Тип:** `macro`
**Размер:** 25 строк

```rsl
MACRO printReportRSF(p_VD,  /* параметры для печати (всегда определены) */
                   p_DDirection,  p_fiid, p_ExcludeFI, p_MDirection, /* параметры для расчета, м.б. неопред. */
                   p_PartyCtgID,  p_PartyCtgAttrID,
                   p_PortfKindID, p_PortfKindAttrID )
var grp = TReportsGroup();

   /* Считать переданные параметры в глобальные переменные.
      Если какие-либо параметры не были заданы, они должны быть == 0 */
   rp_VD              = p_VD;
   rp_DDirection      = p_DDirection;
   rp_FI              = p_fiid;
   rp_ExcludeFI       = p_ExcludeFI;
   rp_MDirection      = p_MDirection;
   rp_PartyCtgID      = p_PartyCtgID;
   rp_PartyCtgAttrID  = p_PartyCtgAttrID;
   rp_PortfKindID     = p_PortfKindID;
   rp_PortfKindAttrID = p_PortfKindAttrID;

   if(PrintBody(grp, p_VD, p_fiid) == true)
      grp.Print( TRUE );
   else
      msgbox( "Нет данных, удовлетворяющих заданной фильтрации." );
   end;

END;
```

---

## Пример 32: `Authorization`

**Источник:** `Mac/DLNG/ws_md_GetRates.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
  MACRO Authorization()
    var stat = SUCCES;
    _tokenKey = GetTokenKeyFromCache();

    if(_tokenKey == "")
      var resp = GetTokenRequest();
      if (resp != "")
        stat = GetTokenKey(resp);
      else
        msgbox("Ошибка авторизации на веб-сервисе.");
        stat = AUTHOR_FAULT;
      end;

    end;
    return stat;
  END;
```

---

## Пример 33: `Блок`

**Источник:** `Mac/DLNG/VA/vacalcreg_form.mac`
**Тип:** `block`
**Размер:** 21 строк

```rsl
PRIVATE MACRO FldProc_RadioReserveNo( pThis:DL_CPanel, Cmd:INTEGER, Key:INTEGER, FldShowValue:@VARIANT, FldRealValue:@VARIANT ):INTEGER
  if( Cmd == DLG_INIT )
     if( FldRealValue == null ) /*инициализация по умолчанию*/
        FldRealValue = UNSET_CHAR;
     end;
     FldShowValue = FldRealValue;
  elif( Cmd == DLG_CHANGEVALUE )
     FldRealValue = FldShowValue;
     if (FldShowValue == SET_CHAR)
       pThis.SetLinkedValue( H_RADIO_RESERVE_YES   , UNSET_CHAR);
       pThis.SetLinkedValue( H_RADIO_RESERVE_ONLYRES, UNSET_CHAR);
     end;
  elif( Cmd == DLG_KEY )
     if( Key == KEY_SPACE )
        if( FldRealValue != SET_CHAR )
           FldShowValue = FldRealValue = SET_CHAR;
        end;
     end;
  end;
  return CM_DEFAULT;
END;
```

---

## Пример 34: `ПроводкаПодОтчет`

**Источник:** `Mac/DLNG/VEKSEL/vsfmotls.mac`
**Тип:** `macro`
**Размер:** 67 строк

```rsl
MACRO ПроводкаПодОтчет(fmo, StepDate, ТребуетсяСписание)
VAR
    Дебет, Кредит,
    Сумма = 0,
    Purpose,
    PurposeOut,
    EnumStr,
    FmordFd,
    ResponsName = "",
    i = 0,
    stat = 0;

    EnumStr = VS_GetBlanksEnumStr(fmo.FrmOrdId, Сумма);

    if(fmo.ResponsPerson > 0)
      ResponsName = PartyName(fmo.ResponsPerson);
    end;

    Purpose = String("Под отчет ", ResponsName,
                     " бланки векселей ", НашБанк(), " ",
                     EnumStr,
                     " (в кол-ве ", Сумма, " шт.)"
                     );

    PurposeOut = String("Списать с подотчетного лица",
                     " бланки векселей ",
                     EnumStr,
                     " (в кол-ве ", Сумма, " шт.)"
                     );

    // Групперовка по счетам учета
    if ( not VS_ForEachForm(fmo,@ГрупировкаПоСчетам,fmo) )
      stat = 1;
      return (stat == 0);
    end;

    if((FmordFd = VSFrmOrdFd(fmo)) == null)
      stat = 1;
    end;

    while ((i < FromGrops.ArrGrp.size) AND (stat == 0) )
      if(not ПолучитьСчетВекселя("Выданные под отчет ц/б", FmordFd, Дебет, MC_OPENACC_CREATE, null, null, StepDate))
         stat = 1;
      elif(not ПолучитьСчетВекселя("БланкиДляРаспр.,Сц/б", FromGrops.ArrGrp[i].FormFd, Кредит, MC_OPENACC_CREATE, null, null, StepDate))
         stat = 1;
      elif (Проводка(Дебет, Кредит, FromGrops.ArrGrp[i].Count, Purpose, 0, 0, NATCUR, 3, null, StepDate) != 0)
          msgbox ("Ошибка при выполнении проводки",
                  "|по передаче бланков под отчет");
          stat = 1;
      end;

      if (ТребуетсяСписание and (stat == 0))
        Кредит = Дебет; // Кредитом является ранее полученный счет КУ "Выданные под отчет ц/б"
        if(not ПолучитьСчетВекселя("ВнебалСчетКорресп", FmordFd, Дебет, MC_OPENACC_CREATE, NATCUR, null, StepDate, FIROLE_CORACC_ACTIVE))
          stat = 1;
        elif (Проводка(Дебет, Кредит, FromGrops.ArrGrp[i].Count, PurposeOut, 0, 0, NATCUR, 3, null, StepDate) != 0)
            msgbox ("Ошибка при выполнении проводки",
                    "|по списанию бланков векселей");
            stat = 1;
        end;
      end;

      i = i + 1;
    end;

    return (stat == 0);
END;
```

---

## Пример 35: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vsr034rp.mac`
**Тип:** `macro`
**Размер:** 26 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

/* Пример использования внешнего массива с назначением платежей.
   Смотри ф. RPS() в файле vsprint.mac
  var PurposeExt=TArray;
      PurposeExt[0] = PM_PURP_VEKSELDRAW;
      PurposeExt[1] = PM_PURP_PAY_DEBT;
      PurposeExt[2] = PM_PURP_TAXINCOME_NJ;
*/
    /* распоряжение на открытие счетов */
    /* распоряжение на выполнение проводок */
    /* МО по выдаче */
    /* распоряжение на банковский валютный платеж */
    /* распоряжение на клиентский валютный платеж */
    /* распоряжение на перечисление средств */
    //if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПОБКS"))
    //  msgbox("Нет документов для печати");
    //  exit(1);
    //end;

    return 1;
END;
```

---

## Пример 36: `Блок`

**Источник:** `Mac/DLNG/DV/dvrepinfo_form.mac`
**Тип:** `block`
**Размер:** 12 строк

```rsl
  if( Cmd == DLG_INIT ) /*Установка значения в поле*/
     if( FldRealValue == null ) /*инициализация по умолчанию*/
        FldRealValue = ПЕРИОД;
     end;
     FldShowValue = DL_GetNameAlg( ALG_DV_REP_PERIOD, FldRealValue );
  elif( Cmd == DLG_CHANGEVALUE ) /*значение поля было изменено*/
     if( FldRealValue == ПЕРИОД )/*разрешаем редактировать только для вида периода "период"*/
        EnableFields( pThis.Data(), PNFLD_DVREPINFO_BEG_DATE );
        EnableFields( pThis.Data(), PNFLD_DVREPINFO_END_DATE );
     else
        DisableFields( pThis.Data(), PNFLD_DVREPINFO_BEG_DATE );
        DisableFields( pThis.Data(), PNFLD_DVREPINFO_END_DATE );
```

---

## Пример 37: `PanelHandler`

**Источник:** `Mac/CELLS/contrstat.mac`
**Тип:** `macro`
**Размер:** 35 строк

```rsl
MACRO PanelHandler( dlg, cmd, id, key )
    if( cmd == DLG_KEY )
        if(( key == F3) and (FldName( dlg, id ) == "PeriodName") )
            MenuChoose = Menu(Periods, NULL, NULL,NULL,NULL,0);
            if( MenuChoose >= 0 )
                if (MenuChoose == 0)
                    Panel.AllYearFlag = "X";
                else
                    Panel.AllYearFlag = "";
                end;
            end;
        elif( (key == SPACE) and (FldName( dlg, id ) == "AllYearFlag") )
            if(Panel.AllYearFlag == "")
                Panel.AllYearFlag = "X";
                MenuChoose = 0;
            else
                Panel.AllYearFlag = "";
                MenuChoose = 1;
            end;
        elif (key == ENTER)
            RunReport();
            return CM_CANCEL;
        elif (key == ESC)
            return CM_CANCEL;
        end;
    elif( cmd == DLG_INIT )
        Panel.AllYearFlag = "";
        MenuChoose = 0;
    end;
    
    if( MenuChoose >= 0 )
        Panel.PeriodName = Periods(MenuChoose);
    end;
    UpdateFields( dlg );
END;
```

---

## Пример 38: `PrintStepDocs`

**Источник:** `Mac/DLNG/VEKSEL/vst010tb.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

    if(not Печать(false, "vsrep", ID_Operation, ID_step, isOprMultiExec, "СПО")) /* Счета, Проводки, МемОрдера */
      msgbox("Нет документов для печати");
      exit(1);
    end;

    return 1;
END;
```

---

## Пример 39: `ProcessFile`

**Источник:** `Mac/Cb/del_cntr.mac`
**Тип:** `macro`
**Размер:** 76 строк

```rsl
MACRO ProcessFile(filename)

  var stat = 0;

  if (GetEQ(filename))
    stat = -1;
  end;/*if*/

  return stat;

END;/*MACRO*/

MACRO CheckCountryLinx(CountryCode)

  var result = false;

  FILE addrempl ("addrempl.dbt", "zp.def") KEY 6;
  FILE bus_trip ("bus_trip.dbt", "zp.def") KEY 4;
  FILE hs_lsht  ("hs_lsht.dbt" , "zp.def") KEY 3;
  FILE lsheet   ("lsheet.dbt"  , "zp.def") KEY 8;
  FILE militreg ("militreg.dbt", "zp.def") KEY 3;
  FILE national ("national.dbt", "zp.def") KEY 4;
  FILE patrzsal ("patrzsal.dbt", "zp.def") KEY 1;
  FILE zsale    ("zsale.dbt"   , "zp.def") KEY 5;

  addrempl.CodeCountry = CountryCode;
  if (ProcessFile(addrempl) == -1)
    MsgBox("Страна используется в файле адресов сотрудников.\nТабельный № сотрудника ", addrempl.Tnumb);
    result = true;
  end;/*if*/

  bus_trip.Country = CountryCode;
  if (ProcessFile(bus_trip) == -1)
    MsgBox("Страна используется в файле командировок сотрудников.\nТабельный № сотрудника ", bus_trip.Tnumb);
    result = true;
  end;/*if*/

  hs_lsht.CodeCountryBorn = CountryCode;
  if (ProcessFile(hs_lsht) == -1)
    MsgBox("Страна используется в файле истории личных карточек.\nТабельный № сотрудника ", hs_lsht.Tnumb);
    result = true;
  end;/*if*/

  lsheet.CodeCountryBorn = CountryCode;
  if (ProcessFile(lsheet) == -1)
    MsgBox("Страна используется в файле личных карточек сотрудников.\nТабельный № сотрудника ", lsheet.Tnumb);
    result = true;
  end;/*if*/

  militreg.CodeCountry = CountryCode;
  if (ProcessFile(militreg) == -1)
    MsgBox("Страна используется в файле военнокоматов.\nID записи ", militreg.IdRec);
    result = true;
  end;/*if*/

  national.Country = CountryCode;
  if (ProcessFile(national) == -1)
    MsgBox("Страна используется в файле гражданства сотрудников.\nТабельный № сотрудника ", national.Tnumb);
    result = true;
  end;/*if*/

  patrzsal.Country = CountryCode;
  if (ProcessFile(patrzsal) == -1)
    MsgBox("Страна используется в файле шаблонов начислений.\nВид перечисления ", patrzsal.KindMove);
    result = true;
  end;/*if*/

  zsale.Country = CountryCode;
  if (ProcessFile(zsale) == -1)
    MsgBox("Страна используется в файле начислений/удержаний.\nВид перечисления ", zsale.KindMove);
    result = true;
  end;/*if*/

  return result;

END;/*MACRO*/
```

---

## Пример 40: `PrintDocument`

**Источник:** `Mac/DLNG/TRUST/tsappforpaym.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
MACRO PrintDocument( SpGroundID ):bool
  var errcode, errtext;

  var Doc = AppForPayment( SpGroundID );

  if( FindGrTemp( Doc.GetTemplate() ) )
    message("Печать договора ...");

    PrintContr(1, Doc);
  else
    msgbox("шаблон не найден");
  end;
```

---
