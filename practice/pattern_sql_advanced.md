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

## Пример 16: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/old/screp0020.mac`
**Тип:** `macro`
**Размер:** 22 строк

```rsl
macro ExecuteStep( doc, FDoc)
  record  deal(dl_tick);
  var     FD;
  var     Dc, Di, Dk, Dp;

  SetBuff( deal, FDoc ); 

  FD = SPFirstDoc( deal, false );

  GetOprDate( FD.GetKindDate(DATE_DEALDATE), Dc );
  GetOprDate( FD.GetKindDate(DATE_DEALEXEC), Di );

  if( Dc != Di )
     if( false)//ПоставитьСнятьВнебалансЧастьРЕПО( FD, FDoc, FD.GetRQ(DLRQ_TYPE_PAYMENT).rec.Amount, FD.GetRQ(DLRQ_TYPE_PAYMENT).rec.FIID, FD.DateArray[DATE_DEALDATE], true ) )
        return 1;
     end;
  else
     if( not ОбновитьСтатусЧастиСделки( FD.dl_leg, DL_LEG_BALANCE ) )
        msgbox("Ошибка при изменении статуса сделки");
        return 1;
     end;
  end;
```

---

## Пример 17: `GetAccountRest`

**Источник:** `Mac/DLNG/SECUR/sectr010.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro GetAccountRest(accNumb,accChap,accCur,restDate)
  var cmd;
  cmd=RsdCommand(RslDefCon,"begin ? := RSB_ACCOUNT.restall(?,?,?,?,?); end;");
  cmd.AddParam("retval",RSDBP_RETVAL,V_NUMERIC);
  cmd.AddParam("p_account",RSDBP_IN,accNumb);
  cmd.AddParam("p_chapter",RSDBP_IN,accChap);
  cmd.AddParam("p_cur",RSDBP_IN,accCur);
  cmd.AddParam("p_date",RSDBP_IN,restDate);
  cmd.AddParam("p_rest_cur",RSDBP_IN,accCur);
  cmd.execute();
  return cmd.value("retval");
OnError(er)
  return numeric(0);
end;
```

---

## Пример 18: `InsertDCOMSUM`

**Источник:** `Mac/DLNG/SECUR/Convert/2728_OutAccData.mac`
**Тип:** `macro`
**Размер:** 22 строк

```rsl
  macro InsertDCOMSUM( DealID, Kind, ComDate, Sum, NDS, Curr, PayCurr )
    var cmd, i = 0;

     cmd = RsdCommand( "insert into dcomsum_buf ( t_DealID, t_Kind, t_Date, t_Sum, t_NDS, t_Cur, t_PayCurr ) " +
                       "                  values ( ?, ?, ?, ?, ?, ?, ? ) " );
     cmd.NullConversion = true;

     cmd.addParam( "", RSDBP_IN, DealID );
     cmd.addParam( "", RSDBP_IN, Kind );
     cmd.addParam( "", RSDBP_IN, ComDate );
     cmd.addParam( "", RSDBP_IN, Sum );
     cmd.addParam( "", RSDBP_IN, NDS );
     cmd.addParam( "", RSDBP_IN, Curr );
     cmd.addParam( "", RSDBP_IN, PayCurr );

     cmd.execute();

     OnError(err);

     Message( "Строка: " + err.line + " | " + err.message );

  end;
```

---

## Пример 19: `ReSelectGroupProc`

**Источник:** `Mac/DEPOSITR/ReSelectGroupFNSPercentInfo.mac`
**Тип:** `macro`
**Размер:** 52 строк

```rsl
macro ReSelectGroupProc(reSelectBank, percInfoArr)
    var stat = true;
    var i = 0;
    var AmountIPBefore = 0, AmountBefore = 0;
    var errCode = 0, errText = "", chgPrz = percInfoArr[i].rec.chgPrz;

    SetOutput(getFullRepName(), false);
    
    if (percInfoArr.size > 0)
        printHeader();
    end;
    
    for (i, 0, percInfoArr.size - 1)
        AmountBefore = percInfoArr[i].rec.prcAmount;
        AmountIPBefore = percInfoArr[i].rec.prcAmountIP;
        
        if (percInfoArr[i].rec.isReady == "X")
            errCode = 22395;
        end;
        
        if (errCode == 0)
            if (percInfoArr[i].rec.unloadFlag == "X")
                errCode = calcChgPrz(reSelectBank, percInfoArr[i].rec, @chgPrz);
            end;
            
            if (errCode == 0)
                var cmd = RsdCommand("BEGIN ? := RSU_RTLFNS.ReSelectFNSData(?, ?, ?, ?); END;");

                cmd.addParam("ok",              RSDBP_RETVAL, V_INTEGER);
                cmd.addParam("ReCalcPcIE",      RSDBP_IN,     0);
                cmd.addParam("period",          RSDBP_IN,     percInfoArr[i].rec.period);
                cmd.addParam("errorRefAccount", RSDBP_IN,     percInfoArr[i].rec.clientID);
                cmd.addParam("errorCode",       RSDBP_IN,     chgPrz);

                cmd.NullConversion = true;
                cmd.execute();
            end;
        end;
        
        if (errCode > 0)
            errText = SetParmMessage(GetErrMessage(errCode));
        end;

        printLine(i, percInfoArr[i].rec, AmountBefore, AmountIPBefore, errText);
    end;
    
    if (percInfoArr.size > 0)
        printFooter();
    end;

    return stat;
end;
```

---

## Пример 20: `GetAccDprt`

**Источник:** `Mac/LC/lc_common.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro GetAccDprt(Account : string, FIID : integer, Chapter : integer) : integer
  var Department = -1;
  var rs = execSQLselect( "SELECT t_Department "
                          "  FROM daccount_dbt "
                          " WHERE t_Chapter = :Chapter "
                          "   AND t_Account = :Account "
                          "   AND t_Code_Currency = :FIID ",
                          makeArray( SQLParam("Chapter", Chapter),
                                     SQLParam("Account", Account),
                                     SQLParam("FIID",    FIID   ) )
                        );
  if(rs and rs.moveNext())
    Department = rs.value("t_Department");
  end;
```

---

## Пример 21: `SfSrv_AddSfDocs`

