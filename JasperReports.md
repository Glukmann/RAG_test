---
title: JasperReports
description: JasperReports — генерация отчётов
category: JasperReports
source: PDF-документация RS-Bank V.6
sections: 2
generated: true
---

# JasperReports

## Введение

В АБС RS-Bank V.6 существует возможность формирования отчетов с помощью
инструмента Jasper Reports. Использование инструмента Jasper Reports предназначено
для снижения трудозатрат на реализацию печатных форм и повышение удобства их
разработки.
С помощью инструмента Jasper Reports отчет может быть выпущен в следующих форматах:
*.html, *.xlsx, *.docx, *.rtf, *.csv, *.odt.
При ссылке на информацию, расположенную в настоящем Руководстве, указывается номер
страницы (в скругленном прямоугольнике 
), соответствующий нужному Вам разделу, или
гиперссылка. Ссылка на раздел другого Руководства дается с указанием названия главы и
раздела, содержащего требуемую информацию.
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
Технология работы с JasperReports
Работа с JasperReports включает следующие этапы:
- Выполнение ряда настроек:
- Настройка файла rsjvm.ini
.
- Настройки реестра RS-Bank
.
- Разработку печатной формы с использованием JasperReports:
- Создание JavaBean-объектов
.
- Создание шаблона JRXML
.
- Создание отчета
.
Перечень каталогов, содержащих файлы JasperReports, представлен в приложении
"Файловый состав для инструмента JasperReports"
.
Настройка файла rsjvm.ini
Для корректной работы инструмента JasperReports в файле rsjvm.ini необходимо добавить
следующие строки:
JasperReports
PATH = ../Java/Common/jr/commons-beanutils-1.9.3.jar
PATH = ../Java/Common/jr/commons-collections-3.2.2.jar
PATH = ../Java/Common/jr/commons-digester-2.1.jar
PATH = ../Java/Common/jr/commons-lang3-3.7.jar
PATH = ../Java/Common/jr/itext-2.1.7.jar
PATH = ../Java/Common/jr/jasperreports-6.5.1.jar
PATH = ../Java/Common/jr
При хранении JavaBean-объектов в архивах необходимо указать путь к каждому архиву.
Настройки реестра RS-Bank
В реестре настроек RS-Bank необходимо:
- установить путь к макрофайлам ..\Mac\Jr в качестве значения настройки реестра
BANK_INI\ОБЩИЕ ПАРАМЕТРЫ\ДИРЕКТОРИИ\MACRODIR;
- установить путь к шаблонам JasperReports ..\Templs\Reporting\Report в качестве значения
настройки реестра BANK_INI\ОБЩИЕ ПАРАМЕТРЫ\ДИРЕКТОРИИ\TEMPLSDIR.
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
Создание JavaBean-объектов
Для получения данных, передаваемых в шаблон JasperReports
, используется генератор
JavaBean-объектов. В дистрибутиве системы для создания JavaBean-объектов реализован
системный модуль 10017 "Генератор объектов JavaBean"
.
Пример использования генератора JavaBean-объектов представлен в приложении
.
Использование пользовательского
интерфейса при создании
JavaBean-объектов
Генератор JavaBean-объектов (см. Рис. 1
) является вспомогательным инструментом,
позволяющим создать jar-файл с указанным именем, содержащим JavaBean-объект, по
переданному тексту sql-запроса. Поддерживается создание нескольких bean-объектов с
отношениями master-detail. Глубина детализации, как и количество detail-объектов на одном
уровне не ограничены.
быть добавлен в меню пользователя с помощью процедуры помодульного формирования
меню (см. раздел "Формирование меню пользователей" в главе "Организация работы с
использованием 
СУД" 
Руководства 
"Система 
управления 
доступом", 
файл
Books\ABS_Security\AccessControl.pdf).
Рис. 1. Генератор JavaBean-объектов.
При обращению к режиму можно настроить следующие параметры:
- название создаваемого JavaBean-объекта;
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
- название пакета, в котором создается JavaBean-объект (в дистрибутиве классы
реализованы в пакете beans);
- путь к java-файлу;
- путь к class-файлу;
- название jar-файла;
- путь к jar-файлу;
- текст sql-запроса.
Для генератора JavaBean-объектов действуют следующие ограничения:
- текст sql-запроса не должен превышать 4KB;
- нельзя генерировать иерархию master-detail.
Создание шаблона JRXML
Основой печатной формы отчета является шаблон, реализуемый в XML-файле
специального формата (JRXML). Файл может быть создан в текстовом редакторе или с
использованием специальных визуальных программ-дизайнеров. Технология разработки
печатной формы в контексте использования JasperReports в RS-Bank ориентирована на
создание шаблона именно в программе-дизайнере в связи с доступностью широкому кругу
пользователей.
Создание отчета
Для создания печатной формы отчета в дистрибутиве используется системный модуль
10018 "Генератор 
отчетов 
JasperReports"
 
