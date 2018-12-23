# -*- coding: utf-8 -*-
import xlsxwriter
import json

filee = open('data.json', 'r') 
data = filee.readline()
data = json.loads(data)

result = []
free_barcode = 5555555555
for row in data:
    tmp=[]
    # isbn == stt
    tmp.append(row[0])
    # khpl
    tmp.append(row[1])
    # book no
    tmp.append("")
    # author
    tmp.append(row[4])
    # title
    tmp.append(row[2])
    # sub title
    tmp.append("")
    # nhan de chinh
    tmp.append("")
    # Lan xuat ban
    tmp.append("")
    # Noi xuat ban
    tmp.append("")
    # Nguoi nhap lieu
    tmp.append("BK Library system")
    # Nam xuat ban
    tmp.append(row[5])
    # So trang
    tmp.append("0p")
    # seri
    tmp.append("")
    # volume
    tmp.append(row[3])
    # Ghi chu chung
    tmp.append("Sách giấy")
    # subject
    tmp.append("")
    # 700$a
    tmp.append("")
    # url 
    tmp.append("")
    # Pernament library
    tmp.append("CL")
    # Current Library
    tmp.append("CL")
    # Location
    tmp.append(row[7])
    # Items type
    tmp.append("BK")
    # Barcode
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
                    if tmp_row[22] == tmpp_bar:
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
    # call no
    tmp.append("")
    # items type 942$c
    tmp.append("BK")
    result.append(tmp)

import codecs
with codecs.open('data_as_marc.json', 'w', encoding='utf8') as filehandle:
    filehandle.write(json.dumps(result))

