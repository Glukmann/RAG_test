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

## Пример 16: `ImportParty`

**Источник:** `Mac/DLNG/DEPO/importParty.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro ImportParty(impIssuer:bool, impLicense:bool, impDepositary:bool)
  var impINN = null;
  var impLIZ = null;
  var impSDEP = null;
  var report = CReportImportParty();
  var statINN = -1, statLIZ = -1, statSDEP = -1;

  if (impIssuer)
    impINN = CImportINN(report);
    if (not impINN.getPath())
      msgbox("Ошибка при определении настройки DEPO\\INNCB_IMPORT. Справочник не загружается");
      impINN = null;
    end;
  end;
```

---

## Пример 17: `UnloadAccount`

**Источник:** `Mac/DEPOSITR/tr_acc.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro UnloadAccount(Acc);
  
  PrintLn( "Выгрузка одного счета" );
  PrintLn( "=====================\n" );

  UpdateExistingStrategy = S_QUERY_USER;

  UnloadAcc(Acc,True,FULL_UNLOAD,False);

  PrintLn( "\n--------------------------------------------" );
  Print( "Процедура завершилась " );
  if ( ErrorsOccured > 0 )
    PrintLn( "с ошибками" );
  else
    PrintLn( "успешно" );
  end;
```

---

## Пример 18: `PrintLogPmSend`

**Источник:** `Mac/Cb/giszhkhproc_rep.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro PrintLogPmSend(Type)
  BegAction (0, "Построение отчета о результатах передачи информации в RS-Connect");

  var Table : TTable = TTable();

  if( Type )
    PrintHeader();
    Table.Print();
    Table.PrintQueries();
  else
    PrintHeaderCharges();
    Table.PrintCharges();
  end;
```

---

## Пример 19: `PrintSWIFTMessageOutIn`

**Источник:** `Mac/DLNG/SECUR/boswift.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro PrintSWIFTMessageOutIn(DraftID, DraftKind)
  VAR ReportFileName, ProcName;
  var Text = "";
  ReportFileName = GetTxtFileName( "message");
  SetOutput( ReportFileName );

  Text = "Исходящее сообщение: \n\n";
  Text = Text + GetMsgText(DraftID, "GetMsgText", DraftKind);
  Text = Text + "\n\nВходящее сообщение: \n\n";
  Text = Text + GetMsgText(DraftID, "GetConfirmText", DraftKind);
  print(Text);

  SetOutput( NULL, true );
  ViewFile( ReportFileName );
end;
```

---

## Пример 20: `for_all_investors_report`

**Источник:** `Mac/DLNG/SECUR/spasssal.mac`
**Тип:** `macro`
**Размер:** 43 строк

```rsl
macro for_all_investors_report( rep_date, num2check, num_start )
     var  i = 0, j, head_printed = false;
     var hor_line = MkStr("─",COLUMN_LEN), owner_id,
         empty_line = mkstr(" ", COLUMN_LEN), acc_rest = $0;
     InitProgress(investors.size, "Поиск остатков", "Просмотр счетов ДЕПО");
     while ( i != num2check )
          iss_totrests[i] = $0;
          i = i + 1;
     end;
     i = 0;
     while ( i < investors.size )
              owner_id = investors[i];
              fill_rests( owner_id, rep_date, num2check, num_start );
              if ( ПолучитьСубъекта(owner_id,pt) != 0 )
                   println("Не могу получить анкету владельца счета ", depoacc.Code);
                   return;
              end;
                  acc_rest = inv_rests[i];
                  if ( rest_exist( num2check ) or (acc_rest != $0) )
                       if ( not head_printed )
                            table_header( num2check, num_start );
                            head_printed = true;
                       end;
                       print("├────────────────────┼──────────┼─────────────┼"); printline_end ( hor_line, num2check, "┼", "┤", -1 );
                       print("│",pt.ShortName:20,"│",ПолучитьКодСубъекта(owner_id,codekind2show):10,"│",acc_rest:13,"│"); printline_end ( iss_rests, num2check, "│", "│", 0 );
                       print("│",depoacc.Code:20,"│          │             │"); printline_end ( empty_line, num2check, "│", "│", -1 );
                       j = 0;
                       while ( j != num2check )
                            iss_totrests[j] = iss_totrests[j] + iss_rests[j];
                            j = j + 1;
                       end;
                  end;
          i = i + 1;
          UseProgress(i);
     end;
     RemProgress;
     if ( head_printed )
          print("└────────────────────┴──────────┴─────────────┴"); printline_end ( hor_line, num2check, "┴", "┘", -1 );
          println("");
          print("Итого по клиентам                ", tot_acc_rest:13, " "); printline_end ( iss_totrests, num2check, " ", "", 0 );
          [];
     end;
end;
```

