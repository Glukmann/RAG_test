# Практика: Работа с датами, временем и денежными типами (Date, Money, DateTime, CurDate)

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

## Пример 2: `ОбработкаСчета`

**Источник:** `Mac/Cb/form_res.mac`  
**Тип:** `macro`  
**Размер:** 82 строк

```rsl
macro ОбработкаСчета( _acc, _RsvParm ) : bool

  record acc(account);
  record RsvParm("rsvprm.dbt");
  var AccRsvParm : CAccRsvParm;
  var stat : bool;
  var accResObj : CalcReserveAccount;

  var ReserveAccount : string;
  var AccountReserveKind : integer;
  var ProcentOfReserveOffshore : double;
  var RestReserveAccount            : money;
  var RestReserveSubAccount         : money;
  var RestReserveLoansSubAccount    : money;
  var RestReserveOffshoreSubAccount : money;
  /*Значения процентов резервирования и категорий качества в текущем формировании*/
  var RiskGroup : integer;
  var ReserveProcent : double;
  var ReserveProcentOffshore : double;
  var ReserveProcentEstimated : double;
  var PtRiskGroup : integer;
  var PtReserveProcent : double;
  var PtReserveProcentOffshore : double;
  var PtReserveProcentEstimated : double;
  /*Классификации резервов*/
  var ClassifReserveLoss     : string;
  var ClassifReserveLoans    : string;
  var ClassifReserveOffshore : string;
  /*Даты послених расчетов по видам резервов*/
  var LastDateCalcReserveLoss : date;
  var LastDateCalcReserveLoans : date;
  var LastDateCalcReserveOffshore : date;
  var LastDateCalcReserveEstimated : date;
  /*Значения процентов резервирования и категорий качества в предыдущем формировании*/
  var LastPtRiskGroup : integer;
  var LastPtReserveProcent : double;
  var LastPtReserveProcentOffshore : double;
  var LastPtReserveProcentEstimated : double;
  var LastRiskGroup : integer;
  var LastReserveProcent : double;
  var LastReserveProcentOffshore : double;
  var LastReserveProcentEstimated : double;
  /*Признаки изменения параметров для видов резерва*/
  var ChangedLoss     : bool;
  var ChangedLoans    : bool;
  var ChangedOffshore : bool;
  var ChangedEstimated : bool;
  var ConsiderMinPercent : bool;
  var HasAccTransactions : bool;


  SetBuff( acc, _acc );
  SetBuff( RsvParm, _RsvParm );
  AccRsvParm = CAccRsvParm( RsvParm, acc, AccOprServ.Date);

  stat = true;

  ChangedLoss     = true;
  ChangedLoans    = true;
  ChangedOffshore = true;
  ChangedEstimated = true;
  ConsiderMinPercent = false;
  HasAccTransactions = false;
  
  InitReserveSum();

  /*Определить вид резерва РВП или РВПС*/
  AccountReserveKind = AccRsvParm.Get_AccountReserveKind(); 
  /*Определить классификации резервов*/
  ClassifReserveLoss     =  AccRsvParm.Get_ClassifReserveLoss(); 
  ClassifReserveLoans    =  AccRsvParm.Get_ClassifReserveLoans(); 
  ClassifReserveOffshore =  AccRsvParm.Get_ClassifReserveOffshore(); 

  ReserveAccount = GetAccCaseReserveAccount( acc.Chapter, acc.Code_Currency, acc.Account );
  LastDateCalcReserveLoss = GetAccLastDateCalcReserveLoss(MakeAccountIDEx(acc));
  LastDateCalcReserveLoans = GetAccLastDateCalcReserveLoans(MakeAccountIDEx(acc));

  if (LastDateCalcReserveLoss != null)
    HasAccTransactions = GetHasAccTransactions(acc.AccountID, LastDateCalcReserveLoss);
  else
    HasAccTransactions = GetHasAccTransactions(acc.AccountID, LastDateCalcReserveLoans);
  end;
```

---

## Пример 3: `MakeFileName`

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

## Пример 4: `ОбработатьСчет`

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

## Пример 5: `isNewDirection`

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

## Пример 6: `УстановитьПодсказку`

**Источник:** `Mac/DLNG/SECUR/scservop.mac`  
**Тип:** `private macro`  
**Размер:** 22 строк

