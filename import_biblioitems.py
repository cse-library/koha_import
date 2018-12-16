# -*- coding: utf-8 -*
from xlrd import open_workbook
from utils import get_type

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

query = """INSERT INTO biblioitems"""
i = 0
for row in data:
    if i == 0:
        query += ' VALUES '
        i += 1
        continue
    # default 999 pages
    row7 = get_type(row[7])
    #print row
    row3=row[3] if row[3].encode('utf-8') else ""
    query += """(%d,%d,'%s',NULL,'%s',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-11-10 02:35:23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL),"""%(int(row[0]), int(row[0]), row3, row7)
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
import codecs
with codecs.open('biblioitems.sql', 'w', encoding='utf8') as filehandle:
    filehandle.write(query)

