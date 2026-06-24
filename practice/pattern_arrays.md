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

## Пример 16: `SendDPRegistry`

**Источник:** `Mac/BOOK/SendPFRNotice.mac`
**Тип:** `macro`
**Размер:** 25 строк

```rsl
macro SendDPRegistry()
  var countrcv = 0;
  var rs = FindNotSyncPersn();
  var source = RSCPFRSource;
  var notice = RSCPFRNotice;
  var clnts = TArray;
  var maxpack, totalrcv;
  var senderID;
  var errReport = "";
  var stat = 0;
  var k = 0;
  var resultlist;
  var IDMas = TArray;
  var CurIDMas = Tarray;
  GetRegistryValue( "RS-CONNECT\\ПФР\\RETAIL\\MAXPACKET", V_INTEGER, maxpack );
  GetRegistryValue( "RS-CONNECT\\SENDERID\\RETAIL", V_STRING, senderID );

  while( rs.movenext() )
    var rs_acc = FindLastAcc(rs.value("t_personid"));
    if( rs_acc.movenext)
      clnts[clnts.size] = clnt(rs, rs_acc);
      IDMas[IDMas.size] = rs.value("t_personid");
      countrcv = countrcv + 1;
    end;
  end;
```

---

## Пример 17: `Init`

**Источник:** `Mac/Cb/ObjAccount.mac`
**Тип:** `macro`
**Размер:** 66 строк

```rsl
macro Init(ObjectType)

 var arrOpr = TArray;
 FltrAccObj = AccountFieldUse(ObjectType);

 FltrAccObj.addCondition( "Маска номера счета" , 
                            "СчНомер",
                            V_STRING,
                            "*",
                            UFF_METHOD_INPUT_EDIT,
                            NULL,
                            "CheckValueMask"
 );

 FltrAccObj.addCondition( "Балансовый счет" , 
                            "СчБаланс",
                            V_STRING,
                            "=!*",
                            UFF_METHOD_INPUT_EDIT,
                            NULL,
                            "CheckValueBal"
 );

 arrOpr = TArray;
 arrOpr[0] = "П";
 arrOpr[1] = "А" ;
 arrOpr[2] = "АП";

 FltrAccObj.addCondition( "Вид счета" , 
                            "СчВид",
                            V_STRING,
                            "=!",
                            UFF_METHOD_INPUT_LIST,
                            arrOpr,
                            NULL
 );


 arrOpr = GetTypeAcList( 1, 0 );


 FltrAccObj.addCondition( "Тип счета" , 
                            "СчТип",
                            V_STRING,
                            "=!",
                            UFF_METHOD_INPUT_LIST,
                            arrOpr,
                            NULL
 );
 
  
 arrOpr = GetTypeAcList( 2, 5 );


 FltrAccObj.addCondition( "Польз. тип счета" , 
                            "СчТипП",
                            V_STRING,
                            "=!",
                            UFF_METHOD_INPUT_LIST,
                            arrOpr,
                            NULL
 );
 

 return FltrAccObj;
end;
```

---

## Пример 18: `CopyArray`

**Источник:** `Mac/DLNG/SECUR/spRepFn2.mac`
**Тип:** `macro`
**Размер:** 11 строк

```rsl
macro CopyArray( DestArray, SourceArray )
   var
      counter;

   DestArray.Size = 0;
   counter = SourceArray.Size;
   while( counter > 0 )
      counter = counter - 1;
      DestArray[counter] = SourceArray[counter];
   end;
end;
```

---

## Пример 19: `find`

**Источник:** `Mac/DLNG/VA/vaoverblval.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
  macro find(_Валюта)
    var i = 0;

    while(i < Param.size)
      if(Param[i].Валюта == _Валюта)
        return i;
      end;
      i = i + 1;
    end;

    return -1;
  end;
```

---

## Пример 20: `ДобавьВМассив`

