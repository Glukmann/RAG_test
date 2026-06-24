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

## Пример 16: `sendFNSPercentCorrectRequest`

**Источник:** `Mac/DEPOSITR/FnsPercentServices.mac`
**Тип:** `macro`
**Размер:** 38 строк

```rsl
macro sendFNSPercentCorrectRequest( reqInfo ) : PRCSendPrimaryRequestResponseType
    var response : PRCSendPrimaryRequestResponseType;
    var ResponseHeader : PrcRequestHeaderType;
    ResponseHeader.ReqID = reqInfo.RequestHeader.ReqID;
    ResponseHeader.SenderID = sendID;
    response.ResponseHeader = ResponseHeader;

    var resultPercentCount = findPercentInfoCount(reqInfo.RequestData.Period, 1);

    if (not resultPercentCount.moveNext())
        var ResponseSenderData : FnsPercentResponseSenderDataType;
        var ObjectError : PRCObjectErrorType;
        ObjectError.ErrorCode = "PRC000003";
        ObjectError.ErrorText = "Перечень данных для корректировки пуст";
        ResponseSenderData.ObjectError = ObjectError;
        response.ResponseSenderData = ResponseSenderData;
    else
        var ResponseServiceData : FnsPercentResponseServiceDataType;
        if (resultPercentCount.value("t_responseID") == StrFor(1))
            ResponseServiceData.ResponseID = SubStr(CreateGUID(), 2, 36);
        else
            ResponseServiceData.ResponseID = resultPercentCount.value("t_responseID");
        end;

        ResponseServiceData.PercentCount = Int(resultPercentCount.value("percentCount"));
        ResponseServiceData.Period = reqInfo.RequestData.Period;
        ResponseServiceData.NOCode = reqInfo.RequestData.NOCode;
        response.ResponseServiceData = ResponseServiceData;

        if (resultPercentCount.value("t_responseID") == StrFor(1))
            updatePercentInfo(ResponseServiceData, 1);
            deleteFromFLC(ResponseServiceData, 1);
            deleteFromPCCorrect(ResponseServiceData);
        end;
    end;

    return response;
end;
```

---

## Пример 17: `GetInfoByCells`

**Источник:** `Mac/CELLS/freeclrep.mac`
**Тип:** `macro`
**Размер:** 124 строк

