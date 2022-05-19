############################################################################
#
#   SQLite3_recovery (Analyzing SQlite3 Database) [ Library File ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  SQLite3_data import *
from SQLite3_func import varint, headertype, headervalue
#
#
#
class FoundData:
    # header (size) = [ (type) 1 byte, (page index) 4 bytes, (start index) 8 bytes,  (end index) 8 bytes, (data size) 8 bytes ]
    header = [1, 4, 8, 8, 8]
    #
    def __init__(self):
        self.d1_type = 0
        self.d2_page_index = 0
        self.d3_data_start_addr = 0
        self.d4_data_end_addr = 0
        self.d5_data_size = 0
#
class SQLite3_r_B00Page:
    def __init__(self, page_index:int, page_start_address:int, page_end_address:int, page_data:bytes ):
        self.d0_page_data_obj      = SQLite3_B00Page(index=page_index, data=page_data)
        self.d1_page_type          = 0
        self.d2_page_index         = page_index
        self.d3_page_start_address = page_start_address
        self.d4_page_end_address   = page_end_address
    #
    def process(self):
        found_data_list = []
        first_addr = self.d0_page_data_obj.x1_check_addr_end
        end_addr   = self.d0_page_data_obj.y2_data_start
        #
        if self.d2_page_index == 1:
            first_addr -= 100
            end_addr -= 100
            #
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            self.d0_page_data_obj = None
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj+1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type            = self.d1_page_type
                fdata.d2_page_index      = self.d2_page_index
                fdata.d3_data_start_addr = first_addr + tmp  + 100
                fdata.d4_data_end_addr   =  end_addr + 100
                fdata.d5_data_size       = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                #
                found_data_list.append(fdata)
            #
        else:
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            self.d0_page_data_obj = None
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj+1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type            = self.d1_page_type
                fdata.d2_page_index      = self.d2_page_index
                fdata.d3_data_start_addr = self.d3_page_start_address + first_addr + tmp
                fdata.d4_data_end_addr   = self.d3_page_start_address + end_addr
                fdata.d5_data_size       = fdata.d4_data_end_addr - fdata.d3_data_start_addr#
                found_data_list.append(fdata)
        #
        return found_data_list
#
class SQLite3_r_B02Page:
    def __init__(self, page_index:int, page_start_address:int, page_end_address:int, page_data:bytes ):
        self.d0_page_data_obj      = SQLite3_B02Page(index=page_index, data=page_data)
        self.d1_page_type          = 2
        self.d2_page_index         = page_index
        self.d3_page_start_address = page_start_address
        self.d4_page_end_address   = page_end_address
    #
    def process(self, txtencoding:str ):
        found_data_list = []
        first_addr = self.d0_page_data_obj.x1_check_addr_end
        end_addr   = self.d0_page_data_obj.y2_data_start
        #
        if self.d2_page_index == 1:
            first_addr -= 100
            end_addr   -= 100
            #
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            #
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = first_addr + tmp + 100
                fdata.d4_data_end_addr = end_addr + 100
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    data = SQLite3_B02Data()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes ) + 100
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                #
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        d1_start += 100
                        d1_end   += 100
                        d2_start += 100
                        d2_end   += 100
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr =  d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        #
                        d1_start += 100
                        d1_end   += 100
                        #
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr = end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
            #
        else:
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            tmp = -1
            #
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = self.d3_page_start_address + first_addr + tmp
                fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                #
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                #
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    #
                    data = SQLite3_B02Data()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        #
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes )
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
        #
        return found_data_list
