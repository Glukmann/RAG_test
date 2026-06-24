# Практика: Объектно-ориентированное программирование (Class, Object, this, свойства, методы)

**Теория:** [BnRSL.md## Объектные типы]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `FindCh_Type`

**Источник:** `Mac/DEPOSITR/r_rest.mac`  
**Тип:** `macro`  
**Размер:** 37 строк

```rsl
Macro FindCh_Type(  Тип_Остатка, Счет_Был_Востр , Вид_Вклада )

  var Rest          = $0,
      StatFind      = False,
      Object        = 2001,
      WasNotPension = False,
      DelReferenc   = "";

    /*
       Ищем зачисление %  за 31.12.98.
       Если в основании упоминается вклад До востр, то остаток должен
       учитываться в сумме остатков по До востр, даже если вклад был
       изначально Пенсионным ( Это огрехи кривой базы )
    */

    /*ClearRecord( sbdepdoc     );
    KeyNum     ( sbdepdoc , 1 );
    Rewind     ( sbdepdoc     );

    sbdepdoc.Referenc         = depositr.Referenc  ;
    sbdepdoc.TypeOper         = Зачисление_Процентов;
    sbdepdoc.DepDate_Document = Date( 31, 12, 1998 );

    StatFind = GetGE( sbdepdoc );
    While( StatFind AND ( sbdepdoc.Referenc         == depositr.Referenc         ) AND
                        ( sbdepdoc.TypeOper         == Зачисление_Процентов ) AND
                        ( sbdepdoc.DepDate_Document == Date( 31, 12, 1998 ) )    )

       If(DocFilter())
         /* Ищем и сравниваем вид вклада в основание документа зачисления % */
         if( Index( Sbdepdoc.Ground, "по данным формы 19" ) AND
             Index( Sbdepdoc.Ground, "ДО ВОСТРЕБ."        )     )

             /* Нашли - счет, который на 01.01. был до востребования */
             WasNotPension = True;
             StatFind      = False;
         end;
```

---

## Пример 2: `GenObj`

**Источник:** `Mac/Mbr/ufgo241.mac`  
**Тип:** `macro`  
**Размер:** 20 строк

```rsl
macro GenObj( addrMes, mode )
  
  var ListNotFoundMes : string = "";
  var ListChoiseMesNotFound = TArray; // набор записей dwlmesval_dbt выбранные в скролинге ненайденных
  var ListReferInsert = TArray;       // список рефернсов вставленных ответов
  var oneMes : bool = true;
  var errorTranz : bool = false;
  var refer;
  var msg = "";
  var protokolName = "";
  var rs : object;
  
  record wlmes( wlmes );
  SetBuff( wlmes, addrMes );
  
  FILE wlreq( wlreq );
  
  if(mode == WLD_GENOBJ_ACTION_ROLLBACK)
    return true;
  end;
```

---

## Пример 3: `rqvpfr_rq`

**Источник:** `Mac/Cb/rqvpfr_go.mac`  
**Тип:** `private macro`  
**Размер:** 22 строк

```rsl
private macro rqvpfr_rq(PartyID, answer:@object)
   var stat=0;
   var mes_not_enough_data=rqvpfr_mes[11];

   var request=CRqVPFR_RQ();

   // начало заполнения request
   var is_not_enough_data=false;
   stat =              get_persn(   PartyID, @request,         @mes_not_enough_data, @is_not_enough_data);
   if(stat!=1)  stat = get_SNILS(   PartyID, @request.SNILS,   @mes_not_enough_data, @is_not_enough_data); end;  // String  СНИЛС (со знаками). \d{3}-\d{3}-\d{3} \d{2}
   if(stat!=1)  stat = GetPassport( PartyID, @request.Passport,@mes_not_enough_data, @is_not_enough_data); end;
   if(stat!=1)  stat = GetTelephon( PartyID, @request.Phone,   @mes_not_enough_data, @is_not_enough_data); end;      // String  Номер телефона клиента \d{10}
   if(is_not_enough_data==true) stat=2; end;

   if(stat==0)      
      request.ReqID         = SubStr(CreateGUID(), 2, 36);     // GUID    Уникальный идентификатор запроса
      request.SenderID      = RSC_SENDERID;                    // String  Идентификатор (код) Абонента, от кого получен Запрос
      request.ReqType       = 1;                               // Integer 1 = Синхронный 0 = Асинхронный
      request.DocID         = SubStr(CreateGUID(), 2, 36);     // GUID    ИД Заявки
      request.ClientID      = PartyID;                                // String  ИД клиента в АС Банка
      request.TimeZona      = GetTimeZona_day()*24;                      // Integer Глубина актуальности сведений в часах
   end;
```

---

## Пример 4: `PrintForm`

**Источник:** `Mac/Mbr/ufpr807.mac`  
**Тип:** `macro`  
**Размер:** 22 строк

```rsl
macro PrintForm( addrMes, MassCopy )

  Bnk_ToRSTrace( "PrintForm807", "Begin", "" );

  var stat = false;
  var FileDirectory = Bnk_GetTxtFileDir();
  var XmlObj : object = ActiveX("Microsoft.XMLDOM");   

  SetBuff( wlmes, addrMes );
  
  FILE MsgTmpFile() txt;
  var MsgTmpFileName, OldName;
  
  // Перенаправляем вывод сообщения в файл, чтобы при многократной печати использовать данные
  //------------------------------------------ 
  MsgTmpFileName = GetTxtFileName("tmpmsprn");
  OldName = SetOutPut( MsgTmpFileName );

  if( not open(MsgTmpFile, MsgTmpFileName) )
    std.msg( String("Файл не открыт:", "|", MsgTmpFileName) );
    return FALSE;
  end;
```

---

## Пример 5: `PrintForm`

**Источник:** `Mac/Mbr/ufpr802.mac`  
**Тип:** `macro`  
**Размер:** 19 строк

```rsl
macro PrintForm( addrMes, MassCopy )
  var stat = false;
  var FileDirectory = Bnk_GetTxtFileDir();
  var XmlObj : object = ActiveX("Microsoft.XMLDOM");

  SetBuff( wlmes, addrMes );
  
  FILE MsgTmpFile() txt;
  var MsgTmpFileName, OldName;
  
  // Перенаправляем вывод сообщения в файл, чтобы при многократной печати использовать данные
  //------------------------------------------ 
  MsgTmpFileName = GetTxtFileName("tmpmsprn");
  OldName = SetOutPut( MsgTmpFileName );

  if( not open(MsgTmpFile, MsgTmpFileName) )
    std.msg( String("Файл не открыт:", "|", MsgTmpFileName) );
    return FALSE;
  end;
```

---

## Пример 6: `PrintForm`

**Источник:** `Mac/Mbr/ufpr805.mac`  
**Тип:** `macro`  
**Размер:** 20 строк

```rsl
macro PrintForm( addrMes, MassCopy )
debugbreak;
  var stat = false;
  var FileDirectory = Bnk_GetTxtFileDir();
  var XmlObj : object = ActiveX("Microsoft.XMLDOM");   

  SetBuff( wlmes, addrMes );
  
  FILE MsgTmpFile() txt;
  var MsgTmpFileName, OldName;
  
  // Перенаправляем вывод сообщения в файл, чтобы при многократной печати использовать данные
  //------------------------------------------ 
  MsgTmpFileName = GetTxtFileName("tmpmsprn");
  OldName = SetOutPut( MsgTmpFileName );

  if( not open(MsgTmpFile, MsgTmpFileName) )
    std.msg( String("Файл не открыт:", "|", MsgTmpFileName) );
    return FALSE;
  end;
```

---

## Пример 7: `GenDoc_v2021_3_0`

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

## Пример 8: `PrintDocument`

**Источник:** `Mac/Cb/cbpracnt.mac`  
**Тип:** `macro`  
**Размер:** 16 строк

```rsl
MACRO PrintDocument(ncopy:integer):bool
  
  debugbreak;
  var payer:string, receiver:string, ground:string;
  var amount:money = 0, amountNDS:money = 0;
  var contr:string = "Договор обслуживания не найден";
  var select:string;
  var params:TArray;
  var rs:object;
  ARRAY SG, SP, SR, SC;

  /* Плательщик */
  payer = pr_pmrmprop.rec.PayerName;
  if( pr_pmrmprop.rec.PayerINN != "" )
    payer =  payer + " ИНН " + pr_pmrmprop.rec.PayerINN;
  end;
```

---

## Пример 9: `UpdateSfContr`

**Источник:** `Mac/Cb/updsfcontr.mac`  
**Тип:** `macro`  
**Размер:** 17 строк

```rsl
macro UpdateSfContr(SfContr, OldSfContr)
  var err = 0;
  var ErrMsg = "";
  record SfContrB( "sfcontr.dbt" );
  record SfContrO( "sfcontr.dbt" );
  SetBuff( SfContrB, SfContr );
  SetBuff( SfContrO, OldSfContr );
  var ZeroDate = date(0,0,0);
  var preacc = null;

 
  if(PrdClient.ProductID != OldPrdClient.ProductID)
    // При смене банковского продукта нужно создать новые объекты БП.
    if(SfContrB.ServKind == PTSK_DEPOS)
      err = ExecMacroFile("dpproduct.mac", "AddDepoAcntObjPRDbyCode", PrdClient.ClientProductID, SfContrB.Object);
      return err;
    end;
```

---

## Пример 10: `PrepareForExportED501`

**Источник:** `Mac/Mbr/uf501.mac`  
**Тип:** `macro`  
**Размер:** 16 строк

```rsl
macro PrepareForExportED501(nodeED501 : object, wlmes, retESSize501: @integer)
  var sInfoID : string = GetStrInfoID(wlmes.MesID);

  // ProprietoryDocument
  var DocumentImageID : integer = 0;
  var rs : RsdRecordset = GetAttObjRs(OBJTYPE_INFO, sInfoID, WLD_INFO_IMGTYPE_DOCUMENT);
  if(rs and rs.moveNext())
    DocumentImageID = rs.value("t_ImageID");
    var Doc : string = "";
    
    if( EncodeAttObjToBase64(DocumentImageID, Doc) )
      var ProprietoryDocumentNode : object = GetChildNode(nodeED501, "ProprietoryDocument");
      ProprietoryDocumentNode.Text = Doc;
    else
      RunError("Ошибка при кодировании данных из прикрепленного объекта");
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

## Пример 12: `CalcServiceSum`

**Источник:** `Mac/DLNG/DEPO/dpszach.mac`  
**Тип:** `macro`  
**Размер:** 40 строк

```rsl
macro CalcServiceSum( sfcontr_addr, BeginDate, EndDate )
    var stat;
    var Sum, BnAccount = "";

    record  rContr( sfcontr );
    record  rBaseSum( "sfbassum.str" );
    file depoacnt(depoacnt) key 1;
    SetBuff( rContr, sfcontr_addr );

    /*Перебираем все поручение на междепозитарный перевод -- зачисление*/
    pmpaym.DocKind     = SP_DEPOPER_ENROLMENT;
    pmpaym.ValueDate   = BeginDate;
    pmpaym.Purpose     = PurpBase;
    pmpaym.SubPurpose  = 0;
    stat = GetGE(pmpaym);
    while(  stat and
           (pmpaym.DocKind   == SP_DEPOPER_ENROLMENT) and
           (pmpaym.ValueDate <= EndDate)
         )
       if(pmpaym.PaymStatus == PM_FINISHED)
          BnAccount = GetHeadAccForAcc(pmpaym.ReceiverDpNode);
          if( (pmpaym.Purpose == PurpBase) and 
              (BnAccount == rContr.Object ) /*счет клиента на который зачислены бумаги*/
            )
             Sum = PaymNominal(pmpaym);

             ClearRecord( rBaseSum );
             rBaseSum.baseType    = SF_BASETYPE_SUM;
             rBaseSum.baseType2   = SF_BASETYPE_SUM;
             rBaseSum.baseSum     = Sum;
             rBaseSum.baseSum2    = Sum;

             rBaseSum.BaseObjectType = OBJTYPE_OPERATIONDEPO;
             rBaseSum.BaseObjectID   = GetSpdraftByPayment(pmpaym.PaymentID);

             if( InsertSumList(rBaseSum) )
                stat = FALSE;
                MacroError = 1;
                MsgBox("Ошибка при вставке базовой суммы");
             end;
```

---

## Пример 13: `PrintTableElementsFromXML`

**Источник:** `Mac/Mbr/ufpr807.mac`  
**Тип:** `private macro`  
**Размер:** 19 строк

```rsl
private macro PrintTableElementsFromXML( XmlObj )
  var isXmlExists = false;

  var i : integer = 0;
  var child : object = null;
  var stat : bool = false;
  var ED807Node : object = null;


  if( valtype(XmlObj) != V_UNDEF )
    i = 0;
    child = null;
    stat = false;
    while( i < XmlObj.childNodes.length )
      child = XmlObj.childNodes.item(i);
      if( child and (child.nodeType == CHILD_NODE) and (GetNodeName( child.NodeName ) == "ED807") )    
        isXmlExists = true;
        ED807Node = child;
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

## Пример 15: `CalcServiceSum`

**Источник:** `Mac/DLNG/DEPO/dpsmezh.mac`  
**Тип:** `macro`  
**Размер:** 40 строк

```rsl
macro CalcServiceSum( sfcontr_addr, BeginDate, EndDate )
    var stat;
    var Sum, DwAccount = "";

    record  rContr( sfcontr );
    record  rBaseSum( "sfbassum.str" );
    file depoacnt(depoacnt) key 1;
    SetBuff( rContr, sfcontr_addr );

    /*Перебираем все поручение на междепозитарный перевод -- списание*/
    pmpaym.DocKind     = SP_DEPOPER_TRANSFERORDER;
    pmpaym.ValueDate   = BeginDate;
    pmpaym.Purpose     = PurpBase;
    pmpaym.SubPurpose  = 0;
    stat = GetGE(pmpaym);
    while(  stat and
           (pmpaym.DocKind   == SP_DEPOPER_TRANSFERORDER) and
           (pmpaym.ValueDate <= EndDate)
         )
       if(pmpaym.PaymStatus == PM_FINISHED)
          DwAccount = GetHeadAccForAcc(pmpaym.PayerDpNode);
          if( (pmpaym.Purpose == PurpBase) and
              (DwAccount == rContr.Object ) /*счет клиента c которого списаны бумаги*/
            )
             Sum = PaymNominal(pmpaym);

             ClearRecord( rBaseSum );
             rBaseSum.baseType    = SF_BASETYPE_SUM;
             rBaseSum.baseType2   = SF_BASETYPE_SUM;
             rBaseSum.baseSum     = Sum;
             rBaseSum.baseSum2    = Sum;

             rBaseSum.BaseObjectType = OBJTYPE_OPERATIONDEPO;
             rBaseSum.BaseObjectID   = GetSpdraftByPayment(pmpaym.PaymentID);

             if( InsertSumList(rBaseSum) )
                stat = FALSE;
                MacroError = 1;
                MsgBox("Ошибка при вставке базовой суммы");
             end;
```

---

## Пример 16: `OperType`

**Источник:** `Mac/DLNG/dlclordcj.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
  MACRO OperType():STRING
    if( (this.Status() == "Исполнено") or (this.Status() == "Частично исполнено") )
       return Data.ReportData[m_StrNum].OperType;
    else
       return "";
    end;
  END;
```

---

## Пример 17: `RegisterReportTableWithHead`

**Источник:** `Mac/DLNG/SECUR/ReportMoveBasketREPO_Report.mac`
**Тип:** `macro`
**Размер:** 30 строк

```rsl
  MACRO RegisterReportTableWithHead()

    SetActiveSheet("Движение цб в РЕПО с корзиной");
    PrintFormatString( "",               
                       "Today", string(Date() + " " + string( Time() ) ),
                       "Num_Oper", string({oper}),
                       "Oper", this.Операционист(),    
                       "H0_1", this.H0_1(),  
                       "H0_2", this.H0_2(), 
                       "H0_5", this.GetAvrName() );
    
    RegisterTable(  "MainTable", "",
                    "SecType",
                    "N",
                    "SecName",
                    "CodeR",
                    "TypeRepoShort",
                    "DZ",
                    "N_DD1",
                    "N_DD2",
                    "QntyOnDate", 
                    "Tot1vp",
                    "Tot2vp",
                    "Rate", 
                    "VP", 
                    "Cont",
                    "CodeR_1",
                    "ISIN"
                  );   
  END;
```

---

## Пример 18: `Блок`

**Источник:** `Mac/DLNG/VA/vatickfd.mac`
**Тип:** `block`
**Размер:** 108 строк

```rsl
        if(ParmKind == MC_TYPE_PARAMETR_CENTR)
           return  GetPartyID({oper});  /* PartyID текущего оператора */
        elif(ParmKind == MC_TYPE_PARAMETR_FIID) /* ФИ сделки */
           if(FIRole == FIROLE_FIREQ) /* требования */
              if(IsBuy())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, BAi, payms))
                    return payms.rec.PayFIID;
                 end;
              elif((IsSale()) OR (IsBarter()))
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.PayFIID;
                 end;
              elif(tick.rec.BofficeKind == DL_VAREPAY)
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, PM_PURP_PRINC_RET, payms))
                    return payms.rec.PayFIID;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_FICOM) /* обязательства */
              if((IsSale()) OR (IsBarter()))
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, BAi, payms))
                    return payms.rec.PayFIID;
                 end;
              elif(IsBuy())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.PayFIID;
                 end;
              elif(tick.rec.BofficeKind == DL_VAREPAY)
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, PM_PURP_PRINC_RET, payms))
                    return payms.rec.PayFIID;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_FIBARTERDIFF) /* доплата в мене */
              if(IsBarter())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, PM_PURP_VSBARTERDIFF, payms))
                    return payms.rec.PayFIID;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_OVERVALUE_REQ) /* переоценка требований */
              if(IsBuy())
                 return NATCUR;
              elif(IsBarter())
                 return Get_II_Currency(VSORDLNK_K_BUY);
              elif(IsSale())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.PayFIID;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_OVERVALUE_COM) /* переоценка обязательств */
              if(IsSale())
                 return NATCUR;
              elif(IsBarter())
                 return Get_II_Currency(VSORDLNK_K_SALE);
              elif(IsBuy())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.PayFIID;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_OVERVALUE_DIFF) /* переоценка доплаты в мене */
              if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, PM_PURP_VSBARTERDIFF, payms))
                 return payms.rec.PayFIID;
              end;
              return -1;
           elif(FIRole == FIROLE_DEALS_TERMREQ)  /*Требования по срочным сделкам*/
              return NATCUR;
           elif(FIRole == FIROLE_DEALS_OVERDUE)  /*Просроченные требования по сделкам*/
              return NATCUR;
           elif( (FIRole == FIROLE_CORACC_ACTIVE) or (FIRole == FIROLE_CORACC_PASSIVE) )
              return this.GetFIIDForCorAccNum();
           end;
        elif(ParmKind == MC_TYPE_PARAMETR_BEGDATE) /* дата начала сделки */
           return tick.rec.DealDate;
        elif(ParmKind == MC_TYPE_PARAMETR_FINDATE) /* базовая дата сделки */
           if((FIRole == FIROLE_FIREQ) OR (FIRole == FIROLE_OVERVALUE_REQ)) /* требования */
              if(IsBuy())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, BAi, payms))
                    return payms.rec.ValueDate;
                 end;
              elif(IsSale() OR IsBarter())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.ValueDate;
                 end;
              end;
              return -1;
           elif((FIRole == FIROLE_FICOM) OR (FIRole == FIROLE_OVERVALUE_COM)) /* обязательства */
              if(IsBuy())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, CAi, payms))
                    return payms.rec.ValueDate;
                 end;
              elif(IsSale() OR IsBarter())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, BAi, payms))
                    return payms.rec.ValueDate;
                 end;
              end;
              return -1;
           elif(FIRole == FIROLE_FIBARTERDIFF) /* доплата в мене */
              if(IsBarter())
                 if(VA_Get1stPlanPaym(tick.rec.BofficeKind, tick.rec.DealID, PM_PURP_VSBARTERDIFF, payms))
                    return payms.rec.ValueDate;
                 end;
              end;
              return -1;
           end;
        end;
```

---

## Пример 19: `ПоляИсходныхСообщений`

**Источник:** `Mac/Cb/swsbsign.mac`
**Тип:** `macro`
**Размер:** 18 строк

```rsl
macro ПоляИсходныхСообщений( )
  /* Очищаем массив */
  ПоляБлокаДанных = Tarray;
  GenObject( "ТПолеБлока", "20",false, false, "", "" );
  if( substr(type_link_mes, 1, 3) == "102")
    GenObject( "ТПолеБлока", "23", false, false, "", "" );
    GenObject( "ТПолеБлока", "21", false, false, "Sequence B", "" );
    GenObject( "ТПолеБлока", "32B", false, false, "Sequence B", "Rules1" );
    if(type_link_mes == "102I")
       GenObject( "ТПолеБлока", "50", true, false, "Sequence B\\50a", "" );
    end;
    GenObject( "ТПолеБлока", "59", true, false, "Sequence B\\59a", "" );
    GenObject( "ТПолеБлока", "71A", false, false, "Sequence B", "" );
    GenObject( "ТПолеБлока", "32A", false, false, "", "Rules1" );
    GenObject( "ТПолеБлока", "19", false, false, "", "Rules1" );
    GenObject( "ТПолеБлока", "53", true, false, "53a", "" );
    GenObject( "ТПолеБлока", "54A", false, false, "", "" );
  end;
```

---

## Пример 20: `Блок`

**Источник:** `Mac/DLNG/SECUR/IncaccpsReg.mac`
**Тип:** `block`
**Размер:** 15 строк

```rsl
  PRIVATE MACRO ExecuteReport( ObjReport:OBJECT )
    ReportRun( this,
               Department,
               Period,
               Year,
               false,
               -1,
               true,
               CirculateInMarket,
               NotCirculateInMarket,
               NominateInRUR,
               NotNominateInRUR,
               AvrID,
               IsBackRepo );
  END;
```

---

## Пример 21: `Блок`

**Источник:** `Mac/CELLS/rent_incrept.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
private class OrderParams
 var Branch = 0;
 var NameBranch = "";
 var CellNumber = 0;
 var ContractNumber = 0;
 var ContrCreateDate = date(0,0,0);
 var TotalSum = $0;
 var TotalSumCur = 0;
 var CurrRevenue = $0;
 var CurrRevenueCur = 0;
 var FutureRevenue = $0;
 var FutureRevenueCur = 0;
 var PayGrRecs = null;
end;
```

---

## Пример 22: `GenDoc`

**Источник:** `Mac/Mbr/nbrkgdc52.mac`
**Тип:** `macro`
**Размер:** 21 строк

```rsl
macro GenDoc( addrMes )
  var rootNode : object = null,
      grpNode : object = null;
  SetBuff( wlmes, addrMes );

  rootNode = NBRK_GetMesDocumentNode(wlmes.MesID);
  rootNode = GetChildNode(rootNode, "BkToCstmrAcctRpt");
  grpNode = GetChildNode( rootNode, "GrpHdr" );

  record wlhead(wlhead);
  var RptNodeArr : TArray = GetChildNodeArr( rootNode, "Rpt" );

  for(var RptNode : object, RptNodeArr)
    ClearRecord(wlhead);
    ReadWlheadFromRpt(wlhead, RptNode, wlmes);

    var NtryNodeArr : TArray = GetChildNodeArr( RptNode, "Ntry" );
    for(var NtryNode : object, NtryNodeArr)
      GenDocReportEntry(wlmes, RptNode, NtryNode, null, TSpecFillConf(wlhead));
    end;
  end;
```

---

## Пример 23: `Блок`

**Источник:** `Mac/Jr/JrFieldInfo.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
class TJrFieldInfo(field : Object)
    const RSD_TYPE_SHORT = 32;
    const RSD_TYPE_LONG = 64;
    const RSD_TYPE_FLOAT = 128;
    const RSD_TYPE_DOUBLE = 256;
    const RSD_TYPE_STRING = 512;
    const RSD_TYPE_DECIMAL = 2048;
    const RSD_TYPE_DATE = 16384;
    const RSD_TYPE_TIME = 32768;
    const RSD_TYPE_TIMESTAMP = 65536;
    const RSD_TYPE_CHAR = 4194304;
    const RSD_TYPE_UNSIGNED_SHORT = 8388608;
    const RSD_TYPE_UNSIGNED_LONG = 16777216;
    const RSD_TYPE_NUMERIC = 33554432;
```

---

## Пример 24: `eventHandler`

**Источник:** `Mac/DLNG/UniLoader/ul_dataKind_i.mac`
**Тип:** `macro`
**Размер:** 19 строк

```rsl
  MACRO eventHandler(EV)
      if (EV.keyCode == ULK_F9)
          if ((this.CheckChanges())and(SaveChanges()))
              close(-EV.keyCode);
          end;
      elif (EV.keyCode == ULK_ESC)
          if (this.CheckChanges())
              var isSave = MsgBoxEx("Сохранить изменения?", MB_YES + MB_NO + MB_CANCEL, IND_YES);
              if (isSave == IND_YES)
                  EV.keyCode = ULK_F9;
                  this.eventHandler(EV);
              elif (isSave == IND_NO)
                  close(-EV.keyCode);
              else
                  EV.keyCode = 0;
              end;
          end;
      end;
  END;
```

---

## Пример 25: `Construct`

**Источник:** `Mac/DLNG/TRUST/trvafd.mac`
**Тип:** `macro`
**Размер:** 20 строк

```rsl
  MACRO Construct( parm1, parm2, parm3, parm4 )
    initVSBannerFD(parm1, parm2, parm3, parm4);

    if((ValType(parm3) == V_INTEGER) and (ValType(parm4) != V_UNDEF) )
      if(copy(tick, parm4))
        isTick = true;
      end;
    end;
    
    if((isTick) and (tick.rec.ClientContrID))
      if(CB_GetTSContrBySfContr( tick.rec.ClientContrID, v_Order ))
        ctgfd =  TS_OrderFD(0,v_Order.rec.ID);
      end;
    elif(this.GetBnr().rec.ContrID)
      if(CB_GetTSContrBySfContr( this.GetBnr().rec.ContrID, v_Order ))
        ctgfd =  TS_OrderFD(0,v_Order.rec.ID);
      end;
    end;

  END;
```

---

## Пример 26: `Блок`

**Источник:** `Mac/DLNG/TRUST/tsportfrep.mac`
**Тип:** `block`
**Размер:** 26 строк

```rsl
     this.RegisterTable( "N_MainTable  ", TableHeader,
               /*1  */   "N_Issuer     ",
               /*2  */   "N_AvrCode    ",
               /*3  */   "N_AvrRegNum  ",
               /*4  */   "N_AvrNomCCY  ",
               /*5  */   "N_Date       ",
               /*6  */   "N_Time       ",
               /*7  */   "N_Amount     ",
               /*8  */   "N_Portf      ",
               /*9  */   "N_BuyPrice   ",
               /*10 */   "N_BuyCost    ",
               /*12 */   "N_MarketPrice",
               /*13 */   "N_MarketCost ",
               /*15 */   "N_BalPrice   ",
               /*16 */   "N_BalCost    ",
               /*18 */   "N_OvervalSum ",
               /*18 */   "N_OvervalSumPeriod ",
               /*20 */   "N_NKDSale    ",
               /*21 */   "N_NKDPartial ",
                         "N_RetNKD     ",
               /*22 */   "N_NKDDate    ",
                         "N_NKDCalc    ",
               /*24 */   "N_NKD2Partial",
                         "N_RetNKD2    ",
               /*25 */   "N_NKD2Date   ",
                         "N_NKD2Period " );
```

---

## Пример 27: `Constructor`

**Источник:** `Mac/CONV_FC/testrest.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro Constructor()
   var stat = true;

   Protocol = clProtocol( ProtocolPath );
   Protocol.Header();

   return stat;
end;
```

---

## Пример 28: `Блок`

**Источник:** `Mac/DLNG/dl_class.mac`
**Тип:** `block`
**Размер:** 12 строк

```rsl
       if( Parametr == -1 )
          /*Бэк-офис*/
          if(dl_acc.rec.OperType == 36)
            if( FIRole == FIROLE_SRCA )
              Parametr = this.GetParmByServKind(SfContr_from.rec.ServKind);
            elif( FIRole == FIROLE_DSTA )
              Parametr = this.GetParmByServKind(SfContr_to.rec.ServKind);
            end;
          else
            Parametr = GetParametrTemplate(ObjectID, Classificator, OperDate, FIRole);
          end;
       end;
```

---

## Пример 29: `SfFormClientOrderExt`

**Источник:** `Mac/Cb/sfpayord.mac`
**Тип:** `macro`
**Размер:** 10 строк

```rsl
macro SfFormClientOrderExt( sidebet, sicredit, sfcomiss, payParams:TSfPayParams, sfinvlnk, SumInInvFIID, 
                            IsBatchMode, oprchild )

  var Payment : RsbPayment;
  var ClnPaym : object; /*RsbPSPayOrder*/;

  var PmAmount = payParams.paySum;
  if( (SumInInvFIID != null) AND (sidebet.rec.FIID != payParams.payFIID) )
    PmAmount = SumInInvFIID;
  end;
```

---

## Пример 30: `start`

**Источник:** `Mac/DEPOSITR/rt_ib_makePostDocument.mac`
**Тип:** `macro`
**Размер:** 44 строк

```rsl
  macro start( inXml, outXml ) 

    var nodeParentElement;
    var stat = 0;

    outXML_cur = outXml;    
    if(not outXml_cur )
      outXml_cur = CreateXMLObject();
      if(not outXml_cur) return; end;

      nodeParentElement = inXml.documentElement.selectSingleNode( "//" + NameInputTag );
      CreateBeginTag( outXml_cur );
    
      if( nodeParentElement )
 
        getParameters( nodeParentElement );

        stat = ProcessTrn( 0, R2M ( this, "make") );
        
        if ( stat )
          createDateTag;
        end;
      end;

    end;//if(not outXml )

    return outXml_cur;
  end;//start( inXml, outXml ) 



end;// class(cBaseDeposit) cMakePostDocument( inXml, outXml ) 


// ───────────────────────────────────────
// Вставка отложенного документа
// ───────────────────────────────────────
macro makePayDocument( inXml, outXml ) 

  var t = cMakePostDocument;
  outXml = t.start( inXml, outXml );

  SetParm(1, outXml);
end;
```

---

## Пример 31: `SaleBCCostRUR`

**Источник:** `Mac/DLNG/VA/vadealfinres.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
  MACRO SaleBCCostRUR():MONEY
    if(m_RS.SaleBCCFI != NATCUR)
      return VA_Convert(m_RS.SaleBCCost, this.ValueDate(), m_RS.SaleBCCFI, NATCUR);
    else
      return m_RS.SaleBCCost;
    end;
  END;
```

---

## Пример 32: `PlanRepDate`

**Источник:** `Mac/DLNG/VA/vadealfinres.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
  MACRO PlanRepDate():DATE
    var Z = DaysInYearByBasis(m_RS.Basis, this.StartDate(), true);
    var PlanRepDate = this.StartDate() + Z;
    
    if(m_RS.AvoirKind == AVOIRISSKIND_DEPOSIT_CERTIFICATE)
      PlanRepDate = m_RS.Maturity;
    else
      if((m_RS.BCTermFormula == VS_TERMF_FIXEDDAY) OR (m_RS.BCTermFormula == VS_TERMF_INATIME))
        PlanRepDate = m_RS.Maturity;
      elif((m_RS.BCTermFormula == VS_TERMF_DURING) and (date(m_RS.BCPresentationDate) > date(0,0,0)))
        PlanRepDate = date(m_RS.BCPresentationDate) + m_RS.Diff;
      elif(m_RS.BCTermFormula == VS_TERMF_ATSIGHT) //по предъявлении
        if(m_RS.Expiry >= this.StartDate()) //но не позднее
          if(m_RS.Expiry < PlanRepDate)
            PlanRepDate = m_RS.Expiry;
          end;
        elif((m_RS.Expiry < this.StartDate()) and (m_RS.Maturity >= this.StartDate())) //но не ранее
          PlanRepDate = m_RS.Maturity;
        end;
      end;
    end;

    return PlanRepDate;
  END;
```

---

## Пример 33: `FillPayment_113_114`

**Источник:** `Mac/Mbr/uf113114gendoc.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro FillPayment_113_114(xml:object, wlmes, Payment:object)
  var tmpstr = "";
  Payment.Number = ReadAttribute(xml,"AccDocNo", "AccDoc");
  Payment.Reference = wlmes.Trn;
  Payment.Date = ToDate(ReadAttribute(xml,"AccDocDate", "AccDoc"));
  Payment.ValueDate = wlmes.OutsideAbonentDate;

  Payment.BaseFIID = NATCUR;
  Payment.BaseAmount = moneyL( ReadAttribute(xml,"Sum") )/100;

  // Payer
  var ClientINN = ReadOptinalAttribute(xml, "INN", "Payer");
  tmpstr = ReadOptinalAttribute(xml, "KPP", "Payer");
  if( tmpstr and ClientINN )
    ClientINN = ClientINN + "/" + tmpstr;
  end;
```

---

## Пример 34: `FnsMesToXml`

**Источник:** `Mac/Mbr/fnsxmlmes_common.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro FnsMesToXml( wlmes, XmlMes : @string, ErrMes : @string ) : bool
  var result : bool = true;
  ErrMes = "";
  XmlMes = "";

  var XmlObj : object = ActiveX("Microsoft.XMLDOM");
  XmlObj.appendChild( XmlObj.createProcessingInstruction("xml", " version='1.0' encoding='windows-1251'") );
  var AllFldsAreRead : bool = false;
  var node : object = null;

  // Часть данных в сообщении записывается на экспорте. Поэтому для их заполнения здесь используем хэндлер.
  var FldHandler : TFldExportHandler;
  if(gVersFormat and IsFnsVersionIs4xx(gVersFormat))
    FldHandler = TFldExportHandlerFns_v4_xx( true );
  else
    FldHandler = TFldExportHandlerFnsXml( true );
  end;
```

---

## Пример 35: `Блок`

**Источник:** `Mac/Cb/bilimpsfclsal.mac`
**Тип:** `block`
**Размер:** 13 строк

```rsl
//АдрГАРТип
class AddrGar() 
    var Регион = "";
    var НаимРегион = "";	
    var МуниципРайон = MunicipalDistr();
    var ГородСелПоселен = UrbanRuralSettl();
    var НаселенПункт = PopulArea();	
    var ЭлПланСтруктур = ElemPlanStruct();
    var ЭлУлДорСети = ElemStreet();
    var ЗемелУчасток = "";	
    var Здание = House();
	var ПомещЗдания = RoomHouse();
    var ПомещКвартиры = RoomApart();
```

---

## Пример 36: `Блок`

**Источник:** `Mac/DLNG/dlpaym.mac`
**Тип:** `block`
**Размер:** 14 строк

```rsl
  Programmer  : Сабитов Р.Р.
  Description : Сервисные ф-ии для платежей
└───────────────────────────────────────────────────────────────────────────*/
IMPORT FIInter;
/* Класс свойств платежа*/
CLASS (TBfile) TBFilePMPROP (p1,p2,p3,p4,p5)
    MACRO find (paym, IsKredit)
        this.KeyNum = 0;
        this.rec.PaymentId = paym.rec.PaymentID;
        if (IsKredit)
            this.rec.DebetCredit = 1;
        else
            this.rec.DebetCredit = 0;
        end;
```

---

## Пример 37: `PaySecCnt`

**Источник:** `Mac/DLNG/SECUR/NpTxRepoReg_Data.mac`
**Тип:** `macro`
**Размер:** 6 строк

```rsl
  MACRO PaySecCnt():INTEGER
     if( m_PaySecCnt == NULL )
        GetPaySecTotAndPaySecCnt(min(this.DD2, this.H0_2()), @m_PaySecCnt, @m_PaySecTot);
     end;
     return m_PaySecCnt;
  END;
```

---

## Пример 38: `ReadRfrdDocInf`

**Источник:** `Mac/Mbr/nbrkgdp8.mac`
**Тип:** `macro`
**Размер:** 20 строк

```rsl
  macro ReadRfrdDocInf( RfrdDocInfNode : object )
    for ( var curNode, RfrdDocInfNode.childNodes )
      if ( curNode.BaseName == "RfrdDocInf" )
        var Nb = ReadOptinalNodeText( curNode, "Nb" );
        if ( Nb != "" )
          wlpmrmprop.Number = substr(Nb, 1, 25);
        end;
        var RltdDt = ReadOptinalNodeText( curNode, "RltdDt" );
        if ( RltdDt != "" )
          wlpmrmprop.Date = ToDateYYYY_MM_DD(RltdDt);
        end;
      elif ( curNode.BaseName == "AddtlRmtInf" )
        if ( Ground == "" )
          Ground = curNode.Text;
        else
          Ground = Ground + "\r\n" + curNode.Text;
        end;
      end;
    end;
  end;
```

---

## Пример 39: `GetCriticalDate`

**Источник:** `Mac/CONV_FC/v_laros_fc_1_2.mac`
**Тип:** `macro`
**Размер:** 73 строк

```rsl
macro GetCriticalDate( Object )
    var stat     = True;
    var Found    = True;
    var NextCalc     = NullDate;
    var FormContr    = sb_dtyp.FormContr;


    if( Object != 2001 )
       stat = GetApplTpForObject( depositr.IsCur,
                                  depositr.Type_Account,
                                  Object );
    else
       stat = True;
    end;

    if( stat )
       /* ищем запись в sb_dtype для связки Object_Type -- ApType */
       stat = GetPc_ALgRec( depositr.IsCur, pc_apltp.ApType, DateConvert );
       if( not stat )
          Protocol.Error( "Не найден алгоритм расчета на", DateConvert,
                          "по вкладу", pc_apltp.ApType );
       end;
    end;

    if( stat )
       if  ( FormContr ==  1 ) /* для срочных                  */
          if( depositr.End_DateDep != NullDate )
             if( PC_ALG.GrafCalc != 0 ) /* задан график расчета процентов */
                 stat = SetCalcDates();
             else
                DateNextCalc = depositr.End_DateDep;
                DatePrevCalc = depositr.Start_DateDep;
             end;
          else
             stat = SetCalcDates();
          end;
       elif( FormContr == 20 ) /* для депозитов                */
          if( Object == 2001 )
             if( PC_ALG.GrafCalc != 0 ) /* задан график расчета процентов */
                 stat = SetCalcDates();
             else
                DateNextCalc = depositr.End_DateDep;
                DatePrevCalc = depositr.Start_DateDep;
             end;
          else
             stat = SetCalcDates();
          end;
       elif( FormContr == 30 ) /* для пролонгируемых депозитов */
          DateNextCalc = depositr.End_DateDep;
          if( depositr.Prol_DateDep != NullDate )
             DatePrevCalc = depositr.Prol_DateDep  - 1;
          else
             DatePrevCalc = depositr.Start_DateDep;
          end;
       else                    /* для недоговоров              */
          stat = SetCalcDates();
       end;
    end;
    if( stat )
       /*CriticalDate = DatePrevCalc + 1;*/
       CriticalDate = DatePrevCalc;
       if( CriticalDate < depositr.Open_Date )
          CriticalDate = depositr.Open_Date;
       end;
    end;

    if( CriticalDate == depositr.Open_Date )
       CriticalDate = NullDate;
    end;

    /*[ #                           ############  # ]( depositr.Account, CriticalDate, Object );*/
    return stat;
end;
```

---

## Пример 40: `PM_SetPrimDocumentState`

**Источник:** `Mac/Cb/pm_setst.mac`
**Тип:** `macro`
**Размер:** 16 строк

```rsl
macro PM_SetPrimDocumentState( Payment:RsbPayment, state:integer )

  var obj:object;

  if( Payment.DocKind == DLDOC_MEMORIALORDER )
    obj = GenObject( "RsbMemorialOrder", Payment.DocumentID );
    if( state == DOCUMENT_ST_DEFERRED )
      obj.State = CB_DOC_STATE_DEFERRED;
    elif( state == DOCUMENT_ST_WORKING )
      obj.State = CB_DOC_STATE_WORKING;
    elif( state == DOCUMENT_ST_REJECTED )
      obj.State = CB_DOC_STATE_REJECTED;
    elif( state == DOCUMENT_ST_CLOSED )
      obj.State = CB_DOC_STATE_CLOSED;
    end;
  end;
```

---
