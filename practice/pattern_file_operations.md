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

## Пример 16: `first`

**Источник:** `Mac/Interbnk/r2i_util.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
macro first : bool

  dpDepList.SetFilter(dpDepList.getFilialID(NumFNCash()));
  ddep = dpDepList.recHandler;
  return next;
end;
```

---

## Пример 17: `ExecuteStep`

**Источник:** `Mac/DLNG/VA/vaw020.mac`
**Тип:** `macro`
**Размер:** 28 строк

```rsl
MACRO ExecuteStep(Buffer, dl_tick)
var stat = 0;

    record tick( dl_tick );
    SetBuff( tick, dl_tick );

    if( tick.DealDate > {curdate} )
       return VA_Err("Преждевременное выполнение шага запрещено.");
    end;

    DealDate = tick.DealDate;

    if((tickFd = VATickFD(tick)) == null)
       return VA_Err("Ошибка при определении первичного документа сделки");
    end;

    ВУтр = ПолучитьВУПолучаемыхЦБВМене(tick);
    ВУоб = ПолучитьВУПередаваемыхЦБВМене(tick);

    ВалРасчетов = tickfd.GetDealPayFI();

    if(not СчетаПоКаждойВалюте(tick))
       stat = 1;
    end;

    return stat;

END;
```

---

## Пример 18: `PrintStepDocs`

**Источник:** `Mac/DLNG/FOREX/fxsw270.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
MACRO PrintStepDocs (
                ID_Operation,  /* Номер экземпляра операции */
                ID_Step,       /* Номер шага операции */
                Kind_Operation,/* Вид операции */
                KindStep)      /* Вид шага операции */

  var oproper = TBfile("oproper.dbt"),
       dl_tick = TBfile("dl_tick.dbt") ;
  RECORD tick(dl_tick);
    
  oproper.rec.ID_Operation = ID_Operation;
    
  if (not oproper.GetEq )
    msgbox( "Не найдена сделка ", ID_Operation );
    return 1;
  end;
```

---

## Пример 19: `GenDoc`

**Источник:** `Mac/Mbr/swgd300.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro GenDoc( addrMes )

  SetBuff( wlmes, addrMes );

  PrintLog( 2,"Генерация подтверждения сделки Forex по МТ300" );

  /* На этапе генерации по МТ300 никаких учетных объектов не вставляем 
     Создаётся фиктивная связь сообщения с нулевым объектом */
  var stat:integer = ConnectMessageToObject( wlmes.MesID, "X", OBJTYPE_CONVDEAL, 0 );
  if( stat )
    std.msg( GetErrMsg() );
  end;
```

---

## Пример 20: `Cash_MassPrint`

**Источник:** `Mac/Cb/prbbio.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro Cash_MassPrint( Num, /* число печатаемых копий, если 0, считается первым вызовом */
                      aa, bb, cc )
  var err;
  setbuff( payment, bb  );
  setbuff( order,   aa );

  if(Num) MassCopy = Num;
  else    MassCopy = КоличествоКопий;
  end;
```

---

## Пример 21: `GenDoc`

**Источник:** `Mac/Mbr/swgd700.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro GenDoc( addrMes )
  SetBuff( wlmes, addrMes );

  PrintLog(2,"Генерация документарного аккредитива по МТ700");
  var stat : integer = 0, ErrMsg : string = "";

  var LcObj : RsbLetterOfCredit = RsbLetterOfCredit();

  ReadFieldsAndFillObj(LcObj, wlmes);

  // Дозаполнить остальные поля аккредитива
  LcObj.Trn = wlmes.Trn;
  LcObj.Department = {OperDprt};
  if( (stat = LcObj.ChangeState(WLD_STATUS_LC_DEFER)) != 0 )
    ErrMsg = GetErrMsgEx(stat, "Ошибка при установке статуса аккредитива");
    RunError(ErrMsg, ErrMsg);
  end;
```