#
class SQLite3_r_B05Page:
    def __init__(self, page_index:int, page_start_address:int, page_end_address:int, page_data:bytes ):
        self.d0_page_data_obj      = SQLite3_B05Page(index=page_index, data=page_data)
        self.d1_page_type          = 5
        self.d2_page_index         = page_index
        self.d3_page_start_address = page_start_address
        self.d4_page_end_address   = page_end_address
    #
    def process(self):
        found_data_list = []
        first_addr = self.d0_page_data_obj.x1_check_addr_end
        end_addr   = self.d0_page_data_obj.y2_data_start
        #
        if self.d2_page_index == 1:
            first_addr -= 100
            end_addr   -= 100
            #
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            #
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = first_addr + tmp + 100
                fdata.d4_data_end_addr = end_addr + 100
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    data = SQLite3_B05Data()
                    res = data.process( offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes ) + 100
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                #
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        d1_start += 100
                        d1_end   += 100
                        d2_start += 100
                        d2_end   += 100
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr =  d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        #
                        d1_start += 100
                        d1_end   += 100
                        #
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr = end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
            #
        else:
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            tmp = -1
            #
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = self.d3_page_start_address + first_addr + tmp
                fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                #
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                #
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    #
                    data = SQLite3_B05Data()
                    res = data.process(offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        #
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes )
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
        #
        return found_data_list
#
class SQLite3_r_B0APage:
    def __init__(self, page_index:int, page_start_address:int, page_end_address:int, page_data:bytes ):
        self.d0_page_data_obj      = SQLite3_B0APage(index=page_index, data=page_data)
        self.d1_page_type          = 10
        self.d2_page_index         = page_index
        self.d3_page_start_address = page_start_address
        self.d4_page_end_address   = page_end_address
    #
    def process(self, txtencoding:str):
        found_data_list = []
        first_addr = self.d0_page_data_obj.x1_check_addr_end
        end_addr   = self.d0_page_data_obj.y2_data_start
        #
        if self.d2_page_index == 1:
            first_addr -= 100
            end_addr   -= 100
            #
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            #
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = first_addr + tmp + 100
                fdata.d4_data_end_addr = end_addr + 100
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    data = SQLite3_B0AData()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes ) + 100
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                #
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        d1_start += 100
                        d1_end   += 100
                        d2_start += 100
                        d2_end   += 100
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr =  d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        #
                        d1_start += 100
                        d1_end   += 100
                        #
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr = end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
            #
        else:
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            tmp = -1
            #
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = self.d3_page_start_address + first_addr + tmp
                fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                #
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                #
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    #
                    data = SQLite3_B0AData()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        #
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes )
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
        #
        return found_data_list
#
class SQLite3_r_B0DPage:
    def __init__(self, page_index:int, page_start_address:int, page_end_address:int, page_data:bytes ):
        self.d0_page_data_obj      = SQLite3_B0DPage(index=page_index, data=page_data)
        self.d1_page_type          = 13
        self.d2_page_index         = page_index
        self.d3_page_start_address = page_start_address
        self.d4_page_end_address   = page_end_address
    #
    def process(self, txtencoding:str ):
        found_data_list = []
        first_addr = self.d0_page_data_obj.x1_check_addr_end
        end_addr   = self.d0_page_data_obj.y2_data_start
        #
        if self.d2_page_index == 1:
            first_addr -= 100
            end_addr   -= 100
            #
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            #
            tmp = -1
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = first_addr + tmp + 100
                fdata.d4_data_end_addr = end_addr + 100
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    data = SQLite3_B0DData()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes ) + 100
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                #
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        d1_start += 100
                        d1_end   += 100
                        d2_start += 100
                        d2_end   += 100
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr =  d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        #
                        d1_start += 100
                        d1_end   += 100
                        #
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = d1_end
                            fdata.d4_data_end_addr = end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
            #
        else:
            data_bytes = self.d0_page_data_obj.d0_bytes[first_addr:end_addr]
            tmp = -1
            #
            for jj in range(len(data_bytes)):
                if data_bytes[jj:jj + 1] != b'\x00':
                    tmp = jj
                    break
            #
            if tmp != -1:
                fdata = FoundData()
                fdata.d1_type = self.d1_page_type
                fdata.d2_page_index = self.d2_page_index
                fdata.d3_data_start_addr = self.d3_page_start_address + first_addr + tmp
                fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                #
                found_data_list.append(fdata)
            #
            if len(self.d0_page_data_obj.l0_addr_list) != 0:
                datalist = []
                for tmp_hex, tmp_int in self.d0_page_data_obj.l0_addr_list:
                    datalist.append(tmp_int)
                #
                self.d0_page_data_obj.l0_addr_list = []
                datalist.sort()
                #
                for tmp_int in datalist:
                    #
                    data = SQLite3_B0DData()
                    res = data.process(encode=txtencoding, offsetindex=tmp_int, pageindex=self.d2_page_index,
                                       pagedata=self.d0_page_data_obj.d0_bytes)
                    #
                    if res:
                        tmp_start_addr = data.d0_index[0]
                        tmp_end_addr = data.d0_index[1]
                        #
                        self.d0_page_data_obj.l0_addr_list.append([tmp_start_addr, tmp_end_addr])
                #
                end_addr  = len(self.d0_page_data_obj.d0_bytes )
                list_size = len(self.d0_page_data_obj.l0_addr_list)
                for jj in range( list_size):
                    if jj != (list_size-1):
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        d2_start, d2_end = self.d0_page_data_obj.l0_addr_list[jj+1]
                        #
                        if d1_end != d2_start:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + d2_start
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
                    #
                    else:
                        d1_start, d1_end = self.d0_page_data_obj.l0_addr_list[jj]
                        if d1_end != end_addr:
                            fdata = FoundData()
                            fdata.d1_type = self.d1_page_type
                            fdata.d2_page_index = self.d2_page_index
                            fdata.d3_data_start_addr = self.d3_page_start_address + d1_end
                            fdata.d4_data_end_addr = self.d3_page_start_address + end_addr
                            fdata.d5_data_size = fdata.d4_data_end_addr - fdata.d3_data_start_addr
                            #
                            found_data_list.append(fdata)
        #
        return found_data_list
