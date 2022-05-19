############################################################################
#
#   main.py (Analyzing SQlite3 Database) [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from SQLite3_data import *
import time, sys, os
#
#
#
class ConsoleColour:
    Black = "0"
    Blue = "1"
    Green = "2"
    Aqua = "3"
    Red = "4"
    Purple = "5"
    Yellow = "6"
    White = "7"
    Gray = "8"
    Light_Blue = "9"
    Light_Green = "A"
    Light_Aqua = "B"
    Light_Red = "C"
    Light_Purple = "D"
    Light_Yellow = "E"
    Light_White = "F"
#
def console(background_colour:str=ConsoleColour.Black, text_colour:str=ConsoleColour.White,
            title:str=""):
    os.system("echo off")
    os.system("color {bg}{tg}".format(bg=background_colour, tg=text_colour))
    os.system("title {title}".format(title=title))
#
def screenClear():
    os.system("cls")
#
def setCursor(visible:bool=True):
    from ctypes import Structure, c_int, byref, windll
    # Structure
    class CONSOLE_CURSOR_INFO(Structure):
        _fields_ = [('dwSize', c_int),
                    ('bVisible', c_int)]
    # Handle
    STD_OUTPUT_HANDLE = -11
    hStdOut = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    # Create structure
    cursorInfo = CONSOLE_CURSOR_INFO()
    cursorInfo.dwSize = 1
    if visible:
        cursorInfo.bVisible = 1
    else:
        cursorInfo.bVisible = 0
    #
    windll.kernel32.SetConsoleCursorInfo(hStdOut, byref(cursorInfo))
#
def textUpdate( total_int, value_int, text_str ):
    fill_padding   = '█'
    fill_dash   = '-'
    percent = int(100*(value_int/total_int))
    bar_padding = int(percent/2.15)
    bar_dash    = 46 - bar_padding
    bar = (fill_padding * bar_padding) + (fill_dash * bar_dash)
    percent = "{0: >2}".format(str(percent))
    txt_str = "{0: <38}".format(str(text_str))
    #
    print( '''\t|%s| %s%%   %s''' % (bar, percent, txt_str), end='\r' )
    if value_int == total_int:
        print()