```rsl
PRIVATE MACRO УстановитьПодсказку( TableName:string, IndexNum:integer, DefaultHint:string, ScrolStatus:integer, ScrolKind:integer ):string
  //  Возможные значения ScrolStatus:
  //  DL_COMM_PREPARING = 0,  // на этапе подготовки
  //  DL_COMM_READIED,        // готовые (создана операция)
  //  DL_COMM_CLOSED,         // закрытые
  //  DL_COMM_ALL             // все


  //  Возможные значения ScrolKind:
  //  DL_COMMDOC     = 104,   // Операции расчета комиссий
  //  DL_RESERVEDOC  = 106,   // Операции резервирования средств под обесценивание ЦБ
  //  DL_OVERVALUE   = 108,   // Операции переоценки ценных бумаг
  //  DL_OVERVALUE_RD  = 123,  // Переоценка внебаланса
  //  DL_OVERVALUE_NVPI = 134,  // Переоценка НВПИ
  //  DL_GET_INCOME     = 157, // БОЦБ - начисление процентного/дисконтного дохода

  //пример
  //return "/*+FIRST_ROWS LEADING(t) INDEX(t ddl_comm_dbt_idx0)*/";

  return DefaultHint;

END;
```

**Комментарий автора:**
Возможные значения ScrolStatus: DL_COMM_PREPARING = 0,  // на этапе подготовки DL_COMM_READIED,        // готовые (создана операция)

---

## Пример 7: `SfFormDocumentsBatch`

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

## Пример 8: `PT_ShowPTInsPanel_example`

**Источник:** `Mac/Cb/PT_ShowPTPanel.mac`  
**Тип:** `private macro`  
**Размер:** 26 строк

```rsl
private macro PT_ShowPTInsPanel_example()
  var party = TRecHandler("party.dbt");
  party.clear();
  var persn = TRecHandler("persn.dbt");
  persn.clear();

  var RezultPartyID : Integer=0;
  var isOk = true;

    // пример №1. Вызов панели юр.лица, PartyID не выгружается.
//  isOk = PT_ShowPTInsPanel();           

    // пример №2. Вызов панели юр.лица, PartyID выгружается.
//  isOk = PT_ShowPTInsPanel(@RezultPartyID);   

    //  пример №3. Вызов панели юр.лица c параметрами
//  party.rec.ShortName = "ООО \"Огонек\"";
//  isOk = PT_ShowPTInsPanel(@RezultPartyID, PTLEGF_INST, "юридического лица", PTLIST_ALLINST, party);  

    // пример №4. Вызов панели физ.лица c параметрами
//  party.rec.ShortName = "Петров П.П.";
//  persn.rec.Born = Date(21,1,1974);
//  isOk = PT_ShowPTInsPanel(@RezultPartyID, PTLEGF_PERSN, "физического лица", PTLIST_ALLINST, party, persn);  

//  println(isOk, " ;", RezultPartyID);
end;
```

---

## Пример 9: `Charge_Batch`

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

## Пример 10: `PrintContr`

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

## Пример 11: `УстановитьПодсказку`

**Источник:** `Mac/DLNG/DEPO/dpglobop.mac`  
**Тип:** `private macro`  
**Размер:** 19 строк

```rsl
PRIVATE MACRO УстановитьПодсказку( TableName:string, IndexNum:integer, DefaultHint:string, ScrolStatus:integer, ScrolKind:integer ):string
  //  Возможные значения ScrolStatus:
  // 0,  //все       
  // 1,  //отложенное
  // 2,  //открытое  
  // 3   //закрытое  
  
  //  Возможные значения ScrolKind:
  // DP_DEPOPER_CONVERT       852, // "Поручение на конвертацию ц/б"             
  // DP_DEPOPER_REPAY         854, // "Поручение на погашение (анулирование) ц/б"
  // DP_DEPOPER_BONEMISS      856, // "Поручение на бонусную эмиссию ц/б"        
  // ALL_KIND_OF_DOC          0,   // Все

  //пример
  //return "/*+FIRST_ROWS LEADING(t) INDEX(t ddpcorpop_dbt_idx0)*/";

  return DefaultHint;

END;
```

**Комментарий автора:**
Возможные значения ScrolStatus: 0,  //все 1,  //отложенное

