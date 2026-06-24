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

## Пример 16: `PrintLog`

**Источник:** `Mac/DLNG/DV/dvfcsapr.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro PrintLog()
  var count = 0;
   if( ErrorsReportLog )
      Rep.AddNewSheetBreak("Протокол", TableErrors);
      ReportData.ReportIsEmpty = false;
      while( count < ErrorStr )

         Rep.AddPrintCell( Errors[count] , 0, 0, "l");
         Rep.AddStr();

         count = count + 1;
      end;
   end;
end;
```

---

## Пример 17: `CBINF_Proc`

**Источник:** `Mac/Cb/cbinfpln.mac`
**Тип:** `macro`
**Размер:** 102 строк

```rsl
macro CBINF_Proc( RegPath, OutType )

    file indexv( indexv ) key 0;
    file indexc( indexc ) key 0;

    var this_stat, nmbRec = 0;

    CBINF_Result = 0;
    CBINF_ErrorStatus = 0;

    if( OutType == CBINF_OutReport )
        if( PrintHeader( RegPath, LIST_PLANNED ) )
            return CBINF_StatusError;
        end;
    end;


    rewind ( indexv );
    
	InitProgress( NRecords(indexv) * 2, "Информирование о необработанных документах", "Планируемые" );
	
    while( next( indexv ) )

	    nmbRec = nmbRec + 1;
	    UseProgress( nmbRec );

        if( ( indexv.date_carry <= {curdate} ) and ( CBINF_OperDocFit( indexv.Oper ) == 0 ) )
        
            if( OutType == CBINF_OutMsg )
            
                this_stat = MsgDocFound( RegPath, CBINF_Planned, indexv );
                if( this_stat )
 	                RemProgress( nmbRec );
                   return this_stat;
                end;
                
            elif( OutType == CBINF_OutReport )
                this_stat = PrintLine( RegPath, CBINF_Planned, indexv );
                if( this_stat )
 	                RemProgress( nmbRec );
                   return this_stat;
                end;
                
            end;/*OutType*/
            
        end;/*if CBINF_OperDocFit*/
        
    end;/*while*/


    while( next( indexc ) )

	    nmbRec = nmbRec + 1;
	    UseProgress( nmbRec );

        if( ( indexc.date_carry <= {curdate} ) and ( CBINF_OperDocFit( indexc.Oper ) == 0 ) )
        
            if( OutType == CBINF_OutMsg )
            
                this_stat = MsgDocFound( RegPath, CBINF_Planned, indexc );
                if( this_stat )
 	                RemProgress( nmbRec );
                   return this_stat;
                end;
                
            elif( OutType == CBINF_OutReport )
                this_stat = PrintLine( RegPath, CBINF_Planned, indexc );
                if( this_stat )
	                RemProgress( nmbRec );
                    return this_stat;
                end;
                
            end;/*OutType*/
            
        end;/*if CBINF_OperDocFit*/
        
    end;/*while*/

    RemProgress( nmbRec );

    if( OutType == CBINF_OutReport )
        if( PrintFooter( RegPath, LIST_PLANNED ) )
            return CBINF_StatusError;
        end;
    end;

    return CBINF_StatusOk;

    
end;/*CBINF_Proc*/

/*test call
const REGPATH = "COMMON\\CBINFPARMS";
var ret;

ret = CBINF_Proc( REGPATH, CBINF_OutReport);

msgbox( "test : stat =  ", ret , " CBINF_Result = ", CBINF_Result );
*/
```

---

## Пример 18: `makeBookpass`

**Источник:** `Mac/DLNG/VA/vax110.mac`
**Тип:** `macro`
**Размер:** 26 строк

```rsl
  MACRO makeBookpass(fd)
    var 
       i = 0, stat = 0, Purpose, СчетДебет, СчетКредит;

    Purpose = String("Постановка сделки на балансовый учет");

    while((stat == 0) AND (i < ArrGrp.size))

      if(not VA_GetAccount("+Форвард, расчеты", fd, СчетДебет, MC_OPENACC_CREATE, ArrGrp[i].FIID, FIROLE_FIREQ, null, StepDate))
         stat = 1;
      elif(not VA_GetAccount("-Форвард, расчеты", fd, СчетКредит, MC_OPENACC_CREATE, ArrGrp[i].FIID, FIROLE_FICOM, null, StepDate))
         stat = 1;
      else
         stat = VA_Bookpass(СчетДебет, 
                        СчетКредит, 
                        ArrGrp[i].amount,
                        Purpose,
                        0, 0,               /* Платеж */
                        ArrGrp[i].FIID,
                        null, null, StepDate
                       );
      end;
      i = i + 1;
    end;
    return stat;
  END;
```

