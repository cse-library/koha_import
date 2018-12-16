# -*- coding: utf-8 -*-
def get_type(string):
    string_list = string.split()
    mini_name = ""
    for string in string_list:
        if string != "":
            #if string.isupper():
            #    mini_name += string
            if "CS" in string:
                child_list = string.split('_')
                for child_str in child_list:
                    if "CS" in child_str:
                        mini_name += child_str
                    else:
                        mini_name += child_str[0:1]
            else:
                mini_name += string[0:1]
    return mini_name

def str_sql_refactor(string):
    result = ""
    result=string.encode("utf-8").replace('"', '\\"')
    result=result.replace("'", "\\'")
    return result
