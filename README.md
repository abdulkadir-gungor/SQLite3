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
  <dt> 3) Browsers &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[example: https://github.com/abdulkadir-gungor/DPAPI]   
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

**[1) sqlite3_multithread](.../sqlite3_multithread/README.md) :** Single-thread and multi-thread usage examples in sqlite3 projects in Python language

**[2) sqlite3_parser](.../sqlite3_multithread/README.md) :** It is an application that extracts recorded data and database information from SQLite3 files using b-tree algorithm. It does not process deleted data.

**[3) sqlite3_recovery](.../sqlite3_multithread/README.md) :** Finds deleted data or remnants of deleted data in the file structure of SQLite3 database.


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


sqlite3_parser
---
aaa

sqlite3_recovery
---
aaa


