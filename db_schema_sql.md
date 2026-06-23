# SQL-запросы RS-Bank (извлечены из макросов)

Данный документ содержит реальные SQL-запросы, извлечённые из производственных макросов RS-Bank, сгруппированные по таблицам.

## Таблица: `dual`

**SQL-запросы (73):**

```sql
cmd = RSDCommand("select cast(rsi_npto.CheckContrIIS(?) as integer) as IsIIS from dual");
```

```sql
var query:string ="SELECT 1        " + "  FROM DUAL     " + " WHERE EXISTS ( " + "SELECT /*+FIRST_ROWS(1)*/ 1                " + "  FROM dmccateg_dbt cat, dmcaccdoc_dbt doc " + " WHERE doc.t_catid    =  cat.t_id          " + "   AND doc.t_account  = :Account           " + "   AND doc.t_currency = :F
```

```sql
var cmd = DL_RSDCommand("select RSI_DlCalendars.GetDateWorkDayForPayStep(?,?,?) as WorkDate FROM dual"); cmd.addParam(dateFrom);
```


## Таблица: `dparty_dbt`

**SQL-запросы (70):**

```sql
const PartySql = "SELECT t.t_partyid, t.t_name, nvl(REGEXP_REPLACE (t.T_NORMALIZEDNAME, '[^[:alnum:]]', '', 1, 0), chr(1)) T_NORMALIZEDNAME FROM dparty_dbt t, dpersn_dbt ps WHERE lpad(to_char(t.T_PARTYID), 10, '0') NOT IN " + "(select t_object from DOBJATCOR_DBT t where t.t_objecttype = 3 and t.t_gr
```

```sql
var strSQL : string = "SELECT t_LegalForm " + "FROM dparty_dbt " + "WHERE t_partyID = " + pmpaym.rec.Payer;
```

```sql
"select * " + "from dparty_dbt " + "where t_PartyId = ? ");
```


## Таблица: `dfininstr_dbt`

**SQL-запросы (45):**

```sql
q = String("select t_ccy from dfininstr_dbt where t_fiid = ", fiid); ds = TRsbDataset(q);
```

```sql
q = String("select t_ISO_Number from dfininstr_dbt where t_fiid = ", fiid); ds = TRsbDataset(q);
```

```sql
q = String("select t_name from dfininstr_dbt where t_fiid = ", fiid); ds = TRsbDataset(q);
```


## Таблица: `ddepositr_dbt`

**SQL-запросы (39):**

```sql
SqlQuery = string("select d.t_SpecialAccess from ddepositr_dbt d where d.t_Referenc=",Indx.Referenc); cmd = RsdCommand(SqlQuery);
```

```sql
findAccount = rsdcommand("select * from ddepositr_dbt where T_REFERENC = :AccountID"); findAccount.AddParam("AccountID", RSDBP_IN, AccountID);
```

```sql
findAccount = rsdcommand("select * from ddepositr_dbt where t_account = :AccNumber" + whereFNcashCond); findAccount.AddParam("AccNumber", RSDBP_IN, AccNumber);
```


## Таблица: `dpmpaym_dbt`

**SQL-запросы (29):**

```sql
query = "select t_paymentid, t_amount, ddlcomis_dbt.t_id from dpmpaym_dbt" + " inner join ddlcomis_dbt on ddlcomis_dbt.t_id = dpmpaym_dbt.t_subpurpose" + " where dpmpaym_dbt.t_dockind = " + DL_SFCONTR + " and dpmpaym_dbt.t_documentid = " + contr_pd.GetContr().ID + " and t_purpose = 83 and t_paymstat
```

```sql
( "Select dep.t_Name " "  from dpmpaym_dbt pm, ddp_dep_dbt dep "
```

```sql
var q = "select t_DocKind " + "  from dpmpaym_dbt " + " where t_PaymentID = :PaymentID ";
```


## Таблица: `daccount_dbt`

**SQL-запросы (28):**

