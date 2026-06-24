---
title: Reporting_RSLprc
description: Процедуры и функции на языке RSL для модуля
category: RSL-процедуры
source: PDF-документация RS-Bank V.6
sections: 119
generated: true
---

## Процедура: `IFRS_GetIFRSAccounts`

```rsl
IFRS_GetIFRSAccounts (TTrID:Integer, Accounts:Tarray):Bool
```

## Процедура: `IFRS_GetRelatedAccounts`

```rsl
IFRS_GetRelatedAccounts (IFRS_Accout:TrecHandleR, Accounts:Tarray, [StartDate:Date], [FinishDate:Date]):Bool
```

## Процедура: `IFRS_GetWorkPeriod`

```rsl
IFRS_GetWorkPeriod (CurStartDate:Date, CurFinishDate:Date [, PrevStartDate:Date] [, PrevFinishDate:Date]):Bool
```

## Процедура: `IFRS_SetWorkPeriod`

```rsl
IFRS_SetWorkPeriod (CurStartDate:Date, CurFinishDate:Date):Bool
```


```rsl
устанавливает заданный рабочий период в качестве текущего.
```

## Класс: `RcbApplication`

```rsl
RcbApplication()
```

Класс "Приложение", представляет собой подсистему "Регламентируемая отчетность".
Через объект класса осуществляется доступ ко всем глобализмам подсистемы. К таким,
например, относятся: параметры подсистемы, текущий отчет, с которым идет работа,
фабрика объектов и т.д.

**Примечание:**

В системе присутствует только один объект указанного класса, который
создается при входе в подсистему и разрушается при выходе из нее.

**Свойства:**

currentReport – текущий отчет. Если работа производится в контексте отчета, указанное
свойство содержит объект класса RcbReport
, являющийся текущим отчетом.
В противном случае свойство принимает значение Null. Свойство доступно
только для чтения и имеет тип Object.

**Пример:**

import RcbCoreInter;
var currentReport = RcbApplication().currentReport;
if (currentReport == NULL)
   MsgBox("Работа вне контекста отчета");
else
   MsgBox(currentReport.form.name);
end;
objectFactory – свойство создает объекты подсистемы. Свойство имеет тип Object,
представляет собой объект класса RcbObjectFactory
 и доступно только для
чтения.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
parameters – параметры приложения. Свойство имеет тип Object, представляет собой
объект класса RcbApplicationParameters
 и доступно только для чтения.
summator – сумматор, выполняющий сведение счетов. Свойство имеет тип Object и
представляет собой объект класса RcbSummator
.
transactionManager – менеджер транзакции; позволяет сохранить изменения в БД или
"откатить" их. Свойство имеет тип Object, представляет собой объект класса
RcbTransactionManager
 и доступно только для чтения.

**Пример:**

import RcbCoreInter;
var currentReport = RcbApplication().currentReport;
currentReport.attributeValue("Бн10201РуП").Reset();
RcbApplication().transactionManager.Commit();
Exit(0);
OnError(err);
RcbApplication().transactionManager.Rollback();
Exit(1);

## Класс: `RcbApplicationParameters`

```rsl
RcbApplicationParameters()
```

## Класс: `RcbAttribute`

```rsl
RcbAttribute()
```

Объект класса представляет собой один атрибут формы. Атрибутом может являться,
например, какое-либо поле отчета, ячейка таблицы и т.д. Кроме того, атрибутом может
быть и какой-нибудь скрытый (невидимый в печатной форме) и вспомогательный
показатель формы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