---

## Пример 22: `ExecuteStep`

**Источник:** `Mac/DLNG/VA/var060.mac`
**Тип:** `macro`
**Размер:** 55 строк

```rsl
MACRO ExecuteStep(Buffer, dl_tick, DocKind, ID_Operation, ID_Step)
var
    stat = 0, paym = TBfile("pmpaym.dbt");

    record tick( dl_tick );
    SetBuff( tick, dl_tick );

    _ID_Operation = ID_Operation;
    _ID_Step = ID_Step;

    GetOprDate( DATE_REP_PAY, @StepDate );

    if( StepDate > {curdate} )
       return VA_Err("Преждевременное выполнение шага запрещено.");
    end;

    VA_Get1stPlanPaym(tick.BofficeKind, tick.DealID, PM_PURP_PRINC_RET, paym);

    if(paym.rec.PayerAccount == "")
       return VA_Err("Ошибка при формировании платежа|Не задан счет плательщика");
    end;

    pm_obj = MyRsbPayment( paym.rec.PaymentID );
    ВалРасчетов = pm_obj.PayerFIID;

    if(not VA_IS_INTEGRATED(@ИнтегрРежимРаботы))
       stat = 1;
    end;

    if((ИнтегрРежимРаботы) AND (pm_obj.PayerBankID != {OurBank}) AND (pm_obj.FuturePayerAmount != 0))
       stat = VA_Err("Плановый платеж не скитован полностью");
    end;

    if((stat == 0) and not DoBkps(tick))
       stat = 1;
    end;

    if((stat == 0) and not SetFinishedToPaym(tick))
       stat = 1;
    end;

    if(stat == 0)
       stat = УВ_СписаниеВекселейПоСделкеСВнебаланса(tick, StepDate);
    end;

    if((stat == 0) and not SetEndedToBanners(tick))
       stat = 1;
    end;

    if((stat == 0) and not VA_InnerMoney_Repay(tick, StepDate, УВПолучСумПогаш))
       stat = 1;
    end;

    return stat;
END;
```

---

## Пример 23: `ExecuteStep`

**Источник:** `Mac/DLNG/VA/var040.mac`
**Тип:** `macro`
**Размер:** 18 строк

```rsl
MACRO ExecuteStep(Buffer, dl_tick)
    var DealDate, stat = 0;
    record tick(dl_tick);

    SetBuff(tick, dl_tick);
    
    DealDate = tick.DealDate;

    if(not WriteOff(tick, DealDate))
        stat = 1;
    end;
    
    if((stat == 0) and not VA_InnerFI(tick, DealDate, VA_GRNUM_SREPAY_EREQ, null, УВПогашениеЦБ))
        stat = 1;
    end;

    return stat;
END;
```

---

## Пример 24: `ПолучитьВУПолучаемыхЦБВМене`

**Источник:** `Mac/DLNG/VA/vaxutils.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
MACRO ПолучитьВУПолучаемыхЦБВМене(tick)
  var ВалютаУчета = -1;
  record dl_tick("dl_tick");

  copy(dl_tick, tick);

  VA_ForEachBanner(dl_tick, @ПолучитьВУ, VSORDLNK_K_BUY, @ВалютаУчета, "BL");

  return ВалютаУчета;
END;
```

---

## Пример 25: `ОпределитьОснованиеПроводки`

**Источник:** `Mac/DLNG/NETTING/dlntlib.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
MACRO ОпределитьОснованиеПроводки (ntg)
    var Основание = "Неттинг с ",
        pt = TRecHandler ("party");

    if (0==ПолучитьСубъекта(ntg.Contractor, pt))
        Основание = Основание + pt.rec.ShortName;
    else
        Основание = Основание + "неизвестным контрагентом";
    end;

    return String(Основание, " за ", ntg.ValueDate:m);
END;
```

---

## Пример 26: `ExecuteStep`

