# Практика: Коллекции, навигация и доступ к полям (value, moveNext, SetParm, GetFieldValue, SetFieldValue)

**Теория:** [BnRSL.md## Класс: `TArray`]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `GetOkatoList`

**Источник:** `Mac/Cb/ws_getparty.mac`  
**Тип:** `macro`  
**Размер:** 67 строк

```rsl
macro GetOkatoList()

  var cmd, rs;

  var Rec = TRecHandler("objattr");
  var Arr = TArray;

  // var query = "          SELECT t_objecttype, " +
              // "                 t_groupid, " +
              // "                 t_attrid, " +
              // "                 t_parentid, " +
              // "                 t_codelist, " +
              // "                 t_numinlist, " +
              // "                 t_nameobject, " +
              // "                 t_chattr, " +
              // "                 t_longattr, " +
              // "                 t_intattr, " +
              // "                 t_name, " +
              // "                 t_fullname, " +
              // "                 t_opendate, " +
              // "                 t_closedate, " +
              // "                 t_classificator, " +
              // "                 t_corractype, " +
              // "                 t_balance, " +
              // "                 t_isobject, " +
              // "                 LEVEL " +
              // "          FROM dobjattr_dbt t " +
              // "                  START WITH (t.t_parentid = 0 AND t.t_objecttype = 3 AND t.t_groupid = 12) " +
              // "                  CONNECT BY     PRIOR t.t_objecttype = t.t_objecttype " +
              // "                             AND PRIOR t.t_groupid = t.t_groupid " +
              // "                             AND PRIOR t.t_attrid = t.t_parentid " +
              // "           ORDER SIBLINGS BY t.t_codelist, LPAD (t.t_numinlist, 35, '0')";

  var query = "          SELECT t_objecttype, " +
              "                 t_groupid, " +
              "                 t_attrid, " +
              "                 t_parentid, " +
              "                 t_codelist, " +
              "                 t_numinlist, " +
              "                 t_nameobject, " +
              "                 t_chattr, " +
              "                 t_longattr, " +
              "                 t_intattr, " +
              "                 t_name, " +
              "                 t_fullname, " +
              "                 t_opendate, " +
              "                 t_closedate, " +
              "                 t_classificator, " +
              "                 t_corractype, " +
              "                 t_balance, " +
              "                 t_isobject " +
              "          FROM dobjattr_dbt t " +
              "          WHERE t.t_parentid = 0 AND t.t_objecttype = 3 AND t.t_groupid = 12";

  cmd = RsdCommand(query);
  rs = RsdRecordset(cmd);

  while(rs.movenext)

    _CopyRecordsetToRecHandler(rs, Rec);

    var p = TRecHandler("objattr");
    copy(p, Rec);

    Arr[Arr.size] = p.rec;

  end;
```

---

## Пример 2: `ОбработатьСчет`

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

## Пример 3: `SfFormDocumentsBatch`

**Источник:** `Mac/Cb/sfcrpaybatch.mac`  
**Тип:** `private macro`  
**Размер:** 157 строк

```rsl
private macro SfFormDocumentsBatch(sfdefArray, sfrepaccCache, SfSrvDoc)
  var stat:integer = 0;
  var cmd, rs, strSql;
  var accTrnData;

  // Для сохранения ошибок
  var ErrorStatusArray  = TArray;
  var ErrorMessageArray = TArray; 
  var DocKindArray      = TArray;
  var DocumentIDArray   = TArray;

  var BankID = {OurBank};
  var OperDprt = {OperDprt};

  // Получить свободный остаток на счете плательщика с учетом претензий
  strSql = "UPDATE dsfpaydoc_tmp tmp " +
           "SET tmp.t_FreeRest = (SELECT RSI_RsbAccTransaction.AccGetFreeAmountEx( ac.t_accountid, tmp.t_DateCarry, -1, 0, 0 ) " +
           "                        FROM daccount_dbt ac " +
           "                       WHERE ac.t_account = tmp.t_PayerAccount AND ac.t_chapter = 1 AND ac.t_code_currency = tmp.t_PayerFIID) " +
	   "WHERE EXISTS (SELECT ac.t_accountid FROM daccount_dbt ac " +
           "               WHERE ac.t_account = tmp.t_PayerAccount AND ac.t_chapter = 1 AND ac.t_code_currency = tmp.t_PayerFIID) ";

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.execute();   


  // Получить свободный остаток с учетом картотек
  strSql = "UPDATE dsfpaydoc_tmp tmp " +
           "SET tmp.t_FreeRest = tmp.t_FreeRest +" +
           "  (SELECT NVL(SUM(ind.t_Sum),0) FROM dpsindacc_dbt ind " +
           "    WHERE ind.t_account = tmp.t_PayerAccount " +
           "    AND ind.t_chapter = 1 AND ind.t_fiid = tmp.t_PayerFIID) ";

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.execute();   


  // Перевести суммы комиссии и НДС в нужные валюты
    // Сумму свободного остатка в валюту счетов по КУ, если получатель наш банк и комиссия начислена:
  strSql = " UPDATE dsfpaydoc_tmp tmp " +
           " SET tmp.t_ConvFreeRest = " +
           " RSI_RSB_FIInstr.ConvSum( tmp.t_FreeRest, tmp.t_PayerFIID, tmp.t_FIIDPaySum, tmp.t_DateCarry, 0 ) "; 
//           " WHERE t_PayerFIID <> t_FIIDPaySum " ;

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.execute();   

    //Суммы оплаты комиссии и ее НДС в  валюту счетов по КУ
  strSql = " UPDATE dsfpaydoc_tmp tmp                                                                                         " +
           " SET tmp.t_ConvPaySum =                                                                                           " +
           "       RSI_RSB_FIInstr.ConvSumType( tmp.t_PaySum, tmp.t_FIIDSum, tmp.t_FIIDPaySum, t_RateType, tmp.t_DateCarry, 0 ), " +
           "     tmp.t_ConvTaxSum =                                                                                           " +
           "       RSI_RSB_FIInstr.ConvSumType( tmp.t_TaxSum, tmp.t_FIIDSum, tmp.t_FIIDPaySum, t_RateType, tmp.t_DateCarry, 0 )  " +
           " WHERE tmp.t_FIIDSum <> tmp.t_FIIDPaySum                                                                             " ;

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.execute();   

    //  Сумму комиссии в валюту счета получателя, если получатель не наши банк или по комиссии не было начисления:
  strSql = " UPDATE dsfpaydoc_tmp tmp                                                                                 " +
           " SET tmp.t_ConvPaySum =                                                                                   " +
           "       RSI_RSB_FIInstr.ConvSum( tmp.t_ConvPaySum, tmp.t_FIIDPaySum, tmp.t_ReceiverFIID, tmp.t_DateCarry, 0 ) " +
           " WHERE tmp.t_FIIDPaySum <> tmp.t_ReceiverFIID                                                                " +
           "   AND (tmp.t_ReceiverID != ? OR tmp.t_IsIncluded != 'X')                                          " ;

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.addParam( "", RSDBP_IN, BankID );
  cmd.execute();   

    // Сумму НДС комиссии из валюты счета по КУ в нац. валюту для проводки учета НДС:
  strSql = " UPDATE dsfpaydoc_tmp tmp                                                                      " +
           " SET tmp.t_ConvTaxSumNC =                                                                      " +
           "       RSI_RSB_FIInstr.ConvSum( tmp.t_ConvTaxSum, tmp.t_FIIDPaySum, ?, tmp.t_DateCarry, 0 )       " +
           " WHERE tmp.t_FIIDPaySum <> ?                                                                      " ;

  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.addParam( "", RSDBP_IN, NATCUR    );
  cmd.addParam( "", RSDBP_IN, NATCUR    );
  cmd.execute();   

  strSql = " UPDATE dsfpaydoc_tmp tmp " +
           " SET tmp.t_Error = ?, " +
           "     tmp.t_ErrMsg = ? " +
           " WHERE t_ConvFreeRest < (t_ConvPaySum + t_ConvTaxSum) " +
           "   AND NOT EXISTS(SELECT ac.t_accountid FROM daccount_dbt ac " +
           "                  WHERE ac.t_account = tmp.t_PayerAccount AND ac.t_chapter = 1 AND ac.t_code_currency = tmp.t_PayerFIID " +
           "                  AND ac.t_Type_Account LIKE ('%Ф%')) "; 


  cmd = RsdCommand( strSql );
  cmd.NullConversion = true;
  cmd.addParam( "", RSDBP_IN, 1 );
  cmd.addParam( "", RSDBP_IN, "Недостаточно средств на счете плательщика. Формирование проводки оплаты невозможно." );
  cmd.execute();   
         
  var IsBankOrderForComm = bBankorderForComm_Setting();

  var sfdefAccTrnCharger = TSfDefAccTrnDataCharger();

    strSql = " SELECT paydoc.*, NVL(ground.t_Ground, chr(1)) As groundVO, payeracc.t_Department As PayerDprt, recacc.t_Department As RecDprt, fininstr.t_Ccy As fiidCCY, " +
             "        DECODE(paydoc.t_RateType,0, RSI_RSB_FIInstr.ConvSum(paydoc.t_PaySum + paydoc.t_TaxSum , paydoc.t_FIIDSum, paydoc.t_FIIDPaySum, paydoc.t_DateCarry, 0 ), "
             "                                    RSI_RSB_FIInstr.ConvSumType(paydoc.t_PaySum + paydoc.t_TaxSum , paydoc.t_FIIDSum, paydoc.t_FIIDPaySum, paydoc.t_RateType, paydoc.t_DateCarry, 0 )) As ConvTotalSum, " +
             "        RSI_RSB_FIInstr.ConvSum(paydoc.t_PaySum + paydoc.t_TaxSum , paydoc.t_FIIDSum, paydoc.t_PayerFIID, paydoc.t_DateCarry, 0 ) As ConvTotalSumPayer, " +
             "        RSI_RSB_FIInstr.ConvSum(paydoc.t_PaySum, paydoc.t_FIIDSum, paydoc.t_PayerFIID, paydoc.t_DateCarry, 0 ) As ConvPaySumPayer, " +
             "        RSI_RSB_FIInstr.ConvSum(paydoc.t_ConvTaxSum , paydoc.t_FIIDPaySum, paydoc.t_PayerFIID, paydoc.t_DateCarry, 0 ) As ConvTaxSumPayer " +
             " FROM dsfpaydoc_tmp paydoc, dsfground_tmp ground, daccount_dbt payeracc, daccount_dbt recacc, dfininstr_dbt fininstr" + 
             " WHERE paydoc.t_SfDefID = ground.t_SfDefID(+) " + 
             " AND payeracc.t_Account = paydoc.t_PayerAccount " + 
             " AND payeracc.t_Chapter = 1 " + 
             " AND payeracc.t_Code_Currency = paydoc.t_PayerFIID " + 
             " AND recacc.t_Account = paydoc.t_ReceiverAccount " + 
             " AND recacc.t_Chapter = 1 " + 
             " AND recacc.t_Code_Currency = paydoc.t_ReceiverFIID " +
             " AND fininstr.t_FIID = paydoc.t_FIIDSum "; 


   cmd = RsdCommand( strSql ); 
   cmd.NullConversion = true;

   cmd.execute();   
   var i = 0;
   rs = RsdRecordset( cmd ); 
   while( rs.moveNext() )
     var ErrorNum = rs.value("t_Error"); 
     var ErrorMsg = rs.value("t_ErrMsg"); 
     var SfDefArrayIndex = rs.value("t_ArrayIndex");
     if(ErrorNum != 0)

       sfdefArray[SfDefArrayIndex].Error = ErrorNum;
       // Сформировать соответствующую запись для отчета sfrepacc.tmp.
       var sfrepacc = TRecHandler ("sfrepacc.tmp");
       ClearRecord( sfrepacc );
                                                                 
       sfrepacc.rec.debit           = rs.value("t_PayerAccount");
       sfrepacc.rec.credit          = rs.value("t_CalcAccount");  //счет кредита проводки
       sfrepacc.rec.BeginDate       = sfdefArray[SfDefArrayIndex].SfDef.rec.DatePeriodBegin;
       sfrepacc.rec.EndDate         = sfdefArray[SfDefArrayIndex].SfDef.rec.DatePeriodEnd  ;
       sfrepacc.rec.TransactionDate = rs.value("t_DateCarry"); 
       sfrepacc.rec.Amount          = rs.value("t_ConvPaySum") + rs.value("t_ConvTaxSum");
       sfrepacc.rec.ContrID         = sfdefArray[SfDefArrayIndex].SfDef.rec.SfContrID    ;
       sfrepacc.rec.FeeType         = SF_FEE_TYPE_PERIOD;                                ;
       sfrepacc.rec.ComissNumber    = sfdefArray[SfDefArrayIndex].SfDef.rec.CommNumber   ;
       sfrepacc.rec.Comment         = ErrorMsg;
       sfrepacc.rec.ErrorCode       = ErrorNum;
       sfrepacc.rec.SfDefcomID      = rs.value("t_SfDefID");
       sfrepacc.rec.Kind            = 1;
       sfrepacc.rec.Department      = sfdefArray[SfDefArrayIndex].SfDef.rec.Department   ;

       if(sfrepaccCache != NULL)
         sfrepaccCache.AddRecord( sfrepacc );
       end;
```

---

## Пример 4: `_ExecuteDepoAcc`

**Источник:** `Mac/DLNG/SECUR/sc_depoacc.mac`  
**Тип:** `private macro`  
**Размер:** 38 строк

```rsl
private macro _ExecuteDepoAcc(_taskID, _execID, _conveyerID, _operationID, _packetID, dl_comm, Department, ClientID, Session, MarketSchemeID, FIID, IsOwnSec)
  var query, cmd, DataSet;
  var DepSet  = TBFile( "dldepset.dbt", "R", 0 );
  var cnt = 1;
  var PrevDepSetID = -1, PrevClientID = 0, prevClientContrID = -1, PrevSession = -2, PrevDocKind = 0;
  var Consolidate = DEPSET_METHODFORMDRAFT_BYDEAL, OwnConsolidate = DEPSET_METHODFORMDRAFT_BYDEAL;
  var ClientConsolidate = DEPSET_METHODFORMDRAFT_BYDEAL;
  var MethodFormPD = DL_METHODFORMPD_EVERY, OwnMethodFormPD = DL_METHODFORMPD_EVERY;
  var ClientMethodFormPD = DL_METHODFORMPD_EVERY;
  var CurrConsolidate = DEPSET_METHODFORMDRAFT_BYDEAL, AddTransAcc = UNSET_CHAR, AddTransAccCln = UNSET_CHAR, CurrAddTransAcc, MarketID;
  var stat = 0, err = 0;
  var DealPart = 0, IsContrGr = false, BuySale;
  var Type, Account, State, Owner, AccountDeponent;
  var needDraft = true;
  record sf(sfcontr);
  var avr_dlrq = TRecHandler("dlrq");
  var num = 0;
  var GrDealForLnkTransAcc = NULL;
  var CntDealDraft = 0;
  var ExDepSet = false;
//  var isQDA = 0;
//  GetRegistryValue("SECUR\\ВЕДЕНИЕ КДУ", V_INTEGER, isQDA);

  FormPD = DL_FormationPD();
  GrDealForLnk = TLnkGrDealToDraft(dl_comm.rec.DocKind, dl_comm.rec.DocumentID, false);

  GrDealForLnkTransAcc = TLnkGrDealToDraft(dl_comm.rec.DocKind, dl_comm.rec.DocumentID, true);
  
  cmd = DL_RSDCommand();

  if((_conveyerID) and (_packetID))
    query =  "with cnvdoc as (select * from dcnvdoc_dbt where t_ExecID = ? and t_ConvTypeID = ? and t_PackID = ?)";
    cmd.AddParam(_execID);
    cmd.AddParam(_conveyerID);
    cmd.AddParam(_packetID);
  else
    query =  "with cnvdoc as ("+GetDepoAccObjectQuery(dl_comm, Department, ClientID, Session, MarketSchemeID, FIID, IsOwnSec)+")";
  end;
```

---

## Пример 5: `CloseZeroAccounts`

**Источник:** `Mac/DLNG/DEPO/dpcloseacc.mac`  
**Тип:** `macro`  
**Размер:** 28 строк

```rsl
macro CloseZeroAccounts()
  var acc = TRecHandler("account");
  var fin = TRecHandler("fininstr");
  var query, DataSet, cmd;
  var CntPrep = 0, CntOpen = 0, CntDraft = 0, CntGlob = 0;
  var mesState = "", mesOpKind = "", mess = "";
  var BegDate = date(0,0,0), EndDate = date(0,0,0);
  var ZeroAccDays:integer = null, ZeroAccCalend:bool = null;
  var count = 0, i = 0;
  var err = 0;
  var NeedCloseAcc = true;
  var NeedCloseCertFI = true;
  var FIID = null;
  var IsAO = null;
  
  var Form = CloseAcc_Panel();

  //Если процедура запущена в безынтерфейсном режиме, запрос пользователю не выдаётся, выполняется переход к следующему этапу процедуры
  if( (GetDialogFlag()) and (not IsShedulerRunning()) )
    //2.1.    Выполняется поиск отложенных или открытых поручений на инвентарные операции, глобальных операций "Депозитария",
    //в которых дата валютирования (т.е. дата формирования проводок по лицевым счетам депо) меньше или равна дате запуска процедуры
    if(Form.Run())
       OperDate = Form.GetFieldValue(PNFLD_CLOSEACC_DATE);
       FIID = Form.GetFieldValue(PNFLD_CLOSEACC_FIID);
       ZeroAccDays = Form.GetFieldValue(PNFLD_CLOSEACC_ZERODAYS);
       ZeroAccCalend = Form.GetFieldValue(PNFLD_CLOSEACC_CALENDAR);
       IsAO = (Form.GetFieldValue(PNFLD_CLOSEACC_ISAO) == SET_CHAR);
    end;
```

---

## Пример 6: `AmountReserveRevaluation`

**Источник:** `Mac/Cb/res_lib.mac`  
**Тип:** `macro`  
**Размер:** 46 строк

```rsl
macro AmountReserveRevaluation(objPrimDoc, DateReserve : date, LastDateCalcReserveLoss : date)
  var RestReserveAccount = $0;
  var RestPrev, Code_Currency;
  var RestNew, RestPrevCurr;
  var ReserveAccount;

  if (GenClassName(objPrimDoc) == "ACCOUNTPRIMDOC")
    var acc = objPrimDoc.GetAccountRec();
    //var LastDateCalcReserveLoss = GetAccLastDateCalcReserveLoss(MakeAccountIDEx(acc));

    ReserveAccount = objPrimDoc.FindAccount(ReserveCatCode, LastDateCalcReserveLoss);
    RestPrev = GetAbsAccRestRate(ReserveAccount, LastDateCalcReserveLoss, LastDateCalcReserveLoss, BalanceChapter, NATCUR);
    RestPrevCurr = RestPrev;

    ConvSum(RestPrevCurr, RestPrevCurr, LastDateCalcReserveLoss, NATCUR, acc.Code_Currency);

    RestNew = RestPrevCurr;
    ConvSum(RestNew, RestNew, DateReserve, acc.Code_Currency, NATCUR);
    RestReserveAccount = RestNew - RestPrev;
    /* Остаток на счете резерва */
    /*var PrevRestReserve = GetAbsAccRestRateAccID(acc.accountID, LastDateCalcReserveLoss, LastDateCalcReserveLoss);
    var RestReserve = GetAbsAccRestRateAccID(acc.accountID, DateReserve, DateReserve);

    RestReserveAccount = RestReserve - PrevRestReserve;
    ConvSum(RestReserveAccount, RestReserveAccount, LastDateCalcReserveLoss, NATCUR, acc.Code_Currency);*/
  elif (GenClassName(objPrimDoc) == "ACCCASEPRIMDOC")

    ReserveAccount =objPrimDoc.FindAccount( ReserveCatCode, LastDateCalcReserveLoss );
    objPrimDoc.GetCaseAccountsRest(LastDateCalcReserveLoss, @Code_Currency);

    /*var params = makeArray(SQLParam("acc", ReserveAccount)
                      ,SQLParam("cur", Code_Currency)
                      );
    var rs = execSQLselect("select t_accountid from daccount_dbt where t_chapter = 1 and t_account = :acc and t_code_currency = :cur", params, true);
    rs.moveNext();*/

    RestPrev = GetAbsAccRest( ReserveAccount, DateReserve, 1 );
    //RestPrev = objPrimDoc.GetCaseAccountsRest(LastDateCalcReserveLoss, @Code_Currency);
    RestPrevCurr = RestPrev;

    ConvSum(RestPrevCurr, RestPrevCurr, LastDateCalcReserveLoss, NATCUR, Code_Currency);

    RestNew = RestPrevCurr;
    ConvSum(RestNew, RestNew, DateReserve, Code_Currency, NATCUR);
    RestReserveAccount = RestNew - RestPrev;
  end;
```

---

## Пример 7: `ExecuteStep`

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

## Пример 8: `PrepMassExecuteStep`

**Источник:** `Mac/DLNG/DV/dvop020.mac`  
**Тип:** `macro`  
**Размер:** 35 строк

```rsl
macro PrepMassExecuteStep()
   var doc;
   var FI = TRecHandler( "fininstr.dbt");
   var turn:variant;
   var FD_Oper:DVFirstDocOper, FD_Pos:DVFirstDocPos, FD_Deal:DVFirstDocDeal;
   var Query:string = "", Data:variant;
   var PaydMargin:money = $0, ReceivedMargin:money = $0, PrevFairValue:money = $0;
   var v_Netto:money = $0;
   var DataSet, cmd;
   var Bonus:money = 0, PaidBonus:money = 0, ReceivedBonus:money = 0, SumTax = $0, ST = $0;
   var q, ds;
   var stat = 0;
   var prevClient      = -1;
   var prevClientContr = 0; 
   var prevFIID        = -1;
   var prevParentFI    = -1;
   var prevBaseFiKind  = -1, prevAvoirKind = -1;
   var alreadyPayed = false;
   var Count = 0;

   Query =   " SELECT to_number(oper.t_DocumentID) DocID, oprtemp.t_ID_Operation, oprtemp.t_ID_Step " +
             "   FROM doprtemp_view oprtemp, doproper_dbt oper " +
             "    WHERE oper.t_ID_Operation = oprtemp.t_ID_Operation " + 
             "      AND oprtemp.t_DocKind = " + DL_DVOPER;

   cmd = DL_RSDCommand(Query); 
   DataSet = cmd.Execute();
   if(DataSet.moveNext())
      ID_Operation = DataSet.ID_Operation;
      ID_Step = DataSet.ID_Step;
      oper.id = DataSet.DocID;
      getEq(oper);
   else
      return ExitStep();
   end;
```

---

## Пример 9: `GetPtsvdpList1`

**Источник:** `Mac/Cb/ws_getparty.mac`  
**Тип:** `macro`  
**Размер:** 32 строк

```rsl
macro GetPtsvdpList1(PartyID : integer)

  var Arr = TArray;

  // var query = " select dp.t_name as filial, p.t_name as name " +
              // "  from dptsvdp_dbt pt, ddp_dep_dbt dp, dparty_dbt p " +
              // " where     pt.t_partyid = " + string(PartyID) +
              // "      and pt.t_partykind = 1 " +
              // "      and pt.t_department = dp.t_code " +
              // "      and dp.t_partyid = p.t_partyid ";

  var query = " SELECT dp.t_name AS filial, p.t_name AS name, pt.t_department AS department"
              " FROM dptsvdp_dbt pt "
              "       JOIN ddp_dep_dbt dp "
              "          ON pt.t_department = dp.t_code "
              "       JOIN dparty_dbt p "
              "          ON dp.t_partyid = p.t_partyid "
              " WHERE pt.t_partyid = " + string(PartyID) + " AND pt.t_partykind = 1";

  var ds = TRsbDataSet(query, RSDVAL_CLIENT, RSDVAL_STATIC);

  while (ds.MoveNext())

    var p = TWSFilName();

    p.filial      = ds.filial;
    p.name        = ds.name;
    p.department  = ds.department;

    Arr[Arr.size] = p;

  end;
```

---

## Пример 10: `ВыполнитьПеревод`

**Источник:** `Mac/DLNG/SECUR/mvcb30.mac`  
**Тип:** `private macro`  
**Размер:** 38 строк

```rsl
PRIVATE MACRO ВыполнитьПеревод(FD, d, comm, opid)
  var RestBonusSum = $0, CarrySum = $0, NKDSum = $0, InterestIncomeSum = $0, DiscountIncomeSum = $0, OverAmountSum = $0, CorrSum = $0;
  var BegBonusSumOld = $0, BegBonusSumNew = $0, ReservSum = $0, IncomeReservSum = $0, CorrEstReserv = $0;
  var OldBalanceCostSum = $0, NewBalanceCostSum = $0, CostBuyNatSum = $0;
  var WrtOverAmountSum = $0;
  var CarryBonus = $0;
  var DataSet, query, cmd;
  var Rest = $0;
  var accReservOld = TRecHandler("account.dbt");
  var accReservNew = TRecHandler("account.dbt");
  var accOverOld = TRecHandler("account.dbt");
  var accCorrOld = TRecHandler("account.dbt");
  var accCorrNew = TRecHandler("account.dbt");
  var accOld     = TRecHandler("account.dbt");
  var CatOverOldAcc = "", CatOverNewAcc = "", CatCode = "";
  var FiRole;
  var SaleID = 0;
  var FD_Deal = NULL;
  
  query =   " select t_SumID "
          + "   from dpmwrtsum_dbt "
          + "  where t_DocKind = ? "
          + "    and t_DocID = ? "
          + "    and t_Buy_Sale = " + PM_WRITEOFF_SUM_SALE
          + "    and t_PartNum = 0 ";

  cmd = DL_RSDCommand(query);
  
  cmd.AddParam(comm.DocKind); 
  cmd.AddParam(comm.DocumentID);

  DataSet = cmd.Execute();

  if( DataSet.moveNext() )
     SaleID = DataSet.SumID;
  else
     SaleID = 0; //Такое может быть, если есть только лоты БПП - по списание не проводится, а меняются сами лоты
  end;
```

---

## Пример 11: `Draw`

**Источник:** `Mac/Mbr/mnspraccinf.mac`  
**Тип:** `macro`  
**Размер:** 54 строк

```rsl
macro Draw( DecisionID : integer )

  var facc    :TBFile = TBFile("account.dbt");
  var fdep    :TBFile = TBFile("dp_dep.dbt");
  var fpt     :TBFile = TBFile("party.dbt");
  var fps     :TBFile = TBFile("persn.dbt");
  Array Text, Buttons;
  Buttons( 0 ) = "Да";
  Buttons( 1 ) = "Нет";
  var ErrMsg = "Не найден(ы) счет(а) ";
  var ErrAcc = TArray(), i = 0;   // не найденные счета
  Счет = TArray();                // обнулим массив счетов для массовой печати
  var bankparams:TArray = NULL;

  file adrFNS(adress);
  var select = "select rgd.t_Date as DocDate, rgd.t_Number as DocNum, rgd.t_DeliveryDate as RestDate, rgd.t_RecipientID as BankID, "+
                      "rgd.t_OriginatorName as NoName, rgd.t_OriginatorID as NoID, lnk.t_Account as Account, lnk.t_FIID as FIID, "+
                      "lnk.t_Chapter as Chapter, "+
                      "case when lnk.t_LnkObjectType = 455 then acclaim.t_Priority else 3 end as ClaimPriority, "+
                      "case when lnk.t_LnkObjectType = 455 then acclaim.t_ClaimID  else 0 end as ClaimID "+
                 "from dwlregdec_dbt rgd, dwlacclnk_dbt lnk, dacclaim_dbt acclaim "+
                "where rgd.t_DecisionID         = ? "+
                  "and lnk.t_ObjectID           = rgd.t_DecisionID "+
                  "and lnk.t_ObjectType         = 519 "+
                  "and acclaim.t_ClaimID(+)     = lnk.t_LnkObjectID ";

  var params = makeArray( SQLParam( "ID", DecisionID ) );
  var rs = execSQLselect( select, params, FALSE );
  var INNnp = IfThenElse( wlregdec.ClientKPP == "", wlregdec.ClientINN, wlregdec.ClientINN + "/" + wlregdec.ClientKPP );

  while( rs.moveNext() )
    facc.KeyNum = 0;
    facc.rec.Account        = rs.value( "Account"  );
    facc.rec.Chapter        = rs.value( "Chapter"  );
    facc.rec.Code_Currency  = rs.value( "FIID"     );
    if( facc.GetEQ() and ( facc.rec.Open_Close == "" ) ) /* счет должен быть в нашем филиале и открыт */
      var INN = getPartyINN( facc.rec.Client , 1);
      if( INN == INNnp )                                 /* владельцем счета является клиент, реквизиты которого заданы в сообщении */
        fps.rec.PersonID = fpt.rec.PartyID = ПолучитьКодСубъекта( INN, PTCK_INN );
        if( (( fpt.GetEQ() ) and ( fpt.rec.LegalForm == PTLEGF_INST  ) and (wlregdec.ClientName == fpt.rec.Name)) or
            (( fps.GetEQ() ) and ( fpt.rec.LegalForm == PTLEGF_PERSN ) and (wlregdec.ClientName == fps.rec.Name1 + "," + fps.rec.Name2 + "," + fps.rec.Name3)) )
          fdep.keyNum = 0;
          fdep.rec.Code = facc.rec.Department;
          if( fdep.GetEQ() ) 
            bankparams = makeArray( SQLParam( "p_PartyID"    , fdep.rec.PartyID     ),
                                    SQLParam( "p_CodeKind"   , PTCK_BIC             ),
                                    SQLParam( "p_Code"       , V_STRING , RSDBP_OUT ),
                                    SQLParam( "p_CodeOwnerID", V_INTEGER, RSDBP_OUT ) );  
            execStoredFunc( "RSBPARTY.PT_GetPartyCodeEx", V_INTEGER, bankparams );
            if( bankparams.value(3).value == rs.value( "BankID" ) )
              Счет( Счет.Size() ) = TRecHandler("account");
              Copy( Счет( Счет.Size() - 1 ), facc );
              RepBankID  = bankparams.value(3).value;
            end;
```

---

## Пример 12: `GetInfoByCells`

**Источник:** `Mac/CELLS/penalrepcell.mac`  
**Тип:** `macro`  
**Размер:** 51 строк

```rsl
Macro GetInfoByCells( ReportDate )

   var sql_str = "";
   var sql_cmd;
   var sql_rst;

   var opendate    = date(00,00,0000);
   var prolongdate = date(00,00,0000);
   var enddate     = date(00,00,0000);
   var nulldate    = date(00,00,0000);

   var result_str  = ""; /* Результирующая строка по клиентам*/
   var StatName    = 1 ; /* Занятая ячейка */

   SQL_STR = SQL_STR + "SELECT   df.t_safenumber, dc.t_cellnumber, dct.t_name, dcnt.t_contractid, ";
   SQL_STR = SQL_STR + "         dcnt.t_opendate, dcnt.t_prolongdate, dcnt.t_enddate ";
   SQL_STR = SQL_STR + "    FROM dds_cell_dbt dc, ";
   SQL_STR = SQL_STR + "         dds_cellt_dbt dct, ";
   SQL_STR = SQL_STR + "         dds_contr_dbt dcnt, ";
   SQL_STR = SQL_STR + "         ddscn_cel_dbt cnc, ";
   SQL_STR = SQL_STR + "         dds_safe_dbt df ";
   SQL_STR = SQL_STR + "   WHERE dc.t_state  = " + string(StatName);
   SQL_STR = SQL_STR + "     AND dc.t_branch = " + string(NumFnCash());
   SQL_STR = SQL_STR + "     AND dc.t_celltypeid = dct.t_celltypeid ";
   SQL_STR = SQL_STR + "     AND dc.t_branch = dcnt.t_branch ";
   SQL_STR = SQL_STR + "     AND dc.t_safeid = cnc.t_safeid ";
   SQL_STR = SQL_STR + "     AND dc.t_cellnumber = cnc.t_cellnumber ";
   SQL_STR = SQL_STR + "     AND cnc.t_branch = dcnt.t_branch ";
   SQL_STR = SQL_STR + "     AND cnc.t_contractID = dcnt.t_contractid ";
   SQL_STR = SQL_STR + "     AND dcnt.T_ISCLOSED != 'З' ";
   SQL_STR = SQL_STR + "     AND dcnt.t_enddate <"+sqlDateToStr(ReportDate);
   SQL_STR = SQL_STR + "     AND df.t_branch = dc.t_branch ";
   SQL_STR = SQL_STR + "     AND df.t_safeid = dc.t_safeid ";
   SQL_STR = SQL_STR + "ORDER BY dc.t_branch, dc.t_safeid, dc.t_celltypeid, dc.t_cellnumber ";

   sql_cmd = RsdCommand( SQL_STR );
   sql_rst = RsdRecordSet( sql_cmd );

   /* Открытие шаблона для формирования отчета */
   If( ObjTempl.OpenTemplate(NameTemplateXLS, false ))
      /* заполнение именованных полей */
      ObjTempl.SetValue_NameCell("DateReport", ReportDate );  
      /* Зарегистрируем таблицу, указав диапазон строки таблицы */
      Table = ObjTempl.RegisterTable("TableLoad");
      bPos  = Table.bRowTable;

      While ( sql_rst.movenext )
         If( GetInfoByClient( sql_rst.value("t_contractid"), result_str ) )
            opendate    = SQL_ConvTypeDate( sql_rst.value("t_opendate" ));
            prolongdate = SQL_ConvTypeDate( sql_rst.value("t_prolongdate" ));
            enddate     = SQL_ConvTypeDate( sql_rst.value("t_enddate" ));
```

---

## Пример 13: `СчитатьПолеИзБуфера`

**Источник:** `Mac/Mbr/swsbin.mac`  
**Тип:** `macro`  
**Размер:** 24 строк

```rsl
macro СчитатьПолеИзБуфера(РелизФормы, КодПоля, строка)
  var позиция, error, TpFieldID, ЧислоСтрок; 
  
  /* Получаем код поля (все между ':') */
  КодПоля = SubString(строка, 2, index(SubString(строка, 2), КодРазделительНомера)-1);
  /* Возвращаем код поля */
  SetParm(1, КодПоля);

  /* определяем ID поля, а заодно и максимальное число строк поля */
  ЧислоСтрок = ЧислоСтрокПоля(КодПоля, TpFieldID); 
  if (ЧислоСтрок == 0) return 2; end;

  /* проверяем наличие поля релиза в текущем контексте */ 
  if( not RlsContext.SetContext( TpFieldID, "", "", error ) ) return 2; end;

  /* Отбрасываем код начала поля */
  строка = SubString(строка, 2);
  /* отбрасываем маркеры поля */
  позиция = index(строка, КодРазделительНомера) + 1;
  if (позиция <= 1)  return 4; end;
  СтрокиПоля(0) = SubStr(строка, позиция);

  return 0;
end;
```

---

## Пример 14: `GetRatesDFS`

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

## Пример 15: `GenPmSwiftMxPacs002`

**Источник:** `Mac/Mbr/swmxPacs2_GenProc.mac`  
**Тип:** `private macro`  
**Размер:** 34 строк

```rsl
private macro GenPmSwiftMxPacs002
( rs : RsdRecordset, 
  DepList : string, // заполняется при вызове из планировщика
  FromSheduler : bool, // заполняется при вызове из планировщика
  PaymentID : integer, // заполняется при вызове из макроса шага операции
  ID_Operation : integer, // заполняется при вызове на шаге операции
  ID_Step : integer // заполняется при вызове на шаге операции
) :TArray

  var PrcRecs : TArray = TArray();

  while(rs.moveNext())
    var RhWlextst : TRecHandler = TRecHandler("wlextst.dbt");
    CopyRSetToFBuff(RhWlextst, rs);

    var ErrMsg : string = "";
    var PaymentObj : RsbPayment = RsbPayment(RhWlextst.rec.PaymentID);

    // Генерим pacs.002 и устанавливаем 
    // wlextst.ObjectID = wlinfo.InfoID, wlextst.ObjectType = OBJTYPE_WLD_INFO
    // (через класс платежа).
    GenNotifyAndUpdatePayment(RhWlextst, @ErrMsg, ID_Operation, ID_Step);

    if( FromSheduler and not ID_Operation and not ID_Step and not ErrMsg and
        (RhWlextst.rec.State == WLPM_EXECNOTIFY_RJCT)
      )
      // Если платеж находится на шаге операции "Обработка отвергнутого" (символ шага "J"), 
      // запустить шаг на выполнение с параметром $(завершить)
      var StepSymbol : string = "J"; //PM_OPR_SYMB_PROCESSREJECT
      if( Opr_IsStepExecuteSymb(PaymentObj.PaymentID, PaymentObj.DocKind, StepSymbol, "R") )           
        PM_SetRejectProcessKind(PM_REJECT_PROCKIND_FINISH);
        PM_ExecuteOperation(PaymentObj.PaymentID, PaymentObj.DocKind);// здесь ошибку не анализируем, т.к. ее не требуется по проекту выводить в отчет
        PM_SetRejectProcessKind(PM_REJECT_PROCKIND_NONE);
      end;
```

---

