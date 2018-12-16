# -*- coding: utf-8 -*-
def get_type:
    if string != "":
        mini_name += string
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
    return None
