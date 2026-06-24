# Практика: SQL-запросы и работа с наборами данных (RsdRecordSet, RsdCommand)

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

## Пример 2: `GetOkatoList`

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

## Пример 3: `ОбработатьСчет`

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

## Пример 4: `isNewDirection`

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

## Пример 5: `SfFormDocumentsBatch`

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

## Пример 6: `ExecuteStep`

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

## Пример 7: `Charge_Batch`

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

## Пример 8: `ОбработкаПортфеля`

**Источник:** `Mac/Cb/form_res.mac`  
**Тип:** `macro`  
**Размер:** 49 строк

```rsl
macro ОбработкаПортфеля( _AcCase, _AcCaseParm, _AcCaseSubCase )
  
  var stat : bool;
  record AcCase(accase);
  record AcCaseParm(accasepm);
  record AcCaseSubCase(accasscs);

  var caseResObj : CalcReserveAccCase;
  var ReserveAccount : string;
  var query, rs;
  var params : TArray;
  var ReserveType : integer;
  /*Значения процентов резервирования и категорий качества в текущем формировании*/
  var RiskGroup      : integer;
  var ReservePercent : double;
  /*Классификации резервов*/
  var ClassifReserveLoss     : string;
  var ClassifReserveLoans    : string;
  /*Даты послених расчетов по видам резервов*/
  var LastDateCalcReserveLoss : date;
  var LastDateCalcReserveLoans : date;
  /*Признаки изменения параметров для видов резерва*/
  var ChangedLoss     : bool;
  var ChangedLoans    : bool;
  var ChangedEstimated : bool;
  var HasAccTransactions : bool;

  SetBuff( AcCase        , _AcCase        );
  SetBuff( AcCaseParm    , _AcCaseParm    );
  SetBuff( AcCaseSubCase , _AcCaseSubCase );

  stat = true;

  ChangedLoss     = true;
  ChangedLoans    = true;
  ChangedEstimated = true;

  InitReserveSum();

  ReserveAccount = GetAccountReserveForCase(AcCase, AcCaseSubCase);

  LastDateCalcReserveLoss = GetCaseLastDateCalcReserveLoss(UniID(AcCaseSubCase, 0, DOCKIND_SUBCASE));
  LastDateCalcReserveLoans = GetCaseLastDateCalcReserveLoans(UniID(AcCaseSubCase, 0, DOCKIND_SUBCASE));

  if (LastDateCalcReserveLoss != null)
    HasAccTransactions = GetHasAccTransactionsForCase(AcCase, AcCaseSubCase, LastDateCalcReserveLoss);
  else
    HasAccTransactions = GetHasAccTransactionsForCase(AcCase, AcCaseSubCase, LastDateCalcReserveLoans);
  end;
```

---

## Пример 9: `_ExecuteDepoAcc`

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

## Пример 10: `formingUNRZEx`

**Источник:** `Mac/Cb/ptgfias.mac`  
**Тип:** `private macro`  
**Размер:** 39 строк

```rsl
private macro formingUNRZEx( ptaddress, mode, status_:@integer, prnMess, retUNRZ:@string, placeFld )
  var i;
  var Text;
  var Result;
  array ButtonCCC;
  array ButtonCC;
  array ButtonC;
  array TextCC;
  var ColumnsR  : TArray = TArray;
  var ColumnsPr : TArray = TArray;
  var ColumnsD  : TArray = TArray;
  var ColumnsP  : TArray = TArray;
  var ColumnsPn : TArray = TArray;
  var ColumnsS  : TArray = TArray;
  var ColumnsH  : TArray = TArray;

  var TempUNRZ, TempPostIndex, TempOkato, TempOktmo, TempFiasGuid, TempCadastral;
  var TempObjectID;
  var Region  , CodeRegion  , newRegion  , newCodeRegion  , newRegionNum,
      Province, CodeProvince, newProvince, newCodeProvince,
      District, CodeDistrict, newDistrict, newCodeDistrict,
      Place   , CodePlace   , newPlace   , newCodePlace   ,
      Plan    , CodePlan    , newPlan    , newCodePlan    ,
      Street  , CodeStreet  , newStreet  , newCodeStreet  ;
  var HouseType, House, HouseType1, NumCorps, HouseType2, Building, 
      newHouseType, newHouse, newHouseType1, newNumCorps, newHouseType2, 
      newBuilding, newStead, newSteadType, newApartType, newFlat;
  var SteadNumber, Flat, GFiasApartType;
  var tmpStatus = 1;//status_;

  var stat, cmd, rs;

  var query;
  var params : TArray;

  macro EvProc( rs, cmd, id, key )
    if(( cmd == DLG_KEY ) and ( key == 13 ))
      return CM_SELECT;
    end;
```

---

## Пример 11: `CloseZeroAccounts`

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

## Пример 12: `CalcDepoCommReserveByAcc`

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

## Пример 13: `AmountReserveRevaluation`

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

## Пример 14: `ExecuteStep`

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

## Пример 15: `PrepMassExecuteStep`

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

## Пример 16: `AddWhereForClientFld`

**Источник:** `Mac/DLNG/NotifContrDeal_Form.mac`
**Тип:** `macro`
**Размер:** 19 строк

```rsl
MACRO AddWhereForClientFld( _date )
  var AddWhere:String = "";

  AddWhere = " EXISTS( SELECT attr.* " +
             "           FROM dobjatcor_dbt attr " +
             "          WHERE attr.t_ObjectType = " + string(OBJTYPE_PARTY) +
             "            AND attr.t_GroupID    = 58 " + 
             "            AND attr.t_Object     = LPAD(t.T_PARTYID, 10, '0') " +
             "            AND (SELECT count(1) " +
             "                   FROM DOBJATCOR_DBT at " +
             "                  WHERE at.t_ObjectType = attr.t_ObjectType " +
             "                    AND at.t_GroupID    = attr.t_GroupID " +
             "                    AND at.t_Object     = attr.t_Object " +
             "                    AND at.t_ValidFromDate <= " + GetSQLDate( _date ) +
             "                 ) > 0 " +
             "       ) ";

  return AddWhere;
END;
```

---

## Пример 17: `GetFactDateForAccOpen`

**Источник:** `Mac/Mbr/fnsaccmsg_lib.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro GetFactDateForAccOpen( buff ) : date

  var rs = execSQLselectPrm( " select st.t_Fact_Date " 
                             "   from doprstep_dbt st, "
                             "        doproper_dbt opr "
                             "  where opr.t_DocumentID = lpad(:DocID, 34, '0') "
                             "    and opr.t_DocKind = :ACCOPEN_KIND "
                             "    and st.t_Id_Operation = opr.t_Id_Operation "
                             "    and st.t_IsExecute = chr(88) "
                             "    and st.t_Kind_Action = 100 ", //REQOPENA_OPENACC
                             SQLParam("DocID", buff.RequestID),
                             SQLParam("ACCOPEN_KIND", PS_REQOPENA)
                           );

  if ( rs and rs.moveNext() )
    return rs.value(0);
  end;
```

---

## Пример 18: `Charges7_pacs_AddXml`

**Источник:** `Mac/Mbr/swmx_pacs_genmes.mac`
**Тип:** `macro`
**Размер:** 31 строк

```rsl
macro Charges7_pacs_AddXml
( Node : XMLMesDocument, // parent node
  NewNodeName : string,
  ComissObj : TDataCharges7,
  PaymentID : integer
) : string // возвращает xml-строку для созданного узла

  var NewNodeXmlStr : string = "";
  var savePos : SavePositionInXmlDocument = SavePositionInXmlDocument(Node);

  Node.AddChildNode(NewNodeName, "", true);

  // node Amt
  SWIFTMX_FillXmlDocByActiveCurrencyAndAmount(Node, "Amt", ComissObj.Amount, ComissObj.FIID );

  // node Agt
  var CorrID : integer = 0;
  var rs = execSQLselectPrm
    ( "Select cs.t_CorrID "
      "  from dpmprop_dbt outprop, dcorschem_dbt cs "
      " where outprop.t_PaymentID = :PaymentID "
      "   and outprop.t_Group = " + PAYMENTS_GROUP_EXTERNAL +
      "   and outprop.t_IsSender = chr(0) "
      "   and cs.t_Number = outprop.t_Corschem "
      "   and cs.t_FIID = outprop.t_PayFIID "
      "   and cs.t_FI_Kind = " + FIKIND_CURRENCY,
      SQLParam("PaymentID", PaymentID)
    );
  if(rs.moveNext())
    CorrID = rs.value("t_CorrID");
  end;
```