---

## Пример 12: `ОбработкаПортфеля`

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

## Пример 13: `formingUNRZEx`

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

## Пример 14: `FillInformationTable`

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

## Пример 15: `CloseZeroAccounts`

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

## Пример 16: `PrintReport`

**Источник:** `Mac/Cb/ptchkrfridn.mac`
**Тип:** `macro`
**Размер:** 29 строк

```rsl
macro PrintReport
(
  ReportFileName, 
  OnDate,
  Dprt,
  NeedChildService,
  IdentifyUndefined,
  IdentifyDeadline,
  AlertDays,
  IdentifyExpired,
  SelectClient,
  SelectProxy,
  SelectBeneficiary,
  SelectBeneOwner
)
  setoutput(ReportFileName);
debugbreak;
[Субъекты экономики для обновления анкеты                                          ];
[                                                                                  ];
[Дата:         ########## г.                                                       ] (date:f);                
[Время:        ########                                                            ] (time:f);
[Пользователь: ##### #                                                             ] ({oper}, {Name_Oper});   
[                                                                                  ];
_PrintReportDepartment(Dprt);
[Подчиненные филиалы: #                                                            ] (IfThenElse(NeedChildService, "да", "нет"));
[По состоянию на дату: ########## г.                                               ] (OnDate:f);
  if(IdentifyExpired)
[Срок обновления истекает в течение ##### дней                                     ] (AlertDays:l);
  end;
```

---

## Пример 17: `Печать`

**Источник:** `Mac/DLNG/DV/dv_journl.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro Печать( OrderDate )
   Rep.AddNewSheetBreak( "за дату "+String(Date(DV_Orders.OrderDate)), Table );
   PrintHead( Date(DV_Orders.OrderDate) );

   while( IsNotEof and (OrderDate == Date(DV_Orders.OrderDate) ) )
      PrintLineTable();
      IsNotEof = DV_Orders.MoveNext();
   end;

   after_44_footer( Rep );
end;
```

---

## Пример 18: `CheckData`

**Источник:** `Mac/DLNG/SECUR/sptagfl.mac`
**Тип:** `macro`
**Размер:** 22 строк

```rsl
macro CheckData ( Data )
   var str;
   if( ValType( Data ) == V_DATE)
     if(Data == Date(0,0,0))
       return str = ("\"___\"" + " _________ " + "20__ ");
     else
       return Data;
     end;
   elif(ValType( Data ) == V_STRING)
     if(Data == "")
       return str = "________________________";
     else
       return Data;
     end;
   else
     if( not Data )
       return str = "________";
     else
       return Data;
     end;
   end;
end;
```

---

## Пример 19: `CheckDenom`

**Источник:** `Mac/DEPOSITR/denomin.mac`
**Тип:** `macro`
**Размер:** 28 строк

```rsl
MACRO CheckDenom(Referenc)
 file doc("sbdepdoc.dbt") key 1; /* файл документов */
 doc.Referenc = Referenc;
 doc.TypeOper = Деноминация;
 doc.DepDate_Document = Date(31,12,2999);
 if(GetLE(doc) AND
    (doc.Referenc == Referenc) AND
    (doc.TypeOper == Деноминация) AND
    (doc.KindOp != 9) /* не архивный документ */)
  ДатаДеном = doc.DepDate_Document;
 else
  ДатаДеном = Date(0,0,0);
 end; /* IF */
END; /* MACRO */


MACRO Den(Сумма, Дата)
 if(Дата > ДатаДеном)
   return Сумма;
 else
   if( Сумма < 0 )
     return -MoneyL( Floor( DoubleL( -Сумма * 100 ) / 1000 + 0.5 ) ) / 100;
   else
     return MoneyL( Floor( DoubleL( Сумма * 100 ) / 1000 + 0.5 ) ) / 100;
   end;
 end;/* IF */
end; /* MACRO */
```

---

## Пример 20: `ПроставитьОтзывностьИПокрытие`

**Источник:** `Mac/Cb/akkrtls.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro ПроставитьОтзывностьИПокрытие(КодОтз: integer, КодПокр: integer): string

   if((КодОтз == 1) And (КодПокр == 1)) return "О"; end;
   if((КодОтз == 2) And (КодПокр == 1)) return "Б"; end;
   if((КодОтз == 1) And (КодПокр == 2)) return "П"; end;
   if((КодОтз == 2) And (КодПокр == 2)) return "Н"; end;

end;
```

