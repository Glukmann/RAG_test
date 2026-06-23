# Практика: Циклы (WHILE, FOR, BREAK, CONTINUE)

**Теория:** [BnRSL.md## Инструкция цикла WHILE]

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

## Пример 2: `FillInformationTable`

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

## Пример 3: `ExecuteStep`

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

## Пример 4: `_ClientIdentMass`

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

## Пример 5: `SortSummaryByCurrency`

**Источник:** `Mac/DEPOSITR/getattach_fm_ex.mac`  
**Тип:** `private macro`  
**Размер:** 43 строк

```rsl
private MACRO SortSummaryByCurrency

  var i = 0;
  var j = 0;
  var tmpVal;

  while ( i < ASize( AComplexCode ) )
    j = i;
    while (j < ASize( AComplexCode ) )
      if ( AComplexCode( j ) < AComplexCode( i ) )
        // ---------------------------------------------------------------
        tmpVal = AComplexCode( i );
        AComplexCode( i ) = AComplexCode( j );
        AComplexCode( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = ACodeISO( i );
        ACodeISO( i ) = ACodeISO( j );
        ACodeISO( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = ACode113( i );
        ACode113( i ) = ACode113( j );
        ACode113( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = ARate( i );
        ARate( i ) = ARate( j );
        ARate( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = AIncomeSum( i );
        AIncomeSum( i ) = AIncomeSum( j );
        AIncomeSum( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = AOutSum( i );
        AOutSum( i ) = AOutSum( j );
        AOutSum( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = AIncomeСheque( i );
        AIncomeСheque( i ) = AIncomeСheque( j );
        AIncomeСheque( j ) = tmpVal;
        // ---------------------------------------------------------------
        tmpVal = AOutСheque( i );
        AOutСheque( i ) = AOutСheque( j );
        AOutСheque( j ) = tmpVal;
      end;
```

---

## Пример 6: `GetPtsvdpList1`

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

## Пример 7: `GetDprtList`

**Источник:** `Mac/Cb/ws_rscore2ikfl.mac`  
**Тип:** `macro`  
**Размер:** 46 строк

```rsl
macro GetDprtList(Request)
  var wsRequest = TWsGetDprtListRequest;

  var i, j, k;
  var query = "";
  /*var wrapquery = "";*/
  var rs;
  var params = TArray;
  var newElem;
  var Response;
  var ConvertedNameMask;

  WS_SetAttributeValue(@wsRequest.Statuses         , 0, "Request", "Statuses"         , Request, V_GENOBJ , false, null, true);
  WS_SetAttributeValue(@wsRequest.DprtCode         , 0, "Request", "DprtCode"         , Request, V_INTEGER, false, null, true);
  WS_SetAttributeValue(@wsRequest.DprtPartyNameMask, 0, "Request", "DprtPartyNameMask", Request, V_STRING , false, null, true);

  query = query + "SELECT ";
  query = query + "  dp.t_Code          ";
  query = query + " ,dp.t_Name          ";
  query = query + " ,dp.t_Status        ";
  query = query + " ,dp.t_PartyID       ";
  query = query + " ,dp.t_NodeType      ";
  query = query + " ,dp.t_BranchType    ";
  query = query + " ,dp.t_OpenNodeDate  ";
  query = query + " ,dp.t_CloseNodeDate ";
  query = query + " ,dp.t_ParentCode    ";
  query = query + " ,pt.t_ShortName     ";
  query = query + " ,pt.t_Name          ";
  query = query + " ,pt.t_OKPO          ";
  query = query + "  FROM ";
  query = query + "    ddp_dep_dbt dp ";
  query = query + "   ,dparty_dbt pt ";

  query = query + " WHERE dp.t_PartyID = pt.t_PartyID(+) ";
  
  if(wsRequest.Statuses != null)
    if(GenPropID(wsRequest.Statuses, "size") != -1)
      i = 0;
      k = 0;
      while(i < wsRequest.Statuses.size)

        if(wsRequest.Statuses[i] != null)

          if(k == 0)
            query = query + " AND dp.t_Status IN ( 0 ";
          end;
```

---

## Пример 8: `GetRatesDFS`

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

## Пример 9: `GenPmSwiftMxPacs002`

**Источник:** `Mac/Mbr/swmxPacs2_GenProc.mac`  
**Тип:** `private macro`  
**Размер:** 34 строк

```rsl
private macro GenPmSwiftMxPacs002
( rs : RsdRecordset, 
  DepList : string, // заполняется при вызове из планировщика
  FromSheduler : bool, // заполняется при вызове из планировщика
  PaymentID : integer, // заполняется при вызове из макроса шага операции
  ID_Operation : integer, // заполняется при вызове на шаге операции
  ID_Step : integer // заполняется при вызове на шаге операции
) :TArray

  var PrcRecs : TArray = TArray();

  while(rs.moveNext())
    var RhWlextst : TRecHandler = TRecHandler("wlextst.dbt");
    CopyRSetToFBuff(RhWlextst, rs);

    var ErrMsg : string = "";
    var PaymentObj : RsbPayment = RsbPayment(RhWlextst.rec.PaymentID);

    // Генерим pacs.002 и устанавливаем 
    // wlextst.ObjectID = wlinfo.InfoID, wlextst.ObjectType = OBJTYPE_WLD_INFO
    // (через класс платежа).
    GenNotifyAndUpdatePayment(RhWlextst, @ErrMsg, ID_Operation, ID_Step);

    if( FromSheduler and not ID_Operation and not ID_Step and not ErrMsg and
        (RhWlextst.rec.State == WLPM_EXECNOTIFY_RJCT)
      )
      // Если платеж находится на шаге операции "Обработка отвергнутого" (символ шага "J"), 
      // запустить шаг на выполнение с параметром $(завершить)
      var StepSymbol : string = "J"; //PM_OPR_SYMB_PROCESSREJECT
      if( Opr_IsStepExecuteSymb(PaymentObj.PaymentID, PaymentObj.DocKind, StepSymbol, "R") )           
        PM_SetRejectProcessKind(PM_REJECT_PROCKIND_FINISH);
        PM_ExecuteOperation(PaymentObj.PaymentID, PaymentObj.DocKind);// здесь ошибку не анализируем, т.к. ее не требуется по проекту выводить в отчет
        PM_SetRejectProcessKind(PM_REJECT_PROCKIND_NONE);
      end;
```

---

## Пример 10: `ВыполнитьПроводкиЗачисленияКДУ`

**Источник:** `Mac/DLNG/SECUR/uniavr50.mac`  
**Тип:** `macro`  
**Размер:** 56 строк

```rsl
macro ВыполнитьПроводкиЗачисленияКДУ(comm, Doc, idOperation)
  var stat = 0;

  var m_qracc = TBFile("scqracc.dbt","w");
  
  var QrAcc = TRecHandler("account.dbt");
  var CorrAcc = TRecHandler("account.dbt");
  var FD;

  var qrAccId = 0;

  var query = 
    " SELECT * "
   +"   FROM dscdlfi_dbt "
   +"  WHERE t_DealKind = ? AND t_DealID = ? ";

  var cmd = DL_RSDCommand(query), cmd2;
  cmd.addParam(comm.DocKind);
  cmd.addParam(comm.DocumentID);

  var DataSet = cmd.execute(), DataSet2;

  while (DataSet.MoveNext())
    query = 
      " SELECT acctrn.t_sum_receiver, scqr.t_QRID "
     +"   FROM doprdocs_dbt t, "
     +"        dacctrn_dbt acctrn, "
     +"        dacctrn_state_dbt acctrn_state, "
     +"        DOPRSTEP_DBT step, "
     +"        DSCQRACC_DBT scqr "
     +"  WHERE     t.t_id_operation = ? "
     +"        AND STEP.T_ID_OPERATION = t.t_id_operation "
     +"        AND t.t_id_step = STEP.T_ID_STEP "
     +"        AND STEP.T_SYMBOL = 'О' "
     +"        AND scqr.t_fiid = ? "
     +"        AND SCQR.T_ACCOUNTID = ACCTRN.T_ACCOUNTID_RECEIVER "
     +"        AND (    t.t_DocKind = 1 "
     +"             AND t.t_AccTrnID = acctrn.t_AccTrnID "
     +"             AND (   (acctrn.t_State = 1 OR acctrn.t_State = 2) "
     +"                  OR acctrn.t_State = 3) "
     +"             AND acctrn.t_State = acctrn_state.t_State(+)) ";

    cmd2 =  DL_RSDCommand(query);
    cmd2.addParam(idOperation);
    cmd2.addParam(comm.Fiid);
    DataSet2 = cmd2.execute();

    while (DataSet2.MoveNext())
      
      //Находим регистр КДУ по проводке списания
      m_qracc.Clear();
      m_qracc.KeyNum = 0;
      m_qracc.rec.QRID = DataSet2.QRID;
      if (not m_qracc.GetEQ())
        return 1;
      end;
```

---

## Пример 11: `EAM_MakeHeaderTextAttach`

**Источник:** `Mac/Cb/eam_ntfdereg.mac`  
**Тип:** `macro`  
**Размер:** 19 строк

```rsl
macro EAM_MakeHeaderTextAttach(NumMess, Events, Header, Text, FileName, AttachStr)
   var result = true;

   if ((GenClassName(Events) == "TArray") and (Events.size > 0))
      var xml = CreateXMLParser();
      var mes = "";
      var head = "Результат обработки сервиса RS-Connect \"Уведомление о снятии с учета физического лица\"";
      if(xml.loadXML(Events[0].Rec.Parm))
         var logDir = REGVAL_LOG_DIR;
         var logName = xml.getElementsByTagName("LogName").item(0).text;
         var logExt = "txt";
         var logFileName = MergeFile(null, logName, logExt);
         var logFullPath = MergeFile(logDir, logName, logExt);
         if (ExistFile(logFullPath))
            var doc = TStreamDoc(logFullPath, "R");
            var content:String = "";
            while(doc.ReadLine())
               content = content + doc.str + "\r\n";
            end;
```

---

## Пример 12: `ProcFormTOFK`

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

## Пример 13: `ListType_4_body`

**Источник:** `Mac/DEPOSITR/comp_r04.mac`  
**Тип:** `macro`  
**Размер:** 36 строк

```rsl
macro ListType_4_body(arrFNcash, kind, type, date1, date2 )
   array arrAutoKey;
   var count = isCompensPayOut(arrFNcash, kind, type, date1, date2, arrAutoKey);
   var FIO="", SumComp="", FIO_pol="";
   var temp_date="",bDay="", bMon="", bYear="";
   var cmd_1, rs_1, cmd_2, rs_2,i=0;
   var payDate=" ", paySum=" ", payDestAccount=" ", payFIO=" ";
   var doplDate=" ", doplSum=" ", doplDestAccount=" ", doplFIO=" ";
   var Flag = false;
    
   var CloseDate="", AccAccount="", Rest="", Type_Account="";

   var count_pay=0;
     count_of_account = count;
     while (i < count) 
      cmd = RsdCommand("select cmp.t_codclient, cmp.t_account, cmp.t_accClsDate, cmp.t_restIn91, cmp.t_FullSum, cmp.t_sum, cmp.t_date,"+
                       " cmp.t_destAccount, cmp.T_DESTCLIENTCODE, dep.t_SpecialAccess as SpecialAccess "+
                       "from dcompens_dbt cmp, ddepositr_dbt dep where cmp.t_fncash = ? and cmp.t_autokey = ? "+
                       " and cmp.T_DESTACCOUNT = dep.T_ACCOUNT and cmp.t_fncash = dep.t_fncash");
      cmd.addParam("t_fncash", RsdBp_in);
      cmd.value("t_fncash") = arrFNcash;
      cmd.addParam("t_autokey", RsdBp_in);
      cmd.value("t_autokey") = arrAutoKey(i);
      cmd.execute();
      rs = RsdRecordset(cmd);
      rs.moveNext();
      if(  (not SpecialAccess) and OperMayListSpecialAccounts and RS.value("SpecialAccess"))
         FIO = "XXXXXX X.X.";
         bYear = "XXXX";
      else

        if ( rs.value(0) != 0) 
           if ( ClientList.GetRecord( rs.value(0) ) )
             FIO = ClientList.CurRec.rec.name1 + " " + SubStr( ClientList.CurRec.rec.name2, 1, 1 ) + ". " + SubStr( ClientList.CurRec.rec.name3, 1, 1 ) + ".";
           DateSplit(ClientList.CurRec.rec.Born, bDay, bMon, bYear );
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

## Пример 15: `fill_BankInfo`

**Источник:** `Mac/DEPOSITR/getattach_fm_ex.mac`  
**Тип:** `macro`  
**Размер:** 19 строк

```rsl
macro fill_BankInfo( Fncash : integer, isNationalCur : bool, item:TIncrementDetailsItem )
  var ourBank_BIC_SWIFT = "";
  var ourBank_Name = "";
  var ourBank_CorrAcc = "";
  var ourBank_INN = "";
  var ourBank_KPP = "";
  var ourBankID = 0;
  var stat = 0;
  var filcode = GetFilial( Fncash );
  var needNextFind = true;
  var ddep =  TRecHandler( "i_dp_dep.rec" ), party = TRecHandler( "i_party.rec" );

  while (needNextFind)
    stat = findDepartment(filcode, NULL, ddep, party);
    if (stat)
      if ( (ourBankID <= 0) and (ourBank_Name == "") )
        ourBank_Name = party.rec.Name;
        ourBankID  = party.rec.partyID;
      end;
```

---

