# SQLite(3)
It is a github directory that covers projects such as sqlite3 database usage, operation and recovery of deleted data using Python language.

What is SQlite(3)?
---
SQLite(3) is an Open-Source database program that uses a sub-set of the SQL database descriptor language. SQlite(3) Databases are used for structured data storage and SQLit(3) is a popular database format appearing in many mobile systems as well as traditional operating systems

Areas where SQlite(3) database is used
---
<dl>
  <dt> 1) Android file systems
  <dd>
  <dd> a) Contacts = /data/data/com.android.providers.contacts/databases/contacts.db
  <dd> b) SMS = /data/data/com.android.providers.telephony/databases/mmssms.db
  <dd> c) Bookmarks = /data/data/com.android.browser/databases/browser.db
  <dd> ...
</dl>
 
<dl>
  <dt> 2) File system of mobile applications
  <dd>
  <dd> a) app_icons
  <dd> b) app_cache
  <dd> c) app_geolocation
  <dd> d) app_databases (whatsapp, Signal, Telegram, Wire, Skype ... )
  <dd> ...
</dl>

<dl>
  <dt> 3) Browsers &emsp; [example: https://github.com/abdulkadir-gungor/DPAPI]   
  <dd>
  <dd> a) Chrome
  <dd> b) Brave
  <dd> c) Opera
  <dd> d) Firefox
  <dd> e) Yandex
  <dd> ...
</dl>

<dl>
   <dt>4) Pc applications, Web apps, Raspberry Pi, ...
   <dd>
</dl>


Projects
---
**Proje Github Links**

**[1) sqlite3_multithread](/sqlite3_multithread/README.md) :** Single-thread and multi-thread usage examples in sqlite3 projects in Python language

**[2) sqlite3_parser](/sqlite3_parser/README.md) :** It is an application that extracts recorded data and database information from SQLite3 files using b-tree algorithm. It does not process deleted data.

**[3) sqlite3_recovery](/sqlite3_recovery/README.md) :** Finds deleted data or remnants of deleted data in the file structure of SQLite3 database.


sqlite3_multithread
---
<dl>
  <dt> File(s)
  <dd>
  <dd> SQLite3DB.py (It includes single-thread and multi-thread classes using SQLite3.)
  <dd> singlethread_sqlite3_read_example.py (Example of reading data from sqlite3 database using the single-threaded class)
  <dd> singlethread_sqlite3_write_example.py (Example of writing data from sqlite3 database using the single-threaded class)
  <dd> multithread_sqlite3_read_example.py (Example of reading data from sqlite3 database using the multi-threaded class)
  <dd> multithread_sqlite3_write_example.py(Example of writing data from sqlite3 database using the multi-threaded class)
  <dd> test.sqlite3 (Example sqlite3 database. Content can be viewed with sqlite3 browser)
</dl>


**Single-Thread**
![singlethread](https://user-images.githubusercontent.com/71177413/169505986-7f83e8ea-25d5-49d5-8395-022d5e900c65.JPG)


**Multi-Thread**
![multithread](https://user-images.githubusercontent.com/71177413/169506034-c75a070d-a5c4-459b-a63b-42adabe3087d.JPG)


**(Source) sqlite3_multithread**

&emsp;[sqlite3_multithread](/sqlite3_multithread/)

sqlite3_parser
---
Does not use ready-made sqlite3 libraries, instead reads the database file by parsing.It parses the sqlite3 file structure using the b-tree algorithm and saves it in a separate file. It does not process deleted data.

**Screenshot [1]**

![s1](https://user-images.githubusercontent.com/71177413/169509541-bfd91283-2e21-4afd-8c2e-49ee195df2af.JPG)

**Screenshot [2]**

![s3](https://user-images.githubusercontent.com/71177413/169512193-2b3acd3a-c460-4494-8d50-b6aa91bea867.JPG)

**(Source) Sqlite3 Parser**

&emsp;[sqlite3_parser](/sqlite3_parser/)

<dl>
  <dt> (Executable) Sqlite3 Parser
  <dd>
  <dd> sqlite3_parser.rar --> zip password: "sqlite3_parser"
  <dd> Link = https://drive.google.com/file/d/1JpVBakK6SbPSMnMIAoqp5EU5zlALY9Si/view?usp=sharing
</dl>

sqlite3_recovery
---
 Finds deleted data or remnants of deleted data in the file structure of SQLite3 database. If the number of columns in a table is given, it produces two log files. If omitted, it just generates a log file.
 1) %time_stamp%_raw_recovery_data.log (It is the file that contains the raw data states of the deleted data or the remains. It is produced in any case.)
 2) %time_stamp%_raw_recovery_data.log (If the number of columns in a table is given, it finds the deleted data in that table. If the header information of each deleted data is damaged, it may not identify that information. For this reason, the success rate of finding such deleted data decreases.)

**Screenshot [1]**

![s2](https://user-images.githubusercontent.com/71177413/169513058-a82bb6ff-5467-42e3-a739-61b321e17b2c.jpg)

**Screenshot [2]**

![s5](https://user-images.githubusercontent.com/71177413/169516775-1ff1cfc1-b205-4d53-a7e2-88da63a39412.jpg)

**(Source) Sqlite3 Recovery**

&emsp;[sqlite3_recovery](/sqlite3_recovery/)

<dl>
  <dt> (Executable) Sqlite3 Recovery
  <dd>
  <dd> sqlite3_recovery.rar --> zip password: "sqlite3_recovery"
  <dd> Link = https://drive.google.com/file/d/1FzenXC04iXa3efefbuqWDCVUs5aU460g/view?usp=sharing
</dl>

Legal Warning
---
Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.