---

## Пример 21: `decrease`

**Источник:** `Mac/DLNG/SECUR/spdpord.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro decrease( name )
[
     Списать со счета депонента

];
     print( "    ", name:40:t );
end;
```

---

## Пример 22: `ExecQIValidPeriodReport`

**Источник:** `Mac/DLNG/SECUR/ws_QIValidPeriod.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
MACRO ExecQIValidPeriodReport(MonitorDate)
  var FullNames = TArray(), Report;
  Report = QIValidPeriodReportXls(MonitorDate);
  Report.Run();
  FullNames = Report.GetFullReportFileNames(); 

  return CreateFileContainer(FullNames[0]);
END;
```

---

## Пример 23: `OutGateRep`

**Источник:** `Mac/CONV_FC/v_laros_fc_1.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
macro OutGateRep()
    var SaveDate = NullDate;

[+----------------------------------------------+
 | Вид вклада     |    Приход    |   Расход     |
 +----------------+--------------+--------------+];

   keynum( report, 3 );
   rewind( report    );

   while( next( report ) )
       if( SaveDate != report.Date )
          SaveDate = report.Date;
[       Обороты за ############ ]( SaveDate );
[+--------------------------------------------+];
       end;

[|################|#############|###############|]
( report.Kind, report.KredSum, report.DebSum );
[+----------------+---------------+-----------+];
   end;

end;
```

---

## Пример 24: `ПечататьОперация`

**Источник:** `Mac/Cb/fm_opprn.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
macro ПечататьОперация(fmop)
    if (fmop.OpType != FM_OP_TYPE_OTHER)
        var Title = "";
        var table = report.AddTable(1, 2);

        if (not report.IsPoi)
            table.table.BottomPadding = 0;
        end;

        if (fmop.OpType == FM_OP_TYPE_MONEY_TRANSFER) // перевод денежных средств
            Title = "Сведения об операции по переводу денежных средств";
            ПереводДенежныхСредств(table, fmop);
        elif (fmop.OpType == FM_OP_TYPE_CASH_TRANSACTION) // операция с наличными
            Title = "Сведения об операции с наличными денежными средствами";
            ОперацияНаличными(table, fmop);
        elif (fmop.OpType == FM_OP_TYPE_PAYMENT_CARD) // операция с платежной картой иностранного
            Title = "Сведения об операции с использованием платежной карты иностранного банка";
            ОперацияКартойИностранного(table, fmop);
        end;

        table.ApplyFirstRowAsHeader(Title);
    end;
end;
```

---

## Пример 25: `UploadAccount`

**Источник:** `Mac/DEPOSITR/tr_acc.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro UploadAccount(Acc);
  
  PrintLn( "Загрузка одного счета" );
  PrintLn( "=====================\n" );

  UpdateExistingStrategy = S_QUERY_USER;

  UploadAcc(Acc,True,FULL_UPLOAD);

  PrintLn( "\n--------------------------------------------" );
  Print( "Процедура завершилась " );
  if ( ErrorsOccured > 0 )
    PrintLn( "с ошибками" );
  else
    PrintLn( "успешно" );
  end;
```

---

## Пример 26: `setFmExReqData`

**Источник:** `Mac/Cb/fmexreq_db.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro setFmExReqData(exReqId, partyId, dateBegin, dateEnd, error:@string)
    var report = TrnFmExReqData;
    report.setFmExReqData(exReqId, partyId, dateBegin, dateEnd, @error);
    return report.getResult();
end;
```

---

## Пример 27: `Report`

