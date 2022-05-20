
# sqlite3_recovery
 
 Finds deleted data or remnants of deleted data in the file structure of SQLite3 database. If the number of columns in a table is given, it produces two log files. If omitted, it just generates a log file.
 1) %time_stamp%_raw_recovery_data.log (It is the file that contains the raw data states of the deleted data or the remains. It is produced in any case.)
 2) %time_stamp%_processed_recovery_data.log (If the number of columns in a table is given, it finds the deleted data in that table. If the header information of each deleted data is damaged, it may not identify that information. For this reason, the success rate of finding such deleted data decreases.)


The algorithm used by the program
---
Detects recorded data by reading the database file. It detects the bytes that are not related to the recorded data and writes them to the log file.

The Compiled Version of the Program Can be Downloaded from the Links Below.
---
<dl>
  <dt> (Executable) Sqlite3 Recovery
  <dd>
  <dd> sqlite3_recovery.rar --> zip password: "sqlite3_recovery"
  <dd> Link = https://drive.google.com/file/d/1FzenXC04iXa3efefbuqWDCVUs5aU460g/view?usp=sharing
</dl>

Requirements
---
Required libraries: pyinstaller

```
pip install pyinstaller
```

"pyinstaller" will be used to make the code one piece executable

Compilation
---

```
pyinstaller --onefile  --icon=main.ico main.py
```

Some Screenshot of the Working of the Program
---

**Screenshot [1]**

![s2](https://user-images.githubusercontent.com/71177413/169552825-378a2af3-07e7-4f86-8647-732e119a6caa.jpg)

**Screenshot [2]**

![s5](https://user-images.githubusercontent.com/71177413/169553043-d3f2c7fe-76ce-4e3f-8e33-5b2caa1345a4.jpg)

**Screenshot [3]**

![y10](https://user-images.githubusercontent.com/71177413/169553173-4e28c555-829d-433d-8c87-b56fdce1bcfe.JPG)


Legal Warning
---
Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.