---

## Пример 19: `ExecuteStep`

**Источник:** `Mac/DLNG/VA/vadlrsrv.mac`
**Тип:** `macro`
**Размер:** 133 строк

```rsl
MACRO ExecuteStep(Buffer, FirstDoc)
var AttrID = 0, ReserveKind = 0, fd,
    stat = 0, ErrMsg = "", СуммаСделки = $0,
    f_overdue = false, // флаг переноса на просрочку
    have_reslnk = true,
    DataSet,
    reslnk = TBfile("dlreslnk.dbt", "W", 0),
    FstBai = TBfile("pmpaym.dbt"),  /* первый платеж по активу сделки */
    FstCai = TBfile("pmpaym.dbt");  /* первый платеж по контрактиву сделки */
var Rold = 0, ResLnkId = 0, КатегКачества = -1, ПроцРезерва = -1;

    SetBuff( tick, FirstDoc );

    OprDate = OprServDoc.ValueDate;

    // всё основные проверки отрабатывают в VA_SvOpFilter

    if(not VA_Get1stPlanPaym(tick.BofficeKind, tick.DealID, BAi, FstBai))
       return SayDlReserveError( tick, 1, "Не найден платеж по базовому активу сделки" );
    elif(not VA_Get1stPlanPaym(tick.BofficeKind, tick.DealID, CAi, FstCai))
       return SayDlReserveError( tick, 1, "Не найден платеж по контрактиву сделки" );
    end;

     // 1. Определяем необходимость создания и вид резерва.
     if(VA_IsBuy(tick.DealType))    // покупка
        ReserveKind = RVKIND_PAYM;
        if(FstBai.rec.PaymStatus == PM_OVERDUE)
            f_overdue = true;
        end;
     elif(VA_IsSale(tick.DealType))   // продажа
        ReserveKind = RVKIND_PAYM;
        if(FstCai.rec.PaymStatus == PM_OVERDUE)
           f_overdue = true;
        end;
     else
        return stat; // мену не учитываем
     end;

     stat = VA_GetReserveParamDeal(tick, OprDate, 0, @КатегКачества, @ПроцРезерва, @ResLnkId, @ErrMsg);
     if(stat != 0)
        if(ErrMsg != "")
           SayDlReserveError(tick, stat, ErrMsg);
        end;
        return stat;
     end;

     // 3. Рассчитывается новая сумма резерва Rnew - в валюте расчетов сделки
     if(ReserveKind == RVKIND_PAYM)
        stat = VA_CalcNewReserveDeal(tick, ПроцРезерва, FstCai.rec.PayFIID, OprDate, @reserve_sum, @ErrMsg);
     end;
     if(stat != 0)
        if(ErrMsg != "")
           SayDlReserveError(tick, stat, ErrMsg);
        end;
        return stat;
     end;

     // 5. Определяется Rold
     DataSet = TRsbDataSet("SELECT t_ReserveAmount " +
        " FROM ddlreslnk_dbt " +
        " WHERE t_Type = 1 AND t_ParentID = " + tick.DealID + " AND t_ChildID > -1 "
          " AND t_LnkDate <= to_date('" + OprDate + "', 'DD.MM.YYYY')" +
        " ORDER BY t_Id DESC ");
     if(DataSet.MoveNext())
        Rold = DataSet.ReserveAmount;
     end;

     // 6. Определяется сумма корректировки резерва
     delta = reserve_sum - Rold;
     if(delta == 0)
        return stat;
     end;

     // 7/10. Обновление/вставка связи со сделкой
     reslnk.KeyNum = 0;
     reslnk.clear();
     reslnk.rec.Id = ResLnkId;
     if(not reslnk.GetEQ)
         have_reslnk = false;
     end;

     reslnk.rec.ReserveKind = ReserveKind;       // Вид резерва
     reslnk.rec.ReserveAmount = reserve_sum;     // Сумма резерва
//     reslnk.rec.ReserveDate = OprDate;           // Дата расчета резерва

     if(have_reslnk AND (reslnk.rec.ChildID == -1) AND //!!!
             (КатегКачества == reslnk.rec.QualityCategory) AND
             (ПроцРезерва == reslnk.rec.ReservePercent))
        reslnk.rec.ChildID = OprServDoc.Id;
        VA_ChangeDLRESLNK(reslnk.rec.Id, reslnk.rec.ChildID, reslnk.rec.ReserveKind, reslnk.rec.ReserveAmount, OprDate);
     else
        reslnk.rec.Id = 0;
        reslnk.rec.ParentID         = tick.DealID;
        reslnk.rec.ChildID          = OprServDoc.Id;
        reslnk.rec.Type             = RSRV_TYPE_VADEAL;
        reslnk.rec.LnkDate          = OprDate;
        reslnk.rec.QualityCategory  = КатегКачества;
        reslnk.rec.ReservePercent   = ПроцРезерва;
        reslnk.rec.ReserveDate      = OprDate;            // Дата расчета резерва
        VA_InsertDLRESLNK(reslnk);
     end;

     fd = VATickFD(tick);
     // 8. Проводка по списанию резерва
     if(reserve_sum == 0)
        if(Rold > 0)
           stat = СписРезерваПоСделке(fd, Rold, OprDate, @ErrMsg);
        end;
        if(stat != 0)
            if(ErrMsg != "")
               SayDlReserveError(tick, stat, ErrMsg);
            end;
        end;
     else // (reserve_sum != 0)
     // 9. Проводки по изменению
        if(f_overdue == true)
           if(Rold > 0)
              stat = СписРезерваПоСделке(fd, Rold, OprDate, @ErrMsg);
           end;
           if(stat != 0)
              if(ErrMsg != "")
                 SayDlReserveError(tick, stat, ErrMsg);
              end;
              return stat;
           end;
           stat = ФормРезерва(fd, Abs(reserve_sum), FIROLE_DEALS_OVERDUE);
        else
           stat = ФормРезерва(fd, delta, FIROLE_DEALS_TERMREQ);
        end;
     end;

     return stat;
END;
```

---

## Пример 20: `GetNRCountryForParty`

**Источник:** `Mac/DEPOSITR/retoprce.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro GetNRCountryForParty ( codeClient )

  var cmd, rs;
  var nrCountry = "";

  cmd = RsdCommand ( "select t_nrcountry from dparty_dbt where t_partyid = ?" );
                     
  rs = RsdRecordset( cmd );
  cmd.addParam( "partyid", RSDBP_IN, codeClient ); 
  cmd.execute;
  
  if ( rs.moveNext( ) )
    nrCountry = rs.value( "t_nrcountry" );
  end;
```

---

## Пример 21: `IsClaimByOperStep`

**Источник:** `Mac/Cb/cbsttls.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro IsClaimByOperStep(ID_Operation:integer)

  var params:TArray;
  var rs:object;
  var select = "SELECT 1 "+
               "FROM dual "+
               "WHERE EXISTS( "+
                  "SELECT 1 "+
                  "FROM doprdocs_dbt opd "+
                  "WHERE opd.t_id_operation = :ID_Operation "+
                  "AND opd.t_dockind = 976) "/*DOCKIND_ACCLMCNG*/;
  params = makeArray( SQLParam("ID_Operation", ID_Operation));
  rs = execSQLselect( select, params, FALSE );
  if(rs and rs.moveNext())
    return true;  
  end;
```

---

