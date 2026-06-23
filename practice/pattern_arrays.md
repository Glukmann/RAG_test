# Практика: Массивы и динамические коллекции (Array, TArray, size, value)

**Теория:** [BnRSL.md## Класс: `TArray`]

Ниже приведены 15 реальных примера из производственной кодовой базы RS-Bank.

## Пример 1: `GetBankTextByOraErr`

**Источник:** `Mac/Cb/mfo_lib.mac`  
**Тип:** `private macro`  
**Размер:** 57 строк

```rsl
private macro GetBankTextByOraErr(oraErrTag, oraErrOptyp, oraErrMesg)
  var bankText = "";
  if(index(oraErrTag, "BNKSEEK:010")) bankText = bankText + "ORA10: Редактирование свойств существующего субъекта."; end;
  if(index(oraErrTag, "BNKSEEK:020")) bankText = bankText + "ORA20: Присвоение роли \"Банк\"."; end;
  if(index(oraErrTag, "BNKSEEK:030")) bankText = bankText + "ORA30: Присвоение роли \"Участник БЭСП\"."; end;
  if(index(oraErrTag, "BNKSEEK:040")) bankText = bankText + "ORA40: Изъятие роли \"Участник БЭСП\"."; end;
  if(index(oraErrTag, "BNKSEEK:042")) bankText = bankText + "ORA42: Установка признака категории \"Категория участия в БЭСП\""; end;
  if(index(oraErrTag, "BNKSEEK:043")) bankText = bankText + "ORA43: Закрытие признака категории \"Категория участия в БЭСП\""; end;
  if(index(oraErrTag, "BNKSEEK:044")) bankText = bankText + "ORA44: Установка признака категории \"Отключение от БЭСП\""; end;
  if(index(oraErrTag, "BNKSEEK:045")) bankText = bankText + "ORA45: Закрытие признака категории \"Отключение от БЭСП\""; end;
  if(index(oraErrTag, "BNKSEEK:050")) bankText = bankText + "ORA50: Создание записи bankdprt."; end;
  if(index(oraErrTag, "BNKSEEK:060")) bankText = bankText + "ORA60: Редактирование блока данных банка."; end;
  if(index(oraErrTag, "BNKSEEK:070")) bankText = bankText + "ORA70: Ввод полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "BNKSEEK:080")) bankText = bankText + "ORA80: Изменение полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "BNKSEEK:090")) bankText = bankText + "ORA90: Ввод краткого наименования по учету ЦБ."; end;
  if(index(oraErrTag, "BNKSEEK:100")) bankText = bankText + "ORA100: Изменено краткого наименование по учету ЦБ."; end;
  if(index(oraErrTag, "BNKSEEK:110")) bankText = bankText + "ORA110: Изменение юридического адреса субъекта."; end;
  if(index(oraErrTag, "BNKSEEK:120")) bankText = bankText + "ORA120: Ввод юридического адреса субъекта."; end;
  if(index(oraErrTag, "BNKSEEK:130")) bankText = bankText + "ORA130: Закрытие кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "BNKSEEK:140")) bankText = bankText + "ORA140: Установка кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "BNKSEEK:150")) bankText = bankText + "ORA150: Закрытие кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "BNKSEEK:160")) bankText = bankText + "ORA160: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "BNKSEEK:170")) bankText = bankText + "ORA170: Установка связи с банком-правопреемником."; end;
  if(index(oraErrTag, "BNKSEEK:180")) bankText = bankText + "ORA180: Установка флага \"Блокировка\" для банка отсутствующего в импортируемом файле."; end;
  if(index(oraErrTag, "BNKSEEK:190")) bankText = bankText + "ORA190: Установка атрибута \"Не является участником электронных расчетов\" для банка отсутствующего в импортируемом файле."; end;
  if(index(oraErrTag, "BNKSEEK:200")) bankText = bankText + "ORA200: Установка даты закрытия банка"; end;
  if(index(oraErrTag, "KORREK:010" )) bankText = bankText + "ORA510: Закрытие кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "KORREK:020" )) bankText = bankText + "ORA520: Закрытие кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "KORREK:030" )) bankText = bankText + "ORA530: Редактирование свойств субъекта."; end;
  if(index(oraErrTag, "KORREK:040" )) bankText = bankText + "ORA540: Присвоение роли \"Банк\"."; end;
  if(index(oraErrTag, "KORREK:050" )) bankText = bankText + "ORA550: Присвоение роли \"Участник БЭСП\"."; end;
  if(index(oraErrTag, "KORREK:052" )) bankText = bankText + "ORA552: Установка признака категории \"Категория участия в БЭСП\""; end;
  if(index(oraErrTag, "KORREK:053" )) bankText = bankText + "ORA553: Установка признака категории \"Отключение от БЭСП\""; end;
  if(index(oraErrTag, "KORREK:054" )) bankText = bankText + "ORA554: Закрытие признака категории \"Категория участия в БЭСП\""; end;
  if(index(oraErrTag, "KORREK:055" )) bankText = bankText + "ORA555: Закрытие признака категории \"Отключение от БЭСП\""; end;
  if(index(oraErrTag, "KORREK:056" )) bankText = bankText + "ORA556: Изъятие роли \"Участник БЭСП\"."; end;
  if(index(oraErrTag, "KORREK:060" )) bankText = bankText + "ORA560: Создание записи bankdprt."; end;
  if(index(oraErrTag, "KORREK:070" )) bankText = bankText + "ORA570: Редактирование блока данных банка."; end;
  if(index(oraErrTag, "KORREK:080" )) bankText = bankText + "ORA580: Изменение полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "KORREK:090" )) bankText = bankText + "ORA590: Ввод полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "KORREK:100" )) bankText = bankText + "ORA600: Изменено краткого наименование по учету ЦБ."; end;
  if(index(oraErrTag, "KORREK:110" )) bankText = bankText + "ORA610: Ввод краткого наименования по учету ЦБ."; end;
  if(index(oraErrTag, "KORREK:120" )) bankText = bankText + "ORA620: Изменение юридического адреса субъекта."; end;
  if(index(oraErrTag, "KORREK:130" )) bankText = bankText + "ORA630: Ввод юридического адреса субъекта."; end;
  if(index(oraErrTag, "KORREK:140" )) bankText = bankText + "ORA640: Закрытие кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "KORREK:150" )) bankText = bankText + "ORA650: Установка кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "KORREK:160" )) bankText = bankText + "ORA660: Закрытие кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "KORREK:170" )) bankText = bankText + "ORA670: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "KORREK:180" )) bankText = bankText + "ORA680: Установка связи с банком-правопреемником."; end;
  if(index(oraErrTag, "KORREK:190" )) bankText = bankText + "ORA690: Установка флага \"Блокировка\"."; end;
  if(index(oraErrTag, "KORREK:200" )) bankText = bankText + "ORA700: Установка даты закрытия банка"; end;
  if(index(oraErrOptyp, "I")) bankText = bankText + " Ошибка вставки!"  ; end;
  if(index(oraErrOptyp, "U")) bankText = bankText + " Ошибка изменения!"; end;
  if(index(oraErrOptyp, "D")) bankText = bankText + " Ошибка удаления!" ; end;
  bankText = bankText + oraErrMesg;
  return bankText;
end;
```

---

## Пример 2: `GetOkatoList`

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

## Пример 3: `GetED807TextByOraErr`

**Источник:** `Mac/Cb/mfo_lib.mac`  
**Тип:** `private macro`  
**Размер:** 42 строк

```rsl
private macro GetED807TextByOraErr(oraErrTag, oraErrOptyp, oraErrMesg)
  var bankText = "";
  if(index(oraErrTag, "ED807:010")) bankText = bankText + "ORA010: Редактирование свойств существующего субъекта."; end;
  if(index(oraErrTag, "ED807:020")) bankText = bankText + "ORA020: Присвоение роли \"Банк\"."; end;
  if(index(oraErrTag, "ED807:030")) bankText = bankText + "ORA030: Ввод полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "ED807:040")) bankText = bankText + "ORA040: Изменение полного наименования по учету ЦБ."; end;
  if(index(oraErrTag, "ED807:050")) bankText = bankText + "ORA050: Ввод краткого наименование по учету ЦБ."; end;
  if(index(oraErrTag, "ED807:060")) bankText = bankText + "ORA060: Изменено краткого наименование по учету ЦБ."; end;
  if(index(oraErrTag, "ED807:070")) bankText = bankText + "ORA070: Присвоение роли \"Участник ПС БР\"."; end;
  if(index(oraErrTag, "ED807:080")) bankText = bankText + "ORA080: Присвоение роли \"Банк\"."; end;
  if(index(oraErrTag, "ED807:090")) bankText = bankText + "ORA090: Закрытие кода вида 1 \"Код\"."; end;
  if(index(oraErrTag, "ED807:100")) bankText = bankText + "ORA100: Установка кода вида 1 \"Код\"."; end;
  if(index(oraErrTag, "ED807:110")) bankText = bankText + "ORA110: Установка кода вида 1 \"Код\"."; end;
  if(index(oraErrTag, "ED807:120")) bankText = bankText + "ORA120: Закрытие кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "ED807:130")) bankText = bankText + "ORA130: Установка кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "ED807:140")) bankText = bankText + "ORA140: Установка кода вида 3 \"БИК (ЦБ РФ)\"."; end;
  if(index(oraErrTag, "ED807:150")) bankText = bankText + "ORA150: Закрытие кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:160")) bankText = bankText + "ORA160: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:170")) bankText = bankText + "ORA170: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:180")) bankText = bankText + "ORA180: Закрытие кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:190")) bankText = bankText + "ORA190: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:200")) bankText = bankText + "ORA200: Установка кода вида 13 \"Рег. номер кред. орг-ции\"."; end;
  if(index(oraErrTag, "ED807:210")) bankText = bankText + "ORA210: Закрытие кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:220")) bankText = bankText + "ORA220: Установка кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:230")) bankText = bankText + "ORA230: Установка кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:240")) bankText = bankText + "ORA240: Закрытие кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:250")) bankText = bankText + "ORA250: Установка кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:260")) bankText = bankText + "ORA260: Установка кода вида 47 \"UIS\"."; end;
  if(index(oraErrTag, "ED807:270")) bankText = bankText + "ORA270: Ввод юридического адреса субъекта."; end;
  if(index(oraErrTag, "ED807:280")) bankText = bankText + "ORA280: Изменение юридического адреса субъекта."; end;
  if(index(oraErrTag, "ED807:290")) bankText = bankText + "ORA290: Создание записи блока данных участника ПС."; end;
  if(index(oraErrTag, "ED807:300")) bankText = bankText + "ORA300: Редактирование блока данных участника ПС."; end;
  if(index(oraErrTag, "ED807:310")) bankText = bankText + "ORA310: Закрытие кода вида 6 \"BIC ISO (SWIFT)\"."; end;
  if(index(oraErrTag, "ED807:320")) bankText = bankText + "ORA320: Установка кода вида 6 \"BIC ISO (SWIFT)\"."; end;
  if(index(oraErrTag, "ED807:330")) bankText = bankText + "ORA320: Обновление кода вида 6 \"BIC ISO (SWIFT)\"."; end;
                                                                                              
  if(index(oraErrOptyp, "I")) bankText = bankText + " >> Ошибка вставки! "  ; end;
  if(index(oraErrOptyp, "U")) bankText = bankText + " >> Ошибка изменения! "; end;
  if(index(oraErrOptyp, "D")) bankText = bankText + " >> Ошибка удаления! " ; end;
  bankText = bankText + oraErrMesg;
  return bankText;
end;
```

---

## Пример 4: `УстановитьПодсказку`

**Источник:** `Mac/DLNG/SECUR/scservop.mac`  
**Тип:** `private macro`  
**Размер:** 22 строк

```rsl
PRIVATE MACRO УстановитьПодсказку( TableName:string, IndexNum:integer, DefaultHint:string, ScrolStatus:integer, ScrolKind:integer ):string
  //  Возможные значения ScrolStatus:
  //  DL_COMM_PREPARING = 0,  // на этапе подготовки
  //  DL_COMM_READIED,        // готовые (создана операция)
  //  DL_COMM_CLOSED,         // закрытые
  //  DL_COMM_ALL             // все


  //  Возможные значения ScrolKind:
  //  DL_COMMDOC     = 104,   // Операции расчета комиссий
  //  DL_RESERVEDOC  = 106,   // Операции резервирования средств под обесценивание ЦБ
  //  DL_OVERVALUE   = 108,   // Операции переоценки ценных бумаг
  //  DL_OVERVALUE_RD  = 123,  // Переоценка внебаланса
  //  DL_OVERVALUE_NVPI = 134,  // Переоценка НВПИ
  //  DL_GET_INCOME     = 157, // БОЦБ - начисление процентного/дисконтного дохода

  //пример
  //return "/*+FIRST_ROWS LEADING(t) INDEX(t ddl_comm_dbt_idx0)*/";

  return DefaultHint;

END;
```

**Комментарий автора:**
Возможные значения ScrolStatus: DL_COMM_PREPARING = 0,  // на этапе подготовки DL_COMM_READIED,        // готовые (создана операция)

---

## Пример 5: `SfFormDocumentsBatch`

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

## Пример 6: `RunAction`

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

## Пример 7: `УстановитьПодсказку`

**Источник:** `Mac/DLNG/DEPO/dpglobop.mac`  
**Тип:** `private macro`  
**Размер:** 19 строк

```rsl
PRIVATE MACRO УстановитьПодсказку( TableName:string, IndexNum:integer, DefaultHint:string, ScrolStatus:integer, ScrolKind:integer ):string
  //  Возможные значения ScrolStatus:
  // 0,  //все       
  // 1,  //отложенное
  // 2,  //открытое  
  // 3   //закрытое  
  
  //  Возможные значения ScrolKind:
  // DP_DEPOPER_CONVERT       852, // "Поручение на конвертацию ц/б"             
  // DP_DEPOPER_REPAY         854, // "Поручение на погашение (анулирование) ц/б"
  // DP_DEPOPER_BONEMISS      856, // "Поручение на бонусную эмиссию ц/б"        
  // ALL_KIND_OF_DOC          0,   // Все

  //пример
  //return "/*+FIRST_ROWS LEADING(t) INDEX(t ddpcorpop_dbt_idx0)*/";

  return DefaultHint;

END;
```

**Комментарий автора:**
Возможные значения ScrolStatus: 0,  //все 1,  //отложенное

---

## Пример 8: `ОбработкаПортфеля`

**Источник:** `Mac/Cb/form_res.mac`  
**Тип:** `macro`  
**Размер:** 49 строк

```rsl
macro ОбработкаПортфеля( _AcCase, _AcCaseParm, _AcCaseSubCase )
  
  var stat : bool;
  record AcCase(accase);
  record AcCaseParm(accasepm);
  record AcCaseSubCase(accasscs);

  var caseResObj : CalcReserveAccCase;
  var ReserveAccount : string;
  var query, rs;
  var params : TArray;
  var ReserveType : integer;
  /*Значения процентов резервирования и категорий качества в текущем формировании*/
  var RiskGroup      : integer;
  var ReservePercent : double;
  /*Классификации резервов*/
  var ClassifReserveLoss     : string;
  var ClassifReserveLoans    : string;
  /*Даты послених расчетов по видам резервов*/
  var LastDateCalcReserveLoss : date;
  var LastDateCalcReserveLoans : date;
  /*Признаки изменения параметров для видов резерва*/
  var ChangedLoss     : bool;
  var ChangedLoans    : bool;
  var ChangedEstimated : bool;
  var HasAccTransactions : bool;

  SetBuff( AcCase        , _AcCase        );
  SetBuff( AcCaseParm    , _AcCaseParm    );
  SetBuff( AcCaseSubCase , _AcCaseSubCase );

  stat = true;

  ChangedLoss     = true;
  ChangedLoans    = true;
  ChangedEstimated = true;

  InitReserveSum();

  ReserveAccount = GetAccountReserveForCase(AcCase, AcCaseSubCase);

  LastDateCalcReserveLoss = GetCaseLastDateCalcReserveLoss(UniID(AcCaseSubCase, 0, DOCKIND_SUBCASE));
  LastDateCalcReserveLoans = GetCaseLastDateCalcReserveLoans(UniID(AcCaseSubCase, 0, DOCKIND_SUBCASE));

  if (LastDateCalcReserveLoss != null)
    HasAccTransactions = GetHasAccTransactionsForCase(AcCase, AcCaseSubCase, LastDateCalcReserveLoss);
  else
    HasAccTransactions = GetHasAccTransactionsForCase(AcCase, AcCaseSubCase, LastDateCalcReserveLoans);
  end;
```

---

## Пример 9: `ValLogProc`

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

## Пример 10: `formingUNRZEx`

**Источник:** `Mac/Cb/ptgfias.mac`  
**Тип:** `private macro`  
**Размер:** 39 строк

```rsl
private macro formingUNRZEx( ptaddress, mode, status_:@integer, prnMess, retUNRZ:@string, placeFld )
  var i;
  var Text;
  var Result;
  array ButtonCCC;
  array ButtonCC;
  array ButtonC;
  array TextCC;
  var ColumnsR  : TArray = TArray;
  var ColumnsPr : TArray = TArray;
  var ColumnsD  : TArray = TArray;
  var ColumnsP  : TArray = TArray;
  var ColumnsPn : TArray = TArray;
  var ColumnsS  : TArray = TArray;
  var ColumnsH  : TArray = TArray;

  var TempUNRZ, TempPostIndex, TempOkato, TempOktmo, TempFiasGuid, TempCadastral;
  var TempObjectID;
  var Region  , CodeRegion  , newRegion  , newCodeRegion  , newRegionNum,
      Province, CodeProvince, newProvince, newCodeProvince,
      District, CodeDistrict, newDistrict, newCodeDistrict,
      Place   , CodePlace   , newPlace   , newCodePlace   ,
      Plan    , CodePlan    , newPlan    , newCodePlan    ,
      Street  , CodeStreet  , newStreet  , newCodeStreet  ;
  var HouseType, House, HouseType1, NumCorps, HouseType2, Building, 
      newHouseType, newHouse, newHouseType1, newNumCorps, newHouseType2, 
      newBuilding, newStead, newSteadType, newApartType, newFlat;
  var SteadNumber, Flat, GFiasApartType;
  var tmpStatus = 1;//status_;

  var stat, cmd, rs;

  var query;
  var params : TArray;

  macro EvProc( rs, cmd, id, key )
    if(( cmd == DLG_KEY ) and ( key == 13 ))
      return CM_SELECT;
    end;
```

---

## Пример 11: `CalcDepoCommReserveByAcc`

**Источник:** `Mac/DLNG/DEPO/dpressrvopstart.mac`  
**Тип:** `private macro`  
**Размер:** 25 строк

```rsl
PRIVATE MACRO CalcDepoCommReserveByAcc(dl_comm, AccountID:integer)
  var cmd, query, DataSet;
  var prc, sz;
  var SumsArr = TArray();
  var BaseAcc = TRecHandler("account.dbt");
  var ReservAcc = TRecHandler("account.dbt");
  var RSAcc = TRecHandler("account.dbt");
  var RSCatCode = "";
  var delta = 0;
  var err = 0;
  var accTrn;
  var i = 0;
  var Rnew = 0.0, Rold = 0.0;
  var fd;
  var resbase = TRecHandler("dpresbase.dbt");
  var resbaseCache = RsbSQLInsert("dpresbase.dbt");
  var resobjArr = TArray();
  var resobjCache = RsbSQLInsert("dpresobj.dbt");
  var realIDs = TArray();
  var ResBaseID = 0;

  if(GetAccount(AccountID, BaseAcc) != 0)
    msgbox("Ошибка при поиске счета");
    return 1;
  end;
```

---

## Пример 12: `ОформитьВыкупВекс`

**Источник:** `Mac/DLNG/VEKSEL/vsrepay3.mac`  
**Тип:** `private macro`  
**Размер:** 24 строк

```rsl
PRIVATE MACRO ОформитьВыкупВекс(bnr, leg, order, tick, lnk, prm)
var
   stat = 0;

   Вексель=bnr;
   ЦУ=leg;
   ВексПД=VSBannerFD(bnr, leg);
   ВалютаНоминала=ЦУ.rec.PFI;
   ВалУч = ВексПД.ОпределитьВалютуУчета();
//   Номинал=ЦУ.rec.Principal;
//   СвязьВД=lnk;
//   ОстДиск=Вексель.rec.DiscountRemainder;
   isPc=ВексельПроцентный(ЦУ);

//   Сп = lnk.rec.BCCost;
//   Спер = 0;
//   СперПр = 0;
//   СуммаСписДк = 0;
//   ДатаДоначисления = Date(0,0,0);

   /*if( (Index(bnr.rec.BCState, "И") == 0) and (ВалУч != ВалютаНоминала) )
     if( not ВыполнитьПереоценкуНВПИ(bnr.rec.BCID, ДатаОформл, ДатаОформл, ВалУч, ВексПД) )
       stat = 1;
     end;
```

---

## Пример 13: `ExecuteStep`

**Источник:** `Mac/Cb/pm061_10.mac`  
**Тип:** `macro`  
**Размер:** 47 строк

```rsl
macro ExecuteStep( Kind_Operation, first, KindDoc, ID_Operation )

  var stat = 0;
  var ActionStep:integer = ACTION_STEP_UNDEF;
  var pmaddpi    = TRecHandler("pmaddpi.dbt");
  var DateNoChange   :date = date(0,0,0);
  var TypeAccount:string = "";
  var TransAccount:string = "";
  var TransChapter;
  var TransFIID;
  var DepID:integer = 0;
  var NameAccount:string = "";
  var rsacc:RsdRecordset;
  var IfNext, pi;
  
  ActionStep = ChooseActionStep();
  
  if( ActionStep == ACTION_STEP_TRANSACCOUNT )

    var AccountID:string = "";
    MakeAccountID( PaymentObj.Chapter, PaymentObj.PayerFIID, PaymentObj.ReceiverAccount, AccountID, SIZEOBJECTLEN );
    var query:string = "SELECT t_AttrID FROM dobjlink_dbt             " +
                       " WHERE t_ObjectType     = :OBJTYPE_ACCOUNT_OBJ  " +
                        "  AND t_GroupID        = :OBJROLE_ACC_TRANSIT  " +
                        "  AND t_AttrType       = :OBJTYPE_ACCOUNT_ATTR " +
                        "  AND t_ObjectID       = :AccountID            " +
                        "  AND t_ValidFromDate <= :VALID_TO_DATE_FROM   " +
                        "  AND t_ValidToDate   >= :VALID_TO_DATE_TO     ";

    var params:TArray = makeArray( SQLParam("OBJTYPE_ACCOUNT_OBJ", OBJTYPE_ACCOUNT    ), 
                                   SQLParam("OBJROLE_ACC_TRANSIT"  , OBJROLE_ACC_TRANSIT),
                                   SQLParam("OBJTYPE_ACCOUNT_ATTR" , OBJTYPE_ACCOUNT    ),
                                   SQLParam("AccountID"            , AccountID          ),
                                   SQLParam("VALID_TO_DATE_FROM"   , VALID_TO_DATE      ),
                                   SQLParam("VALID_TO_DATE_TO"     , VALID_TO_DATE      ) );

    var rs:RsdRecordset = execSQLselect( query, params, true );
  
    if( rs and rs.moveNext() )
      TransAccount = SubStr(rs.Value(0), 10);
      TransChapter = int(SubStr(rs.Value(0),1, 2));
      TransFIID = int(SubStr(rs.Value(0),3, 7));

      if( PaymentObj.FutureReceiverFIID != TransFIID )
        msgbox("Валюта счета получателя отличается от валюты транзитного счета");
        return 1;
      end;
```

---

## Пример 14: `_ClientIdentMass`

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

## Пример 15: `GetPtsvdpList1`

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

