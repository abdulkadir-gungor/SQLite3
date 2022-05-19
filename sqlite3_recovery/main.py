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
from SQLite3_recovery import undefinedRawData, writeDbData, checkRawDataList, writeData
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
    print('\t/\/\                   <Recovery>                         /\/\\')
    print('\t\/\/                                                      \/\/')
    print('\t/\/\ <Program> Analyzing SQlite3 Database V1.1 </Program> /\/\\')
    print('\t\/\/              <Date> 05/2022 </Date>                  \/\/')
    print('\t/\/\                                                      /\/\\')
    print('\t\/\/     <Developer> Abdulkadir GÜNGÖR </Developer>       \/\/')
    print('\t/\/\   <Email> abdulkadir_gungor@outlook.com </Email>     /\/\\')
    print('\t\/\/                                                      \/\/')
    print('\t/\/\                   </Recovery>                        /\/\\')
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
def logFileName_str(raw_recovery_data:bool=False, processed_recovery_data:bool=False):
    if raw_recovery_data:
        return time.strftime("%Y-%m-%d_%H-%M-%S_raw_recovery_data.log")
    elif processed_recovery_data:
        return time.strftime("%Y-%m-%d_%H-%M-%S_processed_recovery_data.log")
    return time.strftime("%Y-%m-%d_%H-%M-%S_raw_recovery_data.log")

#
def recovery(db_file:str, output_encoding:str, filter_page_type):
    #
    if not os.path.exists(db_file):
        print("\tThe database file has been not found!")
        return
    #
    header_size_str_tmp = input("\tHeader size : ")
    header_size_str = header_size_str_tmp.strip()
    if header_size_str.isnumeric():
        header_size = int(header_size_str)
        if header_size == 0:
            header_size = -1
    else:
        header_size = -1
    print()
    #
    setCursor(visible=False)
    st01_total_int = 100
    textUpdate(st01_total_int, 2, '"Preparing the function  ..."')
    time.sleep(0.001)
        #
    textUpdate(st01_total_int, 6, '"Analyzing SQlite3 DB file ..."')
    time.sleep(0.001)
    #
    str_enc, r_data = undefinedRawData(db_file)
    #
    textUpdate(st01_total_int, 30, '"Writing raw data(s) ..."')
    time.sleep(0.001)
    #
    writeDbData(dbfile=db_file, outputfile=logFileName_str(raw_recovery_data=True), listData=r_data, encoding=output_encoding)
    #
    if header_size != -1:
        textUpdate(st01_total_int, 70, '"Processing raw data(s) ..."')
        time.sleep(0.001)
        #
        data_s = checkRawDataList(r_data, header_total_number=header_size, db_file=db_file, encoding=str_enc,
                                 filter_page_type=filter_page_type)
        #
        textUpdate(st01_total_int, 90, '"Writing processed data(s) ..."')
        time.sleep(0.001)
        #
        writeData(dbfile=db_file, outputfile=logFileName_str(processed_recovery_data=True), listData=data_s)
    #
    textUpdate(st01_total_int, st01_total_int, '"(OK)"')
    time.sleep(0.001)
    return
#
#
#
# Main block
if __name__ == '__main__':
    # <Initial variables>
    filter_page_type = [0, 13]
    encoding = "UTF-8"
    background_color =  ConsoleColour.Black
    text_color = ConsoleColour.Light_White
    title = "Analyzing SQlite3 Database (Recovery) V1.1"
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
                recovery(db_file=db_file, output_encoding=encoding, filter_page_type=filter_page_type)
                res = False
            except:
                print("\n\tAn unexpected error occurred!")
        else:
            db_file = input("\tDb file : ")
            print()
            db_file = db_file.replace('"', "")
            try:
                recovery(db_file=db_file, output_encoding=encoding, filter_page_type=filter_page_type)
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