**Источник:** `Mac/DLNG/VEKSEL/vsclsrpo.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
 MACRO ДобавьВМассив(векс, связь, цен_усл, флаг ) 
   if ( флаг == null )
     ArrBnr[ArrBnr.size] = OneBnr (векс, связь, цен_усл )
   else
     ArrBnr_ms[ArrBnr_ms.size] = OneBnr (векс, связь, цен_усл )
   end;
 END;
```

---

## Пример 21: `Блок`

**Источник:** `Mac/CELLS/addchg_incrept.mac`
**Тип:** `block`
**Размер:** 12 строк

```rsl
      cnt = cnt + 1;
    end;
    if(data.PayGrRecs.size > 0)
    [ │  ######  │     #############      │          ######################            │]
    ( data.PayGrRecs[cnt].number:c, 
      getMYearStr(data.PayGrRecs[cnt].period):c, 
      (data.PayGrRecs[cnt].sum + " руб."):c 
    );
    end;
    [ └──────────┴────────────────────────┴────────────────────────────────────────────┘];
    [ ];
    [ ];
```

---

## Пример 22: `PM_ShowMassChDocLog`

**Источник:** `Mac/Cb/pmchdoclog.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
macro PM_ShowMassChDocLog( ChI1:bool, ChI2:bool, ChIWP:bool, Opers:TArray )

  var NameIndex = "";
  var i = 1;
  
  if( ChI1 )
    NameIndex = "№1";
  end;
```

---

## Пример 23: `GetComiss_SWMX`

**Источник:** `Mac/Mbr/swmx_GetComiss.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
macro GetComiss_SWMX
( PaymentID : integer, // ID платежа, для которого определяются реквизиты комиссии (обязательно)
  Group : integer, // Признак группировки (необязательно), значение по умолчанию 0
  OrderFIID : integer, // ID валюты для пересчета (необязательно), значение по умолчанию -1
  RateType : integer // Вид курса для пересчета (необязательно), значение по умолчанию 0
) : TArray // array of TDataCharges7

  DefaultParm(Group, 0);
  DefaultParm(OrderFIID, ALLFININSTR);
  DefaultParm(RateType, 0);

  var ComissList : TArray = TArray();

  var IsEqualPayerFIID : bool = false, IsEqualReceiverFIID : bool = false, FinishProc : bool = false;
  var CmsnTrns : TArray = GetCmsnTrns(PaymentID, @IsEqualPayerFIID, @IsEqualReceiverFIID);

  if( (Group == 0) and (CmsnTrns.size > 0) )
    CopyTrnsToComissList(ComissList, CmsnTrns, PaymentID);
  elif( (Group == 1) and (CmsnTrns.size > 0) )
    CopyTrnGroupToComissList( ComissList, CmsnTrns, PaymentID, OrderFIID, RateType,
      IsEqualPayerFIID, IsEqualReceiverFIID );
  else
    AddCmsnFromDtval(ComissList, PaymentID, Group, OrderFIID, @FinishProc);
  end;
```

---

## Пример 24: `TxGetReplPartykindList`

**Источник:** `Mac/DLNG/SECUR/Replication/ws_txreplpartykind.mac`
**Тип:** `macro`
**Размер:** 13 строк

```rsl
macro TxGetReplPartykindList(
  PageSize:Integer                             // Размер страницы
 ,PageNum:Integer                              // Номер страницы
 ,FilterItems//: TArray of FilterConditionItem // Значения фильтрации
 ,OrderItems//: TArray of OrderItem            // Параметры сортировки
):TArray
  var Query = "", AddWhere = "", OrderBy = "", Cmd = null, Set = null;
  var ReplPartykind = null;
  var ReplPartykindList = TArray();

  if(PageNum == null)
    RunError("Не задан обязательный параметр функции: номер страницы");
  end;
```

---

## Пример 25: `group`

**Источник:** `Mac/DLNG/VA/vae040.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
  MACRO group(Fiid, acc, amount)
   var i = find(Fiid, acc);
     if(i == -1)
        newGrp(fiid, acc, amount);
     else
        add (i, amount);
     end;
  END;
```

---

## Пример 26: `cmpStruct`

**Источник:** `Mac/LC/lcedit.mac`
**Тип:** `macro`
**Размер:** 5 строк

