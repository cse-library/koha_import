# -*- coding: utf-8 -*-
from xlrd import open_workbook
import re, json
from utils import *


wb = open_workbook('data.xlsx')

values = []
for s in wb.sheets():
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
free_barcode = 5555555555
data = values
result = []
for row in data:
    tmp=[]
    tmp.append(row[0])
    tmp.append(row[1])
    tmp.append(row[2])
    tmp.append(row[3])
    tmp.append(row[4])
    tmp.append(row[5])
    barcode = ""
    if row[6] != "":
        if len(row[6]) <= 10:
            barcode = row[6]
        else:
            num_str = "1234567890"
            tmp_arr_barcode = []
            tmp_bar = ""
            for charr in row[6]:
                if charr in num_str:
                    tmp_bar += charr
                else:
                    if len(tmp_bar) > 0:
                        tmp_arr_barcode.append(tmp_bar)
                        tmp_bar = ""
                    continue
            for tmpp_bar in tmp_arr_barcode:
                if barcode != "":
                    break
                for tmp_row in result:
                    if tmp_row[6] == tmpp_bar:
                        print "tmp_row[6]"+"#####"+tmpp_bar
                        continue
                    else:
                        barcode = tmpp_bar
                        #print barcode
                        break
            if barcode == "":
                barcode = str(free_barcode)
                free_barcode += 1
        #print barcode
    else:
        #print barcode
        barcode = str(free_barcode)
        free_barcode += 1
    tmp.append(barcode)
    print barcode
    tmp.append(row[7])
    result.append(tmp)

import codecs
with codecs.open('data.json', 'w', encoding='utf8') as filehandle:
    filehandle.write(json.dumps(result))

