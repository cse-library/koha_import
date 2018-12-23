# -*- coding: utf-8 -*-
import xlsxwriter
import json

workbook = xlsxwriter.Workbook('books_as_marc_part5.xlsx')
worksheet = workbook.add_worksheet()

array = None
filee = open('data_as_marc.json', 'r') 
data = filee.readline()
array = json.loads(data)

for row, data in enumerate(array):
    if row > 40000 and row <= 400000:
        for col, cel in enumerate(data): 
            worksheet.write(row, col, cel)
workbook.close()