```rsl
  macro cmpStruct( newStruct, oldStruct )
    if( newStruct and oldStruct )
      NotChangeArray[NotChangeArray.size] = CmpPrm(TypeAction_Struct, newStruct, oldStruct);
    end;
  end;
```

---

## Пример 27: `AddRecord`

**Источник:** `Mac/DLNG/DV/dvfxreprdl.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
  macro AddRecord( _FICode, _Request, _Liab )
     var i;

     if( DataArr.size == 0 )
        DataArr[DataArr.size] = TItogRecord(_FICode, _Request, _Liab);
        return 0;
     end;

     i = FICodeSearch(_FICode);

     if( i == -1 )
        DataArr[DataArr.size] = TItogRecord(_FICode, _Request, _Liab);
     else
        DataArr[i].Request = DataArr[i].Request + _Request;
        DataArr[i].Liab = DataArr[i].Liab + _Liab;
     end;
  end;
```

---

## Пример 28: `CU_YesNoWin`

**Источник:** `Mac/Cb/commonutil.mac`
**Тип:** `macro`
**Размер:** 12 строк

```rsl
macro CU_YesNoWin(msg : string)
  Array Text;
  Array Button;
  Button(0) = "  Да   ";
  Button(1) = "  Нет  ";
  var but, ind = 0;

  Text(ind) = msg;
  but = ConfWin(Text, Button);
  
  return (but == 0);
end;
```

---

## Пример 29: `PrintVekInfo`

**Источник:** `Mac/DLNG/VA/vaprinfo.mac`
**Тип:** `macro`
**Размер:** 111 строк

