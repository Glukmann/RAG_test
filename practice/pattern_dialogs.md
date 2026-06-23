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

