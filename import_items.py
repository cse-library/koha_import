# -*- coding: utf-8 -*-
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

query = """INSERT INTO items ( itemnumber, biblionumber, biblioitemnumber, barcode, homebranch, notforloan, damaged, itemlost, withdrawn, coded_location_qualifier, restricted, location, permanent_location, itype) """
i = 0
for row in data:
    if i == 0:
        query += 'VALUES'
        i += 1
        continue
    #print str(row[7])
    more_subfields_xml = """ <?xml version="1.0" encoding="UTF-8"?>
<collection
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"
  xmlns="http://www.loc.gov/MARC21/slim">

<record>
  <leader> </leader>
  <datafield tag="" ind1=" " ind2=" ">
    <subfield code="f">%s</subfield>
    <subfield code="f">%s</subfield>
    <subfield code="x"></subfield>
    <subfield code="x"></subfield>
  </datafield>
</record>

</collection>
               enumchron: NULL
              copynumber: NULL
             stocknumber: NULL
              new_status: NULL"""
    query += """(%d, %d, %d, "%s", "%s", %d, %d, %d, %d, "%s", %d, "%s", "%s", "%s" ),"""%(int(row[0]), int(row[0]), int(row[0]), row[6], "CLIB", -1, 1, 1, 1, row[7] if row[7] else "", 1, "CART", "CART", row[1])
#print data
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
#print query
with open('items.sql', 'w') as filehandle:  
    filehandle.write(query.encode('utf-8'))