#
def screenEntry():
    print('')
    print('\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\')
    print('\t\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print('\t/\/\                                                      /\/\\')
    print('\t\/\/ <Program> Analyzing SQlite3 Database V1.1 </Program> \/\/')
    print('\t/\/\              <Date> 05/2022 </Date>                  /\/\\')
    print('\t\/\/                                                      \/\/')
    print('\t/\/\     <Developer> Abdulkadir GÜNGÖR </Developer>       /\/\\')
    print('\t\/\/   <Email> abdulkadir_gungor@outlook.com </Email>     \/\/')
    print('\t/\/\                                                      /\/\\')
    print('\t\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print('\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\')
    print('')
#
def arg():
    argv = sys.argv
    number = len(argv)
    #
    if number == 1:
        return False, ""
    elif number == 2:
        program_name = argv[0].split(sep='\\')[-1]
        first_input = argv[1].lower()
        if first_input == '-help' or first_input == '-h' :
            print()
            print("\t\t [Help] Argument(s) ")
            print( ("\t"+("-"*60)) )
            print("\t[show help]            ==> {0} -h/-help".format(program_name))
            print("\t[run with db file]     ==> {0} file".format(program_name))
            print("\t[run without db file]  ==> {0} ".format(program_name))
            print("\t")
            print("\t")
            print("\t[Examples]")
            print("\t>> {0} ".format(program_name))
            print("\t>> {0} database.sqlite3".format(program_name))
            print("\t>> {0} database.db3".format(program_name))
            print("\t>> {0} database.db".format(program_name))
            print("\t>> {0} database".format(program_name))
            print(("\t" + ("-" * 60)))
            #
            sys.exit(0)
        else:
            return True, argv[1]
    else:
        program_name = argv[0].split(sep='\\')[-1]
        print()
        print("\n\tParameters are wrong!")
        print()
        print()
        print("\t\t [Help] Argument(s) ")
        print(("\t" + ("-" * 60)))
        print("\t[show help]            ==> {0} -h/-help".format(program_name))
        print("\t[run with db file]     ==> {0} file".format(program_name))
        print("\t[run without db file]  ==> {0} ".format(program_name))
        print("\t")
        print("\t")
        print("\t[Examples]")
        print("\t>> {0} ".format(program_name))
        print("\t>> {0} database.sqlite3".format(program_name))
        print("\t>> {0} database.db3".format(program_name))
        print("\t>> {0} database.db".format(program_name))
        print("\t>> {0} database".format(program_name))
        print(("\t" + ("-" * 60)))
        #
        sys.exit(0)
#
def logFileName_str():
    return time.strftime("%Y-%m-%d_%H-%M-%S_database.log")
#
def logFile(db_file, output_file, output_encoding="UTF-8"):
    #
    setCursor(visible=False)
    st01_total_int     = 100
    textUpdate(st01_total_int, 1 , '"Preparing the function  ..."')
    time.sleep(0.001)
    # Check Db File
    try:
        textUpdate(st01_total_int, 2, '"Preparing the function (OK)"')
        time.sleep(0.001)
        textUpdate(st01_total_int, 4, '"Reading database  ..."')
        time.sleep(0.001)
        with open(file=db_file, mode='rb') as frb:
            ofl = frb.read()
    except:
        textUpdate(st01_total_int, 100, '"(ERROR)"')
        time.sleep(0.001)
        print("\n\tFile could not be read!")
        print("\n\n\tPossible causes of error")
        print("\t----------------------------")
        print("\t1) The database file may be not found")
        print("\t2) The database file may be too big.")
        time.sleep(0.001)
        setCursor(visible=True)
        return False
    #
    textUpdate(st01_total_int, 6, '"Reading database (OK)"')
    time.sleep(0.001)
    textUpdate(st01_total_int, 8, '"Analyzing SQlite3 header  ..."')
    time.sleep(0.001)
    db_head_str = SQLite3HeaderData().all()
    db_head = SQLite3Header(ofl).all()
    db_text_encoding = db_head[16]
    #
    with open(file=output_file, mode="w", encoding=output_encoding) as wfile:
        wfile.write("\n")
        wfile.write("\tFilename : ")
        wfile.write(db_file)
        wfile.write("\n\n")
        wfile.write("\t(1) SQLite3 Header Information")
        wfile.write("\n\t")
        wfile.write("-" * 150)
        #
        for ii in range(23):
            wfile.write("\n\t")
            wfile.write(db_head_str[ii][3])
            wfile.write(" : ")
            wfile.write(str(db_head[ii]))
    #
    textUpdate(st01_total_int, 10, '"Analyzing SQlite3 header (OK)"')
    time.sleep(0.001)
    textUpdate(st01_total_int, 12, '"Analyzing SQlite3 page(s)  ..."')
    time.sleep(0.001)
    pages = SQLite3Pages(ofl, db_head[1])
    #
    with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
        wfile.write("\n\n")
        wfile.write("\t(2) SQLite3 Page(s)")
        wfile.write("\n\t")
        wfile.write("-" * 150)
        wfile.write("\n\tAll pages   : (total_number:")
        wfile.write(str(len(pages.d1_all_pages)))
        wfile.write(")   ")
        newline_int = 0
        newline_str = '\n\t\t\t\t\t  '
        for addr in pages.d1_all_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tB00 pages   : (total_number:")
        wfile.write(str(len(pages.d2_b00_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d2_b00_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tB02 pages   : (total_number:")
        wfile.write(str(len(pages.d3_b02_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d3_b02_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tB05 pages   : (total_number:")
        wfile.write(str(len(pages.d4_b05_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d4_b05_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tB0A pages   : (total_number:")
        wfile.write(str(len(pages.d5_b0a_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d5_b0a_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tB0D pages   : (total_number:")
        wfile.write(str(len(pages.d6_b0d_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d6_b0d_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
        wfile.write("\n\tOther pages : (total_number:")
        wfile.write(str(len(pages.d7_bff_pages)))
        wfile.write(")   ")
        newline_int = 0
        for addr in pages.d7_bff_pages:
            wfile.write(" [index:")
            wfile.write(str(addr[0]))
            wfile.write(" addr_int:")
            wfile.write(str(addr[1]))
            wfile.write(" addr_hex:")
            wfile.write(str(hex(addr[1])))
            wfile.write("]")
            newline_int += 1
            if newline_int == 10:
                newline_int = 0
                wfile.write(newline_str)
    #
    textUpdate(st01_total_int, 16, "Analyzing SQlite3 page(s) (OK)")
    time.sleep(0.001)
    st02_all_pages_size = len(pages.d1_all_pages)
    st02_counter        = 0
    textUpdate(st01_total_int, 18, "Analyzing SQlite3 page(s) (OK)")
    time.sleep(0.001)
    for page in pages.d1_all_pages:
        st02_counter += 1
        st02_progress = int((18 + (st02_counter / st02_all_pages_size) * 80))
        textUpdate(st01_total_int, st02_progress, '''"Analyzing {}. page's data(s)"'''.format(str(st02_counter)))
        with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
            wfile.write("\n\n")
            wfile.write("\n\tPage_index :")
            wfile.write(str(page[0]))
            wfile.write("\t [Start_addr (int:")
            wfile.write(str(page[1]))
            wfile.write(") (hex:")
            wfile.write(str(hex(page[1])))
            wfile.write(")]\t [End_addr (int:")
            wfile.write(str(page[2]))
            wfile.write(") (hex:")
            wfile.write(str(hex(page[2])))
            wfile.write(")]\t Type :")
            wfile.write(str(page[4]))
            wfile.write("\n\t")
            wfile.write("-" * 150)
        #
        page_no = page[3]
        page_data_bytes = ofl[page[1]:page[2]]
        #
        if page_no == -1:
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                wfile.write("\n************ UNKNOWN PAGE ********************")
        #
        elif page_no == 0:
            page_obj = SQLite3_B00Page(page[0], page_data_bytes)
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                if page[0] == 1:
                    tmp_free_block_offset_int = page_obj.d2_01_free_block_offset[4]
                    tmp_cell_block_offset_int = page_obj.d4_05_cell_offset[4]
                else:
                    if page_obj.d2_01_free_block_offset[4] != 0:
                        tmp_free_block_offset_int = page[1] + page_obj.d2_01_free_block_offset[4]
                    else:
                        tmp_free_block_offset_int = 0
                    if page_obj.d4_05_cell_offset[4] != 0:
                        tmp_cell_block_offset_int = page[1] + page_obj.d4_05_cell_offset[4]
                    else:
                        tmp_cell_block_offset_int = 0
                #
                tmp_free_block_offset_hex = "{:0>4x}".format( tmp_free_block_offset_int )
                tmp_cell_block_offset_hex = "{:0>4x}".format( tmp_cell_block_offset_int )
                #
                wfile.write("\n\t")
                wfile.write(str(page_obj.d1_00_page_header[5]))
                wfile.write("     : (int:")
                wfile.write(str(page_obj.d1_00_page_header[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d1_00_page_header[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d2_01_free_block_offset[5]))
                wfile.write(" : (int:")
                wfile.write(str(tmp_free_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_free_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d3_03_number_of_cell[5])
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d3_03_number_of_cell[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d3_03_number_of_cell[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d4_05_cell_offset[5]))
                wfile.write(" : (int:")
                wfile.write(str(page_obj.d4_05_cell_offset[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d4_05_cell_offset[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d5_07_number_of_free[5]))
                wfile.write("            : (int:")
                wfile.write(str(tmp_cell_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_cell_block_offset_hex ))
                wfile.write(")")
                if len(page_obj.l0_addr_list) > 0:
                    wfile.write("\n\t***")
                    wfile.write("\n\tFree Page(s)")
                    for tmp in page_obj.l0_addr_list:
                        wfile.write("\n\t<page> (int:")
                        wfile.write(str(tmp[1]))
                        wfile.write(") (hex:")
                        wfile.write(str(hex(tmp[1])))
                        wfile.write(") </page>")
        #
        elif page_no == 2:
            page_obj = SQLite3_B02Page(page[0], page_data_bytes)
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                if page[0] == 1:
                    tmp_free_block_offset_int = page_obj.d2_01_free_block_offset[4]
                    tmp_cell_block_offset_int = page_obj.d4_05_cell_offset[4]
                else:
                    if page_obj.d2_01_free_block_offset[4] != 0:
                        tmp_free_block_offset_int = page[1] + page_obj.d2_01_free_block_offset[4]
                    else:
                        tmp_free_block_offset_int = 0
                    if page_obj.d4_05_cell_offset[4] != 0:
                        tmp_cell_block_offset_int = page[1] + page_obj.d4_05_cell_offset[4]
                    else:
                        tmp_cell_block_offset_int = 0
                #
                tmp_free_block_offset_hex = "{:0>4x}".format( tmp_free_block_offset_int )
                tmp_cell_block_offset_hex = "{:0>4x}".format( tmp_cell_block_offset_int )
                #
                wfile.write("\n\t")
                wfile.write(str(page_obj.d1_00_page_header[5]))
                wfile.write("     : (int:")
                wfile.write(str(page_obj.d1_00_page_header[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d1_00_page_header[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d2_01_free_block_offset[5]))
                wfile.write(" : (int:")
                wfile.write(str(tmp_free_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_free_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d3_03_number_of_cell[5]))
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d3_03_number_of_cell[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d3_03_number_of_cell[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d4_05_cell_offset[5]))
                wfile.write(" : (int:")
                wfile.write(str(tmp_cell_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_cell_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d5_07_number_of_free[5]))
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d5_07_number_of_free[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d5_07_number_of_free[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d6_08_page_pointer_number[5]))
                wfile.write("       : (int:")
                wfile.write(str(page_obj.d6_08_page_pointer_number[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d6_08_page_pointer_number[3]))
                wfile.write(")")
                #
                if len(page_obj.l0_addr_list) > 0:
                    wfile.write("\n\t***")
                    wfile.write("\n\tData(s)")
                    #
                    for addr in page_obj.l0_addr_list:
                        data = SQLite3_B02Data()
                        res = data.process(encode=db_text_encoding, offsetindex=addr[1], pageindex=page[0],
                                           pagedata=ofl[page[1]:page[2]])
                        tmp_start_addr = page[1] + data.d0_index[0]
                        tmp_end_addr  = page[1] + data.d0_index[1]
                        #
                        wfile.write("\n\t[Address_int:")
                        wfile.write(str(tmp_start_addr))
                        wfile.write(" ")
                        wfile.write(str(tmp_end_addr))
                        wfile.write("] [Address_hex:")
                        wfile.write(str(hex(tmp_start_addr)))
                        wfile.write(" ")
                        wfile.write(str(hex(tmp_end_addr)))
                        wfile.write("] ")
                        wfile.write("[is_Valid:")
                        wfile.write(str(res))
                        wfile.write("]  ||  (Data) <Page>")
                        wfile.write(str(data.d1_page_pointer_number))
                        wfile.write("<\\Page>")
                        for kk in data.d6_data_list:
                            wfile.write(" <")
                            wfile.write(kk[2])
                            wfile.write(">")
                            if type(kk[0]) == type(b'0'):
                                wfile.write(str(kk[0].hex(sep="-")))
                            elif type(kk[0]) == type('0'):
                                kk[0] = kk[0].replace("\r\n", "{\\r\\n}")
                                kk[0] = kk[0].replace("\r", "{\\r}")
                                kk[0] = kk[0].replace("\n", "{\\n}")
                                wfile.write(kk[0])
                            else:
                                wfile.write(str(kk[0]))
                            wfile.write("<\\")
                            wfile.write(kk[2])
                            wfile.write(">")
        #
        elif page_no == 5:
            page_obj = SQLite3_B05Page(page[0], page_data_bytes)
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                if page[0] == 1:
                    tmp_free_block_offset_int = page_obj.d2_01_free_block_offset[4]
                    tmp_cell_block_offset_int = page_obj.d4_05_cell_offset[4]
                else:
                    if page_obj.d2_01_free_block_offset[4] != 0:
                        tmp_free_block_offset_int = page[1] + page_obj.d2_01_free_block_offset[4]
                    else:
                        tmp_free_block_offset_int = 0
                    if page_obj.d4_05_cell_offset[4] != 0:
                        tmp_cell_block_offset_int = page[1] + page_obj.d4_05_cell_offset[4]
                    else:
                        tmp_cell_block_offset_int = 0
                #
                tmp_free_block_offset_hex = "{:0>4x}".format( tmp_free_block_offset_int )
                tmp_cell_block_offset_hex = "{:0>4x}".format( tmp_cell_block_offset_int )
                #
                wfile.write("\n\t")
                wfile.write(str(page_obj.d1_00_page_header[5]))
                wfile.write("     : (int:")
                wfile.write( str(page_obj.d1_00_page_header[4]) )
                wfile.write(") (hex:")
                wfile.write( str(page_obj.d1_00_page_header[3]) )
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d2_01_free_block_offset[5]))
                wfile.write(" : (int:")
                wfile.write( str(tmp_free_block_offset_int) )
                wfile.write(") (hex:")
                wfile.write( str(tmp_free_block_offset_hex) )
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d3_03_number_of_cell[5]))
                wfile.write("            : (int:")
                wfile.write( str(page_obj.d3_03_number_of_cell[4]) )
                wfile.write(") (hex:")
                wfile.write( str(page_obj.d3_03_number_of_cell[3]) )
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d4_05_cell_offset[5]))
                wfile.write(" : (int:")
                wfile.write( str(tmp_cell_block_offset_int) )
                wfile.write(") (hex:")
                wfile.write( str(tmp_cell_block_offset_hex) )
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d5_07_number_of_free[5]))
                wfile.write("            : (int:")
                wfile.write( str(page_obj.d5_07_number_of_free[4]) )
                wfile.write(") (hex:")
                wfile.write( str(page_obj.d5_07_number_of_free[3]) )
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(str(page_obj.d6_08_page_pointer_number[5]))
                wfile.write("       : (int:")
                wfile.write( str(page_obj.d6_08_page_pointer_number[4]) )
                wfile.write(") (hex:")
                wfile.write( str(page_obj.d6_08_page_pointer_number[3]) )
                wfile.write(")")
                #
                if len(page_obj.l0_addr_list) > 0:
                    wfile.write("\n\t***")
                    wfile.write("\n\tData(s)")
                    #
                    for addr in page_obj.l0_addr_list:
                        data = SQLite3_B05Data()
                        res = data.process(offsetindex=addr[1], pageindex=page[0],
                                           pagedata=ofl[page[1]:page[2]])
                        tmp_start_addr = page[1] + data.d0_index[0]
                        tmp_end_addr  = page[1] + data.d0_index[1]
                        #
                        wfile.write("\n\t[Address_int:")
                        wfile.write(str(tmp_start_addr))
                        wfile.write(" ")
                        wfile.write(str(tmp_end_addr))
                        wfile.write("] [Address_hex:")
                        wfile.write(str(hex(tmp_start_addr)))
                        wfile.write(" ")
                        wfile.write(str(hex(tmp_end_addr)))
                        wfile.write("] ")
                        wfile.write("[is_Valid:")
                        wfile.write(str(res))
                        wfile.write("]  ||  (Data) <Page>")
                        wfile.write(str(data.d1_page_pointer_number))
                        wfile.write("<\\Page>")
                        wfile.write(" <Int>")
                        wfile.write(str(data.d2_data_number))
                        wfile.write("<\\Int>")
        #
        elif page_no == 10:
            page_obj = SQLite3_B0APage(page[0], page_data_bytes)
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                if page[0] == 1:
                    tmp_free_block_offset_int = page_obj.d2_01_free_block_offset[4]
                    tmp_cell_block_offset_int = page_obj.d4_05_cell_offset[4]
                else:
                    if page_obj.d2_01_free_block_offset[4] != 0:
                        tmp_free_block_offset_int = page[1] + page_obj.d2_01_free_block_offset[4]
                    else:
                        tmp_free_block_offset_int = 0
                    if page_obj.d4_05_cell_offset[4] != 0:
                        tmp_cell_block_offset_int = page[1] + page_obj.d4_05_cell_offset[4]
                    else:
                        tmp_cell_block_offset_int = 0
                #
                tmp_free_block_offset_hex = "{:0>4x}".format( tmp_free_block_offset_int )
                tmp_cell_block_offset_hex = "{:0>4x}".format( tmp_cell_block_offset_int )
                wfile.write("\n\t")
                wfile.write(page_obj.d1_00_page_header[5])
                wfile.write("     : (int:")
                wfile.write(str(page_obj.d1_00_page_header[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d1_00_page_header[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d2_01_free_block_offset[5])
                wfile.write(" : (int:")
                wfile.write(str(tmp_free_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_free_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d3_03_number_of_cell[5])
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d3_03_number_of_cell[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d3_03_number_of_cell[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d4_05_cell_offset[5])
                wfile.write(" : (int:")
                wfile.write(str(tmp_cell_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_cell_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d5_07_number_of_free[5])
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d5_07_number_of_free[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d5_07_number_of_free[3]))
                wfile.write(")")
                #
                if len(page_obj.l0_addr_list) > 0:
                    wfile.write("\n\t***")
                    wfile.write("\n\tData(s)")
                    #
                    for addr in page_obj.l0_addr_list:
                        data = SQLite3_B0AData()
                        res = data.process(encode=db_text_encoding, offsetindex=addr[1], pageindex=page[0],
                                           pagedata=ofl[page[1]:page[2]])
                        tmp_start_addr = page[1] + data.d0_index[0]
                        tmp_end_addr  = page[1] + data.d0_index[1]
                        #
                        wfile.write("\n\t[Address_int:")
                        wfile.write(str(tmp_start_addr))
                        wfile.write(" ")
                        wfile.write(str(tmp_end_addr))
                        wfile.write("] [Address_hex:")
                        wfile.write(str(hex(tmp_start_addr)))
                        wfile.write(" ")
                        wfile.write(str(hex(tmp_end_addr)))
                        wfile.write("] ")
                        wfile.write("[is_Valid:")
                        wfile.write(str(res))
                        wfile.write("]  ||  (Data) ")
                        for kk in data.d5_data_list:
                            wfile.write(" <")
                            wfile.write(kk[2])
                            wfile.write(">")
                            if type(kk[0]) == type(b'0'):
                                wfile.write(str(kk[0].hex(sep="-")))
                            elif type(kk[0]) == type('0'):
                                kk[0] = kk[0].replace("\r\n", "{\\r\\n}")
                                kk[0] = kk[0].replace("\r", "{\\r}")
                                kk[0] = kk[0].replace("\n", "{\\n}")
                                wfile.write(kk[0])
                            else:
                                wfile.write(str(kk[0]))
                            wfile.write("<\\")
                            wfile.write(kk[2])
                            wfile.write(">")
        elif page_no == 13:
            page_obj = SQLite3_B0DPage(page[0], page_data_bytes)
            with open(file=output_file, mode="a", encoding=output_encoding) as wfile:
                if page[0] == 1:
                    tmp_free_block_offset_int = page_obj.d2_01_free_block_offset[4]
                    tmp_cell_block_offset_int = page_obj.d4_05_cell_offset[4]
                else:
                    if page_obj.d2_01_free_block_offset[4] != 0:
                        tmp_free_block_offset_int = page[1] + page_obj.d2_01_free_block_offset[4]
                    else:
                        tmp_free_block_offset_int = 0
                    if page_obj.d4_05_cell_offset[4] != 0:
                        tmp_cell_block_offset_int = page[1] + page_obj.d4_05_cell_offset[4]
                    else:
                        tmp_cell_block_offset_int = 0
                #
                tmp_free_block_offset_hex = "{:0>4x}".format( tmp_free_block_offset_int )
                tmp_cell_block_offset_hex = "{:0>4x}".format( tmp_cell_block_offset_int )
                wfile.write("\n\t")
                wfile.write(page_obj.d1_00_page_header[5])
                wfile.write("     : (int:")
                wfile.write(str(page_obj.d1_00_page_header[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d1_00_page_header[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d2_01_free_block_offset[5])
                wfile.write(" : (int:")
                wfile.write(str(tmp_free_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_free_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d3_03_number_of_cell[5])
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d3_03_number_of_cell[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d3_03_number_of_cell[3]))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d4_05_cell_offset[5])
                wfile.write(" : (int:")
                wfile.write(str(tmp_cell_block_offset_int))
                wfile.write(") (hex:")
                wfile.write(str(tmp_cell_block_offset_hex))
                wfile.write(")")
                wfile.write("\n\t")
                wfile.write(page_obj.d5_07_number_of_free[5])
                wfile.write("            : (int:")
                wfile.write(str(page_obj.d5_07_number_of_free[4]))
                wfile.write(") (hex:")
                wfile.write(str(page_obj.d5_07_number_of_free[3]))
                wfile.write(")")
                #
                if len(page_obj.l0_addr_list) > 0:
                    wfile.write("\n\t***")
                    wfile.write("\n\tData(s)")
                    #
                    for addr in page_obj.l0_addr_list:
                        data = SQLite3_B0DData()
                        res = data.process(encode=db_text_encoding, offsetindex=addr[1], pageindex=page[0],
                                           pagedata=ofl[page[1]:page[2]])
                        tmp_start_addr = page[1] + data.d0_index[0]
                        tmp_end_addr  = page[1] + data.d0_index[1]
                        #
                        wfile.write("\n\t[Address_int:")
                        wfile.write(str(tmp_start_addr))
                        wfile.write(" ")
                        wfile.write(str(tmp_end_addr))
                        wfile.write("] [Address_hex:")
                        wfile.write(str(hex(tmp_start_addr)))
                        wfile.write(" ")
                        wfile.write(str(hex(tmp_end_addr)))
                        wfile.write("] ")
                        wfile.write("[is_Valid:")
                        wfile.write(str(res))
                        wfile.write("]  ||  (Data) <Row_id>")
                        wfile.write(str(data.d2_row_id))
                        wfile.write("<\\Row_id>")
                        #
                        for kk in data.d6_data_list:
                            wfile.write(" <")
                            wfile.write(kk[2])
                            wfile.write(">")
                            if type(kk[0]) == type(b'0'):
                                wfile.write(str(kk[0].hex(sep="-")))
                            elif type(kk[0]) == type('0'):
                                kk[0] = kk[0].replace("\r\n", "{\\r\\n}")
                                kk[0] = kk[0].replace("\r", "{\\r}")
                                kk[0] = kk[0].replace("\n", "{\\n}")
                                wfile.write(kk[0])
                            else:
                                wfile.write(str(kk[0]))
                            wfile.write("<\\")
                            wfile.write(kk[2])
                            wfile.write(">")
    #
    textUpdate(st01_total_int, 100, '"OK!"' )
    time.sleep(0.001)
    print('\n\t"{0}" has been created.'.format(output_file))
    time.sleep(0.001)
    setCursor(visible=True)
    return True
#
#
#
# Main block
if __name__ == '__main__':
    # <Initial variables>
    encoding = "UTF-8"
    background_color =  ConsoleColour.Black
    text_color = ConsoleColour.Light_White
    title = "Analyzing SQlite3 Database V1.1"
    # <Initial variables>
    res, db_file = arg()
    console( background_color, text_color ,title)
    while True:
        screenClear()
        screenEntry()
        if res:
            try:
                db_file = db_file.replace('"',"")
                print( ("\tDb file : "+db_file) )
                print()
                logFile(db_file=db_file, output_file=logFileName_str(), output_encoding=encoding)
                res = False
            except:
                print("\n\tAn unexpected error occurred!")
        else:
            db_file = input("\tDb file : ")
            print()
            db_file = db_file.replace('"', "")
            try:
                logFile(db_file=db_file, output_file=logFileName_str(), output_encoding=encoding)
            except:
                print("\n\tAn unexpected error occurred!")
        print()
        print()
        print("\t[Continue: <Enter>] [Exit: <E>]")
        selection = input("\tSelection : ")
        if selection.lower().strip() == "e":
            screenClear()
            console(ConsoleColour.Black, ConsoleColour.White)
            sys.exit(0)