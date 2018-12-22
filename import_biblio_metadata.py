# -*- coding: utf-8 -*
from xlrd import open_workbook

from utils import str_sql_refactor, get_type

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

#query = """INSERT INTO biblio_metadata"""
query = ""
for i,row in enumerate(data):
    if i == 0:
        #query += ' VALUES '
        continue
    elif i> 100:
        break
    idd = int(row[0])
    title=str_sql_refactor(row[2])
    khpl = str_sql_refactor(row[1])
    author = str_sql_refactor(row[4])
    typee = get_type(row[7])
    metadata="""<?xml version="1.0" encoding="UTF-8"?>
<record
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"
    xmlns="http://www.loc.gov/MARC21/slim">

  <leader>" "</leader>
  <datafield tag="999" ind1=" " ind2=" ">
    <subfield code="c">%d</subfield>
    <subfield code="d">%d</subfield>
  </datafield>
  <datafield tag="082" ind1=" " ind2=" ">
    <subfield code="a">%s</subfield>
    <subfield code="b">" "</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">%s</subfield>
  </datafield>
  <datafield tag="242" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">%s</subfield>
    <subfield code="b">" "</subfield>
    <subfield code="c">" "</subfield>
    <subfield code="n">" "</subfield>
    <subfield code="p">" "</subfield>
  </datafield>
  <datafield tag="250" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="500" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="600" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="651" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="653" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
  </datafield>
  <datafield tag="856" ind1=" " ind2=" ">
    <subfield code="d">" "</subfield>
    <subfield code="u">" "</subfield>
  </datafield>
  <datafield tag="910" ind1=" " ind2=" ">
    <subfield code="a">" "</subfield>
    <subfield code="c">Thuong</subfield>
  </datafield>
  <datafield tag="942" ind1=" " ind2=" ">
    <subfield code="2">" "</subfield>
    <subfield code="c">%s</subfield>
  </datafield>
</record>"""%(idd, idd, khpl, author, title, typee.encode('utf-8'))

    #(idd, idd, khpl, author, title, typee)
    metadata = str_sql_refactor(metadata)
    query += """INSERT INTO biblio_metadata VALUES """
    query += """(%d,%d,'marcxml','MARC21','%s','2018-11-10 04:33:21');"""%(int(row[0]), int(row[0]), metadata)
    query += "\n"
# if query.endswith(','):
#    query = query[:len(query)-1]
#    query += ';'
#print query
with open('100_metadata.sql', 'w') as filehandle:  
    filehandle.write(query)
