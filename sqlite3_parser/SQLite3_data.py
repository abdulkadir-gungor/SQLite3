############################################################################
#
#   SQLite3_data.py (Analyzing SQlite3 Database) [ Library File ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from SQLite3_func import *
#
# (Template) SQLite3HeaderData
class SQLite3HeaderData:
    def __init__(self):
        self.d01_header_signature = [0, 16, 16, "The header signature string"]
        self.d02_page_size = [16, 18, 2, "The database page size in bytes"]
        self.d03_file_format_w_version = [18, 19, 1, "File format write version"]
        self.d04_file_format_r_version = [19, 20, 1, "File format read version"]
        self.d05_reserved = [20, 21, 1, "Bytes of unused 'reserved' space at the end of each page"]
        self.d06_max_emb_frac = [21, 22, 1, "Maximum embedded payload fraction" ]
        self.d07_min_emb_frac = [22, 23, 1, "Minimum embedded payload fraction" ]
        self.d08_leaf_payload_frac = [23, 24, 1, "Leaf payload fraction"]
        self.d09_file_change_counter = [24, 28, 4, "File change counter"]
        self.d10_page_size = [28, 32, 4 ,"Size of the database file in pages"]
        self.d11_page_total_number = [32, 36, 4, "Page number of the first freelist trunk page"]
        self.d12_free_total_number = [36, 40, 4, "Total number of freelist pages"]
        self.d13_schema_cookie = [40, 44, 4, "The schema cookie"]
        self.d14_schema_format_number = [44, 48, 4, "The schema format number"]
        self.d15_page_cache_size = [48, 52, 4, "Default page cache size"]
        self.d16_vacuum = [52, 56, 4, "Auto/incremental-vacuum page number"]
        self.d17_text_encoding = [56, 60, 4, "The database text/str encoding" ]
        self.d18_user_version = [60, 64, 4, "User version number"]
        self.d19_incvacuum = [64, 68, 4, "Incremental-vacuum mode" ]
        self.d20_application_id = [68, 72, 4, "Application ID" ]
        self.d21_reserved = [72, 92, 20, "Reserved for expansion"]
        self.d22_version_valid_number = [92, 96, 4, "The version-valid-for number" ]
        self.d23_sqlite_version_number = [96, 100, 4, "Sqlite version number" ]
    #
    def all(self):
        return [self.d01_header_signature,
                self.d02_page_size,
                self.d03_file_format_w_version,
                self.d04_file_format_r_version,
                self.d05_reserved,
                self.d06_max_emb_frac,
                self.d07_min_emb_frac,
                self.d08_leaf_payload_frac,
                self.d09_file_change_counter,
                self.d10_page_size,
                self.d11_page_total_number,
                self.d12_free_total_number,
                self.d13_schema_cookie,
                self.d14_schema_format_number,
                self.d15_page_cache_size,
                self.d16_vacuum,
                self.d17_text_encoding,
                self.d18_user_version,
                self.d19_incvacuum,
                self.d20_application_id,
                self.d21_reserved,
                self.d22_version_valid_number,
                self.d23_sqlite_version_number]
    #
    def d01(self):
        return self.d01_header_signature
    #
    def d02(self):
        return self.d02_page_size
    #
    def d03(self):
        return self.d03_file_format_w_version
    #
    def d04(self):
        return self.d04_file_format_r_version
    #
    def d05(self):
        return self.d05_reserved
    #
    def d06(self):
        return self.d06_max_emb_frac
    #
    def d07(self):
        return self.d07_min_emb_frac
    #
    def d08(self):
        return self.d08_leaf_payload_frac
    #
    def d09(self):
        return self.d09_file_change_counter
    #
    def d10(self):
        return self.d10_page_size
    #
    def d11(self):
        return self.d11_page_total_number
    #
    def d12(self):
        return self.d12_free_total_number
    #
    def d13(self):
        return self.d13_schema_cookie
    #
    def d14(self):
        return self.d14_schema_format_number
    #
    def d15(self):
        return self.d15_page_cache_size
    #
    def d16(self):
        return self.d16_vacuum
    #
    def d17(self):
        return self.d17_text_encoding
    #
    def d18(self):
        return self.d18_user_version
    #
    def d19(self):
        return self.d19_incvacuum
    #
    def d20(self):
        return self.d20_application_id
    #
    def d21(self):
        return self.d21_reserved
    #
    def d22(self):
        return self.d22_version_valid_number
    #
    def d23(self):
        return self.d23_sqlite_version_number