```rsl
Macro GetInfoByCells()

   var sql_str = "";
   var sql_cmd;
   var sql_rst;

   var opendate    = date(00,00,0000);
   var prolongdate = date(00,00,0000);
   var enddate     = date(00,00,0000);
   var nulldate    = date(00,00,0000);

   var result_str        = ""; /* Результирующая строка по клиентам*/
   var result_str_trust  = ""; /* Результирующая строка по клиентам*/

   var StatNameFree = 0 ; /* Свободная ячейка */
   var StatNameDuty = 1 ; /* Занятая ячейка */
   var StatNameBron = 2 ; /* Забронированная ячейка */

   var  CellNameFree = "СВОБОДНА",
        CellNameDuty = "ЗАНЯТА",     
        CellNameBrok = "НЕИСПРАВНА",       
        CellName     = ""; 

   /* Общее количество несиправных ячеек */
   var OverBrokenCells = 0;

   var counter = 1; /* индикатор возрастания */
                   
   SQL_STR = " SELECT   df.t_safenumber, dc.t_cellnumber, dc.T_RESERVEDFOR,   dct.t_name, nvl(dcnt.t_contractid,0) AS t_contractid, dc.t_state,";
   SQL_STR = SQL_STR + "         dcnt.t_opendate, dcnt.t_prolongdate, dcnt.t_enddate ";
   SQL_STR = SQL_STR + "    FROM dds_cellt_dbt dct, dds_cell_dbt dc LEFT JOIN dds_contr_dbt dcnt ";
   SQL_STR = SQL_STR + "         ON dc.t_branch = dcnt.t_branch ";
   SQL_STR = SQL_STR + "       AND dc.t_safeid = dcnt.t_safeid ";
   SQL_STR = SQL_STR + "       AND dc.t_cellnumber = dcnt.t_cellnumber ";
   SQL_STR = SQL_STR + "       AND ( dcnt.t_closedate = TO_DATE ('01.01.0001', 'dd.mm.yyyy') OR  dcnt.t_closedate > "+sqlDateToStr({curdate})+" ) ";
   SQL_STR = SQL_STR + "         , ";
   SQL_STR = SQL_STR + "         dds_safe_dbt df ";
   SQL_STR = SQL_STR + "   WHERE dc.t_branch =  "+ string(NumFnCash());
   SQL_STR = SQL_STR + "     AND (dc.t_state = " + StatNameFree + " OR dc.t_state = "+StatNameDuty + " OR dc.t_state = "+ StatNameBron+" ) ";
   SQL_STR = SQL_STR + "     AND dc.t_celltypeid = dct.t_celltypeid ";
   SQL_STR = SQL_STR + "     AND df.t_branch = dc.t_branch ";
   SQL_STR = SQL_STR + "     AND df.t_safeid = dc.t_safeid ";
   SQL_STR = SQL_STR + "ORDER BY dc.t_branch, dc.t_safeid, dc.t_celltypeid, dc.t_cellnumber ";

   sql_cmd = RsdCommand( SQL_STR );
   sql_rst = RsdRecordSet( sql_cmd );

   /* Открытие шаблона для формирования отчета */
   If( ObjTempl.OpenTemplate(NameTemplateXLS, false ))
      /* заполнение именованных полей */
      ObjTempl.SetValue_NameCell("DateReport", GetCurDate() );  
      ObjTempl.SetValue_NameCell("NameFnCash", doGetBranchName());
      /* Зарегистрируем таблицу, указав диапазон строки таблицы */
      Table = ObjTempl.RegisterTable("TableReport");
      bPos  = Table.bRowTable;

      While ( sql_rst.movenext )
         Message(" Формирование отчета по арендованным ячейкам, обработано ... " , counter );         

         opendate    = SQL_ConvTypeDate( sql_rst.value("t_opendate" ));
         prolongdate = SQL_ConvTypeDate( sql_rst.value("t_prolongdate" ));
         enddate     = SQL_ConvTypeDate( sql_rst.value("t_enddate" ));

         /* если по договору было продления срока, то дату начала будет датой пролонгации */ 
         If( prolongdate > opendate )
            opendate = prolongdate;
         end;

         /* Определение типа ячейки */
         If( sql_rst.value("t_state")  == 0 )
            CellName = CellNameFree; 
         elif( (sql_rst.value("t_state") > 0 ) AND (sql_rst.value("T_RESERVEDFOR") != -1 ))
            CellName = CellNameDuty;     
         elif( (sql_rst.value("t_state") == 1) AND( sql_rst.value("T_RESERVEDFOR") == -1 )) /* Ярмольчук. Если не занята, то неисправна. (обходим ситуацию, когда операция вкрытия сторнировалась) */
            CellName = CellNameDuty;     
         elif( (sql_rst.value("t_state") > 0 ) AND( sql_rst.value("T_RESERVEDFOR") == -1 )) 
            CellName = CellNameBrok;     
            OverBrokenCells =OverBrokenCells + 1;
         end;

         /* Заполняем строку таблицы данными */
         Table.SetValueCell("Cell1" , string(counter));
         Table.SetValueCell("Cell2" , string(sql_rst.value("t_name") ) ); 
         Table.SetValueCell("Cell3" , string(CellName));
         Table.SetValueCell("Cell4" , string(sql_rst.value("t_safenumber") ) );
         Table.SetValueCell("Cell5" , string(sql_rst.value("t_cellnumber") ) );

         /*Определение владельцев договора */
         If( sql_rst.value("t_contractid") > 0 )
            GetInfoByClient( sql_rst.value("t_contractid"), result_str ); 
         else
            result_str = "";
         end;
         Table.SetValueCell("Cell6" , string(result_str));

         Table.SetValueCell("Cell7" , string(opendate ));
         Table.SetValueCell("Cell8" , string(enddate )); 

         /* определение доверенных лиц договора */
         If( sql_rst.value("t_contractid") > 0 )
            GetClientTrust( sql_rst.value("t_contractid"), result_str_trust );
         else
            result_str_trust = "";
         end;
         Table.SetValueCell("Cell9" , string( result_str_trust )); 

         Table.AddStr(); 

         counter = counter + 1;
      end;
      /* Формируем итоги */
      ObjTempl.SetValue_NameCell("OverAllCells", GetOverAllCells() );  
      ObjTempl.SetValue_NameCell("BusyCells"   , GetBusyCells()    );
      ObjTempl.SetValue_NameCell("FreeCells"   , GetFreeCells()    );  
      ObjTempl.SetValue_NameCell("BrokenCells" , OverBrokenCells   );

      Table.EndTable(); 
      ObjTempl.SaveAsTemplate(NameReportXLS);
      PrintLn(" Отчет - ",NameReportXLS," сформирован, для печати формы, переключитесь в окно Excel !!! " );
   else
      MsgBox(" Ошибка открытия формы шаблона: ", NameTemplateXLS );   
      Exit(1);
   end;
End;
```

---

## Пример 18: `WebCore_CB_GetRegParm`

