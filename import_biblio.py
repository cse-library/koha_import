# -*- coding: utf-8 -*
from xlrd import open_workbook

from utils import str_sql_refactor

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

query = """INSERT INTO biblio"""
i = 0
for row in data:
    if i == 0:
        query += ' VALUES '
        i += 1
        continue
    row4=str_sql_refactor(row[4])
    row2=str_sql_refactor(row[2])
    query += """(%d,'BMN','%s','%s',NULL,'không',NULL,NULL,0,'2018-11-10 04:33:21','2018-11-09','%s'),"""%(int(row[0]), row4, row2, row2)
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
with open('biblio.sql', 'w') as filehandle:  
    filehandle.write(query)