activePeriod – период, в течение которого атрибут входит в состав формы. Свойство
имеет тип Object и представляет собой объект класса RcbPeriod
.
form – форма, которой принадлежит атрибут. Свойство имеет тип Object и представляет
собой объект класса RcbForm
.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
var attribute = form.attribute("Бн20202__А");
MsgBox(attribute.form.name);
id – идентификатор атрибута. Свойство доступно только для чтения и имеет тип String.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
MsgBox(form.attribute("Бн20202__А").id
isManual – признак, указывающий на то, что значение атрибута должно быть введено
пользователем; тип Bool.
name – наименование атрибута. Свойство имеет тип String и доступно только для чтения.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
MsgBox(form.attribute("Бн20202__А").name);
precision – точность значения в единицах измерения (количество знаков после запятой);
тип Integer.
structure – ссылка на структуру, к которой привязан атрибут. Если атрибут является
простым (не составным), свойство принимает значение Null. Свойство имеет тип
Object и представляет собой класс RcbStructure
.

**Пример:**

import RcbCoreInter;
var form = RcbApplication().objectFactory.CreateForm("Форма
701");
var attribute = form.attribute("КО_список");
MsgBox(attribute.structure.name);
type – тип атрибута ("("Дата", "Штуки", "Деньги", "Число", "Проценты", "Строка", "Не
определен"). 
Свойство 
имеет 
тип 
Object, 
является 
объектом 
класса
RcbValueType и доступно только для чтения.

**Методы:**

isDependet()

## Класс: `RcbAttributeIterator`

```rsl
RcbAttributeIterator()
```

Класс "Итератор атрибутов", используется для навигации по коллекции атрибутов формы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

currentItem – текущий атрибут коллекции. Свойство имеет тип Object и представляет
собой объект класса RcbAttribute
.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
var attributeIterator = form.CreateAttributeIterator();
var attribute = NULL;
attributeIterator.MoveFirst();
while (not attributeIterator.IsDone())
   attribute = attributeIterator.currentItem;
   Println(attribute.name);
   attributeIterator.MoveNext();
end;

**Методы:**

count()

## Класс: `RcbAttributeValue`

```rsl
RcbAttributeValue()
```

Объект класса представляет собой значение атрибута отчета RcbAttribute
. Данный
объект поддерживает интерфейс значений как простого (RcbValue
), так и составного
(RcbCompositeValue
) атрибута формы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

attribute – ссылка на атрибут формы. Свойство имеет тип Object, является объектом
класса RcbAttribute
 и доступно только для чтения.
current – ссылка на точное или масштабированное значение (в зависимости от текущих
единиц измерения отчета: если в единицах национальной валюты, то exact,
иначе – scaled).
currentAsString – строковое представление текущего значения с учетом всех свойств
отчета и атрибута или поля структуры (точность, размерность и т.д.); тип String.
exact – значение в единицах национальной валюты. Тип свойства зависит от типа
значения (или поля структуры – для составного значения).
exactAsString – строковое представление точного значения с учетом всех свойств отчета
и атрибута или поля структуры (точность, размерность и т.д.); тип String.
parent – ссылка на родительское значение. Для корневого значения равно Null. Свойство
имеет тип Object, является объектом класса RcbCompositeValue
 и доступно
только для чтения.
report – ссылка на отчет, которому принадлежит значение атрибута. Свойство имеет тип
Object, является объектом класса  RcbReport
 и доступно только для чтения.
scaled – масштабированное значение в единицах измерения. Тип свойства зависит от
типа значения (или поля структуры – для составного значения).
scaledAsString – строковое представление масштабированного значения с учетом всех
свойств отчета и атрибута или поля структуры (точность, размерность и т.д.); тип
String.
valueId – идентификатор составного значения, должен быть уникален в пределах одного
атрибута. Корневое значение всегда имеет идентификатор, равный 0. Свойство
имеет тип Integer.

**Методы:**

addValue ([valueId/keyValue:Integer, Object]):Object

## Метод: `пересчитывает`

```rsl
все значения в единицах измерения по точным значениям. removeAllValues()
```

## Метод: `суммирует`

```rsl
зависимые значения.
```

**Параметры:**

summaryUnit – единицы суммирования (объект класса RcbSummaryUnit).
filter – фильтр на суммируемые значения (объект класса RcbIteratorFilter
).
value(valueId/keyValue:Integer,Object):Object

## Класс: `RcbAttributeValueIterator`

```rsl
RcbAttributeValueIterator()
```

Объект класса предназначен для итерирования значений атрибутов отчета. Используется
для навигации по коллекции значений атрибутов отчета.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

currentItem – текущий атрибут. Свойство имеет тип Object и представляет собой объект
класса RcbAttributeValue
.

**Пример:**

import RcbCoreInter;
var report = RcbApplication().currentReport;
var 
attributeValueIterator 
=
report.CreateAttributeValueIterator();
var attributeValue = NULL;
var recordsCount = 0;
InitProgress(attributeValueIterator.count);
attributeValueIterator.MoveFirst();
while (not attributeValueIterator.IsDone())
   attributeValue = attributeValueIterator.currentItem;
   Println(attributeValue.attribute.name);
   recordsCount = recordsCount + 1;
   UseProgress(recordsCount);
   attributeValueIterator.MoveNext();
end;
RemProgress();

**Методы:**

count():Integer

## Класс: `RcbCompositeValue`

```rsl
RcbCompositeValue()
```

Объект класса представляет собой значение составного атрибута формы. Помимо того,
что он содержит значения полей структуры составного атрибута, он содержит и список
подчиненных ему значений. Таким образом, в общем случае, он является узлом дерева
значений составных атрибутов.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

parent – ссылка на родительское составное значение. Для корневого значения свойство
равно Null. Свойство имеет тип Object, представляет собой объект класса
RcbCompositeValue
 и доступно только для чтения.
valueId – идентификатор составного значения; уникален в пределах одного атрибута.
Корневое значение всегда имеет идентификатор, равный 0. Свойство имеет тип
Integer.

**Методы:**

addValue ([keyValue/valueId:Object, Integer]):Object

## Метод: `может`

```rsl
содержать один из параметров: fieldId  идентификатор поля (String). valueId – идентификатор составного значения (Integer). Если подчиненное составное значение не найдено, метод возвращает значение Null. keyValue – ключевое значение искомого составного значения (объект класса RcbKeyValue ). Если подчиненное составное значение не найдено, метод возвращает значение Null.
```

**Возвращаемое значение:**



## Класс: `RcbField`

```rsl
RcbField()
```

Объект класса описывает поле структуры, использующейся для создания составных
атрибутов формы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

id – идентификатор поля; тип String.
name – наименование поля; тип String.
number – порядковый номер в структуре; тип Integer. 
precision – точность значения поля в единицах измерения (количество знаков после
запятой); тип Integer. 
size – размер поля (для строкового значения); тип Integer. 
structure – ссылка на структуру, которой принадлежит поле. Свойство имеет тип Object,
представляет собой объект класса RcbStructure
 и доступно только для
чтения.
type – тип поля; тип Integer.

## Класс: `RcbFieldIterator`

```rsl
RcbFieldIterator()
```

Объект класса предназначен для итерирования полей структуры. Используется для
навигации по коллекции полей структуры.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

currentItem – текущий элемент коллекции. Свойство имеет тип Object и представляет
собой объект класса RcbField
.

**Методы:**

count():Integer

## Класс: `RcbForm`

```rsl
RcbForm()
```

Объект класса описывает отчетную форму, регламентируемую Центральным Банком
Российской Федерации (ЦБ РФ). Форма предоставляется банками в ЦБ РФ и
представляет собой шаблон отчета, содержащий его общие характеристики, атрибуты,
операции.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

dimension – размерность формы, определенная ЦБ. Свойство имеет тип Object и
представляет собой объект класса RcbDimension.
id – идентификатор отчетной формы. Свойство имеет тип String и доступно только для
чтения.
name – наименование отчетной формы. Свойство имеет тип String и доступно только для
чтения.
summaryUnit – единицы сведения. Свойство имеет тип Object и представляет собой
объект класса RcbSummaryUnit.

**Методы:**

addAttribute (attributeId:String):Object

## Класс: `RcbIterator`

```rsl
RcbIterator()
```

Базовый класс итераторов.

**Методы:**

count ():Integer

## Класс: `RcbIteratorFilter`

```rsl
RcbIteratorFilter()
```

Базовый класс для фильтров итераторов.

**Методы:**

isSuitable(obj:Object):Bool

## Класс: `RcbIteratorSorter`

```rsl
RcbIteratorSorter()
```

Базовый класс для сортировщиков итераторов.

**Методы:**

isLess(lhs:Object, rhs:Object):Bool

## Класс: `RcbIteratorSynchronizer`

```rsl
RcbIteratorSynchronizer()
```

Базовый класс для синхронизаторов итераторов.

**Методы:**

addIterator(iterator:Object)

## Класс: `RcbKey`

```rsl
RcbKey()
```

Объект класса представляет собой ключ структуры. Объект определяет множество полей,
значения которых уникально идентифицируют составное значение атрибута среди
множества других составных значений этого атрибута.
Внимание!
Запрещено вводить в состав ключа поля с типом значения "Деньги"
или "Штуки".

**Свойства:**

fieldsCount – количество полей ключа. Свойство имеет тип Integer и доступно только для
чтения.
structure – ссылка на структуру, которой соответствует ключ. Свойство имеет тип Object
(RcbStructure
) и доступно только для чтения.

**Методы:**

addField (fieldId:String)

## Класс: `RcbKeyValue`

```rsl
RcbKeyValue()
```

## Класс: `RcbLinearCombination`

```rsl
RcbLinearCombination()
```

## Класс: `RcbLinearRelation`

```rsl
RcbLinearRelation()
```

## Класс: `RcbNode`

```rsl
RcbNode()
```

## Класс: `RcbNormalizer`

```rsl
RcbNormalizer()
```

## Класс: `RcbObjectFactory`

```rsl
RcbObjectFactory()
```

Объект класса позволяет создавать объекты подсистемы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Методы:**

createForm (formId:String):Object

## Класс: `RcbPeriod`

```rsl
RcbPeriod()
```

Объект класса представляет собой период времени. Период характеризуется датой
начала и датой окончания.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.
Конструктор класса RcbPeriod (beginDate:Date, endDate:Date) содержит следующие
параметры:
beginDate – дата начала периода.
endDate – дата окончания периода.

**Свойства:**

beginDate – дата начала периода; тип Date.
daysQuantity – количество дней в периоде; тип Integer.
endDate – дата окончания периода; тип Date.
kind – вид периода, значение вычисляется по датам начала и конца периода. Свойство
имеет тип Object, представляет собой объект класса RcbPeriodKind и доступно
только для чтения.

**Методы:**

isBelongTo (period:Object):Bool

## Класс: `RcbReport`

```rsl
RcbReport()
```

Объект 
класса 
описывает 
отчет 
(конкретную 
форму 
(RcbForm)) 
подсистемы
"Регламентируемой отчетности" со всеми заданными параметрами, необходимыми для
выпуска отчета (период отчета, номер отделения, режим выпуска, структура кредитной
организации, режим сведения и т.д.). Параметры выпуска отчета описываются классом
RcbReportContext
.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

context – контекст отчета. Свойство имеет тип Object, представляет собой объект класса
RcbReportContext
 и доступно только для чтения.
dimension – размерность значений атрибутов отчета. Свойство имеет тип Object и
представляет объект класса RcbDimension.
form – ссылка на отчетную форму, по которой создан отчет. Свойство имеет тип Object,
представляет собой объект класса RcbForm
 и доступно только для чтения.
isCalculated – признак расcчитанного отчета; тип Bool. Признак выставляется для отчета,
для которого успешно выполнена операция расчета или импорта.
isComplete – признак завершенного (законченного) отчета; тип Bool.

**Примечание:**

Завершенный отчет – это отчет с доступом только на чтение. Для такого
отчета запрещены модифицирующие операции типа "Расчет", "Импорт",
"Редактирование". Кроме того, запрещено изменение значений атрибутов из
списка атрибутов. Однако, запрет осуществляется исключительно на уровне
интерфейса - все операции доступны при использовании прикладного
программного интерфейса.
multiplier – множитель, определяющий размерность единиц измерения отчета; тип
Double.
normalizationAlgorithm – алгоритм нормализации, используемый в отчете. Свойство
имеет 
тип 
Object 
и 
представляет 
собой 
объект 
класса
RcbNormalizationAlgorithm.
previousPeriod – период предыдущего отчета. Свойство имеет тип Object и представляет
собой объект класса RcbReport.

**Примечание:**

Указанный период может использоваться как ссылка на отчет, который был
рассчитан перед текущим. Это необходимо для обеспечения различной
сходимости между данными текущего и предыдущего отчета (например, для
балансовых форм входящие остатки текущего отчета должны быть равны
исходящим остаткам предыдущего).

**Методы:**

attributeValue (attributeId:String):Object

## Класс: `RcbReportContext`

```rsl
RcbReportContext()
```

Объект класса содержит всю необходимую информацию для создания отчета по
конкретной форме: период, узел ТС, режим выпуска, организационная структура, признак
сводного отчета.
Конструктор 
класса 
RcbReportContext 
(period:Object, 
departmentCode:Integer,
issueMode:Integer, 
organizationStructure:Integer, 
isSummaryMode:Bool) 
содержит
следующие параметры:
period – период отчета (RcbPeriod
).
departmentCode – узел ТС, по которому выпускается отчет.
issueMode – режим выпуска отчета.
organizationStructure – организационная структура. Возможные значения:
· 1 – территориальная;
· 2 – региональная.
isSummaryMode – признак сводного отчета.

**Свойства:**

departmentCode – код узла территориальной структуры, по которому выпускается отчет.
Свойство имеет тип Integer и доступно только для чтения.
issueMode – режим выпуска отчета. Свойство имеет тип Integer и доступно только для
чтения. Возможные значения:
- 1 (Branch) – подразделение: в отчет включаются данные только по текущему
узлу выбранной организационной структуры;
- 2 (Department) – филиал: в отчет включаются данные по текущему узлу и по
всем подчиненным узлам типа ВСП по выбранной организационной структуре;
- 3 (Bank) – банк: в отчет включаются данные по текущему узлу и по всем
подчиненным узлам по выбранной организационной структуре.
Для каждого узла анализируется привилегия {0008} для проверки доступа к
данным узла.
isSummaryMode – режим работы со сводными данными. Свойство имеет тип Bool и
доступно только для чтения.
organizationStructure – организационная структура. Свойство имеет тип Integer и
доступно только для чтения. Возможные значения:
- 1 (territorial) – территориальная структура;
- 2 (regional) – региональная структура.
period – период отчета. Свойство имеет тип Object, представляет собой объект класса
RcbPeriod
 и доступно только для чтения.

## Класс: `RcbStructure`

```rsl
RcbStructure()
```

Объект класса описывает структуру, предназначенную для работы с атрибутами формы.
Выделяют следующие виды атрибутов:
· Простые атрибуты – имеют одно значение, определяемое характеристиками атрибута.
· Составные атрибуты – привязаны к одной из структур, заданных для формы.
Структура определяет составное значение атрибута: набор простых значений,
соответствующих полям структуры.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

form – ссылка на форму, к которой привязана структура. Свойство имеет тип Object,
представляет собой объект класса RcbForm
 и доступно только для чтения.
id – идентификатор структуры. Свойство имеет тип String и доступно только для чтения.
key – ключ структуры. Свойство имеет тип Object, представляет собой объект класса
RcbKey
 и доступно только для чтения.
name – наименование структуры. Свойство имеет тип String и доступно только для
чтения.

**Методы:**

addField (fieldId:String):Object

## Класс: `RcbStructureIterator`

```rsl
RcbStructureIterator()
```

Объект класса предназначен для итерирования структур формы. Используется для
навигации по коллекции структур формы.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

currentItem – текущий элемент коллекции структур. Свойство имеет тип Object и
представляет собой объект класса RcbStructure
.

**Пример:**

import RcbCoreInter;
var 
form 
=
RcbApplication().objectFactory.CreateForm("Балансовые
счета");
var structureIterator = form.CreateStructureIterator();
var structure = NULL;
var recordsCount = 0;
InitProgress(structureIterator.count);
structureIterator.MoveFirst();
while (not structureIterator.IsDone())
   structure = structureIterator.currentItem;
   Println(structure.name);
   recordsCount = recordsCount + 1;
   UseProgress(recordsCount);
   structureIterator.MoveNext();
end;
RemProgress();

**Методы:**

count():Integer

## Класс: `RcbSummator`

```rsl
RcbSummator()
```

Объект класса представляет собой сумматор, выполняющий сведение счетов.

**Методы:**

getSummarizedReportsList (report:Object):Tarray

## Класс: `RcbTransactionManager`

```rsl
RcbTransactionManager()
```

Объект класса позволяет сохранить или откатить все изменения, внесенные в
программную модель. Например, в макросе расчета отчета вычисляются значения
атрибутов отчета. Во время выполнения макроса произошло прерывание работы. В этом
случае, можно сохранить (либо не сохранять) результат всех вычислений.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Методы:**

commit () – метод предназначен для сохранения всех изменений, внесенных в базу
данных с момента последнего вызова методов commit или rollback.
rollback () – метод предназначен для отката всех изменений, сделанных с момента
последнего вызова методов commit или rollback.

## Класс: `RcbValue`

```rsl
RcbValue()
```

Объект класса представляет собой значение простого атрибута или поля составного
атрибута, используемое в подсистеме "Регламентируемая отчетность". Значение может
иметь такой тип как "Дата", "Штуки", "Деньги", "Число", "Проценты" или "Строка".

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

current – ссылка на точное или масштабированное значение (в зависимости от текущих
единиц измерения отчета: если в единицах национальной валюты, то exact, иначе
- scaled).
currentAsString – строковое представление текущего значения с учетом всех свойств
отчета и атрибута или поля структуры (точность, размерность и т.д.); тип String.
exact – значение в единицах национальной валюты. Тип свойства зависит от типа
значения (или поля структуры – для составного значения).
exactAsString – строковое представление точного значения с учетом всех свойств отчета
и атрибута или поля структуры (точность, размерность и т.д.); тип String.
scaled – значение в единицах измерения. Тип свойства зависит от типа значения (или
поля структуры – для составного значения).
scaledAsString – строковое представление масштабированного значения с учетом всех
свойств отчета и атрибута или поля структуры (точность, размерность и т.д.).

**Методы:**

isDefined():Bool

## Класс: `RcbValueIterator`

```rsl
RcbValueIterator()
```

Объект класса предназначен для итерирования значений составных атрибутов.
Используется для навигации по коллекции составных значений.

**Примечание:**

Объект данного класса нельзя явно создавать в RSL.

**Свойства:**

currentItem – текущее значение атрибута. Свойство имеет тип Object и представляет
собой объект класса RcbCompositeValue
.

**Методы:**

count ():Integer

## Класс: `RcbValueIteratorSynchronizer`

```rsl
RcbValueIteratorSynchronizer()
```

Объект класса предназначен для создания синхронизатора итератора по составным
значениям.
Конструктор 
класса 
RcbValueIteratorSynchronizer 
(kind:Object, 
sorter:Object,
iterator:Object) содержит следующие параметры:
kind – вид синхронизации (RcbIteratorSynchronizerKind).
sorter – сортировщик (RcbIteratorSorter
).
iterator – итератор (RcbIterator
). Для вида синхронизации RCB_ISK_OUTER_JOIN
является обязательным параметром. По умолчанию значение параметра равно
Null.

**Методы:**

addIterator(iterator:Object)

## Класс: `RepParameter`

```rsl
RepParameter()
```

## Класс: `RepParameterCollection`

```rsl
RepParameterCollection()
```

## Класс: `RepParameters`

```rsl
RepParameters()
```

## Класс: `RepOperdaysOpened`

```rsl
RepOperdaysOpened (departmentList:Object, beginDate:Date, endDate:Date)
```

## Класс: `RepOperdaysOpenedRecord`

```rsl
RepOperdaysOpenedRecord()
```

## Класс: `RepDocInfoServer`

```rsl
RepDocInfoServer (codeKind:Integer [, onlyDocFld:Integer] [, nameClientKind:Integer])
```

## Класс: `RepSqlQuery`

```rsl
RepSqlQuery([queryText:String]):Object
```


```rsl
представляет собой контейнер для параметризованного SQL-запроса. Применяется для наиболее эффективной работы механизма DocInfo (получение информации по документу). Объект класса хранит текст SQL-запроса, его параметры и их значения. Связывание параметров и текста запроса позиционное, т.е. параметры связываются с запросом в порядке их добавления в объект класса. Конструктор класса RepSqlQuery ([queryText:String]) имеет параметр queryText – необязательный текст SQL-запроса. Параметры запроса обозначаются символом "?".
```

**Пример:**

import Reporting;
/* Создание объекта RepSqlQuery с заданием текста SQL-
запроса*/
var queryWithText = RepSqlQuery(         "SELECT *"
                                 + "\n" + "  FROM
darhdoc_dbt"
                                 + "\n" + " WHERE
(t_account_payer = ? OR t_account_receiver = ?)"
                                 + "\n" + "   AND t_chapter
= ?"
                                 + "\n" + "   AND
t_date_carry BETWEEN ? AND ?"
                                 + "\n" + "   AND
t_result_carry != 23");
/* Создание объекта RepSqlQuery без задания текста SQL-
запроса*/
var queryWithoutText = RepSqlQuery();

**Свойства:**

value (name:String) – свойство задает значение параметра; name – уникальный
идентификатор параметра. Свойство имеет тип Variant и доступно только для
записи.

**Пример:**

import Reporting;
var query = RepSqlQuery("SELECT * FROM daccount_dbt WHERE
t_account LIKE ?");
query.addParameter("accountMask");
query.value("accountMask") = "40702%"

**Методы:**

addParameter (name:String [, value:Variant])

## Класс: `RepBranchFieldFilter`

```rsl
RepBranchFieldFilter (RepDepartmentList:Object)
```


```rsl
используется для фильтрации объектов по узлам типа ВСП (территориальная/региональная структура). Конструктор класса RepBranchFieldFilter (RepDepartmentList:Object) содержит параметр RepDepartmentList – класс списка головных подразделений.
```

**Пример:**

import reporting;
var 
departmentList 
=
RepDepartmentList( 
organizationStructure, 
issueMode,
{operDprt} );
var branchFieldFilter = RepBranchFieldFilter( departmentList
);

**Методы:**

GetAsSqlString (alias:String [, privilege:Integer]):String

## Класс: `RepPartyFilter`

```rsl
RepPartyFilter (departmentList:Object):Object
```


```rsl
предназначен для фильтрации субъектов по узлам типа ВСП (территориальная/региональная структура) с учетом вида обслуживания.
```

**Примечание:**

В подсистеме "Регламентируемая отчетность" для фильтрации субъектов
используется 
класс 
RcbPartyFilter, 
определенный 
в 
модуле 
…
\Mac\ReptReg\DepartmentFilter.mac. 
Интерфейс 
класса 
аналогичен
интерфейсу класса RepPartyFilter.
Конструктор 
класса 
RepPartyFilter 
(departmentList:Object) 
имеет 
параметр
departmentList – список узлов территориальной/региональной структуры, по которым
осуществляется 
фильтрация. 
Список 
узлов 
реализуется 
объектом 
класса
RepDeparmentList.

**Пример:**

import Reporting;
var 
RcbPartyFilterSingleton 
=
RepPartyFilter(RcbDepartmentList());

**Методы:**

getAsSqlString (partyIdFieldName:String, partyKind:Integer, String [, serviceKind:Integer,
String] [, beginDate:Date] [, endDate:Date] [, privilege:Integer]):String

## Процедура: `repQuietReport`

```rsl
repQuietReport (parameters:Object, String):String
```

## Процедура: `ПолучитьИнформациюПоДокументу`

```rsl
ПолучитьИнформациюПоДокументу (doc:File, Record, doc_inf:File, Record, ВидКода:Integer, [, РеквизитыНашегоБанка:Bool, Integer], [, ИспользоватьИсторию:Bool]):Integer
```

## Процедура: `ПолучитьНазваниеКлиента`

```rsl
ПолучитьНазваниеКлиента (val1:File, Record, val2:File, Record):Integer
```

## Процедура: `ПроверитьСчетПоМаске`

```rsl
ПроверитьСчетПоМаске (Счет:Integer, Маска:Integer):Integer
```

## Процедура: `ЦиклПоДокументам`

```rsl
ЦиклПоДокументам (Глава:Integer, НазваниеМакроФункции:Record, String [, Валюта:Integer] [, Филиал:Integer] [, ДатаНачала:Date] [, ДатаКонца:Date] [, РеквизитыНашегоБанка:Bool, Integer]):Integer
```

## Процедура: `RCB_FloorTerm`

```rsl
RCB_FloorTerm (value:Variant):Double
```

## Процедура: `SymbCreditCB`

```rsl
SymbCreditCB ([valForm:String], [valSymb:String], [valDateT:Date], [valDateB:Date]):MoneyL
```

## Процедура: `SymbDebetCB`

```rsl
SymbDebetCB ([valForm:String], [valSymb:String], [valDateT:Date], [valDateB:Date]):MoneyL)
```

## Процедура: `SymbForAccountCB`

```rsl
SymbForAccountCB ( valForm:String, valAcnt:String, valCurr:Integer):String
```

## Процедура: `SymbIsBotLevelCB`

```rsl
SymbIsBotLevelCB ([valForm:String], [valSymb:String]):Integer
```

## Процедура: `SymbRestCB`

```rsl
SymbRestCB ([valForm:String], [valSymb:String], [valDateT:Date], [valDateB:Date]):MoneyL
```

## Процедура: `ОкруглитьВТысячи`

```rsl
ОкруглитьВТысячи (val:Variant)
```

## Процедура: `ПогрешностьОкругления`

```rsl
ПогрешностьОкругления (val:Variant, val: Variant):MoneyL
```

## Процедура: `БалансовыйПредыдущегоПорядка`

```rsl
БалансовыйПредыдущегоПорядка ( value:String, [value:Integer]):String
```

## Процедура: `ПоЛицевомуСчету`

```rsl
ПоЛицевомуСчету (Val:Variant, Account:String, Type:String, Date1:Date [, Date2:Date]):Integer
```

## Процедура: `ПолучитьДанныеБаланса98`

```rsl
ПолучитьДанныеБаланса98 (DateBegin:Date, DateEnd:Date, Store:Variant, PeriodId:Integer):Bool
```

## Процедура: `ПорядокБалансовогоСчета`

```rsl
ПорядокБалансовогоСчета (value:String):Integer
```

## Процедура: `СчетаВКорреспонденции`

```rsl
СчетаВКорреспонденции (Сум:MoneyL, ВидСч:String, СчетД:String, СчетК:String, ДатаКонцаПериода:Date, [ДатаНачалаПериода:Date]):Variant
```

## Процедура: `ChangeVarActivPeriod`

```rsl
ChangeVarActivPeriod (form:Long, String, var:Long, String, bdInclude:Date, bdExclude:Date)
```

## Процедура: `ЗаписатьЗначениеПоля`

```rsl
ЗаписатьЗначениеПоля ( valFormName:String, valVarName:String, valFieldName:String, valBuff:String, Val:Variant):Bool
```


```rsl
помещает или изменяет в заданном поле переменной структурного типа указанное значение. Значение буфера предварительно должно быть получено вызовом функции ПрочитатьПеременную . Если значение буфера не определено или задана пустая строка, буфер инициализируется полями с неопределёнными значениями.
```

**Параметры:**

valFormName – имя формы.
valVarName – имя переменной.
valFieldName – имя поля.
valBuff – буфер значения переменной. Параметр может принимать значение типа Double,
Integer, MoneyL, String, Variant.
Val – значение поля.

**Возвращаемое значение:**



## Процедура: `ПрочитатьЗначениеПоля`

```rsl
ПрочитатьЗначениеПоля (valFormName:String, valVarName:String, valFieldName:String, valBuff:Object, valVal:Variant):Bool
```


```rsl
читает значение из буфера и возвращает его в качестве последнего параметра.
```

**Параметры:**

valFormName – имя формы.
valVarName – имя переменной.
valFieldName – имя поля.
valBuff – буфер значения переменной. Значение буфера должно быть предварительно
получено с помощью процедуры ПрочитатьПеременную
.
valVal – возвращаемое значение поля. Параметр может принимать значение типа Double,
MoneyL, String, Variant.

**Возвращаемое значение:**



## Процедура: `ПрочитатьЗначенияПеременных`

```rsl
ПрочитатьЗначенияПеременных ([valCheck:Integer], [NumDprt:Integer]):Bool
```

## Процедура: `ПрочитатьПеременную`

```rsl
ПрочитатьПеременную (valVal:Variant, valRepDate:Date, valPrevDate:Date, valForm:Variant, valVariable:Variant, [KeyID:Integer]):Bool
```

## Процедура: `ПрочитатьПеременную2`

```rsl
ПрочитатьПеременную2 (valR:Variant, valT:Variant, valRepDate:Date, valPrevDate:Date, valForm:Variant, valVariable:Variant):Bool
```

## Процедура: `СохранитьЗначенияПеременных`

```rsl
СохранитьЗначенияПеременных ([valCheck:Integer]):Integer
```

## Процедура: `СохранитьПеременную`

```rsl
СохранитьПеременную (valFormName:String, valDate:Date, valVal:Variant, valPrevDate:Date, valVarName:String, [valFlags:Integer]):Bool
```

## Процедура: `СохранитьПеременную2`

```rsl
СохранитьПеременную2 (valR:Variant valT:Variant, valDate:Date, valPrevDate:Date, valForm:String, valName:String, [valCheck:Integer]):Bool
```

## Процедура: `УдалитьЗначенияПеременных`

```rsl
УдалитьЗначенияПеременных ([val:Date, Integer, String], [val:Date, Integer, String], [val:Integer, String], [val:String], val:Integer):Integer
```

## Процедура: `ВнестиВСоставляющие`

```rsl
ВнестиВСоставляющие (Form:Integer, String, VarName:String, InForm:Integer, String, InVarName:String, Sort:Integer, Coeff:String, [Errcode:Integer], [ErrMess:String], [FlagPrevPeriod:Bool]):Bool
```

## Процедура: `ПолучитьВидПериода`

```rsl
ПолучитьВидПериода (DateBegin:Date, DateEnd:Date, [KindPeriodName:String]):Integer
```

## Процедура: `ПроверитьЕдиницыИзмерения`

```rsl
ПроверитьЕдиницыИзмерения ([Form:Variant])
```

## Процедура: `СвойстваОтчетнойФормы`

```rsl
СвойстваОтчетнойФормы (vBuff:Variant, vBuff:Object):Bool
```

## Процедура: `СвойстваПеременной`

```rsl
СвойстваПеременной (vForm:Variant, vVariable:Variant, vBuff:Object, [vIsMessage:Variant]):Bool
```

## Процедура: `СоздатьПеременную`

```rsl
СоздатьПеременную (vVar:String, vVar:Object, iErrorId:Integer, szErrMsgByff:String):Bool
```

## Процедура: `УдалитьПеременную`

```rsl
УдалитьПеременную (FormName:Variant, VarName:Variant, [ErrorCode:Integer], [ErrorDesc:String]):Bool
```

## Процедура: `АнонсироватьДаты`

```rsl
АнонсироватьДаты (val:Integer, val:String, val:String, val:Date, val:Date, val:Variant):Bool
```

## Процедура: `ВыбратьСохраненнДаты`

```rsl
ВыбратьСохраненныеДаты (val:Integer, val:String, val:String, val:Date, val:Date, [val:Integer]):Integer
```

## Процедура: `ДенонсироватьДаты`

```rsl
ДенонсироватьДаты (val:Integer, val:String, val:String, val:Date, val:Date):Integer
```

## Процедура: `ПолучитьДатыПредыдущегоПериода`

```rsl
ПолучитьДатыПредыдущегоПериода (val:Date, val:Date):Bool
```

## Процедура: `ПроверитьСохраненнДаты`

```rsl
ПроверитьСохраненнДаты (val:Integer, val:String, val:String, val:Date, val:Date; [val:Object]):Integer
```

## Процедура: `СписокОтчетовПоФорме`

```rsl
СписокОтчетовПоФорме (NumDprt:Integer, FormName:String, VarKind:String, RepDate:Date, PrevDate:Date):Bool
```

## Процедура: `ИнфоВыполненияВСтек`

```rsl
ИнфоВыполненияВСтек ()
```

## Процедура: `ИнфоВыполненияИзСтека`

```rsl
ИнфоВыполненияИзСтека ()
```

## Процедура: `ИнфоВосстановитьГлоб`

```rsl
ИнфоВосстановитьГлоб ()
```

## Процедура: `ИнфоЗадатьПодсистемеГлоб`

```rsl
ИнфоЗадатьПодсистемеГлоб ()
```

## Процедура: `УстановитьФлагВозврата`

```rsl
УстановитьФлагВозврата (val:Integer):Variant
```

## Процедура: `ЗначениеПоИмени`

```rsl
ЗначениеПоИмени (VarName:String):Variant
```

## Процедура: `ОтпуститьОперацию`

```rsl
ОтпуститьОперацию (Имя_формы:String, Вид_переменных:String, Название_операции:String):Integer
```

## Процедура: `ПроверитьРегистрациюОп`

```rsl
ПроверитьРегистрациюОп ( Имя_формы:String, Вид_переменных:String, Название_операции:String):Integer
```

## Процедура: `РегистрироватьОперацию`

```rsl
РегистрироватьОперацию (Имя_формы:String, Вид_переменных:String, Название_операции:String):Integer
```

## Процедура: `УстановитьЗначениеПоИмени`

```rsl
УстановитьЗначениеПоИмени (VarName:String, NewValue:String):Bool
```

## Процедура: `ПрочитатьСтруктурноеЗначение`

```rsl
ПрочитатьСтруктурноеЗначение (Буфер0, Название1:String, Значение2:Variant [, Название3, Значение4, ...]):Bool
```

## Процедура: `ПрочитатьСтруктурноеЗначение2`

```rsl
ПрочитатьСтруктурноеЗначение2 (buffer, fieldName:String, value1:Variant, value2:Variant, [fieldName:String], [value1:Variant], [value2:Variant]): Bool
```

## Процедура: `РассчитатьСтруктурныеЗначения`

```rsl
РассчитатьСтруктурныеЗначения (Дата0:Date, Дата1:Date, Variant, Форма2:Variant, Переменная3:Variant):Bool
```

## Процедура: `СохранитьСтруктурноеЗначение`

```rsl
СохранитьСтруктурноеЗначение (Буфер0:Object, Название1:String, Значение2:Variant [, Название3, Значение4, ...])
```

## Процедура: `СохранитьСтруктурноеЗначение2`

```rsl
СохранитьСтруктурноеЗначение2 (Буфер:File, Object, Record, fieldName:String, value1:DoubleL, MoneyL, String, value2:DoubleL, Variant, [fieldName:String], [value1:DoubleL, MoneyL, String], [value2:DoubleL, Variant]):Integer
```

## Процедура: `в`

```rsl
случае успешного завершения возвращает значение TRUE или сгенерированный номер типа Integer при добавлении нового значения. При возникновении ошибки возвращается значение FALSE.
```

**Пример:**

import ReptCbCommon;    /* СохранитьСтруктурноеЗначение2() 
   */
import cy_find; 
/* 
НайтиИдентификаторОтчетаПоНазванию()
*/ 
CONST 
formID 
= 
НайтиИдентификаторОтчетаПоНазванию
( {Название отчета} );
RECORD cy_mcomp ( "cy_mcomp.dbt","cy_files.def" );
ClearRecord( cy_mcomp );
var varName = "Ф118_итого";
var 
varId 
= 
НайтиИдентификаторПеременнойПоНазванию
( varName, formId );
cy_mcomp.iNumDprt   = НомерПодразделения;
cy_mcomp.bdRepDate  = ДатаОтчета;
cy_mcomp.bdPrevDate = ПредДатаОтчета;
cy_mcomp.iFormId    = FormID;
cy_mcomp.iVarId     = VarId;
cy_mcomp.iParentId  = 0;
cy_mcomp.iKeyId     = -1;
/* В первом случае поле "Сумма" действительного типа примет
значения 
  1500(в национальной валюте) и 2 в единицах измерения,
  если для формы установлены единицы измерения "Тысячи".
*/
/* (1) Пример автоматического расчета действительного поля
структурной переменной.
*/
var isSuccess = СохранитьСтруктурноеЗначение2( cy_mcomp,
"Сумма", 1500, NULL, "Заемщик", "Было дело", NULL );
/* 
(2) 
Пример 
явного 
задания 
действительного 
поля
структурной переменной.
*/
var isSuccess = СохранитьСтруктурноеЗначение2( cy_mcomp,
"Сумма", 1500, 1,    "Заемщик", "Было дело", NULL );

## Процедура: `УдалитьСтруктурныеЗначения`

```rsl
УдалитьСтруктурныеЗначения (Дата0:Date, Дата1:Date, Variant, Форма2:Variant, Переменная3:Variant, Номер4:Integer [, Флаг5:Integer]):Bool
```

## Процедура: `ПолучитьКаталогЭкспорта`

```rsl
ПолучитьКаталогЭкспорта ():String
```

## Процедура: `ПолучитьКаталогИмпорта`

```rsl
ПолучитьКаталогИмпорта ():String
```

## Процедура: `ПолучитьРеальныйНомерПлана`

```rsl
ПолучитьРеальныйНомерПлана ():Integer
```

## Процедура: `Ред_СписокЛицевыхТекст`

```rsl
Ред_СписокЛицевыхТекст (val:String, val:String, val:Integer, val:String, val:String):Bool
```

## Процедура: `ExecuteSystemOperation`

```rsl
ExecuteSystemOperation (operationNumber:Integer):Integer
```

## Процедура: `rcbQuietReport`

```rsl
rcbQuietReport (parameters:Object, String):String
```

## Процедура: `RANDOM`

```rsl
RANDOM (Parm):DoubleL
```

## Процедура: `SQRT`

```rsl
SQRT (Value:DoubleL, Integer, MoneyL):DoubleL
```

## Процедура: `ЗначениеВСтрокуЭкспорта`

```rsl
ЗначениеВСтрокуЭкспорта (ReturnString:String, VarName:String,):Bool
```

## Процедура: `ИмяФайлаОбменаДанными`

```rsl
ИмяФайлаОбменаДанными (FileName:String, DepartNumber: Integer, FormName:String, VarKind:Variant, Date:Date, IsExport:Bool):Bool
```

## Процедура: `ПолучитьОпределениеФайлаЭкспорта`

```rsl
ПолучитьОпределениеФайлаЭкспорта (SignStr:String, NumDprt:Integer, FormName:String, VarKind:String, DoubDate:String, Bool, Variant, BegDate:Date, EndDate:Date, [MakeDate:Date], [Version:Double, Integer], [VersPrefix:String], [VersSuffix:String], [Dimension:Integer]):Double
```

## Процедура: `ПоследняяОшибкаЭкспИмп`

```rsl
ПоследняяОшибкаЭкспИмп ():String
```

## Процедура: `ПроверитьИспользованиеДвухДат`

```rsl
ПроверитьИспользованиеДвухДат ( FormName:String, VarKind:String, IsDoubleDate:Integer):Bool
```

## Процедура: `РаскрытьОпределениеФайлаЭкспорта`

```rsl
РаскрытьОпределениеФайлаЭкспорта (SignStr:String, NumDprt:Integer, , VarKind:String, DoubDate:String, BegDate:Date, EndDate:Date, [MakeDate:Date], [Version:Double], [VersPrefix:String], [VersSuffix:String], [Dimension:Integer]):Double
```

## Процедура: `СтрокаИмпортаВЗначение`

```rsl
СтрокаИмпортаВЗначение (StringImp:String):Bool
```