---

## Пример 21: `_GetElementByRsvClass`

**Источник:** `Mac/Cb/res_liba.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro _GetElementByRsvClass( ListClassif : integer, Classif : integer ) : string
  record llvalues( "llvalues.dbt" );
  ClearRecord( llvalues );
  if( Classif )
    LL_FindLLVALUES( ListClassif, Classif, llvalues );
    return llvalues.Code;
  end;
```

---

## Пример 22: `СчитатьНачалоБлокаSB`

**Источник:** `Mac/Mbr/swsbin.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
macro СчитатьНачалоБлокаSB(КодНачалаБлокаПрочитан, str, NameLen)
  var строка, длина, НомерБлока;

  if (ValType(NameLen) == V_UNDEF)
    NameLen = 1;
  end;
```

---

## Пример 23: `VA_GetShifrOper`

**Источник:** `Mac/DLNG/VA/vacateg.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
MACRO VA_GetShifrOper(PayerAccount:STRING, PayerFIID:INTEGER, ReceiverAccount:STRING, ReceiverFIID:INTEGER, Chapter:INTEGER)
  record PayerAcc("account");
  record ReceiverAcc("account");
  var Шифр = "";

  ClearRecord(PayerAcc);
  ClearRecord(ReceiverAcc);

  DL_GetAccount( Chapter, PayerFIID, PayerAccount, PayerAcc);
  DL_GetAccount( Chapter, ReceiverFIID, ReceiverAccount, ReceiverAcc);

  Шифр = DL_GetShifrOper(Chapter, PayerAcc, ReceiverAcc); 

  return Шифр;
END;
```

---

## Пример 24: `GetReportAction`

**Источник:** `Mac/DLNG/IR/ir_CMfunctions.mac`
**Тип:** `macro`
**Размер:** 40 строк

```rsl
macro GetReportAction( TemplNum:integer ):integer
    if   ( TemplNum == DLGR_TEMPL_BULKREPORT )
        return BULKREPORT;
    elif ( (TemplNum == DLGR_TEMPL_CHANGEMSG) or (TemplNum == DLGR_TEMPL_CHANGEMSGWTHREQUEST) )
        if ( TemplNum == DLGR_TEMPL_CHANGEMSGWTHREQUEST )
            return CHANGEDEALWTHREQUEST;
        end;
        return CHANGEDEAL;
    elif ( (TemplNum == DLGR_TEMPL_MAKEDEAL) or (TemplNum == DLGR_TEMPL_MAKEDEALWTHREQUEST) )
        if( TemplNum == DLGR_TEMPL_MAKEDEALWTHREQUEST )
            return MAKEDEALWTHREQUEST;
        end;
        return MAKEDEAL;
    // обязательства
    elif ( (not (TemplNum < DLGR_TEMPL_CLOSECONTR)) AND (not (TemplNum > DLGR_TEMPL_NETTINGSUSPWTHREQUEST)) AND (not GAmsg) )
        if( (TemplNum == DLGR_TEMPL_CLOSECONTRWTHREQUEST) OR 
            (TemplNum == DLGR_TEMPL_EXECDELAYMSGWTHREQUEST) OR
            (TemplNum == DLGR_TEMPL_EXECHOLDMSGWTHREQUEST) OR
            (TemplNum == DLGR_TEMPL_EARLYEXECMSGWTHREQUEST) OR
            (TemplNum == DLGR_TEMPL_REJECTIONMSGWTHREQUEST) OR
            (TemplNum == DLGR_TEMPL_NETTINGSUSPWTHREQUEST) )
            return OBLIGATIONCHANGEWTHREQUEST;
        end;
        return OBLIGATIONCHANGE;
    // сообщения по ГС
    elif ( (TemplNum == DLGR_TEMPL_MAKECONTRACT) or (TemplNum == DLGR_TEMPL_MAKECONTRACTWTHREQUEST) )
        if( TemplNum == DLGR_TEMPL_MAKECONTRACTWTHREQUEST )
            return MAKECONTRACTWTHREQUEST;
        end;
        return MAKECONTRACT;
    elif ( (TemplNum == DLGR_TEMPL_CLOSECONTR) )
        return CLOSECONTRACT;
    elif ( TemplNum == DLGR_TEMPL_RECONCILIATION )
        return RECONCILIATION;
    elif ( TemplNum == DLGR_TEMPL_REVALUATION_FAIRVALUE )
        return FAIRVALUE;
    else
        return 0;
    end;
end;
```

