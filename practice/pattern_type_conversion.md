# Практика: Преобразование типов данных (int, string, NVL, SQL_ConvType, ValType)

**Теория:** [BnRSL.md## Скалярные типы]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `РаспечататьПоле`

**Источник:** `Mac/Mbr/swrurprn.mac`  
**Тип:** `macro`  
**Размер:** 149 строк

```rsl
macro РаспечататьПоле( имя, поле, standart )

  if ( valtype(Standart)==V_UNDEF ) standart = ST_UNDEF; end;

  if( поле!="" )
    /* ----------------- Печать поля 11 (A,R,S) ----------------------- */
    if( (имя == "11A") OR (имя == "11R") OR (имя == "11S") )
      [###:MT AND DATE OF ORIGINAL MESSAGE](имя);
      PrintMultiFields( поле, 10, 3 );
    /* ----------------- Печать поля 12 ------------------------------ */
    elif( имя == "12" )
      [###:SUB-MESSAGE TYPE](имя);
      [    #](поле);
    /* ----------------- Печать поля 13 ------------------------------ */
    elif( имя == "13" )
      [###:DATA/TIME INDICATOR](имя);
      [    #](поле);
    /* ----------------- Печать поля 20 ------------------------------ */
    elif( имя == "20" )
      [###:TRANSACTION REFERENCE NUMBER](имя);
      [    #](поле);
    /* ----------------- Печать поля 21 ------------------------------ */
    elif( имя == "21" )
      [###:RELATED REFERENCE](имя);
      [    #](поле);
    /* ----------------- Печать поля 25 ------------------------------ */
    elif( имя == "25" )
      [###:ACCOUNT IDENTIFICATION](имя);
      [    #](поле);
    /* ----------------- Печать поля 28 (любое) ---------------------- */
    elif( SubStr(имя,1,2) == "28" )
      [###:STATMENT NUMBER/SEQUENCE NUMBER](имя);
      [    #](поле);
    /* ----------------- Печать поля 30 ------------------------------ */
    elif( имя == "30" )
      [###:VALUE DATE](имя);
      [    ##########](YYMMDD2Date(поле):f);
    /* ----------------- Печать поля 32A ----------------------------- */
    elif( имя == "32A" )
      [###:VALUE DATE, CURRENCY CODE, AMOUNT](имя);
      [    #](поле);
      PrintField32( поле );
    /* ----------------- Печать поля 32B ----------------------------- */
    elif( имя == "32B" )
      PrintField32B( поле );
    /* ----------------- Печать поля 32 ----------------------------- */
    elif( имя == "32C" )
      [###:VALUE DATE, CURRENCY CODE, AMOUNT](имя);
      [    #](поле);
      PrintField32( поле );
    /* ----------------- Печать поля 32A ----------------------------- */
    elif( имя == "32D" )
      [###:VALUE DATE, CURRENCY CODE, AMOUNT](имя);
      [    #](поле);
      PrintField32( поле );
    /* ----------------- Печать поля 34F ----------------------------- */
    elif( SubStr(имя,1,3) == "34F" )
      [####:NUMBERS AND SUMM OF ENTRIES](имя);
      [     #](поле);
    /* ----------------- Печать поля 50 ------------------------------ */
    elif( (имя == "50") OR (имя == "50K") )
      [###:ORDERING CUSTOMER](имя);
      StrRestoreStandart( поле, поле, standart );
      PrintMultiFields( поле, 35, 4 );
    /* ---------- Печать полей 52, 53, 54, 56, 57, 58 ---------------- */
    elif( (SubStr(имя,1,2) == "52") OR (SubStr(имя,1,2) == "53") OR
          (SubStr(имя,1,2) == "54") OR (SubStr(имя,1,2) == "56") OR
          (SubStr(имя,1,2) == "57") OR (SubStr(имя,1,2) == "58") )
      PrintIns( имя, поле, standart );
    /* ----------------- Печать поля 59 ------------------------------ */
    elif( имя == "59" )
      [###:BENEFICIARY CUSTOMER](имя);
      StrRestoreStandart( поле, поле, standart );
      PrintMultiFields( поле, 35, 5 );
    /* ----------------- Печать поля 60 (любое) ---------------------- */
    elif ( SubStr(имя,1,2) == "60" )
      PrintField60_62_64_65( имя, поле );
    /* ----------------- Печать поля 61 ------------------------------ */
    elif( имя == "61" )
      [###:STATEMENT LINE](имя);
      PrintField61( поле, standart );
    /* ----------------- Печать полей 62, 64, 65 --------------------- */
    elif ( SubStr(имя,1,2) == "62" )
      PrintField60_62_64_65( имя, поле );
    elif ( SubStr(имя,1,2) == "64" )
      PrintField60_62_64_65( имя, поле );
    elif ( SubStr(имя,1,2) == "65" )
      PrintField60_62_64_65( имя, поле );
    /* ----------------- Печать поля 70 ------------------------------ */
    elif( имя == "70" )
      [###:DETAILS OF PAYMENT](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 4 );
     /* ----------------- Печать поля 71A ----------------------------- */
    elif ( имя == "71A" )
      [###:DETAILS OF CHARGES](имя);
      [    #](поле);
    /* ----------------- Печать поля 71B ------------------------------ */
    elif( имя == "71B" )
      [###:DETAILS OF CHARGES](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 6 );
    /* ----------------- Печать поля 72 ------------------------------ */
    elif( имя == "72" )
      [###:SENDER TO RECEIVER INFORMATION](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 6 );
    /* ----------------- Печать поля 75 ------------------------------ */
    elif( имя == "75" )
      [###:QUERIES](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 6 );
    /* ----------------- Печать поля 76 ------------------------------ */
    elif( имя == "76" )
      [###:ANSWERS](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 6 );
     /* ----------------- Печать поля 77E ----------------------------- */
    elif ( имя == "77E" )
      [###:PROPRIETARY MESSAGE](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 78, 125 );
    /* ----------------- Печать поля 77A ------------------------------ */
    elif( имя == "77A" )
      [###:NARRATIVE](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 35, 20 );
    /* ----------------- Печать поля 79 ------------------------------ */
    elif( имя == "79" )
      [###:NARRATIVE DESCRIPTION OF THE MESSAGE TO WHICH TRE QUERY RELATES](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 50, 35 );
    /* ----------------- Печать поля 86 ------------------------------ */
    elif( имя == "86" )
      [###:INFORMATION TO ACCOUNT OWNER](имя);
      StrRestoreStandart( поле, поле, standart, 0 );
      PrintMultiFields( поле, 65, 6 );
    /* ----------------- Печать поля 90 ------------------------------ */
    elif( SubStr(имя,1,2) == "90" )
      [###:NUMBERS AND SUMM OF ENTRIES](имя);
      [    #](поле);
    /* ----------------- Печать поля MFIELDS -------------------------- */
    elif( имя == "MFIELDS" )
      [COPY OF LEAST THE MANDATORY FIELDS OF THE ORIGINAL MESSAGE];
      PrintMultiFields( поле, 35, 55 );
    /* ----------------- Все остальные поля ---------------------------- */
    else
      PrintOtherField( имя, поле );
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

## Пример 4: `PrintContr`

**Источник:** `Mac/DLNG/TRUST/tsorder.mac`  
**Тип:** `private macro`  
**Размер:** 39 строк

```rsl
private macro PrintContr( ncopy:integer )

  var ComNumber = -1;
  var TempFile;
  var DocName;
  var persnFlag = false;
  var Account, BankName, CorrAcc, BankID;
  var AccountTr, BankNameTr, CorrAccTr, BankIDTr;
  var Val, Share, FIID;
  var fullstr, rub, Rstr, kop, procstr;
  var TotalSumm, ShortValText, TotalSummText, ValText, TotalSummCop, CopText;
  var ClientPaymAcc, ClientPaymBank, BICClientPaymBank, ClientPaymCorrAcc;
  var OurPaymAcc, OurPaymBank, BICOurPaymBank;
  var RateCom;
  var OurBankLicFlag, OurRepresPosFlag, OurRepresFlag, OurRepresDocFlag, ClientRepresPosFlag, ClientRepresFlag,
      MinVCapFlag, TotalSummFlag,
      ComManagFlag, ComSuccesFlag, ComOUTCapFlag, ComOUTEndFlag;
  var HeadPR  = "┌─────┬────────────────────────────────────────────────────────────────────────────────────────────────────┐\n"+
                "│  №  │                                             Описание                                               │\n"+
                "├─────┼────────────────────────────────────────────────────────────────────────────────────────────────────┤";

  var FootPR  = "└─────┴────────────────────────────────────────────────────────────────────────────────────────────────────┘\n";
  var DelimPR = "├─────┼────────────────────────────────────────────────────────────────────────────────────────────────────┤";
  var iPR = 1;
  var ReportFileName, errcode, errtext;
  FILE ReportOutFile() txt write; /*файл вывода для протокола*/
  var MngPlanFlag = FALSE, MngPlanGBPRate, MngPlanID, CalcPeriodName, CalcPeriodText, ComissEnd, QuantyCalDays = 0;
  var ComPeriod:integer = -1, ComPeriodStr:string = "";

  /*Шаблон*/
  [#]( GrTemp.rec.File_Name );

  /*Имя выходного файла*/
  DocName = "Договор ИДДУ № " + Order.Number();
  if( ncopy > 1 )
     /*добавить в название номер копии, иначе будет ошибка при создании, т.к. получим
       несколько документов с одинаковыми именами*/
     DocName = DocName + "_"+ string(ncopy);
  end;
```

---

## Пример 5: `FillInformationTable`

**Источник:** `Mac/Cb/xcompl_mass_check.mac`  
**Тип:** `private macro`  
**Размер:** 31 строк

```rsl
private macro FillInformationTable(obj : @variant)
    var stat = true;
    InitProgress( obj.ResultSelect.size, "~Ctrl-Break~ Прервать", "Заполнение временной таблицы" );
    var pdlserviceCache = RsbSQLInsert("pdlservice.tmp");
    var pdlservice = TRecHandler("pdlservice.tmp");

    var t = 0, j = 0, jt = 0;
    var sizea = obj.ResultSelect.size;
    while (t < sizea)
        var i = t;
        ClearRecord (pdlservice);
        var SelectResult = obj.ResultSelect[i];
        if(ValType(SelectResult.RowID)      != V_UNDEF) pdlservice.rec.RowID           = SelectResult.RowID;     end;
        if(ValType(SelectResult.IdentMess)  != V_UNDEF) pdlservice.rec.SystemId        = SelectResult.IdentMess; end;
        if(ValType(SelectResult.DateMess)   != V_UNDEF) pdlservice.rec.UpDateAt        = SelectResult.DateMess;  end;
        if(ValType(SelectResult.AttrDel)    != V_UNDEF) pdlservice.rec.IsDeletedPeople = SelectResult.AttrDel;   end;
        if(ValType(SelectResult.FullName)   != V_UNDEF) pdlservice.rec.FullName        = SelectResult.FullName;  end;
        if(ValType(SelectResult.birthdate)  != V_UNDEF) pdlservice.rec.BirthDate       = SelectResult.birthdate; end;
        if(ValType(SelectResult.NameDoc)    != V_UNDEF) pdlservice.rec.PaperName       = SelectResult.NameDoc;   end;
        if(ValType(SelectResult.SeriesDoc)  != V_UNDEF) pdlservice.rec.PaperSeries     = SelectResult.SeriesDoc; end;
        if(ValType(SelectResult.NumDoc)     != V_UNDEF) pdlservice.rec.PaperNumber     = SelectResult.NumDoc;    end;
        if(ValType(SelectResult.Issue)      != V_UNDEF) pdlservice.rec.PaperIssue      = SelectResult.Issue;     end;
        if(ValType(SelectResult.CodeCat)    != V_UNDEF) pdlservice.rec.CategoryCode    = SelectResult.CodeCat;   end;
        if(ValType(SelectResult.DescrCat)   != V_UNDEF) pdlservice.rec.CategoryName    = SelectResult.DescrCat;  end;
        if(ValType(SelectResult.Job)        != V_UNDEF) pdlservice.rec.Post            = SelectResult.Job;       end;
        if(ValType(SelectResult.Biography)  != V_UNDEF) pdlservice.rec.Biography       = SelectResult.Biography; end;

        pdlserviceCache.AddRecord(pdlservice);
        t = t + 1;
        UseProgress(t);
    end;
```

---

## Пример 6: `ExecuteStep`

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

## Пример 7: `ReportOnOneExchangeReestr`

**Источник:** `Mac/DEPOSITR/od_ex_rs.mac`  
**Тип:** `macro`  
**Размер:** 62 строк

```rsl
macro ReportOnOneExchangeReestr( TypeOperation )

  var OutCurr, IncCurr,
      Loop;
  var КодВалюты; /* Код валюты ОП */

  ClearRecord(Reestr);
  Reestr.ExchangeNumber = {ExBankNumber};
  Reestr.Emp_Ref        = Session.Emp_Ref;
  Reestr.Sess_Ref       = Session.Number;
  Reestr.Type_Ref       = RstTypes.Type;
  Reestr.OutCurr_Ref    = ANY_CURR;
  Reestr.IncomeCurr_Ref = ANY_CURR;
  Reestr.Rate_Ref       = 0;

  КодВалюты = int(Curr.ExternalCode);

  /* покупка валюты, ПД и неплатежеспособной валюты */
  if(   ( TypeOperation == CDF_OperCurrBuy        ) OR
        ( TypeOperation == CDF_OperPayDocBuy      ) OR
        ( TypeOperation == CDF_OperUnpayCurrBuy   ) )
     Reestr.OutCurr_Ref    = OutCurr = {NationalCur};
     Reestr.IncomeCurr_Ref = IncCurr = КодВалюты;
  /* продажа валюты и ПД за рубли */
  elif( ( TypeOperation == CDF_OperCurrSale       ) OR
        ( TypeOperation == CDF_OperPayDocSale     ) )
     Reestr.OutCurr_Ref    = OutCurr = КодВалюты;
     Reestr.IncomeCurr_Ref = IncCurr = {NationalCur};
  /* покупка/продажа ПД за валюту */
  elif( ( TypeOperation == CDF_OperPayDocSaleCurr ) OR
        ( TypeOperation == CDF_OperPayDocBuyCurr  ) OR
  /* проверка на подлинность */
        ( TypeOperation == CDF_OperCheck          ) OR
  /* замена неплатежной валюты */
        ( TypeOperation == CDF_OperChange         ) OR
  /* размен валюты */
        ( TypeOperation == CDF_OperSplit        ) )
     Reestr.OutCurr_Ref    = OutCurr = КодВалюты;
     Reestr.IncomeCurr_Ref = IncCurr = КодВалюты;
  /* принятие на инкассо и экспертизу */
  elif( ( TypeOperation == CDF_OperExpert         ) OR
        ( TypeOperation == CDF_OperIncasso        ) OR
        ( TypeOperation == CDF_OperPayDocExpert   ) OR
        ( TypeOperation == CDF_OperPayDocIncasso  ) OR
  /* получение по пластиковым картам */
        ( TypeOperation == CDF_OperCardTake     ) )
     Reestr.OutCurr_Ref    = OutCurr = ANY_CURR;
     Reestr.IncomeCurr_Ref = IncCurr = КодВалюты;
  /* конверсия */
  elif  ( TypeOperation == CDF_OperCurrConversion ) 
     Reestr.OutCurr_Ref    = OutCurr = ANY_CURR;
     Reestr.IncomeCurr_Ref = IncCurr = ANY_CURR;
  /* возврат с инкассо и экспертизы */
  elif( ( TypeOperation == CDF_OperReturnExpert        ) OR
        ( TypeOperation == CDF_OperReturnIncasso       ) OR
        ( TypeOperation == CDF_OperPayDocReturnExpert  ) OR
        ( TypeOperation == CDF_OperPayDocReturnIncasso ) OR
  /* выдача по пластиковым картам */
        ( TypeOperation == CDF_OperCardGive       ) )
     Reestr.OutCurr_Ref    = OutCurr = КодВалюты;
     Reestr.IncomeCurr_Ref = IncCurr = ANY_CURR;
  end;
```

---

## Пример 8: `_ClientIdentMass`

**Источник:** `Mac/Cb/ws_clientident.mac`  
**Тип:** `private macro`  
**Размер:** 54 строк

```rsl
private macro _ClientIdentMass(oClientIdent)
    var wsClientIdentMass : RSCReqFindClientsListResponse;
    var clientsList;
    var oClientListElem;
    var i = 0;

    // Legal
    var pClientIdentMassLegalPrm = ClientIdentMassLegalPrm();
    var pClientIdentMassLegalPrmCount = 0;
    //Person
    var pClientIdentMassPersonPrm = ClientIdentMassPersonPrm();
    var pClientIdentMassPersonPrmCount = 0;

    if(GenPropID(oClientIdent, "clientsList") != -1) // обращаемся к свойству, если оно существует в объекте
        WS_SetAttributeValue(@clientsList, 1, "", "clientsList", oClientIdent, V_GENOBJ, true, null);
        if(GenPropID(clientsList, "size") != -1)
            wsClientIdentMass.resultList = TArray(false, clientsList.size);

            pClientIdentMassLegalPrm.IdenArray = TArray(false, clientsList.size);
            pClientIdentMassLegalPrm.CodeArray = TArray(false, clientsList.size);
            pClientIdentMassLegalPrm.NameArray = TArray(false, clientsList.size);
            pClientIdentMassLegalPrm.ClientID  = TArray(false, clientsList.size);

            pClientIdentMassPersonPrm.IdenArray = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.NameArray = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.Name1 = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.Name2 = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.Name3 = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.Born = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.PaperKind = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.PaperSeries = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.PaperNumber = TArray(false, clientsList.size);
            pClientIdentMassPersonPrm.ClientID    = TArray(false, clientsList.size);
            

            while(i < clientsList.size)
                oClientListElem = clientsList[i];

                var wsClientIdent : TClientIdent;
                WS_CheckParameter(1, oClientListElem, true, V_GENOBJ);
                wsClientIdent = TClientIdent;
                FillTWsClientIdent(oClientListElem, wsClientIdent, false);

                var ClientRequisites = wsClientIdent.ReqFindClient;
                if (ClientRequisites.Type == ReqTypeIns)
                    pClientIdentMassLegalPrm.IdenArray[pClientIdentMassLegalPrmCount] = /*pClientIdentMassLegalPrmCount + 1*/wsClientIdent.id;

                    if (ValType(ClientRequisites.INN) != V_UNDEF)
                        var INN = "";
                        splitINN_KPP(ClientRequisites.INN, INN);
                        pClientIdentMassLegalPrm.CodeArray[pClientIdentMassLegalPrmCount] = INN;
                    else 
                        pClientIdentMassLegalPrm.CodeArray[pClientIdentMassLegalPrmCount] = "";
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

## Пример 10: `GetInfoByCells`

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

## Пример 11: `ОбработатьСообщениеSB`

**Источник:** `Mac/Mbr/swsbin.mac`  
**Тип:** `macro`  
**Размер:** 23 строк

```rsl
macro ОбработатьСообщениеSB( КодНачалаБлокаПрочитан, СчитанныйКодНачалаБлока, Отправитель, Получатель, ДатаОтправки, AddSign:bool )

  /* Вспомогательные переменные */
  var НомерФормы, РелизФормы, НомерБлока, Приоритет, result, СчитанныйБлок, Вид;
  var НомерПриложения, Block177, Block451, Block405, BlockMUR, FlagACK = false;
  var КодНазначениеСообщения, АбонентОтправитель, АбонентПолучатель, 
      ВремяОтправки, Ключ, ДлинаКлюча, ДатаКлюча, rsms;
  var tmp1, tmp2, tmp3;
  var CryptoAPI = RsCryptoAPI();

  УдалитьПеременныеБлока();
  ОчиститьДополнительныйТекстовыйБлокБуфер();
  if(not СчитатьБлокСлужебнойИнформацииСМФР(КодНачалаБлокаПрочитан, КодНазначениеСообщения, Отправитель, Получатель, АбонентОтправитель, АбонентПолучатель, ДатаОтправки, ВремяОтправки, Ключ, ДлинаКлюча, ДатаКлюча)) return -1; end;
  if(СчитатьДополнительныйТекстовыйБлокБуфер(КодНачалаБлокаПрочитан)) return -1; end;
  if((not СчитатьBasicHeaderBlockAck(КодНачалаБлокаПрочитан, tmp1, НомерПриложения, Block177, Block451, Block405, BlockMUR))
      AND (НомерПриложения != НомерПриложенияFIN) ) return -1; end;
  
  /* второй раз читать Basic Header Block надо только для ACK/NAK, UAK/UNK */
  if(НомерПриложения == НомерПриложенияFINСервис)
     result = СчитатьBasicHeaderBlock(КодНачалаБлокаПрочитан, tmp1, НомерПриложения);
     if((valtype(result)==V_INTEGER) AND (result == КонецФайла)) return 3; end;
     if( not result ) return -1; end;
  end;
```

**Комментарий автора:**
Вспомогательные переменные */

---

## Пример 12: `ExecuteCaseStep`

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

## Пример 13: `GetRatesDFS`

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

## Пример 14: `SvOpReservLine`

**Источник:** `Mac/DLNG/SECUR/scservop.mac`  
**Тип:** `private macro`  
**Размер:** 24 строк

```rsl
private macro SvOpReservLine( Data:SvOpReserve, Num:INTEGER, headIsPrinted, p_ItogReservLineByFIID:ItogReservLineByFIID )
  var Reserv, ReservChange, StrLine = "", DealCode, Contractor, ResKindStr = "", ind = 0, AccDbt = "", BaseAcc = "", RiskGrp, ResPc, BaseSum, RiskGrp2, ResPc2, BaseSum2, AccCred = "", ReservAcc = "";
  var ReservChangeOR = $0, SumOR = $0;
  var BuyCostAcc = TRecHandler("account"), BuyCostRest = $0.0, BonusAcc = TRecHandler("account"), BonusRest = $0.0, PayedNKDAcc = TRecHandler("account"), PayedNKDRest = $0.0, AccruedNKDAcc = TRecHandler("account"),
      AccruedNKDRest = $0.0, DiscountAcc = TRecHandler("account"), DiscountRest = $0.0, CorrCostAcc = TRecHandler("account"), CorrCostRest = $0.0, OverAcc = TRecHandler("account"), OverRest = $0.0;
  var PDAcc = TRecHandler("account"), DDAcc = TRecHandler("account"), PDRest = $0.0, DDRest = $0.0;
  var FD;
  var IsBPP = 0;
  var AccCateg = "", NKDCat = "", ReservAccount = "", AccCategNum = "", NKDCatNum = "";
  var ReservAccRec = TRecHandler( "account" );
  var ReservAccRecPD = TRecHandler( "account" );
  var CorReservAcc = TRecHandler( "account" );
  var IsAddRes = 1;
  var FirolePD = -1, FiroleDD = -1;
  var FIROLE_ = -1;
  var RestReserv = 0, RestReservPD = 0, RestCorReserv = 0;

  if( not ((ScOprServDoc.OperationKind == KINDRES_REQ) and (Data.ResKind == KINDRES_SALEREPO2)) )
     Reserv       = money(ABS(Data.BaseSum)*double(Data.ResPc)/100.);
     if((ValType(Data.CorrectSum) != V_UNDEF) and (Data.CorrectSum != $0))
       ReservChange = ABS(Data.CorrectSum);
     else
       ReservChange = ABS(Reserv-Data.OldReserv);
     end;
```

---

## Пример 15: `ExecuteStep`

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