**Источник:** `Mac/Cb/ws_notes.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro WebCore_CB_GetRegParm ():WebResponseBuilder

  ResponseBuilder = WebResponseBuilder();

  var ErrorMessage : WsErrorMessage = WsErrorMessage();
  
  var err=0;
  
  var ProcValue;
  
  GetRegistryValue( "BANK_INI/ОБЩИЕ ПАРАМЕТРЫ/ДОСТУП/ИСТОРИЯ ЗНАЧЕНИЙ ПРИМЕЧАНИЙ", V_BOOL, ProcValue, err);

  if(err == 0)
    
    responseBuilder.SetUserObject( ProcValue);
	 
  else

    responseBuilder.SetUserObject( false);
	
  end;
```

---

## Пример 19: `КОРРЕСП_ГЛАВА_Г`

**Источник:** `Mac/DLNG/dlreport.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
MACRO КОРРЕСП_ГЛАВА_Г():BOOL
  VAR ErrCode = 0;
  VAR RetVal:bool = true;
  GetRegistryValue( "COMMON\\КОРРЕСП_ГЛАВА_Г", V_BOOL, RetVal, ErrCode );
  if( ErrCode != 0 )
     RetVal = true;
  end;
```

---

## Пример 20: `Run`

**Источник:** `Mac/DLNG/SECUR/TaxAccSecur_Form.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
  macro Run()
    var stat = Run();

    RepParams.Period       = GetFieldValue(PNFLD_TAXACCSECUR_PERIOD);
    RepParams.Year         = GetFieldValue(PNFLD_TAXACCSECUR_YEAR);
    RepParams.Growth       = GetFieldValue(PNFLD_TAXACCSECUR_Growth);
    RepParams.BegDate      = GetFieldValue(PNFLD_TAXACCSECUR_BEGDATE);
    RepParams.EndDate      = GetFieldValue(PNFLD_TAXACCSECUR_ENDDATE);
    RepParams.SubKind      = GetFieldValue(PNFLD_TAXACCSECUR_SUBKIND);
    RepParams.Print_NUNP = RepParams.Print_NUSVOD = RepParams.Print_NUMSFO = false;
    if( RepParams.SubKind == SC_NUNP )
      RepParams.Print_NUNP = true;
    elif( RepParams.SubKind == SC_NUNSVOD )
      RepParams.Print_NUNP = true;/*нужен для свода*/
      RepParams.Print_NUSVOD = true;
    elif( RepParams.SubKind == SC_NUMSFO )
      RepParams.Print_NUNP = true;/*нужен для свода*/
      RepParams.Print_NUSVOD = true;
      RepParams.Print_NUMSFO = true;
    end;

    return stat;
  end;
```

---

## Пример 21: `SendEmail`

**Источник:** `Mac/Cb/QueueWSLib.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro SendEmail(title, content)
    var EmailList;
    GetRegistryValue("COMMON\\QUEUE\\E-MAIL", V_STRING, EmailList);

    AddNotifyToDbt(title, content, EmailList);
    SendNotyfyToEmail(false, false);
end;
```

---

## Пример 22: `DL_GetValueName`

**Источник:** `Mac/DLNG/dldlngfun.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
macro DL_GetValueName( List, Element, Name )
   var ll = TRecHandler("llvalues.dbt");
   if( LL_FindLLVALUES( List, Element, ll ) == true )
      SetParm( 2, ll.rec.Name );
      return ll.rec.Code;
   else
      SetParm( 2, "" );
      return "";
   end;
end;
```

---

## Пример 23: `ExecuteCollectionOper`

**Источник:** `Mac/DEPOSITR/collection_oper.mac`
**Тип:** `macro`
**Размер:** 129 строк