```sql
var AccAccQuery = "select t_Chapter, t_Code_Currency, t_Account from daccount_dbt where t_Account = ?"; var AccAccSelect = DL_RSDCommand(AccAccQuery);
```

```sql
var AccTaxQuery = "select t_Chapter, t_Code_Currency, t_Account from daccount_dbt where t_Account = ?"; var AccTaxSelect = DL_RSDCommand(AccTaxQuery);
```

```sql
cmd = DL_RSDCommand(  "select * from daccount_dbt" + " where t_AccountID = ? "
```


## Таблица: `ddp_dep_dbt`

**SQL-запросы (28):**

```sql
select = String("select dep.t_code, party.t_shortname ", "from ddp_dep_dbt dep, dparty_dbt party ",
```

```sql
select = String("select dep.t_name from ddp_dep_dbt dep ", "where dep.t_code = ", code);
```

```sql
var findDep =  rsdcommand("select * from ddp_dep_dbt where T_CODE = ?"); findDep.AddParam("codeCur", RSDBP_IN, Int(element.key2));
```


## Таблица: `ddl_tick_dbt`

**SQL-запросы (25):**

```sql
Select = DL_RSDCommand("select * from ddl_tick_dbt where t_DealID = ?"); Select.AddParam(prm.DealID);
```

```sql
var q = "select tick.t_DealCode DealCode, tickRepo.t_DealCode Repo" + " from ddl_tick_dbt tick, ddl_tick_dbt tickRepo"
```

```sql
rs = TRsbDataSet("select t_DealID from ddl_tick_dbt tick where" + " tick.t_ParentID = " + String(DealID));
```


## Таблица: `dsbdepdoc_dbt`

**SQL-запросы (25):**

```sql
var strcmd = "SELECT t_rest, t_kindop, t_action, t_issuspended, t_typeoper, t_flags, t_mode, t_referenc " + "FROM dsbdepdoc_dbt " + "WHERE t_referenc <= ? and t_date_document <= ? and t_NumDayDoc <= ? " + "ORDER BY t_referenc desc, t_date_document desc, t_NumDayDoc desc";
```

```sql
var strcmd = "SELECT t_rest, t_kindop, t_action, t_issuspended, t_typeoper, t_flags, t_mode, t_referenc " + "FROM dsbdepdoc_dbt " + "WHERE t_referenc <= ? and t_date_document <= ? and t_NumDayDoc <= ? " + "ORDER BY t_referenc desc, t_date_document desc, t_NumDayDoc desc";
```

```sql
var strcmd = "SELECT t_ground, t_kindop, t_action, t_issuspended, t_typeoper, t_flags, t_mode " + "FROM dsbdepdoc_dbt " + "WHERE t_referenc = ? and t_depdate_document = ? and t_typeoper = ? ";
```


## Таблица: `dcurrency_dbt`

**SQL-запросы (18):**

```sql
strcmd = "SELECT t_code_currency " + "FROM dcurrency_dbt " + "WHERE t_externalcode = ?";
```

```sql
var findInCur =  rsdcommand("select * from dcurrency_dbt where T_CODE_CURRENCY = ?"); findInCur.AddParam("codeCur", RSDBP_IN, Int(inCurrCode));
```

```sql
var findOutCur =  rsdcommand("select * from dcurrency_dbt where T_CODE_CURRENCY = ?"); findOutCur.AddParam("codeCur", RSDBP_IN, Int(outCurrCode));
```


## Таблица: `dperson_dbt`

**SQL-запросы (17):**

```sql
cmd = RsdCommand("select T_NAME from DPERSON_DBT WHERE T_OPER = :id"); rs = RsdRecordset(cmd);
```

```sql
VAR Choice = DL_Scroll("select  prs.t_Oper Oper, prs.t_Name NameOper, dep.t_Name NameDep from dperson_dbt prs, ddp_dep_dbt dep "  + " where prs.t_CodeDepart = dep.t_Code " + " order by prs.t_oper",
```