**Источник:** `Mac/DLNG/MMARK/mmcntre_j.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
MACRO ExecuteStep( Buffer, Document, DocKind, IDOperation, IDStep)

  debugbreak;
  record sfcontr( sfcontr );
  SetBuff( sfcontr, Document );
  DL_PrepareCarryBuffer (Buffer);

  ID_Operation = IDOperation;
  ID_Step      = IDStep;

  contr_pd = MMFirstDoc (DL_SFCONTR, sfcontr.ID, false);

  if (KvitAmounts[0] < $0)
      return 1;
  end;
```

---

## Пример 27: `ExecuteStep`

**Источник:** `Mac/DLNG/VEKSEL/vsv024rp.mac`
**Тип:** `macro`
**Размер:** 25 строк

```rsl
MACRO ExecuteStep(Buffer, dl_order, DocKind, ID_Operation, ID_Step)
var
    StepDate, stat = 0;

    record order( dl_order );
    SetBuff( order, dl_order );

    VS_CurrIDOperation = ID_Operation;
    VS_CurrIDStep      = ID_Step;

    if(GetOprStatus(VS_OPERSTATUS_VSDEALS_ENDED_ZPHR) != VS_OPERSTATUS_VSDEALS_ENDED_COMPLETE)
      msgbox ("Завершите шаг \"Передача записи для хранилища\", чтобы продолжить операцию выкупа");
      return 1;
    end;

    if(not VS_TestStepDate(DATE_REP_DOC, @StepDate, order.SignDate))
       return 1;
    end;

    if(not ПроводкиПоНалогам(order, StepDate)) /* удержать налоги, сформировать платежи, создать объекты НДР*/
      stat = 1;
    end;

    return stat;
END;
```

---

## Пример 28: `СформироватьОтчетДляПроводки`

**Источник:** `Mac/Cb/pr2161lib.mac`
**Тип:** `macro`
**Размер:** 58 строк

```rsl
MACRO СформироватьОтчетДляПроводки( pr_document, onlyPrimary )

  var IsDepo : bool = (pr_document.rec.Chapter == CHAPT5);
  var RecID : string = IfThenElse( IsDepo,
                       GetRecIDForCarryDepo(pr_document),
                       "ID (dacctrn_dbt.AccTrnID): " + string( pr_document.rec.AccTrnID ) );

  var Carry       = Проводка( pr_document.rec.Chapter );
  var ExRateCarry = Проводка( pr_document.rec.Chapter );
  var factr:TBFile = TBFile( "acctrn", "R", 0 );
  Carry.ДобавитьСторону( СторонаПроводки( pr_document.rec.Account_Payer, 
                                          pr_document.rec.FIID_Payer   , 
                                          pr_document.rec.Chapter      , 
                                          pr_document.rec.Sum_Payer    , 
                                          PRT_Debet                    ,
                                          pr_document.rec.Sum_NatCur   ,
                                          IsDepo                       ,
                                          pr_document.rec.AccTrnID     ) );
  Carry.ДобавитьСторону( СторонаПроводки( pr_document.rec.Account_Receiver, 
                                          pr_document.rec.FIID_Receiver   , 
                                          pr_document.rec.Chapter         , 
                                          pr_document.rec.Sum_Receiver    , 
                                          PRT_Credit                      ,
                                          pr_document.rec.Sum_NatCur      ,
                                          IsDepo                          ,
                                          pr_document.rec.AccTrnID        ) );
  
  МемориальныйОрдер2161У(  RecID,
                           pr_document.rec.Numb_Document ,
                           pr_document.rec.Date_Carry    ,
                           pr_document.rec.TypeDocument  ,
                           Carry                         ,
                           pr_document.rec.Ground        ,
                           IsDepo                        ).PrintReport();
                       
  if( not onlyPrimary and ( pr_document.rec.ExRateAccTrnID > 0 ) )
    factr.rec.AccTrnID = pr_document.rec.ExRateAccTrnID;    
    if( factr.GetEQ() )
      ExRateCarry.ДобавитьСторону( СторонаПроводки( factr.rec.Account_Payer, 
                                                    factr.rec.FIID_Payer   , 
                                                    factr.rec.Chapter      , 
                                                    factr.rec.Sum_Payer    , 
                                                    PRT_Debet              ,
                                                    factr.rec.Sum_NatCur   ) );
      ExRateCarry.ДобавитьСторону( СторонаПроводки( factr.rec.Account_Receiver, 
                                                    factr.rec.FIID_Receiver   , 
                                                    factr.rec.Chapter         , 
                                                    factr.rec.Sum_Receiver    , 
                                                    PRT_Credit                ,
                                                    factr.rec.Sum_NatCur      ) );
      return МемориальныйОрдер2161У( "ID (dacctrn_dbt.AccTrnID): " + string( pr_document.rec.AccTrnID ),
                                      factr.rec.Numb_Document ,
                                      factr.rec.Date_Carry    ,
                                      factr.rec.TypeDocument  ,
                                      ExRateCarry             ,
                                      factr.rec.Ground        ).PrintReport();
    end;
  end;
```