```rsl
macro ExecuteCollectionOper( objectType, objectId, param )
    var returnObj = FuncObjResult( FUNCOBJ_RESULT_OK, "", 0 );
    var cmd, rs;
    var trnStat = 0;

    ClearRecord(operParm);
    ClearRecord(ddoc);
    OpenDepFiles();

    cmd = RsdCommand( "  select dep.t_iscur, " +
                      "         dep.t_fncash, " +
                      "         dep.t_referenc, " +
                      "         dep.t_account, " +
                      "         dep.t_code_currency, " +
                      "         dep.t_Type_Account, " +
                      "         dep.t_CodClient, " +
                      "         dep.t_SvodAccount, " +
                      "         ar.t_sum, " + 
                      "         ar.t_Source, " +
                      "         ar.t_Id, " +
                      "         ar.t_GroupRequirement, " +
                      "         ar.t_PaymentID, " + 
                      "         ar.t_Priority, " +
                      "         ar.t_Comment, " +
                      "         ar.t_PenaltyKind " +
                      "  from drt_ArrestParm_dbt ar  " +
                      "       inner join ddepositr_dbt dep " +
                      "                  on ar.t_referenceAcc = dep.t_referenc " +
                      " where ar.t_id = ? ");

    cmd.addParam( "", RSDBP_IN, Int( objectId ) );
    cmd.execute;

    rs = RsdRecordSet( cmd );
    if ( rs.moveNext )
        OpenDepFiles();
        var FlagCur = NumFlagCur;
        var FNCash  = NumFNCash;
        ddoc.IsCur = Int( rs.value("t_iscur") );
        ddoc.FNCash = Int( rs.value("t_fncash") );
        ddoc.RealFNCash = Int( rs.value("t_fncash") );
        ddoc.Referenc = Int( rs.value("t_referenc") );
        ddoc.Account = SQL_ConvTypeStr( rs.value("t_account") );
        ddoc.Code_Currency = Int( rs.value("t_code_currency") );
        ddoc.Type_Account = SQL_ConvTypeStr( rs.value("t_Type_Account") );
        ddoc.CodClient = Int( rs.value("t_CodClient") );
        ddoc.Date_Document = getCurDate( );
        ddoc.DepDate_Document = getCurDate( );
        ddoc.Oper = {oper};
        ddoc.YesSbook = "X";
        ddoc.IsControl = StrFor(1);
        ddoc.InSum = SQL_ConvTypeSum( rs.value("t_sum") );
        ddoc.TypeOper = 98;
        ddoc.ApplType = 0;
        ddoc.TypeComplexOper = ddoc.TypeOper;

        ClearRecord(operParm);
        operParm.Type_Oper       = ddoc.TypeOper;
        operParm.TypeComplexOper = operParm.Type_Oper;
        operParm.Referenc        = ddoc.Referenc;
        operParm.DepDate         = {curdate};
        operParm.Type_Account    = ddoc.Type_Account;
        operParm.IdClaim         = rs.value("t_Id");
        // Если права принадлежат вносителю, то операция должна выполняться от имени вносителя
        if (checkDoesImporterHasRights(rs.value("t_SvodAccount"), rs.value("t_FNCash"), {curdate}) != 0)
            operParm.DocumentAuthor  = 4; // ACCOUNT_IMPORTER
        end;

        setFNCash(rs.value("t_fncash"));
        setFlagCur(rs.value("t_iscur"));

        var restAcc = 0;
        getRestAccForArrest(rs.value("t_Referenc"), 
                            rs.value("t_code_currency"), 
                            rs.value("t_PenaltyKind"), 
                            rs.value("t_Priority"), 
                            false, 
                            restAcc);
        if ( (restAcc > 0) and (restAcc < SQL_ConvTypeSum( rs.value("t_sum") )) )
            ddoc.OutSum = restAcc;
        end;

        trnStat = Выполнение_Операции(operParm, ddoc);

        if (trnStat != 0)
            returnObj.state = FUNCOBJ_RESULT_FATAL;
            if ((trnStat == 1696) or (trnStat == 22448))
                fnsPutInFuncObj(trnStat, Int(rs.value("t_PaymentID")), ddoc.InSum, ddoc.Oper, "0", objectId);
                returnObj.errorText = "Не удалось выполнить 98 операцию";
                returnObj.errorCode = trnStat;
            else
                returnObj.errorText = "Не удалось выполнить 98 операцию";
                returnObj.errorCode = trnStat;
            end;
        else
            var resCode = 4, tmpId = 0;
            // Определим результат выполнения
            var arrChecKCmd = RsdCommand("select t_totalSum from DSB_ARREST_DBT where t_idarrestparm = ? order by t_id DESC");
            arrChecKCmd.addParam( "", RSDBP_IN, Int( objectId ) );
            arrChecKCmd.execute;                    
            var rsArrChecK = RsdRecordSet(arrChecKCmd);
            if (rsArrChecK.moveNext())
                if (rsArrChecK.value("t_totalSum") != 0)
                    resCode = 11;
                end;
            end;

            fnsPutInFuncObj(resCode, Int(rs.value("t_PaymentID")), ddoc.InSum, ddoc.Oper, operParm.ApplicationKey, objectId);

            returnObj.state = FUNCOBJ_RESULT_OK;
            returnObj.errorText = "";
        end;

        CloseDepFiles();
        InterDesk_EndDocBunch();
        setFNCash(FNCash);
        setFlagCur(FlagCur);
    else
        returnObj.state = FUNCOBJ_RESULT_FATAL;
        returnObj.errorText = "Не найдена запись об аресте";
    end;

  return returnObj;

OnError( error )
    returnObj.state = FUNCOBJ_RESULT_FATAL;
    returnObj.errorText = error.Message;
    return returnObj;
end;
```

---

## Пример 24: `ReadDC`

**Источник:** `Mac/Mbr/swsbpars.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro ReadDC(Stream, Count, MacroFill)
  var DKFlag;
  
  if( StrmGetLexeme(Stream, Count, DKFlag, TS_ALPHA, TL_FIXED, 1))
    PrintLog(3, "ReadDC: " + DKFlag);
    SetParm(1, Count); /* запись в 1-й аргумент!*/
    return ExecMacro2(MacroFill, DKFlag);
  end;
```

---