```rsl
MACRO PrintVekInfo(dateB, dateE, ap, mode, mode_kind, UserLot)
VAR N, cmd, ok,
    status,
    PrevDate, PrevBuy, BuySum = $0, BuyFI,
    FirstTime, PrMes = TRUE,
    sqlSource, sqlSelect,
    v_count,
    start_date = dateB,
    progr = 0,
    F15_1, F16_1, F17_1, PFI_ISO_Code,print_count = 0;

    Dl_CallInsertStat( IIF( mode == 2, DL_OUTREPORT_EXCEL, DL_OUTREPORT_STD ) );
    sqlSource = " FROM dvsbanner_dbt vb, dfininstr_dbt fin WHERE ";

    if(mode_kind == VARM_VS) sqlSource = sqlSource + " vb.t_bcformkind = " + VSBANNER_FORMKIND_SIMPLE;
     elif (mode_kind == VARM_DS) sqlSource = sqlSource + " vb.t_bcformkind = " + VSBANNER_FORMKIND_CERT;
     elif (mode_kind == VARM_VS_DS) sqlSource = sqlSource + " ( vb.t_bcformkind = " + VSBANNER_FORMKIND_SIMPLE + " OR vb.t_bcformkind = " + VSBANNER_FORMKIND_CERT + " ) " ;
    end;

    sqlSource = sqlSource + " AND vb.t_Issuer not in (select t_PartyID from ddp_dep_dbt) "
                          + " AND fin.t_FIID = vb.t_FIID ";

    if (mode_kind == VARM_VS) sqlSource = sqlSource + " AND fin.t_avoirkind = " + AVOIRISSKIND_BILL;
    elif (mode_kind == VARM_DS) sqlSource = sqlSource + " AND fin.t_avoirkind = " + AVOIRISSKIND_DEPOSIT_CERTIFICATE;
    elif (mode_kind == VARM_VS_DS) sqlSource = sqlSource + " AND ( fin.t_avoirkind = " + AVOIRISSKIND_BILL + " OR fin.t_avoirkind = " + AVOIRISSKIND_DEPOSIT_CERTIFICATE + " ) " ;
    end;

    if(UserLot != "")
      sqlSource = sqlSource + " and vb.t_UserLot = '"+UserLot+"'";
    end;

    sqlSelect = "SELECT count(*) cnt " + sqlSource;
    cmd = TRsbDataSet(sqlSelect);
    cmd.MoveNext();

    v_count = int(cmd.cnt);
    v_count = v_count * (dateE - dateB + 1);

    cmd = TRsbDataSet("select vb.t_IssuerName, vb.t_BCID BCID, vb.t_BCTermFormula BCTermFormula, " +
                  "vb.t_BCPresentationDate BCPresentationDate, vb.t_IssuePlace IssuePlace, " +
                  "vb.t_BCNumber BCNumber, vb.t_BCSeries BCSeries, vb.t_BCFormKind BCFormKind" +
                  sqlSource +
                  "order by vb.t_IssuerName, vb.t_BCSeries, vb.t_BCNumber ", RSDVAL_CLIENT, RSDVAL_STATIC);

    cmd.NullConversion = true;

    VA_Rep_InitProgress(v_count);

    while(dateB <= dateE)
      if (IsWorkDay(dateB))

        N = 0;
        FirstTime = TRUE;
        TFaceValue.size = 0;
        TSum.size       = 0;
        TAcc_Bonus.size = 0;
        TAcc_Disk.size  = 0;
        TAcc_Proc.size  = 0;
        TBalans.size    = 0;
        TCurrCost.size  = 0;
        TFairValue.size = 0;

        TRes_Sum = $0;

        ok = cmd.MoveFirst();

        while(ok)
           if((ПодсистемаВекселяНаДату(cmd.BCID, dateB) == "N")
          and VA_GetABCStatusOnDate(cmd.BCID, dateB, status) and (status == VABANNER_STATUS_ACCOUNT))
              if(VA_GetBalanceDate(cmd.BCID, dateB, @PrevDate, @PrevBuy, @BuySum, @BuyFI)) // получаем информацию по сделке зачисления
                 if(not СделкаСКлиентом(PrevBuy))
                    N = N + 1;

                    if(FirstTime)
                       PrintHeader(dateB, not PrMes, UserLot);
                       FirstTime = FALSE;
                       PrMes = FALSE;
                    end;

                    PrintVeksel(N, cmd.IssuerName, cmd.BCID, cmd.BCTermFormula, cmd.BCPresentationDate,
                                   cmd.IssuePlace, cmd.BCNumber, cmd.BCSeries, cmd.BCFormKind,
                                   PrevDate, PrevBuy, BuySum, BuyFI, dateB, ap);
                 end;
              else
                 // не найдена сделка покупки, вероятно - разъезд в базе
                 ErrorStr[ErrorStr.Size] = "Не найдена сделка, которой был зачислен вексель " + trim(cmd.BCSeries) + " N " + trim(cmd.BCNumber);
              end;
           end;

           ok = cmd.MoveNext();
           UseProgress(progr = progr + 1);
        end;

        if(NOT FirstTime)
           PrintFooter(N, ap);
        end;

      end; //if (IsWorkDay(dateB))

      dateB = dateB + 1;//увеличиваем дату на один день
    end;

    RemProgress();

    rep.Print(mode, not PrMes, date_as_str(start_date),
        "Нет ни одной записи за указанный период для формирования отчета!");

    VA_PrintProtokol(ErrorStr);

    return 0;
END;
```

---

## Пример 30: `PrintData`

**Источник:** `Mac/Mbr/gginfpmsendrep.mac`
**Тип:** `macro`
**Размер:** 30 строк

```rsl
  macro PrintData( rs:RsdRecordSet )
    if( RepType == GGPIPmSendReqsGeneratingReportType_Generating )
      [│#####│##########│###############│###########│#########################│#########│#########################│###############│##################################################│###########│##################################################│
      ]( rs.Value("t_Number"), 
         date(rs.Value("t_Date")), 
         rs.Value("t_Kind"), 
         rs.Value("t_PayID"), 
         rs.Value("t_PayerAcc"), 
         rs.Value("t_RecBIC"), 
         rs.Value("t_ReceiverAcc"), 
         rs.Value("t_Amount"),
         rs.Value("t_Ground"):w, 
         rs.Value("t_ReqID"), 
         rs.Value("t_Result"):w );
    else
      [│#####│##########│###############│###########│#########################│#########│#########################│###############│##################################################│###########│######################################│##################################################│
      ]( rs.Value("t_Number"), 
         date(rs.Value("t_Date")), 
         rs.Value("t_Kind"), 
         rs.Value("t_PayID"), 
         rs.Value("t_PayerAcc"), 
         rs.Value("t_RecBIC"), 
         rs.Value("t_ReceiverAcc"), 
         rs.Value("t_Amount"),
         rs.Value("t_Ground"):w, 
         rs.Value("t_ReqID"),
         rs.Value("t_MessID"), 
         rs.Value("t_Result"):w );
    end;
  end;
```