#
# (Process) SQlite3Header
class SQLite3Header:
    def __init__(self, data:bytes):
        if len(data) > 99:
            ii = SQLite3HeaderData().all()
            self.d01_header_signature = data [ii[0][0]:ii[0][1]].decode(encoding='UTF-8')
            #
            tmp = data[ii[1][0]:ii[1][1]]
            if big_endian_to_int(tmp) == 1:
                self.d02_page_size = 65536
            else:
                self.d02_page_size = big_endian_to_int(tmp)
            #
            tmp = big_endian_to_int( data[ii[2][0]:ii[2][1]] )
            if tmp == 1:
                self.d03_file_format_w_version = "Legacy"
            elif tmp == 2:
                self.d03_file_format_w_version = "WAL"
            else:
                self.d03_file_format_w_version = "Error!"
            #
            tmp = big_endian_to_int(data[ii[3][0]:ii[3][1]])
            if tmp == 1:
                self.d04_file_format_r_version = "Legacy"
            elif tmp == 2:
                self.d04_file_format_r_version = "WAL"
            else:
                self.d04_file_format_r_version = "Error!"
            #
            tmp = data[ii[4][0]:ii[4][1]]
            if tmp == b'\x00':
                self.d05_reserved = 0
            else:
                self.d05_reserved = -1
            #
            tmp = big_endian_to_int( data[ii[5][0]:ii[5][1]] )
            if tmp == 64:
                self.d06_max_emb_frac = tmp
            else:
                self.d06_max_emb_frac = -1
            #
            tmp = big_endian_to_int( data[ii[6][0]:ii[6][1]] )
            if tmp == 32:
                self.d07_min_emb_frac = 32
            else:
                self.d07_min_emb_frac = -1
            #
            tmp = big_endian_to_int( data[ii[7][0]:ii[7][1]] )
            if tmp == 32:
                self.d08_leaf_payload_frac = 32
            else:
                self.d08_leaf_payload_frac = -1
            #
            self.d09_file_change_counter = big_endian_to_int( data[ii[8][0]:ii[8][1]] )
            self.d10_page_size = big_endian_to_int( data[ii[9][0]:ii[9][1]] )
            self.d11_page_total_number = big_endian_to_int( data[ii[10][0]:ii[10][1]] )
            self.d12_free_total_number = big_endian_to_int( data[ii[11][0]:ii[11][1]] )
            self.d13_schema_cookie = big_endian_to_int( data[ii[12][0]:ii[12][1]] )
            #
            tmp = big_endian_to_int(data[ii[13][0]:ii[13][1]])
            if   tmp == 1:
                self.d14_schema_format_number = "Version 3.0.0 (2004-06-18)"
            elif tmp == 2:
                self.d14_schema_format_number = "Version 3.1.3 (2005-02-20)"
            elif tmp == 3:
                self.d14_schema_format_number = "Version 3.1.4 (2005-03-11)"
            elif tmp == 4:
                self.d14_schema_format_number = "Version 3.3.3 (2006-01-10)"
            else:
                self.d14_schema_format_number = "{"+str(tmp)+"} Unknown"
            #
            self.d15_page_cache_size = big_endian_to_int(data[ii[14][0]:ii[14][1]])
            self.d16_vacuum = big_endian_to_int(data[ii[15][0]:ii[15][1]])
            #
            tmp = big_endian_to_int(data[ii[16][0]:ii[16][1]])
            if tmp == 1:
                self.d17_text_encoding = "UTF-8"
            elif tmp == 2:
                self.d17_text_encoding = "UTF-16LE"
            elif tmp == 3:
                self.d17_text_encoding = "UTF-16BE"
            else:
                self.d17_text_encoding = ""
            #
            self.d18_user_version = big_endian_to_int(data[ii[17][0]:ii[17][1]])
            self.d19_incvacuum = big_endian_to_int(data[ii[18][0]:ii[18][1]])
            #
            tmp = data[ii[19][0]:ii[19][1]]
            if tmp == b'\x00\x00\x00\x00': # 0x00000000
                self.d20_application_id = "SQLite3 database"
            elif tmp == b'\x0f\x05\x51\x12': # 0x0f055112
                self.d20_application_id = "Fossil checkout"
            elif tmp == b'\x0f\x05\x51\x13': # 0x0f055113
                self.d20_application_id = "Fossil global configuration"
            elif tmp == b'\x0f\x05\x51\x11': # 0x0f055111
                self.d20_application_id = "Fossil repository"
            elif tmp == b'\x42\x65\x44\x62': # 0x42654462
                self.d20_application_id = "Bentley Systems BeSQLite Database"
            elif tmp == b'\x42\x65\x4c\x6e': # 0x42654c6e
                self.d20_application_id = "Bentley Systems Localization File"
            elif tmp == b'\x5f\x4d\x54\x4e': # 0x5f4d544e
                self.d20_application_id = "Monotone source repository"
            elif tmp == b'\x47\x50\x4b\x47': # 0x47504b47
                self.d20_application_id = "OGC GeoPackage file"
            elif tmp == b'\x47\x50\x31\x30': # 0x47503130
                self.d20_application_id = "OGC GeoPackage version 1.0 file"
            elif tmp == b'\x45\x73\x72\x69': # 0x45737269
                self.d20_application_id = "Esri Spatially-Enabled Database"
            elif tmp == b'\x4d\x50\x42\x58': # 0x4d504258
                self.d20_application_id = "MBTiles tileset"
            else:
                self.d20_application_id = ""
            #
            self.d21_reserved = big_endian_to_int(data[ii[20][0]:ii[20][1]])
            self.d22_version_valid_number = big_endian_to_int(data[ii[21][0]:ii[21][1]])
            #
            tmp = big_endian_to_int(data[ii[22][0]:ii[22][1]])
            mm = int( tmp / 1000000)
            bb = int( (tmp%100000)/1000 )
            cc = tmp % 1000
            self.d23_sqlite_version_number = "{mm:02d}.{bb:02d}.{cc:03d}".format(mm=mm,bb=bb,cc=cc)
    #
    def all(self):
        return [ self.d01_header_signature,
                 self.d02_page_size,
                 self.d03_file_format_w_version,
                 self.d04_file_format_r_version,
                 self.d05_reserved,
                 self.d06_max_emb_frac,
                 self.d07_min_emb_frac,
                 self.d08_leaf_payload_frac,
                 self.d09_file_change_counter,
                 self.d10_page_size,
                 self.d11_page_total_number,
                 self.d12_free_total_number,
                 self.d13_schema_cookie,
                 self.d14_schema_format_number,
                 self.d15_page_cache_size,
                 self.d16_vacuum,
                 self.d17_text_encoding,
                 self.d18_user_version,
                 self.d19_incvacuum,
                 self.d20_application_id,
                 self.d21_reserved,
                 self.d22_version_valid_number,
                 self.d23_sqlite_version_number ]
    #
    def d01(self):
        return self.d01_header_signature
    #
    def d02(self):
        return self.d02_page_size
    #
    def d03(self):
        return self.d03_file_format_w_version
    #
    def d04(self):
        return self.d04_file_format_r_version
    #
    def d05(self):
        return self.d05_reserved
    #
    def d06(self):
        return self.d06_max_emb_frac
    #
    def d07(self):
        return self.d07_min_emb_frac
    #
    def d08(self):
        return self.d08_leaf_payload_frac
    #
    def d09(self):
        return self.d09_file_change_counter
    #
    def d10(self):
        return self.d10_page_size
    #
    def d11(self):
        return self.d11_page_total_number
    #
    def d12(self):
        return self.d12_free_total_number
    #
    def d13(self):
        return self.d13_schema_cookie
    #
    def d14(self):
        return self.d14_schema_format_number
    #
    def d15(self):
        return self.d15_page_cache_size
    #
    def d16(self):
        return self.d16_vacuum
    #
    def d17(self):
        return self.d17_text_encoding
    #
    def d18(self):
        return  self.d18_user_version
    #
    def d19(self):
        return  self.d19_incvacuum
    #
    def d20(self):
        return self.d20_application_id
    #
    def d21(self):
        return self.d21_reserved
    #
    def d22(self):
        return self.d22_version_valid_number
    #
    def d23(self):
        return  self.d23_sqlite_version_number