**Источник:** `Mac/DEPOSITR/ingorder.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro Report( ApplicationKind, ApplicationKey )

  var
    BranchStrNum = "",
    DepartNum = "",
    DepartName = "";

  GetBranchParams( NumFNCash, BranchStrNum, DepartNum, DepartName );

  G_ApplicationKind = ApplicationKind;
  G_ApplicationKey = ApplicationKey;

  PrintList;

end;
```

---

## Пример 28: `PrintPayReqRSF`

**Источник:** `Mac/Cb/prpmrqvi.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
MACRO PrintPayReqRSF(): bool

  var PayerPr   :TPartyProperties = TPartyProperties("Payer",    pr_pmpaym, pr_debet,  pr_pmrmprop);
  var ReceiverPr:TPartyProperties = TPartyProperties("Receiver", pr_pmpaym, pr_credit, pr_pmrmprop);

  return PayOrder0401060Report( PayerPr, ReceiverPr ).Print();
END;
```

---

## Пример 29: `GenerateReport`

**Источник:** `Mac/DLNG/dl_rep_Register_269_TC.mac`
**Тип:** `macro`
**Размер:** 71 строк

```rsl
  MACRO GenerateReport()
    var LastNameFileTmp = "";

      if (panel.run() == -316)
          if (panel.isIP_IBC) InstLoadModule("mm_rep_Register_269_TC.mac"); end;

          BegAction(0, "Формирование отчета");

          Rep.OpenTemplate("Report_Register_269_TC.xls", false);

          FillVariable();

          IsExistsRepDataProfit = false;
          IsExistsRepDataCost   = false;
          ErrorMesage.ClearArray();

          if (panel.isProfit)
              SheetActivate("Доходы");
              FillHeaderProfit();
              if (panel.isIP_IBC) FillBodyProfitForIBC(); end;
              if (panel.isIP_SEC) FillBodyProfitForSecur(); end;
          end;

          if (panel.isCost)
              SheetActivate("Расходы");
              FillHeaderCost();
              if (panel.isIP_IBC) FillBodyCostForIBC(); end;
              if (panel.isIP_SEC) FillBodyCostForSecur(); end;
          end;

          ErrorModulePrefix = "";

          if (
              (not IsExistsRepDataProfit) and
              (not IsExistsRepDataCost)
             )
              ErrorLog("Нет данных для формирования отчета.");
          end;

          var SheetCount = 4;
          if (not IsExistsRepDataProfit)
              Rep.SheetDelete(1);
              SheetCount = SheetCount - 1;
          end;
		  
          if (not IsExistsRepDataCost)
              Rep.SheetDelete(SheetCount - 2);
              SheetCount = SheetCount - 1;
          end;

          if (ErrorMesage.size > 0)
              FillErrLog();
          else
              Rep.SheetDelete(SheetCount - 1);
          end;

          SheetActivate(1);

          EndAction();

          if (panel.repFormat == 2)
 
              LastNameFileTmp = SetOutPut(panel.repFilePath, true);
              LastNameFileTmp = SetOutPut(LastNameFileTmp, true);
              DelFile(panel.repFilePath);
              Rep.SaveAs(panel.repFilePath, WINREP_OUTPUT_EXCEL);
          else
              Rep.SaveAsTemplate(NULL, true);
          end;
      end;
  END;
```

---

## Пример 30: `PrintAkkreditivRSF`

**Источник:** `Mac/Cb/prpmacvi.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
MACRO PrintAkkreditivRSF( ncopy:integer ):bool

  var PayerProps   :TPartyProperties = TPartyProperties("Payer",    pr_pmpaym, pr_debet,  pr_pmrmprop);
  var ReceiverProps:TPartyProperties = TPartyProperties("Receiver", pr_pmpaym, pr_credit, pr_pmrmprop);

  return PayAkkr0401060Report(PayerProps, ReceiverProps).Print();

END;
```

---

## Пример 31: `Report`