**Источник:** `Mac/Cb/sfsrv_lib.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
macro SfSrv_AddSfDocs( Action, SfDefCom, AccTrnID:bigint, AccTrnID_NDS:bigint )

  var strSql : string; 
  var cmd : RsdCommand;

  strSql = " UPDATE dsfdeftmp_tmp SET t_AccTrnID = ?, t_AccTrnID_NDS = ? "
           " WHERE t_feeType = ? AND t_commNumber = ? AND t_conID = ? AND t_DatePeriodBegin = ? AND t_Action = ? ";
  
  cmd = RsdCommand( strSql );

  cmd.addParam( "", RSDBP_IN, AccTrnID );
  cmd.addParam( "", RSDBP_IN, AccTrnID_NDS );

  cmd.addParam( "", RSDBP_IN, SfDefCom.feeType );
  cmd.addParam( "", RSDBP_IN, SfDefCom.commNumber );
  cmd.addParam( "", RSDBP_IN, SfDefCom.SfContrID );
  cmd.addParam( "", RSDBP_IN, SfDefCom.datePeriodBegin );
  cmd.addParam( "", RSDBP_IN, Action );

  cmd.execute();

  return 0;

end;
```

---

## Пример 22: `prep`

**Источник:** `Mac/DLNG/MMARK/mmautokvit.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
MACRO prep()
    //dialog_flag = SetDialogFlag(0);
    ClearKvit();

    var stat = execStoredFunc("RSI_MMARK.FillKvitTmp", V_INTEGER,
        makeArray(
            SQLParam("", 0),
            SQLParam("", 0),
            SQLParam("", {curdate}),
            SQLParam("", 0)
        )
    );

    //Prnt();
END;
```

---

## Пример 23: `CheckPaymReceiverName`

**Источник:** `Mac/Cb/rmcmptl.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro CheckPaymReceiverName
( PaymentID:integer, 
  SecondError:@integer, 
  fromInPmPrePro:bool,
  CmpAttr : integer //м.б. null
):integer

  var arr = makeArray( SQLParam( "p_PaymentID", PaymentID),
                       SQLParam( "p_CompareInPaym", IfThenElse(fromInPmPrePro, 1, 0)),
                       //SQLParam( "p_SecondError", IfThenElse(SecondError,SecondError,0), RSDBP_OUT ) 
					   SQLParam( "p_SecondError", V_INTEGER, RSDBP_OUT ) 
                     );
  if(CmpAttr != null)
    arr[arr.size] = SQLParam( "p_CmpAttr", CmpAttr)
  end;
```

---

## Пример 24: `UFEBS_InsertMesIdentificator`

**Источник:** `Mac/Mbr/ufgenmes.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro UFEBS_InsertMesIdentificator(MesID : integer, EDNo : string, EDDate : string, EDAuthor : string)
  execStoredFunc( "WLD_UFEBS.InsertMesIdentificator", V_UNDEF, makeArray ( SQLParam("p_MesID",    MesID),
                                                                            SQLParam("p_EDNo",     EDNo),
                                                                            SQLParam("p_EDDate",   EDDate),
                                                                            SQLParam("p_EDAuthor", EDAuthor),
                                                                            SQLParam("p_Tmp",      1),
                                                                            SQLParam("p_ObjType",  OBJTYPE_MES)
                                                                          ) );
end;
```

---

## Пример 25: `ReadED711MessageFields`

**Источник:** `Mac/Mbr/ufgd711_class.mac`
**Тип:** `macro`
**Размер:** 94 строк

```rsl
macro ReadED711MessageFields( ED711MessageFields : @TED711MessageFields )
  
  var fieldname = "", fieldvalue = "", blockname = "";
  
  while( СчитатьПоле(fieldname, fieldvalue, blockname) )
        
    if ( blockname == "" )
      if ( fieldname == "EDNo" )
        ED711MessageFields.EDNo = int(fieldvalue);
      elif ( fieldname == "EDDate" )
        ED711MessageFields.EDDate = ToDateYYYY_MM_DD(fieldvalue);
      elif ( fieldname == "EDAuthor" )
        ED711MessageFields.EDAuthor = fieldvalue;
      elif ( fieldname == "EDReceiver" )
        ED711MessageFields.EDReceiver = fieldvalue;
      elif ( fieldname == "CreationReason" )
        ED711MessageFields.CreationReason = fieldvalue;
      elif ( fieldname == "CreationDateTime" )
        ED711MessageFields.CreationDateTime = fieldvalue;
      end;
    elif ( blockname == "BICAccount" )    
      if ( fieldname == beginField )
        ED711MessageFields.BICAccount = TED711BICAccountFields();
      elif ( fieldname == "BIC" )
        ED711MessageFields.BICAccount.BIC = fieldvalue;
      elif ( fieldname == "CorrespAcc" )  
        ED711MessageFields.BICAccount.CorrespAcc = fieldvalue;
      end;    
    elif ( blockname == "FPSLiquidityInfo" )  
      if ( fieldname == beginField )
        ED711MessageFields.FPSLiquidityInfo = TED711FPSLiquidityInfoFields();
      elif ( fieldname == "BusinessDay" )
        ED711MessageFields.FPSLiquidityInfo.BusinessDay = ToDateYYYY_MM_DD(fieldvalue);
      elif ( fieldname == "FPSLiquidity" )
        ED711MessageFields.FPSLiquidityInfo.FPSLiquidity = moneyL(fieldvalue);
        ED711MessageFields.FPSLiquidityInfo.isReadFPSLiquidity = true;
      elif ( fieldname == "FPSEnterPosition" )
        ED711MessageFields.FPSLiquidityInfo.FPSEnterPosition = moneyL(fieldvalue);
        ED711MessageFields.FPSLiquidityInfo.isReadFPSEnterPosition = true;
      elif ( fieldname == "FPSPosition" )
        ED711MessageFields.FPSLiquidityInfo.FPSPosition = moneyL(fieldvalue);
        ED711MessageFields.FPSLiquidityInfo.isReadFPSPosition = true;
      elif ( fieldname == "CurrentBalance" )
        ED711MessageFields.FPSLiquidityInfo.CurrentBalance = moneyL(fieldvalue);
      elif ( fieldname == "ArrestSum" )
        ED711MessageFields.FPSLiquidityInfo.ArrestSum = moneyL(fieldvalue);
      elif ( fieldname == "MandatoryReserveSum" )
        ED711MessageFields.FPSLiquidityInfo.MandatoryReserveSum = moneyL(fieldvalue);
      elif ( fieldname == "CreditLimitSum" )
        ED711MessageFields.FPSLiquidityInfo.CreditLimitSum = moneyL(fieldvalue);
      elif ( fieldname == "CollectionOrdersSum" )
        ED711MessageFields.FPSLiquidityInfo.CollectionOrdersSum = moneyL(fieldvalue);
      end;
    elif ( blockname == "FPSTurnover" )
      if ( fieldname == beginField )
        ED711MessageFields.FPSTurnover = TED711FPSTurnoverFields();
      elif ( fieldname == "FPSCreditSum" )
        ED711MessageFields.FPSTurnover.FPSCreditSum = moneyL(fieldvalue);
        ED711MessageFields.FPSTurnover.isReadFPSCreditSum = true;
      elif ( fieldname == "FPSDebetSum" )
        ED711MessageFields.FPSTurnover.FPSDebetSum = moneyL(fieldvalue);
        ED711MessageFields.FPSTurnover.isReadFPSDebetSum = true;
      end;
    elif ( blockname == "LiqEDID" )
      if ( fieldname == beginField )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size] = TED711LiqEDIDFields();
      elif ( fieldname == "Sum" )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].Sum = moneyL(fieldvalue);
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].isReadSum = true;
      elif ( fieldname == "LiquidityTransKind" )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].LiquidityTransKind = fieldvalue;
      end;
    elif ( blockname == "LiqEDID\\EDRefID" )
      if ( fieldname == beginField )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].EDRefID = TED711NoDateAuthorFields();
      elif ( fieldname == "EDNo" )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].EDRefID.EDNo = int(fieldvalue);
      elif ( fieldname == "EDDate" )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].EDRefID.EDDate = ToDateYYYY_MM_DD(fieldvalue);
      elif ( fieldname == "EDAuthor" )
        ED711MessageFields.LiqEDID[ED711MessageFields.LiqEDID.size - 1].EDRefID.EDAuthor = fieldvalue;        
      end;
    elif ( blockname == "InitialED" )
      if ( fieldname == beginField )
        ED711MessageFields.InitialED = TED711NoDateAuthorFields();
      elif ( fieldname == "EDNo" )
        ED711MessageFields.InitialED.EDNo = int(fieldvalue);
      elif ( fieldname == "EDDate" )
        ED711MessageFields.InitialED.EDDate = ToDateYYYY_MM_DD(fieldvalue);
      elif ( fieldname == "EDAuthor" )
        ED711MessageFields.InitialED.EDAuthor = fieldvalue;
      end;
    end;
  end;
```