## Пример 22: `Блок`

**Источник:** `Mac/DLNG/dlgenagrsc.mac`
**Тип:** `block`
**Размер:** 13 строк

```rsl
/* Макрофункция инициализации нового актива 
   необходимо заполнить структуру "Документ"
   возвращаемое значение
   0 - ошибок не было
   1 - была ошибка
*/
private macro Связанные_сделки()  
  var res = 0;
  var querySql, query;
  var GenAgrId = СтарыйДокумент.rec.GenAgrId;
  querySql = "SELECT COUNT(*) AS t_cnt FROM DV_ALLDEAL deals, DDL_GENAGR_DBT genagr"
            +" WHERE genagr.T_GENAGRID = deals.T_GENAGRID"
            +" AND   genagr.T_GENAGRID = ? ";
```

---

## Пример 23: `GetChgAvrCount`

**Источник:** `Mac/DLNG/SECUR/ws_chgavr.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
macro GetChgAvrCount(
  FilterItems//:TArray of FilterCondItem // Массив элементов фильтра скроллинга
):Integer

  var result:integer = 0;
  var stat:integer = -1;
  var strAddWhere:string = "";

  var query =
     " SELECT COUNT(dl_comm.t_documentId) C "
     + " FROM ddl_comm_dbt dl_comm, "
          + " davrkinds_dbt avrkinds, "
          + " dfininstr_dbt fininstr, " 
          + " dparty_dbt party "
     + " WHERE dl_comm.t_dockind = " + string(DL_CHGAVRNOM/*139*/)
     +  " AND fininstr.t_FIID = dl_comm.t_FIID "
     +  " AND avrkinds.t_FI_Kind = " + string(FIKIND_AVOIRISS/*2*/)
     +  " AND avrkinds.t_AvoirKind = fininstr.t_AvoirKind AND party.t_PartyID=fininstr.t_Issuer";

  strAddWhere = GetChgAvrAddWhereCondition( FilterItems );
  if( strAddWhere != "" )
     query = query + " AND " + strAddWhere;
  end;
```

---

## Пример 24: `Проверить_ГенСоглашение`

**Источник:** `Mac/DLNG/dlgenagr.mac`
**Тип:** `macro`
**Размер:** 89 строк

```rsl
MACRO Проверить_ГенСоглашение (Режим)
    var stat = 0, rs = NULL, ObjType = NULL,
        sqlstr = "";

    if (Режим == DL_MAC_INIT)    
        ObjType = GetObjType(ГенСоглашение.DocKind);

        if (not DL_GenRefByTypeDoc(ObjType, ГенСоглашение.Code))
            msgbox("Ошибка при генерации номера генерального соглашения");
            stat = 1;
        end;

        cacheGenAgrCode = ГенСоглашение.Code;
        isRetRef        = true;
    elif (Режим == DL_MAC_DEINIT)    
        if (isRetRef)
            ObjType = GetObjType(ГенСоглашение.DocKind);
            DL_RestoreRefByTypeDoc(ObjType, cacheGenAgrCode);
        end;
    elif (Режим == DL_MAC_USER)    
        ФункцияПользователя_ГенСоглашение();
    elif ((Режим == DL_MAC_INSERT)or(Режим == DL_MAC_UPDATE))
        if (ГенСоглашение.Code == "")
            msgbox("Не задан номер ГС");
            return 1;
        end;

        sqlstr = "select Count(1)as cnt from ddl_genagr_dbt where t_Code = '" + ГенСоглашение.Code + 
                  "' and t_DocKind = " + ГенСоглашение.DocKind + " and t_GenAgrID <> " + ГенСоглашение.GenAgrID;
        rs = TRsbDataSet(sqlstr);      
        rs.MoveNext();
        if (rs.CNT > 0)
             msgbox("Ген. соглашение с таким номером уже введено");
             return 1;
        end;   

        if (ГенСоглашение.Start == date(0,0,0))
            msgbox("Не задана дата начала");
            return 1;
        end;

        if (ГенСоглашение.Duration == 0)
            msgbox("Срок ГС равен 0");
            return 1;
        end;

        if ((ГенСоглашение.PartyID == -1) and (ГенСоглашение.PartyGroup == 0))
            msgbox("Необходимо задать контрагента или группу контрагентов");
            return 1;
        end;
    elif (Режим == DL_MAC_DELETE)
        // 0 - проверка пошла успешно. не 0 - ошибка (ругаемся сами)
        if (ГенСоглашение.DocKind == 4610) // КО
            rs = TRsbDataSet("select count(1) as cnt from ddl_tick_dbt tick where tick.t_BOfficeKind = 100" +
                             " and tick.t_GenAgrID = " + ГенСоглашение.GenAgrID);
        elif (ГенСоглашение.DocKind == 4611) // МБК
            rs = TRsbDataSet("select count(1) as cnt from ddl_tick_dbt tick where tick.t_BOfficeKind = 102" +
                             " and tick.t_GenAgrID = " + ГенСоглашение.GenAgrID);
        elif (ГенСоглашение.DocKind == DL_GENAGRDVDOC) // ПИ
           rs = TRsbDataSet(" select count(1) as cnt " +
                            " from ( select deal.t_GenAgrID from ddvdeal_dbt deal where deal.t_GenAgrID = " + String(ГенСоглашение.GenAgrID) +
                            "        union " +
                            "        select ndeal.t_GenAgrID from ddvndeal_dbt ndeal where ndeal.t_GenAgrID = " + String(ГенСоглашение.GenAgrID) + " )");
        end;

        rs.MoveNext();
        if (rs.cnt > 0)
            msgbox("Удаление невозможно! Есть привязанные сделки");
            return 1;
        end;
    elif (Режим == DL_MAC_COMPLETE)
        // при вставке, если номер в кэше и документе совпадают, то откатывать референс не надо
        if (cacheGenAgrCode == ГенСоглашение.Code)
            isRetRef = false;
        end;
    elif (Режим == DL_MAC_NOTCOMPLETE)    
        // сообщение придет, когда мы в транзакции вставки или редактирования
        // возвращаемое значение не влияет
    elif (Режим == DL_MAC_CREATEOP)    
        // 0 - проверка пошла успешно. не 0 - ошибка (ругаемся сами)
    elif (Режим == DL_MAC_DELETEOP)    
        // 0 - проверка пошла успешно. не 0 - ошибка (ругаемся сами)
    elif (Режим == DL_MAC_MASSACTION)    
        // 1 раз приходит при вызове групповых действий
        // 2 раз - при завершении групповых действий
    end;

    return stat;
END;
```

---

## Пример 25: `CheckTYPEACCOUNT`

**Источник:** `Mac/DLNG/FOREX/fxlb.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
MACRO CheckTYPEACCOUNT(Account, symb)
    var ds;

    ds = TRsbDataSet("select * from daccount_dbt where (t_account = '" + Account + "')and(t_type_account like '%А%')");
    if (not ds.MoveNext())
        return false;
    end;

    return true;
END;
```

---

## Пример 26: `Операционист`

**Источник:** `Mac/DLNG/SECUR/ReportMoveBasketREPO_Report.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
  MACRO Операционист()
    var vRS = TRsbDataSet("SELECT person.t_Name " +
                         "  FROM dperson_dbt person " +
                         " WHERE person.t_oper = " + string({oper})
                        );

    if( vRS.MoveNext() )
      return vRS.Name;
    end;
    return "";
  END;
```

---

## Пример 27: `BnkFSSP_GetInternalKeyDocDate`

**Источник:** `Mac/Cb/pm_fssp.mac`
**Тип:** `macro`
**Размер:** 18 строк

```rsl
macro BnkFSSP_GetInternalKeyDocDate
( DocFSSPID : integer, 
  InternalKey : @string, 
  DocDate : @date
)
  var rs = execSQLselectPrm
    ( "Select t_InternalKey, t_DocDate "
      "  from dfssprequire_dbt "
      " where t_ID = :DocFSSPID ",
      SQLParam("DocFSSPID", DocFSSPID)
    );

  if(rs.moveNext())
    InternalKey = rs.value("t_InternalKey");
    DocDate = rs.value("t_DocDate");
  else
    RunError("Не найдена запись группового требования ИД=" + DocFSSPID);
  end;
```