## Пример 25: `WriteCommonPart`

**Источник:** `Mac/Mbr/uf108taxgm.mac`
**Тип:** `macro`
**Размер:** 26 строк

```rsl
  macro WriteCommonPart(xml : object, mes : object)
    if( MustWriteTaxInfo() )
      var elem : object = xml.createElement("DepartmentalInfo");

      if(CommonTaxAuthorState)
        elem.setAttribute("DrawerStatus", CommonTaxAuthorState);
      end;

      if(not CommonBTTTICode)
        CommonBTTTICode = "0";
      end;
      elem.setAttribute("CBC", CommonBTTTICode );

      if(CommonOKATOCode)
        elem.setAttribute("OKATO", CommonOKATOCode );
      end;

      elem.setAttribute("PaytReason",   "0" );
      elem.setAttribute("TaxPeriod",    "0" );
      elem.setAttribute("DocNo",        "0" );
      elem.setAttribute("DocDate",      "0" );
      elem.appendChild(xml.createTextNode(""));

      mes.appendChild(elem);
    end;
  end;
```

---

## Пример 26: `FindClientByID`

**Источник:** `Mac/Cb/pr_mocur.mac`
**Тип:** `macro`
**Размер:** 32 строк

```rsl
macro FindClientByID(PartyID, INN, Address)

record PtAdress ( adress );

var cINN;

   SetParm(1,"");
   SetParm(2,"");

   ClearRecord(PtAdress);

   if ( PartyID < 0 )
      return false;
   end;

   cINN = GetPartyINN( PartyID, 1 ); /* Длиннный ИНН */
   SetParm(1,cINN);

   party.PartyID = PartyID;
   if ( GetEQ(party) )
      НайтиЮридическийАдресСубъекта(party.PartyID,PtAdress);
      country.CodeLat3 = PtAdress.Country;
      if ( GetEq(country) )
         SetParm(2, MakeAddress());
      else
         SetParm(2, MakeAddressWithoutCountry());
      end;
   else
      return false;
   end;
   return true;
end;
```

---

## Пример 27: `FillOurParm`

**Источник:** `Mac/Cb/pr_mocur.mac`
**Тип:** `macro`
**Размер:** 25 строк

```rsl
macro FillOurParm(Name, Address, Code, Acc)

   record PtAdress ( adress );
   ClearRecord(PtAdress);

   SetParm(0,"");
   SetParm(1,"");
   SetParm(2,"");
   SetParm(3,"");

   SetParm(0,{Name_Bank});
   SetParm(2,{MFO_Bank});
   SetParm(3,{CORAC_BANK});
   party.PartyID = {OurBank};
   if ( GetEQ(party) )
      НайтиЮридическийАдресСубъекта(party.PartyID,PtAdress);
      country.CodeLat3 = PtAdress.Country;
      if ( GetEQ(country) )
         SetParm(1,MakeAddress());
      else
         SetParm(1,MakeAddressWithoutCountry());
      end;
   end;

end;
```

---

## Пример 28: `ИспользоватьСводныеПроводки`

**Источник:** `Mac/DLNG/SECUR/sp_carsf.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
MACRO ИспользоватьСводныеПроводки( IsClientAcc:BOOL ):BOOL
   var Enable, ErrCode;

   if( IsClientAcc )
            GetRegistryValue( MAKE_CARRY_SUMMARY_CLNT, V_BOOL, Enable, ErrCode );
         else /*собственные сделки*/
            GetRegistryValue( MAKE_CARRY_SUMMARY, V_BOOL, Enable, ErrCode );
         end;

         if( (ErrCode == 0) AND (Enable != 0) )
            return true;
         end;

   return false;
END;
```

---

## Пример 29: `SelectBranch`

**Источник:** `Mac/CELLS/accrpack.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro SelectBranch( Branch, FlagAll )

  Branch = {DepFNCash};
  FlagAll = false;

  SetParm( 0, Branch );
  SetParm( 1, FlagAll );

end;
```

---

## Пример 30: `GetPartyPropertys`

**Источник:** `Mac/Cb/prpocl.mac`
**Тип:** `macro`
**Размер:** 48 строк