---

## Пример 19: `DefineIndent`

**Источник:** `Mac/Cb/sgn_opr.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro DefineIndent( LevelIndent )
  var i, FullIndent;
  FullIndent = "";
  i = 0;
  while( i < LevelIndent )
    FullIndent = FullIndent + Indent;
    i = i + 1;
  end;
```

---

## Пример 20: `GetLine`

**Источник:** `Mac/Cb/lib_rep.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
  macro GetLine( nLine )
    var i, Indent;
    if( nLine < SplitContent.Size() )
      Indent = ""; i = 0;
      while( i < LeftIndentSize )
        Indent = Indent + " ";
        i = i + 1;
      end;
      return Indent + SplitContent(nLine);
    end;
    return "";
  end;
```

---

## Пример 21: `ОбработатьСообщения`

**Источник:** `Mac/Mbr/swin503.mac`
**Тип:** `macro`
**Размер:** 51 строк

```rsl
macro ОбработатьСообщения( node )
  /* Инициализация*/
  var i = 0;
  var child:object;

  var Документов = 0;
  while( i < node.childNodes.length )
    child = node.childNodes.item(i);
    if( child and (child.nodeType==CHILD_NODE) and (GetNodeName(child.NodeName) == "SWIFTContainer") )
      if (not DecodeBase64(StrSubst(StrSubst(ReadNodeText(child, "SWIFTDocument"), "\n", ""), "\r", ""), CurrentMessage))
        ErrImport( "Ошибка при декодировании SWIFTDocument" );
        return IMPORT_MACRO_ERROR;
      end;
      CurrentMPosition = 1;
      CurrentMLine = 1;
      var КодНачалаБлокаПрочитан, СчитанныйКодНачалаБлока, Отправитель, Получатель, ДатаОтправки;

      /* Считываем заголовок файла */
      if( not СчитатьЗаголовок( Отправитель, Получатель, ДатаОтправки ) )
        return IMPORT_MACRO_ERROR;
      end;
      var continue0 = TRUE;
      var stat = 0;
      while( continue0 )
        stat = ОбработатьСообщение( КодНачалаБлокаПрочитан, СчитанныйКодНачалаБлока, Отправитель, Получатель, ДатаОтправки );
        if( stat == 1 )
          continue0 = FALSE;
        elif( stat == 3 ) /* найден конец файла */
          continue0 = FALSE;
        elif( stat == -1 )
          return IMPORT_MACRO_ERROR;
        elif( stat == 0 )
          stat = СчитатьРазделительСообщений(КодНачалаБлокаПрочитан, СчитанныйКодНачалаБлока);
          if( stat == 1 )
            continue0 = FALSE;
          elif( stat == -1 )
            return IMPORT_MACRO_ERROR;
          end;
        end;

        Документов = Документов + 1;
        message("Идет прием сообщений. Обработано: ", Документов );
      end;

      /* Считываем код конца файла */
      if( not СчитатьКонцовку() )
         return IMPORT_MACRO_ERROR;
      end;
    end;
    i=i+1;
  end;
```

---

## Пример 22: `PrintDocument`

**Источник:** `Mac/Cb/mld2161u.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
MACRO PrintDocument(ncopy: integer):bool
  debugbreak;
  CopyCont = ncopy;
  while(CopyCont)
    СформироватьОтчетДляМультивалютногоМО( pr_multydoc, 0 );
    CopyCont = CopyCont - 1;
  end;
```

---

## Пример 23: `ExecuteStep`

**Источник:** `Mac/DLNG/TRUST/tscalc030.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
macro ExecuteStep( doc, FDoc, DocKind, _OperationID, ID_Step )

  Oper.SetRecordAddr( FDoc );
  FD = TS_CalcORCB_FD( Oper );

  while( FD.MoveNextOrder() )
     if( ПеревестиСредства( FD.OrderFD.ID, doc ) == false )
        return 1;
     end;
  end;
```

---

## Пример 24: `GetPaymSum`

**Источник:** `Mac/DLNG/dldlngfun.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
  MACRO GetPaymSum(id) /* возвращает платеж */
     var i = 0;
     while(i < Payms.size)
        if(id == Payms(i).PaymID)
           return Payms(i).PaymSum;
        end;
        i = i + 1;
     end;

     return -1;
  END;
```

---

## Пример 25: `VA_Rep_InitProgress`

**Источник:** `Mac/DLNG/VA/vamisc.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
MACRO VA_Rep_InitProgress(n, head, stat)
    VA_ByDefault(stat, "~Ctrl-Break~ Прервать");
    VA_ByDefault(head, "Формирование отчета");

    InitProgress(n, stat, head);
END;
```