---

## Пример 29: `CheckConditions`

**Источник:** `Mac/DEPOSITR/chk_trn_grp.mac`
**Тип:** `macro`
**Размер:** 22 строк

```rsl
macro CheckConditions(trndoc)
  var ok = true;
  var doc = TRecHandler( "sbdepdoc.dbt" );

  if (NeedCheckTypeAccount(trndoc.Type_Account))
    doc.clear();
    doc.rec.IsCur = trndoc.IsCur;
    doc.rec.FNCash = trndoc.FNCash;
    doc.rec.Account = trndoc.Account;
    doc.rec.Referenc = trndoc.Referenc;
    doc.rec.ApplType = trndoc.ApplType;
    doc.rec.InSum = trndoc.Sum;
    doc.rec.iApplicationKind = trndoc.iApplicationKind;
    doc.rec.ApplicationKey = trndoc.ApplicationKey;
    doc.rec.TypeComplexOper = doc.rec.TypeOper = trndoc.TypeOper;
    doc.rec.Type_Account = trndoc.Type_Account;
    doc.rec.DepDate_Document = trndoc.Date_Document;
    doc.rec.CodClient = trndoc.CodClient;
    if (CheckAlgPoint(doc, 240) != 0)
      ok = false;
    end;
  end;
```

---

## Пример 30: `GetLatestOperDate`

**Источник:** `Mac/DEPOSITR/t2s_comm.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
macro GetLatestOperDate;

  var
    SK_DepDoc = KeyNum(DepDoc, 6),
    RecFound,
    OpFound = false,
    RetVal = Dep.Open_Date;


  DepDoc.Referenc = Dep.Referenc;
  DepDoc.Date_Document = {curdate};
  DepDoc.NumDayDoc = 32767;
  RecFound = GetLE(DepDoc);
  while(RecFound and (not OpFound)
    and (DepDoc.Referenc == Dep.Referenc))
    if((DepDoc.TypeOper != Расчет_Процентов)
      and (DepDoc.TypeOper != Зачисление_Процентов)
      and IsServDoc(DepDoc))
      RetVal = DepDoc.Date_Document;
      OpFound = true;
    end;
    RecFound = Prev(DepDoc);
  end;
```

---

## Пример 31: `NameTurnKind`

**Источник:** `Mac/Cb/rep_nu.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
MACRO NameTurnKind( Kind )
/*
FILE alg(namealg) ; /* алгоритмы выборов */
CONST ALG_NU_TURN = 111;

  alg.iTypeAlg = ALG_NU_TURN; /* Виды оборотов */
  alg.iNumberAlg = Kind; /* Номер вида */
  if ( getEQ(alg) ) return alg.szNameAlg;
  else return "":
  end;
```

