# Практика: Обработка ошибок и исключений (OnError, BtrError)

**Теория:** [BnRSL.md## Комментарии]

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

## Пример 2: `ExecuteStep`

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

## Пример 3: `СчитатьПолеИзБуфера`

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

## Пример 4: `GetGr_Docs_Date`

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

## Пример 5: `ProcFormTOFK`

**Источник:** `Mac/Cb/mfo_lib.mac`  
**Тип:** `macro`  
**Размер:** 45 строк

```rsl
macro ProcFormTOFK(PrnProtocol)

  var error;
  var Is_Form_Name_TOFK : bool = false;
  var cmd, rs;
  var query : string = "";
  var PartyID : integer = 0;
  var ShortNamePartyID : string = "";
  var ACCNTCBRBIC : string = NULL;
  var PartyBIC : string = "";
  var PartyID_ACCNTCBRBIC : integer = 0;
  var ShortNamePartyID_ACCNTCBRBIC : string = "";
  var Name_TOFK : string = "";
  var str : string = "";
  
  ProtocolTOFK = TArray(false, 10000, 10000);
      
  GetRegistryValue("CB\\BNKSIMPORT\\FORM_NAME_TOFK", V_BOOL, Is_Form_Name_TOFK, error, false, {oper}); // После импорта ED807 обновить наименование субъекта вида 17 для ТОФК
   
  if(Is_Form_Name_TOFK == true)
    
    query = "SELECT p.T_PartyID, p.T_ShortName FROM dparty_dbt p, dpartyown_dbt po WHERE p.T_PartyID = po.T_PartyID AND po.T_PartyKind = " + PTK_OFK;
    
    cmd = RsdCommand(query); 
    cmd.execute;
    rs = RsdRecordset(cmd);
    while(rs.moveNext)
      PartyID = 0;
      ShortNamePartyID = "";
      ACCNTCBRBIC = NULL;
      PartyBIC = "";
      PartyID_ACCNTCBRBIC = 0;
      ShortNamePartyID_ACCNTCBRBIC = "";
      Name_TOFK = "";    
    
      PartyID          = rs.value(0);
      ShortNamePartyID = rs.value(1);
      
      ACCNTCBRBIC = GetACCNTCBRBIC(PartyID);
      PartyBIC = GetBIC(PartyID);
    
      if(ACCNTCBRBIC == NULL)
        ProtocolTOFK[ProtocolTOFK.size] = "Для субъекта с кодом " + PartyBIC + " не найден действующий корреспондентский счет";
        continue;
      end;
```

---

## Пример 6: `UpdateSfDefSum`

**Источник:** `Mac/Cb/sfcrpaybatch.mac`  
**Тип:** `macro`  
**Размер:** 34 строк

```rsl
macro UpdateSfDefSum(sfdefArray)
  var stat = 0;
  var nArray = sfdefArray.size();
  var i = 0;
  var sfdefsumhistCache = RsbSQLInsert("sfdefsumhist.dbt");

  var DefIDArray      = TArray;
  var FeeTypeArray    = TArray;

  var sizea = 0;
  while( i < nArray )
    var IndexSfDefArray = i;
    if((sfdefArray[IndexSfDefArray].IsNDSSumReset == true ) AND (sfdefArray[IndexSfDefArray].Error == 0))
      var sfdefsumhist = TRecHandler("sfdefsumhist.dbt");
      ClearRecord( sfdefsumhist );

      sfdefsumhist.rec.FeeType     = sfdefArray[IndexSfDefArray].sfdef.rec.FeeType;
      sfdefsumhist.rec.ID          = sfdefArray[IndexSfDefArray].sfdef.rec.ID;
      sfdefsumhist.rec.OperationID = sfdefArray[IndexSfDefArray].oprID_Operation;
      sfdefsumhist.rec.StepID      = sfdefArray[IndexSfDefArray].oprID_Step;
      sfdefsumhist.rec.Sum         = sfdefArray[IndexSfDefArray].sfdef.rec.Sum;
      sfdefsumhist.rec.SumNDS      = sfdefArray[IndexSfDefArray].sfdef.rec.SumNDS;
      
      sfdefsumhistCache.AddRecord( sfdefsumhist );

      var IncDocID = String(sfdefArray[IndexSfDefArray].sfdef.rec.FeeType:5)+String(sfdefArray[IndexSfDefArray].sfdef.rec.ID:10);
      IncDocID = StrSubst( IncDocID, " ", "0" );
      AddDocumentToStepMass(2007, IncDocID, sfdefArray[IndexSfDefArray].oprID_Operation, sfdefArray[IndexSfDefArray].oprID_Step); // SFDEF_SUM_HIST       = 2007

      DefIDArray[i]      = sfdefArray[IndexSfDefArray].sfdef.rec.ID;
      FeeTypeArray[i]    = sfdefArray[IndexSfDefArray].sfdef.rec.FeeType;

      sizea = sizea + 1;
    end;
```

---

## Пример 7: `DepoSfPay`

**Источник:** `Mac/Cb/sfcrpaybatch.mac`  
**Тип:** `private macro`  
**Размер:** 31 строк

```rsl
private macro DepoSfPay( sfdefArray )
  var stat = 0;
  var nArray = sfdefArray.size();
  var i = 0;
  var j = 0;

  var sqlString, rs, cmd;
  cmd = RsdCommand( "DELETE FROM dsfdefdepo_tmp" );
  cmd.execute();

  var sfdefdepoCache = RsbSQLInsert("sfdefdepo.tmp");

  var sizea = 0;
  while( i < nArray )
    var IndexSfDefArray = i;
    var NeedDepo = IsDepoSfPay( sfdefArray[IndexSfDefArray].sfdef.rec.FeeType, sfdefArray[IndexSfDefArray].sfdef.rec.CommNumber );

    if((sfdefArray[IndexSfDefArray].SfDef.rec.Status == SFDEFCOM_STATUS_PAYED) AND (sfdefArray[IndexSfDefArray].Error == 0) AND NeedDepo)

      var sfdefdepo = TRecHandler("sfdefdepo.tmp");
      ClearRecord( sfdefdepo );
      sfdefdepo.rec.FeeType     = sfdefArray[IndexSfDefArray].sfdef.rec.FeeType;   
      sfdefdepo.rec.SfDefID     = sfdefArray[IndexSfDefArray].sfdef.rec.ID;     
      sfdefdepo.rec.Date        = sfdefArray[IndexSfDefArray].DateCarry;
      sfdefdepo.rec.OperationID = sfdefArray[IndexSfDefArray].oprID_Operation; 
      sfdefdepo.rec.StepID      = sfdefArray[IndexSfDefArray].oprID_Step;     
      
      sfdefdepoCache.AddRecord( sfdefdepo );

      sizea = sizea + 1;
    end;
```

---

## Пример 8: `CreateOutFileName`

**Источник:** `Mac/Cb/fm_frzchkout.mac`  
**Тип:** `private macro`  
**Размер:** 18 строк

```rsl
private macro CreateOutFileName( Date_Seance, Seance, Repeat, FileKind )
  
  var day, mon, year, fname, ext;
  var OutFileName;

  var error;
  /* вид кода филиала */
  var BankID, DprtCodeParty, DprtCodeKind;
  OutFileType = DefineFileType( Repeat );

  DateSplit( Date_Seance, day , mon, year );

  /* имя файла для КФМ*/
//  if( FileKind == 0 )
    fname = SubStr( {MFO_Bank}, 5, 5 ) + string(OutFileType);
    if( day < 10 ) 
       fname = fname + "0" ;
    end;
```

---

## Пример 9: `DL_GetTxRate_Limit`

**Источник:** `Mac/DLNG/dltxrate.mac`  
**Тип:** `macro`  
**Размер:** 25 строк

```rsl
macro DL_GetTxRate_Limit(CalcDate:date, Kind:integer, FIID:integer, Period:integer, StRate:@double, Error:@string, DealDate:Date, CalcKind:integer)
  var DlTxRate_Cur = TRecHandler( "dltxrate_cur.dbt" );
  var DlTxRate_Nat = TRecHandler( "dltxrate_nat.dbt" );
  var cbkrt = TRecHandler( "cbkeyrate.dbt" ); //буфер записи с данными ключевой ставки

  var Diff = 0.0;
  var cmd, DataSet;
  var DiffMax = 0, DiffMin = 0;

  StRate = 0.0;
  Error = "";

  if( FIID == NATCUR )

     if(DealDate < date(1,1,2015))/*Если валюта долгового обязательства  рубли и дата заключения ранее 01.01.2015*/
        if (not СтавкаРефинансированияЦБ (NATCUR, CalcDate, StRate))
           Error = "Не найдена ставка рефинансирования ЦБ РФ на "+DateToStr(CalcDate)+".";
        else
           if( DL_GetTxRateNatOnDate( CalcDate, DlTxRate_Nat ) )
       
              if( Kind == СТ_269_ПРИВЛЕЧЕНИЕ )
                 Diff = SQL_ConvTypeSum(DlTxRate_Nat.rec.max_diff);
              else
                 Diff = SQL_ConvTypeSum(DlTxRate_Nat.rec.min_diff);
              end;
```

---

## Пример 10: `GetESAccRest`

**Источник:** `Mac/Cb/GkboEsInfo.mac`  
**Тип:** `macro`  
**Размер:** 46 строк

```rsl
macro GetESAccRest(param: string, message: string, chapter : integer ): integer  
  var stat = 0;
  var Error : string = "";
  var xml = CreateXMLParser();
  xml.loadXML(param);
  var EsAccRestMessageFields = TEsAccRestMessageFields();
  if( ParseParameters( xml, @EsAccRestMessageFields ) and CheckParams( EsAccRestMessageFields, @Error ) )
    for( var Acc, EsAccRestMessageFields.AccList )
      var rs : RsdRecordset = execSQLselectPrm
        ( "select account.t_AccountID as t_AccountID, account.t_Department as t_Department, dp_dep.t_PartyID as t_DepPartyID, account.t_Code_Currency as t_FIID " +
          "  from daccount_dbt account, dfininstr_dbt fininstr, ddp_dep_dbt dp_dep " +
          " where account.t_Code_Currency = fininstr.t_FIID " +
          "   and fininstr.t_ISO_Number = :AccFI " +
          "   and account.t_Account = :Account " +
          "   and account.t_Chapter = :Chapter " +
          "   and dp_dep.t_Code(+) = account.t_Department ",
          SQLParam( "AccFI",   Acc.AccFI ),
          SQLParam( "Account", Acc.Account ),
          SQLParam( "Chapter", chapter ) );

      if(rs and rs.moveNext())
        var DepartmentBIC : string = ПолучитьКодСубъекта(rs.value( "t_DepPartyID" ), PTCK_BIC);
        var BankRegNum : string = ПолучитьКодСубъекта(rs.value( "t_DepPartyID" ), PTCK_BANKREGNUM);
        BankRegNum = GetSymbolsAfterSlash(BankRegNum);

        if( Acc.AccPeriod.BeginDate == Acc.AccPeriod.EndDate )
          FillEsAccRest( EsAccRestMessageFields.DocKind, EsAccRestMessageFields.ReqType,
                         Acc.Account, rs.value( "t_AccountID" ), 
                         Acc.AccFI, rs.value( "t_FIID" ), rs.value( "t_Department" ), 
                         DepartmentBIC, BankRegNum, Acc.AccPeriod.BeginDate, Acc.AccPeriod.BeginDate,
                         chapter, EsAccRestMessageFields.RegPartyKind
                       );
        else
          FillEsAccRest( EsAccRestMessageFields.DocKind, EsAccRestMessageFields.ReqType,
                         Acc.Account, rs.value( "t_AccountID" ), 
                         Acc.AccFI, rs.value( "t_FIID" ), rs.value( "t_Department" ), 
                         DepartmentBIC, BankRegNum, Acc.AccPeriod.BeginDate, Acc.AccPeriod.BeginDate,
                         chapter, EsAccRestMessageFields.RegPartyKind
                       );
          FillEsAccRest( EsAccRestMessageFields.DocKind, EsAccRestMessageFields.ReqType,
                         Acc.Account, rs.value( "t_AccountID" ), 
                         Acc.AccFI, rs.value( "t_FIID" ), rs.value( "t_Department" ), 
                         DepartmentBIC, BankRegNum, Acc.AccPeriod.EndDate, Acc.AccPeriod.EndDate,
                         chapter, EsAccRestMessageFields.RegPartyKind
                       );
        end;      
```

---

## Пример 11: `GetObjectLinkInfo`

**Источник:** `Mac/Cb/ws_objlinks.mac`  
**Тип:** `macro`  
**Размер:** 30 строк

```rsl
macro GetObjectLinkInfo(ObjectType : integer, ObjectID : integer)

  //DebugBreak;

  var responseBuilder = WebResponseBuilder;
  var error           = WsErrorMessage;
  var question        = WsQuestion;

  var ObjectIDStr = GetObjectIDStr(ObjectType, ObjectID);

  var p = TWsObjectLinkInfo();

  p.ObjectTypeName      = GetObjectTypeName(ObjectType);
  p.ObjLinkTypes        = GetObjLinkTypes(ObjectType);

  p.ObjLinksCollection  = TArray;
  p.ObjLinksCollection.size = 5;

  var i:integer = 0;

  while( i < p.ObjLinkTypes.size() )

    var OL = TWsObjLinks();

    OL.ObjectType = p.ObjLinkTypes[i];
    OL.ObjLinks = CB_GetObjLinks(ObjectType, p.ObjLinkTypes[i], ObjectIDStr);

    if(OL.ObjectType == OBJTYPE_CURRENCY)
      p.ObjLinksCollection[0] = OL;
    end;
```

**Комментарий автора:**
DebugBreak;

---

## Пример 12: `CheckObj`

**Источник:** `Mac/Mbr/sfrcofrs1.mac`  
**Тип:** `macro`  
**Размер:** 57 строк

```rsl
macro CheckObj( addrReq )
  record Req(reqchnga);
  SetBuff(Req, addrReq);
/*Вторая очередь реализации
  // массив, в хранящий список номеров проверок, соответствие номера и названия см. fnsMesAccCommon.mac
  var ArrayValidations : TArray = makeArray ( GenMesCheckBankName,
                                              GenMesCheckBankINN,
                                              GenMesCheckBankSizeINN,
                                              GenMesCheckBankKPP,
                                              GenMesCheckBankSizeKPP,
                                              GenMesCheckBankSymbolKPP,
                                              GenMesCheckBankExistIFNS,
                                              GenMesCheckIFNShasCode,
                                              GenMesCheckBankRegNumb,
                                              GenMesCheckDepRegNumb,
                                              GenMesCheckBankBIC,
                                              GenMesCheckBankOGRN,
                                              GenMesCheckBankSizeOGRN,
                                              GenMesCheckClientName,
                                              GenMesCheckClientFIO,
                                              GenMesCheckClientINN_v5_14,
                                              GenMesCheckClientSizeINN,
                                              GenMesCheckClientKPP,
                                              GenMesCheckClientSizeKPP,
                                              GenMesCheckClientSymbolKPP,
                                              GenMesCheckClientOGRN,
                                              GenMesCheckClientSizeOGRN,
                                              GenMesCheckContractNumber,
                                              GenMesCheckEmployeeSigningMSG,
                                              GenMesCheckChangePropertis,
                                              GenMesCheckBankAddressExistIndex,
                                              GenMesCheckBankAddressSizeIndex,
                                              GenMesCheckBankAdressRegionCode,
                                              GenMesCheckBankAdressSizeRegionCode,
                                              GenMesCheckBankRegionCodeExist,
                                              GenMesCheckBankAdressExistLocality,
                                              GenMesCheckNotMatchPropetis,
                                              GenMesCheckTypeAccCode,
                                              GenMesCheckClientChangeGround,
                                              GenMesCheckNotLatinSymbInClientFIO,
                                              GenMesCheckNotLatinSymbInClientFIOBeforeChanges,
                                              GenMesCheckClientFIO_513,
                                              GenMesCheckClientFIOBeforeChanges,
                                              GenMesCheckClientKPPNonResident,
                                              GenMesCheckTypeAccCodeOld
                                             );

  return MNS_CommonCheck( Req, ArrayValidations, ACCMSG_KIND_CHNG, fns311p_version_514 );
*/
  var XmlMode : WorkWithXmlMesDocument = WorkWithXmlMesDocument();
  var ArrayValidations : TArray = makeArray ( GenMesCheckChangePropertis );
  return SFR_CommonCheck( Req, ArrayValidations, ACCMSG_KIND_CHNG, 0 );

OnError(er)
  std.msg(RsbGetErrorEx(er));
  return FALSE;
end;
```

---

## Пример 13: `ExecuteParamStep`

**Источник:** `Mac/DLNG/SECUR/nptxwrt010.mac`  
**Тип:** `macro`  
**Размер:** 19 строк

```rsl
macro ExecuteParamStep( kind_oper, DocKind, FDoc, ID_Operation, ID_Step )
  record nptxop("nptxop");
  var err = 0;
  var v_MMVB_Code = "", v_MMVB_ID = -1;
  var MaxSumIIS = 0;
  var QueryInWrt = "";
  var year;
  var mes = "";
  var OperID = "";
  var notes;

  SetBuff( nptxop, FDoc );

  OperID = string(nptxop.ID:34:o);
  notes = RsbObjNotes(OBJTYPE_WRTMONEY, OperID);
  
  if( not InsertOprStatus(46071, 1)) //Установить ДО = Открыт
      return Error( "Ошибка при установке статуса вида \"Установить ДО\" операции" );        
  end;
```

---

## Пример 14: `ЗаписатьBasicHeaderBlock`

**Источник:** `Mac/Mbr/swiftout.mac`  
**Тип:** `macro`  
**Размер:** 19 строк

```rsl
macro ЗаписатьBasicHeaderBlock()
  var BankCode, Destination, BranchCode, НомерТерминала;
  var error;

  BankCode = ПолучитьКодСубъекта( {OurBank}, PTCK_SWIFT, error );
  if( error ) ErrExport( "Не найден SWIFT-код Отправителя сообщения! " ); return FALSE; end;

  Destination = SubStr(BankCode,1,Len_BIC_Destination);
  if(StrLen(Destination) != Len_BIC_Destination) ErrExport( "Неправильно указан Отправитель сообщения (BIC)!" ); return FALSE; end;
  BranchCode = SubStr(BankCode,Len_BIC_Destination+1,Len_BIC_BranchCode);
  if( (BranchCode!="")AND(StrLen(BranchCode) != Len_BIC_BranchCode) ) ErrExport( "Неправильно указан Отправитель сообщения (код отделения)!" ); return FALSE; end;
  if(BranchCode=="") BranchCode=MkStr(CodeFor(СимволBICПоУмолчанию),Len_BIC_BranchCode); end;
  /* !!! Код приложения всегда FIN, ApplicationID=01 */

  if( ВидТерминала == TPFRMT_PCC )
     НомерТерминала = "A";
     if(НомерСессии == NULL)
       НомерСессии = ".SS.";
     end;
```

---

## Пример 15: `GenDoc_v2021_3_0`

**Источник:** `Mac/Mbr/ufgd101.mac`  
**Тип:** `macro`  
**Размер:** 25 строк

```rsl
macro GenDoc_v2021_3_0( addrMes, type )
  var xml:object = ActiveX( "MSXML.DOMDocument" );
  var Строка, Сумма, Corschem, Currency, Error, TagPayer, TagPayee, PaytKind;
  var DebetCredit = PRT_Credit;

  /*Для аккредитивов*/
  var Representation  :string,      /*Платеж по представлению*/
      AddCondition    :string,      /*Дополнительные условия*/
      PayCondition    :string,      /*Условия оплаты*/
      AkkrCover       :string,      /*Покрытие*/
      AkkrAccount     :string,      /*счет получателя*/
      AkkrType        :string,      /*Тип аккредитива*/
      AkkrExpire      :string,      /*Срок действия аккредитива*/
      AcptAccNo       :string;      /*Номер счёта по учёту аккредитивов*/

  SetBuff( wlmes, addrMes );

  PrintLog( 2, "Генерация платежа по " + type );

  var ErrorMes = "";
  if( ( InList( type, ED101, ED103, ED104, ED105 ) ) and isDuplicated( wlmes, ErrorMes ) )
    if ( ErrorMes != "" )
      std.msg(ErrorMes);
      return false;
    end;
```

---

## Пример 16: `ПолучитьОбщиеПараметрыСводного`

**Источник:** `Mac/Mbr/swsm102n.mac`
**Тип:** `macro`
**Размер:** 59 строк

```rsl
macro ПолучитьОбщиеПараметрыСводного( publicCharges, publicRate, publicBankOperationCode )
   var IsFirst = TRUE, field_value, CurrentCode, error, TextError;

   publicCharges = null;
   publicRate = null;

   PaymMulty.SubSplittedPayment = wlpmpaym.PaymentID;
   PaymMulty.CreatedInSS = 1;   
   while( OneStepMultyPaym( IsFirst, wlpmpaym.PaymentID ) )      

      /* Ищем свойства */
      if( FindPayment( PaymMulty.PaymentID, 0, 0, 0, 0, true, 0, wlpmpropdeb, wlpmpropcred, wlpmrmprop ) != 0 )
         std.out( 2, "PaymentID: " + PaymMulty.PaymentID );
         RunError( "|Не найден платеж" );
      end;

      field_value = GetCommisCode (wlpmrmprop.ComissCharges);

      if ( IsFirst )
          publicCharges = field_value;
      elif ( (valtype(publicCharges)!=V_UNDEF) AND (publicCharges!=field_value) )
          publicCharges = null;
      end;

      if( (PaymMulty.FIID != PaymMulty.PayFIID) AND (PaymMulty.Rate != 0.0) )
         if ( IsFirst )
            publicRate = DefineSWIFTRateByPmPaym(PaymMulty);
         elif ( (valtype(publicRate)!=V_UNDEF) AND (publicRate!=DefineSWIFTRateByPmPaym(PaymMulty)) )
           publicRate = null;
         end;
      else
         publicRate = null;
      end;

      CurrentCode = "";
      NotesPaymentSelve.ReadNextNote( PaymMulty.PaymentID, BankOperationCodeField, CurrentCode, error );
//      if ( not error )
//        ЗаписатьПолеЛог( BankOperationCodeField, CurrentCode ) ;
//      end;
      /* Убедимся, что нет конфликтующих кодов */
      TextError = NotesPaymentSelve.ReadNextNote( PaymMulty.PaymentID, BankOperationCodeField, CurrentCode, error );
      if ( error )
         RunError( "|" + TextError );
      end;
      if ( IsFirst )
         publicBankOperationCode = CurrentCode;
      else
         if ( publicBankOperationCode!=CurrentCode )
            publicBankOperationCode = BANKOPERCODE_CREDIT;
         end;
      end;

      IsFirst = FALSE;
   end;  

   SetParm( 0, publicCharges );
   SetParm( 1, publicRate );
   SetParm( 2, publicBankOperationCode );
end;
```

---

## Пример 17: `FindMultiPaym`

**Источник:** `Mac/Cb/pmmulti.mac`
**Тип:** `macro`
**Размер:** 22 строк

```rsl
macro FindMultiPaym( PayFIID, CorSchem, ValueDate, Department )
  var op = OP_MULTI_FIRST, MultyID = 0, Count = 1, Num, error, CheckDprt = FALSE;

  GetRegistryValue( PathDprtMulti, V_BOOL, CheckDprt, error );

  while( Count AND (GetMultiPayments( op, PM_PROP_READY, TempPaym, PayFIID, CorSchem ) == TRUE) )
    op = OP_MULTI_NEXT;
    if( TempPaym.ValueDate == ValueDate )
      if( (CheckDprt == FALSE) OR (TempPaym.Department == Department) )    
        /* Если есть ограничение - подсчитываем текущее количество */
        if( MaxMultiPaym != 0 ) 
          Num = CalcMultiPayments( TempPaym.PaymentID );
        end;
        /* Если нет ограничения или вписываемся - то добавляем */
        if( (MaxMultiPaym == 0) OR ((MaxMultiPaym != 0) AND (Num < MaxMultiPaym)) )
          /* Здесь могут быть дополнительные проверки на сведение */
          MultyID = TempPaym.PaymentID;
          Count   = 0;
        end;
      end;
    end;
  end;
```

---

## Пример 18: `callUnrpGetRequest`

**Источник:** `Mac/Cb/ws_unrp_get_request.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro callUnrpGetRequest(request, urlAddress)
    var wsClient = initWsClient(urlAddress);
    var javaReq = request.toJava;
    var result = wsClient.wsUNRPGetRequest(request.toJava);
    return UniversalReportGetRequestResponseType.fromJava(result);
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 19: `callEfrsbMassCheck`

**Источник:** `Mac/Cb/ws_efrsb_masscheck.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro callEfrsbMassCheck(request, urlAddress)
    var wsClient = initWsClient(urlAddress);
    var result = wsClient.wsEFRSBMassCheck(request.toJava);
    return EfrsbMassCheckResponse.fromJava(result);
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 20: `callSbpSendReceivers`

**Источник:** `Mac/BOOK/ws_sbp_receivers.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro callSbpSendReceivers( request, urlAddress )
    var wsClient = initWsClient(urlAddress);
    var result = wsClient.wsSBPSendReceivers( request.toJava );
    return GetReceiverInfoRespType.fromJava( result );
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 21: `callService`

**Источник:** `Mac/Cb/ws_rkl_get_client_info.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro callService(request, urlAddress)
    var wsClient = initRklWsClient(urlAddress);
    var javaReq = request.toJava;
    var result = wsClient.rklGetClientInfo(javaReq);
    return RklGetClientInfoResponseType.fromJava(result);
OnError(e) 
    properlyThrow(e);
end;
```

---

## Пример 22: `callUNRPGiveResult`

**Источник:** `Mac/Cb/ws_unrp_give_result.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro callUNRPGiveResult(request, urlAddress)
    var wsClient = initWsClient(urlAddress);
    var javaReq = request.toJava;
    var result = wsClient.wsUNRPGiveResult(request.toJava);
    return UniversalReportGiveResultResponseType.fromJava(result);
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 23: `SetCalcDates`

**Источник:** `Mac/CONV_FC/v_laros_fc_1_2.mac`
**Тип:** `macro`
**Размер:** 42 строк

```rsl
macro SetCalcDates()
   var stat = True;

   WorkWithDate( DateConvert, PC_ALG.GrafCalc, PC_ALG.DayCalc, DateNextCalc );
   /*println( depositr.Account, " " , DateConvert, " " , DateNextCalc );*/

   if( DateNextCalc != NullDate )
      /* Определили дату следующего причисления */
      WorkWithDateBack( DateNextCalc,
                        PC_ALG.GrafCalc,
                        PC_ALG.DayCalc,
                        DatePrevCalc );
      if( DatePrevCalc == NullDate )
         Protocol.Error("Для счета ", depositr.Account,
                                  "не определена дата начала периода расчета" );
         stat = False;
      end;
      if( IsIntresting( Trim( depositr.Type_Account ) ) ) /* Пока для срочного с ежемесячной выплатой */
         /* Определили дату следующего причисления */

         WorkWithDateBack( DatePrevCalc,
                           PC_ALG.GrafCalc,
                           PC_ALG.DayCalc,
                           DatePrevCalc );
         if( DatePrevCalc == NullDate )
            Protocol.Error( "Для \"интересного\" вида вклада", sb_dtyp.Kind,
                            " и счета ", depositr.Account,
                            "не определена дата начала периода расчета" );
            stat = False;
         end;
      end;
   else
      Protocol.Error( "Для счета ", depositr.Account,
                      "не определена дата окончания периода расчета" );
      stat = False;

   end;
   /*println( DatePrevCalc, " ", DateNextCalc );*/


   return stat;
end;
```

---

## Пример 24: `Payment_RePayment`

**Источник:** `Mac/ACQUIRER/acq_Pay.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro Payment_RePayment(tran,isGroup)
var stat = true;
var trnOpenFiles = 1;
isOwn = true;
// ProfilerStart("Payment_RePayment");
  Error = 20005; //Транзакция не может быть оплачена
  notGroupPayment = not isGroup;

  if ( isGroup )
    trnOpenFiles = 0;
  end;
```

---

## Пример 25: `callOOServiceSendInfExecOrder`

**Источник:** `Mac/Cb/ws_oo_SendInfExecOrder.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro callOOServiceSendInfExecOrder(request, urlAddress)
    var wsClient = initOoWsClient(urlAddress);
    var result = wsClient.ooGetExecPayInfo(request.toJava);
    return OOSendInfExecOrderResponseType.fromJava(result);
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 26: `ОбработатьЦБ`

**Источник:** `Mac/DLNG/SECUR/Replication/txproc_avr_fun.mac`
**Тип:** `macro`
**Размер:** 20 строк

```rsl
MACRO ОбработатьЦБ( AvoirData:TAvoirData, Action:integer, Error:TArray ) : BOOL
   var   ret:bool = true;

   gAvoirData         = AvoirData;
   gAvoirData.Action  = Action;

   if( (Error != null) and (valtype(Error) == V_GENOBJ) )
      gAvoirData.Error   = Error;
   end;

   if( gAvoirData.InTrn == false )
      if (ProcessTrn(0, "ProcessAvoiriss", fininstr, avoiriss, avrinvst, objcode, objrgdoc, objkcode, objcode, objalreg, partyown ) == false )
         ret = false;
      end;
   else
      ProcessAvoiriss();
   end;

   return ret;
END;
```

---

## Пример 27: `StartConversion`

**Источник:** `Mac/DLNG/SECUR/Convert/dv_cnvmsfo9.mac`
**Тип:** `macro`
**Размер:** 48 строк

```rsl
MACRO StartConversion()
    var error = 0;
    
    msgbox("Начало конвертации");
    
    if( (СчетДляУчетаФР != БС_706) and (СчетДляУчетаФР != БС_10801_10901) )
        msgbox("Не реализована обработка значения "+СчетДляУчетаФР+" для параметра \"СчетДляУчетаФР\"");
        error = 1;
    end;
    
    if( not error )
        StartTransaction("1. Проставляем признак ПФИ");
        УстановитьПризнакПФИ();
        EndTransaction(error);
    end;
    
    if( not error )
        StartTransaction("2. Обработка сделок \"Своп\"");
        error = ВыполнитьПереносОстатковПоОперациямСвоп();
        EndTransaction(error);
    end;
    
    if(not error)
        msgbox("Конвертация успешно завершена");
    else
        msgbox("При конвертации возникли ошибки.\nПосле устранения причин ошибок повторную конвертацию следует выполнять, начиная с проблемного блока.\nВсе предыдущие успешно выполненные блоки следует закомментировать в макросе.");
    end;
    
OnError( errObj );
    if(RslDefCon.IsInTrans)
        RslDefCon.RollbackTrans();
    end;
    
    if(errObj and errObj.err and errObj.err.environment)
        var j;
        var err_text = "", delim = "";
        j = 0;
        while(j < errObj.err.environment.ErrorCount)
            err_text = err_text + delim  + errObj.err.environment.error(j).descr;
            delim = "\n";
            j = j + 1;
        end;
        
        MsgBox(err_text);
    end;
    
    return 1;
END;
```

---

## Пример 28: `ProcessPayment`

**Источник:** `Mac/Cb/pmmulti.mac`
**Тип:** `macro`
**Размер:** 39 строк

```rsl
macro ProcessPayment( Cs, PayFIID, ValueDate, Department )
  var ID, result = RES_MULTI_SKIP, RefID = 0, Number = "", UseMulti = FALSE, error;

  RES_MULTI_PAYM = result;

  GetRegistryValue( PathUseMulti, V_BOOL, UseMulti, error );

  if( (error == 0) AND (UseMulti == TRUE) )
    
    /* Считываем максимальное допустимое число платежей в сводном */
    GetRegistryValue( PathMaxMulti, V_INTEGER, MaxMultiPaym, error );

    /* Ищем сводные платежи по схеме расчетов и филиалу текущего платежа */
    ID = FindMultiPaym( PayFIID, Cs, ValueDate , Department);

    if( ID != 0 )               /* Вставляем платеж в имеющийся сводный */
      result = RES_MULTI_ADD;
      MultiPaym.PaymentID  = ID;
      MultiPaym.Department = Department;
    else
      result = RES_MULTI_NEW;    /* Начинаем новый сводный платеж */

      if( (GetReferenceIDByType(
               520, /*OBJTYPE_MULTIPAYMENT*/
               1,                    
               RefID ) == 0) AND (RefID != 0) )
        if( GenerateReference( RefID, Number ) != 0 )
          MsgBox( "Ошибка при генерации номера сводного платежа" );
          return 1;
        end;
      end;

      MultiRmprop.Number = Number;      

    end;

    /* Заполняем результат обработки платежа */
    RES_MULTI_PAYM = result;
  end;
```

---

## Пример 29: `ЗакрытьКредитнуюЛинию`

**Источник:** `Mac/DLNG/MMARK/mmlibr.mac`
**Тип:** `macro`
**Размер:** 54 строк

```rsl
MACRO ЗакрытьКредитнуюЛинию( tick )
    var  error = 0, flag, stat, account, rest, fd;

    GetRegistryValue("MMARK\\ОБЩИЕ\\ЗАКРЫВАТЬ_СЧЕТА_ПО_СДЕЛКЕ",
                    V_BOOL, flag, stat);

    if (stat)
        mm_error("Ошибка при работе с реестром");
        error = 1;
    else
        if (flag)
            fd = MMFirstDoc(tick.BOfficeKind, tick.DealID, true);

            if ((fd.GetTick().GenAgrID > 0) and
                (fd.GetGenAgr().AccMode == 2))
                return 0;
            end;        
			
            account = TRsbDataSet("select categ.t_code, accdoc.t_account, accdoc.t_currency, "
                                    "accdoc.t_chapter, accdoc.t_firole from "
                                    "dmcaccdoc_dbt accdoc, dmccateg_dbt categ where "
                                    "(accdoc.t_dockind = 208)and "
                                    "(accdoc.t_docid = " + tick.DealID + ")and "
                                    "(accdoc.t_catid = categ.t_id)and "
                                    "(categ.t_updatemode = 0)");

                while(account.MoveNext)
                    if (MC_FindAndOpenAccount(account.code, fd, date(31,12,9999), 0, MC_OPENACC_CHECKEXIST))
                        rest = Money(0);

                        rest = abs(RestA(account.account, {curdate}, NULL, account.chapter, account.currency)) +
                                abs(RestA(account.account, date(31,12,9999), NULL, account.chapter, account.currency));
    
                        if (rest > 0)
                            mm_error("Не нулевой остаток на счете " + account.account);
                            error = 1;
                            break;
                        elif (MC_FindAndCloseAccount (account.code, fd, {curdate}, account.firole, account.currency, MC_ACC_CLOSE_ALL))
                            mm_error("Невозможно закрыть счет " + account.account);
                            error = 1;
                            break;
                        else
                            error = 0;
                        end;
                    else
                        error = 0;
                    end;
                end;
            else
                error = 0;
            end;
        end;
    return error;
END;
```

---

## Пример 30: `ОбработатьТребование`

**Источник:** `Mac/DLNG/SECUR/Replication/txproc_paym_fun.mac`
**Тип:** `macro`
**Размер:** 20 строк

```rsl
MACRO ОбработатьТребование( DemandData:TDemandData, Action:integer, Error:TArray ) : BOOL
   var   ret:bool = true;

   gDemandData         = DemandData;
   gDemandData.Action  = Action;

   if( (Error != null) and (valtype(Error) == V_GENOBJ) )
      gDemandData.Error   = Error;
   end;

   if( gDemandData.InTrn == false )
      if (ProcessTrn(0, "ProcessDemand", rq, pmlink ) == false )
         ret = false;
      end;
   else
      ProcessDemand();
   end;

   return ret;
END;
```

---

## Пример 31: `OperBlock`

**Источник:** `Mac/Cb/ws_blockoper.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro OperBlock(OperBlockParm)
    var wsOperBlock : TWsOperBlock = TWsOperBlock;
    var wsAnswer : TWsOperBlockAnswer;

    WS_CheckParameter(1, OperBlockParm, true, V_GENOBJ);
    FillTWsOperBlock(OperBlockParm, @wsOperBlock);

    wsAnswer.stat = AL_WsOperBlock(wsOperBlock.Oper, wsOperBlock.Status, wsOperBlock.StartDate, wsOperBlock.EndDate);
    if (wsAnswer.stat)
        wsAnswer.error = GetErrMsg();
    end;

    return wsAnswer;
end;
```

---

## Пример 32: `GetCardControlFileDate`

**Источник:** `Mac/Cb/countryccimp.mac`
**Тип:** `macro`
**Размер:** 19 строк

```rsl
macro GetCardControlFileDate(ImportFilePath)
    var PalaceDate = ZeroValue(V_DATE);
    if (ExistFile(ImportFilePath))
        InitExcel();

        var err = "";
        if (OpenExcel(false, ImportFilePath, @err))
            var ActiveSheet = ExcelApplication.ActiveSheet;
            if (CheckHeader(ActiveSheet, headerStart) or CheckHeader(ActiveSheet, headerStart2))
                PalaceDate = GetPlaceDate(ActiveSheet);
            end;
            ExcelApplication.Quit();
        end;
    end;

    return PalaceDate;
OnError
    return ZeroValue(V_DATE);
end;
```

---

## Пример 33: `check`

**Источник:** `Mac/DEPOSITR/GS/GSDeleteSenders.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
  macro check(): bool
    deleteSender();
    
    return true;

  OnError(err)
    return handleError(err);
  end;
```

---

## Пример 34: `RunImport`

**Источник:** `Mac/Cb/es_import_xml.mac`
**Тип:** `macro`
**Размер:** 28 строк

```rsl
macro RunImport(RunESCheckParty, FullFileName)
    const UnknownFormat = "Ошибка: файл " + FullFileName + " имеет не поддерживаемую структуру";
    RunESCheckParty = false;

    ClearTables();
    
    var parsererr = "";
    if (not ValidateXmlFileByXsdNamespace(FullFileName, "es.xsd", "http://eu.europa.ec/fpi/fsd/export", @parsererr))
        return String(UnknownFormat + ". " + parsererr);
    end;

    var rootHandler = TRootElementHandler(null);
    rootHandler.FullFileName = FullFileName;
    var sp = SaxParser(rootHandler);
    sp.parse(FullFileName);

    ProcessTrn(0, R2M(rootHandler, "MergeData"));
    EndAction();
    return true;
OnError(error)
    EndAction();

    if (rootHandler.error == EXIT_NO_ERROR)
        return true;
    end;

    return UnknownFormat;
end;
```

---

## Пример 35: `Fill22FH`

**Источник:** `Mac/Mbr/swndd544.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro Fill22FH( Qualifier, Scheme, Indicator )
   var error;
   msginf.NeedBlock = false;
   if ( CurrentBlock==SETDET_Block )
       if ( Qualifier=="SETR" )          
          msginf.SettlementTransactionType = GetllValueElement(OBJTYPE_MSGTRANS, Indicator, error);
          if ( error )
             return false;
          end;          
       end;
   elif( Qualifier=="TTCO" )
     if( Indicator == "GTDL")
       msginf.NeedBlock = true;
     end;
   end;
   return true;
end;
```

---

## Пример 36: `GetFileName`

**Источник:** `Mac/Mbr/swsbfref.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro GetFileName( SeqValue, ObjKind, ObjAddr )
  var refer, PayerMesID, CodePayerMesBank, error;
  
  if (ObjKind==OBJTYPE_SESS)
    SetBuff(wlsess,  ObjAddr);
    if (wlpmpaym.PayerMesBankID)
      PayerMesID = wlsess.InsideAbonentID;
    else 
      PayerMesID = {OurBank};
    end;       

    CodePayerMesBank = ПолучитьКодСубъекта(PayerMesID, PTCK_SBRF, Error);
    if (Error != 0)
      CodePayerMesBank = CodePayerMesBankDefault;
    end;

    refer = string("sw", SeqValue:6, ".", CodePayerMesBank:3:r);
    refer = strsubst(refer, " ", "0");
  else
    refer = "";
  end;
```

---

## Пример 37: `callKYCGetRiskService`

**Источник:** `Mac/Cb/ws_kyc_get_risk_client_request.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro callKYCGetRiskService(request, urlAddress)
    var wsClient = initWsClient(urlAddress);
    var javaReq = request.toJava;
    var result = wsClient.wsKYCGetRiskClient(request.toJava);
    return KYCGetRiskClientResponseType.fromJava(result);
OnError(e)
    properlyThrow(e);
end;
```

---

## Пример 38: `GetWaitingSynWS`

**Источник:** `Mac/Cb/QueueWSLib.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro GetWaitingSynWS()


  var error = 0;
  if(GWaitingSyn == -2)
    GetRegistryValue( "COMMON\\QUEUE\\WAITING SYNC", V_INTEGER, GWaitingSyn, error );
  end;
```

---

## Пример 39: `GetMessageFunction`

**Источник:** `Mac/Mbr/swdpgmes.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro GetMessageFunction(msginf:object)   
   var error, res;
   res = GetllValueElement(OBJTYPE_MSGFUN, msginf.messageFunction, error);
   if ( error )
      RunError( "|Неверное значение функции сообщения" );
   end;
   return res;
end;
```

---

## Пример 40: `OON_ImportList`

**Источник:** `Mac/Cb/oonimportlist.mac`
**Тип:** `macro`
**Размер:** 53 строк

```rsl
macro OON_ImportList(FullFileName, Mode, ImpListMode)
    var Result : ImportResult;
    var erstr;
    Result.stat = true;

    var file_path = FullFileName;
    if(not IsStandAlone) //Трехзвенка
        var strFile, strExt;
        SplitFile(FullFileName, strFile, strExt);
        file_path = CallRemoteRsl("dlreptl.mac", "DLREPTL_GetTxtFileDir") + strFile + UserNumber + strExt; // dlwrept.mac

        if (not CopyFile(FullFileName, "$" + file_path))
            msgbox ("Ошибка при передаче файла на терминал");
            return false;
        else
            var FullTxtFilePath = DLREPTL_GetTxtFileDir() + strFile + "_" + UserNumber + strExt;
            if (not CopyFile("$" + file_path, FullTxtFilePath))
                msgbox ("Ошибка при передаче файла на терминал");
                return false;
            else
                file_path = FullTxtFilePath;
            end;
        end;
    end;

    if ((Mode == FM_OON_IMP_XML) or (Mode == FM_OON_IMP_XML_RU))
        Result = OON_ImportListStart(file_path, ImpListMode, Mode);
    end;

    if (result.Stat AND (ImpListMode != 1))
        var q = MsgBoxEx ("Выполнить Процедуру проверки субъектов экономики по Перечню санкций СБ ООН? ", MB_YES + MB_NO);
        if (q == IND_YES)
            FM_PtLstStartOONProc();
        end;
    else
        if ((ValType(result.Error) == V_STRING) and (result.Error != ""))
            erstr = result.Error;
            MsgBox (erstr);
        end;
    end;

    return Result.Stat;
OnError(error)
    var detail = error.err;

    if (ValType(error.err) == V_UNDEF)
        detail = error.Message;
    end;
    erstr = "Ошибка: файл \"" + FullFileName + "\" не загружен. " + detail;
    EndAction ();
    MsgBox (erstr);
    return false;
end;
```

---