---

## Пример 25: `InitBeginReportDate`

**Источник:** `Mac/DLNG/SECUR/ReportMoveBasketREPO_Report.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
  MACRO InitBeginReportDate()
    var Day, Month, Year;
    datesplit( m_ReportDate, Day, Month, Year );
    return date(1, 1, Year);
  END;
```

---

## Пример 26: `PrintDocument`

**Источник:** `Mac/Cb/Prcsioo3352u.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
MACRO PrintDocument(ncopy:integer):bool

  var DocKind:integer = pr_pmpaym.rec.DocKind;
  var data : TInOutOrderPrintData = TInOutOrderPrintData();

  if( DocKind == 445 )   /*Приходно-расходный кассовый ордер*/
    data.InitByCashOrder( pr_pmpaym, pr_pmrmprop, pr_pscshdoc );  
    if( data.format == 0 )
      data.DateStr = DDpMMpYYYY( pr_pmpaym.rec.valuedate );
    end;
  else
    MsgBox("Данный вид документа не поддерживается макросом");
    return FALSE;
  end;
```

---

## Пример 27: `GGFillPaymentAmount`

**Источник:** `Mac/Mbr/ggreqacrlproc.mac`
**Тип:** `macro`
**Размер:** 27 строк

```rsl
macro GGFillPaymentAmount(p_RsbGGAcrl : RsbGGAccrual, p_PaymentAmount : money)
   const prmPaymentAmount : integer = 1;
   var stat : integer = 0;

   if ((p_RsbGGAcrl.PayAmount != $0.00) AND (p_RsbGGAcrl.TotalAmount != $0.00))
      var button:integer = ConfWin(makeArray("Создать платеж на сумму:" ), makeArray(string("Общая сумма начисления ", p_RsbGGAcrl.TotalAmount), string("Сумма к оплате ", p_RsbGGAcrl.PayAmount), "Отмена"), 0);
      if (button == 0)
         SetParm(prmPaymentAmount, p_RsbGGAcrl.TotalAmount);
      elif (button == 1)
         SetParm(prmPaymentAmount, p_RsbGGAcrl.PayAmount);
      else
         stat = 1;
      end;
   elif (p_RsbGGAcrl.TotalAmount != $0.00)
      if ((p_RsbGGAcrl.AddPayCond != 1) AND (p_RsbGGAcrl.AddPayCond != 3))
         SetParm(prmPaymentAmount, p_RsbGGAcrl.TotalAmount);
      elif ((p_RsbGGAcrl.AddPayCond == 1) AND ((p_RsbGGAcrl.DiscountTo > {curdate}) OR (p_RsbGGAcrl.DiscountTo == BDATE_ZERO)))
         SetParm(prmPaymentAmount, p_RsbGGAcrl.TotalAmount - p_RsbGGAcrl.DiscountAmount);
      elif ((p_RsbGGAcrl.AddPayCond == 3) AND ((p_RsbGGAcrl.DiscountTo > {curdate}) OR (p_RsbGGAcrl.DiscountTo == BDATE_ZERO)))
         SetParm(prmPaymentAmount, p_RsbGGAcrl.TotalAmount - (p_RsbGGAcrl.TotalAmount * p_RsbGGAcrl.DiscountAmount / 100.00));
      end;
   else
      SetParm(prmPaymentAmount, p_RsbGGAcrl.PayAmount);
   end;

   return stat;
end;
```

---

## Пример 28: `ExecuteStep`

**Источник:** `Mac/Cb/fsspcorrect20.mac`
**Тип:** `macro`
**Размер:** 19 строк

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
  var param = TRecHandler("fsspcorrprm.dbt");
  var PayDocs = FssRequireObj.PayDocs;

  stat = FSSP_GetCorrectParam(ID_Operation, ID_Step - 1, param);

  if (stat)
    FSSP_OpMsg("Не возможно cоздать документ корректировки");
    return 1;
  end;
