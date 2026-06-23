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