# [ ... , foundData0 , foundData1, foundData2, ...] = undefinedRawData(db)
def undefinedRawData(db:str):
    with open(file=db, mode='rb') as frb:
        ofl = frb.read()
    #
    head = SQLite3Header(ofl).all()
    page_size = head[1]
    str_encoding = head[16]
    del head
    #
    pages = SQLite3Pages(ofl, page_size)
    r_data = []
    for page in pages.d1_all_pages:
        if page[3] == -1:
            if page[0] == 1:
                tmp = FoundData()
                tmp.d1_type = page[3]
                tmp.d2_page_index = page[0]
                tmp.d3_data_start_addr = page[1]
                tmp.d4_data_end_addr = page[2]
                tmp.d5_data_size = page_size - 100
            else:
                tmp = FoundData()
                tmp.d1_type = page[3]
                tmp.d2_page_index = page[0]
                tmp.d3_data_start_addr = page[1]
                tmp.d4_data_end_addr = page[2]
                tmp.d5_data_size = page_size
            r_data .append(tmp)
        #
        elif page[3] == 0:
            tmp = SQLite3_r_B00Page(page_index=page[0], page_start_address=page[1], page_end_address=page[2],
                                    page_data=ofl[page[1]:page[2]])
            r_data += tmp.process()
        elif page[3] == 2:
            tmp = SQLite3_r_B02Page(page_index=page[0], page_start_address=page[1], page_end_address=page[2],
                                    page_data=ofl[page[1]:page[2]])
            r_data += tmp.process(txtencoding=str_encoding)
        elif page[3] == 5:
            tmp = SQLite3_r_B05Page(page_index=page[0], page_start_address=page[1], page_end_address=page[2],
                                    page_data=ofl[page[1]:page[2]])
            r_data += tmp.process()
        elif page[3] == 10:
            tmp = SQLite3_r_B0APage(page_index=page[0], page_start_address=page[1], page_end_address=page[2],
                                    page_data=ofl[page[1]:page[2]])
            r_data += tmp.process(txtencoding=str_encoding)
        elif page[3] == 13:
            tmp = SQLite3_r_B0DPage(page_index=page[0], page_start_address=page[1], page_end_address=page[2],
                                    page_data=ofl[page[1]:page[2]])
            r_data += tmp.process(txtencoding=str_encoding)
    #
    return str_encoding, r_data
#
def readDbData(db:str, offset:int, datasize:int ):
    with open(file=db, mode="rb") as rfile:
        rfile.seek(offset)
        data = rfile.read(datasize)
    return data
