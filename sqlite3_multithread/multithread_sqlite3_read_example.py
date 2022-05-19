############################################################################
#
#   multithread_sqlite3_read_example.py [ Main Program ]
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
#
db3 = sqlite3(db_name)
#
print()
print("\tData(s)")
print( ("\t"+("-"*50)) )
# sqlite read example
for id, name, surname in db3.db_read(sql_read_txt):
    res = "\tId:{id: <5} \tName:{name: <20} \tSurname:{surname: <20}".format(id=str(id), name=name, surname=surname)
    print(res)
#
# Optional
db3.db_close()