и 
классы 
TJrReportGenerator 
и
TJrJavaBeanProcessor
.
Использование пользовательского
интерфейса при создании отчета
Генератор отчетов JasperReports (см. Рис. 2
), реализованный системным модулем
10018 – это  инструмент, позволяющий из текста sql-запроса, шаблона JRXML и JavaBean-
объекта получить печатную форму в разных форматах.
может быть добавлен в меню пользователя с помощью процедуры помодульного
формирования 
меню 
(см. 
раздел 
"Формирование 
меню 
пользователей" 
в 
главе
"Организация работы с использованием СУД" Руководства "Система управления доступом",
файл Books\ABS_Security\AccessControl.pdf).
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
Рис. 2. Генератор отчетов JasperReports.
При обращению к режиму можно настроить следующие параметры:
- название JavaBean-объекта;
- название пакета;
- название шаблона JasperReports;
- название файла отчета;
- формат файла отчета (может быть выбран из списка, содержащего возможные форматы);
- текст sql-запроса;
- RSL-код инициализации.
Для генератора отчетов действуют следующие ограничения:
- текст sql-запроса не должен превышать 4KB;
- параметр
RSL-код 
инициализации 
служит 
для 
задания 
параметров 
шаблона
JasperReports или runtime-библиотеки JasperReports. В это поле пишется код на RSL в
следующем формате:
m_generator.addParameter("имя_параметра_1", значение_параметра_1);
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
…
m_generator.addParameter("имя_параметра_N", значение_параметра_N);
Формирование печатной форма отчета
В разделе представлены, классы TJrReportGenerator
 и TJrJavaBeanProcessor
,
описанные на языке RSL, предназначенные для формирования печатной формы отчета.
TJrReportGenerator
Класс предназначен для создания печатной формы по переданному шаблону и источников
данных. Позволяет выполнить экспорт в форматы: txt, html, xls(x), rtf, csv, odt, ods, docx.
addParameter(name, value)
Процедура добавляет параметр с указанным именем и значением.
Параметры:
name – имя параметра.
value – значение параметра.
setDataSource(collection)
Процедура устанавливает источник данных – коллекции JavaBean-объектов.
Параметр:
collection – источник данных – коллекции JavaBean-объектов.
create(template)
Процедура создает печатную форму с использованием указанного шаблона.
Параметр:
template – шаблон печатной формы.
export(fileName, exportType)
Процедура выполняет экспорт печатной формы в указанный файл в заданном формате.
Параметры:
fileName – имя файла экспорта.
exportType – формат экспорта.
Технология работы с JasperReports
© АО Эр-Стайл Софтлаб, 2021-2025
TJrJavaBeanProcessor
Класс предназначен для формирования источника данных – коллекции JavaBean-объектов.
constructor(packageName, objectName)
Конструктор класса.
Параметры:
packageName – название пакета.
objectName – название JavaBean-объекта.
fillCollection(dataset[, detailBeansDatasetsFactory])
Процедура формирует источники данных по объекту, реализующему интерфейс
RsdDataset, или по тексту sql-запроса.
Параметры:
dataset – источник данных для master-объекта. В источнике данных для master-объекта
должны быть поля с именами, содержащими подстроку "$BC$". Значением таких
полей являются точные имена detail-объектов с учетом регистра в виде
<имя_пакета>.<имя_объекта>.
detailBeansDatasetsFactory – прикладной 
rsl-объект. 
Параметр 
используется 
для
создания источников данных, имеющих отношения master-detail. Для работы с
master-detail необходимы специальным образом сформированные источники
данных master-объектов. Источник данных (текст sql-запроса) detail-объекта
формируется 
в 
прикладном 
rsl-объекте 
(detailBeansDatasetsFactory),
содержащем метод getDataset(detailObjectName, rs). Метод получает название
detail-объекта JavaBean и текущую строку ИД master-объекта.
getDataSource()
Процедура предназначена для получения коллекции JavaBean-объектов.
© АО Эр-Стайл Софтлаб, 2021-2025

## Приложение

Файловый состав для инструмента
JasperReports
Файлы инструмента JasperReports располагаются в следующих каталогах:
- ..Java\Common\jr – директория для размещения java-архивов (jar) классов JasperReports и
необходимых сторонних библиотек:
- commons-beanutils-1.9.3.jar;
- commons-collections-3.2.2.jar;
- commons-digester-2.1.jar;
- commons-lang3-3.7.jar;
- itext-2.1.7.jar;
- jasperreports-6.5.1.jar.
- ..Java\Common\jr\beans
- 
директория 
для 
размещения 
java-архивов 
либо
скомпилированных классов JavaBean-объектов, используемых при формировании отчетов
JasperReports:
- AccRestsAccountBean.class;
- AccRestsReportBean.class.
- ..Java\Reporting\Jr – директория для размещения архивов с классами, являющимися
частью инструментария для работы с JasperReports:
jrtools.jar.
- ..Mac\Jr – директория для размещения макрофайлов, являющихся частью инструментария
для работы с JasperReports:
- JrCreateJavaBean.mac;
- JrDatasetNameParser.mac;
- JrFieldInfo.mac;
- JrJavaBeanProcessor.mac;
- JrJavaBeansGenerator.mac;
- JrReportBase.mac;
- JrReportGenerator.mac.
- ..Templs\Reporting\Report – директория для размещения шаблонов JasperReports,
используемых проектом RS-Reporting V6. Директория по мере необходимости может
дополняться поддиректориями:
AccRests.jasper.
© АО Эр-Стайл Софтлаб, 2021-2025
Пример использования генератора
JavaBean-объектов
/*
$Name:          JrCreateJavaBean.mac
$Module:        JasperReports
$Description:   Пример использования объекта TJrJavaBeansGenerator для создания
JavaBean-объекта
*/
import rsexts;
import JrJavaBeansGenerator;
private class TDetailBeansDatasetsFactory()
   macro getDataset(detailObjectName, rs)
       var queryText = "";
       if (detailObjectName == "beans.DetailBean01")
           queryText = "SELECT t_account,"
              + "\n" + "       (SELECT fi.t_fi_code FROM dfininstr_dbt fi
