############################################################################
#
#   SQLite3_func.py (Analyzing SQlite3 Database) [ Library File ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	05/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import struct

#   00 00 00 01 = 1
#   Big Endian
def big_endian_to_int(data:bytes):
    multiply = 1
    res = 0
    for ii in data[::-1]:
        res += ii * multiply
        multiply *= 256
    return res

#   00 00 00 01 = 128
#   Little Endian
def little_endian_to_int(data:bytes):
    multiply = 1
    res = 0
    for ii in data:
        res += ii * multiply
        multiply *= 256
    return res

#
# size, value = varint()
#  (0, -1) => Incorrect Input
def varint(data:bytes):
    size = len(data)
    if size == 0:
        return  0, -1
    elif size > 9:
        size = 9
        data = data[:9]
    #
    counter = 0
    for jj in data:
        counter += 1
        if jj < 128 :
            break
        if counter == size:
            return 0, -1
    #
    data = data[:counter][::-1]
    multiply = 1
    res = 0
    isFirst = True
    #
    for ii in data:
        if isFirst:
            res = ii
            isFirst = False
        else:
            res += (ii-128) * multiply
        multiply *= 128
    return counter, res


#   00 00 00 01 = 1
#   Big Endian
def big_endian_to_IEEE_754_2008__64_bit(data:bytes):
    if len(data) == 8:
        return True, struct.unpack('>d', data)[0]
    else:
        return  False, -1

#
# size, type, comment = headertype(val:int)
def headertype(val:int):
    if   val == 0:
        return 0, 0, """Value is a NULL"""
    elif val == 1:
        return 1, 1, """Value is an 8-bit twos-complement integer"""
    elif val == 2:
        return 2, 1, """Value is a big-endian 16-bit twos-complement integer"""
    elif val == 3:
        return 3, 1, """Value is a big-endian 24-bit twos-complement integer"""
    elif val == 4:
        return 4, 1, """Value is a big-endian 32-bit twos-complement integer"""
    elif val == 5:
        return 6, 1, """Value is a big-endian 48-bit twos-complement integer"""
    elif val == 6:
        return 8, 1, """Value is a big-endian 64-bit twos-complement integer"""
    elif val == 7:
        return 8, 2, """Value is a big-endian IEEE 754-2008 64-bit floating point number"""
    elif val == 8:
        return 0, 3, """Value is the integer 0 (Only available for schema format 4 and higher)"""
    elif val == 9:
        return 0, 4, """Value is the integer 1 (Only available for schema format 4 and higher)"""
    elif val == 10 or val == 11:
        return -1, 5, """Reserved for internal use"""
    elif val == 12:
        return 0, 6, """Value is a BLOB that is (N-12)/2 bytes in length"""
    elif val == 13:
        return 0, 7, """Value is a string in the text encoding and (N-13)/2 bytes in length (The null terminator is not stored)"""
    elif val > 13:
        if val%2 == 0:
            return int((val-12)/2), 6, """Value is a BLOB that is (N-12)/2 bytes in length"""
        elif val%2 == 1:
            return int((val-13)/2), 7, """Value is a string in the text encoding and (N-13)/2 bytes in length (The null terminator is not stored)"""
        else:
            return -1, 8, """Error!"""
    else:
        return -1, 8, """Unknown"""


#
#   codecs = "UTF-8", "UTF-16LE", "UTF-16BE"
#   type   = 0,1,2,3,4,5,6,7,8,9
#   data   = bytes
#
#   headervalue( codecs="UTF-8", 1, b'\x01' )
def headervalue(codecs:str, type:int, data:bytes):
    try:
        if type == 0:
            return True, "NULL", 0, "Null"
        elif type == 1:
            return True, big_endian_to_int(data), 1, "Int"
        elif type == 2:
            res = big_endian_to_IEEE_754_2008__64_bit(data)
            return res[0], res[1], 2, "Floating_point_number_(IEEE_754-2008_64-bit)"
        elif type == 3:
            return True, 0,  1, "Int"
        elif type == 4:
            return True, 1,  1, "Int"
        elif type == 5:
            return False, "", 5, "Reserved"
        elif type == 6:
            if data is not None:
                if len(data) == 0:
                    data = b''
            else:
                data = b''
            return True, data, 6, "Blob"
        elif type == 7:
            if data is not None:
                if len(data) == 0:
                    res = ''
                else:
                    enc = "utf-8"
                    if codecs == "UTF-8":
                        enc = "utf-8"
                    elif codecs == "UTF-16LE":
                        enc = "utf_16_be"
                    elif codecs == "UTF-16BE":
                        enc = "utf_16_le"
                    #
                    res = data.decode(encoding=enc, errors="strict")
            else:
                res = ''
            return True, res, 7, "String"
        elif type == 8:
            return False, b'', 8, "Error!"
        elif type == 8:
            return False, b'', 9, "Unknown!"
    #
    except:
        return False, b'', 8, "Error!"