```sql
var findOperPartyID = rsdcommand("SELECT * FROM dperson_dbt WHERE T_Oper = ? "); findOperPartyID.AddParam("oper", RSDBP_IN, contractor);
```


## Таблица: `ddlrq_dbt`

**SQL-запросы (17):**

```sql
query =   "select rq.* from ddlrq_dbt rq " + " where rq.t_DocKind = ? "
```

```sql
cmd = DL_RSDCommand( "SELECT count(*) as count " +"  FROM ddlrq_dbt rq_sp1, ddlrq_dbt rq_sp2, ddl_tick_dbt Tick, (SELECT t_Kind_Operation, t_DocKind, "
```

```sql
Query = "SELECT * FROM ddlrq_dbt" + " WHERE  t_DocKind = ?"
```


## Таблица: `dsfcontr_dbt`

**SQL-запросы (17):**

```sql
sql = "select CONTR.T_ID " + " FROM DSFCONTR_DBT CONTR, DTSORDER_DBT ORD " + " WHERE CONTR.T_SERVKIND = " + string(PTSK_TRUST) + "  AND CONTR.T_ID = ORD.t_SfContrID " + "  AND CONTR.T_PARTYID = ? " + "  AND ord.T_dockind = ?";
```

```sql
Select = "select sfc.t_id, sfc.t_DateConc, sfc.t_Name, sfc.t_Number, prt1.t_ShortName Payer, prt2.t_ShortName Contractor " + "  from dsfcontr_dbt sfc, dparty_dbt prt1, dparty_dbt prt2 "+ " where prt1.t_PartyID = sfc.t_partyID"+ "   and prt2.t_PartyID = sfc.t_ContractorID ";
```

```sql
Select = "SELECT CONTR.T_ID ID, CONTR.T_NUMBER NUM, CONTR.T_NAME NAME, CONTR.T_DATECONC DATECONC, " + "(SELECT T_SHORTNAME FROM DPARTY_DBT WHERE T_PARTYID = CONTR.T_PARTYID) PARTYID, " + "(SELECT T_SHORTNAME FROM DPARTY_DBT WHERE T_PARTYID = CONTR.T_CONTRACTORID) CONTRACTORID " + "FROM DSFCONTR_DBT
```


## Таблица: `err`

**SQL-запросы (16):**

```sql
sqlString = "SELECT t.t_partyid                                                           " + "      ,t.ora_err_tag$                                                        " + "      ,t.ora_err_optyp$                                                      " + "      ,t.ora_err_mesg$
```

```sql
sqlString = "SELECT t.t_partyid                                                           " + "      ,t.ora_err_tag$                                                        " + "      ,t.ora_err_optyp$                                                      " + "      ,t.ora_err_mesg$
```

```sql
sqlString = "SELECT t.t_objectid                                                           " + "      ,t.ora_err_tag$                                                         " + "      ,t.ora_err_optyp$                                                       " + "      ,t.ora_err_mesg$
```


## Таблица: `ddl_secur_dbt`

**SQL-запросы (15):**

```sql
QueryStr = "select * from ddl_secur_dbt sec where (sec.t_contractkind = " + DL_MMPAWN + ")and " "(sec.t_contractid = " + prm_order.ContractID + ")";
```

```sql
QueryStr = "select * from ddl_secur_dbt sec where (sec.t_contractkind = " + DL_IBCDOC + ")and " "(sec.t_contractid = " + prm_dealID + ")and(sec.t_generalcontract = " + prm_order.ContractID + ")";
```

```sql
QueryStr = "select nvl(sum(t_Nominal), 0) as sumNominal from ddl_secur_dbt where "; QueryStr = QueryStr + "(t_contractkind = " + DL_MMPAWN + ")and(t_contractid = " + prm_order.ContractID + ")";
```


## Таблица: `dnptxobj_dbt`

**SQL-запросы (15):**