---

## Пример 28: `Dcoup`

**Источник:** `Mac/DLNG/SECUR/OverSecReg_Report.mac`
**Тип:** `macro`
**Размер:** 30 строк

```rsl
  MACRO Dcoup():DATE //дата погашения купона, который гасится первым в период между <DDB>+1 и <H0.4> включительно
     if( m_Dcoup == null )
        m_Dcoup = date(0,0,0);

        if( FI_AvrKindsEQ( FIKIND_AVOIRISS, AVOIRISSKIND_BOND, m_RS.AvoirKind ) )

           VAR sql2   = RSDCommand( " SELECT t_DrawingDate " +
                                    "   FROM dfiwarnts_dbt " +
                                    "  WHERE t_FIID         =  ? AND " +
                                    "        t_IsPartial   != 'X' AND " +
                                    "        t_DrawingDate >=  ? AND " +
                                    "        t_DrawingDate <=  ? " +
                                    " ORDER BY t_DrawingDate ASC "
                                  );
          
           sql2.addParam( "", RSDBP_IN, m_RS.t_FIID );
           sql2.addParam( "", RSDBP_IN, this.DDB()+1 );
           sql2.addParam( "", RSDBP_IN, this.H0_4() );
           sql2.execute();
          
           VAR DataSet   = TRsbDataSet(sql2);
           if( DataSet.MoveNext() )
              m_Dcoup = SQL_ConvTypeDate( DataSet.t_DrawingDate );
           end;

        end;
     end;

     return m_Dcoup;
  END;
```

---

## Пример 29: `CreateOprKindFromAppServ`

**Источник:** `Mac/Cb/ws_oprkoper.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro CreateOprKindFromAppServ(KindOperation)
  var OprKindItem : TWsOprkoper = TWsOprkoper();

  var cmd : RsdCommand, dataSet;

  cmd.cmdText = "select t_name from doprkoper_dbt WHERE t_kind_operation = ?";

  cmd.AddParam("", RSDBP_IN,  KindOperation);

  cmd.execute();

  dataSet = RsdRecordset(cmd);

  if(dataSet.moveNext())
    OprKindItem.Name          = dataSet.value(0);
    OprKindItem.KindOperation = KindOperation;
  end;
```

---

## Пример 30: `SelectPacketNum`

**Источник:** `Mac/Cb/ws_masptdub.mac`
**Тип:** `macro`
**Размер:** 126 строк

```rsl
macro SelectPacketNum(taskID, execID, ConvTypeID, PacketSize, CheckParm)
  var cmd, cmd2,cmdS, rs, rs2;
  var sqlString;
  var PacketNum = 0;
  var PackID = 0;
  var PrevPackID = 0; 


  var PacketNumInst = 0; 
  var PacketNumPersn = 0;
  CreatePacketPartyWith(taskID, execID, ConvTypeID, CheckParm, @PacketNumInst, @PacketNumPersn );

  var cnvdocCache = RsbSQLInsert("cnvdoc.dbt");

  var LegalForm = PTLEGF_INST;
  var PacketSizePartyFrom = 1;
  var PacketSizePartyTo   = PacketNumInst;


  while(LegalForm <= PTLEGF_PERSN)
    
    cmd = RsdCommand();
    cmdS = RsdCommand();

    cmd.NullConversion = true;
    cmdS.NullConversion = true;

    
    if((PacketSizePartyFrom <= PacketSizePartyTo) AND (PacketSizePartyTo != 0) )
      var strFrom = " FROM dparty_dbt party "; //  ", dpartyown_dbt partyown"
      var strWhere =  " party.t_Locked <> 'X' and party.t_LegalForm = " + LegalForm +
                      " and party.t_IsProbDoubler <> 'X' and party.t_IsDoubler <> 'X' ";

      var StrDepList = GetDepartmentsStrList();

      if(CheckParm.FromClientDep)
        strWhere = strWhere + " AND EXISTS ( SELECT 1 ";
        strWhere = strWhere +  "  from dptsvdp_dbt ptsvdp ";
        strWhere = strWhere +  " where ptsvdp.t_PartyID = party.t_PartyID ";
        strWhere = strWhere +  "   and rownum <= 1 "; 
        strWhere = strWhere +  "   and ptsvdp.t_PartyKind = 1 ";  // PTK_CLIENT
        strWhere = strWhere +  "   and ptsvdp.t_Department in ( ";

        if(CheckParm.FromClientAllSubDep)
          strWhere = strWhere +  StrDepList;
        else
          strWhere = strWhere +  string({OperDprtNode});
        end;

        strWhere = strWhere +  " ) )";
      end;

      var  sqlCount = "SELECT COUNT(DISTINCT(party.t_PartyID)) as CountRec ";
      sqlCount = sqlCount + strFrom;

      if(strlen(strWhere) > 0)
        sqlCount = sqlCount + " WHERE " ;
        sqlCount = sqlCount + strWhere;
      end;

      cmd.CmdText = sqlCount;

      rs = RsdRecordset(cmd);

      var CountRec = 0;
      if( rs.moveNext() )
        CountRec = rs.value("CountRec");
      end;

      if( CountRec > 0 )
        sqlString = "SELECT DISTINCT party.t_PartyID AS PartyID ";
        sqlString = sqlString + strFrom;

        if(strlen(strWhere) > 0)
          sqlString = sqlString + " WHERE " ;
          sqlString = sqlString + strWhere;
        end;

        sqlString = sqlString + " ORDER BY PartyID ";

        cmdS.CmdText = sqlString;
        rs2 = RsdRecordset(cmdS);

        var RowNum = 1;
        var PackTmp = 1; // используется только для вставки пачки
        while( rs2.moveNext() )
          var PartyID = rs2.value("PartyID");

          var cnvdoc = TRecHandler("cnvdoc.dbt");
          ClearRecord( cnvdoc );

          cnvdoc.rec.TaskID     = taskID; 
          cnvdoc.rec.ExecID     = execID; 
          cnvdoc.rec.ConvTypeID = ConvTypeID;
          cnvdoc.rec.PackID     = 0; 
          cnvdoc.rec.ObjectType = 0;
          cnvdoc.rec.ObjectID   = PartyID;
          
          cnvdocCache.AddRecord( cnvdoc );

          if(RowNum > (PackTmp * PacketSize))
            PrevPackID = PackTmp;

            cnvdocCache.Insert();
            cnvdocCache = RsbSQLInsert("cnvdoc.dbt");
            CopyCnvDoc(taskID, execID, ConvTypeID, @PackID, PacketSizePartyFrom, PacketSizePartyTo); 
           
            PackTmp = PackTmp + 1; 
          end;
          RowNum = RowNum + 1;
        end;

        cnvdocCache.Insert();
        cnvdocCache = RsbSQLInsert("cnvdoc.dbt");
        CopyCnvDoc(taskID, execID, ConvTypeID, @PackID, PacketSizePartyFrom, PacketSizePartyTo);
     end;
    end;

    PacketSizePartyFrom = PacketNumInst+1;            
    PacketSizePartyTo   = PacketNumPersn;

    PacketNum = PackID;

    PackID = PackID + 1; // ЮЛ и ФЛ помещаем в разные пачки. 
    LegalForm = LegalForm + 1;
  end;
```

---

## Пример 31: `ПолучитьПоручения`

**Источник:** `Mac/DLNG/DV/dv_journl.mac`
**Тип:** `macro`
**Размер:** 57 строк