---

## Пример 32: `FillBankContragent_camt`

**Источник:** `Mac/Mbr/swmx_camt_lib.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro FillBankContragent_camt(rsbcnf : RsbWldConfirmation, wlmes, TranslateID : string)
  record pmpttrf(pmpttrf); ClearRecord(pmpttrf);
  var IsPtFound : bool = false; // участник найден
  var SrvPmPtTrf : RsbPmPtTrf = rsbcnf.TrfParties();

  if(rsbcnf.DKFlag == WL_CREDIT)
    if( SrvPmPtTrf.FindByRole("DbtrAgt", pmpttrf) == 0 )
      IsPtFound = true;
    end;
  else
    if( SrvPmPtTrf.FindByRole("CdtrAgt", pmpttrf) == 0 )
      IsPtFound = true;
    end;
  end;
```

---

## Пример 33: `PrintOtherField`

**Источник:** `Mac/Mbr/swmesprn.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro PrintOtherField( имя, поле )
  FILE wltpfld(wltpfld) key 1;

  wltpfld.TpID = TRANSP_SWIFT;
  wltpfld.Name = имя;

  if( GetEQ( wltpfld ) )
    [###:#](имя, StrUpr(wltpfld.Description ));
    PrintMultiFields( поле, wltpfld.LenEdit, wltpfld.NumLines );
  else
    [###:#](имя, поле);
  end;
```

---

## Пример 34: `GenDoc`

**Источник:** `Mac/Mbr/fnsgdkwtx.mac`
**Тип:** `macro`
**Размер:** 127 строк