---

## Пример 31: `del`

**Источник:** `Mac/DEPOSITR/atexit.mac`
**Тип:** `macro`
**Размер:** 8 строк

```rsl
  macro del( fn )
    var objFn = getFnObj(fn);
    var i = m_funcs.lsearch(Functor(objFn,null), @CompByFuncName);
    if( i < 0 )
      RunError("Функция не найдена");
    end;
    m_funcs.remove(i);
  end;
```

---

## Пример 32: `CreateString`

**Источник:** `Mac/CELLS/classes.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
macro CreateString( str )
var retString = "Условие:\n",i = 0;
array mass;

  StrSplit(str,mass,50);
  while( i < asize(mass) )
    retString = retString + mass(i) + "\n";
    i = i + 1;
  end;
```

---

## Пример 33: `InitDefValue`

**Источник:** `Mac/DLNG/UniLoader/ul_dataKind_i.mac`
**Тип:** `macro`
**Размер:** 15 строк

```rsl
  MACRO InitDefValue()
      if  (ValType(rs) != V_UNDEF)
          fld_idField.Value       = rs.Value("t_id");
          fld_nameField.Value     = rs.Value("t_name");
          fld_macroField.Value    = rs.Value("t_macro");
          fld_objClassField.Value = rs.Value("t_objClass");
      else
          fld_idField.Value       = 0;
          fld_nameField.Value     = "";
          fld_macroField.Value    = "";
          fld_objClassField.Value = "";
      end;

      this.Redraw();
  END;
```

---

## Пример 34: `FSSP_CalcPayAccReserve`

**Источник:** `Mac/Cb/fsspreserve.mac`
**Тип:** `macro`
**Размер:** 87 строк

