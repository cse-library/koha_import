# -*- coding: utf-8 -*-
from xlrd import open_workbook
import re
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
data = values

query = """INSERT INTO items"""
i = 0
bacode_tmp = 5555555555
for row in data:
    if i == 0:
        query += ' VALUES '
        i += 1
        continue
    barcode = ""
    if row[6] != "":
        if ';' in row[6]:
            barcode_list = row[6].split(';')
            barcode = str(barcode_list[0])
        elif ',' in barcode:
            barcode_list = row[6].split(',')
            barcode = barcode_list[0]
        elif " " in barcode:
            barcode_list = row[6].split(' ')
            barcode = barcode_list[0]
        elif "\n" in barcode:
            barcode_list = row[6].split('\n')
            barcode = barcode_list[0]
        else:
            barcode = row[6]
        if barcode == "":
            barcode = str(bacode_tmp)
            bacode_tmp += 1
        elif barcode in query:
            barcode = str(bacode_tmp)
            bacode_tmp += 1
    row7 = get_type(row[7])
    more_subfields_xml = """<collection
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"
  xmlns="http://www.loc.gov/MARC21/slim">

<record>
  <leader>         a              </leader>
  <datafield tag="999" ind1=" " ind2=" ">
    <subfield code="f">" "</subfield>
  </datafield>
</record>

</collection>"""
    more_subfields_xml = ""#str_sql_refactor(more_subfields_xml) 
    query += """(%d,%d,%d,'%s','2018-11-09',NULL,'CLIB',0.00,0.00,'2018-11-09',NULL,'2018-11-09',NULL,-1,1,NULL,3,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'CLIB',NULL,'2018-11-10 05:22:21','CART','CART',NULL,NULL,NULL,'FIC',NULL,'000','%s','%s',NULL,'0',NULL,NULL),"""%(int(row[0]), int(row[0]), int(row[0]), barcode, row7, more_subfields_xml)
#print data
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
import codecs
with codecs.open('witems.sql', 'w', encoding='utf8') as filehandle:
    filehandle.write(query)