```rsl
macro GenDoc( addrMes )

  SetBuff( wlmes, addrMes );
  
  PrintLog(2,"Генерация УО по KWT");

  var field_name, field_value, block_name, err = 0;
  var FileName:string = "";
  var MesID:integer = 0, MesState:integer = 0;
  var isFirstResult:bool = true;
  var ResultCode:string = "";
  var DateTime:string = "";
  var needCreateError:bool = false;
  var Description, Code, Value;
  var ResultID = 0;
  var isErrorInserted = false;

  var RejectFlag:bool = false;
  GetRegistryValue( "PS\\REQOPENACC\\OPERATION\\Отвергать_Части_Выписки", V_BOOL, RejectFlag, err);
  
  while( СчитатьПоле( field_name, field_value, block_name ) )
    if( field_name == "ИмяФайла" )
      FileName = field_value;

      if( Index( FileName, "BZ1" ) == 1 )
        FileName = Substr( FileName, 5, StrLen( FileName ) - 4 - 9 )
      end;
 
      var select = "select mes.t_MesID, mes.t_State, mes.t_InsideAbonentID, mes.t_InsideAbonentCodeKind, mes.t_InsideAbonentCode " +
                   "  from dwlmes_dbt mes, dwlsess_dbt sess " +
                   "    where mes.t_SessionID = sess.t_SessionID " +
                   "      and upper(substr(sess.t_FileName, instr(sess.t_FileName, '\\', -1, 1) + 1)) = upper(:FILENAME || '.xml')";
      var params = makeArray( SQLParam("FILENAME", FileName) );
      var rs = execSQLselect( select, params, FALSE );

      if( rs and rs.moveNext() )
        MesID = rs.Value(0);
        MesState = rs.Value(1);
        wlmes.InsideAbonentID = rs.Value(2);
        wlmes.InsideAbonentCodeKind = rs.Value(3);
        wlmes.InsideAbonentCode = rs.Value(4);

        if( CheckOtherMess( MesID ) )
          return false;
        end;
      end;
    end;

    if( field_name == "ДатаВремяПроверки" )
      DateTime = field_value;
    end;

    var reqBlck = "Результат";
    var pos = index(block_name, reqBlck);
    if( (pos > 0) AND (pos+strlen(reqBlck) == strlen(block_name)+1 ) ) // проверим, что это последний блок
      if( field_name == "КодРезПроверки" )
        ResultCode = field_value;
      end;
      if( field_name == "Пояснение" )
        Description = field_value;
      end;
      if( field_name == "КодРекв" )
        Code = field_value;
      end;
      if( field_name == "ЗначРекв" )
        Value = field_value;
      end;

      if( (field_name == "_end") AND (isFirstResult == true) )
        isFirstResult = false;
        var NoChangeState:bool = false, State = -1;
        if( ResultCode != "01" )

          needCreateError = true;

          if( ( MesState == 25 ) and ( RejectFlag == false ) )
            ResultID = GetResultID( MesID );
            if( ResultID > 0 )
              /*Связь подтверждения с входящим сообщением */
              var meslnk = TRecHandler("wlmeslnk.dbt");
              meslnk.rec.MesID = wlmes.MesID;
              meslnk.rec.Direct  = "X";/*WLD_MES_IN*/
              meslnk.rec.ObjID   = ResultID;
              meslnk.rec.ObjKind = OBJTYPE_MESDEFECT;
              var MesLnkObj = RsbWlMesLnk( meslnk.rec.ObjKind, meslnk.rec.ObjID, meslnk.rec.Direct );            
              MesLnkObj.Insert( meslnk );
              MesLnkObj.Save();
            else
              if( FindOrigMessAndReceipt( MesID, FileName, 0 ) == TRUE )
                NoChangeState = TRUE;
                State = 100;
              else
                NoChangeState = FALSE;
                State = 0;
              end;
              DefectMes( MesID, NULL, NoChangeState, State );
            end;
          else 
            DefectMes( MesID, @ResultID );
          end;
          isErrorInserted = CreateWlError( ResultCode, Description, Code, Value, ResultID );
        else // ResultCode == "01"
          var DeliveryDate:date;

          if( (FindOrigMessAndReceipt( MesID, FileName, 1 ) == TRUE) OR (wlmes.State == WLD_STATUS_MES_DEFECT) )
            NoChangeState = true;
          else
            NoChangeState = false;
          end;

          ВставитьПодтверждениеОДоставке( MesID, NoChangeState, GetDate( DateTime ), GetllName( OBJTYPE_WLRESCODE_MNS, FNS_RP_APPROVED ), true )
        end;
      elif( needCreateError == true ) //isFirstResult == false
        if( field_name == "_end" ) // необходимо проверять блоками, иначе одна ошибка будет записываться несколько раз
          isErrorInserted = CreateWlError( ResultCode, Description, Code, Value, ResultID );
        end;
        if( ( MesID > 0 ) and ( RejectFlag == false ) )   
          DefectOtherMess( MesID );
        end;
      end;
    end;

    if( isErrorInserted and needCreateError )
      ResultCode = Description = Code = Value = "";
      isErrorInserted = false;
    end;
  end;
```

---

## Пример 35: `ExecuteStep`

**Источник:** `Mac/DLNG/DV/dvnop075.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro ExecuteStep( doc, FDoc, DocKind, ID_Operation, ID_Step )

  record ndeal(dvndeal);
  var Payment:RsbPayment;
  var PaymentID:integer = 0;
  var ДатаИсполненияШага:date;

  SetBuff(ndeal, FDoc);
  var FD = DVFirstDocNDeal(DocKind, ndeal);

  if (FD.ОтказОтИсполнения())
     return 0;
  end;
```

---

## Пример 36: `FillOwreqByPayDocType`

**Источник:** `Mac/Cb/ws_oo_type_PayDocType.mac`
**Тип:** `macro`
**Размер:** 19 строк