---

## Пример 26: `GenDoc`

**Источник:** `Mac/Mbr/ufgd463.mac`
**Тип:** `macro`
**Размер:** 34 строк

```rsl
macro GenDoc( addrMes )
debugbreak;
  var xml:object = ActiveX( "MSXML.DOMDocument" );
  
  SetBuff( wlmes, addrMes );

  PrintLog( 2, "Генерация информационного сообшения по ED463" );
  
  var FieldName, FieldValue, BlockName;
  var Annotation, CtrlCode, RefEDNo, RefEDDate, RefEDAuthor, ErrorDiagnostic;
  
  while( СчитатьПоле(FieldName, FieldValue, BlockName) )
    if( BlockName == "" )
      if( FieldName == "CtrlCode" )
        CtrlCode = FieldValue;
      end;
    elif( BlockName == "Annotation" )
      if( FieldName == "Annotation" )
        Annotation = FieldValue;
      end;
    elif( BlockName == "EDRefID" )
      if( FieldName == "EDNo" )
        RefEDNo = FieldValue;
      elif( FieldName == "EDDate" )
        RefEDDate = FieldValue;
      elif( FieldName == "EDAuthor" )
        RefEDAuthor = FieldValue;
      end;
    elif( BlockName == "ErrorDiagnostic" )
      if( FieldName == "ErrorDiagnostic" )
        ErrorDiagnostic = FieldValue;
      end;
    end;
  end;
```

---

## Пример 27: `DL_GetDateWorkDayForPayStep`

**Источник:** `Mac/DLNG/dl_calendtls.mac`
**Тип:** `macro`
**Размер:** 26 строк

```rsl
MACRO DL_GetDateWorkDayForPayStep(dateFrom:DATE, calenId:INTEGER, fiid:INTEGER, isObl:BOOL, isEarly:@BOOL, EarlyOnlyForObl, NoSettlCalend)
  var WorkDate = dateFrom;
  isEarly = false;

  if ((ValType(dateFrom) == V_DATE) and (dateFrom > date(1,1,1900)))
    var cmd = RsdCommand( "begin ?:= RSI_DlCalendars.GetDateWorkDayForPayStep(?,?,?,?,?,?,?);\n end; " );
    cmd.addParam("", RSDBP_OUT, V_DATE);
    cmd.addParam("", RSDBP_IN, dateFrom);
    cmd.addParam("", RSDBP_IN, calenId);
    cmd.addParam("", RSDBP_IN, fiid);
    cmd.addParam("", RSDBP_IN, IIF(isObl,1,0));
    cmd.addParam("", RSDBP_OUT, V_INTEGER);
    if (ValType(EarlyOnlyForObl) == V_BOOL)
      cmd.addParam("", RSDBP_IN,IIF(EarlyOnlyForObl,1,0));
    else
      cmd.addParam("", RSDBP_IN,0);
    end;
    if (ValType(NoSettlCalend) == V_INTEGER)
      cmd.addParam("", RSDBP_IN,NoSettlCalend);
    else
      cmd.addParam("", RSDBP_IN,0);
    end;
    cmd.execute();
    WorkDate = SQL_ConvTypeDate(cmd.value(0));
    isEarly = SQL_ConvTypeInteger(cmd.value(5)) == 1;
  end;
```

---

## Пример 28: `ReadFields`

**Источник:** `Mac/Mbr/ufgd332.mac`
**Тип:** `macro`
**Размер:** 42 строк