---

## Пример 26: `merge`

**Источник:** `Mac/DEPOSITR/vector.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
  macro merge( a )
    var i = 0;
    var vsize = prvtASize(a);
    while( i < vsize )
      push_back( a(i) );
      i = i + 1;
    end;
  end;
```

---

## Пример 27: `RestInList`

**Источник:** `Mac/DEPOSITR/secrest1.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
macro RestInList (TestRest)
  var i = 1,
      stat = false;
  while ((NOT stat)
     AND (i < 21))
    if (TestRest == Rest(i))
      stat = true;
    end;
    i = i + 1;
  end;
```

---

## Пример 28: `makeBookpass`

**Источник:** `Mac/DLNG/VA/var060.mac`
**Тип:** `macro`
**Размер:** 38 строк

```rsl
  MACRO makeBookpass(tick, Purpose)
    var
       i = 0, stat = 0, SumDbt = 0, fd, ВалДеб, ВалКред,
       СчетДоход, СчетРасход;

    while((stat == 0) AND (i < ArrGrp.size))
      if(IsEnrol)
        ВалДеб = ВалРасчетов;
        ВалКред = ArrGrp[i].fiid;
      else
        ВалДеб = NATCUR;
        ВалКред = ArrGrp[i].fiid;
      end;

      if(ВалДеб == ВалКред)
         /* одновалютная проводка */
         stat = VA_Bookpass(ArrGrp[i].AccDbt, ArrGrp[i].acc, ArrGrp[i].amount, Purpose,
                        0, 0,               /* Платеж */
                        ВалДеб,
                        null, null, StepDate
                       );
      else
         /* многовалютная проводка */
         SumDbt = ArrGrp[i].payamount;//VA_Convert(ArrGrp[i].amount, StepDate, ArrGrp[i].fiid, ВалДеб);
         if(not VA_MBookpass(0,
                          ВалДеб, ArrGrp[i].AccDbt, SumDbt,
                          ВалКред, ArrGrp[i].acc, ArrGrp[i].amount,
                          Purpose,
                          null, null,
                          null, StepDate))
            stat = VA_Err("Ошибка при выполнении проводки",
                          "|", Purpose);
         end;
      end;
      i = i + 1;
    end;
    return stat;
  END;
```

---

## Пример 29: `ArrFind`

**Источник:** `Mac/Cb/lib_arr.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
MACRO ArrFind( arr, val, IsEqual:variant)
    var i = 0;
    while( i < arr.size )
        if(ValType(IsEqual) != V_UNDEF)
          if(ExecMacro2(IsEqual, arr[i], val))
            return i;
          end;
        else
          if( arr[i] == val )
            return i;
          end;
        end;
        i = i + 1;
    end;
    return -1;
END;
```

---

## Пример 30: `Блок`

**Источник:** `Mac/DLNG/VEKSEL/vsordfd.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
    MACRO GetBasisFIRole(FIRole)
      var i = 0;
      if (FIRole == FIROLE_UNDEF)
        return FIROLE_FIDOC;
      end;
      while (i < FIRoleBArray.Size)
        if (FIRoleBArray[i] == FIRole)
          return FIRole;
        end;
        i = i + 1;
      end;
      Error = 1;
      return FIROLE_UNDEF;
    END;
```

---

## Пример 31: `SortingOnDecrease`

**Источник:** `Mac/Invh/Fun_lvm.mac`
**Тип:** `macro`
**Размер:** 19 строк

```rsl
MACRO SortingOnDecrease(Arr)
var  flag = 1, tmp, i,j;
var  arrSize = Asize(Arr);

  i = 1;
  while(flag and (i < arrSize) )
    flag = 0;
    j    = arrSize - 1;
    while(j >= i)
      if( Arr(j-1) < Arr(j) )
         tmp      = Arr(j-1);
         Arr(j-1) = Arr(j);
         Arr(j)   = tmp;
         flag = 1;
      end;
      j = j - 1;
    end;
    i = i + 1;
  end;
```

---

## Пример 32: `GetFieldNum`

**Источник:** `Mac/DLNG/DEPO/spinfrep.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
  macro GetFieldNum(field)
    var i = 0;
    
    while((i < PanFieldNums.size()) AND (ValType(PanFieldNums[i]) != V_UNDEF))
      if(PanFieldNums[i] == field)
        return i;
      end;
      i = i + 1;
    end;

    return -1;
  end;
```

---

## Пример 33: `NeedImportRate`

