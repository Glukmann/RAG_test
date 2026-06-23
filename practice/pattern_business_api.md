# Практика: Банковская бизнес-логика (ExecuteStep, RunError, GetAccount, IsExistAccount, ПроводкаПоКатегориямУчета)

**Теория:** [BnRSL.md## Структура RSL-программы]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `ОбработатьСчет`

**Источник:** `Mac/Mbr/fnsgmbvdx.mac`  
**Тип:** `private macro`  
**Размер:** 98 строк

```rsl
private macro ОбработатьСчет( recAcc:TRecHandler, PartNum, AccNum, wlregdec )

  record Fin( fininstr ); ClearRecord( Fin );
  record Acc( account  ); ClearRecord( Acc );
  record party( party);
  var tmpstr = "", FullINN = "";
    // Файл \ ВЫПБНДОПОЛ
    StartBlockLogXML("ВЫПБНДОПОЛ");
    /*ПорНом*/
    ЗаписатьПолеЛог( "ПорНом", AccNum );
    /*ПорНомДФ*/
    ЗаписатьПолеЛог( "ПорНомДФ", PartNum );
    /*НомСчВклЭС*/
    ЗаписатьПолеЛог( "НомСч", recAcc.rec.Account );

    var IsDeposit = InList( wlregdec.LnkTypeInfo, 6/*WLD_SUBKIND_FNSINFO_NS2*/, 
                                                  7/*WLD_SUBKIND_FNSINFO_OS2*/,
                                                  8/*WLD_SUBKIND_FNSINFO_VS2*/ );

    var AccDprtName : string = ""; 
    CB_GetDepartmentCodeAndName(recAcc.rec.Department, null, null, AccDprtName);

    /*Блок "Файл \ ВЫПБНДОПОЛ \ Операции"*/
    var query = string (
  "SELECT wlconf.t_DateValue,\n",
  "       wlconf.t_ShifrOper,\n",
  "       wlconf.t_DocNumber,\n",
  "       wlconf.t_DocDate,\n",
  "       wlconf.t_BankAcc  t_CorrAcc,\n",
  "       wlconf.t_BankName t_BankName,\n",
  "       wlconf.t_CodeValue t_BankCode,\n",
  "       wlconf.t_ReceiverINN  t_ClientINN,\n",
  "       wlconf.t_ReceiverKPP  t_ClientKPP,\n",  
  "       wlconf.t_Sum,\n",
  "       wlconf.t_DKFlag,\n",
  "       wlconf.t_Description,\n",  
  "       wlconf.t_ReceiverAccount t_ClientAccount,\n",
  "       wlconf.t_ReceiverName    t_ClientName \n",  
  "  FROM dwlconf_dbt wlconf\n"
  "           WHERE     wlconf.t_HeadID = ?\n",
  "                 AND wlconf.t_HeadKind = " + WLCONF_HEADKIND_WLREGDEC + "\n",
  "                 AND wlconf.t_Account = ?\n",
  "                 AND wlconf.t_FIID = ?\n",
  "                 AND wlconf.t_NumberPart = ?\n"                   
  "        ORDER BY wlconf.t_ConfID;");

    var rs_wlconf:RsdRecordset = execSQLselect(query, 
        MakeArray(SQLParam("", wlregdec.DecisionID),
          SQLParam("", recAcc.rec.Account),
          SQLParam("", recAcc.rec.FIID),
          SQLParam("", int( PartNum ))));
    var ИдБлок = 1;
    if (rs_wlconf)
      while ( rs_wlconf.moveNext() )
        // Файл \ ВЫПБНДОПОЛ \ Операции
        StartBlockLogXML("Операции");
        ЗаписатьПолеЛог( "ИдБлок", string(ИдБлок) );
        ИдБлок = ИдБлок + 1;
        ЗаписатьПолеЛог( "ДатаОпер", YYYYMMDDXML( date(rs_wlconf.value( "t_DateValue" )) ) );
        /*НазнПл*/
        ЗаписатьПолеЛог( "НазнПл", substr( StrSubst ( rs_wlconf.value( "t_Description" ), SYMB_ENDL, SYMB_BLANK), 1, 1000 ) );

        // Файл \ ВЫПБНДОПОЛ \ Операции \ РеквДок
        StartBlockLogXML("РеквДок");
        ЗаписатьПолеЛог( "ВидДок", rs_wlconf.value( "t_ShifrOper" ) );
        ЗаписатьПолеЛог( "НомДок", subStr( rs_wlconf.value( "t_DocNumber" ), 1, 20 ) );

        /*ДатаДок*/
        ЗаписатьПолеЛог( "ДатаДок", YYYYMMDDXML( date(rs_wlconf.value("t_DocDate")) ) );
        FinishBlockLogXML( "РеквДок" );


        // Файл \ ВЫПБНДОПОЛ \ Операции \ РеквБанка
        StartBlockLogXML("РеквБанка");

        /*НомКорСч*/
        ЗаписатьПолеЛог( "НомКорСч", rs_wlconf.value("t_CorrAcc") );

        /*НаимБП*/
        ЗаписатьПолеЛог( "НаимБП", substr( rs_wlconf.value("t_BankName"), 1, 160 ) );

        /*БИКБП*/
        tmpstr = rs_wlconf.value("t_BankCode");
        ЗаписатьПолеЛог( "БИКБП", tmpstr );

        FinishBlockLogXML( "РеквБанка" );


        ФормированиеДанныхКонтрагента(rs_wlconf);

        // Файл \ ВЫПБНДОПОЛ \ Операции \ СуммаОпер
        StartBlockLogXML( "СуммаОпер" );
        /*Дебет*/
        if( rs_wlconf.value( "t_DKFlag" ) == WL_DEBET )
          ЗаписатьПолеЛог( "Дебет", string( rs_wlconf.value( "t_Sum" ) ) );
        else
          ЗаписатьПолеЛог( "Дебет", "0.00" );
        end;
```

---

## Пример 2: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/nptxwrt100.mac`  
**Тип:** `macro`  
**Размер:** 42 строк

```rsl
macro ExecuteStep( Doc, FDoc, DocKind, ID_Operation, ID_Step )
  var paym   = TBFile("pmpaym.dbt");
  var dlrq   = TRecHandler("dlrq.dbt");
  var DtAccount = TRecHandler("account");
  var CtAccount = TRecHandler("account");
  var AccountBuf = TRecHandler("account");
  var rqacc = TRecHandler("dlrqacc");
  var sa = TRecHandler("settacc");
  record nptxop("nptxop");
  record DebProp("pmprop") BTR;
  record CredProp("pmprop") BTR;
  record PayerAccountBuff("account");
  record ReceiverAccountBuff("account");
  var DlRqNew = TRecHandler("dlrq.dbt");
  var PaymentObj = null;
  var Ground = "";
  var tr = null;
  var stat = 0;
  var FD = null;
  var ВидРО = 0;
  var query, Select, DataSet;
  var НеФормироватьПроводкиПоТО = false;
  var Oper = TRecHandler("nptxop.dbt");
  var SumTaxVal = $0.0;
  var rRqAcc = TRecHandler("dlrqacc.dbt");
  var MainTaxAccount = TRecHandler("account.dbt");
  var AddTaxAccount = TRecHandler("account.dbt");
  var party = TRecHandler("party.dbt");
  var Notres = false;
  var Taxe = $0, Taxe15 = $0;
  var nptxopFile = TRecHandLer("nptxop.dbt");
  var СальдирующаяПроводка = false; //Пока всегда отключена. При необходимости нужно заводить настройку и использовать её

  ClearGTT_DNPTXOBJ_TMP();

  SetBuff( nptxop, FDoc );

  Copy(Oper, nptxop);

  if((nptxop.SubKind_Operation != DL_NPTXOP_WRTKIND_ENROL) and (nptxop.FlagTax == SET_CHAR)) //если НЕ зачисление и налог удерживается
    stat = CreateHoldTaxObjects8(Oper, ID_Step, abs(Oper.rec.Tax), @Taxe, @Taxe15);
  end;
```

---

## Пример 3: `CalcDepoCommReserveByAcc`

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

## Пример 4: `ExecuteStep`

**Источник:** `Mac/Cb/fssprecal10.mac`  
**Тип:** `macro`  
**Размер:** 46 строк

```rsl
macro ExecuteStep
(
  dldoc        : memaddr,
  doc          : memaddr,                            
  DocKind      : integer,
  ID_Operation : integer,
  ID_Step      : integer                           
)
// begin
  var stat = 0, result;
  var msg;
  var iter, AccIter;
  var PayedObj, PayedObjDocs;
  var DoublerIntersects;
  var AccEquire = FssRequireObj.AccEquire;
  
  var DocTypeSet = makeArray(O_IP_ACT_GACCOUNT_MONEY, O_IP_ACT_CURRENCY_ROUB, O_IP_ACT_ENDARR_GMONEY);
  if (not FSSP_FindArrestedRequire(FssRequireObj.InternalKey, FssRequireObj.DocInfoDate, DocTypeSet, PayedObj))
    msg = GetErrMsg();
    FSSP_OpMsg("Отзыв не может быть выполнен: " + msg);

    //FssRequireObj.State = FSSPREQUIRE_NOTEXECUTED;
    FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_CANT_TERM; // Обращение взыскания не может быть прекращено в связи с отсутствием постановления об обращении взыскания
    FssRequireObj.RestrictionAnswerType = FSSPACCEQUIRE_AT_PRIMARY; // Постановление не исполнено в связи с отсутствием первичного Постановления
    InsertOprStatus(RSBFSSREQUIRE_OPST_DOCUMENT, RSBFSSREQUIRE_DS_NOTIFY);
    
    return 0;
  else
    FssRequireObj.GetDoublerIntersects(PayedObj, DoublerIntersects);

    if (not DoublerIntersects.size)
      // Если пересечений нет 
      stat = FssRequireObj.Compare(PayedObj);

      if (stat)
        //FssRequireObj.State = FSSPREQUIRE_NOTEXECUTED;
        FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_OTHER_CLIENT; // Арест наложен на другого должника
        FssRequireObj.RestrictionAnswerType = FSSPACCEQUIRE_AT_OTHER; // Постановление не исполнено по иным причинам

        AccIter = AccEquire.First();
        while (AccIter)
          if (not AccEquire.IsExcluded)
            // Счёт найден, но принадлежит другому клиенту
            AccEquire.ArrestRecoveryState = FSSPACCEQUIRE_RT_FOUND_OTHER_CLIENT; 
            AccEquire.Update();
          end;
```

---

## Пример 5: `ExecuteStep`

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

## Пример 6: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/nptxwrt050.mac`  
**Тип:** `macro`  
**Размер:** 31 строк

```rsl
macro ExecuteStep( kind_oper, FDoc, DocKind, ID_Operation, ID_Step )
  record nptxop("nptxop");
  var err = 0;
  var nptxopFile = TRecHandLer("nptxop.dbt");
  var Bg = $0.0, Bs = $0.0, Pm = $0, Pg = $0.0, Pd = $0, Ps = $0.0, Po = $0.0, Tout = $0.0, ToutNat = $0.0, Dg = $0.0, Ds = $0.0, Bm = $0.0, Dm = $0.0, Bd = $0.0, Bpd = $0.0, Pp = $0, Bp = $0, Dp = $0;
  var SO = $0.0;
  var Rg = 0.0, Rs = 0.0, Rp = 0.0;  
  var DataSet;
  var sfcontr = TBFile("sfcontr.dbt");
  var IIS = UNSET_CHAR;
  var TaxPay = $0;
  var AccAccDS;
  var AccTaxDS;
  var MaxTaxe1 = $0, MaxTaxe2 = $0;
  var year = 0;
  var NumberOp = "";
  var Dg1 = $0.0, Dg2 = $0.0, Dg9 = $0.0, Dp1 = $0.0, Dp2 = $0.0, Dp9 = $0.0;
  
  SetBuff( nptxop, FDoc );
  var Dbeg:date, Dend:date = nptxop.OperDate;

  DateSplit(nptxop.OperDate, NULL, NULL, year);
  
  nptxopFile.Clear();

  if(ЕстьНеисполненнаяПорожденнаяОперация(nptxop.ID, @NumberOp))
    if(isOprMultiExec()OR (MsgBoxEx( "Порождённая операция расчёта НОБ № "+ NumberOp +" не выполнена. Продолжить выполнение текущей операции зачисления/списания? ",
                   MB_YES+MB_NO, IND_YES/*, 
                   "", ""*/) != IND_YES ))
       return 1;
    end;
```

---

## Пример 7: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/scoverdr.mac`  
**Тип:** `macro`  
**Размер:** 29 строк

```rsl
macro ExecuteStep( Doc, FDoc )

  var    FD, dat, error; 
  var    SumNKD = $0, AvoirCost = $0, NewSum = $0, OldSum = $0, D = $0, Kind = ""; 
  var    ВыполненоВидовПереоценки = 0, ExistsCourse = false, SinceDate; 
  var    RateRec = $0, err;

  var    DlMarket = TBFile( "dlmarket.dbt", "R", 0 ), MarketID = null, CentrOffice = null; 

  SetBuff( deal, FDoc ); 
  dat = ScOprServDoc.CommDate; 
  FD = SPFirstDoc( deal );

  var датаОстатка = DL_GetBalanceDateAfterWorkDayByCalendar(dat, 0, FD.ПолучитьКалендСвязанный());

  /*переоценка по валюте*/ 
  /*4. Если Flag2 ==да и в сделке (ВЦ != НацВ и ВР = НацВ и ВН = НацВ) */
  /* выполнить переоценку по валюте*/ 
  if( (ScOprServDoc.Flag2 == SET_CHAR) AND 
      (FD.dl_leg.rec.CFI != NATCUR) AND (FD.GetParametr(MC_TYPE_PARAMETR_PAYCURRENCY) == NATCUR) AND (FD.fininstr.rec.FaceValueFI == NATCUR)
  )        
     /*ВыполненоВидовПереоценки = ВыполненоВидовПереоценки + 1;        */

     /*счет переоценки требований*/
     if( ОпределитьПереоцениваемыйСчет( FD, dat, "Т" ) != 0 )
        return 1;
        InsertErrorLog_XML(ScOprServDoc.DocumentID, ScOprServDoc.DocKind);
        ClearErrorArr();
     end;
```

---

## Пример 8: `GenMes`

**Источник:** `Mac/Mbr/swgm910r.mac`  
**Тип:** `macro`  
**Размер:** 47 строк

```rsl
macro GenMes( addrMes, addrConf )
  var field_value;
  var PaymentObj, Tag;

  SetBuff( wlmes,  addrMes );
  SetBuff( wlconf, addrConf );

  PrintLog(2,"Генерация сообщения по МТ910 стандарт RUR5");

  /* 20 - номер транзакции (документа) */
  ЗаписатьПолеЛог( TransactionReferenceNumberField, wlmes.TRN );

  /* 21 Related Reference */
  field_value = FillRelatedReferenceForDebitCreditConfirmation(wlconf);
  ЗаписатьПолеЛог( RelatedReferenceField, field_value );

  /* 25 - счет подтверждения */
  ЗаписатьПолеЛог( AccountIdentificationField, wlconf.Account );
  
  /* 13D - Date/Time Indication */
  field_value = GetSWIFTDate( date() ) + GetSWIFTTime(Time()) + GetSessTimeZone();
  ЗаписатьПолеЛог( DateTimeIndicationField, field_value );  
  
  /* 32A - дата валютирования, код валюты, сумма */
  field_value = GetSWIFTDate( wlconf.DateValue ) +
                ПолучитьКодВалютыЛог( wlconf.FIID ) +
                GetSWIFTAmount( wlconf.Sum );
  ЗаписатьПолеЛог( ValueDateCurrencyCodeAmountField_A, field_value );

  debugbreak;
  PaymentObj = RsbPayment(wlconf.DocumentID);
  // Если плательщик - банк, то заполняем поле 52а, в противном случае - 50a
  if( ((PaymentObj.Payer > 0) and ВидСубъекта(PaymentObj.Payer, PTK_BANK)) or ( not IsClientPayerAccount(PaymentObj) ) )
    /* 52a - банк приказодателя */
    if( (wlconf.CodeValue!="") OR (wlconf.BankName!="") )
      ClearRecord(Route);
      Route.PartyID  = wlconf.BankID;
      Route.CodeKind = wlconf.CodeKind;
      Route.CodeName = wlconf.CodeName;
      Route.CodeValue = wlconf.CodeValue;
      Route.Name = wlconf.BankName;
      Route.InAccount = "";
      Route.OutAccount = "";
      ЗаписатьПолеМаршрутаКонтекст0Лог( OrderingInstitutionField, "52a", Route, "", "", ST_RUR5 );
      if( not УстановитьКонтекстБлока( ".." ) )
         RunError("|Ошибка при установке контекста блока ..");
      end;
```

---

## Пример 9: `GetClientProductList`

**Источник:** `Mac/Cb/ws_rscore2ikfl.mac`  
**Тип:** `macro`  
**Размер:** 57 строк

```rsl
macro GetClientProductList(Request)
  var wsRequest = TWsGetClientProductListRequest;
  var i, j, k;
  var query = "";
  var rs;
  var params = TArray;
  var newElem;
  var Response;
  var ServiceKind;
  var SfContrID;

  WS_SetAttributeValue(@wsRequest.PartyID    , 0, "Request", "PartyID"    , Request, V_INTEGER, true , null, true);
  WS_SetAttributeValue(@wsRequest.ObjectTypes, 0, "Request", "ObjectTypes", Request, V_GENOBJ , false, null, true);
  WS_SetAttributeValue(@wsRequest.Rows       , 0, "Request", "Rows"       , Request, V_INTEGER, false, null, true);
  WS_SetAttributeValue(@wsRequest.OnDate     , 0, "Request", "OnDate"     , Request, V_DATE   , false, null, true);
  WS_SetAttributeValue(@wsRequest.Oper       , 0, "Request", "Oper"       , Request, V_INTEGER, false, null, true);
  WS_SetAttributeValue(@wsRequest.Department , 0, "Request", "Department" , Request, V_INTEGER, false, null, true);
  WS_SetAttributeValue(@wsRequest.Roles      , 0, "Request", "Roles"      , Request, V_GENOBJ , false, null, true);

  query = query + "SELECT ";
  query = query + "  pc.t_ClientProductID AS ClientProductID ";
  query = query + " ,pc.t_ProductID AS ProductID ";
  query = query + " ,pp.t_Name AS ProductName ";
  query = query + " ,pp.t_ServiceKind AS ServiceKind ";
  query = query + " ,pc.t_PartyID AS PartyID ";
  //query = query + " ,pcr.t_Role AS Role ";
  query = query + " ,pp.t_ProductKindID AS ProductKindID ";
  query = query + " ,pk.t_Name AS ProductKindName ";
  query = query + " ,pc.t_DocNumber AS DocNumber ";
  query = query + " ,pc.t_Branch AS Branch ";
  query = query + " ,pc.t_BeginDate AS BeginDate ";
  query = query + " ,pc.t_EndDate AS EndDate ";
  query = query + " ,pc.t_ParentClientProductID AS ParentClientProductID ";
  query = query + " ,pc.t_ObjectType AS ObjectType ";
  query = query + " ,ob.t_Name AS ObjectName ";
  query = query + " ,pc.t_ObjectID AS ObjectID ";
  query = query + " ,pc.t_SfContrID AS SfContrID ";
  query = query + "  FROM ";
  query = query + "    dprdclient_dbt pc ";
  query = query + "   ,dprdproduct_dbt pp ";
  //query = query + "   ,dprdclntrole_dbt pcr ";
  query = query + "   ,dprdkind_dbt pk ";
  query = query + "   ,dobjects_dbt ob ";
  query = query + " WHERE pc.t_ProductID = pp.t_ProductID ";
  //query = query + "   AND pcr.t_ClientProductID = pc.t_ClientProductID ";
  //query = query + "   AND pcr.t_PartyID = pc.t_PartyID ";
  query = query + "   AND pk.t_ProductKindID = pp.t_ProductKindID ";
  query = query + "   AND ob.t_ObjectType = pc.t_ObjectType ";

  if(_CheckPartyID(wsRequest.PartyID) < 0)
    RunError("Задано некорректное значение поля: идентификатор/код субъекта", 0);
  else
    query = query + "   AND pc.t_PartyID = ? ";

    j = params.size;
    params[j] = SQLParam("", wsRequest.PartyID);
  end;
```

---

## Пример 10: `ExecuteStep`

**Источник:** `Mac/Cb/fssplivingwage10.mac`  
**Тип:** `macro`  
**Размер:** 46 строк

```rsl
macro ExecuteStep
(
  dldoc        : memaddr,
  doc          : memaddr,                            
  DocKind      : integer,
  ID_Operation : integer,
  ID_Step      : integer                           
)
// begin
  var stat = 0;
  var PreviousObj;
  var DoublerIntersects;
  var AccEquire = FssRequireObj.AccEquire;

  if ( (FssRequireObj.DocType == O_IP_ACT_CHNG_LIVING_WAGE) or (FssRequireObj.DocType == O_IP_ACT_END_LIVING_WAGE) )
    // Если вид Нового требования равен O_IP_ACT_CHNG_LIVING_WAGE или O_IP_ACT_END_LIVING_WAGE 
    var DocTypeSet = makeArray(O_IP_ACT_LIVING_WAGE, O_IP_ACT_LIVING_WAGE_COURT, O_IP_ACT_ARREST_ACCMONEY, 
      O_IP_ACT_ENDARR_GMONEY, O_IP_ACT_GACCOUNT_MONEY, O_IP_ACT_CURRENCY_ROUB
    );

    if (not FSSP_FindArrestedRequire(FssRequireObj.InternalKey, FssRequireObj.DocInfoDate, DocTypeSet, PreviousObj))
      FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_REQLIVINGWAGENOTFOUND; // Пост. с требованием о сохранении прожит. минимума не найдено
      FssRequireObj.RestrictionAnswerType = FSSPACCEQUIRE_AT_OTHER; // Постановление не исполнено по иным причинам
      InsertOprStatus(RSBFSSREQUIRE_OPST_DOCUMENT, RSBFSSREQUIRE_DS_NOTIFY);

      FSSP_OpMsg("Постановление с требованием о сохранении прожиточного  минимума не найдено");

      return 0;
    else
      // Сравнить субъектов-должников в Предыдущем и Новом требованиях
      FssRequireObj.GetDoublerIntersects(PreviousObj, DoublerIntersects);

      if (not DoublerIntersects.size)
        // Если пересечений нет 
        stat = FssRequireObj.Compare(PreviousObj);

        if (stat)
          FssRequireObj.State = FSSPREQUIRE_NOTEXECUTED;
          FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_LIVINGWAGEOTHERPERSON; // Пост. с требованием о сохранении прожит. минимума вынесено по иному лицу
          FssRequireObj.RestrictionAnswerType = FSSPACCEQUIRE_AT_OTHER; // Постановление не исполнено по иным причинам
          InsertOprStatus(RSBFSSREQUIRE_OPST_DOCUMENT, RSBFSSREQUIRE_DS_NOTIFY);

          FSSP_OpMsg("Постановление с требованием о сохранении прожиточного минимума вынесено по иному лицу");

          return 0;
        end;
```

---

## Пример 11: `ExecuteStep`

**Источник:** `Mac/DLNG/VA/vaoverfrbnr.mac`  
**Тип:** `macro`  
**Размер:** 23 строк

```rsl
MACRO ExecuteStep(Buffer, FirstDoc)
  var query, cmd, DataSet;
  var CatDeb = "", CatCred = "", Ground = "";
  var DebAcc = "", CredAcc = "";
  var stat = 0;
  var Дата={curdate};
  var AvoirKind = AVOIRISSKIND_BILL;
  var ObjType = OverObjType;
  record bnr( vsbanner );
  var banFd;
  var СчетВекселя;
  var БС, СС, СП, ПервПереоц;
  var МинусПереоценкаСчет, ПлюсПереоценкаСчет;
  var МинусПереоценкаОстаток, ПлюсПереоценкаОстаток;
  var ТекущийПлюсПереоценкаКат, ТекущийМинусПереоценкаКат,
      ТекущийПлюсДоходыКат, ТекущийМинусРасходыКат;
  
  SetBuff( bnr, FirstDoc );

  if (ValType(OprServDoc) != V_UNDEF)
    if(OprServDoc.ValueDate > date(0,0,0))
      Дата = OprServDoc.ValueDate;
    end;
```

---

## Пример 12: `ExecuteStep`

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

## Пример 13: `РассчитатьКомиссии`

**Источник:** `Mac/DLNG/TRUST/TsChargeCom.mac`  
**Тип:** `macro`  
**Размер:** 38 строк

```rsl
MACRO РассчитатьКомиссии( _ServOp:MEMADDR )

  var OrderOFBU:TS_OrderFD = NULL;
  var cmd, fCalcItogs, RecCount = 0, MaxRecCount;

  ServOp.SetRecordAddr( _ServOp );
  OrderOFBU = TS_OrderFD( 0, ServOp.rec.OrderID );

  InitProgress( -1, "Операция начисления комиссии за управление ДОФБУ", "Отбор договоров для операции");
  cmd = RsdCommand(RslDefCon, "begin\n TrustAPI.SelectOrdersForChargeCom(?);\n end; ");
  cmd.NullConversion = true;
  cmd.addParam( "", RSDBP_IN, ServOp.rec.ID );
  cmd.execute();

  MaxRecCount = SQL_GetNRecs( "SELECT * FROM DTSCALCITOGS_TMP WHERE t_Exclude = chr(0)" );
  RemProgress();

  InitProgress( MaxRecCount, "Выполнение ...", "Операция начисления комиссии за управление ДОФБУ" );
  fCalcItogs = TBfile( "TSCALCITOGS.TMP", "W", 0 );
  fCalcItogs.AddFilter(" t_Exclude = chr(0) " );

  while( fCalcItogs.Next() )
     if( fCalcItogs.rec.Sort == 0 )
        /* Для ДП ОФБУ */
        var OrderFD = TS_OrderFD( 0, fCalcItogs.rec.OrderID );
        var ДатаПервичногоВнесения = OrderFD.ДатаПервичногоВнесения();
        var ДатаПолногоВывода      = OrderFD.ДатаПолногоВывода();

        if( (ДатаПервичногоВнесения == Date(0,0,0)) OR (ДатаПервичногоВнесения >= ServOp.rec.EndDate) OR
            ((ДатаПолногоВывода != Date(0,0,0)) AND (ДатаПолногоВывода <= ServOp.rec.BegDate))
          )
           /*удаляем ненужные договора ккоторые окончились до начала периода или начинаются после периода*/
           fCalcItogs.Delete();
        else
           if( ПересчитатьКомиссии( ServOp, fCalcItogs, OrderFD, OrderOFBU ) == 0 )
              if( not fCalcItogs.update() )
                 runerror( "ошибка при обновлении записи в DTSCALCITOGS_TMP" );
              end;
```

---

## Пример 14: `ExecuteStep`

**Источник:** `Mac/Cb/case_or.mac`  
**Тип:** `macro`  
**Размер:** 27 строк

```rsl
macro ExecuteStep( doc, primdoc, DocKind, ID_Operation )

  file   accaseFile("accase.dbt");
  record accasscs(accasscs);
  record accase(accase);
  
  var IncomeReserveAccount : string;
  var OutlayReserveAccount : string;
  var ReserveAccount : string;
  var accasePD : AccCasePrimdoc;
  var query, rs;
  var params : TArray;
  var queryCase, rsCase;
  var paramsCase : TArray;
  var ReserveType : integer;
  var ReserveKind : integer;
  var ClassifReserve : string;
  var IncomeCatCodePrm;
  var OutlayCatCodePrm;

  SetBuff( accasscs, primdoc );

  accaseFile.CaseID = accasscs.CaseID;

  if( GetEQ( accaseFile ) )
    Copy( accase, accaseFile );
  end;
```

---

## Пример 15: `ExecuteStep`

**Источник:** `Mac/Cb/sfsrvpay.mac`  
**Тип:** `macro`  
**Размер:** 44 строк

```rsl
macro ExecuteStep( outBuff, primDoc )

  var stat = 0;

  setbuff( SfContr, primDoc  );

  var rs, cmd;
  record SfDefCom("sfdef.dbt");
  record SfAccrue("sfaccrue.dbt");

  var PayerAccount = "", ReceiverAccount = "";
  var NDSPayerAccount : string, NDSReceiverAccount : string;

  var prevFIID_CommSum = -1;
  var PayerFIID = -1, ReceiverFIID = -1;

  var SfConComPD : SfConComPrimDoc;
  var IsNVPI:bool;

  var AccTrnID:bigint = 0, AccTrnID_NDS:bigint = 0;

  var Action = DEFCOM_ACTIONKIND_PAY;
  var Comment = "";

  cmd = RsdCommand( " SELECT * FROM DSFDEFTMP_TMP WHERE t_Action = ? AND t_Skip = chr(0) " +
                    " ORDER BY t_ConID, t_ConComID, t_FIID_CommSum "  );
  cmd.addParam( "", RSDBP_IN, Action );

  rs = RsdRecordset( cmd );
  while( rs.moveNext() )    

    SfSrv_FillSfDefComRecord( rs, SfDefCom );
    SfSrv_FillSfAccrueRecord( rs, SfAccrue );
    
    if( prevFIID_CommSum != SfDefCom.FIID_Sum )
      prevFIID_CommSum = SfDefCom.FIID_Sum;
      IsNVPI = SfSrv_IsNVPICarry( SfContr.PayFIID, SfDefCom.FIID_Sum, SfContr.PayRateDateKind );

      SfConComPD = SfConComPrimDoc( 83, SfConComRec, SfContr, SfDefCom.FIID_Sum);

      stat = SfSrv_GetCarryParms( IsNVPI, SfConComPD, SfDefCom, SfAccrue, SfContr,  
                                  @PayerFIID, @ReceiverFIID,
                                  @PayerAccount, @ReceiverAccount, @NDSPayerAccount, @NDSReceiverAccount, 0, 0 );
    end;
```

---