#
#
def writeDbData(dbfile:str, outputfile:str,  listData:list, encoding:str="UTF-8"):
    with open(file=outputfile, mode='w', encoding=encoding) as wfile:
        wfile.write("\n")
        wfile.write("\tFilename : ")
        wfile.write(dbfile)
        wfile.write("\n")
        total = 0
        for data in listData:
            total += 1
            wfile.write("\n")
            wfile.write("\n")
            wfile.write("\t")
            wfile.write("-"*100)
            wfile.write("\n")
            wfile.write("\tData No      : ")
            wfile.write( str(total) )
            wfile.write("\n")
            wfile.write("\tPage index   : ")
            wfile.write(str(data.d2_page_index))
            wfile.write("\n")
            wfile.write("\tPage type    : ")
            if data.d1_type == -1:
                wfile.write("(unknown)")
            else:
                wfile.write( str(hex(data.d1_type)) )
            wfile.write("\n")
            wfile.write("\tData address : [ (int:")
            wfile.write(str(data.d3_data_start_addr))
            wfile.write("-")
            wfile.write(str(data.d4_data_end_addr))
            wfile.write(") (hex:")
            wfile.write(str(hex(data.d3_data_start_addr)))
            wfile.write("-")
            wfile.write(str(hex(data.d4_data_end_addr)))
            wfile.write(") ]")
            wfile.write("\n")
            wfile.write("\tData Size    : ")
            wfile.write(str(data.d5_data_size))
            wfile.write(" byte(s)")
            wfile.write("")
            wfile.write("\n")
            wfile.write("\t***) Data Content")
            #
            tmp_bytes = readDbData(dbfile, data.d3_data_start_addr, data.d5_data_size)
            txt0_template = "{0: ^4}"
            txt1_bytestring  = "\n\t[Representation of byte(s) as char]          | "
            txt1_hexadecimal = "\n\t[Representation of byte(s) as hexadecimal]   | "
            txt1_bytes_int   = "\n\t[Representation of byte(s) as int]           | "
            count = 0
            check_number = 16
            #
            for tmp_ii in tmp_bytes:
                count += 1
                if count  < check_number:
                    cc1 = int.to_bytes(tmp_ii,1,'big')
                    cc2 = cc1.__repr__()[2:-1]
                    txt1_bytestring  += txt0_template.format(cc2) + " | "
                    txt1_hexadecimal += txt0_template.format(str(hex(tmp_ii))) + " | "
                    txt1_bytes_int   += txt0_template.format(str(tmp_ii)) + " | "
                else:
                    if (count%check_number) == 1:
                        wfile.write(txt1_bytestring)
                        wfile.write(txt1_hexadecimal)
                        wfile.write(txt1_bytes_int)
                        wfile.write("\n")
                        #
                        txt1_bytestring  = "\n\t                                      (char) | "
                        txt1_hexadecimal = "\n\t                               (hexadecimal) | "
                        txt1_bytes_int   = "\n\t                                       (int) | "
                        #
                        cc1 = int.to_bytes(tmp_ii, 1, 'big')
                        cc2 = cc1.__repr__()[2:-1]
                        txt1_bytestring += txt0_template.format(cc2) + " | "
                        txt1_hexadecimal += txt0_template.format(str(hex(tmp_ii))) + " | "
                        txt1_bytes_int += txt0_template.format(str(tmp_ii)) + " | "
                    else:
                        cc1 = int.to_bytes(tmp_ii, 1, 'big')
                        cc2 = cc1.__repr__()[2:-1]
                        txt1_bytestring += txt0_template.format(cc2) + " | "
                        txt1_hexadecimal += txt0_template.format(str(hex(tmp_ii))) + " | "
                        txt1_bytes_int += txt0_template.format(str(tmp_ii)) + " | "
                #
            wfile.write(txt1_bytestring)
            wfile.write(txt1_hexadecimal)
            wfile.write(txt1_bytes_int)
            wfile.write("\n")
