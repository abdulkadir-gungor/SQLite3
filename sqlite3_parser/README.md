# sqlite3_parser
Does not use ready-made sqlite3 libraries, instead reads the database file by parsing.It parses the sqlite3 file structure using the b-tree algorithm and saves it in a separate file. It does not process deleted data.

The algorithm used by the program
---

![x2](https://user-images.githubusercontent.com/71177413/169533189-3baf1067-c3e9-45e4-a97b-a1a434b07e1a.JPG)

![x5](https://user-images.githubusercontent.com/71177413/169535943-5ec01ccd-1405-4fe3-8e60-aa8b15e34742.JPG)


It first reads the database file in bytes. Parses read data according to sqlite database structure. Writes parsed data to "%time_stamp%_database.log" file.

The Compiled Version of the Program Can be Downloaded from the Links Below.
---
<dl>
  <dt> (Executable) Sqlite3 Parser
  <dd>
  <dd> sqlite3_parser.rar --> zip password: "sqlite3_parser"
  <dd> Link = https://drive.google.com/file/d/1JpVBakK6SbPSMnMIAoqp5EU5zlALY9Si/view?usp=sharing
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
