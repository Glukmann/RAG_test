# Практика: Математические и агрегатные функции (abs, SUM, IIF, round, min, max)

**Теория:** [BnRSL.md## Выражения]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `SfFormDocumentsBatch`

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

## Пример 2: `RunAction`

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

## Пример 3: `ExecuteStep`

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

## Пример 4: `ValLogProc`

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

## Пример 5: `GenMes`

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

## Пример 6: `ИзменитьСрокиИсполнения_ДляСделки`

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

## Пример 7: `SP_FillDealRQ`

**Источник:** `Mac/DLNG/SECUR/ws_deals_regenerate.mac`  
**Тип:** `private macro`  
**Размер:** 27 строк

```rsl
private macro SP_FillDealRQ( PanelDeal, RQ/*:CScRQ*/ ):integer

  var stat:integer = 0;

  /* Дальнейшее заполнение полей через макрос */
  stat = SP_FillDealRQMac( PanelDeal, RQ );

  if( stat == 0 )

    var DLRQACC/*:CScRQAcc = CScRQAcc()*/;
    /* найти реквизиты для ТО */
    var NewRq:Bool = ((RQ.RQAcc.ID == 0) or (FindDLRQACC(PanelDeal.RQAcc, RQ.RQAcc.ID, @DLRQACC) == false) or (DLRQACC.Party != SP_GetPartyID(RQ.Party))); /* если не нашли ранее использованные реквизиты или они не подходят, то подберем новые */
    if( NewRq or ((DLRQACC != null) and (DLRQACC.Fiid != RQ.RQAcc.Fiid)) )
       if( FindDLRQACCbyDocKind(PanelDeal.RQAcc, RQ.DocKind, RQ.DocID, SP_GetNameAlgNumberAlg(RQ.SubKind), SP_GetPartyID(RQ.Party), DLRQ_TYPE_UNKNOWN,
                                IIF(SP_GetNameAlgNumberAlg(RQ.SubKind) == DLRQ_SUBKIND_CURRENCY, SP_GetFIID(PanelDeal.Deal.CrncPay), SP_GetFIID(RQ.FI)), @DLRQACC) )
          SetRQAcc_ByRecordSharp(RQ.RQAcc, DLRQACC);
          //RQ.RQAcc = DLRQACC;
       else
          if((SP_GetNameAlgNumberAlg(RQ.SubKind) != DLRQ_SUBKIND_AVOIRISS) and (not NewRq)) //По ц/б реквизиты не обязательны. Для валюты если !NewRq, то оставим старые реквизиты.
             /* для денежных ТО, если не нашли ПР в нужной валюте, то ищем первую подходящую ПР с любой валютой */
             if( FindDLRQACCbyDocKind(PanelDeal.RQAcc, RQ.DocKind, RQ.DocID, SP_GetNameAlgNumberAlg(RQ.SubKind), SP_GetPartyID(RQ.Party), DLRQ_TYPE_UNKNOWN,
                                      IIF(SP_GetNameAlgNumberAlg(RQ.SubKind) == DLRQ_SUBKIND_CURRENCY, SP_GetFIID(PanelDeal.Deal.CrncPay), SP_GetFIID(RQ.FI)), @DLRQACC, SP_GetNameAlgNumberAlg(RQ.Type), true) )
                SetRQAcc_ByRecordSharp(RQ.RQAcc, DLRQACC);
                //RQ.RQAcc = DLRQACC;
             else
                stat = 31813; /* Не найдены платежные реквизиты для ТО */
             end;
```

---

## Пример 8: `Draw`

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

## Пример 9: `БУ_ПроводкиИзмененияСроковИсполнения_ДляСделки`

**Источник:** `Mac/DLNG/SECUR/scchdateacc.mac`  
**Тип:** `macro`  
**Размер:** 26 строк

```rsl
macro БУ_ПроводкиИзмененияСроковИсполнения_ДляСделки( FD:SPFirstDoc, Action:Integer, FactDate:Date, PlanDate:Date, ExecDate:Date, GrDealID:integer )
  var AvanceSum = $0, PaySum = $0, CarrySum, DealType, Ground;
  var DebetAcc, CreditAcc, ChdAcc, FIRole, ForvAcc, ForvAccMinus, ForvAccPlus, BppCat, BppCurr;
  var ExistLink = false, NeedInsertDepoDraft = false, err, stat, RegistrDate;
  var Sum, N = 0, MinDate = date(0,0,0);

  var FD1, FD2, save_BegDateM = null, save_FinDateM = null, save_BegDateP = null, save_FinDateP = null;
  var MnOD = TRecHandler("account");
  var PlOD = TRecHandler("account");
  var MnOD_2 = TRecHandler("account");
  var PlOD_2 = TRecHandler("account");
  var NewAcc = TRecHandler("account");
  var UpdateAcc = true, i = 0;
  var DateKind = 0;
  var ReqOrCom = "";

  if( Action == DEALCALC_ACTION_BEFORE_PAY ) /*досрочная оплата*/
       
       if( (ТОЗакрыто( FD.GetRQ(DLRQ_TYPE_DELIVERY) ) != true) AND 
           (FD.DateArray[DATE_DEALSETAVOIRISS_PLAN] == FactDate)
         )  /*SCR 58456*/
          if( MsgBoxEx( "Плановая дата поставки равна дате досрочной оплаты.|Выполнять досрочную оплату ?",
              MB_YES+MB_NO, IND_NO, 
              "Досрочная оплата", "Подтверждение начала операции" ) != IND_YES ) 
             return 1; 
          end;
```

---

## Пример 10: `SvOpReservLine`

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

## Пример 11: `SaveP`

**Источник:** `Mac/Cb/ws_getparty.mac`  
**Тип:** `private macro`  
**Размер:** 36 строк

```rsl
private macro SaveP(PartyInfo, Party : @RsbParty, SkipCheckPartyPapers)

  PT_PrintDebug( "ws_getparty.mac.log", "PartyInfo.Party.legalform=" + PartyInfo.Party.legalform);

  record persnidcRecord("persnidc.dbt");
  record persnRecord("persn.dbt");

  clearRecord(persnidcRecord);
  clearRecord(persnRecord);

  var d, m, y;

  var stat = true;

  // проверить существование свойства Party в объекте PartyInfo
  var iprop = GenPropID(PartyInfo, "Party");

  if(iprop != -1) // обращаемся к свойству, если оно существует в объекте

    var wParty = GenGetProp(PartyInfo, "Party");

    // работа с объектом Party

    // Party.OwnerKind           = wParty.ownerkind;
    Party.LegalForm           = wParty.legalform;
    Party.ShortName           = wParty.shortname;
    Party.FullName            = wParty.name;
    // Party.AddName             = wParty.addname;
    Party.NRCountry           = wParty.nrcountry;
    Party.OfshoreZone         = wParty.ofshorezone;
    if(PartyInfo.Party.LegalForm == 1)
      Party.OKPO                = wParty.okpo;
      Party.SuperiorID          = wParty.superior;
    else
      Party.IsNotResident       = wParty.notresident;
    end;
```

---

## Пример 12: `DVCalcFrVal`

**Источник:** `Mac/DLNG/DV/dvAlgCalcFrValOFAv.mac`  
**Тип:** `macro`  
**Размер:** 39 строк

```rsl
MACRO DVCalcFrVal( pFrVal:TRecHandler, pDEAL:TRecHandler, pFI_1:TRecHandler, pFI_2:TRecHandler ):integer

  var Fininstr = TRecHandler( "fininstr.dbt" );

  if( pFrVal.rec.Date == date(0,0,0) )
     MsgBox("Не задана дата расчёта.");
  elif( (pDEAL.rec.DVKind != DV_FORWARD) and (pDEAL.rec.DVKind != DV_FORWARD_T3) )
     MsgBox("В операции некорректно указан алгоритм расчета. ПФИ не является форвардом на ценную бумагу.");
  elif( ПолучитьФинИн(pFI_1.rec.FIID, Fininstr) )
     MsgBox("Не найден ФИ c ID = " + pFI_1.rec.FIID + ".");
  elif( Fininstr.rec.FI_Kind != FIKIND_AVOIRISS )
     MsgBox("В операции некорректно указан алгоритм расчета. ПФИ не является форвардом на ценную бумагу.");
  elif( pFI_1.rec.OpenDate == UNSET_CHAR )
     MsgBox("В операции некорректно указан алгоритм расчета. ПФИ не является форвардом с открытой датой.");
  elif( (pFI_1.rec.PriceFIID != Fininstr.rec.FaceValueFI) and (FI_IsCouponAvoiriss(Fininstr)== true) )
     MsgBox("В операции некорректно указан алгоритм расчета. ПФИ является форвардом на купонную ценную бумагу, валюта номинала которой не равна валюте цены форварда.");
  else
     var Course:double = 0.0;  /*Рыночная цена ц/б, которая является БА форварда*/
     if( not ПолучитьКурсЗаданногоTипа(@Course, pFI_1.rec.FIID, NATCUR, RATETYPE_MARKET_PRICE, pFrVal.rec.Date, true, null, DV_RATETYPE_CBR ) or
         (Course == 0.0) )
        MsgBox("Не найден курс вида 'Рыночная цена' для FIID = " + String(pFI_1.rec.FIID));
     else
        var F:money = 0.0, AccFIID:integer = IIF(pFI_1.rec.AccFIID != ALLFININSTR, pFI_1.rec.AccFIID, pFI_1.rec.PriceFIID),
            Sвба:double = 0.0, Sвр:double = 0.0, S1:money = 0.0, S2:money = 0.0;

        if( pFrVal.rec.Date <= pDEAL.rec.BeginDate )
           F = pFI_1.rec.Price;
        else
           var S:money = pFI_1.rec.Price + НКД(pFI_1.rec.FIID, 1, pFrVal.rec.Date);
           var Stat:integer = 0;
           var Днач:date = pDEAL.rec.BeginDate;
           var F0:money = 0;

           while( Stat == 0 )
              var Доконч:date = date(0,0,0);
              if( DV_GetDrawingDate(pFI_1.rec.FIID, Днач, pFrVal.rec.Date, @Доконч) == false )
                 Stat = 1;
                 Доконч = pFrVal.rec.Date;
              end;
```

---

## Пример 13: `SP_CreateDealAllRQ`

**Источник:** `Mac/DLNG/SECUR/ws_deals_regenerate.mac`  
**Тип:** `private macro`  
**Размер:** 20 строк

```rsl
private macro SP_CreateDealAllRQ( PanelDeal/*CScPanelDeal*/ )

  var stat:integer = 0;
  var OperGroup = SP_GetOperationGroup_( PanelDeal.Deal.DealType, PanelDeal.Deal.BofficeKind, IIF(PanelDeal.Deal.Flag1, "X", ""), IIF(PanelDeal.Deal.Flag4, "X", "") );
  var Kind:integer = DLRQ_KIND_UNKNOWN;
  var DealPart:integer = 0;
  var EnsureTree = TArray();
  var Ensure = null;
  var EnsureCount:Integer = 0;

  if( PanelDeal.Deal.BofficeKind == DL_SECURITYDOC ) /* покупка, продажа, РЕПО */
     /* ТО для сделок из одной части, а также 1-я часть РЕПО */
     DealPart = 1;

     /* по деньгам */
     if( IsBUY(OperGroup) )
        Kind = DLRQ_KIND_COMMIT;
     else
        Kind = DLRQ_KIND_REQUEST;
     end;
```

---

## Пример 14: `ClearDealRQACC`

**Источник:** `Mac/DLNG/SECUR/ws_deals_regenerate.mac`  
**Тип:** `private macro`  
**Размер:** 21 строк

```rsl
private macro ClearDealRQACC( PanelDeal/*CScPanelDeal*/ ):integer

  var stat:integer = 0;
  var OperGroup = SP_GetOperationGroup_( PanelDeal.Deal.DealType, PanelDeal.Deal.BofficeKind, IIF(PanelDeal.Deal.Flag1, "X", ""), IIF(PanelDeal.Deal.Flag4, "X", "") );
  var ToDelete:bool = true;
  var i:integer = 0;

  var RQAccTA = PanelDeal.RQAcc;

  while( i < RQAccTA.size() )
     if( RQAccTA(i).Action != OperationKind_Delete )
        ToDelete = true;

		// Оставляем ТО, которые используются (отсальное удалено по 200762)
        var RQ = PanelDeal.RQ;
        var j:integer = 0;
        while( j < RQ.size() )
           if( (RQ(j).RQAcc.ID == RQAccTA(i).ID) and (RQ(j).Action != OperationKind_Delete) )
              ToDelete = false;
              break;
           end;
```

---

## Пример 15: `AfterSaveP`

**Источник:** `Mac/Cb/ws_getparty.mac`  
**Тип:** `private macro`  
**Размер:** 34 строк

```rsl
private macro AfterSaveP(PartyInfo, PartyID, ErrorMessage : @WsErrorMessage)

  PT_PrintDebug( "ws_getparty.mac.log", "AfterSaveP");

  file partyname (partyname) key 0 write;
  file partykname (partykname) key 0;

  file ptsvdp (ptsvdp) key 0 write;
  file client (client) key 5 write;

  var stat = true;

  var PartyKind = GetPartyKind(PartyInfo.ListKind);

  // проверить существование свойства PartynameCollection в объекте PartyInfo
  var iprop = GenPropID(PartyInfo, "PartynameCollection");

  if(iprop != -1) // обращаемся к свойству, если оно существует в объекте

    var wPartynameCollection = GenGetProp(PartyInfo, "PartynameCollection");
    
    var i = 0;
    
    if(wPartynameCollection != NULL)

      while(i < wPartynameCollection.size)
      
        if(wPartynameCollection[i].action == PT_CREATE)
        
          stat = PartyNameAddExt(PartyID, wPartynameCollection[i].nametypeid, wPartynameCollection[i].name);
          
          if(stat == false)
            break;
          end;
```

---