```rsl
macro ПолучитьПоручения( Client, SfContr )
  var sqlQueryOrder = "", 
      sqlQueryCarry = "";

  sqlQueryOrder = " SELECT 1 isOrder," +
                  "        ( SELECT Party.T_NAME FROM dparty_dbt Party WHERE Party.T_PARTYID = DVDeal.T_CLIENT ) ClientName," +
                  "        ( SELECT SfContr.T_NUMBER FROM dsfcontr_dbt SfContr WHERE SfContr.T_ID = DVPos.T_CLIENTCONTR ) SfContrName," +
                  "        ( SELECT SfContr.T_DATEBEGIN FROM dsfcontr_dbt SfContr WHERE SfContr.T_ID = DVPos.T_CLIENTCONTR ) SfContrDate," +
                  "        DVDeal.T_KIND OrderKind," +
                  "        DVDeal.T_POSITION POSITION," +
                  "        SpGround.T_REGISTRDATE OrderDate," +
                  "        SpGround.T_REGISTRTIME OrderTime," +
                  "        SpGround.T_XLD OrderNum," +
                  "        ( SELECT Person.T_NAME" +
                  "            FROM dperson_dbt Person" +
                  "           WHERE Person.T_Oper = DVDeal.T_Oper ) ProxyAgent " +
                  "   FROM ddvdeal_dbt DVDeal, ddvfipos_dbt DVPos, dfininstr_dbt ContrFI, dfideriv_dbt ContrDV, dspgrdoc_dbt SpGrDoc, dspground_dbt SpGround" +
                  "  WHERE (DVDeal.T_State = 1 or DVDeal.T_State = 2) and " +
                  "        ContrFI.T_FIID = DVDeal.T_FIID and " +
                  "        ContrDV.T_FIID = DVDeal.T_FIID and" +
                  "        DVPos.T_FIID = DVDeal.T_FIID and " +
                  "        DVPos.T_DEPARTMENT = DVDeal.T_DEPARTMENT and " +
                  "        DVPos.T_CLIENT = DVDeal.T_CLIENT and " +
                  "        DVPos.T_BROKER = DVDeal.T_BROKER and " + 
                  "        SpGrDoc.T_SOURCEDOCKIND = 192 and" +
                  "        SpGrDoc.T_SOURCEDOCID = DVDeal.T_ID and " +
                  "        SpGround.T_SPGROUNDID = SpGrDoc.T_SPGROUNDID and " +
                  "        SpGround.T_KIND = 251 " +
                  /*условия по датам*/
                  "        and SpGround.T_RegistrDate >= " + GetSQLDate( DateStart ) +
                  "        and SpGround.T_RegistrDate <= " + GetSQLDate( DateEnd );

   if( Client and ( Client != UNDF ) )
       sqlQueryOrder = sqlQueryOrder + " and DVDeal.T_CLIENT = " + String( Client );
   end;

   if( SfContr and ( SfContr != UNDF ) )
       sqlQueryOrder = sqlQueryOrder + " and DVPos.T_CLIENTCONTR = " + String( SfContr );
   end;

   if( IsMarket or IsRecept ) 
     sqlQueryCarry = FormQuery( Client, SfContr );
   end;

   if( IsMarket or IsRecept ) 
     sqlQueryOrder = "( " + sqlQueryOrder  + " ) union all " + 
                     "( " + sqlQueryCarry + " )";
   end;

   sqlQueryOrder = sqlQueryOrder +
                   " ORDER BY OrderDate, OrderTime, SfContrName, ClientName, SfContrDate, OrderKind;";

   DV_Orders = TRsbDataSet( sqlQueryOrder, RSDVAL_CLIENT, RSDVAL_STATIC );
   DV_Orders.MoveLast();
   return DV_Orders.GetRecCount();
return 0;
end;
```

---

## Пример 32: `ProcessInNotifications`

**Источник:** `Mac/Mbr/ufInNtf_Proc.mac`
**Тип:** `macro`
**Размер:** 44 строк

```rsl
macro ProcessInNotifications
( DepList : string,
  DateFlag : string
)
  var Report : TUfInNtfReport = TUfInNtfReport();
  var query : string =
      "SELECT wlreq.t_ReqID " +
      " FROM dwlreq_dbt wlreq," +
      " dwlmeslnk_dbt wlmeslnk," +
      " dwlmes_dbt wlmes," +
      " dwlmesrls_dbt wlmesrls," +
      " dwlmesfrm_dbt wlmesfrm," +
      " dwladdfld_dbt wladdfld," +
      " ddp_dep_dbt dep," +
      " dwlsess_dbt wlsess " +
      " WHERE     Wlreq.t_Kind = " + MESKIND_ANSWER +
      " AND Wlreq.t_State = " + WLD_STATUS_REQ_RECEIV +
      " AND Wlreq.t_Direct = 'X'" +
      " AND Wlreq.t_ReqID = wlmeslnk.t_ObjID" +
      " AND Wlmeslnk.t_ObjKind = " + OBJTYPE_REQ +
      " AND Wlmeslnk.t_MesID = wlmes.t_MesID"
      " AND Wlmes.t_RlsFormID = wlmesrls.t_RlsFormID"
      " AND Wlmesrls.t_FormID = wlmesfrm.t_FormID"
      " AND Wlmesfrm.t_Name = 'ED244'" +
      " AND Wladdfld.t_ObjectID = wlreq.t_ReqID " +
      " AND Wladdfld.t_Number = 'RequestCode'" +
      " AND Wladdfld.t_Value = '00' " +
      " AND Wlreq.t_Queries LIKE " +
      "        '%/ОТ' || '" + UfNtfCar_GetAnswerCodeSuccess + "'"
      "        || '/%'" + 
      " AND Wlreq.t_RecipientID = dep.t_PartyID" + 
      GetDepCondition(DepList) +
      " AND Wlmes.t_SessionId = wlsess.t_SessionID " +
      GetDateCondition(DateFlag); 

  var rs = execSQLselect(query);
  var stat:integer;
  var old = SetDialogFlag(0);
  var mode_multi : bool = Opr_SetMultiExec( true ); // в групповом режиме
  Report.PrintRepHeader();
  while(rs and rs.moveNext())
     stat = ProcessInObject(rs.Value(0), OBJTYPE_REQ);
     Report.PrintTableRow(rs.Value(0), stat);
  end;
```

---

## Пример 33: `RunImport`

**Источник:** `Mac/Cb/bnkdirpls.mac`
**Тип:** `macro`
**Размер:** 25 строк

```rsl
macro RunImport(importPathName)
  var i = 0;
  var cmd : RsdCommand;
  var strFile : string;
  var strDate : string;

  SplitFile(importPathName, strFile);

  strDate = substr(strFile, strlen(strFile) - 7);
  
  cmd = RsdCommand("BEGIN RsbBicImport.ImportBnkDirPls(?, ?, ?); END;");
  cmd.addParam( "p_Oper", RSDBP_IN );
  cmd.addParam( "p_Date", RSDBP_IN );
  cmd.addParam( "p_LoadDelta", RSDBP_IN );
  cmd.value("p_Oper") = {oper};
  cmd.value("p_Date") = strDate;
  cmd.value("p_LoadDelta") = LoadDelta;
  cmd.execute();
  OnError(err);
  PrintLn( "Строка: ", err.line );
  PrintLn( err.message );
  while( i < cmd.connection.environment.ErrorCount )
    PrintLn( cmd.connection.environment.Error(i).Descr);
    i = i + 1;
  end;
```

---

## Пример 34: `SIRNSD_Step_Action`

**Источник:** `Mac/DLNG/DEPO/sirnsdImport.mac`
**Тип:** `macro`
**Размер:** 125 строк