**Источник:** `Mac/DLNG/SECUR/profitax.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro Report(FromDate, UptoDate, keep_silence, FIID, Sum/*structSum*/);
  var continueSale, continueBuy, FirstBuyFlag, i = 0;
  var OurDeals = DealFiltered (FromDate, UptoDate, FIID);
  var SaleDealNum, SaleDealAmount, SaleDealPrice,
       BuyDealNum,  BuyDealAmount,  BuyDealPrice,
      FinRezIn,
      FinRezOut,                       
      EstimIn,
      EstimOut,                        
      TaxOverpayment,
      TaxUnderpay;

  if(not keep_silence)
    InitProgress(OurDeals.NRecords, "Создание отчета... ", "Отчет по налогооблагаемой прибыли");
  end;
```

---

## Пример 32: `checkexec_OperationsOverValueNVPI`

**Источник:** `Mac/DLNG/SECUR/ws_monitorcheckexec.mac`
**Тип:** `macro`
**Размер:** 65 строк

```rsl
macro checkexec_OperationsOverValueNVPI(MonitorDate, TypeEvent) : integer
   
   var query, ds, str_select = "", report = "", report_all = "", FD, FD2, ErrCode, RegValue, Flag2 = false, NeedExecute = false;
   Flag2 = true;

   query = RSDCommand( GetSQL_UnprocessedObjects_OpOverValueNVPI(MonitorDate) );
   query.execute();

   ds = TRsbDataSet(query, RSDVAL_CLIENT, RSDVAL_STATIC);
   while( ds.MoveNext() )
      if( ds.DocKind == DL_SECURITYDOC )
         FD = SPFirstDoc( ds.DocKind, ds.DealID );
         if(FD.ExistBack)
            FD2 = SPFirstDoc( LEG_KIND_DL_TICK_BACK, ds.DealID );
         end;

         if( SP_DealNeedOverValueNVPI( MonitorDate, FD.tick ) != 0 )
            NeedExecute = false;
         else
            NeedExecute = true;
         end;

         if( (Flag2 == true) and (NeedExecute == false) )
            if( SP_RepoNeedOverValueNVPI( MonitorDate, FD.tick ) != 0 )
               NeedExecute = false;
            else
               NeedExecute = true;
            end;
         end;

         if( not NeedExecute )
            continue;
         end;

         report = report + String("   ", FD.tick.rec.DealDate:13, " | ", FD.tick.rec.DealCode:14, " | ", FD.fininstr().rec.FI_Code:15, " | ", FD.fininstr().rec.Name:27, "\n");
      elif( ds.DocKind == DL_NTGSEC )
         FD = DL_NettingDoc( ds.DocKind, ds.DealID );

         if( SP_NtgNeedOvervalueNVPI( MonitorDate, FD.dl_nett() ) != 0 )
            continue;
         end;

         report = report + String("   ", FD.dl_nett().rec.SigningDate:13, " | ", FD.DealNumber():14, " | ", "":15, " | ", "":27, "\n");
      end;
   end;

   if(report != "")
      report_all =

      "   Дата переоценки НВПИ: " + string(SubStr(String(MonitorDate),1,10):10) + "\n" +
      " ----------------------------------------------------------------------------------\n" +
      "   Дата операции | Номер операции |     Код ц/б     |       Наименование ц/б       \n" +    
      " ----------------------------------------------------------------------------------\n" + 
      report + 
      " ----------------------------------------------------------------------------------\n";
   end;

   WriteToProtocol(TypeEvent, MonitorDate, report_all );

   if(report != "")
      return STATE_NO_PROCESSED;
   else
      return STATE_PROCESSED;
   end;
end;
```

---

## Пример 33: `report`

**Источник:** `Mac/DEPOSITR/661.mac`
**Тип:** `macro`
**Размер:** 14 строк

```rsl
macro report;

  var namestr = "", address = "", i = 0, groupTurns;
  var GroupDebitTotalK = $0.0L, GroupCreditTotalK = $0.0L,
      DebitTotalK = $0.0L, CreditTotalK = $0.0L;
  var GroupDebitTotalN = $0.0L, GroupCreditTotalN = $0.0L,
      DebitTotalN = $0.0L, CreditTotalN = $0.0L;
  var GroupDebitTotalF = $0.0L, GroupCreditTotalF = $0.0L,
      DebitTotalF = $0.0L, CreditTotalF = $0.0L;

  namestr = {Name_Bank} + " " + {NumberBranch};
  if( statusBranch != I_DEPARTMENT_TYPE_FILIAL )
    namestr = namestr + " Филиал " + ddep.rec.Name;
  end;
```