```rsl
macro FSSP_CalcPayAccReserve
(
  SummRub : money, // Сумма к оплате
  AccountList : TArray, // TArray<TAccRestPrmElement> - Список счетов оплаты
  FssRequireObj : RsbFssRequire
)
// begin
  var stat = 0;
  var msg;
  var SummAmount = ZeroValue(V_MONEY);
  var AccEquire = FssRequireObj.AccEquire;

  // счета списка, по которым создана претензия резервирования
  var ReservAccountList = TArray(true, AccountList.size, AccountList.size);

  var Tmp;
  var RateType = 7; // ЦБ РФ
  GetRegistryValue("COMMON\\ПАРАМЕТРЫ ПРОЦЕДУР\\ГРУППОВАЯ ОПЛАТА\\ВИД_КУРСА", V_INTEGER, RateType);
  AccountList.sort(@AccountSortCallback);

  var i = 0;
  var RestElem;
  var oldRoundingUp;

  while (i < AccountList.size)
    var elem : TAccRestPrmElement = AccountList[i];
    if (elem.Origin == FSSPORIGIN_CORE)
      var Sum : Money = 0.0;
      var Amount : Money = SummRub;

      if (elem.CodeCurrency != 0)
        oldRoundingUp = FISetRoundingUp(4);
        ConvSum (Amount, SummRub, {curdate}, 0, elem.CodeCurrency, RateType);
        FISetRoundingUp(oldRoundingUp);
      end;

      var IsI2 = "";
      var IsWP = "";
      stat = FSSP_GetFreeAmount(elem.Account, elem.CodeCurrency, {curdate}, 
        FssRequireObj.Priority, @Sum, @IsI2, @IsWP, Round(Amount, 2));
      
      if ((Sum > ZeroValue(V_MONEY)) and (AccEquire.Find(elem.Account)))
        if (elem.CodeCurrency != 0)
          oldRoundingUp = FISetRoundingUp(4);
          ConvSum (Tmp, Sum, {curdate}, elem.CodeCurrency, 0, RateType);
          FISetRoundingUp(oldRoundingUp);

          RestElem = TAccRes(elem, Round(Tmp, 2));
          SummAmount = SummAmount + Round(Tmp, 2);
        else
          RestElem = TAccRes(elem, Sum);
          SummAmount = SummAmount + Sum;
        end;

        ReservAccountList[ReservAccountList.size] = RestElem;
        // Если на счете ХП признак наличия картотеки №2 или картотеки ОР
        if ((IsI2 == "X") or (IsWP == "X"))
          AccEquire.K2 = true;
          AccEquire.Update();
        end;
      end;
    else
      var result : TAccRestResultOther = FSSP_GetAccountRestOther(elem, FssRequireObj, SummRub, true);
      FSSP_CheckAccRestResultOther(result);

      if ((result.SummRub > ZeroValue(V_MONEY)) and (AccEquire.Find(elem.Account)))
        if (elem.CodeCurrency != 0)
          oldRoundingUp = FISetRoundingUp(4);
          ConvSum (Tmp, result.SummRub, {curdate}, elem.CodeCurrency, 0, RateType);
          FISetRoundingUp(oldRoundingUp);

          RestElem = TAccRes(elem, Tmp);
          SummAmount = SummAmount + Tmp;
        else
          RestElem = TAccRes(elem, result.SummRub);
          SummAmount = SummAmount + result.SummRub;
        end;

        ReservAccountList[ReservAccountList.size] = RestElem;
        if (result.IsK2)
          AccEquire.K2 = true;
          AccEquire.Update();
        end;
      end;
    end;
    i = i + 1;
  end;
```

---

## Пример 35: `СоздатьУзелName`

**Источник:** `Mac/DLNG/dl_elank.mac`
**Тип:** `macro`
**Размер:** 9 строк

```rsl
  MACRO СоздатьУзелName(Name,vObj)
    var УзелName =  CreateNode(Name, "xserializer:id",getXid());

    УзелName.appendChild(CreateElementValue("av:Код",vObj.cod));
    УзелName.appendChild(CreateElementValue("av:Описание",vObj.value));
    УзелName.appendChild(CreateElementValue("av:Активно",vObj.act));

    return (УзелName);
  End;
```

---

## Пример 36: `FillActiveList`

**Источник:** `Mac/DLNG/DEPO/dpposord.mac`
**Тип:** `macro`
**Размер:** 24 строк

```rsl
macro FillActiveList( condition_date, depoacc_id )
  var i = 0,
      stat,
      sub_stat,
      rest = $0;
  var query;

  KeyNum( accvanl, 1 );
  ClearRecord( accvanl );

  KeyNum( accsub, 0 );
  ClearRecord( accsub );

  //если мы сюда зашли, то значит хоть один счет уже найден, тогда
  stat = account.MoveFirst();

  if ( stat )
    DepoRootList.Size  = 0;
    DepoAccList.Size   = 0;
    IssuerList.Size    = 0;
    DepoAvoir.Size     = 0;
    DepoRestAvoir.Size = 0;
    XidIKList.Size     = 0;
  end;
```

---

## Пример 37: `IsMetalNameString`

**Источник:** `Mac/DEPOSITR/ingpimp.mac`
**Тип:** `macro`
**Размер:** 36 строк

```rsl
MACRO IsMetalNameString( str   : string, 
                         metal : integer,
                         boxed : bool ) : integer
    var subs = TArray,
        ret;        
        
    str = Trim( str );
    str = StrLwr ( str );
               
    subs = SubStrings( str, " " );    
    SetParm( 2, false );
        
    var i = 0;
    ret = PRS_ERR;
    while ( i < METALS.Size )
        if ( subs(0) == StrLwr( METALS(i) ) )
            SetParm( 1, i );            
            i = METALS.Size;
            ret = PRS_OK; 
        end;
        i = i + 1;
    end;

    if ( (ret == PRS_OK) and (subs.Size > 1) )
        
        if ( (subs.Size == 3) and (subs(1) == "в") and (subs(2) == "футляре") )
            SetParm( 2, true );      
        else
            ret = PRS_ERR;
        end;
        
    end;
            
    return ret;
 
END;
```

