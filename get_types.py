from xlrd import open_workbook
import json

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

i = 0
type_list = []
for row in data:
    if i == 0:
        i += 1
        continue
    if row[7] not in type_list:
        type_list.append(row[7])
#print query
with open('types.json', 'w') as filehandle:  
    filehandle.write(json.dumps(type_list))
