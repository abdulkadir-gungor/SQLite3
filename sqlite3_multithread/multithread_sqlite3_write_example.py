############################################################################
#
#   multithread_sqlite3_write_example.py [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  SQLite3DB import MultiThread_Db as sqlite3
#
#
db_name = "test.sqlite3"
sql_read_txt = "Select * from SimpleTablo;"
sql_write_txt = "Insert into SimpleTablo(Id, Name, Surname) values( {id}, '{name}', '{surname}' );"
#
db3 = sqlite3(db_name)
#
print()
print("\t[First] Data(s)")
print( ("\t"+("-"*50)) )
# sqlite3 read example
for id, name, surname in db3.db_read(sql_read_txt):
    res = "\tId:{id: <5} \tName:{name: <20} \tSurname:{surname: <20}".format(id=str(id), name=name, surname=surname)
    print(res)
# sql sentences
add_txt1 = sql_write_txt.format(id=7, name="Christopher", surname="Dickinson")
add_txt2 = sql_write_txt.format(id=8, name="Ferdinand", surname="Sentric")
# sqlite3 write
db3.db_write(add_txt1)
db3.db_write(add_txt2)
db3.db_save()
#
print()
print("\t[After Write] Data(s)")
print( ("\t"+("-"*50)) )
# sqlite read example
for id, name, surname in db3.db_read(sql_read_txt):
    res = "\tId:{id: <5} \tName:{name: <20} \tSurname:{surname: <20}".format(id=str(id), name=name, surname=surname)
    print(res)
#
# Optional
db3.db_close()