**Источник:** `Mac/imp_rate.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
MACRO NeedImportRate( code )

 var i = 0;
 const n = СписокВалют.size;

 while( i < n )
  if( СписокВалют(i) == code )
   return TRUE;
  end;
```

---

## Пример 34: `makeBookpass`

**Источник:** `Mac/DLNG/VA/vaw120.mac`
**Тип:** `macro`
**Размер:** 40 строк

```rsl
  MACRO makeBookpass()
    var СчетДоход, СчетРасход, sum_dbt, i = 0, stat = 0, at = VA_AccTrans();

    while((stat == 0) AND (i < ArrGrpDisc.size))
      stat = VA_Bookpass(ArrGrpDisc[i].dbt,
                     ArrGrpDisc[i].crd,
                     ArrGrpDisc[i].amount,
                     String("Начисление дисконта по векселю"),
                     0, 0,               /* Платеж */
                     ArrGrpDisc[i].AccFI,
                     null, null, StepDate,
                     null, null, null, null,
                     "18");
      i = i + 1;
    end;
    i = 0;

    at.date_carry   = StepDate;
    at.CatPayer     = "ВнебалСчетКорресп";
    at.CatReceiver  = "Разн.ценности и документы";
    at.FIIDPayer    = NATCUR;
    at.FiRolePayer  = FIROLE_CORACC_ACTIVE;
    at.Ground       = String("Выдача векселя контрагенту");
    at.Chapter      = 3;
    while((stat == 0) AND (i < ArrGrp.size))
        at.FDPayer      = ArrGrp[i].fd;
        at.FDReceiver   = ArrGrp[i].fd;
        at.PrimaryDoc   = ArrGrp[i].fd;
        at.FIIDReceiver = NATCUR;
        at.SumReceiver  = ArrGrp[i].amount;

        if (not at.carry())
            stat = VA_Err("Ошибка при выполнении",
                          "|проводки по выдаче векселя",
                          "|контрагенту");
        end;
      i = i + 1;
    end;
    return stat;
  END;
```

---

## Пример 35: `FormatRate`

**Источник:** `Mac/Mbr/swgm399.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro FormatRate(Rate)
  var retRate = Rate.asDouble, i;

  i = 0;
  while(i < Rate.Point)
    retRate = retRate/10;
    i = i+1;
  end;
```

---

## Пример 36: `GetErrorString`

**Источник:** `Mac/DLNG/dlquery.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
  macro GetErrorString(e)
    var strErr = e.message;
    var i = 0;

    while( i < m_Select.connection.environment.ErrorCount )
      strErr = strErr + m_Select.connection.environment.Error(i).Descr;
      i = i + 1;
    end;

    return strErr;
  end;
```

---

## Пример 37: `PrintLog`

**Источник:** `Mac/DLNG/DV/dvoposrp.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro PrintLog()
  var count = 0;
   if( ErrorsReportLog )
      Rep.AddNewSheetBreak("Ошибки", TableErrors);
      while( count < ErrorStr )

         Rep.AddPrintCell( Errors[count] , 0, 0, "l");
         Rep.AddStr();

         count = count + 1;
      end;
   end;
end;
```

---

## Пример 38: `ПроводкиОтнесенияНадежных`

**Источник:** `Mac/DLNG/TRUST/trvaprdslib.mac`
**Тип:** `macro`
**Размер:** 100 строк