```rsl
  macro ReadFields() : bool
    var fieldname = "", fieldvalue = "", blockname = "";
    while ( СчитатьПоле(fieldname, fieldvalue, blockname) )
      if  (blockname == "")
        if  (fieldname == "EDAuthor")
          OriginatorUIS = fieldvalue;
        elif(fieldname == "EDReceiver")
          RecipientUIS = fieldvalue;
        end;
      elif(blockname == "PartInfo")
        if  (fieldname == "PartNo")
          PartNo = fieldvalue;
        elif(fieldname == "PartAggregateID")
          PartAggregateID = fieldvalue;
        end;
      elif(blockname == "TotalLiquidity")
        if  (fieldname == "BIC")
          TotalLiquidity.BIC = fieldvalue;
        end;
      elif(blockname == "TotalLiquidity\\Liquidity")
        if  (fieldname == "LiquiditySum")
          TotalLiquidity.LiquiditySum = fieldvalue;
        end;
      elif(blockname == "PURLiquidity")
        if  (fieldname == beginField)
          PURLiquidity[ PURLiquidity.size ] = LiquidityInfo();
        elif(fieldname == "BIC")
          PURLiquidity[ PURLiquidity.size-1 ].BIC = fieldvalue;
        end;
      elif(blockname == "PURLiquidity\\Liquidity")
        if  (fieldname == "LiquiditySum")
          PURLiquidity[ PURLiquidity.size-1 ].LiquiditySum = fieldvalue;
        end;
      elif(blockname == "InitialED")
        if  (fieldname == "EDDate")
          EDDate_InitMes = fieldvalue;
        end;
      end; 
    end; // while ( СчитатьПоле(fieldname, fieldvalue, blockname) )

    return TRUE;
  end;
```

---

## Пример 29: `GenDoc`

**Источник:** `Mac/Mbr/swgd752.mac`
**Тип:** `macro`
**Размер:** 62 строк

```rsl
macro GenDoc( addrMes )
  SetBuff( wlmes, addrMes );

  PrintLog( 2, "Генерация учетного объекта по сообщению MT750" );
  
  var ErrMsg = "";
  var fieldName = "", fieldValue = "", OK : bool;
  var field20 = "",
      field21 = "",
      field23 = "",
      field30 = "",
      field32 = "", 
      field71 = "", 
      field33 = "",
      field33Name = "",
      field53 = "",
      field53Name = "",
      field54 = "",
      field54Name = "",
      field72 = "", 
      field79 = "", 
      field57 = "",
      field57Name = "";

  while ( СчитатьПоле(fieldName, fieldValue) )
    OK = true;

    if( fieldName == TransactionReferenceNumberField )
      field20 = fieldValue;
    elif( fieldName == RelatedReferenceField )
      field21 = fieldValue;
    elif( fieldName == BankOperationCodeField )
      field23 = fieldValue;
    elif( fieldName == ValueDateField )
      field30 = fieldValue;
    elif( fieldName == ValueDateCurrencyCodeAmountField_B )
      field32 = fieldValue;
    elif( fieldName == DetailsOfChargesField_D )
      field71 = fieldValue;
    elif( InList(fieldName, TotalAmountClaimedField, CurrencyOriginalOrderedAmountField) )
      field33 = fieldValue;
      field33Name = fieldName;
    elif( substr(fieldName,1,2) == Sender_sCorrespondentField )
      field53 = fieldValue;
      field53Name = fieldName;
    elif( substr(fieldName,1,2) == Receiver_sCorrespondentField )
      field54 = fieldValue;
      field54Name = fieldName;
    elif( fieldName == SenderToReceiverInformationField_Z )
      field72 = fieldValue;
    elif( fieldName == NarrativeDescriptionField_Z )
      field79 = fieldValue;
    elif( substr(fieldName, 1, 2) == AccountWithInstitutionField )
      field57 = fieldValue;
      field57Name = fieldName;
    end;

    if( not OK )
      std.msg("Ошибка при обработке поля формы " + fieldname);
      return FALSE;
    end;
  end;
```

---

## Пример 30: `IdentClientByReqFindClientPerson`

**Источник:** `Mac/Cb/ws_client_lib.mac`
**Тип:** `macro`
**Размер:** 103 строк