WHERE fi.t_fiId = t_code_currency) t_currency,"
              + "\n" + "       t_code_currency,"
              + "\n" + "       t_chapter,"
              + "\n" + "       'beans.SubdetailBean01' t_subdetailBean01_$BC$"
              + "\n" + "  FROM daccount_dbt"
              + "\n" + " WHERE t_chapter = " + rs.value("t_chapter")
              + "\n" + "   AND ROWNUM < 50"
       elif (detailObjectName == "beans.SubdetailBean01")
           queryText = "SELECT t_client * 1.0 t_activeRest"
              + "\n" + "  FROM daccount_dbt"
              + "\n" + " WHERE t_account = " + rs.value("t_account")
              + "\n" + "   AND t_chapter = " + rs.value("t_chapter")
              + "\n" + "   AND t_code_currency = " +
rs.value("t_code_currency")
              + "\n" + "   AND ROWNUM < 50"
       else
           queryText = "";
       end;
       return queryText;
   end;
end;
var sourcePath = "..\\txtfile";
var objectName = "ComplexBean"; // название объекта JavaBean
var jarName = "Jr"+objectName; // название jar-файла
var generatedSourcePath = sourcePath + "\\" + objectName; // путь к
создаваемому java-файлу с исходным кодом объекта JavaBean
var generatedClassPath = sourcePath + "\\" + objectName + "Class"; // путь к
скомпилированному java-файлу объекта JavaBean
var generatedJarPath = sourcePath; // путь к создаваемому jar-файлу
© АО Эр-Стайл Софтлаб, 2021-2025
var packageName = "beans"; // название пакета для объекта JavaBean
var generator = TJrJavaBeansGenerator(generatedSourcePath, generatedClassPath,
generatedJarPath, packageName);
var queryText = "SELECT 'Глава ' || t_chapter || '. ' || t_name AS
t_chapterName,"
             + "\n" + "       'beans.DetailBean01' AS t_detailBean01_$BC$,"
             + "\n" + "       t_chapter"
             + "\n" + "  FROM dobchaptr_dbt"
             + "\n" + " WHERE t_chapter = ANY(1,2,3,4,5)"
             + "\n" + " ORDER BY t_chapter"
             ;
var 
jarPath 
= 
generator.generate(queryText, 
objectName, 
jarName,
TDetailBeansDatasetsFactory());
private macro listDir(path, mask)
   var list = TArray();
   var dirList = TDirList(path + "\\" + mask);
   var i = 0;
   while (i < dirList.count)
       if (   (dirList.name(i) == ".")
           or (dirList.name(i) == "..")
          )
           i = i + 1;
           continue;
       end;
       if (dirList.isDir(i))
           for (var fn, listDir(path + "\\" + dirList.name(i), mask))
               list[list.size] = fn;
           end;
       else
           list[list.size] = path + "\\" + dirList.name(i);
       end;
       i = i + 1;
   end;
   return list;
end;
var compiledJavaPath = "";
if (generatedClassPath != "")
   for (var fn, listDir(generatedClassPath, "*.class"))
       compiledJavaPath = compiledJavaPath + "\n" + fn;
   end;
end;
var generatedSources = "";
for (var sfn, generator.getGeneratedSourceFileNames())
   generatedSources = generatedSources + "\n" + sfn;
end;
println("Созданы файлы:"
 +"\n"+jarPath
 +"\n"+compiledJavaPath
 +"\n"+generatedSources
     ); 
Алфавитный указатель
© АО Эр-Стайл Софтлаб, 2021-2025
Алфавитный
указатель
- A -
addParameter     11
- C -
constructor     12
create     11
- E -
export     11
- F -
fillCollection     12
- G -
getDataSource     12
- S -
setDataSource     11
- T -
TJrJavaBeanProcessor     12
TJrReportGenerator     11
Контактная информация
R-Style Softlab
http://www.softlab.ru/
Фактический адрес
117647, г. Москва, ул. Профсоюзная, д. 125А, 6 этаж
Связаться с нами можно по телефонам и электронной почте:
Сопровождение
т: (495) 796-9311; E-mail: support@softlab.ru
Корпоративные продажи
т: (495) 796-9310; E-mail: sales@softlab.ru
