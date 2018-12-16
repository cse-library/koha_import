from xlrd import open_workbook
import json

with open('types.json', 'r') as filehandle:  
    data = filehandle.read()
data = json.loads(data)

query = """INSERT INTO itemtypes VALUES """
for row in data:
    string_list = row.split()
    mini_name = ""
    for string in string_list:
        if string != "":
            #if string.isupper():
            #    mini_name += string
            if "CS" in string:
                child_list = string.split('_')
                print child_list
                for child_str in child_list:
                    if "CS" in child_str:
                        mini_name += child_str
                        print mini_name
                    else:
                        mini_name += child_str[0:1]
            else:
                mini_name += string[0:1]
    query += """('%s','%s',0.000000,0.000000,0.000000,0,'vokal/Book.png','','','message',NULL,0,''),"""%(mini_name, row)
if query.endswith(','):
    query = query[:len(query)-1]
    query += ';'
print query
import codecs
with codecs.open('types.sql', 'w', encoding='utf8') as filehandle:  
    filehandle.write(query)