```sql
QueryCond   = "select NVL(sum( (CASE WHEN N.t_Direction = " + string(TXOBJ_DIR_OUT) + "                      THEN -N.t_Sum0 " + "                      ELSE  N.t_Sum0 END " + ") " + "              ), 0 " + "           ) C2 " + "  from dnptxobj_dbt N " + " where N.t_Client = ? " + " AND RSI_NPTO.Check
```

```sql
QueryCond   = "select NVL(sum( (CASE WHEN N.t_Direction = " + string(TXOBJ_DIR_OUT) + "                      THEN -N.t_Sum0 " + "                      ELSE  N.t_Sum0 END " + ") " + "              ), 0 " + "           ) C2 " + "  from dnptxobj_dbt N " + " where N.t_Client = ? " + " AND RSI_NPTO.Check
```

```sql
QueryCond   = "select NVL(sum( (CASE WHEN N.t_Direction = " + string(TXOBJ_DIR_OUT) + "                      THEN -N.t_Sum0 " + "                      ELSE  N.t_Sum0 END " + ") " + "              ), 0 " + "           ) C2 " + "  from dnptxobj_dbt N " + " where N.t_Client = ? " + " AND RSI_NPTO.Check
```


## Таблица: `dpmwrtsum_dbt`

**SQL-запросы (13):**

```sql
m_SqlTxt =  "SELECT NVL(SUM( case when fin.t_AvoirKind != ? "+ "                then round(WRTSUM.t_Amount,0) "+ "                else WRTSUM.t_Amount end ), 0) am, WRTSUM.t_fiid, WRTSUM.t_party, WRTSUM.t_CONTRACT "+ "  FROM DPMWRTSUM_DBT WRTSUM, dfininstr_dbt fin "+ " WHERE WRTSUM.t_Department = ?
```

```sql
m_SqlTxt ="SELECT NVL(SUM( case when fin.t_AvoirKind != ? "+ "                then round(B.t_Amount,0) "+ "                else B.t_Amount end ), 0) am, L.t_FIID , L.t_Party, L.t_CONTRACT "+ "  FROM DPMWRTSUM_DBT L, DPMWRTBC_DBT B, dfininstr_dbt fin "+ " WHERE  L.t_Department = ? "+ "   AND L.t_Part
```

```sql
var cmd = RSDCommand("select q.SumID, q.BalanceCost, q.Amount, q.DealID, q.AmountBD  as AmountBD " + "  from (" + "        select L.t_SumID SumID, L.t_Parent Parent, L.t_BalanceCostBD BalanceCost, L.t_AmountBD Amount, L.t_AmountBD AmountBD, DECODE(L.t_Parent, 0, L.t_DealID, (select t_DealID from dpm
```


## Таблица: `dobjcode_dbt`

**SQL-запросы (13):**

```sql
cmd = rsdcommand("SELECT t_ObjectID FROM dobjcode_dbt WHERE t_ObjectType = 3 " + "  AND t_CodeKind = ? " + "  AND t_State = 0 " + "  AND t_Code = ? ");
```

```sql
cmd = DL_RSDCommand("SELECT code.T_BankDate BankDate FROM DOBJCODE_DBT code WHERE code.T_OBJECTTYPE = 3 AND code.t_CODEKIND = 17 AND code.T_STATE = 0 AND code.T_OBJECTID = ? AND code.T_BankDate < ? ORDER BY code.T_BankDate DESC ");
```

```sql
var doublers_sql = "select pt.t_name, bik.t_code " + sql_base + ",(select t_code, t_objectid from dobjcode_dbt WHERE t_objecttype = 3 and t_codekind = 3 AND t_bankclosedate = TO_DATE ('01/01/0001', 'MM/DD/YYYY') and t_state = 0) bik " + ",dparty_dbt pt where cnt.t_objectid = pt.t_partyid and bik.t_o
```


## Таблица: `dbicplusiban_tmp`