```rsl
macro GetPartyPropertys(PartyID,rec,MFO,CorAc,Place)
file Коды_Субъектов(partcode);
file Параметры_Банков (bankdprt);
file Субъекты (party);

    if ( ПолучитьСубъекта (PartyID,rec) != 0 )
        msgbox("Не найден банк-получатель");
        return 1;
    else
         Коды_Субъектов.PartyID  = rec.PartyID;
         Коды_Субъектов.CodeKind = 3;
         If (GetEQ(Коды_Субъектов)) /* Если есть БИК у самого банка, то возвращаем его */
                SetParm(2, Коды_Субъектов.Code);
                Параметры_Банков.PartyID = rec.PartyID;
                if (GetEQ(Параметры_Банков))
                    SetParm(3, Параметры_Банков.corAcc);
                else
                    SetParm(3, "");
                end;
         else        /* Если нет, берем вышестоящую организацию и ищем ее БИК*/
                if ( ПолучитьСубъекта (rec.Superior,rec) != 0 )
                    SetParm(2, "");
                    SetParm(3, "");
                else
                    Коды_Субъектов.PartyID  = rec.PartyID;
                    Коды_Субъектов.CodeKind = 3;
                    If (GetEQ(Коды_Субъектов))
                        SetParm(2, Коды_Субъектов.Code);
                    else
                        SetParm(2, "");
                    end;
                end;
                Параметры_Банков.PartyID = rec.PartyID;
                if (GetEQ(Параметры_Банков))
                        SetParm(3, Параметры_Банков.corAcc);
                else
                        SetParm(3, "");
                end;
          end;
          Параметры_Банков.PartyID = rec.PartyID;
/*          if (GetEQ(Параметры_Банков))
                  SetParm(4, Параметры_Банков.place + " " + rec.Place );
          else*/
                  SetParm(4, "");
/*          end;*/
    end;

END;
```

---

## Пример 31: `IsSuchShortNameCln`

**Источник:** `Mac/DLNG/DEPO/dpacvl.mac`
**Тип:** `macro`
**Размер:** 45 строк

```rsl
macro IsSuchShortNameCln( DstNumber, ShortName, IsSuchName, UsrID, UsrNumber )
  var stat;
  var bstat;
  var SaveKeyNumber;
  var SavePos;
  var bftext;


  SetParm( 2, FALSE );
  SetParm( 3, 0 );
  SetParm( 4, -1 );
  
  SaveKeyNumber = KeyNum( dpac );
  SavePos = GetPos(dpac);

  if( SavePos )
    stat = FindDEPOACbyShortName( dpac, 0, ShortName );
    if(stat == FALSE)
      bstat = Status();
      if(bstat ==4) /* Записи в пользовательском файле нет */
        stat = TRUE;
      else
        println("Ошибка поиска записи в файле dpac.dbt");
      end;
    else
      /* Запись в пользовательском файле нашли */
      if( dpac.Number != DstNumber ) /* Действительно есть, т.к. не нашего номера */
        SetParm( 2, TRUE );
        SetParm( 3, dpac.ID );
        SetParm( 4, dpac.Number );
      end;
    end;
    if(stat)   
      KeyNum( dpac, SaveKeyNumber );
      stat = GetDirect(dpac, SavePos);
      if(not stat )
        status(bftext);
        println( "Ошибка восстановления позиции в файле depoac.dbt, SavePos ="+SavePos+"\n"+BerrText( bftext ) );
      end;
    end;
  else
    status(bftext);
    println( "Ошибка сохранения позиции в файле depoac.dbt, ID ="+dpac.ID+"\n"+BerrText( bftext ) );
    stat = FALSE;
  end;
```

---

## Пример 32: `PrintReport`

**Источник:** `Mac/Cb/pmmassrep.mac`
**Тип:** `macro`
**Размер:** 44 строк

```rsl
MACRO PrintReport()

  var select :string = "select rm.t_Number, rm.t_Date, db.t_BankCode, pm.t_PayerAccount, cr.t_BankCode, pm.t_ReceiverAccount, "
                              "t.t_ErrorStatus, decode( nvl(t.t_ErrorMessage, CHR(1)), CHR(1), msg.t_Contents, t.t_ErrorMessage ) "
                       "from doprtemp_tmp  t, "
                            "dpmpaym_dbt   pm, "
                            "dpmrmprop_dbt rm, "
                            "dpmprop_dbt   db, "
                            "dpmprop_dbt   cr, "
                            "dbank_msg     msg "
                       "where pm.t_PaymentID = t.t_OrderID "
                         "and rm.t_PaymentID = pm.t_PaymentID "
                         "and db.t_PaymentID = pm.t_PaymentID "
                         "and db.t_DebetCredit = 0 "
                         "and cr.t_PaymentID = pm.t_PaymentID "
                         "and cr.t_DebetCredit = 1 "
                         "and msg.t_Number(+) = t.t_ErrorStatus "
                        "order by pm.t_PaymentID";

    [
        Результаты массовой обработки документов

     ┌─────────┬──────────┬─────────────────┬─────────────────────┬─────────────────┬─────────────────────┬────────────────────────────────────────┐
     │  Номер  │ Дата     │ Банк плательщика│ Счет плательщика    │ Банк получателя │ Счет получателя     │ Результат обработки                    │
     ├─────────┼──────────┼─────────────────┼─────────────────────┼─────────────────┼─────────────────────┼────────────────────────────────────────┤ ];

  var rs:RsdRecordset = execSQLselect( select );
  var result:string = "";
  var total_success:integer = 0, total_error:integer = 0;

  while( rs.moveNext() )
    
    if( not rs.value(6) )
      result = "Успешно обработан";
      total_success = total_success + 1;
    else
      result = string( rs.value(6), " ", rs.value(7) );
      total_error = total_error + 1;
    end;

    [│######## │##########│#################│#####################│#################│#####################│########################################│ ]
    ( rs.value(0):r, date(rs.value(1)):l, rs.value(2):l, rs.value(3):l, rs.value(4):l, rs.value(5):l, result:l:w );

  end;
```

