from xlrd import open_workbook

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

query = """INSERT INTO biblioitems ( biblioitemnumber, biblionumber, volume, itemtype ) """
i = 0
for row in data:
    if i == 0:
        query += 'VALUES'
        i += 1
        continue
    query += """(%d, %d, "%s", "%s" ),"""%(int(row[0]), int(row[0]), row[3].encode("utf-8"), row[1].encode("utf-8"))
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
with open('biblioitems.sql', 'w') as filehandle:  
    filehandle.write(query)
