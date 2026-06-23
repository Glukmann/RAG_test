# Практика: Обработка строк (string, strlen, substr, pos, trim)

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

## Пример 2: `MakeFileName`

**Источник:** `Mac/Cb/sfef_xml.mac`  
**Тип:** `private macro`  
**Размер:** 59 строк

```rsl
private macro MakeFileName(bilfactura, bilef)
    // УИОЭДОУИПол                    Идентификатор оператора ЭДО поставщика + Код поставщика
    var filename;
    var day, mon, year;

    if (bilfactura.rec.Assignment != OBJSFASSIGNMENT_RECALC)
        filename = "ON_NSCHFDOPPR_" + bilef.rec.OpSupID + bilef.rec.SupCode + "_";

        // УИОЭДОУИОтпр       Идентификатор оператора ЭДО получателя + Код получателя
        filename = filename + bilef.rec.OpRecID + bilef.rec.RecCode + "_";

        // GGGGMMDD
        DateSplit(Date(GetDbDate()), day, mon, year);
        filename = filename + LPAD4(year, "0") + LPAD2(mon, "0") + LPAD2(day, "0") + "_";

        // N1 36 символьный GUID
        filename = filename + SubStr(CreateGUID(), 2, 36) + "_";

        // N2 формируется значение "1" в случае, если в файле имеется элемент <СведПрослеж> со значениями вложенных элементов 
        // (при отсутствии показателя принимает однозначное значение "0")
        filename = filename + "${N2}_";

        // N3 формируется значение "1" в случае, если используется в целях контроля за движением товаров, подлежащих маркировке 
        // (при отсутствии показателя принимает однозначное значение "0") ? в текущей реализации всегда "0";
        filename = filename + "0_";

        // N4 формируется значение "1" в случае, если используется в целях контроля за движением алкогольной продукции, 
        // подлежащей маркировке (при отсутствии показателя принимает однозначное значение "0" ? в текущей реализации всегда "0");
        filename = filename + "0_";

        // N5 формируется значение "1" в случае, если используется в целях контроля за движением/оборотом табачной продукции, 
        // сырья, никотинсодержащей про-дукции и никотинового сырья (при отсутствии показателя принимает однозначное значение "0" ? в текущей реализации всегда "0");
        filename = filename + "0_";

        // N6 формируется значение "1" в случае, если использование настоящего формата предусмотрено в рамках движения нефтепродуктов
        // (при отсутствии показателя принимает однозначное значение "0" ? в текущей реализации всегда "0");
        filename = filename + "0_";

        // N7 формируется свободное двузначное число, которое принимает значение в соответствии со списком в электронной форме, 
        // размещенный на официаль-ном сайте Федеральной налоговой службы в информационно-телекоммуникационной сети "Интернет" в виде отдельного файла 
        // (при отсутствии показателя принимает однозначное значение "00" ? в текущей реализации всегда "00").
        filename = filename + "00";
    else
        // Корректировка
        filename = "ON_NKORSCHFDOPPR${N2}_";

        // А идентификатор получателя файла обмена корректировочного счета-фактуры
        filename = filename + bilef.rec.SupCode + "_";

        // О идентификатор отправителя файла обмена корректировочного счета-фактуры
        filename = filename + bilef.rec.RecCode + "_";

        // GGGGMMDD
        DateSplit(Date(GetDbDate()), day, mon, year);
        filename = filename + LPAD4(year, "0") + LPAD2(mon, "0") + LPAD2(day, "0") + "_";

        // N 36 символьный GUID
        filename = filename + SubStr(CreateGUID(), 2, 36);
    end;
```

**Комментарий автора:**
УИОЭДОУИПол                    Идентификатор оператора ЭДО поставщика + Код поставщика

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

## Пример 4: `Шапка_по_клиенту`

**Источник:** `Mac/DEPOSITR/rpctax_a.mac`  
**Тип:** `macro`  
**Размер:** 48 строк