---

## Пример 33: `FSSP_IsPayFmControlEnabled`

**Источник:** `Mac/Cb/fssp_lib.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro FSSP_IsPayFmControlEnabled()
    var flag = false;
    GetRegistryValue("COMMON\\ПАРАМЕТРЫ ПРОЦЕДУР\\ГРУППОВАЯ ОПЛАТА\\ПРОВЕРЯТЬ_ФМ", V_BOOL, flag);
    return flag;
end;
```

---

## Пример 34: `FX_KvitRequirement`

**Источник:** `Mac/DLNG/FOREX/fxpayreq.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
MACRO FX_KvitRequirement(fd)
  var TranModeReq, KvitMode,
      stat = 0, i = 0, paym,
      ReqAccount = "",
      MaxiDate = Date(0,0,0),   
      CurCom, CurReq;

  fd.SetCurrency(CurCom, CurReq);
  GetRegistryValue("КОНВЕРСИОННЫЕ ОПЕРАЦИИ\\ИСПОЛЬЗОВАНИЕ ТС\\ИСПОЛНЕНИЕ ТРЕБОВАНИЙ",
                   V_INTEGER, TranModeReq, stat);
  
  if (not stat)
    GetRegistryValue("КОНВЕРСИОННЫЕ ОПЕРАЦИИ\\РЕЖИМ КВИТОВКИ",
                     V_INTEGER, KvitMode, stat);
  end;
```

---

## Пример 35: `УВ_ПолучитьСуммуДисконтаНаДату`

**Источник:** `Mac/DLNG/VA/vamisc.mac`
**Тип:** `macro`
**Размер:** 43 строк

```rsl
MACRO УВ_ПолучитьСуммуДисконтаНаДату(fd, VDate)
  var bnr = fd.GetBnr();
  var leg = fd.GetLeg();
  var tick = fd.GetTick();
  var P = 0, T = 0;
  var Днач = УВ_ПолучитьСуммуНачальногоДисконта(bnr, leg, VDate);
  var Драсч = $0;
  var DiscKind = 0, err = 0;
  var IncomeDateType = DL_INCOMEDATETYPE_PLUSONE;

  if(Днач > $0)
    T = VS_GetTermCircDate(bnr, leg); // срок обращения векселя (определяется от даты выпуска до плановой даты погашения включительно)

    if(T > 0)
      GetRegistryValue("ДОВЕРИТЕЛЬНОЕ УПРАВЛЕНИЕ\\РАБОТА С НЕЭМИССИОННЫМИ ЦБ\\НАЧИСЛЕНИЕ ДИСКОНТА", V_INTEGER, DiscKind, err);

      if((bnr.rec.BCTermFormula == VS_TERMF_DURING) and (bnr.rec.BackOffice == "А"/*ДУ*/) and (not err) and (not DiscKind)) // по минимальному сроку
        if(bnr.rec.BCPresentationDate > ZeroDate)
          P = VDate - bnr.rec.BCPresentationDate;
        end;
      else
        P = VDate - VS_GetStartDate(bnr, leg);
      end;

      if(P > 0)
        if(bnr.rec.BCTermFormula != VS_TERMF_INATIME)
          if(DL_GetStartIncomeDateType(@IncomeDateType) and (IncomeDateType == DL_INCOMEDATETYPE_CBR))
            P = P + 1; // чтобы учесть дату начала, которая была потеряна при вычитании

            if((tick != null) or (VDate >= DL_GetBnrPlanRepayDate(bnr, leg)))
              P = P - 1; // в дату погашения саму дату погашения учитывать не нужно
            end;
          end;
        end;

        if(P > T)
          P = T;
        end;

        Драсч = Round(Днач * P / T, 2); // нужно до 2-х знаков здесь, в противном случае накапливается ошибка
      end;
    end;
  end;
```

---

## Пример 36: `GetFormFields`

