# Практика: Печатные формы и отчёты (JasperReports, TRepForm, TStreamDoc)

**Теория:** [BnRSL.md## Класс: `TRepForm`]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `EAM_MakeHeaderTextAttach`

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

## Пример 2: `ReportRun706`

**Источник:** `Mac/DLNG/DV/dvbycntr706.mac`  
**Тип:** `private macro`  
**Размер:** 58 строк

```rsl
PRIVATE MACRO ReportRun706( Report:variant )
   RECORD REmi( party );
   RECORD DEmi( party );
   var Fininstr = TRecHandler("fininstr.dbt");
   var AV = Trechandler( "avoiriss.dbt" );
   var NRec = 0, FD, Count = 0; 
   var EmiID, CFI, Summa = $0, NumInList = "";

   /*отбираем поставочные сделки форвард, в которых НЕ выставлен признак ПФИ и которые в БОЦБ еще не пришли*/
   var RsdDVQuery, DVDealData,
       DVQuery = " SELECT DVDeal.T_ID, DVDeal.t_DocKind " +
                 "   FROM ddvndeal_dbt DVDeal, dfininstr_dbt fin, ddvnfi_dbt nfi " +
                 "  WHERE nfi.T_DealID = DVDeal.T_ID " +
                 "    and nfi.T_TYPE = 0 " +
                 "    and fin.t_fiid = nfi.T_fiid " +
                 "    and fin.t_FI_KIND = ? " +/* отбираем сделки, кот. совершены с исходным активом - ценной бумагой */
                 "    and DVDeal.T_IsTrust = chr(0) " +
                 "    and DVDeal.T_DVKIND in (?, ?, ?) "+
                 "    and DVDeal.T_State > 0 " +
                 "    and DVDeal.T_Date >= ? " +
                 "    and DVDeal.T_Date <= ? " +
                 "    and nFI.t_ExecType = ? " +
                 "    and not exists (select 1 " +
                 "                      from DPARTYOWN_DBT PARTYOWN " +
                 "                     where PARTYOWN.T_PARTYID = DVDeal.T_Contractor " +
                 "                       and PARTYOWN.T_PARTYKIND = ? " +/*Сделка считается внебиржевой, если контрагент по сделке не равен бирже*/
                 "                   ) ";
                                                                                       
   RsdDVQuery = DL_RSDCommand(DVQuery);

   RsdDVQuery.addParam(FIKIND_AVOIRISS);
   
   RsdDVQuery.addParam(DV_FORWARD);
   RsdDVQuery.addParam(DV_FORWARD_T3);
   RsdDVQuery.addParam(DV_OPTION);
   
   RsdDVQuery.addParam(Report.GetBegDate());
   RsdDVQuery.addParam(Report.GetEndDate());
   RsdDVQuery.addParam(DVSETTLEMET_STATE);
   RsdDVQuery.addParam(PTK_MARKETPLASE);

   NRec = RsdDVQuery.GetCount();

   DVDealData = RsdDVQuery.execute();
                                                                                                                
   InitProgress( NRec, "Отчет \"Сведения об объемах внебиржевых сделок\"", "Просмотр внебиржевых сделок с ПФИ" );
   while( DVDealData.MoveNext() )
      FD = DVFirstDocNDeal(DVDealData.DocKind, DVDealData.ID);

      ClearRecord( FDlByCntrTmp );
      ClearRecord( REmi );
      
      /*Замена эмитента возможна только для облигаций, в этом случае получим его из истории*/
      if( FI_IsBond(FD.BaseFI()))
         EmiID = FI_GetIssuerOnDate( FD.BaseFI(), Report.GetEndDate());   
      else
         EmiID = FD.BaseFI().rec.Issuer;
      end;
```

---

## Пример 3: `SC_RunCmd`

**Источник:** `Mac/DLNG/SECUR/scsrvrepfun.mac`  
**Тип:** `macro`  
**Размер:** 23 строк

```rsl
MACRO SC_RunCmd(CmdStr)
  var cmdFName     = SP_GetGUID()+".cmd";
  var cmdFullPath  = GetRepFullPath(false);
  var cmdFullFName = cmdFullPath + cmdFName; //полный путь до исполняемого файла (на СП)
  var SAcmdFullFName = cmdFullFName;      //полный путь до исполняемого файла на СП
  var err = 0;
  var f = TStreamDoc(cmdFullFName, "C");

  f.WriteLine(CmdStr);
  f = NULL;

  if(not isStandAlone())
    //скопируем файл на терминал
    var termDir = GetRepFullPath(true); //полный путь до директории отчетов на терминале

    err = SC_CopyFile(cmdFullPath, "$" + termDir, cmdFName);

    if(err)
      msgbox("Ошибка при копировании исполняемого файла на терминал");
      cmdFullFName = "";
    else
      cmdFullFName = "$" + termDir+cmdFName;
    end;
```

---

## Пример 4: `Report`

**Источник:** `Mac/DLNG/SECUR/spturnrp.mac`  
**Тип:** `macro`  
**Размер:** 16 строк

```rsl
macro Report(LogOprID, fi_id, beg_date, end_date)
   var ItogFirst = 0, ItogDebet = 0, ItogCredit = 0;
   var bal_ItogFirst = 0, bal_ItogDebet = 0, bal_ItogCredit = 0;

   var AvrList = ReportFIIDs();
   var stat, stat_1, CountReport = 0;
   var query, is_header_first;
   var isFirst = false;

   stat = AvrList.FirstFIID();
   while(stat)
      if(AvrList.Rec.FIID == -1 )
        __Individual = true;
      else
        __Individual = false;
      end;
```

---

## Пример 5: `printReportRSF`

**Источник:** `Mac/DLNG/FOREX/fxreprdl2.mac`  
**Тип:** `macro`  
**Размер:** 13 строк

```rsl
MACRO printReportRSF( FIID_Request, FIID_Liability, p_dealstatus )
//var grp = TReportsGroup();

   /* Установить параметры отчета по переданным значениям */
   FI_Req = FIID_Request;
   FI_Liab = FIID_Liability;
   _DealStatus = p_dealstatus;

   if(PrintBody(/*grp*/) == true)
//      grp.Print( TRUE );
   else
      msgbox( "Нет данных, удовлетворяющих заданной фильтрации." );
   end;
```

**Комментарий автора:**
var grp = TReportsGroup(); Установить параметры отчета по переданным значениям */

---

## Пример 6: `CopyDepClient`

**Источник:** `Mac/DEPOSITR/merge_br.mac`  
**Тип:** `macro`  
**Размер:** 16 строк

```rsl
macro CopyDepClient( CodClient );

  var
    Stat=True;

  From(I_DepClient).CodClient = CodClient;
  if(GetEQ(From(I_DepClient)))
    /* Берем только что вставленную запись в файл отчета */
    /* Если она есть! */
    if( GetDirect( Report ) )
      Report.FIO = String( Trim( From( I_DepClient ).Sname ) + " " +
                           Trim( From( I_DepClient ).Name  ) + " " +
                           Trim( From( I_DepClient ).Pname )        );
      if( not Update( Report ) )
        PrintLn (" Запись в файле отчёта не обновлена ");
      end;
```

---

## Пример 7: `exec_guidepaym`

**Источник:** `Mac/DLNG/SECUR/ws_monitorexecution.mac`  
**Тип:** `macro`  
**Размер:** 23 строк

```rsl
macro exec_guidepaym(MonitorDate,KindPay)
  var FullNames = TArray(), Report;

  Report = Guidepaym_ReportXls(MonitorDate,KindPay);
  Report.Run();
  FullNames = Report.GetFullReportFileNames(); 

  return CreateFileContainer(FullNames[0]);

/*
  var protocol = report_guidepaym(MonitorDate, KindPay);

  SetOutput( string("..\\txtfile\\protocol_", Random(998)+1,".txt"), false );

  println(protocol);

  var prevName = SetOutput( null, true );
  var FC = CreateFileContainer(ConvertTxt2Html(prevName));
  RemoveFile(prevName);
  RemoveFile(prevName + ".html");
  return FC;
*/
end;
```

---

## Пример 8: `PrintExcelReport`

**Источник:** `Mac/BOOK/form253.mac`  
**Тип:** `macro`  
**Размер:** 20 строк

```rsl
Macro PrintExcelReport()

	/*Устанавливаем макрос выравнивания в таблице (BSV)*/
	Rep.SetExecuteMacro("253SpcFrmt.mac");

	Rep.PrintExcelRep(1, Head5 );

	/*Устанавливаем выравнивание в таблице (не работает на терминале, переехало в 253SpcFrmt.mac)(BSV)*/
	/*Rep.ObjExcel.SetDiapazon(12,0,19,6);
	Rep.ObjExcel.SetAlign(ALIGN_CENTER);
	Rep.ObjExcel.Range.VerticalAlignment = -4108;

	Rep.ObjExcel.SetDiapazon(17,1,19,1);
	Rep.ObjExcel.SetAlign(ALIGN_LEFT);*/

   /* Делаем окно с Excel активным */

	Rep.ShowExcel();
	Exit(1);
End;
```

**Комментарий автора:**
Устанавливаем макрос выравнивания в таблице (BSV)*/

---

## Пример 9: `DoReport`

**Источник:** `Mac/DEPOSITR/merge_br.mac`  
**Тип:** `macro`  
**Размер:** 25 строк

```rsl
Macro DoReport( BranchName_From , BranchName_To )

  var TmpType = "";
  var Counter = 0l;
  var Itog    = $0;
  var i       = 0 ;

  OutHead   ( BranchName_From , BranchName_To);

  ClearRecord(Report);
  KeyNum(Report , 0);
  Rewind(Report);

  TmpType = Report.ВидВклада;

  Initprogress ( NRecords ( Report ) , NULL , " Формирование отчета ");
  While ( next ( report ) )

      If( TmpType == Report.ВидВклада )
          Counter = Counter + 1 ;
          Itog    = Itog    + Report.Rest ;
      else
          if( TmpType!= "" )
              OutBottom( Counter , Itog  , TmpType );
          end;
```

---

## Пример 10: `DL_FldProc_PrintMethod`

**Источник:** `Mac/DLNG/DlRepForm_h.mac`  
**Тип:** `macro`  
**Размер:** 11 строк

```rsl
MACRO DL_FldProc_PrintMethod( pThis:DL_CPanel, Cmd:INTEGER, Key:INTEGER, FldShowValue:@VARIANT, FldRealValue:@VARIANT ):INTEGER
  MACRO Name( Id:INTEGER )
     if( Id == DL_OUTREPORT_STD )
        return "Стандартный";
     elif( Id == DL_OUTREPORT_EXCEL )
        return "Excel";
     elif( Id == DL_OUTREPORT_TXT)
        return "Текстовый файл с разделителями";
     elif( Id == DL_OUTREPORT_EXCEL_NO_FORMAT )
        return "Excel, без форматирования";
     end;
```

---

## Пример 11: `GosFileToDbt`

**Источник:** `Mac/Cb/impcciso_gos.mac`  
**Тип:** `macro`  
**Размер:** 13 строк

```rsl
macro GosFileToDbt(GosListPath, ErrText : @string)
    Message("Загрузка файла " + GosListPath + " в БД. Ждите...");
    var doc = TStreamDoc(GosListPath, "R", "rsansi");

    var del_cmd = RsdCommand("DELETE FROM DGOSLIST_TMP");
    del_cmd.execute;

    var Line = "";
    while (doc.readLine (@Line))
        if (StrLwr(Line) == "приложение а")
            if (GotoBeforeFirstTableRecord(doc))
                ReadTableRecords(doc);
            end;
```

---

## Пример 12: `AdmListFooter`

**Источник:** `Mac/DLNG/DEPO/dpadmlst.mac`  
**Тип:** `private macro`  
**Размер:** 23 строк

```rsl
private macro AdmListFooter()
  var Excel;
  var err;
  
  DP_StdFooter_Ex(Rep, RepFontStyleTitel, NULL, NULL, tablewidth);
  if(запуск_из_адм_операций == true)
    RemProgress();

    GetRegistryValue( "DEPO\\DEPOREPTOEXCEL", V_BOOL, Excel, err );
    //AdmListFooter() вызывается последней из GenAdmReport(), файл dpdpadm.c; поэтому здесь вызывается DP_EndProtocol()
    if(not err)
       DP_AddProtocol(Rep, "protocol");  //добавим протокол к уже сформированному отчету
       DP_EndProtocol();                 //закончить протоколирование

       InExcel(Excel);
    else
       MsgBox("Не могу найти настройку выпуска отчетов в Excel");

       DP_AddProtocol(Rep, "protocol");  //добавим протокол к уже сформированному отчету
       DP_EndProtocol();                 //закончить протоколирование
       
       InExcel(false);
    end;
```

---

## Пример 13: `exec_run_calc_comiss`

**Источник:** `Mac/DLNG/SECUR/ws_monitorexecution.mac`  
**Тип:** `macro`  
**Размер:** 12 строк

```rsl
macro exec_run_calc_comiss(MonitorDate)
  var filename = string("..\\txtfile\\protocol_",{oper},".txt");
  var report = "exec";

  SetOutPut(filename);
  if(RunComCalc(MonitorDate,-1,-1,-1,-1,1,false,@report) == 0)
    SetOutput (NULL,TRUE);
    var FC = CreateFileContainer(ConvertTxt2Html(filename));
    RemoveFile(filename);
    RemoveFile(filename + ".html");
    return FC;
  end;
```

---

## Пример 14: `DL_FldProc_NpTxPrintMethod`

**Источник:** `Mac/DLNG/DlRepForm_h.mac`  
**Тип:** `macro`  
**Размер:** 7 строк

```rsl
MACRO DL_FldProc_NpTxPrintMethod( pThis:DL_CPanel, Cmd:INTEGER, Key:INTEGER, FldShowValue:@VARIANT, FldRealValue:@VARIANT ):INTEGER
  MACRO Name( Id:INTEGER )
     if( Id == DL_OUTREPORT_STD )
        return "Стандартный";
     elif( Id == DL_OUTREPORT_EXCEL )
        return "Excel";
     end;                                           
```

---

## Пример 15: `FldProc_NpTxPrintMethod`

**Источник:** `Mac/DLNG/SECUR/nptxpit2_form.mac`  
**Тип:** `macro`  
**Размер:** 7 строк

```rsl
MACRO FldProc_NpTxPrintMethod( pThis:DL_CPanel, Cmd:INTEGER, Key:INTEGER, FldShowValue:@VARIANT, FldRealValue:@VARIANT ):INTEGER
  MACRO Name( Id:INTEGER )
     if( Id == DL_OUTREPORT_EXCEL )
        return "Excel";
     elif( Id == DL_OUTREPORT_XML )
        return "XML";
     end;                                           
```

---