```rsl
macro SIRNSD_Step_Action()
   var count = 0, i = 0;
   // Сохраним время запуска процедуры для протокола
   var jvm = CreateObject("rsjvm", "TJavaHost", "GlobalJavaHost");
   jvm = null;
   parm.startTime = time();
   // 1. Выпуски
   if (parm.isAvoir)
      var cmdAvr, dataSetAvr;
      var dataAvr:TAvoirData = null;

      var  sql = " DECLARE "
               + " BEGIN "
               + "    RSB_NSD.UpdateStateNSD(" + GetSQLDate({curdate}) + ") ;  "
               + " END; ";

      var exec = RSDCommand(sql);

      exec.execute();

      if (parm.isProtocolExt)
        cmdAvr = DL_RSDCommand("SELECT * FROM dsirnsd_avr_tmp WHERE T_State = 3");
        var countPA = cmdAvr.GetCount();
        if (countPA > 0)
          dataSetAvr = cmdAvr.Execute();
          while(dataSetAvr.moveNext())
            dataAvr = CreateDataAvr(dataSetAvr, parm.isProtocolExt);
            action.AddProtocolProcessedRec(dataAvr);
          end;
        end;
      end;

      cmdAvr = DL_RSDCommand("SELECT * FROM dsirnsd_avr_tmp WHERE T_State = 0");

      count = cmdAvr.GetCount();
      if (count > 0)
         InitProgress(count, "Обработка выпусков", "Обработка выпусков");   

         // 1. пробегаемся по выпускам НЕ депоз. расписки
         cmdAvr = null;
         cmdAvr = DL_RSDCommand("SELECT * FROM dsirnsd_avr_tmp WHERE T_State = 0 AND T_KINDDATA != ?");
         cmdAvr.addParam(AVOIRISSKIND_DEPOSITORY_RECEIPT);         

         dataSetAvr = cmdAvr.Execute();
         while(dataSetAvr.moveNext())
            if (dataSetAvr.State == 0) // проверим на статус, обо при обработке цб может получиться такое, что статус след. бумаги поменялся на 3, а в массиве он будет 0)
               dataAvr = CreateDataAvr(dataSetAvr, parm.isProtocolExt);
               if (dataAvr != null)
                 action.ActionOnData(dataAvr);
               end;
            end;
            i = i + 1;
            UseProgress(i);
         end;
         // 2. а теперь депоз. расписки, ибо у них есть ссылки на выпуски, которые надо было загрузить сначала
         cmdAvr = null;
         cmdAvr = DL_RSDCommand("SELECT * FROM dsirnsd_avr_tmp WHERE T_State = 0 AND T_KINDDATA = ?");
         cmdAvr.addParam(AVOIRISSKIND_DEPOSITORY_RECEIPT);
         
         dataSetAvr = null;   
         dataSetAvr = cmdAvr.Execute();
         while(dataSetAvr.moveNext())
            if (dataSetAvr.State == 0) // проверим на статус, обо при обработке цб может получиться такое, что статус след. бумаги поменялся на 3, а в массиве он будет 0)
               dataAvr = CreateDataAvr(dataSetAvr, parm.isProtocolExt);
               if (dataAvr != null)
                 action.ActionOnData(dataAvr);
               end;
            end;
            i = i + 1;
            UseProgress(i);
         end;
         RemProgress();
      end;
   end;
   // 2. Организации
   if (parm.isOrg)
      var cmdOrg, dataSetOrg;
      var dataOrg:TOrganizationData;

      sql = " DECLARE "
               + " BEGIN "
               + "    RSB_NSD.UpdateStateOrgNSD();  "
               + " END; ";
      
      exec = RSDCommand(sql);

      exec.execute();

      if (parm.isProtocolExt)
        cmdOrg = DL_RSDCommand("SELECT * FROM dsirnsd_org_tmp WHERE T_State = 3");
        var countPO = cmdOrg.GetCount();
        if (countPO > 0) 
          dataSetOrg = cmdOrg.Execute();
          while(dataSetOrg.moveNext())
            dataOrg = TOrganizationData(parm.isProtocolExt);
            dataOrg.fillFromTMP(dataSetOrg);
            action.AddProtocolProcessedRec(dataOrg);
          end;
        end;
      end;

      cmdOrg = DL_RSDCommand("SELECT * FROM dsirnsd_org_tmp WHERE T_State = 0");

      count = cmdOrg.GetCount();
      if (count > 0)
         i = 0;

         dataSetOrg = cmdOrg.Execute();
         InitProgress(count, "Обработка организаций", "Обработка организаций");
         while(dataSetOrg.moveNext())
            dataOrg = TOrganizationData(parm.isProtocolExt);

            dataOrg.fillFromTMP(dataSetOrg);
            action.ActionOnData(dataOrg);

            i = i + 1;
            UseProgress(i);
         end;
         RemProgress();
      end;
   end;

   action.PrintReport(parm);
   exit(1);
end;
```

---

## Пример 35: `Блок`

**Источник:** `Mac/DLNG/SECUR/Convert/corrlotfrbond.mac`
**Тип:** `block`
**Размер:** 15 строк

```rsl
    FOR one_lot IN (SELECT LOT.T_SUMID, LOT.T_CORRINTTOEIR, LOT.T_CORRINTTOEIRDATE, FI.T_FACEVALUEFI
                      FROM DPMWRTSUM_DBT LOT, DFININSTR_DBT FI, DAVOIRISS_DBT AVR, DDL_TICK_DBT TK
                     WHERE LOT.T_PARTY = -1
                       AND LOT.T_AMOUNT > 0
                       AND LOT.T_AMORTCALCKIND = 2 /*ЭПС*/
                       AND FI.T_FIID = LOT.T_FIID
                       AND FI.T_FI_KIND = 2
                       AND RSI_RSB_FIINSTR.FI_AvrKindsGetRoot(FI.T_FI_KIND, FI.T_AVOIRKIND) = RSI_RSB_Fiinstr.AVOIRKIND_BOND
                       AND AVR.T_FIID = FI.T_FIID
                       AND AVR.T_FLOATINGRATE = 'X'
                       AND TK.T_DEALID = LOT.T_DEALID
                       --AND RSB_SECUR.GetDealMarketTestAttrID(TK.T_BOfficeKind, TK.T_DealID) = 1 /*Тест на рыночность пройден = Да*/
                     ORDER BY LOT.T_SUMID
                   )
    LOOP
```

---

## Пример 36: `Блок`

**Источник:** `Mac/Cb/fm_masschptmvk.mac`
**Тип:** `block`
**Размер:** 13 строк

```rsl
  var query:string = " SELECT pt.t_PartyID || ' ' || pt.t_Name as PartyStr, " +
                     "   DECODE (subj.t_SubjectForm, "+
                     "           2,  (SELECT t_SubjectID || ' ' || LISTAGG(t_Name, '; ') WITHIN GROUP (ORDER BY  T_ISGENERAL DESC ) "+ 
                     "                 FROM DMVKPERSON_DBT prs "+
                     "                WHERE prs.t_SubjectID = cm.t_SubjectID GROUP BY t_SubjectID), "+
                     "           (SELECT t_SubjectID || ' ' || LISTAGG(t_Name, '; ') WITHIN GROUP (ORDER BY  T_ISGENERAL DESC ) "+
                     "              FROM DMVKINSTITUTE_DBT ins "+
                     "             WHERE ins.t_SubjectID = cm.t_SubjectID GROUP BY t_SubjectID)) "+
                     "      AS MvkPartyStr, "+
                     " cm.t_MatchFlags, cm.t_NameMatchPrc, subj.t_SubjectForm "+ 
                     " FROM DMVKCHECKPTMATCH_DBT cm, DPARTY_DBT pt, DMVKSUBJECT_DBT subj " +
                     " WHERE cm.t_CheckID = ? AND cm.t_PartyID = pt.t_PartyID  AND cm.t_SubjectID = subj.t_SubjectID " +
                     " ORDER BY pt.t_PartyID";
```

---

## Пример 37: `ПечататьСообщение`

**Источник:** `Mac/Cb/fm_opprn.mac`
**Тип:** `macro`
**Размер:** 62 строк

