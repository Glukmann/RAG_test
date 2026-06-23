# Практика: Продвинутая работа с SQL (SQLParam, addParam, execSQLselect, DL_RSDCommand, TRsbDataSet)

**Теория:** [BnRSL.md## Класс: `RsdRecordset`]

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

## Пример 3: `isNewDirection`

**Источник:** `Mac/DEPOSITR/calccorr.mac`  
**Тип:** `macro`  
**Размер:** 34 строк

```rsl
macro isNewDirection
//
// Возвращает true, если Детский счет (конкретный)
// обрабатывался по-новому, т.е. проценты были причислены
// во время выполнения 82 операции.
// Функция ищет операцию 72/82 (причисление процентов 
// при обработке договора). Если операция найдена, ее
// DepDate_Document равен Prol_DateDep-1 и ее сумма не 0,
// то счет обработан по-новому.
// 
// Проверка имеет смысл только в том квартале, когда сменили 
// условия причисления процентов при обработке договоров.
// В следующем квартале допустимо возвращать true и не париться.
// Но в макросе момент смены параметра я не определю - нет историчности.
// 
  var ret = true;
  var InSum;
  var cmd,rs;
  var strcmd = "SELECT t_InSum FROM dsbdepdoc_dbt " +
               " WHERE t_Referenc = ? "             +
               "   AND t_TypeOper = 72 AND t_TypeComplexOper = 82 ";

  if ( DEP_ACC_REC.Prol_DateDep != Date( 0, 0, 0 ) )
    strcmd = strcmd + " AND t_DepDate_Document = ? ";
    cmd = RsdCommand( strcmd );
    cmd.addParam("t_Referenc", RsdBp_in);
    cmd.value   ("t_Referenc") = DEP_ACC_REC.Referenc;
    cmd.addParam("t_DepDate_Document", RsdBp_in);
    cmd.value   ("t_DepDate_Document") = DEP_ACC_REC.Prol_DateDep - 1;
  else
    cmd = RsdCommand( strcmd );
    cmd.addParam("t_Referenc", RsdBp_in);
    cmd.value   ("t_Referenc") = DEP_ACC_REC.Referenc;
  end;
```

**Комментарий автора:**
 Возвращает true, если Детский счет (конкретный) обрабатывался по-новому, т.е. проценты были причислены

---

## Пример 4: `SfFormDocumentsBatch`

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

## Пример 5: `Charge_Batch`

**Источник:** `Mac/Cb/sf_lib.mac`  
**Тип:** `private macro`  
**Размер:** 38 строк

```rsl
private macro Charge_Batch( chargers, _size )

  var sqlStr = " SELECT t_Account, t_Amount, t_FIID FROM dpmaddpi_dbt WHERE t_PaymentID = ? AND t_DebetCredit = ? ";
  var i:integer = 0;
  while( i < _size )
    if( chargers[i].bChargeable == true )
      var cmd = RsdCommand( sqlStr );
      cmd.addParam( "", RSDBP_IN, chargers[i].PaymentID );
      cmd.addParam( "", RSDBP_IN, PRT_Credit );

      var rs = RsdRecordset( cmd );
      var isPmWithNDS = false;
      if( getPmAddPiParms(chargers[i], rs, @isPmWithNDS) == false )
        if( isPmWithNDS == false )
          //Определить сумму комиссий по платежу: AmountComiss = pmPaym.BaseAmount.
          chargers[i].AmountComiss = chargers[i].BaseAmount;      
          //Определить валюту сумм комиссий по платежу: FiidComiss = pmPaym.BaseFIID.
          chargers[i].FIIDComiss = chargers[i].BaseFIID;
          //Массово заменить счет получателя платежа: pmPaym.ReceiverAccount = accFromComiss.
          //correctReceiverAccount( charger );
        else //по платежу есть разноска
          //Удалить разноски платежа pmPaym->pmaddpi. Действие удаления привязать к шагу операции соответствующего платежа.
          deletePmAddPi( chargers[i] );


          //Если начисление НДС и комиссий было произведено на один и тот же счет - AccFromComiss = AccFromNDS, 
          if( chargers[i].AccFromComiss == chargers[i].AccFromNDS )      
            correctPaymParms( chargers[i] );
          else //Иначе (начисление было произведено на разные счета)
            //1.  Создать разноску по оплате комиссий для платежа Paym:
            var Ground = " Оплата комиссии " + chargers[i].ComissCode; 
            insertPmAddPi( chargers[i].PaymentID, chargers[i].FiidComiss, chargers[i].AmountComiss, 
                           chargers[i].FiidComiss, chargers[i].AmountComiss, chargers[i].AccFromComiss, Ground );
            //2.  Создать разноску по оплате НДС для платежа Paym:
            Ground = " НДС по комиссии " + chargers[i].ComissCode; 
            insertPmAddPi( chargers[i].PaymentID, chargers[i].FiidComiss, chargers[i].AmountNDS, 
                           chargers[i].FiidComiss, chargers[i].AmountNDS, chargers[i].AccFromNDS, Ground );
          end;
```

---

## Пример 6: `_ExecuteDepoAcc`

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

## Пример 7: `AmountReserveRevaluation`

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

## Пример 8: `ExecuteStep`

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

## Пример 9: `ExecuteStep`

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

## Пример 10: `PrepMassExecuteStep`

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

## Пример 11: `ИзменитьСрокиИсполнения_ДляСделки`

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

## Пример 12: `GetPtsvdpList1`

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

## Пример 13: `ВыполнитьПеревод`

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

## Пример 14: `Draw`

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

## Пример 15: `GetClientProductList`

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