```

---

## Пример 29: `GenDoc`

**Источник:** `Mac/Mbr/ofkgdflt.mac`
**Тип:** `macro`
**Размер:** 46 строк

```rsl
macro GenDoc( addrMes )

  SetBuff( wlmes, addrMes );
  
  PrintLog(2,"Генерация квитанции FAULT");
  debugbreak();
  var field_name, field_value;
  
  // параметры функций генерации уч.объектов
  var mESid             = 0,
      ErrCode           = 0,
      State             = 0,
      ErrDescription    = "",
      CreateDate        = date(),
      CreateTime        = time(),
      FinalPaymentID    = TArray(),
      sing              = 1, //!!!
      RequestMessageID  = "",
      Faultcode         = "",
      Faultstring       = "",
      ResultCode        = 0,
      ResultID          = 0;

  var RegVal = false, error = 0;
  GetRegistryValue( "Межбанковские расчеты//ГИС ГМП//GenObjIncorrSign", V_BOOL, RegVal, error );

  while( СчитатьПоле(field_name, field_value) )    
    if( field_name == "_sing" )
      sing = field_value;
    end;
    if( field_name == "ResultCode" )
      ResultCode = int(field_name);
    end;
    if( field_name == "RequestMessageID" )
      RequestMessageID = field_value;
    end;
    if( field_name == "FinalPaymentID" )
      FinalPaymentID[FinalPaymentID.size] = field_value;
    end;
    if( field_name == "Faultcode" )
      Faultcode = field_value;
    end;
    if( field_name == "Faultstring" )
      Faultstring = field_value;
    end;
  end;
```

---

## Пример 30: `LC_LinkMesToLcdoc`

**Источник:** `Mac/LC/lclib.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro LC_LinkMesToLcdoc
( MesID : integer, 
  LcObj : RsbLetterOfCredit, 
  LinkKind : integer, 
  ObjectID : integer,
  ObjectType : integer,
  saveChangesLcObj : bool
)

  if(not LinkKind)
    LinkKind = LCMES_LINKKIND_MESSAGE;
  end;
```

---

## Пример 31: `ExecuteStep`

**Источник:** `Mac/Cb/fsspcfndacc10.mac`
**Тип:** `macro`
**Размер:** 52 строк

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
  var AccEquire = FssRequireObj.Accequire;

  FSSP_WriteTrace("Begin ExecuteStep");

  // Проверка возможности списания средств со счета
  FSSP_WriteTrace("Before FSSP_FillAccounts");
  var result = FSSP_FillAccounts(FssRequireObj, GetDBDate(), ACC_ALL);
  FSSP_WriteTrace("After FSSP_FillAccounts");

  if ((result == FILLACCRES_NO_ACCOUNTS) or (result == FILLACCRES_NO_ACTIVE_ACCOUNTS))
    FssRequireObj.State = FSSPREQUIRE_PROCESS; // Обрабатывается
    
    FssRequireObj.RestrictionAnswerType = FSSPACCEQUIRE_AT_OTHER; // Постановление не исполнено по иным причинам
    FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_RT_NOT_FOUND; // Счёт не найден

    var iter = AccEquire.First();
    var ArrestRecoveryState = 0;
    
    if (iter)
      ArrestRecoveryState = AccEquire.ArrestRecoveryState;
    end;

    if (ArrestRecoveryState != 0)
      if (ArrestRecoveryState == FSSPACCEQUIRE_RT_FOUND_OTHER_CLIENT)
        // Счёт найден, но принадлежит другому клиенту
        FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_OTHER_CLIENT; // Арест наложен на другого должника
      elif (ArrestRecoveryState == FSSPACCEQUIRE_RT_NOT_FOUND)
        // Счёт не найден
        FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_RT_NOT_FOUND; // Счёт не найден
      elif (ArrestRecoveryState == FSSPACCEQUIRE_RT_FOUND_ACC_CLOSE)
        // Счёт найден, счёт закрыт
        FssRequireObj.RestrictionRejectType = FSSPACCEQUIRE_ACCCLOSED; // Счет закрыт
      end;
    end;

    InsertOprStatus(RSBFSSREQUIRE_OPST_DOCUMENT, RSBFSSREQUIRE_DS_NOTIFY);
    InsertOprStatus(RSBFSSREQUIRE_OPST_FIND_ACC, RSBFSSREQUIRE_NO_FINDACCOUNT);
  else
    // Список счетов для оплаты постановления сформирован
    FssRequireObj.State = FSSPREQUIRE_PROCESS;
    InsertOprStatus(RSBFSSREQUIRE_OPST_FIND_ACC, RSBFSSREQUIRE_NO_FINDACCOUNT);
  end;
```