**SQL-запросы (13):**

```sql
rs = RsdRecordset("SELECT count(1) FROM dbicplusiban_tmp WHERE t_processrecord IN (0, 1)" ); if( rs.MoveNext() )
```

```sql
rs = RsdRecordset("SELECT COUNT(1) FROM dbicplusiban_tmp WHERE t_processrecord <> -2 AND t_modification_flag = '" + ModificationFlag + "'" ); if( rs.MoveNext() )
```

```sql
rs = RsdRecordset("SELECT COUNT(1) FROM dbicplusiban_tmp WHERE t_processrecord = 1" ); if( rs.MoveNext() )
```


## Таблица: `dcompens_dbt`

**SQL-запросы (13):**

```sql
cmd = RsdCommand("select cmp.t_codclient, cmp.t_account, cmp.t_accClsDate, cmp.t_restIn91, cmp.t_rate, "+ " cmp.t_FullSum, cmp.t_sum, cmp.t_date, cmp.t_destAccount, cmp.T_DESTCLIENTCODE, dep.t_SpecialAccess as SpecialAccess"+ " from dcompens_dbt cmp, ddepositr_dbt dep where cmp.t_fncash = ? and cmp.
```

```sql
cmd_1 = RsdCommand("select t_lastname, t_firstname, t_patrname, t_birthdate from dcompens_dbt where t_fncash = ? and t_autokey = ? "); cmd_1.addParam("t_fncash", RsdBp_in);
```

```sql
cmd_1 = RsdCommand("select dcompens_dbt.t_date, dcompens_dbt.t_sum, dcompens_dbt.t_destaccount from dcompens_dbt " "where (dcompens_dbt.t_kind <> ? or dcompens_dbt.t_appltype <> ? or dcompens_dbt.t_fncash <> ? or dcompens_dbt.t_account <> ?) "
```


## Таблица: `dpartcode_dbt`

**SQL-запросы (12):**

```sql
sqlPartcode = RSDCommand("select t_Code from dpartcode_dbt " + " where t_PartyID = ? " + "   and t_CodeKind = 1");
```

```sql
Select = "select distinct prt.t_Name, prt.t_ShortName, " + "       partcode.t_Code, clt.t_PartyID " + "  from dpartcode_dbt partcode, dclient_dbt clt, dparty_dbt prt " + " where clt.t_ServiceKind in(" + ServCond + ")" + IncludeBankCond + "   and clt.t_PartyID = partcode.t_PartyID " + "   and prt.t_P
```

```sql
sString = "SELECT ROWNUM AS FROWNUM, " + "    NVL ((SELECT T_CODE FROM DPARTCODE_DBT WHERE T_PARTYID = lnk.T_PARTYID AND T_CODEKIND = 1), CHR (1)) T_CODE1, " + "    PT.T_NAME, " + "    PS.T_BORN, " + "    SERV.T_CATEGORYCODE, " + "    SERV.T_SYSTEMID, " + "    SERV.T_ISDELETEDPEOPLE " + "FROM DPDLSE
```


## Таблица: `v_scwrthistex`

**SQL-запросы (12):**

```sql
cmd = DL_RSDCommand(  "select 1" + "  from v_scwrthistex "
```

```sql
return "SELECT t.T_FIID, rsb_pmwrtoff.WRTGetPortfolioAmount(?,t.t_FIID,?,?,-1,-1,?,1,0,0) DURest " + "from ( select t.T_FIID" + "         FROM v_scwrthistex t, dfininstr_dbt fin " + "        WHERE t.t_instance = (SELECT MAX (t_instance) " + "                                FROM v_scwrthistex " + "
```

```sql
return "SELECT t.T_FIID, rsb_pmwrtoff.WRTGetPortfolioAmount(?,t.t_FIID,?,?,-1,-1,?,1,0,0) DURest " + "from ( select t.T_FIID" + "         FROM v_scwrthistex t, dfininstr_dbt fin " + "        WHERE t.t_instance = (SELECT MAX (t_instance) " + "                                FROM v_scwrthistex " + "
```