```rsl
macro IdentClientByReqFindClientPerson(ClientRequisites : @variant, pLegalForm)
    var result = TClientIdentSuccess;
    var finder = TClientIdentFinder;

    var LegalForm = ReqTypePersn;
    if (ValType(pLegalForm) != V_UNDEF)
        LegalForm = pLegalForm;
    end;
    
    result.ReqID = "";
    result.ClientFullName = "";
    result.CountRezult = 0;
    result.ClientID = 0;
        
    finder.AddCondition(finder.COND_AND, "PS.T_PERSONID = PT.T_PARTYID");

    if (ClientRequisites.FullName != null)
        finder.AddCondition(finder.COND_AND, "PT.T_NORMALIZEDNAME = ?");
        finder.AddParam(NormalizeString(ClientRequisites.FullName));
    else
        if (ClientRequisites.FIO != null)
            var FIO = ClientRequisites.FIO;
            finder.AddCondition(finder.COND_AND, "RSI_RSB_STRING.NormalizeString2(PS.T_NAME1) = ?");
            finder.AddParam(NormalizeString(FIO.Surname));
                
            finder.AddCondition(finder.COND_AND, "RSI_RSB_STRING.NormalizeString2(PS.T_NAME2) = ?");
            finder.AddParam(NormalizeString(FIO.FirstName));
                
            if (FIO.Patronymic != null)
                finder.AddCondition(finder.COND_AND, "RSI_RSB_STRING.NormalizeString2(PS.T_NAME3) = ?");
                finder.AddParam(NormalizeString(FIO.Patronymic));
            end;
        end;
    end;
    
    if ((ClientRequisites.BirthDate != null) and (ClientRequisites.BirthDate != ZeroValue(V_DATE)))
        finder.AddCondition(finder.COND_AND, "PS.T_BORN = ?");
        finder.AddParam(ClientRequisites.BirthDate);
    end;
        
    var IDoc = ClientRequisites.IDoc;
    if (LegalForm == ReqTypePersn)
        if (ClientRequisites.IDoc != null)
            if(((IDoc.SerDoc != "") or (IDoc.NumDoc != "")) and (IDoc.TypeDoc != null))
                finder.AddCondition(finder.COND_AND, "PS.T_PERSONID = PD.T_PERSONID");
                finder.AddCondition(finder.COND_AND, "PD.T_PAPERKIND = ?");
                finder.AddParam(Int(IDoc.TypeDoc));

                if(IDoc.SerDoc != "") 
                    finder.AddCondition(finder.COND_AND, 
                    "REGEXP_REPLACE(RSI_RSB_STRING.NormalizeIDocSer(PD.T_PAPERSERIES), '(\\-|\\s+)') = REGEXP_REPLACE(?, '(\\-|\\s+)')");
                    finder.AddParam(NormalizeIDocSer(IDoc.SerDoc));
                end;

                if(IDoc.NumDoc != "") 
                    finder.AddCondition(finder.COND_AND, "PD.T_PAPERNUMBER = ?");
                    finder.AddParam(IDoc.NumDoc);
                end;
            else
                finder.AddCondition(finder.COND_AND, "PS.T_PERSONID = PD.T_PERSONID(+)");
                finder.AddCondition(finder.COND_AND, "PD.T_PAPERKIND(+) = 0");
            end;
        else
            finder.AddCondition(finder.COND_AND, "PS.T_PERSONID = PD.T_PERSONID(+)");
            finder.AddCondition(finder.COND_AND, "PD.T_PAPERKIND(+) = 0");
        end;
    elif (LegalForm == ReqTypePersnFssp)
        if(((IDoc.SerDoc != "") or (IDoc.NumDoc != "")) and (IDoc.TypeDoc != null))
            finder.AddCondition(finder.COND_AND, "(PD.t_paperkind is null or (");
            finder.AddCondition(finder.COND_NO, "PD.T_PAPERKIND = ?");

            var TypeDoc = GetPaperKindFromConnectDocKind(IDoc.TypeDoc);
            finder.AddParam(TypeDoc);

            if(IDoc.SerDoc != "") 
                finder.AddCondition(finder.COND_AND, 
                "REGEXP_REPLACE(RSI_RSB_STRING.NormalizeIDocSer(PD.T_PAPERSERIES), '(\\-|\\s+)') = REGEXP_REPLACE(?, '(\\-|\\s+)')");
                finder.AddParam(NormalizeIDocSer(IDoc.SerDoc));
            end;

            if(IDoc.NumDoc != "") 
                finder.AddCondition(finder.COND_AND, "PD.T_PAPERNUMBER = ?");
                finder.AddParam(IDoc.NumDoc);
            end;

            finder.AddCondition(finder.COND_NO, "))");
        else
            finder.AddCondition(finder.COND_AND, "PD.T_PAPERKIND = 0");
        end;
    end;
 
    finder.Find(LegalForm);
        
    result.CountRezult = finder.CountRezult();
    result.ClientID = finder.ClientID();
    result.ClientFullName = finder.ClientFullName();

    if(result.ClientID > 0)
      GetTwins(result.ClientID, result.Twins);
    end;
      
    return result;
end;
```

---

## Пример 31: `Блок`

**Источник:** `Mac/BOOK/GZRputpr.mac`
**Тип:** `block`
**Размер:** 12 строк

```rsl
	rest_before_cmd.addParam( "Referenc", RSDBP_IN,rs.value("t_Referenc") );
	rest_before_cmd.addParam( "Date_Document", RSDBP_IN,DateReport );
	rest_before_cmd.addParam( "NumDayDoc", RSDBP_IN,NumDayDoc );
	rest_before_cmd.addParam( "Date_Document2", RSDBP_IN,DateReport );
    rest_before_cmd.execute;
    rest_before_rs = RsdRecordset( rest_before_cmd );
    if (rest_before_rs.moveNext)
      RestBefore = rest_before_rs.value("t_Rest");
    else
      RestBefore = 0;
    end;
    rest_before_rs.close;
```

---

## Пример 32: `CheckTaxPropForUfebsMes`

**Источник:** `Mac/Cb/pmtax.mac`
**Тип:** `macro`
**Размер:** 57 строк

```rsl
macro CheckTaxPropForUfebsMes
( Payment : RsbPayment,
  MesForm : string,
  ErrMsg : @string

) : integer

  execSQL("delete from dpmmeschk_tmp");

  var params : TArray = makeArray
  ( SQLParam( "p_Type", MesForm ),
    SQLParam( "p_PaymentID", Payment.PaymentID ),
    SQLParam( "p_DocKind", Payment.DocKind ),
    SQLParam( "p_RmNumber", Payment.Number ),
    SQLParam( "p_RmDate", Payment.Date ),
    SQLParam( "p_PayerINN", Payment.PayerINN ),
    SQLParam( "p_ReceiverINN", Payment.ReceiverINN ),
    SQLParam( "p_TaxAuthorState", Payment.TaxAuthorState ),
    SQLParam( "p_BTTTICode", Payment.BTTTICode ),
    SQLParam( "p_OkatoCode", Payment.OkatoCode ),
    SQLParam( "p_TaxPmDate", Payment.TaxPmDate ),
    SQLParam( "p_TaxPmNumber", Payment.TaxPmNumber ),
    SQLParam( "p_PartPaymDateMain", Payment.PartPaymDateMain),
    SQLParam( "p_UIN", Payment.UIN ),
    SQLParam( "p_PayerAccount", Payment.PayerAccount ),
    SQLParam( "p_ReceiverAccount", Payment.ReceiverAccount),
    SQLParam( "p_TaxPmGround", Payment.TaxPmGround),
    SQLParam( "p_TaxPmPeriod", Payment.TaxPmPeriod),
    SQLParam( "p_ReceiverBankID", Payment.ReceiverBankID),
    SQLParam( "p_ReceiverCorrAccNostro", Payment.ReceiverCorrAccNostro),
    SQLParam( "p_PrimDocOrigin", Payment.PrimDocOrigin),
    SQLParam( "p_Ground", Payment.Ground),
    SQLParam( "p_ReceiverName", Payment.ReceiverName),
    SQLParam( "p_TaxOperID", Payment.TaxOperID)
  );

  var retval : integer = execStoredFunc( "RSI_PM_TAXPROP.CheckTaxPropForUfebsMesRSL", V_INTEGER, params );
  if( retval )
    var rs = execSQLselectPrm( "select t_ErrMes, NVL(t_ShortErrMes, CHR(1)) ShortErrMes from dpmmeschk_tmp "
                                 " where t_PaymentID = :PaymentID ",
                                 SQLParam("PaymentID", Payment.PaymentID) );
    if(rs and rs.moveNext())
      ErrMsg = rs.value("ShortErrMes");

      Payment.Notes.DelNote( NOTEKIND_PAYM_TAXWARNING );
      Payment.Notes.AddNote( NOTEKIND_PAYM_TAXWARNING, SubStr(StrSubst(rs.value("t_ErrMes"), "|", "\n"), 1, 1499));
      if ( not IsOperationRunning() )
        Payment.Notes.Save();
      end;
    end;

  else
    Payment.Notes.DelNote( NOTEKIND_PAYM_TAXWARNING );
    if ( not IsOperationRunning() )
      Payment.Notes.Save();
    end;
  end;
```