#
# Detect SQLite3Pages
class SQLite3Pages:
    def __init__(self, data:bytes, pagesize):
        self.d1_all_pages = []
        self.d2_b00_pages = []
        self.d3_b02_pages = []
        self.d4_b05_pages = []
        self.d5_b0a_pages = []
        self.d6_b0d_pages = []
        self.d7_bff_pages = []
        #
        size = len(data)
        if size >= pagesize:
            type_int = -1
            type_str = "Unknown"
            if data[100:101] == b'\x00':
                type_int = 0
                type_str = "Free page"
                self.d2_b00_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
            elif data[100:101] == b'\x02':
                type_int = 2
                type_str = "An interior index page"
                self.d3_b02_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
            elif data[100:101] == b'\x05':
                type_int = 5
                type_str = "An interior table page"
                self.d4_b05_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
            elif data[100:101] == b'\x0A':
                type_int = 10
                type_str = "A leaf index page"
                self.d5_b0a_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
            elif data[100:101] == b'\x0D':
                type_int = 13
                type_str = "A leaf table page"
                self.d6_b0d_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
            else:
                self.d7_bff_pages.append( [1, 100, pagesize] )
                self.d1_all_pages.append([1,  100, pagesize,  type_int, type_str])
        #
        counter = 0
        while True:
            counter += 1
            start = counter * pagesize
            end   = (counter + 1) * pagesize
            if size < end:
                break
            else:
                type_int = -1
                type_str = "Unknown"
                hh = counter + 1
                if data[start:start+1] == b'\x00':
                    type_int = 0
                    type_str = "Free page"
                    self.d2_b00_pages.append([hh ,start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
                elif data[start:start+1] == b'\x02':
                    type_int = 2
                    type_str = "An interior index page"
                    self.d3_b02_pages.append([hh, start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
                elif data[start:start+1] == b'\x05':
                    type_int = 5
                    type_str = "An interior table page"
                    self.d4_b05_pages.append([hh, start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
                elif data[start:start+1] == b'\x0A':
                    type_int = 10
                    type_str = "A leaf index page"
                    self.d5_b0a_pages.append([hh, start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
                elif data[start:start+1] == b'\x0D':
                    type_int = 13
                    type_str = "A leaf table page"
                    self.d6_b0d_pages.append([hh, start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
                else:
                    self.d7_bff_pages.append([hh, start, end])
                    self.d1_all_pages.append([hh, start, end, type_int, type_str])
#
#
class SQLite3_B00Page:
    def __init__(self, index:int, data:bytes ):
        self.d0_bytes = data
        self.d0_index = index
        self.d1_00_page_header = [ 0, 1, 1, data[0:1].hex(), big_endian_to_int(data[0:1]), "Page header signature" ]
        self.d2_01_free_block_offset = [1, 3, 2, data[1:3].hex(), big_endian_to_int(data[1:3]), "Free block offset address" ]
        self.d3_03_number_of_cell = [3, 5, 2, data[3:5].hex(), big_endian_to_int(data[3:5]), "Number of cell" ]
        self.d4_05_cell_offset = [5, 7, 2, data[5:7].hex(), big_endian_to_int(data[5:7]), "Cell block offset address" ]
        self.d5_07_number_of_free = [7, 8, 1, data[7:8].hex(), big_endian_to_int(data[7:8]), "Number of free"]
        self.l0_addr_list = list()
        self.l1_total_addr_list = list()
        self.l2_check_addr_list = list()
        #
        ee = 4
        rr = 8
        jj = 0
        for ii in  range(self.d5_07_number_of_free[4]):
            jj = rr + ii * ee
            rem = big_endian_to_int(data[jj:jj + ee])
            self.l0_addr_list.append( [data[jj:jj+ee].hex(), rem] )
        #
        if self.d0_index == 1:   # First Page
            if jj == 0:          # if there is no data
                self.y1_addr_end   =  rr + 100
                self.y2_data_start =  (len(data)) + 100
            else:                # if there is data
                self.y1_addr_end   =  jj + ee + 100
                self.y2_data_start =  (len(data))
        else:                    # Other Page(s)
            self.y1_addr_end   =  jj + ee
            self.y2_data_start =  (len(data))
        #
        big_int = lambda n1, n2: n1 if n1 > n2 else n2
        pp = big_int(self.d3_03_number_of_cell[4], self.d5_07_number_of_free[4])
        for ii in  range(pp):
            jj = rr + ii * ee
            self.l1_total_addr_list.append( [data[jj:jj+ee].hex(), big_endian_to_int(data[jj:jj+ee])] )
        #
        if index == 1:
            size = len(data) + 100
        else:
            size = len(data)
        jj = rr
        while True:
            ###
            if jj+ee > size:
                break
            tmp = data[jj:jj+ee]
            ###
            if tmp == b'\x00\x00\x00\x00':
                break
            else:
                rem = big_endian_to_int(data[jj:jj+ee])
                self.l2_check_addr_list.append( [data[jj:jj+ee].hex(), rem]  )
            ###
            jj += ee
        #
        if self.d0_index == 1:  # First Page
            if jj == rr:  # if there is no data
                self.x1_check_addr_end = rr + 100
                self.x2_check_data_start = size
            else:  # if there is data
                self.x1_check_addr_end = jj + 100
                self.x2_check_data_start = size
        else:  # Other Page(s)
            self.x1_check_addr_end = jj
            self.x2_check_data_start = size
#
#
class SQLite3_B02Page:
    def __init__(self, index:int, data:bytes ):
        self.d0_bytes = data
        self.d0_index = index
        self.d1_00_page_header = [ 0, 1, 1, data[0:1].hex(), big_endian_to_int(data[0:1]), "Page header signature" ]
        self.d2_01_free_block_offset = [1, 3, 2, data[1:3].hex(), big_endian_to_int(data[1:3]), "Free block offset address" ]
        self.d3_03_number_of_cell = [3, 5, 2, data[3:5].hex(), big_endian_to_int(data[3:5]), "Number of cell" ]
        self.d4_05_cell_offset = [5, 7, 2, data[5:7].hex(), big_endian_to_int(data[5:7]), "Cell block offset address" ]
        self.d5_07_number_of_free = [7, 8, 1, data[7:8].hex(), big_endian_to_int(data[7:8]), "Number of free"]
        self.d6_08_page_pointer_number = [8, 12, 4, data[8:12].hex(), big_endian_to_int(data[8:12]), "Page pointer number"]
        self.l0_addr_list = list()
        self.l1_total_addr_list = list()
        self.l2_check_addr_list = list()
        #
        ee = 2
        rr = 12
        jj = 0
        if index == 1:
            min = len(data) + 100
        else:
            min = len(data)
        for ii in  range(self.d3_03_number_of_cell[4] - self.d5_07_number_of_free[4]):
            jj = rr + ii * ee
            rem = big_endian_to_int(data[jj:jj + ee])
            if rem < min:
                min = rem
            self.l0_addr_list.append( [data[jj:jj+ee].hex(), rem] )
        #
        if self.d0_index == 1:  # First Page
            if jj == 0:  # if there is no data
                self.y1_addr_end = rr + 100
                self.y2_data_start = min
            else:  # if there is data
                self.y1_addr_end = jj + ee + 100
                self.y2_data_start = min
        else:  # Other Page(s)
            self.y1_addr_end = jj + ee
            self.y2_data_start = min
        #
        for ii in  range( self.d3_03_number_of_cell[4] ):
            jj = rr + ii * ee
            self.l1_total_addr_list.append( [data[jj:jj+ee].hex(), big_endian_to_int(data[jj:jj+ee])] )
        #
        jj = rr
        if index == 1:
            size = len(data) + 100
        else:
            size = len(data)
        min = size
        while True:
            ###
            if jj+ee > size:
                break
            tmp = data[jj:jj+ee]
            ###
            if tmp == b'\x00\x00':
                break
            else:
                rem = big_endian_to_int(data[jj:jj+ee])
                if rem < min:
                    min = rem
                self.l2_check_addr_list.append( [data[jj:jj+ee].hex(), rem]  )
            ###
            jj += ee
        #
        if self.d0_index == 1:  # First Page
            if jj == rr:  # if there is no data
                self.x1_check_addr_end = rr + 100
                self.x2_check_data_start = size
            else:  # if there is data
                self.x1_check_addr_end = jj + 100
                self.x2_check_data_start = min
        else:  # Other Page(s)
            self.x1_check_addr_end = jj
            self.x2_check_data_start = min
#
#
class SQLite3_B05Page:
    def __init__(self, index:int, data:bytes ):
        self.d0_bytes = data
        self.d0_index = index
        self.d1_00_page_header = [ 0, 1, 1, data[0:1].hex(), big_endian_to_int(data[0:1]), "Page header signature" ]
        self.d2_01_free_block_offset = [1, 3, 2, data[1:3].hex(), big_endian_to_int(data[1:3]), "Free block offset address" ]
        self.d3_03_number_of_cell = [3, 5, 2, data[3:5].hex(), big_endian_to_int(data[3:5]), "Number of cell" ]
        self.d4_05_cell_offset = [5, 7, 2, data[5:7].hex(), big_endian_to_int(data[5:7]), "Cell block offset address" ]
        self.d5_07_number_of_free = [7, 8, 1, data[7:8].hex(), big_endian_to_int(data[7:8]), "Number of free"]
        self.d6_08_page_pointer_number = [8, 12, 4, data[8:12].hex(), big_endian_to_int(data[8:12]), "Page pointer number"]
        self.l0_addr_list = list()
        self.l1_total_addr_list = list()
        self.l2_check_addr_list = list()
        #
        ee = 2
        rr = 12
        jj = 0
        if index == 1:
            min = len(data) + 100
        else:
            min = len(data)
        for ii in  range(self.d3_03_number_of_cell[4] - self.d5_07_number_of_free[4]):
            jj = rr + ii * ee
            rem = big_endian_to_int(data[jj:jj + ee])
            if rem < min:
                min = rem
            self.l0_addr_list.append( [data[jj:jj+ee].hex(), rem] )
        #
        if self.d0_index == 1:  # First Page
            if jj == 0:  # if there is no data
                self.y1_addr_end = rr + 100
                self.y2_data_start = min
            else:  # if there is data
                self.y1_addr_end = jj + ee + 100
                self.y2_data_start = min
        else:  # Other Page(s)
            self.y1_addr_end = jj + ee
            self.y2_data_start = min
        #
        for ii in  range( self.d3_03_number_of_cell[4] ):
            jj = rr + ii * ee
            self.l1_total_addr_list.append( [data[jj:jj+ee].hex(), big_endian_to_int(data[jj:jj+ee])] )
        #
        jj = rr
        if index == 1:
            size = len(data) + 100
        else:
            size = len(data)
        min = size
        while True:
            ###
            if jj+ee > size:
                break
            tmp = data[jj:jj+ee]
            ###
            if tmp == b'\x00\x00':
                break
            else:
                rem = big_endian_to_int(data[jj:jj+ee])
                if rem < min:
                    min = rem
                self.l2_check_addr_list.append( [data[jj:jj+ee].hex(), rem]  )
            ###
            jj += ee
        #
        if self.d0_index == 1:  # First Page
            if jj == rr:  # if there is no data
                self.x1_check_addr_end = rr + 100
                self.x2_check_data_start = size
            else:  # if there is data
                self.x1_check_addr_end = jj + 100
                self.x2_check_data_start = min
        else:  # Other Page(s)
            self.x1_check_addr_end = jj
            self.x2_check_data_start = min
#
#
class SQLite3_B0APage:
    def __init__(self, index:int, data:bytes ):
        self.d0_bytes = data
        self.d0_index = index
        self.d1_00_page_header = [ 0, 1, 1, data[0:1].hex(), big_endian_to_int(data[0:1]), "Page header signature" ]
        self.d2_01_free_block_offset = [1, 3, 2, data[1:3].hex(), big_endian_to_int(data[1:3]), "Free block offset address" ]
        self.d3_03_number_of_cell = [3, 5, 2, data[3:5].hex(), big_endian_to_int(data[3:5]), "Number of cell" ]
        self.d4_05_cell_offset = [5, 7, 2, data[5:7].hex(), big_endian_to_int(data[5:7]), "Cell block offset address" ]
        self.d5_07_number_of_free = [7, 8, 1, data[7:8].hex(), big_endian_to_int(data[7:8]), "Number of free"]
        self.l0_addr_list = list()
        self.l1_total_addr_list = list()
        self.l2_check_addr_list = list()
        #
        ee = 2
        rr = 8
        jj = 0
        if index == 1:
            min = len(data) + 100
        else:
            min = len(data)
        for ii in  range(self.d3_03_number_of_cell[4] - self.d5_07_number_of_free[4]):
            jj = rr + ii * ee
            rem = big_endian_to_int(data[jj:jj + ee])
            if rem < min:
                min = rem
            self.l0_addr_list.append( [data[jj:jj+ee].hex(), rem] )
        #
        if self.d0_index == 1:  # First Page
            if jj == 0:  # if there is no data
                self.y1_addr_end = rr + 100
                self.y2_data_start = min
            else:  # if there is data
                self.y1_addr_end = jj + ee + 100
                self.y2_data_start = min
        else:  # Other Page(s)
            self.y1_addr_end = jj + ee
            self.y2_data_start = min
        #
        for ii in  range( self.d3_03_number_of_cell[4] ):
            jj = rr + ii * ee
            self.l1_total_addr_list.append( [data[jj:jj+ee].hex(), big_endian_to_int(data[jj:jj+ee])] )
        #
        jj = rr
        if index == 1:
            size = len(data) + 100
        else:
            size = len(data)
        min = size
        while True:
            ###
            if jj+ee > size:
                break
            tmp = data[jj:jj+ee]
            ###
            if tmp == b'\x00\x00':
                break
            else:
                rem = big_endian_to_int(data[jj:jj+ee])
                if rem < min:
                    min = rem
                self.l2_check_addr_list.append( [data[jj:jj+ee].hex(), rem]  )
            ###
            jj += ee
        #
        if self.d0_index == 1:  # First Page
            if jj == rr:  # if there is no data
                self.x1_check_addr_end = rr + 100
                self.x2_check_data_start = size
            else:  # if there is data
                self.x1_check_addr_end = jj + 100
                self.x2_check_data_start = min
        else:  # Other Page(s)
            self.x1_check_addr_end = jj
            self.x2_check_data_start = min
#
#
class SQLite3_B0DPage:
    def __init__(self, index:int ,data:bytes ):
        self.d0_bytes = data
        self.d0_index = index
        self.d1_00_page_header = [ 0, 1, 1, data[0:1].hex(), big_endian_to_int(data[0:1]), "Page header signature" ]
        self.d2_01_free_block_offset = [1, 3, 2, data[1:3].hex(), big_endian_to_int(data[1:3]), "Free block offset address" ]
        self.d3_03_number_of_cell = [3, 5, 2, data[3:5].hex(), big_endian_to_int(data[3:5]), "Number of cell" ]
        self.d4_05_cell_offset = [5, 7, 2, data[5:7].hex(), big_endian_to_int(data[5:7]), "Cell block offset address" ]
        self.d5_07_number_of_free = [7, 8, 1, data[7:8].hex(), big_endian_to_int(data[7:8]), "Number of free"]
        self.l0_addr_list = list()
        self.l1_total_addr_list = list()
        self.l2_check_addr_list = list()
        #
        ee = 2
        rr = 8
        jj = 0
        if index == 1:
            min = len(data) + 100
        else:
            min = len(data)
        for ii in  range(self.d3_03_number_of_cell[4] - self.d5_07_number_of_free[4]):
            jj = rr + ii * ee
            rem = big_endian_to_int(data[jj:jj + ee])
            if rem < min:
                min = rem
            self.l0_addr_list.append( [data[jj:jj+ee].hex(), rem] )
        #
        if self.d0_index == 1:  # First Page
            if jj == 0:  # if there is no data
                self.y1_addr_end = rr + 100
                self.y2_data_start = min
            else:  # if there is data
                self.y1_addr_end = jj + ee + 100
                self.y2_data_start = min
        else:  # Other Page(s)
            self.y1_addr_end = jj + ee
            self.y2_data_start = min
        #
        for ii in  range( self.d3_03_number_of_cell[4] ):
            jj = rr + ii * ee
            self.l1_total_addr_list.append( [data[jj:jj+ee].hex(), big_endian_to_int(data[jj:jj+ee])] )
        #
        jj = rr
        if index == 1:
            size = len(data) + 100
        else:
            size = len(data)
        min = size
        while True:
            ###
            if jj+ee > size:
                break
            tmp = data[jj:jj+ee]
            ###
            if tmp == b'\x00\x00':
                break
            else:
                rem = big_endian_to_int(data[jj:jj+ee])
                if rem < min:
                    min = rem
                self.l2_check_addr_list.append( [data[jj:jj+ee].hex(), rem]  )
            ###
            jj += ee
        #
        if self.d0_index == 1:  # First Page
            if jj == rr:  # if there is no data
                self.x1_check_addr_end = rr + 100
                self.x2_check_data_start = size
            else:  # if there is data
                self.x1_check_addr_end = jj + 100
                self.x2_check_data_start = min
        else:  # Other Page(s)
            self.x1_check_addr_end = jj
            self.x2_check_data_start = min
#
#
class SQLite3_B0DData:
    def __init__(self):
        self.d0_index = [0, 0] # [start, end]
        self.d1_total_data_size = 0
        self.d2_row_id = 0
        self.d3_cell_start_index = 0
        self.d4_header_data_size = 0
        self.d5_header_list = [] # [ ... ,[type, comment, size], [type, comment, size], [type, comment, size], ... ]
        self.d6_data_list = [] # [ ... , [res_val, res_type, res_str],  ... ]
    #
    def process(self, encode:str ,offsetindex:int, pageindex:int, pagedata:bytes):
        if pageindex == 1:
            offsetindex = offsetindex - 100
        #
        jj = offsetindex
        ii = 0
        while True:
            ii += 1
            t_size , total_val =  varint( pagedata[jj:(jj+ii)] )
            if total_val != -1:
                break
            #
            if ii == 9:
                return False
        #
        self.d1_total_data_size = total_val
        #
        jj = offsetindex + t_size
        ii = 0
        while True:
            ii += 1
            row_size , row_val =  varint( pagedata[jj:(jj+ii)] )
            if row_val != -1:
                break
            #
            if ii == 9:
                return False
        #
        self.d2_row_id = row_val
        self.d3_cell_start_index = offsetindex + t_size + row_size
        self.d0_index = [offsetindex, offsetindex + t_size + row_size + self.d1_total_data_size ]
        #
        ii = 0
        while True:
            ii += 1
            h_size, header_val =  varint( pagedata[self.d3_cell_start_index:(self.d3_cell_start_index+ii)] )
            if header_val != -1:
                break
            #
            if ii >= 9:
                return False
        #
        self.d4_header_data_size = header_val
        #
        h_start = self.d3_cell_start_index + h_size
        h_end   = self.d3_cell_start_index + header_val + 1
        b_start = h_end - 1
        b_end   = self.d0_index[1]
        body_bytes = b''
        # --- <check> ---
        if h_start < h_end:
            header_bytes = pagedata[h_start:h_end]
        else:
            return False
        #
        if b_start < b_end:
            body_bytes   = pagedata[b_start:b_end]
        #
        if self.d3_cell_start_index >= self.d0_index[1]:
            return False
        #
        if self.d3_cell_start_index+self.d4_header_data_size > self.d0_index[1]:
            return False
        #
        if self.d0_index[0] + self.d4_header_data_size >= self.d0_index[1]:
            return False
        # --- </check> ---
        ii_start = 0
        ii_end = 0
        ii_counter = 0
        jj_counter = (header_val - 1)
        #
        while True:
            if jj_counter <= 0:
                break
            #
            while True:
                ii_counter += 1
                ii_end += 1
                h_n_size, h_n_value = varint( header_bytes[ii_start:ii_end] )
                if h_n_value != -1:
                    break
                #
                if ii_counter >= 9:
                    return False
            ii_start = ii_start + h_n_size
            ii_end   = ii_start
            ii_counter = 0
            #
            jj_size, jj_type, jj_comment = headertype(val=h_n_value)
            self.d5_header_list.append( [jj_type, jj_comment, jj_size] )
            #
            if h_n_size != 0:
                jj_counter -= h_n_size
            else:
                jj_counter -= 1
            #
        #
        ii_start = 0
        for tmp_type, tmp_com ,tmp_size in self.d5_header_list:
            if tmp_size == 0:
                tmp_data = b''
            else:
                tmp_data = body_bytes[ii_start:ii_start+tmp_size]
            ii_start += tmp_size
            res_bool, res_val, res_type, res_str = headervalue(codecs=encode, type=tmp_type, data=tmp_data)
            #
            if res_bool:
                self.d6_data_list.append( [res_val, res_type, res_str] )
            else:
                return False
        return True
#
#
class SQLite3_B0AData:
    def __init__(self):
        self.d0_index = [0, 0] # [start, end]
        self.d1_total_data_size = 0
        self.d2_cell_start_index = 0
        self.d3_header_data_size = 0
        self.d4_header_list = [] # [ ... ,[type, comment, size], [type, comment, size], [type, comment, size], ... ]
        self.d5_data_list = [] # [... , [res_val, res_type, res_str] , ...]

    def process(self, encode:str ,offsetindex:int, pageindex:int, pagedata:bytes):
        if pageindex == 1:
            offsetindex = offsetindex - 100
        #
        jj = offsetindex
        ii = 0
        while True:
            ii += 1
            t_size , total_val =  varint( pagedata[jj:(jj+ii)] )
            if total_val != -1:
                break
            #
            if ii == 9:
                return False
        #
        self.d0_index = [offsetindex, (offsetindex + t_size + total_val) ]
        self.d1_total_data_size = total_val
        self.d2_cell_start_index = offsetindex + t_size
        #
        ii = 0
        while True:
            ii += 1
            h_size, header_val =  varint( pagedata[self.d2_cell_start_index:(self.d2_cell_start_index+ii)] )
            if header_val != -1:
                break
            #
            if ii >= 9:
                return False
        #
        self.d3_header_data_size = header_val
        #
        h_start = self.d2_cell_start_index + h_size
        h_end   = self.d2_cell_start_index + header_val + 1
        b_start = h_end - 1
        b_end   = self.d0_index[1]
        body_bytes = b''
        # --- <check> ---
        if h_start < h_end:
            header_bytes = pagedata[h_start:h_end]
        else:
            return False
        #
        if b_start < b_end:
            body_bytes   = pagedata[b_start:b_end]
        #
        if self.d2_cell_start_index >= self.d0_index[1]:
            return False
        #
        if self.d2_cell_start_index+self.d3_header_data_size > self.d0_index[1]:
            return False
        #
        if self.d0_index[0] + self.d3_header_data_size > self.d0_index[1]:
            return False
        # --- </check> ---
        ii_start = 0
        ii_end = 0
        ii_counter = 0
        jj_counter = (header_val - 1)
        #
        while True:
            if jj_counter <= 0:
                break
            #
            while True:
                ii_counter += 1
                ii_end += 1
                h_n_size, h_n_value = varint( header_bytes[ii_start:ii_end] )
                if h_n_value != -1:
                    break
                #
                if ii_counter >= 9:
                    return False
            ii_start = ii_start + h_n_size
            ii_end   = ii_start
            ii_counter = 0
            #
            jj_size, jj_type, jj_comment = headertype(val=h_n_value)
            self.d4_header_list.append( [jj_type, jj_comment, jj_size] )
            #
            if h_n_size != 0:
                jj_counter -= h_n_size
            else:
                jj_counter -= 1
            #
        #
        ii_start = 0
        for tmp_type, tmp_com ,tmp_size in self.d4_header_list:
            if tmp_size == 0:
                tmp_data = b''
            else:
                tmp_data = body_bytes[ii_start:ii_start+tmp_size]
            ii_start += tmp_size
            res_bool, res_val, res_type, res_str = headervalue(codecs=encode, type=tmp_type, data=tmp_data)
            #
            if res_bool:
                self.d5_data_list.append( [res_val, res_type, res_str] )
            else:
                return False
        #
        return True
#
#
class SQLite3_B05Data:
    def __init__(self):
        self.d0_index = [0, 0] # [start, end]
        self.d1_page_pointer_number = 0
        self.d2_data_number = 0

    def process(self, offsetindex: int, pageindex: int, pagedata: bytes):
        if pageindex == 1:
            offsetindex = offsetindex - 100
        #
        jj = offsetindex + 4
        self.d1_page_pointer_number = big_endian_to_int( pagedata[offsetindex:jj] )
        #
        ii = 0
        while True:
            ii += 1
            n_size , number_val =  varint( pagedata[jj:(jj+ii)] )
            if number_val != -1:
                break
            #
            if ii == 9:
                return False
        #
        self.d2_data_number = number_val
        self.d0_index = [offsetindex, (jj + n_size)]
        #
        return True
#
#
class SQLite3_B02Data:
    def __init__(self):
        self.d0_index = [0, 0] # [start, end]
        self.d1_page_pointer_number = 0
        self.d2_total_data_size = 0
        self.d3_cell_start_index = 0
        self.d4_header_data_size = 0
        self.d5_header_list = [] # [ ... ,[type, comment, size], [type, comment, size], [type, comment, size], ... ]
        self.d6_data_list = [] # [... , [res_val, res_type, res_str] , ...]

    def process(self, encode:str ,offsetindex:int, pageindex:int, pagedata:bytes):
        if pageindex == 1:
            offsetindex = offsetindex - 100
        #
        mm = offsetindex + 4
        self.d1_page_pointer_number = big_endian_to_int( pagedata[offsetindex:mm] )
        #
        jj = mm
        ii = 0
        while True:
            ii += 1
            t_size , total_val =  varint( pagedata[jj:(jj+ii)] )
            if total_val != -1:
                break
            #
            if ii == 9:
                return False
        #
        self.d0_index = [offsetindex, (mm + t_size + total_val) ]
        self.d2_total_data_size = total_val
        self.d3_cell_start_index = mm + t_size
        #
        ii = 0
        while True:
            ii += 1
            h_size, header_val =  varint( pagedata[self.d3_cell_start_index:(self.d3_cell_start_index+ii)] )
            if header_val != -1:
                break
            #
            if ii >= 9:
                return False
        #
        self.d4_header_data_size = header_val
        #
        h_start = self.d3_cell_start_index + h_size
        h_end   = self.d3_cell_start_index + header_val + 1
        b_start = h_end - 1
        b_end   = self.d0_index[1]
        body_bytes = b''
        # --- <check> ---
        if h_start < h_end:
            header_bytes = pagedata[h_start:h_end]
        else:
            return False
        #
        if b_start < b_end:
            body_bytes   = pagedata[b_start:b_end]
        #
        if self.d3_cell_start_index >= self.d0_index[1]:
            return False
        #
        if self.d3_cell_start_index+self.d4_header_data_size > self.d0_index[1]:
            return False
        #
        if self.d0_index[0] + 4 + self.d4_header_data_size > self.d0_index[1]:
            return False
        # --- </check> ---
        ii_start = 0
        ii_end = 0
        ii_counter = 0
        jj_counter = (header_val - 1)
        #
        while True:
            if jj_counter <= 0:
                break
            #
            while True:
                ii_counter += 1
                ii_end += 1
                h_n_size, h_n_value = varint( header_bytes[ii_start:ii_end] )
                if h_n_value != -1:
                    break
                #
                if ii_counter >= 9:
                    return False
            ii_start = ii_start + h_n_size
            ii_end   = ii_start
            ii_counter = 0
            #
            jj_size, jj_type, jj_comment = headertype(val=h_n_value)
            self.d5_header_list.append( [jj_type, jj_comment, jj_size] )
            #
            if h_n_size != 0:
                jj_counter -= h_n_size
            else:
                jj_counter -= 1
            #
        #
        ii_start = 0
        for tmp_type, tmp_com ,tmp_size in self.d5_header_list:
            if tmp_size == 0:
                tmp_data = b''
            else:
                tmp_data = body_bytes[ii_start:ii_start+tmp_size]
            ii_start += tmp_size
            res_bool, res_val, res_type, res_str = headervalue(codecs=encode, type=tmp_type, data=tmp_data)
            #
            if res_bool:
                self.d6_data_list.append( [res_val, res_type, res_str] )
            else:
                return False
        #
        return True