## Таблица: `dsb_algop_dbt`

**SQL-запросы (12):**

```sql
sqlfndMinSum = "SELECT * FROM DSB_ALGOP_DBT WHERE T_KIND = ? AND T_ISCUR = ? AND T_NUMSTEPALG IN (240, 242) AND T_NUMOPERT IN (3) " " AND T_PRMD > 0 AND T_FLAGEXE <> CHR (0) ORDER BY T_PRMD ASC";
```

```sql
sqlfndMinSum = "SELECT * FROM DSB_ALGOP_DBT WHERE T_KIND = ? AND T_ISCUR = ? AND T_NUMSTEPALG IN (240, 242) AND T_NUMOPERT IN (73) " " AND T_PRMD > 0 AND T_FLAGEXE <> CHR (0) ORDER BY T_PRMD ASC";
```

```sql
sqlfndMinSum = "SELECT * FROM DSB_ALGOP_DBT WHERE T_KIND = ? AND T_ISCUR = ? AND T_NUMSTEPALG IN (240, 242) AND T_NUMOPERT IN (73,3) " " AND T_PRMD > 0 AND T_FLAGEXE <> CHR (0) ORDER BY T_PRMD ASC";
```


## Таблица: `dbnkdirpls_tmp`

**SQL-запросы (12):**

```sql
rs = RsdRecordset("SELECT count(1) FROM dbnkdirpls_tmp WHERE t_processrecord >= 0" ); if( rs.MoveNext() )
```

```sql
rs = RsdRecordset("SELECT COUNT(1) FROM dbnkdirpls_tmp WHERE t_processrecord >= 0 AND t_modification_flag = '" + ModificationFlag + "'" ); if( rs.MoveNext() )
```

```sql
rs = RsdRecordset("SELECT COUNT(1) FROM dbnkdirpls_tmp WHERE t_processrecord = 1" ); if( rs.MoveNext() )
```


## Таблица: `dpcrate_dbt`

**SQL-запросы (11):**

```sql
cmd2 = RSDCommand ("select max(T_BEGINDATE) as MAXDATE from DPCRATE_DBT " + "where T_AUTOPERC = ? and T_BEGINDATE <= ? ");
```

```sql
cmd = RSDCommand ("select T_AUTOKEY from DPCRATE_DBT " + "where T_MACRO <> 0 and T_AUTOPERC = ?");
```

```sql
cmd = RSDCommand ("select T_BEGINDATE, T_AUTOKEY from DPCRATE_DBT " + "where T_MACRO <> 0 and T_AUTOPERC = ? and T_BEGINDATE <= ?" + "and T_BEGINDATE >= ?");
```


## Таблица: `dwlmes_dbt`

**SQL-запросы (11):**

```sql
select = "select t_mesID, t_state from dwlmes_dbt where t_direct=chr(0) and T_TRN=:RelatedRef and T_Department = :OperD"; params = makeArray( SQLParam("RelatedRef", wlmes.RelatedRef),
```

```sql
var select = "Select t_MesID " + "  from dwlmes_dbt " + " where t_Trn = :Trn " + "   and t_Direct = 'X' ";
```

```sql
var select = "Select t_MesID " + "  from dwlmes_dbt " + " where t_Trn = :Trn ";
```


## Таблица: `dadress_dbt`

**SQL-запросы (11):**

```sql
"SELECT t.t_number, t.t_opendate, dp.t_partyid, " + "       (SELECT p.t_shortname FROM dparty_dbt p WHERE p.t_partyid = dp.t_partyid) as t_BankDepartment, " + "       (select t_adress from (SELECT * FROM dadress_dbt WHERE t_ObjectType = 3 AND t_type IN (1, 2, 3) AND t_id = RSI_RSBPARTY.PT_GetCurADRE
```