```rsl
  MACRO ПроводкиОтнесенияНадежных(ValueDate)
    var i = 0;
    var stat = 0;
    var natsum = 0.0;
    var Ground = "";
    var bnrfd = null, fd = null;

    //дисконт
    while((not stat) and (i<parmOD.size))

      natsum = parmOD[i].Summ;

      if(parmOD[i].fiid != NATCUR)
        if( (not TS_SmartConvertSum( natsum, parmOD[i].Summ, ValueDate, parmOD[i].fiid, NATCUR, true ) ) )
          stat = 1;
        end;
      end;

      fd = OrderFD;
      Ground = "Отнесение начисленного ранее дисконтного дохода на доход ";
      if(not GroupByIssuer)
        if((fromTick == true) and (ValType(tickfd) != V_UNDEF))
          bnrfd = TS_VABnrFD(DL_VSBANNER, parmOD[i].BCIDs[0], tickfd.tick.rec.BOfficeKind, tickfd.tick);
        else
          bnrfd = TS_VABnrFD(DL_VSBANNER, parmOD[i].BCIDs[0], NULL, NULL);
        end;
        Ground = Ground + bnrfd.CreateGroundByBnr("векселя (_IssuerName_, _BCSeries_, _BCNumber_)");
        fd = bnrfd.ctgfd;
      end;

      if( not ПроводкаПоКатегориямУчетаПоДоговору(
                 fd,
                 NULL,
                 NULL,
                 parmOD[i].DebetAcc, parmOD[i].CreditAcc,
                 ValueDate,
                 parmOD[i].DebetAcc.rec.Chapter,
                 parmOD[i].fiid,
                 parmOD[i].Summ,
                 null,
                 OrderFD.Number,
                 Ground,
                 null, null,
                 null, null,
                 NATCUR, natsum
                 )
          )
            stat = 1;
      end;

      i = i+1;
    end;

    //проценты
    i=0;
    while((not stat) and (i<parmOP.size))
      natsum = parmOP[i].Summ;

      if(parmOP[i].fiid != NATCUR)
        if( (not TS_SmartConvertSum( natsum, parmOP[i].Summ, ValueDate, parmOP[i].fiid, NATCUR, true ) ) )
          stat = 1;
        end;
      end;

      fd = OrderFD;
      Ground = "Отнесение начисленного ранее процентного дохода на доход ";
      if(not GroupByIssuer)
        if((fromTick == true) and (ValType(tickfd) != V_UNDEF))
          bnrfd = TS_VABnrFD(DL_VSBANNER, parmOP[i].BCIDs[0], tickfd.tick.rec.BOfficeKind, tickfd.tick);
        else
          bnrfd = TS_VABnrFD(DL_VSBANNER, parmOP[i].BCIDs[0], NULL, NULL);
        end;
        Ground = Ground + bnrfd.CreateGroundByBnr("векселя (_IssuerName_, _BCSeries_, _BCNumber_)");
        fd = bnrfd.ctgfd;
      end;

      if( not ПроводкаПоКатегориямУчетаПоДоговору(
                 fd,
                 NULL,
                 NULL,
                 parmOP[i].DebetAcc, parmOP[i].CreditAcc,
                 ValueDate,
                 parmOP[i].DebetAcc.rec.Chapter,
                 parmOP[i].fiid,
                 parmOP[i].Summ,
                 null,
                 OrderFD.Number,
                 Ground,
                 null, null,
                 null, null,
                 NATCUR, natsum
                 )
          )
            stat = 1;
      end;
      i = i+1;
    end;

    return stat;
  END;
```

---

## Пример 39: `deleteNotDigit`

**Источник:** `Mac/Cb/fmexreq_func.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro deleteNotDigit(s)
    var ss = "";
    var len = strlen(s);
    var arr = TArray;
    arr = StrSplit2(s, 1);
    var i = 0;
    while (i < len)
        if ( (arr(i) >= "0") and (arr(i) <= "9"))
            ss = ss + arr(i);
        end;
        i = i + 1;
    end;
    return ss;
end;
```

---

## Пример 40: `InsertHeadDocs_camt_052_053`

**Источник:** `Mac/Mbr/swmx_camt_lib.mac`
**Тип:** `macro`
**Размер:** 33 строк

```rsl
macro InsertHeadDocs_camt_052_053
( GrpHdrNode : XMLMesDocument, 
  NtryNodes : TArray, 
  wlhead, 
  wlmes,
  MainNodeCreDtTm : date,
  TranslateID : string
)

  for( var NtryNode, NtryNodes ) // ReportEntry10
    var TransferDate : date = DivideYYYY_MM_DDThhmmssZToDateTime(NtryNode.ReadOptionalNodeText("BookgDt/Dt"));
    if(TransferDate == BNK_ZERODATE)
      TransferDate = MainNodeCreDtTm;
    end;

    var NtryDtlsNodes = NtryNode.GetChildNodes("NtryDtls");

    for( var NtryDtlsNode, NtryDtlsNodes )
      var BtchNodes = NtryDtlsNode.GetChildNodes("Btch"); // BatchInformation2
      for( var BtchNode, BtchNodes )
        InsertWlconfByBtchNode_camt_052_053(GrpHdrNode, NtryNode, BtchNode, wlhead, wlmes, TransferDate, TranslateID);
      end;

      var TxDtlsNodes = NtryDtlsNode.GetChildNodes("TxDtls"); // EntryTransaction10
      for( var TxDtlsNode, TxDtlsNodes )
        InsertWlconfByTxDtlsNode_camt_052_053(GrpHdrNode, NtryNode, NtryDtlsNode, TxDtlsNode, wlhead, wlmes, TransferDate, TranslateID);
      end;
    end; // for NtryDtlsNode

  end; // for NtryNode

end; // macro InsertHeadDocs_camt_052_053
```

---