```rsl
macro ПечататьСообщение(_fmop)
    record fmop("fm_op.dbt");
    SetBuff(fmop, _fmop);

    if(Report)
        OpCounter = OpCounter + 1;
        CreateHeadersFooters(fmop);

        Информация(fmop);
        //Report.AddParagraph();
        Report.MoveToEnd();
        Операция(fmop);

        if (not Report.IsPoi())
            Report.AddParagraph();
        end;

        report.MoveToEnd();

        ПечататьОперация(fmop);
        Report.AddParagraph();

        var cmd = RsdCommand("SELECT t_ID FROM dfm_op_pt_dbt WHERE t_FMOpID = ? AND T_OPPARTYIDNEW = 0 ORDER BY t_Kind");
        cmd.NullConversion = true;
        cmd.AddParam ("", RSDBP_IN, fmop.ID);

        var rs = RsdRecordset(cmd);
        while (rs.MoveNext())
            var fm_op_pt = TBfile("fm_op_pt.dbt", "R", 0);
            fm_op_pt.rec.ID = Int(rs.value(0));

            if (fm_op_pt.GetEq())
                if (not report.IsPoi())
                    report.MoveToEnd();
                end;

                report.InsertNewPage();

                //if (not report.IsPoi())
                    report.MoveToEnd();
                //end;

                УчастникОперации(fmop, fm_op_pt, false);

                var cmd2 = RsdCommand("SELECT t_ID FROM dfm_op_pt_dbt WHERE t_FMOpID = ? AND t_OpPartyID = ? AND T_OPPARTYIDNEW <> 0 ORDER BY t_Kind");
                cmd2.NullConversion = true;
                cmd2.AddParam ("", RSDBP_IN, fmop.ID);
                cmd2.AddParam ("", RSDBP_IN, fm_op_pt.rec.ID);

                var rs2 = RsdRecordset(cmd2);
                while (rs2.MoveNext())
                    fm_op_pt = TBfile("fm_op_pt.dbt", "R", 0);
                    fm_op_pt.rec.ID = Int(rs2.value(0));

                    if (fm_op_pt.GetEq())
                        УчастникОперации(fmop, fm_op_pt, true);
                    end;
                end;
            end;
        end;
    end;
end;
```

---

## Пример 38: `Constructor`

**Источник:** `Mac/DLNG/TRUST/tspordepo.mac`
**Тип:** `macro`
**Размер:** 137 строк

```rsl
  macro Constructor( SpGroundID )
    var query, SQLcmd, RSD;
    var curCB:CB;
    var i:integer = 0;
    query = RSDCommand(
        " select ground.t_DocTemplate, paym.t_ValueDate, groundDraft.t_SignedDate, "+
        "   groundDraft.t_Xld, groundDraft.t_RegistrDate, groundDraft.t_RegistrTime,"+
        "   paym.t_DocKind Kind, tsorder.t_RegNum, acntPayer.t_Name pNum,          "+
        "   acntReceiver.t_Name rNum,                                              "+
        "   tsorder.t_ID orderID, tsorder.t_DocKind OrderDocKind,                  "+
        "   acntPayer.t_BriefCode PayerCode, acntReceiver.t_BriefCode ReceiverCode,"+ 
        "   paym.t_Amount, paymDraft.t_PaymentID, paym.t_DocumentID,               "+
        "   party.t_ShortName, acP.t_ShortName pType, acR.t_ShortName rType,       "+
        "   partPayer.t_BriefCode pPartCode, partReceiver.t_BriefCode rPartCode,   "+
        "   paym.t_BaseFIID,                                                       "+
        "   acntReceiver.t_AutoKey rAutoKey, acntPayer.t_AutoKey pAutoKey          "+
        " from dtsiorqst_dbt iorqst,                                               "+
        "      dpmpaym_dbt   paym,                                                 "+
        "      dspdrprop_dbt prop,                                                 "+
        "      dspdraft_dbt  draft,                                                "+
        "      dspground_dbt ground,                                               "+
        "      dspground_dbt groundDraft,                                          "+
        "      dspgrdoc_dbt  grdoc,                                                "+
        "      dtsorder_dbt  tsorder,                                              "+
        "      dspdrmove_dbt drmove,                                               "+
        "      dpmpaym_dbt   paymDraft,                                            "+
        "      ddepoacnt_dbt acntPayer,                                            "+
        "      ddepoacnt_dbt acntReceiver,                                         "+
        "      ddepoacnt_dbt partPayer,                                            "+
        "      ddepoacnt_dbt partReceiver,                                         "+
        "      dparty_dbt    party,                                                "+
        "      ddepoac_dbt   acP,                                                  "+
        "      ddepoac_dbt   acR                                                   "+
        " where ground.t_SPgroundID           = ?                                  "+
        "       AND ground.t_SPgroundID       = grdoc.t_SPgroundID                 "+
        "       AND tsorder.t_ID              = grdoc.t_SourceDocID                "+
        "       AND tsorder.t_DocKind         = grdoc.t_SourceDocKind              "+
        "       AND tsOrder.t_ID              = iorqst.t_OrderID                   "+
        "       AND iorqst.t_ID               = paym.t_DocumentID                  "+
        "       AND ( paym.t_DocKind          = 906 OR paym.t_DocKind = 910 )      "+
        "       AND paym.t_PaymentID          = prop.t_PaymentID                   "+
        "       AND prop.t_DraftID            = draft.t_Autokey                    "+
        "       AND draft.t_SPgroundID        = groundDraft.t_SPgroundID           "+
        "       AND (groundDraft.t_Xld        = ground.t_AltXld                    "+
        "            OR  groundDraft.t_AltXld = ground.t_Xld )                     "+
        "       AND drmove.t_DraftID          = draft.t_AutoKey                    "+
        "       AND paymDraft.t_PaymentID     = drmove.t_PaymentID                 "+
        "       AND partPayer.t_AutoKey(+)    = paymDraft.t_PayerDpNode            "+
        "       AND partReceiver.t_AutoKey(+) = paymDraft.t_ReceiverDpNode         "+
        "       AND acntPayer.t_AutoKey(+)    = partPayer.t_Root                   "+
        "       AND acntReceiver.t_AutoKey(+) = partReceiver.t_Root                "+
        "       AND acntReceiver.t_Owner      = party.t_PartyID                    "+
        "       AND partPayer.t_Type        = acP.t_ID                             "+
        "       AND partReceiver.t_Type  = acR.t_ID                                "

    );

    query.addParam( "", RSDBP_IN, SpGroundID );
    query.execute();
    var DataSet = TRSBDataSet(query);

    if( DataSet.MoveNext() )
      DocTempl            = DataSet.DocTemplate;
      paymID              = DataSet.PaymentID;
      DocumentID          = DataSet.DocumentID;

      ДатаПоставки        = DataSet.ValueDate;
      ДатаПодачиПоручения = DataSet.SignedDate;
      ВхНомер             = DataSet.Xld;
      ДатаРегистрации     = DataSet.RegistrDate;
      ВремяРегистрации    = DataSet.RegistrTime;
      Вид                 = DataSet.Kind;
      НаимПасСчетаДепо    = DataSet.pNum;
      НаимАктСчетаДепо    = DataSet.rNum;
      Счет                = DataSet.PayerCode;
      Счет1               = DataSet.ReceiverCode;
      Количество          = DataSet.Amount;
      НомерДоговора       = DataSet.RegNum;
      Депонент            = DataSet.ShortName;
      rType               = DataSet.rType;
      rPartCode           = DataSet.rPartCode;
      pType               = DataSet.pType;
      pPartCode           = DataSet.pPartCode;
      FIID                = DataSet.BaseFIID;
      OrderID             = DataSet.OrderID;
      OrderDocKind        = DataSet.OrderDocKind;
      rAutoKey            = DataSet.rAutoKey;

      if( Вид == 906 ) // Заявление на ввод каритала
        AutoKey             = DataSet.pAutoKey;
      elif( Вид == 910 ) // Заявление на вывод каритала
        AutoKey             = DataSet.rAutoKey;
      end;
    end;

    if( (DocKind == 203 /*DOCKIND_DEPO_REC*/) OR (DocKind == 204/*DOCKIND_DEPO_WITHDR*/) ) /* поручение депо (нэцб) */
      query = RSDCommand(
          " select distinct fin.t_AvoirKind, fin.t_Point,   "+
          "        cm.t_Series, cm.t_NumberFirst,           "+
          "        cm.t_Issuer, leg.t_Principal             "+
          " from dcertmove_dbt cm, dcertif_dbt cert,        "+
          "      dvsbanner_dbt bnr, ddl_leg_dbt leg,        "+
          "      dfininstr_dbt fin                          "+
          " where cm.t_PaymTO = ?                           "+
          "     and cert.t_FIID = cm.t_FIID                 "+
          "     and cert.t_Issuer = cm.t_Issuer             "+
          "     and cert.t_IssuerDate = cm.t_IssuerDate     "+
          "     and cert.t_Series = cm.t_Series             "+ 
          "     and cert.t_NumberFirst = cm.t_NumberFirst   "+
          "     and bnr.t_InventoryXID = cert.t_Xid         "+
          "     and bnr.t_Department = cert.t_Department    "+
          "     and leg.t_DealID = bnr.t_BCID               "+
          "     and leg.t_LegID = 0 and leg.t_LegKind = 1   "+
          "     and fin.t_FIID = cert.t_FIID                " 
      );
  
      query.addParam( "", RSDBP_IN, paymID );
      query.execute();
      DataSet = TRSBDataSet(query);

      i = 0;
      while( DataSet.MoveNext() )
        ArrayCB[i] = CB();
        ArrayCB[i].AvKind      = DataSet.AvoirKind;
        ArrayCB[i].Series      = DataSet.Series;
        ArrayCB[i].NumberFirst = DataSet.NumberFirst;
        ArrayCB[i].Issuer      = DataSet.Issuer;
        ArrayCB[i].Principal   = DataSet.Principal;
        ArrayCB[i].Point       = DataSet.Point;
  
        i = i + 1;
      end;

    elif( DocKind == 299 ) /* поручение депо (эцб) */
      
    end;
  end;
```

