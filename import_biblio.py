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

query = """INSERT INTO biblio ( biblionumber, frameworkcode, author, title, datecreated ) """
i = 0
for row in data:
    if i == 0:
        query += 'VALUES'
        i += 1
        continue
    row4=row[4].encode("utf-8").replace('"', '\\"')
    row4=row4.replace("'", "\\'")
    row2=row[2].encode("utf-8")
    row2=row2.replace("'", "\\'")
    query += """(%d, '%s', '%s', '%s', '1970-01-01 00:00:00' ),"""%(int(row[0]), "BMN", row4, row2)
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
with open('biblio.sql', 'w') as filehandle:  
    filehandle.write(query)