---

## Пример 32: `CheckAndSetStaticAccType`

**Источник:** `Mac/DEPOSITR/t2s_comm.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro CheckAndSetStaticAccType

  var
    RetVal = false;

  if(Convert(Dep.Sum_Rest) > $3.00)
    if({curdate} - GetLatestOperDate > 365 * 10)
      StaticAccType = SA_STATIC;
      RetVal = true;
    end;
  else
    if({curdate} - GetLatestOperDate > 365 * 5)
      StaticAccType = SA_UNITED;
      RetVal = true;
    end;
  end;
```

---

## Пример 33: `Fill11`

**Источник:** `Mac/Mbr/swgdn95r.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro Fill11( FormName, Date, SessNum, ISN )
  MTn95.InitFormName = FormName;
  MTn95.InitDate = Date;
  return TRUE;
end;
```

---

## Пример 34: `AcqObjSelect`

**Источник:** `Mac/ACQUIRER/acq_Pay.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro AcqObjSelect(_taskID, _execID, _conveyerID, _packetSize, _Params)
  var packetNum = 0;

  var Branch    = NumFNCash();
  var ZeroDate  = Date(0,0,0);
  var CurDate   = {curdate};

  /*
  if ( GenPropID( _Params, "SelValue1" ) != -1 )
    [SelValue1 = #]( String( _Params.SelValue1 ) );
  end;
```

---

## Пример 35: `GetParametrTemplate`

**Источник:** `Mac/Cb/mc_prim_doc.mac`
**Тип:** `macro`
**Размер:** 71 строк

```rsl
  macro GetParametrTemplate( ObjectID, Classificator, OperDate, FIRole ) : integer
    
    var Parametr = -1;

    if( Classificator == LLCLASS_CHAPTER_OCP )

      /* глава учета */
      Parametr = acctrn.rec.Chapter;

    elif( Classificator == LLCLASS_SIDEBALANCE_CORACCKIND )

      /* вид корреспондирующего счета */  
      if( (FIRole == FIROLE_INCOME_DEBET) or (FIRole == FIROLE_EXPEND_DEBET) )
        
        Parametr = GetSideBalance( acctrn.rec.Chapter, acctrn.rec.FIID_Payer, acctrn.rec.Account_Payer );
      
      elif( (FIRole == FIROLE_INCOME_CREDIT) or (FIRole == FIROLE_EXPEND_CREDIT) )
      
        Parametr = GetSideBalance( acctrn.rec.Chapter, acctrn.rec.FIID_Receiver, acctrn.rec.Account_Receiver );

      end;
    
    elif( (Classificator == LLCLASS_KIND_AKT_BANK) or (Classificator == LLCLASS_FI_KIND) )

      /* вид актива */  
        if( (FIRole == FIROLE_INCOME_DEBET ) or (FIRole == FIROLE_EXPEND_DEBET ) ) Parametr = GetFIKind( acctrn.rec.FIID_Payer    );
      elif( (FIRole == FIROLE_INCOME_CREDIT) or (FIRole == FIROLE_EXPEND_CREDIT) ) Parametr = GetFIKind( acctrn.rec.FIID_Receiver );
      end;

    elif( (ObjectID == OBJTYPE_IST_DOH_RASH) AND (Classificator == LLCLASS_KIND_COURCE_DIF) )
      
      Parametr = 6;

    elif( Classificator == LLCLASS_SYMBOLNUMBERS )

      if( OperDate >= DateBegin446P )
        Parametr = 0;
      end;

    elif( Classificator == LLCLASS_DEAL_CASH_KIND )

      if(Index( acctrn.rec.TypeDocument, "Q" ) != 0)
        Parametr = 1;
      else
        /* вид сделки: наличная или нет */
        if( (FIRole == FIROLE_INCOME_DEBET) or (FIRole == FIROLE_EXPEND_DEBET) )
        
          Parametr = GetDealCashKind( acctrn.rec.Chapter, acctrn.rec.FIID_Payer, acctrn.rec.Account_Payer );
      
        elif( (FIRole == FIROLE_INCOME_CREDIT) or (FIRole == FIROLE_EXPEND_CREDIT) )
      
          Parametr = GetDealCashKind( acctrn.rec.Chapter, acctrn.rec.FIID_Receiver, acctrn.rec.Account_Receiver );

        end;
      end;

    elif( Classificator == LLCLASS_CODE_FI )
      
      if( OperDate >= DateBeginМСФО )
        Parametr = 0;
      else
          if( (FIRole == FIROLE_INCOME_DEBET ) or (FIRole == FIROLE_EXPEND_DEBET ) ) Parametr = ExRate_GetParameter_CodeFI( acctrn.rec.FIID_Payer    );
        elif( (FIRole == FIROLE_INCOME_CREDIT) or (FIRole == FIROLE_EXPEND_CREDIT) ) Parametr = ExRate_GetParameter_CodeFI( acctrn.rec.FIID_Receiver );
        end;
      end;

    end;

    return Parametr;

  end;
```

