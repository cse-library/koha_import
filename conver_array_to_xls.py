# -*- coding: utf-8 -*-
import xlsxwriter
import json

workbook = xlsxwriter.Workbook('books_part0.xlsx')
worksheet = workbook.add_worksheet()

array = None
filee = open('data.json', 'r') 
data = filee.readline()
array = json.loads(data)

for row, data in enumerate(array):
    if row > 0 and row <= 10000:
        for col, cel in enumerate(data): 
            worksheet.write(row, col, cel)
workbook.close()
