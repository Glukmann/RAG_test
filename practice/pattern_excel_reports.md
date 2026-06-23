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

