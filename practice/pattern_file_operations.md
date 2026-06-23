# Практика: Работа с таблицами базы данных (FILE, Tbfile, навигация, модификация записей)

**Теория:** [BnRSL.md## Объектные типы]

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

## Пример 5: `RunAction`

**Источник:** `Mac/DLNG/SECUR/nptxhold040.mac`  
**Тип:** `private macro`  
**Размер:** 63 строк

```rsl
PRIVATE MACRO RunAction( Oper, Doc, ID_Step, ID_Operation )
  var DlRqNew = TRecHandler("dlrq");
  var rRqAcc = TRecHandler("dlrqacc.dbt");
  var MainTaxAccount = TRecHandler("account.dbt");
  var AddTaxAccount = TRecHandler("account.dbt");
  var party = TRecHandler("party.dbt");
  var Notres = false;
  VAR stat = 0;
  var Taxe = $0, Taxe15 = $0;
  var СальдирующаяПроводка = false; //Пока всегда отключена. При необходимости нужно заводить настройку и использовать её
  var isDividend = false;
  var category = "";
  var TxArr = TArray();
  var FD = DLFirstDocNPTXOP( Oper );
  var DtAccount = TrecHandler( "account.dbt");
  var CtAccount = TrecHandler( "account.dbt");
  var Year = 0;
  var mcaccdoc = TBFile( "mcaccdoc" );
  var res = 0, strAccount = "";

  mcaccdoc.Clear();

  DateSplit(Oper.rec.PrevDate, null, null, Year);

  // Повышенный налог с разными ставками
  if((Oper.rec.DocKind == DL_HOLDNDFL) and (Oper.rec.Subkind_Operation == DL_TXHOLD_OPTYPE_VEKSEL))
    var i = -1, taxesSum = $0, taxesSumHigh = $0; // по таблице расшифровки расчета налога

    TxArr = GetTaxByLimits(ID_Operation, false, false);

    if(TxArr.size == 0)
      var NOBSum = $0, NOBSumHigh = $0;
      var intIIS = ContrIsIIS(Oper.rec.Contract);
      var taxesCalcSum = $0, taxesCalcSumHigh = $0;
      var vTaxBaseKind = IIF(intIIS == 1, NPTXTOTALBASE_TAXBASEKIND_IIS,
                           IIF(Oper.rec.Subkind_Operation == DL_TXHOLD_OPTYPE_VEKSEL, NPTXTOTALBASE_TAXBASEKIND_ONB,
                               NPTXTOTALBASE_TAXBASEKIND_BROK));
      var TxArrToMerge = GetTaxByLimits(ID_Operation, false, true);

      STB_GetNOBSum(TxArrToMerge, @NOBSum, @NOBSumHigh);
      STB_GetCalcTaxesSumByKind(TxArrToMerge, STB_GetNOBKind(vTaxBaseKind), @taxesCalcSum, @taxesCalcSumHigh);
      STB_GetTaxesSum(TxArrToMerge, @taxesSum, @taxesSumHigh);

      taxesSum = taxesCalcSum - taxesSum;
      taxesSumHigh = taxesCalcSumHigh - taxesSumHigh;

      // соортируем по году, дате и времени
      qsort(TxArrToMerge, "STB_CmpTaxRateParm");

      // сливаем в одну запись одинаковые ставки
      TxArr = STB_MergeTaxes(TxArrToMerge, Oper.rec.OperDate, Year);

      i = -1;
      while((i=i+1) < TxArr.size)
        TxArr[i].NOB = $0;
        TxArr[i].TaxBaseKind = vTaxBaseKind;
        TxArr[i].NOBKind = vTaxBaseKind;
        if(TxArr[i].CalcPITaxTrue == TxArr[i].HoldPITax)
          TxArr[i].HoldPITax = $0;
          TxArr[i].Deleted = true;
        else
          TxArr[i].HoldPITax = TxArr[i].CalcPITaxTrue - TxArr[i].HoldPITax;
        end;
```

---

## Пример 6: `PT_ShowPTInsPanel_example`

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

## Пример 7: `ExecuteStep`

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

## Пример 8: `PrintContr`

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

## Пример 9: `ОбработкаПортфеля`

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

## Пример 10: `_ExecuteDepoAcc`

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

## Пример 11: `ValLogProc`

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

## Пример 12: `PrepMassExecuteStep`

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

## Пример 13: `ExecuteStep`

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

## Пример 14: `ExecuteStep`

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

## Пример 15: `GenMes`

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