```rsl
macro FillOwreqByPayDocType(Owreq : TRecHandler, PayDocData : PayDocType)
  DebugPrint("FillOwreqByPayDocType", "Begin");

  Owreq.rec.InvoiceID = PayDocData.InvoiceID;
  Owreq.rec.InvoiceDate = PayDocData.InvoiceDate;
  Owreq.rec.SignAmountTax = PayDocData.SignAmountTax;
  Owreq.rec.Tax         = int(PayDocData.Tax);
  Owreq.rec.AmountTax   = ConvCurrUnits(PayDocData.AmountTax, PayDocData.CurrencyCode);
  Owreq.rec.Amount      = ConvCurrUnits(PayDocData.Amount, PayDocData.CurrencyCode);
  Owreq.rec.AmountToPay = ConvCurrUnits(PayDocData.AmountToPay, PayDocData.CurrencyCode);
  Owreq.rec.CurrCode    = PayDocData.CurrencyCode;
  Owreq.rec.PaymGround  = PayDocData.Purpose;
  Owreq.rec.ValidUntil  = PayDocData.ValidUntil;

  FillOwreqByPayeeType(Owreq, PayDocData.Payee);
  FillOwreqByPayerOrg (Owreq, PayDocData.PayerOrg);

  DebugPrint("FillOwreqByPayDocType", "End");
end;
```

---

## Пример 37: `ExecuteStep`

**Источник:** `Mac/DLNG/DV/dvnop071.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro ExecuteStep( doc, FDoc, DocKind, ID_Operation, ID_Step )

  record ndeal(dvndeal);
  var Payment:RsbPayment;
  var PaymentID:integer = 0;
  var ДатаИсполненияШага:date;

  SetBuff( ndeal, FDoc );
  var FD = DVFirstDocNDeal(DocKind, ndeal);

  if (FD.ОтказОтИсполнения())
     return 0;
  end;
```

---

## Пример 38: `ExecuteStep`

**Источник:** `Mac/DLNG/SECUR/old/scrou0327.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro ExecuteStep( doc, FDoc)

  record deal(dl_tick);       
  var    dat, FD, FD2, error; 

  SetBuff( deal, FDoc ); 
  FD = SPFirstDoc( deal, false );
//  FD2 = SPFirstDoc( deal, true );

  GetOprDate( FD.GetKindDate(DATE_DEALSETAVOIRISS), dat ); /*Дата поставки ц/б */
  if( dat > {curdate} )
     return SayErrorBuySale( deal, "Преждевременное выполнение шага запрещено." );
  end;
```

---

## Пример 39: `StartDepoAcc`

**Источник:** `Mac/DLNG/SECUR/scstartdepo.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
MACRO StartDepoAcc(DocumentID, IsWebService)
  var dl_comm = TBFile("dl_comm.dbt");
  var err = 0;

  dl_comm.rec.DocumentID = DocumentID;
  if(not dl_comm.GetEQ())
    msgbox("Ошибка поиска операции");
    return 1;
  end;
```

---

## Пример 40: `Печать_ОтчетСканирования`

**Источник:** `Mac/Cb/ostscan.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
MACRO Печать_ОтчетСканирования (Вызов,rec_step,Статус,Сообщение)

        setbuff (oprstep_rec,rec_step);

var stat;
        if (Вызов==Первый)
[                     Отчет о групповом выполнении шагов операций.    ];
[┌────────┬───────┬──────┬──────────────────────────────────────────────────────────────────────┐];
[│ Номер  │ Номер │Номер │                           Сообщение                                  │];
[│операции│ шага  │ошибки│                                                                      │];
[├────────┼───────┼──────┼──────────────────────────────────────────────────────────────────────┤];
        elif (Вызов==Ошибка)

                if (Статус == 0)
                        Сообщение = "Шаг выполнен успешно";
                end;
                
[│########│#######│######│######################################################################│]
(oprstep_rec.ID_Operation,oprstep_rec.ID_Step,Статус,Сообщение:w);

        elif (Вызов==Последний)
[└────────┴───────┴──────┴──────────────────────────────────────────────────────────────────────┘];
        end;
END;
```

---