---

## Пример 33: `Блок`

**Источник:** `Mac/DEPOSITR/PrepareFNSPercentInfo.mac`
**Тип:** `block`
**Размер:** 10 строк

```rsl
        for (var i, 0, period - BEG_DATE_FNS)
            var curPeriod = BEG_DATE_FNS + i;
            var statusString = "";
            var cmd = RsdCommand("BEGIN ? := rsu_rtlfns.CorrectFNSPercentInfo(?, ?, ?); END;");
            cmd.addParam("retVal",    RSDBP_RETVAL, V_INTEGER);
            cmd.addParam("period",    RSDBP_IN,     String(curPeriod));
            cmd.addParam("beginDate", RSDBP_IN,     Date(1, 1, curPeriod));
            cmd.addParam("endDate",   RSDBP_IN,     Date(31, 12, curPeriod));
            cmd.NullConversion = true;
            cmd.execute();
```

---

## Пример 34: `Блок`

**Источник:** `Mac/DLNG/IR/ir_inboundmsg.mac`
**Тип:** `block`
**Размер:** 10 строк

```rsl
  var params:TArray = TArray();
  params[0] = SQLParam( "p_Date"    , {curdate} ); 
  params[1] = SQLParam( "p_IR_OP_ID", ir_op.rec.ID ); 
  params[2] = SQLParam( "p_op_Kind",  ir_op.rec.DocKind ); 
  params[3] = SQLParam( "p_oper",     {oper} ); 
  params[4] = SQLParam( "p_LogHeader",Header ); 
//debugbreak;
  var stat:integer = execStoredFunc( "RSP_REPOSITORY.GetIncomingSRS", V_INTEGER, params );
/*
  if( (not stat) )
```

---

## Пример 35: `UpdateSfRepAcc`

**Источник:** `Mac/Cb/sfopr.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro UpdateSfRepAcc(SfDefComRec, Comment)

  var strQuery = "", cmd;  

  strQuery = "UPDATE DSFREPACC_TMP SET T_COMMENT = ?, T_ERRORCODE = 1 WHERE T_BEGINDATE = ?  AND T_CONTRID = ? AND T_FEETYPE = ? AND T_COMISSNUMBER = ? AND (T_ERRORCODE IS NULL OR T_ERRORCODE = 0)";
             
  cmd = RsdCommand( strQuery );

  cmd.addParam( "", RSDBP_IN, substr(Comment, 1, 256) );
  cmd.addParam( "", RSDBP_IN, SfDefComRec.DatePeriodBegin );
  cmd.addParam( "", RSDBP_IN, SfDefComRec.SfContrID       );
  cmd.addParam( "", RSDBP_IN, SfDefComRec.FeeType         );
  cmd.addParam( "", RSDBP_IN, SfDefComRec.CommNumber      );

  cmd.execute();
  
end;
```

---

## Пример 36: `ShowMenu`

**Источник:** `Mac/Cb/bbbodoc.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
  macro ShowMenu( DebetCredit:integer ):integer
    return ConfWin( IfThenElse( DebetCredit == PRT_Debet, 
                                makeArray( "Ошибка в распределении суммы по дебету. Сохранить?"  ),
                                makeArray( "Ошибка в распределении суммы по кредиту. Сохранить?" ) ),
                    makeArray( " Да", " Нет" )
                  );
  end;
```

---

## Пример 37: `InsKvit`

**Источник:** `Mac/DLNG/DV/dvautokvit.mac`
**Тип:** `macro`
**Размер:** 18 строк

```rsl
MACRO InsKvit(DealID, PlanPaymID, FactPaymID, KvitAmount, DocKind, Auto, Stat)
    var v_Stat = 0;
    if(Stat != null)
       v_Stat = Stat;
    end;

    VAR ins = RSDCommand("INSERT INTO ddv_kvit_tmp (t_dealid, t_planpaymid, t_factpaymid, t_kvitamount, t_dockind, t_auto, t_stat) VALUES (?,?,?,?,?,?,?)");
    ins.addParam("", RSDBP_IN, DealID);
    ins.addParam("", RSDBP_IN, PlanPaymID);
    ins.addParam("", RSDBP_IN, FactPaymID);
    ins.addParam("", RSDBP_IN, KvitAmount);
    ins.addParam("", RSDBP_IN, DocKind);
    ins.addParam("", RSDBP_IN, Auto);
    ins.addParam("", RSDBP_IN, v_Stat);
    ins.execute();

    //PRINTLN("DealID: " + DealID + "; PlanPaymID: " + PlanPaymID + "; FactPaymID: " + FactPaymID + "; KvitAmount: " + KvitAmount + "; Auto: " + Auto);
END;
```

---

## Пример 38: `GetAccountClaimListForAnaliticAcc`

**Источник:** `Mac/Cb/claim_utils.mac`
**Тип:** `macro`
**Размер:** 48 строк