```rsl
macro Шапка_по_клиенту( pSeqVal, pStatus )

  var stat = True;
  var Citizenship;
  var sIsMale;
  var sCountryRF = "---";
  var sCountry1  = "---";
  var sCountry2  = "---";
  var sCountry   = "---";
  var IDType = "",
      IDCode = "--";
  var sCorpus = "", iCorpus = 0;
  var sPostIndex = "";
  var sRegion = "";
  var sProvince = "";
  var sDistrict = "";
  var sPlaceType = "";
  var sPlace = "";
  var sStreet = "";
  var sHouse = "";
  var sFlat = "";
  var vAddrType = 1;
  var vAddrTypeRF  = 1;
  var vAddrTypeRez = 1;
  var sAddressNR = "";
  var vSeqVal = 1, numSeq = 1;
  var vBankINN = "", vBankKPP = "", vIndKPP = 0;
  var vObjStr = "";
  var vLenCorr = StrLen( InputPanel_Correct );
  var sPanCorr = "";
  var dd, mm, yyyy;

  COMCLNT.GetRecord( COMCLNT.CurRec.rec.CodClient );

  vObjStr = SubStr( String( 10000000000 + COMCLNT.CurRec.rec.CodClient ), 2 );

  /* Чтение записи ИНН в стране гражданства */
  sINNcitizen = "";
  obj_code.Clear();
  obj_code.rec.ObjectType = 3;  
  obj_code.rec.ObjectID = COMCLNT.CurRec.rec.CodClient;
  obj_code.rec.CodeKind = 33;
  if ( obj_code.GetGE() )
    if ( ( obj_code.rec.ObjectType == 3 )  AND 
         ( obj_code.rec.ObjectID == COMCLNT.CurRec.rec.CodClient )  AND 
         ( obj_code.rec.CodeKind == 33 ) )
      sINNcitizen = obj_code.rec.Code;
    end;
```

---

## Пример 5: `PrintContr`

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

## Пример 6: `ValLogProc`

**Источник:** `Mac/DEPOSITR/val_tran.mac`  
**Тип:** `macro`  
**Размер:** 33 строк

```rsl
macro ValLogProc ( date1, date2, p_iso, p_client, p_group, p_sum, p_filial )

  array iSumO; // Итоговые суммы переводов из России
  array iSumI; // Итоговые суммы переводов в  Россию
  array iCur;  // Коды валют для итоговых сумм

  var curCur = -1; // Текущий код валюты
  var indCur = -1; // Текущий индекс массивов итоговых сумм 
  var numCur;      // Максимальное значение индекса массивов

  var stat = true;
  var nrec = 0;
  var nsrt = 0;
  var rezid = "";
  var group = "";
  var sum = $0;
  var equivSum;
  var corrAcc = "";
  var bankName = {Name_Bank};
  var tm;
  var needProcess = true;
  var errCode = 0;
  var errText;

  var TxtDir = GetRegVal( "BANK_INI\\ОБЩИЕ ПАРАМЕТРЫ\\ДИРЕКТОРИИ\\TEXTDIR", true );
  var FNdt;
  var NameBranch;

  // Определение имени рабочего файла
  if ( StrLen( TxtDir ) > 0 )
    if ( SubStr( TxtDir, StrLen( TxtDir ), 1 ) != "\\" )
      TxtDir = TxtDir + "\\";
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

## Пример 8: `GetPtsvdpList1`

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

## Пример 9: `GetInfoByCells`

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

## Пример 10: `Таблица_доходов_по_ставке`

**Источник:** `Mac/DEPOSITR/rpctax_a.mac`  
**Тип:** `macro`  
**Размер:** 33 строк

```rsl
macro Таблица_доходов_по_ставке( pStatus, pSeqVal )

  var stat = True;

  var vCommonTaxPayGet = $0.0;
  var vCommonTaxPayPut = $0.0;

  var vCommonTaxPayPay = "          0";

  var vDuty            = $0.0;
  var vDutyPayer       = $0.0;
  var vDutyInspection  = $0.0;

  var vMon1 = "", vCod1 = "", vSum1 = 0.0;

  var nOper1 = Index( sOper, " " );
  var nOper2 = Index( SubStr( sOper, nOper1+1 ), " " );
  var sOper1 = "";
  var sOper2 = "";
  var sOper3 = ""; 

  var dd, mm, yyyy;

  var nItem = 1;  // Номер строки "месяца" - от 1 до 15

  if ( nOper1 > 0 )
    sOper1 = SubStr( sOper, 1, nOper1-1 );
    if ( nOper2 > 0 )
      sOper2 = SubStr( sOper, nOper1+1, nOper2-1 );
      sOper3 = SubStr( sOper, nOper1+nOper2+1 );
    else
      sOper2 = SubStr( sOper, nOper1+1 );
    end;