---

## Пример 39: `ОбработатьКурс`

**Источник:** `Mac/DLNG/SECUR/Replication/txproc_rate.mac`
**Тип:** `macro`
**Размер:** 43 строк

```rsl
macro ОбработатьКурс(Action, t_instancedate, Init_Action:String)
   var SQL, cmd, rs, Счетчик;

   SQL = "select count(*) from DTXCOURSE_DBT where t_replstate = 0 and t_action = " + Action + " and trunc(t_instancedate) = " + t_instancedate;
   cmd = RsdCommand( SQL);
   rs = RsdRecordSet(cmd);

   if (rs.Movenext)
      Счетчик = rs.Value(0);
      MaxVal = rs.Value(0);
   end;

   var ProgressIndicator = CreateProgressIndicator(true);
   ProgressIndicator.Start(Int(MaxVal), "Обработка курсов...");

   Счетчик = 0;

   SQL = "select * from DTXCOURSE_DBT where t_replstate = 0 and t_action = " + Action + " and trunc(t_instancedate) = " + t_instancedate + " order by t_basefiid, t_marketsectorid, t_type, trunc(t_ratedate)";
   cmd = RsdCommand( SQL);
   rs = RsdRecordSet(cmd);

   while (rs.Movenext)
      Счетчик = Счетчик + 1;

      ProgressIndicator.Update(Int(Счетчик), MaxVal);

      if(RslDefCon.IsInTRans == false)
         RslDefCon.BeginTrans();
      end;

      if (ProcessRate(rs))
         RslDefCon.CommitTrans();
      else
         RslDefCon.RollbackTrans();
      end;
   end;

   ProgressIndicator.Stop();

   return TRUE;
OnError(er)
   ЗанестиЗаписьВПротокол(601, 70, "", "", StrFor(1), "Ошибка: " + er.message, date(t_instancedate));
end;
```

---

## Пример 40: `ОформитьВыкупВекселей`

**Источник:** `Mac/DLNG/VEKSEL/vsrepay3.mac`
**Тип:** `macro`
**Размер:** 82 строк

```rsl
MACRO ОформитьВыкупВекселей(order, overtrans, Дата, vsacc, CanPayAccModi, Налог_объект:@variant, NeedToTax:bool)
var
   prm = RepPrm(),
   СчетЗачисления = "",
   stat = 0;
   ClearGTT_DNPTXOBJ_TMP();
   Договор = order;
   ЧерезТранзит = overtrans;
   СчетПлатУжеИзменен = false;
   ПолучитьСубъекта(order.Contractor, pt_cntr);
   ПоУмолчанию(vsacc, "");
   ПоУмолчанию(CanPayAccModi, true);
   ПоУмолчанию(Дата, {curdate});
   var Сумма_ProcBill = 0.0;
   Счет_Векселя = vsacc;
   ДатаОформл   = Дата;
   
   if (NeedToTax != NULL)//если передавали флаг, то используем его. Не передавали - не используем
     prm.NeedToTax = NeedToTax;
   end;
   
   if(Договор.DocKind == DL_VSINTERCHANGE)  /* Соглашение о зачете требований */
      СчетаДогОпределены = true;
      СчетПлатУжеИзменен = true;
   elif(Договор.DocKind == DL_VSBARTERORDER) /* мена */
      СчетПлатУжеИзменен = (not CanPayAccModi);
   elif(Договор.DocKind == DL_VEKSELDRAWORDER) /* погашение */
      СчетПлатУжеИзменен = true;
   end;

   if(ЧерезТранзит)
      if(not VS_GetAccountOnOrder(order, "-Расчеты", VSORDLNK_K_DRAW, ДатаОформл, @СчетЗачисления, true))
         stat = 1;
      end;
   end;

   prm.СчетЗачисления = СчетЗачисления;
   prm.flag = VS_GetSetting("РЕЖИМ РАБОТЫ\\ДОНАЧИСЛЕНИЕ ПРОЦЕНТОВ");

   if (stat == 0)
      stat = ДляКаждогоВекселя(order, @ОформитьВыкупВекселя, VSORDLNK_K_DRAW, prm, "BL");
   end;
   
   
     /*для ProcBill проводки не нужны. выполняем "наверху"*/
     var paramsArr = TArray();
     paramsArr[0] = Сумма_ProcBill;
     paramsArr[1] = Дата;
     paramsArr[2] = VS_CurrIDOperation;
     paramsArr[3] = VS_CurrIDStep;

    if ( (stat == 0) and ( (NeedToTax != NULL) and (NeedToTax ==true ) or ( NeedToTax == NULL ) ) ) 
      stat = ДляКаждогоВекселя(Договор, @CreateНДР_ProcBill, VSORDLNK_K_DRAW, paramsArr );
      Сумма_ProcBill = paramsArr[0];
    end;
    if (stat == 0)
      stat = СоздатьНДР_PlusG_2800(ДатаОформл, pt_cntr, Сумма_ProcBill, order, VS_CurrIDOperation, VS_CurrIDStep );
    end;
    if (stat == 0)
      stat = СоздатьНДР_BaseBill(ДатаОформл, pt_cntr, Сумма_ProcBill, order, VS_CurrIDOperation, VS_CurrIDStep );
    end;
   
   if (stat == 0)
        var tmp = DL_ChangeDLORDER(order.ContractID, "DateOfPayment", ДатаОформл);
        
        if (tmp)
             var cmd2 = null; 
             /************************************************************/
             /*перенос из временной таблицы в постоянную                 */
             /*Почему то си-код с такой же командой выполнятсья не желает*/
             /************************************************************/
             /*cmd2 = RSDCommand("BEGIN RSI_NPTO.StartInsertTaxObject(?,?); END;"); 
             cmd2.addParam( "", RSDBP_IN, VS_CurrIDOperation        ); 
             cmd2.addParam( "", RSDBP_IN, VS_CurrIDStep         ); 
             cmd2.execute();*/
        end;
        Налог_объект = prm.Налог_объект;
        return tmp;
   end;

   return false;
END;
```

---