```rsl
macro GetAccountClaimListForAnaliticAcc( v               : @TArray  // результирующий массив
                                        ,Account         : String  // - номер лицевого (сводного) счета 
                                        ,Chapter         : Integer //- глава лицевого (сводного) счета 
                                        ,Currency        : Integer  //- идентификатор финансового инструмента лицевого (сводного) счета 
                                        ,AnaliticAccount : Integer  // ID аналитическоко счета из прикладного кода
                                        ,BankDate        : Date     //  дата, за которую запрошены данные. 
                                       ) : integer
   if( ValType(BankDate) != V_DATE ) BankDate = {curdate}; end;

   var q = "SELECT cl.t_ClaimID                           "+
           "  FROM daccount_dbt ac, dacclaim_dbt cl       "+
           "       INNER JOIN dacclaimstate_dbt st        "+
           "               ON cl.t_ClaimID = st.t_ClaimID "+
           " WHERE ac.t_Chapter = ? AND ac.t_Account = ? AND ac.t_Code_Currency = ? "+
           "   AND cl.t_AccountID = ac.t_AccountID AND cl.t_AnaliticAccount = ? "+
           "   AND st.t_State IN( :ACCLAIM_STATUS_ACTIVE, :ACCLAIM_STATUS_MODIFIED, :ACCLAIM_STATUS_STOPED) "+
           "   AND st.t_StateDate=                        "+
           "      (SELECT max(t.t_StateDate) FROM dacclaimstate_dbt t        "+
           "        WHERE t.t_ClaimID = cl.t_ClaimID AND t.t_StateDate <= ?) "+
           " GROUP BY cl.t_ClaimID                        ";

  var params = makeArray( SQLParam( "", Chapter  ),
                          SQLParam( "", Account  ),
                          SQLParam( "", Currency ),
                          SQLParam( "", AnaliticAccount ),
                          SQLParam( "ACCLAIM_STATUS_ACTIVE",   1 ),
                          SQLParam( "ACCLAIM_STATUS_MODIFIED", 2 ),
                          SQLParam( "ACCLAIM_STATUS_STOPED",   3 ),
                          SQLParam( "", BankDate ));

  var rs = execSQLselect( q, params, FALSE );

  var stat=0;

  v = TArray();
  while(rs.moveNext())
     acclaim.rec.ClaimID =  rs.value(0);
     if(acclaim.GetEQ)
        v[v.size]              = CCLAIMLIST_ANALITICA();
        v[v.size-1].acclaim_buf=TRecHandler("acclaim.dbt");
        copy(v[v.size-1].acclaim_buf, acclaim);
        v[v.size-1].v_acclaimstate = TArray();
        stat = set_array_acclaimstate( acclaim.rec.ClaimID, @(v[v.size-1].v_acclaimstate));
     else
        stat=1;
        break;
     end;
  end;
```

---

## Пример 39: `InsertDAVRREST`

**Источник:** `Mac/DLNG/SECUR/Convert/2728_OutAccData.mac`
**Тип:** `macro`
**Размер:** 30 строк

```rsl
  macro InsertDAVRREST( Department, FIID, BuyGoal, Portfolio, Amount, BalAcc, BalAccRest, OutAcc, OutAccRest, NKDAcc, NKDAccRest, Cost )
    var cmd, i = 0;

     cmd = RsdCommand( "insert into davrrest_buf ( t_Department, t_FIID, t_BuyGoal, t_Portfolio, t_Amount, t_BalAcc, t_Balance, t_OutAcc, t_Outlay, t_NKDAcc, t_NKD, t_Cost ) " +
                       "                  values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ) " );
     cmd.NullConversion = true;

     cmd.addParam( "", RSDBP_IN, Department );
     cmd.addParam( "", RSDBP_IN, FIID );
     cmd.addParam( "", RSDBP_IN, BuyGoal );
     cmd.addParam( "", RSDBP_IN, Portfolio );
     cmd.addParam( "", RSDBP_IN, Amount );
     cmd.addParam( "", RSDBP_IN, BalAcc );
     cmd.addParam( "", RSDBP_IN, BalAccRest );
     cmd.addParam( "", RSDBP_IN, OutAcc );
     cmd.addParam( "", RSDBP_IN, OutAccRest );
     cmd.addParam( "", RSDBP_IN, NKDAcc );
     cmd.addParam( "", RSDBP_IN, NKDAccRest );
     cmd.addParam( "", RSDBP_IN, Cost );

     cmd.execute();


     Message( "Выгружен счет: " + BalAcc + " остаток: " + string(BalAccRest) + "\nОстаток стоимости покупки: " + string(Cost) );
          
     OnError(err);

     Message( "!!! Ошибка при сохранении счета: " + BalAcc + " остаток: " + string(BalAccRest) );

  end;
```

---

## Пример 40: `CalculateBaseSum_DC`

**Источник:** `Mac/DLNG/SECUR/SCPeriodComm.mac`
**Тип:** `macro`
**Размер:** 139 строк