#
class RawData():
    #
    def __init__(self):
        self.d0_rawdata_addr       = 0
        self.d1_rawdata_size       = 0
        self.d2_rawdata_header_int = [ ] # [ ..., [head_size, head_value], ... ]
        self.d3_rawdata_values_size = [ ] # [ ..., [type value_size], ... ]
        self.d4_rawdata_values     = [ ] # [ ..., [type, value], ...]
#
def checkRawData(data:bytes, header_total_number:int, encoding:str):
    if (data is None) or (data == b''):
        return False, []
    #
    res_list = []
    data_bytes_size = len(data)
    #
    o_cell_offset   = -99
    o_cell_size     = -99
    o_cell_value    = -99
    #
    for jj in range(data_bytes_size):
        tmp_jj = data[jj:(jj+1)]
        if tmp_jj != b'\x00':
            counter = 1
            while True:
                tmp_jj = data[ (jj + counter - 1) : (jj + counter) ]
                if tmp_jj == b'':
                    break
                res, val = varint( data[jj:jj+counter] )
                if res > 0:
                    o_cell_offset = jj
                    o_cell_size   = res
                    o_cell_value  = val
                    break
                else:
                    counter += 1
            break
    #
    header_offset = o_cell_offset + o_cell_size
    if  o_cell_value < (3 + o_cell_size + 1) or (o_cell_value-3) > len(data[o_cell_offset:]):
            return False, res_list
    else:
        if header_total_number == 1:
            rrdata = RawData()
            rrdata.d0_rawdata_addr = o_cell_offset
            rrdata.d1_rawdata_size = o_cell_value - 3
            rrdata.d3_rawdata_values_size.append( [-1, (rrdata.d1_rawdata_size - o_cell_size)] )
            rrdata.d4_rawdata_values = [ ["Unknown", data[header_offset:]] ]
            res_list.append(rrdata)
            if (o_cell_value-3) != len(data[o_cell_offset:]):
                start = o_cell_offset + (o_cell_value-3)
                val1, res1 = checkRawData( data[start:], header_total_number, encoding)
                if val1:
                    if len(res1) != 0:
                        res_list += res1
        else:
            rrdata = RawData()
            rrdata.d0_rawdata_addr = o_cell_offset
            rrdata.d1_rawdata_size = o_cell_value - 3
            # header_offset
            offset = 0
            for ll in  range(header_total_number-1):
                counter = 0
                while True:
                    counter += 1
                    tmp_jj = data[ (header_offset + offset + counter - 1): (header_offset + offset + counter) ]
                    if tmp_jj == b'':
                        break
                    res, val = varint( data[ (header_offset + offset):(header_offset + offset + counter)] )
                    if res > 0:
                        offset += res
                        rrdata.d2_rawdata_header_int.append( [res, val] )
                        break
                    else:
                        counter += 1
                        if counter > 9:
                            return False, []
            rawdata_start = header_offset + offset
            header_0_val  = rrdata.d1_rawdata_size - (rawdata_start-3)
            values_size = []
            #
            for h_size, h_value in rrdata.d2_rawdata_header_int:
                size, type, comment = headertype(h_value)
                values_size.append( [type, size] )
                header_0_val -= size
            #
            if header_0_val < 1:
                return False, []
            #
            rrdata.d3_rawdata_values_size = [ [-1, header_0_val] ]
            rrdata.d3_rawdata_values_size += values_size
            del values_size
            #
            count = 0
            for ii in range(len(rrdata.d3_rawdata_values_size)):
                if ii == 0:
                    oo = rrdata.d3_rawdata_values_size[ii]
                    rrdata.d4_rawdata_values.append( ["Unknown", data[rawdata_start:(rawdata_start+oo[1] )] ])
                    count += oo[1]
                else:
                    oo = rrdata.d3_rawdata_values_size[ii]
                    res, val, type_int, type_str = headervalue(codecs=encoding, type=oo[0], data=data[(rawdata_start+count):(rawdata_start+count+oo[1])] )
                    rrdata.d4_rawdata_values.append( [type_str , val] )
                    count += oo[1]
            #
            res_list.append( rrdata )
            t_size = len(data)
            #
            if t_size < (rrdata.d0_rawdata_addr + rrdata.d1_rawdata_size):
                return False, []
            elif t_size == (rrdata.d0_rawdata_addr + rrdata.d1_rawdata_size):
                return True, res_list
            else:
                val2, list2 = checkRawData(data[(rrdata.d0_rawdata_addr + rrdata.d1_rawdata_size):],header_total_number, encoding)
                if val2:
                    if len(list2) != 0:
                        res_list += list2
    #
    return True, res_list