---

## Пример 38: `InsertFilialPayment`

**Источник:** `Mac/BOOK/PFRCommon.mac`
**Тип:** `macro`
**Размер:** 17 строк

```rsl
macro InsertFilialPayment( FNCash, realFNCash )
  file trnpayf("trn_payf.dbt") key 0 write;
  trnpayf.NumberContract = trnpaym.value("t_NumberContract");
  trnpayf.Num_PayMessage = trnpaym.value("t_Num_PayMessage");
  trnpayf.DateDocumentFilial = trnpaym.value("t_DateDocumentGlobal");
  trnpayf.PaymAppKind = trnpaym.value("t_iApplicationKind");
  trnpayf.PaymAppKey = trnpaym.value("t_ApplicationKey");
  trnpayf.FlagCur = trnpaym.value("t_FlagCur");
  trnpayf.Code_Currency = trnpaym.value("t_GlobalCurrency");
  trnpayf.TypeOper = trnpaym.value("t_TypeOper");
  trnpayf.ApplType = trnpaym.value("t_ApplType");
  trnpayf.Ground = trnpaym.value("t_Ground");
  if ( ValType( realFNCash ) != V_UNDEF )
    trnpayf.RealFNCash = Int( realFNCash );
  else
    trnpayf.RealFNCash = trnpaym.value("t_Department");
  end;
```

---

## Пример 39: `VS_MakeFRMOrder`

**Источник:** `Mac/DLNG/VEKSEL/vsfmotls.mac`
**Тип:** `macro`
**Размер:** 31 строк

```rsl
MACRO VS_MakeFRMOrder( Order, StepDate )
var
    frmorder  = TBFile("vsfrmord"), /* договор распоряжения по залогу */
    LnkArray = TArray,
    stat = 0;

    frmorder.rec.Signed = Order.Signed;
    frmorder.rec.OperType = VS_BLANKOPER_INCASH;
    frmorder.rec.ResponsPerson = Order.ResponsPerson;
    frmorder.rec.Status = VSFRMORD_STATUS_PREP;
    frmorder.rec.Kind_Operation =  CB_GetFirstValidOpenOpKind(DL_VSFRMORD, OPPF_FITALL, "К");
    frmorder.rec.Oper = 0;
    frmorder.rec.Department = Order.SendToDepartment;
    frmorder.rec.SendToDepartment = Order.SendToDepartment;
    frmorder.rec.Branch = Order.SendToDepartment;

    /* заполним буфер связок договор-вексель */

    if ( not VS_ForEachForm(Order,@ЗаполнениеLnk,LnkArray) )
      stat = 1;
    elif( LnkArray.Size == 0 )
        stat = 1;
    elif(VS_GetFmoNumber(frmorder) != 0)
        msgbox("Ошибка при генерации номера |распоряжения на прием бланков в кассу");
        stat = 1;
    else
        VS_InsertVSFRMORD(frmorder, LnkArray);
    end;

    return (stat == 0);
END;
```

---

## Пример 40: `CreateColList_Lmts`

**Источник:** `Mac/Mbr/nbrk_FillColLists.mac`
**Тип:** `macro`
**Размер:** 7 строк

```rsl
macro CreateColList_Lmts(ColList : TArray)
  AddColListElem( ColList, "Тип лимита", "Tp", 35, 4 );
  AddColListElem( ColList, "Счет", "IBAN", 34, 20 );
  AddColListElem( ColList, "Дата начала", "Dt", 10, 10 );
  AddColListElem( ColList, "Сумма", "Amt", 19, 19 );
  AddColListElem( ColList, "Д/К", "CdtDbtInd", 4, 4 );
end;
```

---