---

## Пример 36: `GetFieldValue`

**Источник:** `Mac/DLNG/SECUR/CompareSumCup_form.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
  MACRO GetFieldValue(
    FieldNumber : Integer,
    ShowValue   : @Variant,
    RealValue   : @Variant
  )
    return GetFieldValueEx( ReDefineFieldNum[FieldNumber], @ShowValue, @RealValue );
  END;
```

---

## Пример 37: `ExecuteStep`

**Источник:** `Mac/DLNG/DV/dvop200.mac`
**Тип:** `macro`
**Размер:** 18 строк

```rsl
MACRO ExecuteStep( Doc, FirstDoc, FirstDocKind )

  RECORD rFirstDoc( dvdeal );
  RECORD OverAcc( account );  /* счет переоценки */
  RECORD CorrAcc( account );   /* счет маржи переоценки */

  VAR AvFI      = TRecHandler( "fininstr" ), 
      InsOperPS = TRecHandler( "dvoperps" );
  VAR OperPS:variant, FD:DVFirstDocDeal;
  VAR P:double = 0.0, Ds:money = $0, DsR:money = $0, Sa:money = $0, Sy:money = $0, NKD:money = $0, П:money = $0, N:money = $0;
  VAR ReqOrCom:string = "";
  VAR CatAcc:string = "", StrGround:string = "";
  VAR DebAcc:string = "", CredAcc:string = "";

  if( SvOpDvOper.rec.ID <= 0 )
     MsgBox("Шаг \"Переоценка по рыночной цене ц/б\" должен выполняться только из соответствующей сервисной операции.");
     return 1;
  end;
```

---

## Пример 38: `GetCriticalAction`

**Источник:** `Mac/Cb/ws_webcritact.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro GetCriticalAction(caid :Integer) // : CriticalAction

    var ca = FindCriticalAction(caid);
    if (ca == null)
        RunError("Не найдено КД");
    end;

    return ParseCriticalAction(ca);
end;
```

---

## Пример 39: `Печать_ОтчетСканирования`

**Источник:** `Mac/DLNG/SECUR/inaccsrvopdactscn.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
MACRO Печать_ОтчетСканирования( NumExec:INTEGER, FDoc:VARIANT, ErrStatus:INTEGER, ErrMessage:STRING, Action:INTEGER )

  GrDoc.SetRecordAddr( FDoc );

  if( Action == 3 )
     DeleteGrDocFromOper( NumExec, ErrStatus, ErrMessage );
  end;
```

---

## Пример 40: `GetAccStatement_BR`

**Источник:** `Mac/Cb/ic_getaccstatement_zbr.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro GetAccStatement_BR(RequestData/* : TRequestData*/)
  WS_CheckParameter(1, RequestData, true, V_GENOBJ);
  var localRD : TRequestData = FillRequestData(RequestData);

  var ResponseData : TResponseData;

  var wlregdec = RsbFnsInfoVS(0);
  wlregdec.Type    = WLD_TYPE_REGDEC_IVS;
  if (localRD.DateIn != null)
    wlregdec.Date    = localRD.DateIn;
  end;
```

---