```sql
var query = "SELECT a.t_Adress adr " + " FROM dadress_dbt a "
```

```sql
var query = "select * from dadress_dbt where t_objecttype = 3 AND t_objectid = " + string(PartyID) + " AND t_Id = RSI_RSBPARTY.PT_GetCurADRESS(t_objecttype, t_partyid, t_type)";
```


## Таблица: `dsfconcom_dbt`

**SQL-запросы (11):**

```sql
var Sql= "SELECT count(1) numr " "  FROM dsfconcom_dbt concom, dsfcomiss_dbt com " + " WHERE com.t_feetype = concom.t_feetype " + "   AND com.t_number = concom.t_commnumber " + "   AND concom.t_FeeType = ?" + "   AND concom.t_CommNumber = ?" + "   AND concom.t_ObjectType = ? " + "   AND concom.t_SfP
```

```sql
var Sql= "SELECT count(1) numr " "  FROM dsfconcom_dbt concom, dsfcomiss_dbt com " + " WHERE com.t_feetype = concom.t_feetype " + "   AND com.t_number = concom.t_commnumber " + "   AND concom.t_FeeType = ?" + "   AND concom.t_CommNumber = ?" + "   AND concom.t_ObjectType = ? " + "   AND concom.t_SfP
```

```sql
var Sql= "SELECT count(1) AS numr "+ "  FROM dsfconcom_dbt concom, dsfcomiss_dbt com, (SELECT DISTINCT concom.t_ObjectID AS SfPlanID "+ "                                                   FROM dsfconcom_dbt concom, dsfcomiss_dbt com " + "                                                  WHERE com.t_
```


## Таблица: `dfiwarnts_dbt`

**SQL-запросы (11):**

```sql
var select = RSDCommand("select count(1) amount " + " from  dfiwarnts_dbt " + "where  t_FIID = ? " + "  and  t_IsPartial = 'X'");
```

```sql
var query =   "select fiwarnts.t_FirstDate" + IIF(IsA12 or IsA21, " - 1", "") + " as t_FirstDate " + "from dfiwarnts_dbt fiwarnts "
```

```sql
var Select = Dl_RSDCommand("SELECT WR.T_FIID, FI.T_NAME, AV.T_ISIN, AV.T_LSIN, CASE WHEN WR.T_ISPARTIAL = CHR(88) THEN 'ЧП' ELSE 'Купон' END AS KIND_PAY, " + "       WR.T_NUMBER, WR.T_LISTDATE, WR.T_DRAWINGDATE " + "FROM DFIWARNTS_DBT WR, DFININSTR_DBT FI, DAVOIRISS_DBT AV " + "WHERE WR.T_FIID = FI.
```


## Таблица: `ddl_comm_dbt`

**SQL-запросы (11):**

```sql
var cmd = DL_RSDCommand("select * from DDL_COMM_DBT "+ " WHERE T_DocumentID = ? "+ "   AND T_DocKind = ? ");
```

```sql
query= "SELECT DEPSET.T_EXTDEPOCODEOUR FROM DDL_COMM_DBT IOCOMM, DDLGRDEAL_DBT, DDLDEPSET_DBT DEPSET WHERE "+ "IOCOMM.T_DOCKIND = ? "+ "AND IOCOMM.T_DOCUMENTID = ? "+ "AND DEPSET.T_DEPSETID = IOCOMM.T_DEPSETID ";
```

```sql
query = "SELECT t.T_DOCUMENTID, t.T_DOCKIND, t.T_OPER, t.T_COMMCODE " + "  FROM DDL_COMM_DBT t, DSFCOMISS_DBT sfcomiss, DSFCONCOM_DBT sfconcom, DSFCONTR_DBT sfcontr " + " WHERE t.T_DOCKIND = ? " + "   AND t.T_COMMSTATUS < 2 " + "   AND sfcontr.T_ID (+) = t.T_CONTRACTID " + "   AND sfconcom.T_ID (+)
```