---

## Пример 34: `PrintUnderLn`

**Источник:** `Mac/DEPOSITR/tr2stat.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro PrintUnderLn(Str, UlChr)

  var
    Len = StrLen(Str),
    i = 0;

  PrintLn(" " + Str);
  Print(" ");
  while(i < Len)
    Print(UlChr);
    i = i + 1;
  end;
```

---

## Пример 35: `PrintBottom`

**Источник:** `Mac/DEPOSITR/passive1.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro PrintBottom

  [--------------------------------------------------------------------------------------------------------------------];
  Print( StrFor( 12 ) );
end;
```

---

## Пример 36: `PrintEnd`

**Источник:** `Mac/Invh/R_ware.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
macro PrintEnd ()
  /*печать подвала*/
  Report(3);
         /*"", "", "", "", "",
         "", "", "", "", "", "");*/
end;
```

---

## Пример 37: `MakeReport`

**Источник:** `Mac/DEPOSITR/act_prn.mac`
**Тип:** `macro`
**Размер:** 32 строк

```rsl
MACRO MakeReport( prmode, /* режим печати*/
                  copies /* количество копий отчетных документов */ )
    /* по умолчанию печатается все подряд в одном экземпляре */  
    if ( (ValType( prmode ) == V_UNDEF) )
        prmode = PRMODE_ACT_SPEC_LIST;    
    end;
 
    if ( (ValType( copies ) == V_UNDEF) or (copies <= 0) )
        copies = 1;
    end;

    if ( (prmode != PRMODE_LIST) and not RunActTakePanel() )
        if ( (prmode == PRMODE_ACT_SPEC) or (prmode == PRMODE_ACT) )
            return;
        else
            prmode = PRMODE_LIST;  
        end;     
    end;     

    var report = ActTakeReport( prmode );    

    report.pump();
    report.formatData();

    while ( copies > 0 )
    report.print();
        copies = copies - 1;
    end;

onError( errObj );
    msgbox( what(errObj) );  
END;
```

---

## Пример 38: `FormReport`

**Источник:** `Mac/BOOK/IPSRecipSend.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
macro FormReport(numpart,   // номер пачки
                 errText,   // текст ошибки, не связанной с получателем
                 responce ) // структура ответа получателя
  SetOutput(getFullRepName(), true);

  if(errText == "")
    if( numpart == 0 )
      print("Синхронизация со справочником RS-Connect");
    end;
    print("\n\t Отправка сообщения в RS-Connect " + (numpart + 1) + ":");
    if(responce.responseConnectData.objectError.ErrorCode != "0")
      print("\n\t\tСообщение не принято со следующими ошибками:");
      var j = 0;
      while(j < responce.responseConnectData.objectError.ErrorText.size)
        print("\n\t\t" + responce.responseConnectData.objectError.ErrorText[j]);
        j = j + 1;
      end;
      print("\n");
    else
      print("\n\t\t Выполнено успешно");
    end;
  else
    print(errText);
  end;
```

---

## Пример 39: `Блок`

**Источник:** `Mac/DLNG/SECUR/IncaccpsReg.mac`
**Тип:** `block`
**Размер:** 15 строк

```rsl
  if( RepForm.GetFieldValue( PNFLD_INCACCPS_REG_NOTGOS ) == true )
    /* затем запускаем 8-2 */
    NGosRep = SP_TxReg82_Report( RepForm.GetFieldValue( PNFLD_INCACCPS_REG_DEPCODE ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_PERIOD ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_YEAR ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_CIRCINMARKET ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_NOTCIRCINMARKET ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_NOMINRUR ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_NOMINCUR ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_AVRCODE ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_BACKREPO ),
                                 RepForm.GetFieldValue( PNFLD_INCACCPS_REG_PRINTMETHOD ) );
    NGosRep.Run();
  end;
end;
```

---

## Пример 40: `Constructor`

**Источник:** `Mac/DEPOSITR/merge_br.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
Macro Constructor

 var OpenStat = True;

  if( not Create( Report ) )
     OpenStat = False;
  end;
```

---
