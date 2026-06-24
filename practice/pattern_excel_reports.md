# Практика: Excel, печатные формы и шаблоны отчётов (AddPrintCell, CopyAllSheetInTotalBook, ExportToExcel, Template)

**Теория:** [BnRSL.md## Класс: `TRepForm`]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `SvOpSetInitParms`

**Источник:** `Mac/DLNG/SECUR/scservop.mac`  
**Тип:** `macro`  
**Размер:** 31 строк

```rsl
MACRO SvOpSetInitParms(p_dl_com)
  VAR dl_comm_buf = TRecHandler( "dl_comm" );
  dl_comm_buf.SetRecordAddr( p_dl_com );

  /*пример*/
  // if( dl_comm_buf.rec.DocKind == DL_GET_INCOME )
  //    dl_comm_buf.rec.Flag1        = SET_CHAR;/*процентный*/
  //    dl_comm_buf.rec.Flag4        = UNSET_CHAR;/*дисконтный*/
  //    dl_comm_buf.rec.Flag5        = UNSET_CHAR;/*только по выпускам ц/б, где были движения*/
  //    dl_comm_buf.rec.Flag7        = UNSET_CHAR;/*Начисление корректировки по ЭПС*/
  //    dl_comm_buf.rec.Flag2        = SET_CHAR;/*доход, подлежащий выплате контрагентам по сделкам РЕПО/займа*/
  //    dl_comm_buf.rec.Flag3        = SET_CHAR;/*Начисление дохода (расхода) по сделкам РЕПО/займа*/
  //    dl_comm_buf.rec.CreateReport = SET_CHAR;/*Формировать отчет*/
  // elif( dl_comm_buf.rec.DocKind == DL_OVERVALUE )
  //    /*выставим все галочки*/
  //    dl_comm_buf.rec.Flag2        = SET_CHAR;/*выпуски, с которыми были заключены сделки*/
  //    dl_comm_buf.rec.Flag3        = SET_CHAR;/*выпуски, по которым была поставка ц/б*/
  //    dl_comm_buf.rec.Flag4        = SET_CHAR;/*выпуски, по которым была оплата ц/б*/
  //    dl_comm_buf.rec.Flag6        = SET_CHAR;/*переоценка только Т/О, исполняемых на следующий день*/
  //
  //    if( (dl_comm_buf.rec.Flag2 == SET_CHAR) or (dl_comm_buf.rec.Flag3 == SET_CHAR) or (dl_comm_buf.rec.Flag4 == SET_CHAR) )
  //       dl_comm_buf.rec.Flag1 = SET_CHAR;/*Вложения в ценные бумаги*/
  //    end;
  //    if( (dl_comm_buf.rec.Flag6 == SET_CHAR) )
  //       dl_comm_buf.rec.Flag5 = SET_CHAR;/*Требования/обязательства по возврату ц/б*/
  //    end;
  //
  //    dl_comm_buf.rec.CreateReport = SET_CHAR;/*Формировать отчет*/
  // end;

END;
```

---

## Пример 2: `ПечататьОбщиеПараметры`

**Источник:** `Mac/Cb/scdpcert.mac`  
**Тип:** `macro`  
**Размер:** 36 строк

```rsl
macro ПечататьОбщиеПараметры()
   var width = 25;
   var FaceValue = "";
   var FaceValueFI = "";
   var CloseDate;
   file fin("fininstr");
   file dp("dp_dep");
   var CCY = "";
   var RetSumm = "-";
   var Cost = "-";
   var Department = "-"; 

   CertRep.AddEmptyStr();

   //1. Дата составления
   CertRep.AddStr();
   CertRep.AddPrintCell( "составлена:", width, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( invcard.RegistrDate, 0, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //2. состояние карточки
   CertRep.AddStr();
   CertRep.AddPrintCell( "состояние карточки:", width, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( GetNameAlg( 5211, invcard.Status), 0, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( "установлено: " + invcard.StatusDate, 0, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //3.кол-во сертификатов
   CertRep.AddStr();
   CertRep.AddPrintCell( "всего сертификатов:", width, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( 1+" (" +NumToStr(1)+") шт.", 0, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //4.всего на сумму
   FaceValue   = vficert.FaceValue;
   FaceValueFI = vficert.FaceValueFI;
   
   if( FaceValueFI != -1)
     fin.FIID = FaceValueFI;
     if( GetEQ(fin))
       CCY = fin.CCY;
     end;
```

---

## Пример 3: `ПечататьПараметрыСертификата`

**Источник:** `Mac/Cb/scdpcert.mac`  
**Тип:** `macro`  
**Размер:** 40 строк

```rsl
macro ПечататьПараметрыСертификата(CertStr)
   
   var FaceValue = "-", FaceValueFI = "-";
   var FiName = "";
   var FiCode = "";
   var Price = "", Factor = "";
   var BaseStr = "";
   file fin("fininstr");
   file avrk("avrkinds.dbt");

   fin.FIID = vficert.FIID;
   GetEQ(fin);  //бумаги не может не быть ни при каких условиях

   avrk.FI_Kind   = fin.FI_Kind;
   avrk.AvoirKind = fin.AvoirKind;
   GetEQ(avrk);
   
   CertRep.AddEmptyStr();
   //1.заголовок
   CertRep.AddStr();
   CertRep.AddPrintCell( "ПАРАМЕТРЫ "+CertStr+" СЕРТИФИКАТА", 60, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //2.код ФИ
   CertRep.AddStr();
   CertRep.AddPrintCell( sign+"код анкеты:", 25, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( fin.FI_Code, 20, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //3.имя ФИ
   CertRep.AddStr();
   CertRep.AddPrintCell( sign+"наименование:", 25, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( fin.Name, 20, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //4.Вид сертификата
   CertRep.AddStr();
   CertRep.AddPrintCell( sign+"вид:", 25, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   CertRep.AddPrintCell( avrk.Name, 40, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   //5.Дата внесения вклада
   CertRep.AddStr();
   if( FI_AvrKindsEQ( FIKIND_AVOIRISS, AVOIRISSKIND_SAVING_CERTIFICATE, vficert.AvoirKind ))
     CertRep.AddPrintCell( sign+"дата внесения вклада:", 30, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   elif( FI_AvrKindsEQ( FIKIND_AVOIRISS, AVOIRISSKIND_DEPOSIT_CERTIFICATE, vficert.AvoirKind ))
     CertRep.AddPrintCell( sign+"дата внесения депозита:", 30, 0, "l:" + FontStyleTitel, REP_ELEM_STR );
   end;
```

---

## Пример 4: `EAM_MakeHeaderTextAttach`

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

## Пример 5: `GetOffices`

**Источник:** `Mac/Cb/kgrko_imp.mac`  
**Тип:** `private macro`  
**Размер:** 23 строк

```rsl
private macro GetOffices(kobrcode)
    var result;
    var outResponse = "";

    var stat = SendSoap("GetOffices", "IntCode", kobrcode, @outResponse);
    if (stat)
        result = -1;
    else
        var xml = CreateXMLParser();
        xml.validateOnParse = true;
        xml.async = false;

        stat = xml.loadXML(outResponse);

        if(stat)
            var CoOffices = xml.getElementsByTagName("CoOffices").item(0);

            if (ValType(CoOffices) != V_UNDEF)
                var i = 0;
                var size = CoOffices.childNodes.length;
                if (size)
                    result = TArray(size);
                end;
```

---

## Пример 6: `GetESAccRest`

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

## Пример 7: `PrintTableFooter`

**Источник:** `Mac/DLNG/SECUR/repadvnr.mac`  
**Тип:** `private macro`  
**Размер:** 35 строк

```rsl
private macro PrintTableFooter( Party, IsOurClient )
   var
      JurAddress, PostalAddress, PartyFullName, OurFullName;

   /* H2 - Юридический адрес стороны по сделке, для которой формируется
      уведомление */
   JurAddress = GetPartyAddress( Party.PartyID );

   /* H3 - Почтовый адрес стороны по сделке (из анкеты субъекта), для
      которой формируется уведомление */
   PostalAddress = GetPartyAddress( Party.PartyID, false, false, PTADDR_POST );
       Rep.AddPrintCell("Место нахождения: " + JurAddress, Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
       Rep.AddStr();
       Rep.AddPrintCell("Адрес для получения почтовых отправлений: "+ PostalAddress, Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
       Rep.AddStr();

  
   if( IsOurClient )
      /* H4 -  Полное наименование стороны по сделке, для которой формируется
               уведомление, дополненное слева текстом "По поручению ".
               Заполняется, только если указанная сторона по сделке - наш
               клиент, действующий по договору */
      PartyFullName = Party.Name;

      /* H5 -  Полное наименование нашего банка, дополненное слева текстом
               "уведомление направляется ". Заполняется, только если
               указанная сторона по сделке - наш клиент, действующий по
               договору. */
      OurFullName = GetPartyFullNameByID( {OurBank} );
       Rep.AddPrintCell("По поручению " + PartyFullName, Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
       Rep.AddStr();
       Rep.AddPrintCell("уведомление направляется " + OurFullName, Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
       Rep.AddStr();

       end;
```

---

## Пример 8: `GenDoc_v2021_3_0`

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

## Пример 9: `PrintLogXls`

**Источник:** `Mac/Cb/pdnchklog_xls.mac`  
**Тип:** `macro`  
**Размер:** 38 строк

```rsl
macro PrintLogXls
(
  OpenCheck, 
  CloseCheck,
  PdnPartyKind,
  PartyID,
  CheckFinProc,
  CheckNeedDelete,
  CheckDecor,
  IsScheduler
)
  var ObjPrint:CTemplateXLS = CTemplateXLS(NULL, NULL, NULL, NULL, NULL, NULL, true); // основной объект отчёта
  
  ObjPrint.CreateTotalBook();

  var stat =  ObjPrint.OpenTemplate("pdnchklog.xls");
  if( stat )
    Var Table = ObjPrint.RegisterTable("N1_MainTable");

    var dattim = string(date:f);
    var datdat = string(time:f);
    var usr = string(({oper}));
    var usn = {Name_Oper};
    var sub = GetPartyFieldByID(PartyID);
    var csd = GetPdnPartyKindFieldByID(PdnPartyKind);

    Table.SetValueCell("dattim"                ,  dattim);
    Table.SetValueCell("datdat"                ,  datdat);
    Table.SetValueCell("usr"                   ,  usr   ); 
    Table.SetValueCell("usn"                   ,  usn   );
    Table.SetValueCell("sub"                   ,  sub   );
    Table.SetValueCell("csd"                   ,  csd   ); 
    Table.AddStr(); 

    Table.EndTable();

//    stat = ObjPrint.CopyAllSheetInTotalBook("Общие сведения"); // кидаем закладку в книгу
  end;
```

---

## Пример 10: `CBINF_Proc`

**Источник:** `Mac/Cb/cbinfrmn.mac`  
**Тип:** `macro`  
**Размер:** 18 строк

```rsl
macro CBINF_Proc( RegPath, OutType/*CBINF_Out...*/ )
    var this_stat, nmbRec = 0;
    var IsOurDoc;
    var LimitDate;
    var rs;         
    var cmd;        
    var f;
    file rminprop (rminprop) key 0;
    file corschem( corschem ) key 1;

    CBINF_ErrorStatus = 0;
    CBINF_Result = 0;
    

    if( OutType == CBINF_OutReport )
        if( PrintHeader( RegPath, LIST_RMINPROP ) )
            return CBINF_StatusError;
        end;
```

---

## Пример 11: `GenMes`

**Источник:** `Mac/Mbr/ufgm501.mac`  
**Тип:** `macro`  
**Размер:** 27 строк

```rsl
macro GenMes( addrMes, addrInfo )
  record wlmes(wlmes);
  record wlinfo(wlinfo);

  SetBuff( wlmes, addrMes );
  SetBuff( wlinfo, addrInfo );

  var xml : object = ActiveX("Microsoft.XMLDOM");  
  var mes : object = xml.createElement("ED501");
  mes.setAttribute("xmlns", "urn:cbr-ru:ed:v2.0");

  FillEDNoDateAuthorByRef_XMLField(mes, wlmes.TRN);
  UFEBS_InsertMesIdentificator(wlmes.MesID, ReadAttribute(mes, "EDNo"), ReadAttribute(mes, "EDDate"), ReadAttribute(mes, "EDAuthor"));
  mes.setAttribute("ActualReceiver", GetEDReceiverForED501(wlinfo) );

  var elem : object = null;

  // ProprietoryDocument
  elem = xml.createElement("ProprietoryDocument");  
  elem.appendChild(xml.createTextNode(""));
  mes.appendChild(elem);

  // ProprietoryAttachment
  var Narrative : string = "";
  if(not WlinfoHasAttachedObjects(wlinfo.InfoID))
    Narrative = ПрочитатьТекстИнфСообщения(wlinfo);
  end;
```

---

## Пример 12: `PrintFooter`

**Источник:** `Mac/DEPOSITR/getattach_fm_ex.mac`  
**Тип:** `private macro`  
**Размер:** 43 строк

```rsl
private MACRO PrintFooter( Отчет, Date_ )

  var i = 0;
  var strCodeISO;
  var strCode113;

  var saveCode113 = "ЮЮЮ";
  var saveInSum   = $0.0;
  var saveOutSum  = $0.0;

  SortSummaryByCurrency( );

  Отчет.AutoScan(
  "[                                                 \n" +
  " Итого по реестру                                 \n" +
  "                                                  \n" +
  " ┌──────┬────────┬──────────┬───────────────┬───────────────┐\n" +
  " │ Код  │   Код  │   Курс   │    Итого      │    Итого      │\n" +
  " │валюты│операции│          │    приход     │    расход     │\n" +
  " │      │        │          │               │               │\n" +
  "]()"
  );

  while ( i < ASize( AComplexCode ) )
    if ( ACode113( i ) == CodeTotal )

      if ( ( saveInSum != $0.0 )  OR  ( saveOutSum != $0.0 ) )

        Отчет.AutoScan(
        "[├──────┼────────┼──────────┼───────────────┼───────────────┤" +
        "]()"
        );

        Отчет.AutoScan(
        "[│######│########│##########│###############│###############│" +
        "]()",
        strCodeISO, "l",
        "Итого", "l",
        "",  "l",
        saveInSum, "r:0:2",
        saveOutSum,"r:0:2"
        );
      end;
```

---

## Пример 13: `exec_guidepaym`

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

## Пример 14: `ImportED501`

**Источник:** `Mac/Mbr/uf501.mac`  
**Тип:** `macro`  
**Размер:** 10 строк

```rsl
macro ImportED501(nodeED501 : object, WlmesTrn : string)
  // Получить текст из xml, декодировать и сохранить

  // ProprietoryDocument
  var ProprietoryDocumentNode : object = GetChildNode(nodeED501, "ProprietoryDocument");
  var Doc : string = StrSubst(StrSubst(ProprietoryDocumentNode.Text, "\n", ""), "\r", "");
  var FName : string = GetFileNameED501(WlmesTrn, "Doc");
  if( not DecodeAndSaveFileFromBase64(Doc, FName) )
    RunError("Ошибка при сохранении ProprietoryDocument");
  end;
```

**Комментарий автора:**
Получить текст из xml, декодировать и сохранить ProprietoryDocument

---

## Пример 15: `PrintExcelReport`

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

## Пример 16: `Блок`

**Источник:** `Mac/DLNG/SECUR/incaccps_Form.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
     AddFieldProc( 0, PNFLD_INCACCPS_REG_PERIOD,          DL_PNFLD_PERIOD,      @DL_FldProc_Period,      FormData.Period, 17, 8 ); 
     AddFieldProc( 0, PNFLD_INCACCPS_REG_YEAR,            DL_PNFLD_YEAR,        @DL_FldProc_Year,        FormData.Year );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_GOS,             H_GOS_CHECKBOX,       @DLUSR_FldProc_GosCheckBox, FormData.IsGos );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_AVRKIND,         H_AVRKIND,            @DLUSR_FldProc_AvrKind );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_NOTGOS,          H_NOTGOS_CHECKBOX,    @DLUSR_FldProc_GosCheckBox, FormData.IsNotGos );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_CIRCINMARKET,    DL_PNFLD_CHECKBOX,    @DL_FldProc_CheckBox,    FormData.CirculateInMarket );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_NOTCIRCINMARKET, DL_PNFLD_CHECKBOX,    @DL_FldProc_CheckBox,    FormData.NotCirculateInMarket );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_NOMINRUR,        DL_PNFLD_CHECKBOX,    @DL_FldProc_CheckBox,    FormData.NominateInRUR );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_NOMINCUR,        DL_PNFLD_CHECKBOX,    @DL_FldProc_CheckBox,    FormData.NotNominateInRUR );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_AVRCODE,         DL_PNFLD_AVRCODE,     @DLUSR_FldProc_AvrCode );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_AVRNAME,         DL_PNFLD_AVRNAME,     @Default );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_BACKREPO,        DL_PNFLD_CHECKBOX,    @DL_FldProc_CheckBox,    FormData.IsBackRepo );
     AddFieldProc( 0, PNFLD_INCACCPS_REG_PRINTMETHOD,     DL_PNFLD_PRINTMETHOD, @DL_FldProc_PrintMethod, DL_OUTREPORT_EXCEL, 36, 25 );
  END;
```

---

## Пример 17: `printHeader`

**Источник:** `Mac/DEPOSITR/FnsPercentServices.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
macro printHeader(peroid)
    [                       Ошибки форматно-логического контроля
            Налоговый период ####
    ] (peroid);
end;
```

---

## Пример 18: `Блок`

**Источник:** `Mac/DLNG/SECUR/dpcomrep.mac`
**Тип:** `block`
**Размер:** 12 строк

```rsl
      if(Data.ReportRun)
         if(Data.PrintHeadClient)
            EndCopyTable();
            Data.PrintHeadClient = false;
         end;
         AddStandardFooter("N1_");
         CopyAllSheetInTotalBook(NULL, false, "N1_Footer", 1);
      else
         PrintFormatString(
            "Нет начисленных или оплаченных комиссий, соответствующих параметрам отчета.",
            "N1_NoData", "Нет начисленных или оплаченных комиссий, соответствующих параметрам отчета."
         );
```

---

## Пример 19: `PrintLine`

**Источник:** `Mac/DLNG/SECUR/sprgjour.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro PrintLine(DepoAccCode, DepoType, OpenDate, CloseDate)
   DP_AddPrintCell( Rep, DepoAccCode, 0, 0, "l:" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, DepoType, 0, 0, "l:" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, OpenDate, 0, 0, "l:f:" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, CloseDate, 0, 0, "l:" + RepFontStyleTitel );
   Rep.AddStr();
end;
```

---

## Пример 20: `ReportHead`

**Источник:** `Mac/DLNG/DV/dvdlrrep.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro ReportHead( Period, Year )

   Rep.AddPrintCell("СВЕДЕНИЯ О СДЕЛКАХ С ЦЕННЫМИ БУМАГАМИ, СОВЕРШЕННЫХ ПРОФЕССИОНАЛЬНЫМ УЧАСТНИКОМ", Rep.GetHeaderWidth(), 0, "c:" + FontStyleTitel, REP_ELEM_STR);
   Rep.AddStr();
   Rep.AddPrintCell("за " + PeriodName_GetMonthsAndQuart( Period, Year ), Rep.GetHeaderWidth(), 0, "c:" + FontStyleTitel, REP_ELEM_STR);
   Rep.AddStr();
end;
```

---

## Пример 21: `PrintHeader`

**Источник:** `Mac/DEPOSITR/pcestimg.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
macro PrintHeader

  [ ];
  [            Групповой расчет и начисление накопленных процентов];
  [ ];
  [ +--------------------+------+-------------------------------+-------------+];
  [ |                    |      |          Сумма процентов      |             |];
  [ |     Вид вклада     |Валюта+-------------------------------+     Дата    |];
  [ |                    |      |   Начисленная |  Начисленная  |             |];
  [ |                    |      |    на дату    |     всего     |             |];
  [ +--------------------+------+---------------+---------------+-------------+];

  WasPrintHeader = TRUE;

end;
```

---

## Пример 22: `PrintStr`

**Источник:** `Mac/DLNG/DEPO/dpunconclmas.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro PrintStr(CodeDA, NameDA, NameDep, CodeDep,
               OpenDateDA, CodeDP, OpenDateDP)

   DP_AddPrintCell( Rep, ContrNum, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, ContrName, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, ContrDate, 0, 0, "l:w" + RepFontStyleTitel );

   DP_AddPrintCell( Rep, CodeDA, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, NameDA, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, NameDep, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, CodeDep, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, OpenDateDA, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, CodeDP, 0, 0, "l:w" + RepFontStyleTitel );
   DP_AddPrintCell( Rep, OpenDateDP, 0, 0, "r:w" + RepFontStyleTitel );
   Rep.AddStr();
end;
```

---

## Пример 23: `PrintLine`

**Источник:** `Mac/DLNG/DV/dvfcsapr.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro PrintLine( v_curDate, Code, ContrName, Curr, AccumMarginSum, InterestRate, InterestSum )

  Rep.AddPrintCell( Date(v_curDate):f, 0, 0, "c" );
  Rep.AddPrintCell( Code, 0, 0, "c");
  Rep.AddPrintCell( ContrName, 0, 0, "l");
  Rep.AddPrintCell( Curr, 0, 0, "c");
  Rep.AddPrintCell( Money(AccumMarginSum), 0, 2, "r");
  Rep.AddPrintCell( Double(InterestRate)+"%", 0, 4, "c");
  Rep.AddPrintCell( Money(InterestSum), 0, 2, "r");

  Rep.AddStr();
end;
```

---

## Пример 24: `DepoKindSubHeader`

**Источник:** `Mac/DLNG/SECUR/sprgjour.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro DepoKindSubHeader(Kind)
   if ( Kind == depo_acc_active )
      Rep.AddEmptyStr();
      DP_AddPrintCell( Rep, " Счета депо мест хранения", 30, 0, "l:" + RepFontStyleTitel,_isapp, REP_ELEM_STR );
      Rep.AddStr();
   else 
      Rep.AddEmptyStr();
      DP_AddPrintCell( Rep, " Счета депо депонентов", 30, 0, "l:" + RepFontStyleTitel,_isapp, REP_ELEM_STR );
      Rep.AddStr();
   end;
end;
```

---

## Пример 25: `PrintLine_VA`

**Источник:** `Mac/DLNG/dltkjrnl.mac`
**Тип:** `macro`
**Размер:** 84 строк

```rsl
macro PrintLine_VA( 
                 StrNumber,                                 
                 DealCode:string,                    
                 Date1: string,                      
                 DealKindName:string,                
                 ContrShortName:string,              
                 ClientShortName:string,             
                 SfContrNumber:string,               
                 IssShortName:string,                
                 AvrKind:string,                     
                 AvrSeries:string,                   
                 PayISO:string,
                 SumInNom:money,                    
                 PayCCY:string,                      
                 StateDate:string,                                      
                 StateFactDate:string,               
                 PayDate:string,                     
                 PayFactDate:string,                 
                 ReportKind:string,                  
                 ReportNum:string,                   
                 ReportDate:string                 
                )

   if( GetIdentProgram() == CodeFor("А") )
      Rep.AddPrintCell(DealCode,        0, 0, "c");/*Номер сделки ДУ в системе внутр. учета */
      Rep.AddPrintCell(date(Date1),     0, 0, "l");/*Дата заключения сделки*/
      Rep.AddPrintCell("вне биржи",     0, 0, "l");/*Для сделок модуля УВ всегда "вне биржи"*/
      Rep.AddPrintCell(DealKindName,    0, 0, "c");/*Вид сделки*/
      Rep.AddPrintCell(ContrShortName,  0, 0, "l");/*сокращенное наименование контрагента*/
      Rep.AddPrintCell(ClientShortName, 0, 0, "l");
      Rep.AddPrintCell("",              0, 0, "l");/*№  поручения клиента*/
      Rep.AddPrintCell(SfContrNumber,   0, 0, "l");
      Rep.AddPrintCell(IssShortName,    0, 0, "l");
      Rep.AddPrintCell(AvrKind,         0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");
      Rep.AddPrintCell(AvrSeries,       0, 0, "c");/*серия № векселя*/
      Rep.AddPrintCell("",              0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");/*Цена -для сделок модуля УВ, не заполняется*/
      Rep.AddPrintCell("",              0, 0, "c");/*Кол-во- не заполняется для векселей)*/
      Rep.AddPrintCell(SumInNom,        0, 4, "c");/*Сумма сделки  - Для НЭЦБ цена каждого векселя по сделке*/
      Rep.AddPrintCell(PayISO,          0, 0, "c");/*Для УВ - валюта цены каждого векселя по сделке*/
      Rep.AddPrintCell(StateDate +  "  " +  StateFactDate,  0, 0, "l");
      Rep.AddPrintCell(PayDate + "  " + PayFactDate,        0, 0, "l");
      Rep.AddPrintCell(ReportKind + " № " + ReportNum, 0, 0, "l");
      Rep.AddPrintCell(ReportDate,      0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");
   else
      Rep.AddPrintCell(StrNumber,       0, 0, "c");
      Rep.AddPrintCell(DealCode,        0, 0, "c");
      Rep.AddPrintCell(Date1,           0, 0, "l");
      Rep.AddPrintCell("",              0, 0, "l");
      Rep.AddPrintCell("",              0, 0, "l");
      Rep.AddPrintCell("вне биржи",     0, 0, "l");
      Rep.AddPrintCell(DealKindName,    0, 0, "c");
      Rep.AddPrintCell(ContrShortName,  0, 0, "l");
      Rep.AddPrintCell(ClientShortName, 0, 0, "l");
      Rep.AddPrintCell("",              0, 0, "l");/*№  поручения клиента*/
      Rep.AddPrintCell(SfContrNumber,   0, 0, "l");
      Rep.AddPrintCell(IssShortName,    0, 0, "l");
      Rep.AddPrintCell(AvrKind,         0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");/*Код ц/б - не заполняется*/
      Rep.AddPrintCell(AvrSeries,       0, 0, "c");/*серия № векселя*/
      Rep.AddPrintCell("",              0, 0, "c");/*Транш не заполняется*/
      Rep.AddPrintCell("",              0, 0, "c");/*ISIN не заполняется*/
      Rep.AddPrintCell(PayISO,          0, 0, "c");/*Валюта расчетов*/
      Rep.AddPrintCell("",              0, 0, "c");/*Кол-во не заполняется*/
      Rep.AddPrintCell("",              0, 0, "c");/*Цена не заполняется*/
      Rep.AddPrintCell("",              0, 0, "c");/*Валюта Цены не заполняется*/
      Rep.AddPrintCell(SumInNom,        0, 4, "c");/*Для УВ цена каждого векселя по сделке*/
      Rep.AddPrintCell("",              0, 0, "c");/*Для УВ  не выводится*/
      Rep.AddPrintCell(PayCCY,          0, 0, "c");/*валюта цены каждого векселя по сделке*/
      Rep.AddPrintCell(StateDate ,      0, 0, "l");
      Rep.AddPrintCell(StateFactDate,   0, 0, "l");
      Rep.AddPrintCell(PayDate,         0, 0, "l");
      Rep.AddPrintCell(PayFactDate,     0, 0, "l");
      Rep.AddPrintCell(ReportKind,      0, 0, "l");
      Rep.AddPrintCell(ReportNum,       0, 0, "l");
      Rep.AddPrintCell(ReportDate,      0, 0, "c");
      Rep.AddPrintCell("",              0, 0, "c");
   end;
 
   Rep.AddStr();
END;
```

---

## Пример 26: `BeginRepTab`

**Источник:** `Mac/DLNG/dlclordcj.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
  MACRO BeginRepTab()
    
     m_Report.PrintFormatString( "\n#\n",
                                "N1_A1" , m_Report.RepName());

     m_Report.CopyAllSheetInTotalBook( null, false, "N1_TableHeader", 1 );

     m_Report.RegisterTable( "N1_MainTable", TableHeader,
                             "N1_D2",
                             "N1_T1",
                             "N1_M1",
                             "N1_A2",
                             "N1_A3",  
                             "N1_A4",  
                             "N1_D3", 
                             "N1_A9", 
                             "N1_A5",
                             "N1_Fl",
                             "N1_N1",
                             "N1_S1",
                             "N1_S2",
                             "N1_A6",
                             "N1_A7");      
  END;
```

---

## Пример 27: `createReport`

**Источник:** `Mac/CELLS/chgrept_realt.mac`
**Тип:** `macro`
**Размер:** 29 строк

```rsl
macro createReport()  
  ObjPrint.AddDoc("Доп_соглашение_риэлтор",
    Номер_доп_согл,
    Номер_договора,
    Город, 
    Инфо_по_заведующей, 
    Наименование_клиента, 
    Поверенный,
    День_вып,Месяц_вып,Год_вып,
    День_дог,Месяц_дог,Год_дог,
    День_кон,Месяц_кон,Год_кон,
    День1_нач,Месяц1_нач,Год1_нач,
    День1_кон,Месяц1_кон,Год1_кон,
    Первая_группа(0).ФИО, Первая_группа(0).Паспорт, Первая_группа(0).Выдан,
    Первая_группа(1).ФИО, Первая_группа(1).Паспорт, Первая_группа(1).Выдан,
    Первая_группа(2).ФИО, Первая_группа(2).Паспорт, Первая_группа(2).Выдан,
    Первая_группа(3).ФИО, Первая_группа(3).Паспорт, Первая_группа(3).Выдан,
    День2_нач,Месяц2_нач,Год2_нач,
    День2_кон,Месяц2_кон,Год2_кон,
    Вторая_группа(0).ФИО, Вторая_группа(0).Паспорт, Вторая_группа(0).Выдан,
    Вторая_группа(1).ФИО, Вторая_группа(1).Паспорт, Вторая_группа(1).Выдан,
    Вторая_группа(2).ФИО, Вторая_группа(2).Паспорт, Вторая_группа(2).Выдан,
    Вторая_группа(3).ФИО, Вторая_группа(3).Паспорт, Вторая_группа(3).Выдан,
    Почтовый_адрес_банка, {Bank_INN}, Счет_банка, {MFO_Bank}, {CORAC_Bank}, Телефоны_банка,
    Данные_клиента
  );

  ObjPrint.CreateTemplateData();
end;
```

---

## Пример 28: `Блок`

**Источник:** `Mac/DLNG/TRUST/tsdeals.mac`
**Тип:** `block`
**Размер:** 23 строк

```rsl
    CopyAllSheetInTotalBook( null, false, "N1_Head", 0 );
  END;
/*================================================================================================*/
  PRIVATE MACRO PrintLine(A1, A2, A3, A4)
     PrintTableLine( "N1_A1",     A1, null,
                     "N1_A2",     A2, null,
                     "N1_A3"+App, A3, null,
                     "N1_A4"+App, A4, null
                   );
  END;
/*================================================================================================*/
  PRIVATE MACRO IsEXCH(gr, BrokerID):bool
    if( IsEXCHANGE(gr) )
      return true;
    elif( IsOutEXCHANGE(gr) AND (BrokerID != -1) )
      if( ВидСубъекта(BrokerID, PTK_MARKETPLASE) == true )
        return true;
      end;
    end;
    return false;
  END;
/*================================================================================================*/
  PRIVATE MACRO ОпределитьПосредникаСделки( Deal )
```

---

## Пример 29: `PrintReport`

**Источник:** `Mac/Cb/sfrepacp.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro PrintReport( AllDprt, Dprt, Attr, Comiss, EndDate, TrnDate )
  PrintHeader();

  SfRep_PrintTop();

  PrintParm( Dprt, Attr, Comiss, EndDate, TrnDate );

  PrintContext( AllDprt, Dprt );
end;
```

---

## Пример 30: `BeginReport`

**Источник:** `Mac/DLNG/SECUR/incbncom.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
  MACRO BeginReport()
     m_Report.PrintHeader();
     m_Report.RegisterTable("N1_MainTable", TableHeader,
                            "N1_ID", "N1_SfContr", "N1_Contr", "N1_Kind", "N1_Period", "N1_Cur", "N1_Rur", 
                            "N1_Sum", "N1_SumCorr", "N1_Note"
                           );

     m_Report.SetCellAutoSumma( null, "N1_Cur", "N1_Rur","N1_Sum","N1_SumCorr" );
  END;
```

---

## Пример 31: `PrintHead0`

**Источник:** `Mac/DLNG/DV/opposrep.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro PrintHead0( BankClient:integer  )
   var SheetName = ПолучитьКодФилиала( RepData.Department );
   /*для каждого филиала своя вкладка*/
   if( BankClient == BankAcc )
      SheetName = SheetName + "_1";
   else
      SheetName = SheetName + "_2";
   end;

   if( RepData.FirstSheet )
      Rep.AddNewSheetBreak( SheetName, Table );
   else
      RepData.FirstSheet = SheetName;
   end;

   Rep.AddPrintCell("Филиал: " + ПолучитьКодФилиала( RepData.Department ), Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
   Rep.AddEmptyStr();
   Rep.AddPrintCell("Субрегистр внутреннего учета открытых позиций по фьючерсным контрактам и опционам", Rep.GetHeaderWidth(), 0, "c:" + FontStyleHead0, REP_ELEM_STR);
   Rep.AddStr();
   RepData.PrintDep = false;
end;
```

---

## Пример 32: `PrintHeader`

**Источник:** `Mac/Cb/overacc.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
MACRO PrintHeader(Дата)
[                                       Обработка счетов с овердрафтом
                                                за #

](Дата);
[┌─┬───────────────────────┬────────────────────────────────────────────────────┐];
[│О│      Номер счета      │ Результат                                          │];
[├─┼───────────────────────┼────────────────────────────────────────────────────┤];
END;
```

---

## Пример 33: `Блок`

**Источник:** `Mac/DLNG/TRUST/tsrealizreg_form.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
  PRIVATE MACRO Init()
     AddFieldProc( 0, PNFLD_TSREALIZREG_BEGDATE,          DL_PNFLD_BEGINDATE,        @DL_FldProc_BeginDate,   TsRealizRegData.BegDate ); 
     AddFieldProc( 0, PNFLD_TSREALIZREG_ENDDATE,          DL_PNFLD_ENDDATE,          @DL_FldProc_EndDate,     TsRealizRegData.EndDate );
     AddFieldProc( 0, PNFLD_TSREALIZREG_CLIENTCODE,       DL_PNFLD_CLIENT_NUM_OFBU,  @DL_FldProc_ClientNDFL,  TsRealizRegData.ClientCode );
     AddFieldProc( 0, PNFLD_TSREALIZREG_CLIENTNAME,       DL_PNFLD_CLIENT_NAME_OFBU, @Default,                TsRealizRegData.ClientName );
     AddFieldProc( 0, PNFLD_TSREALIZREG_CLIENTCONTR,      DL_PNFLD_CONTRACT_OFBU,    @DL_FldProc_ContractIDDU,TsRealizRegData.ClientContr ); 
     AddFieldProc( 0, PNFLD_TSREALIZREG_ORCB,             DL_PNFLD_CHECKBOX,         @DLUSR_FldProc_ORCB,     TsRealizRegData.ORCB );
     AddFieldProc( 0, PNFLD_TSREALIZREG_ORCB_EMISS,       H_ORCB_EMISS,              @DL_FldProc_CheckBox,    TsRealizRegData.ORCB_Emiss );
     AddFieldProc( 0, PNFLD_TSREALIZREG_ORCB_DERIV,       H_ORCB_DERIV,              @DL_FldProc_CheckBox,    TsRealizRegData.ORCB_Deriv );
     AddFieldProc( 0, PNFLD_TSREALIZREG_NO_ORCB,          DL_PNFLD_CHECKBOX,         @DLUSR_FldProc_NO_ORCB,  TsRealizRegData.NO_ORCB );
     AddFieldProc( 0, PNFLD_TSREALIZREG_NO_ORCB_EMISS,    H_NO_ORCB_EMISS,           @DL_FldProc_CheckBox,    TsRealizRegData.NO_ORCB_Emiss );
     AddFieldProc( 0, PNFLD_TSREALIZREG_NO_ORCB_NO_EMISS, H_NO_ORCB_NO_EMISS,        @DL_FldProc_CheckBox,    TsRealizRegData.NO_ORCB_NO_Emiss ); 
     AddFieldProc( 0, PNFLD_TSREALIZREG_ISEXCEL,          DL_PNFLD_CHECKBOX,         @DL_FldProc_CheckBox,    TsRealizRegData.IsExcel );
  END;
```

---

## Пример 34: `BeginRepTab`

**Источник:** `Mac/DLNG/TRUST/tsmtgain.mac`
**Тип:** `macro`
**Размер:** 23 строк

```rsl
  MACRO BeginRepTab()
    
     m_Report.PrintFormatString( ClientHeader,
                                "N1_K0", m_Report.ClientName(),
                                "N1_K1", m_Report.ClientContr(),
                                "N1_K2", m_Report.TaxRate()
                               );
     m_Report.CopyAllSheetInTotalBook( null, false, "N1_TableHeader", 1 );

     m_Report.RegisterTable( "N1_MainTable", TableHeader,
                             "N1_A1",       
                             "N1_A2",       
                             "N1_A3",         
                             "N1_A4",           
                             "N1_A5",           
                             "N1_A6",          
                             "N1_A7",          
                             "N1_A8",
                             "N1_A9",
                             "N1_A10",
                             "N1_A11",
                             "N1_A12");      
  END;
```

---

## Пример 35: `PrintCellTable`

**Источник:** `Mac/DLNG/DEPO/dprdistr.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
macro PrintCellTable( Str, S_Size, Big )
  if( (ValType(Big) != V_UNDEF) and Big )
    DP_AddPrintCell( DivRep, Str, S_Size, DataCrp.Point, "r:" + FontStyleTitel );
  else
    DP_AddPrintCell( DivRep, Str, S_Size, DataCrp.Point, "r:" + FontStyleTitel1 );
  end;
```

---

## Пример 36: `printFooter`

**Источник:** `Mac/DLNG/MMARK/mmrprorl.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
MACRO printFooter
if (not flagXLS)
[└──────────────────────┴───────────────────────────────┴───┴────────────────────┴──────────┴──────────┴──────┴──────────┴────────┼────────────────┼────────────────┼──┘];
[                                                                                                                           Итого │################│################│   ]
( g_req:r, g_com:r );
[                                                                                                                                 └────────────────┴────────────────┘   ];
[  ];
[  ];
else
	Rep.SetValue_NameCell("T_B1", g_req );  
	Rep.SetValue_NameCell("T_B2", g_com );  
end;
```

---

## Пример 37: `PrintCellTable`

**Источник:** `Mac/DLNG/DEPO/dpnotdiv.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
macro PrintCellTable( Str ,t_point, Right )
  if( ( ValType( Right ) != V_UNDEF ) and Right )
    DP_AddPrintCell( DivRep, Str, 0, t_point, "r:" + FontStyleTitel );
  else
    DP_AddPrintCell( DivRep, Str, 0, t_point, "l:" + FontStyleTitel );
  end;
```

---

## Пример 38: `PrintHead0`

**Источник:** `Mac/DLNG/TRUST/tsopposrep.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro PrintHead0( BankClient:integer  )
   var SheetName = ПолучитьКодФилиала( RepData.Department );
   /*для каждого филиала своя вкладка*/
   if( BankClient == BankAcc )
      SheetName = SheetName + "_1";
   else
      SheetName = SheetName + "_2";
   end;

   if( RepData.FirstSheet )
      Rep.AddNewSheetBreak( SheetName, Table );
   else
      RepData.FirstSheet = SheetName;
   end;

   Rep.AddPrintCell("Филиал: " + ПолучитьКодФилиала( RepData.Department ), Rep.GetHeaderWidth(), 0, "l:" + FontStyleTitel, REP_ELEM_STR);
   Rep.AddEmptyStr();
   Rep.AddPrintCell("Субрегистр внутреннего учета открытых позиций по фьючерсным контрактам и опционам", Rep.GetHeaderWidth(), 0, "c:" + FontStyleHead0, REP_ELEM_STR);
   Rep.AddStr();
   RepData.PrintDep = false;
end;
```

---

## Пример 39: `printOneAvoirissection`

**Источник:** `Mac/DLNG/DEPO/dpregown.mac`
**Тип:** `macro`
**Размер:** 50 строк

```rsl
macro printOneAvoirissection( FIIDfrom, Elem : Owners, condition_date )
   var FIID, lsin, avoiriss, issue, code_currency, FaceValue, Quantity:double = 0.0, BurdenedQuantity:double = 0.0;
   var point = AVOIRISS_SUM_PRECISION;
   record fins("fininstr");

   if ( Elem != null )
     FIID = abs(Elem.FIID);
     Quantity = double(Elem.Quantity);
     BurdenedQuantity = double(Elem.BurdenedQuantity);
   else
     FIID = FIIDfrom;
   end;

   lsin = GetFICode( FIID, null, FICK_LSIN );
   avoiriss = getAVOIRISS( FIID );
   issue = getIssue( FIID );

   if ( not ПолучитьФинИн( FIID, fins ) )
     code_currency = GetFICode( fins.FaceValueFI, null, FICK_ISOSTRING );
     point = fins.SumPrecision;

     if(OwnerMaxPoint < point)
       OwnerMaxPoint = point;
     end;
   else
     code_currency = "";
   end;

   FaceValue = GetFaceValue(FIID, condition_date);

   if ( Elem != null )
     DP_AddPrintCell( Rep,  lsin, 15, 0, "l:" + RepFontStyleTitel + "ex_B(l)", is_ap, REP_ELEM_STR );
   else
     DP_AddPrintCell( Rep,  lsin, 15, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   end;
   DP_AddPrintCell( Rep,  " ", 1, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  avoiriss, 20, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  " ", 1, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  issue, 5, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  "  ", 2, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  FaceValue, 19, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  " ", 1, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   DP_AddPrintCell( Rep,  code_currency, 3, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
   if ( Elem != null )
     DP_AddPrintCell( Rep,  " ", GetLenTotal()-(15+1+20+1+5+2+19+1+3)+1, 0, "l:" + RepFontStyleTitel, is_ap, REP_ELEM_STR );
     DP_AddPrintCell( Rep,  Quantity, 17, DP_GetPrecision(Quantity, point), "r:" + RepFontStyleTitel + "ex_B(rl)", is_ap, REP_ELEM_STR );
     DP_AddPrintCell( Rep,  BurdenedQuantity, 19, DP_GetPrecision(BurdenedQuantity, point), "r:" + RepFontStyleTitel + "ex_B(rl)", is_ap, REP_ELEM_STR );
   end;
   Rep.AddStr();
end;
```

---

## Пример 40: `ПечатьКупонов`

**Источник:** `Mac/DLNG/DEPO/dpavrfrm.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro ПечатьКупонов( НаборКупонов )
    var i = 0;
    Rep.AddEmptyStr();
    while( i < НаборКупонов.Size )
      if ( НаборКупонов[i].percent != 0 )
        DP_AddPrintCell( Rep,  НаборКупонов[i].real_num, 0, 0, "l:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  НаборКупонов[i].p_date, 0, 0, "l:f:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  string(НаборКупонов[i].percent)+"%", 0, 0, "l:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  EMPTY_STR, 0, 0, "l:" + RepFontStyleTitel );
        Rep.AddStr();
      else
        DP_AddPrintCell( Rep,  НаборКупонов[i].real_num, 0, 0, "l:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  НаборКупонов[i].p_date, 0, 0, "l:f:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  EMPTY_STR, 0, 0, "l:" + RepFontStyleTitel );
        DP_AddPrintCell( Rep,  НаборКупонов[i].value, 0, 0, "l:" + RepFontStyleTitel );
        Rep.AddStr();
      end;
      i = i + 1;
    end;

end;
```

---