```rsl
  MACRO CalculateBaseSum_DC( BeginDate:DATE, EndDate:DATE ):BOOL
     VAR cmd, rs, ClientID, DateCond = "", query_com = "", query_total = "", ЗаданМоментРасчета = false;

     if( (EndDate == NULL) OR (EndDate == DATE(0,0,0)) )
        EndDate = BeginDate;
     end;

     if( this.МоментРасчета_2( COMM_IN_COMPAYDATE ) )
        DateCond = " AND tick.t_CommDate = ? ";
        ЗаданМоментРасчета = true;
     elif( this.МоментРасчета_2( COMM_IN_DELIVERYDATE ) )/*"дата поставки"*/
        DateCond = " AND RQ_avr.t_PlanDate = ? ";
        ЗаданМоментРасчета = true;
     elif( this.МоментРасчета_2( COMM_IN_PAYDATE ) )/*"дата оплаты"*/
        DateCond = " AND RQ_cur.t_PlanDate = ? ";
        ЗаданМоментРасчета = true;
     end;

     /*общая часть для 1 и 2 часте сделок*/
     query_com = "SELECT Leg.t_ID LegID, Leg.t_LegKind, tick.t_ClientID, tick.t_BrokerID, tick.t_PartyID, tick.t_IsPartyClient, "+
                 "       Leg.t_Registrar, Leg.t_RegistrarContrID, leg.t_PayRegTax, "+
                 "             Leg.t_RejectDate, "
                 "       RQ_cur.t_Amount BaseSum, RQ_cur.t_FIID BaseSumFIID "+
                 "  FROM ddl_tick_dbt tick, ddl_leg_dbt Leg, DDLRQ_DBT RQ_avr, ddlrq_dbt RQ_cur "+
                 " WHERE     tick.t_BofficeKind = ? " +/*пока только по сделкам (уточнила, что паи , погашения не нужны)*/
                 "       AND tick.t_DealStatus  != ? " +
                 "       AND tick.t_DealDate    >= ? " +
                 "       AND Leg.t_DealID       = tick.t_DealID " +
                 "       AND Leg.t_LegKind      = ? "+
                 "       AND Leg.t_LegID        = 0 " +
                 "       AND RQ_cur.t_DocKind   = tick.t_BofficeKind " +
                 "       AND RQ_cur.t_DOCID     = tick.t_DealID " +
                 "       AND RQ_cur.t_DEALPART  = ? " + 
                 "       AND RQ_cur.t_Type      = "+DLRQ_TYPE_PAYMENT+ 
                 "       AND RQ_cur.t_SUBKIND   = " +DLRQ_SUBKIND_CURRENCY+
                 "       AND RQ_avr.t_DocKind   = tick.t_BofficeKind " +
                 "       AND RQ_avr.t_DOCID     = tick.t_DealID " +
                 "       AND RQ_avr.t_DEALPART  = RQ_cur.t_DEALPART " + 
                 "       AND RQ_avr.t_Type      = "+DLRQ_TYPE_DELIVERY+ 
                 "       AND RQ_avr.t_SUBKIND   = " +DLRQ_SUBKIND_AVOIRISS+
                 "       AND ( RSB_SECUR.GetSfContrID(tick.t_DealID) = ? or "+/*основной договор по сделке(НБ с биржей\брокером\посредником или Клиента с НБ)*/
                 "             (tick.t_ClientID <= 0 and (Leg.t_RegistrarContrID = ? and Leg.t_PayRegTax = 'X')) or "+/*регистратору по 1 или 2 ч*/
                 "             RSB_SECUR.GetSfContrID(tick.t_DealID,tick.t_PartyID) = ? "+/*с клиентом-контрагентом*/
                 "                ) "+
                 "       and ( tick.t_ClientID > 0 or " +
                 "             NVL((SELECT count(1) " +
                 "                    FROM dpmwrtsum_dbt s"+
                 "                        WHERE s.t_DocKind   = ? "+
                 "                     AND s.t_DocID     = RQ_avr.t_ID "+
                 "                     AND s.t_DealID    = RQ_avr.t_DOCID "+
                 "                     AND s.t_DealID    = tick.t_DealID "+
                 "                     AND s.t_State != ?),0) = 0 "+/*проверили, что лот 1 или 2ч НБ или Клиента не существует или не поставлен*/
                 "           ) " +DateCond;

     if(GlobalDealIDForCalc > 0)
       query_com = query_com + " and tick.t_DealID = ? ";
     end;

     query_total = query_com +
                   " union all "+
                   query_com +
                   " AND leg.t_PayRegTax = 'X' "+
                   " AND leg.t_RegistrarContrID > 0 ";
        
     cmd = DL_RSDCommand();                                                                                              

     cmd.addParam(DL_SECURITYDOC);
     cmd.addParam(DL_CLOSED);     
     cmd.addParam(BeginDate);
     cmd.addParam(LEG_KIND_DL_TICK);/*1ч*/
     cmd.addParam(1);/*1ч*/
     cmd.addParam(this.rContr.rec.ID ); 
     cmd.addParam(this.rContr.rec.ID ); 
     cmd.addParam(this.rContr.rec.ID ); 

     cmd.addParam(DLDOC_PAYMENT ); 
     cmd.addParam(PM_WRTSUM_NOTFORM );
        
     if( ЗаданМоментРасчета )
        cmd.addParam(EndDate );        
     end;

     if(GlobalDealIDForCalc > 0)
       cmd.addParam(GlobalDealIDForCalc);
     end;

     cmd.addParam(DL_SECURITYDOC);
     cmd.addParam(DL_CLOSED);     
     cmd.addParam(BeginDate);
     cmd.addParam(LEG_KIND_DL_TICK_BACK);/*2ч*/
     cmd.addParam(2);/*2ч*/
     cmd.addParam(this.rContr.rec.ID ); 
     cmd.addParam(this.rContr.rec.ID ); 
     cmd.addParam(this.rContr.rec.ID ); 

     cmd.addParam(DLDOC_PAYMENT ); 
     cmd.addParam(PM_WRTSUM_NOTFORM );
        
     if( ЗаданМоментРасчета )
        cmd.addParam(EndDate );        
     end;

     if(GlobalDealIDForCalc > 0)
       cmd.addParam(GlobalDealIDForCalc);
     end;

     rs = cmd.execute(query_total);

     while( rs.MoveNext() )
        if( (this.rComiss.rec.Code == ВТБДепо) and (rs.PayRegTax == SET_CHAR) )

          if( ((rs.ClientID <= 0) and (this.rComiss.rec.ReceiverID == rs.Registrar) and (this.rContr.rec.ID == rs.RegistrarContrID)) OR 
              ( (rs.ClientID > 0) and 
                ((this.rComiss.rec.ReceiverID == rs.Registrar) and (rs.RegistrarContrID > 0))
            )
            )
             /*сохраняем по части сделки (1 или 2)*/
             if( InsertBaseSum( rs.LegKind, rs.LegID, rs.BaseSum, rs.BaseSumFIID ) != true )
                return false;
             end;
          end;
        elif((rs.LegKind == LEG_KIND_DL_TICK) and/*только по 1 ч сделки*/
             ( (this.rComiss.rec.Code == БрокерНов) and (GetPartyContrCode( rs.BrokerID ) == BROKER_CODE) and (this.rComiss.rec.ReceiverID == rs.BrokerID) and
              ( ((rs.ClientID > 0) and (this.rContr.rec.ContractorID == {OurBank}))/*для клиенской*/ or ( (rs.ClientID <= 0) and (this.rComiss.rec.ReceiverID == this.rContr.rec.ContractorID) )/*для своих сделок*/)
            )
            )
           /*сохраняем 1 часть сделки (по комиссии НЕ регистратору всегда по 1 части)*/
           if( InsertBaseSum( rs.LegKind, rs.LegID, rs.BaseSum, rs.BaseSumFIID ) != true )
              return false;
           end;
        else
           if( InsertBaseSum( rs.LegKind, rs.LegID, rs.BaseSum, rs.BaseSumFIID ) != true )
              return false;
           end;
        end;
     end;

     return true;
  END;
```

---