**Источник:** `Mac/DLNG/TRUST/TSCardAnAccRep_Form.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
  MACRO GetFormFields()
     TSCardAnAccRepFormData.ReportDate     = GetFieldValue( PNFLD_CARD_REPORT_DATE      );
     TSCardAnAccRepFormData.OFBU           = GetFieldValue( PNFLD_CARD_OFBU             );
     TSCardAnAccRepFormData.OFBU_Number    = GetFieldValue( PNFLD_CARD_OFBU_NUMBER      );
     TSCardAnAccRepFormData.OFBU_Name      = GetFieldValue( PNFLD_CARD_OFBU_NAME        );
     TSCardAnAccRepFormData.IDDU           = GetFieldValue( PNFLD_CARD_IDDU             );
     TSCardAnAccRepFormData.PrevReportDate = GetFieldValue( PNFLD_CARD_PREV_REPORT_DATE );
     TSCardAnAccRepFormData.Contract       = GetFieldValue( PNFLD_CARD_CONTRACT         );
     TSCardAnAccRepFormData.Trustor        = GetFieldValue( PNFLD_CARD_TRUSTOR          );
  END;
```

---

## Пример 37: `MatchPayment`

**Источник:** `Mac/BOOK/PFRMatchPayment.mac`
**Тип:** `macro`
**Размер:** 28 строк

```rsl
macro MatchPayment( payment )
  CopyRSetToFBuff( recTrnPaym, payment );

  var rdd;
  var stat = FindRDDByPayment( recTrnPaym, rdd );
 
  if( stat )
    var inn, kpp;
    var rddCount = 0;
    // Найденные записи проверить на совпадение ИНН/КПП
    while( stat )
      GetINNKPP( rdd.value("t_PayerPartyId"), rdd.value("t_PayerTempPartyId"), inn, kpp );
      if( (inn == recTrnPaym.rec.PayerINN) and (kpp == recTrnPaym.rec.PayerKPP) )
        rddCount = rddCount + 1;
        DocId = rdd.value("t_documentId");
        DocNumber = SQL_ConvTypeStr(rdd.value("t_documentNumber"));
        DocAmount = rdd.value("t_DebitAmount");
        PaymentId = int(SQL_ConvTypeStr(rdd.value("t_incomePaymentId")));
      end;
      stat = rdd.moveNext();
    end;
    // Установка связи между п/п и входящим РДД
    if( rddCount == 1 )
      stat = ProcessTrn(null, "SetMatchingTRN");
    else
      stat = false;
    end;
  end;
```

---

## Пример 38: `Блок`

**Источник:** `Mac/DLNG/VEKSEL/vsprcexp.mac`
**Тип:** `block`
**Размер:** 10 строк

```rsl
        m_Month = m_Form.GetFieldValue( PNFLD_PRCEXP_MONTH );
        m_Year = m_Form.GetFieldValue( PNFLD_PRCEXP_YEAR );
        m_BeginDate = Date( 1, m_Month, m_Year );
        if( m_Month == 12 )
            m_EndDate = Date( 31, m_Month, m_Year );
        else
            m_EndDate = Date( 1, m_Month + 1, m_Year ) - 1;
        end;
        m_FIID = m_Form.GetFieldValue( PNFLD_PRCEXP_CURCODE );
        m_Department = m_Form.GetFieldValue( PNFLD_PRCEXP_DEPARTCODE );
```

---

## Пример 39: `Блок`

**Источник:** `Mac/DLNG/dlclordco_form.mac`
**Тип:** `block`
**Размер:** 25 строк

```rsl
  if( Cmd == DLG_INIT )
     if( FldRealValue == null )
        FldRealValue = -1;
     end;
     if( FldRealValue <= 0 )
        FldShowValue = STR_ALLVALUE;
        pThis.SetLinkedValue( H_CLIENT_NAME, "");
        SetServKind( pThis, FldRealValue );
     else
        if( not ПолучитьСубъекта( FldRealValue, Party ) )
            FldShowValue = GetPartCode(FldRealValue);
            pThis.SetLinkedValue( H_CLIENT_NAME, Party.rec.ShortName);
            SetServKind( pThis, FldRealValue );
        end;
     end;
  elif( (Cmd == DLG_KEY) AND (Key == KEY_SPACE) )
     FldRealValue = -1;
     FldShowValue = STR_ALLVALUE;
     pThis.SetLinkedValue( H_CLIENT_NAME, "" );
     pThis.SetLinkedValue( H_CONTR, null );
     SetServKind( pThis, FldRealValue );
  elif( (Cmd == DLG_KEY) AND (Key == KEY_F3) )
     if( pThis.GetFieldValue( PNFLD_DLCLORDCO_IsBO ) == "X" )
        ServKind[ServKind.Size] = BO;
     end;
```

---

## Пример 40: `ОнлайнРегистрацияКлиентовНаБирже`

**Источник:** `Mac/DLNG/dlcontrfunc.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro ОнлайнРегистрацияКлиентовНаБирже()
  var ErrCode, RetMode;
  GetRegistryValue("SECUR\\ОНЛАЙН РЕГИСТРАЦИЯ КЛ НА БИРЖЕ", V_BOOL, RetMode, ErrCode);
  return RetMode and (ErrCode == 0);
end;
```

---
