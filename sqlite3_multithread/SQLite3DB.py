############################################################################
#
#   SQLite3DB.py [ Library File ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from threading import Thread
from queue import  Queue
import  sqlite3
#
#
#
# The database performs its operations in a single thread.
class SingleThread_DB(object):
    # class constructor
    def __init__(self, db_path):
        try:
            self.__connection = sqlite3.connect(db_path)
            self.__cursor     = self.__connection.cursor()
            self.__iscontinue = True
        except:
            self.__iscontinue = False
    # check error!
    def db_isError(self):
        return not self.__iscontinue
    # db "read" operations
    def db_read(self, req, arg=None):
        if self.__iscontinue:
            self.__cursor.execute(req, arg or tuple())
            for raw_data in self.__cursor:
                yield raw_data
    # db "write" or "execute" operations
    def db_write(self, req, arg=None):
        if self.__iscontinue:
            self.__cursor.execute(req, arg or tuple())
    # db "save" operations
    def db_save(self):
        if self.__iscontinue:
            self.__connection.commit()
    # db "close"
    def db_close(self):
        try:
            self.__cursor.close()
        except:
            pass
        try:
            self.__connection.close()
        except:
            pass
        self.__iscontinue = False
    # class destructor
    def __del__(self):
        self.db_close()
#
#
#
# The database performs its operations in multi threads.
class MultiThread_Db(Thread):
    # class constructor
    def __init__(self,db_path):
        try:
            super(MultiThread_Db,self).__init__()
            self.__db = db_path
            self.__reqs = Queue()
            self.__iscontinue = True
        except:
            self.__iscontinue = False
        #
        try:
            self.start()
        except:
            self.__iscontinue = False
    # check error!
    def db_isError(self):
        return not self.__iscontinue
    # thread run
    def run(self):
        try:
            connection = sqlite3.connect(self.__db)
            cursor = connection.cursor()
            #
            while self.__iscontinue:
                try:
                    req, arg, res = self.__reqs.get()
                    if req == 'DB_Close': break
                    if req == 'DB_Save':
                        connection.commit()
                    else:
                        cursor.execute(req, arg)
                        if res:
                            for rec in cursor:
                                res.put(rec)
                            res.put('raw_data_end')
                except:
                    break
            #
            try:
                cursor.close()
            except:
                pass
            try:
                connection.close()
            except:
                pass
        #
        except:
            pass
    # db "read" operations
    def db_read(self, req, arg=None):
        if self.__iscontinue:
            res=Queue()
            self.__reqs.put((req, arg or tuple(), res))
            while True:
                rec = res.get()
                if rec=='raw_data_end': break
                yield rec
        else:
            yield None
    # db "write" or "execute" operations
    def db_write(self, req, arg=None,res=None):
        if self.__iscontinue:
            self.__reqs.put((req, arg or tuple(), res))
    # db "save" operations
    def db_save(self):
        if self.__iscontinue:
            self.__reqs.put(('DB_Save', None, None))
    # db "close"
    def db_close(self):
        if self.__iscontinue:
            self.__reqs.put(('DB_Close', None, None))
        self.__iscontinue = False
    # class destructor
    def __del__(self):
        self.db_close()
        self.join()