```

---

## Пример 11: `СчитатьПолеИзБуфера`

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

## Пример 12: `ReadCodeWord`

**Источник:** `Mac/Mbr/swparser.mac`  
**Тип:** `macro`  
**Размер:** 31 строк

```rsl
macro ReadCodeWord( Stream, Count, Narrative, NumStr, LenStr, LenCode )
  var Str = "",
      CodeWord = "",
      ch = "",
      Info = "",
      StrmLen = StrLen(Stream),
      i=0,n=0,
      err=FALSE;
  КодыПоля = Tarray;
  while((NOT err) AND (n<NumStr) ) 
    /* первый символ в строке - слэш "/" */
    if( (Count<=StrmLen) AND (SubStr(Stream, Count, 1) == SYMB_SLASH) )
      Count = Count + 1;
      /* считываем кодовое слово */
      if( (Count<StrmLen)
         AND StrmGetLexeme( Stream, Count, CodeWord, TS_ALPHA, TL_MAX, LenCode )
         AND (CodeWord!="")
        )
        /* кодовое слово должно завершаться слэшем */
        if( (Count<=StrmLen) AND ( SubStr(Stream, Count, 1) == SYMB_SLASH) )
          Count = Count + 1;
          /* считываем additional information - эту же строку до конца */
          if( (Count<=StrmLen)
             AND StrmGetLexeme( Stream, Count, Info, TS_XSETRUSBIG, TL_MAX, LenStr-2 )
            )

            if(SubStr(Stream, Count, 1) == SYMB_ENDL)
              /* пропуск CrLf */
              Count = Count + 1;
              n = n + 1;
            end;
```

---

## Пример 13: `GetGr_Docs_Date`

**Источник:** `Mac/Cb/bilimpsf.mac`  
**Тип:** `macro`  
**Размер:** 21 строк

```rsl
macro GetGr_Docs_Date(ТекстИнфДокументОбОтгрузкеЗначен, ShipDocDataArray)
   var ShipNumArray       = TArray;
   var ShipDocArray       = TArray;
   var ShipDocDateArray   = TArray;
   
   var NumDocString = ТекстИнфДокументОбОтгрузкеЗначен;  
   var Error = false;

   var Gr_Num = "",  Gr_Docs  = "", Gr_DateDocs = "";
   if(NumDocString != "")
     var beginN = 0; 

     // Делим строку с  "№ п/п" до "№"
     if((beginN = Index(NumDocString, "№ п/п")) > 0)
       beginN = beginN + strlen("№ п/п");
       var TmpStr = NumDocString;
       TmpStr = substr(TmpStr, beginN);
       var sbegin = strbrk(TmpStr, "№");
       if(sbegin == 0)
//         sbegin = strbrk(TmpStr, "N"); ??
       end;
```

---

## Пример 14: `ExecuteCaseStep`

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

## Пример 15: `ПроверитьИтоговыеПлатежи`

**Источник:** `Mac/DLNG/NETTING/dlnt10.mac`  
**Тип:** `private macro`  
**Размер:** 22 строк

```rsl
PRIVATE MACRO ПроверитьИтоговыеПлатежи( ntg )
  VAR idx = 0, cnt = СписокТребОбяз.size, pmobj = NULL;

  if( not ForEachPMResPaym(ntg.IdentProgram, ntg.NettingID, @ДобавитьИтоговыйПлатеж, NULL) )
     Err.Добавить(NTG_ERR_NOFNLPM);
     return false;
  else
     while( idx < cnt )
        pmobj = НайтиРезультирПлатеж(СписокТребОбяз[idx].ФИ);

        if( pmobj )
           if( СписокТребОбяз[idx].Стр == СписокТребОбяз[idx].Соб )
// оставляем нулевые платежи
//              Err.Добавить(NTG_ERR_CNTFNLPM, string(СписокТребОбяз[idx].ФИ));
//              return false;
           elif( СписокТребОбяз[idx].Стр < СписокТребОбяз[idx].Соб )
              if( (PaymIsDemand(pmobj, ntg) != "") or
                  (pmobj.BaseAmount != (СписокТребОбяз[idx].Соб - СписокТребОбяз[idx].Стр))
                )
                 Err.Добавить(NTG_ERR_BADFNLPM, ПолучитьКодФинИн(СписокТребОбяз[idx].ФИ));
                 return false;
              end; 
```

---