#
def checkRawDataList( r_data_list, header_total_number:int, db_file:str, encoding:str, filter_data_no=None, filter_page_index=None, filter_page_type=None):
    checkList = []
    #
    if  filter_data_no is not None:
        if len(filter_data_no) != 0:
            for tmp in filter_data_no:
                checkList.append( [tmp, r_data_list[(tmp-1)]]  )
    #
    if  filter_page_index is not None:
        if len(filter_page_index) != 0:
            for tmp in filter_page_index:
                data_no = 0
                for tmp_data in r_data_list:
                    data_no += 1
                    if tmp_data.d2_page_index == tmp:
                        checkList.append([data_no, tmp_data])

    #
    if  filter_page_type is not None:
        if len(filter_page_type) != 0:
            for tmp in filter_page_type:
                data_no = 0
                for tmp_data in r_data_list:
                    data_no += 1
                    if tmp_data.d1_type == tmp:
                        checkList.append([data_no, tmp_data])
    #
    if (filter_data_no is None) and (filter_page_index is None) and (filter_page_type is None):
        data_no = 0
        for tmp_data in  r_data_list:
            data_no += 1
            checkList.append([data_no, tmp_data])
    #
    res_list = []
    for data_no, tmp_data in checkList:
        tmp_bytes = readDbData(db_file, tmp_data.d3_data_start_addr, tmp_data.d5_data_size)
        #
        try:
            res, list1 = checkRawData(tmp_bytes, header_total_number, encoding)
            if res:
                if len(list1) != 0:
                    for tmp in list1:
                        res_list.append( [data_no,                     # Data No
                                          tmp_data.d1_type,            # Data Type
                                          tmp_data.d2_page_index,      # Page index
                                          tmp_data.d3_data_start_addr, # Page address
                                          tmp] )                       # Raw Data
        #
        except:
            pass
    #
    return res_list
#
def writeData(dbfile:str, outputfile:str,  listData:list, encoding:str="UTF-8"):
    with open(file=outputfile, mode='w', encoding=encoding) as wfile:
        wfile.write("\n")
        wfile.write("\tFilename : ")
        wfile.write(dbfile)
        w_temp = -1
        for tmp in listData:
            if w_temp != tmp[0]:
                wfile.write("\n\n")
                wfile.write("\tData No      : ")
                wfile.write( str(tmp[0]) )
                wfile.write("\n")
                wfile.write("\tPage Index   : ")
                wfile.write( str(tmp[2]) )
                wfile.write("\n")
                wfile.write("\tPage Type    : (hex:")
                wfile.write( str(hex(tmp[1])) )
                wfile.write(" (int:")
                wfile.write( str(tmp[1]) )
                wfile.write(")")
                wfile.write("\n")
                wfile.write("\tPage Address : (hex:")
                wfile.write( str(hex(tmp[3])) )
                wfile.write(") (int:")
                wfile.write( str(tmp[3]) )
                wfile.write(") \n\t***")
            wfile.write("\n\tData(s)      : ")
            for data_type, data in tmp[4].d4_rawdata_values:
                if (data_type == 'Unknown') or (data_type == 'Blob'):
                    wfile.write(" <")
                    wfile.write( str(data_type) )
                    wfile.write(">hexadecimal:")
                    wfile.write( str(data.hex(sep='-')) )
                    wfile.write("</")
                    wfile.write( str(data_type) )
                    wfile.write("> ")
                else:
                    wfile.write(" <")
                    wfile.write( str(data_type) )
                    wfile.write(">")
                    wfile.write( str(data) )
                    wfile.write("</")
                    wfile.write( str(data_type) )
                    wfile.write("> ")
            w_temp = tmp[0]

