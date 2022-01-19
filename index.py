#!/usr/bin/env python
import json
from os import name

#########################################################################
#console menu 
menu_option = {                                                         #
    1: "\t\t\t1.Update",  # sửa                                         #
    2: "\t\t\t2.Delete",  # xóa                                         #
    3: "\t\t\t3.insert",  # thêm                                        #
    4: "\t\t\t4.search",  # tìm kiếm                                    #
    5: "\t\t\t5.show data",                                             #
    6: "\t\t\t6.Exit!",                                                 #
}   
#########################################################################

def print_menu():                                                       #
    for key in menu_option.keys():                                      #
        print(menu_option[key])                                         #
#########################################################################

#########################################################################        
#convert char                       
def convertChar(char):                                                  #
    if char >= "A" and char <= "Z":                                     #
        return chr(ord(char) + 32)                                      #
                                                                        #
    return chr                                  
#########################################################################

#########################################################################
def toLowerCase(string):
    newString = []                                                      #
    for char in string:                                                 #
        newString.append(convertChar(char))                             #
    return "".join(newString)
#########################################################################

#########################################################################
def insert(dict):                                       
    input_key = input("\t\t\tEnter english word: ")                     #
    input_value = input("\t\t\tEnter vietnamese word: ")                #
    cv_key = toLowerCase(input_key)                                     #
    cv_value = toLowerCase(input_value)                                 #
    if cv_key not in dict:                                              #
        dict[cv_key] = cv_value                                         #
    else:                                                               #
        print("\t\t\tduplicate. add temp value!")                       #
        # dict[cv_key] = [dict[cv_key], cv_value]
        
#########################################################################

#########################################################################
def update(dict):
    input_key = input("\t\t\tenter english word want to found: ")       #
    input_value = input("\t\t\tenter replace vietnamese word: ")        #
    cv_key = toLowerCase(input_key)                                     #
    cv_value = toLowerCase(input_value)                                 #
    if cv_key in dict:                                                  #
        dict[cv_key] = cv_value                                         #
    else:                                                               #
        print("\t\t\t{} not found".format(input_key))                   #

#########################################################################

#########################################################################
def delete(dict):
    input_key = input("\t\t\tenter english word delete: ")              #
    cv_key = toLowerCase(input_key)                                     #
    if cv_key in dict:                                                  #
        del dict[cv_key]                                                #
        print("\t\t\t{} deleted ".format(cv_key))                       #
    else:                                                               #
        print("\t\t\t{} not found".format(cv_key))                      #

#########################################################################

#########################################################################
def search(dict):   
    input_key = input("\t\t\tenter english word want to find: ")        #
    cv_key = toLowerCase(input_key)                                     #
    if cv_key in dict:                                                  #
        print("\t\t\tyour vietnamese word: " + dict[cv_key])            #
    else:                                                               #
        print("\t\t\t{} not exist.".format(cv_key))                     #

#########################################################################

#########################################################################
def load_file(file_path):   
    with open(file_path, encoding="utf-8") as f:                        #
        f_load = json.loads(f.read())                                   #
        return f_load                                                   #
    
#########################################################################

#########################################################################
def save_file(file_path, dict):
    with open(file_path, "w", encoding="utf-8") as f:                   #
        f.write(json.dumps(dict))                                       #

#########################################################################
        
#########################################################################
if __name__ == "__main__":
    file_path = "dict.txt"
    dict = load_file(file_path)
    init_dict = dict
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("\t\t\tEnter your choice: "))
        except:
            print("\t\t\tWrong input. Please enter a number ...")
        # Check what choice was entered and act accordingly
        if option == 1:
            print("\t\t\t--- UPDATE")
            update(dict)
            save_file(file_path, init_dict)
            print("\t\t\tUPDATE success!")
        elif option == 2:
            print("\t\t\t--- DELETE")
            delete(dict)
            save_file(file_path, dict)
        elif option == 3:
            print("\t\t\t---INSERT")
            insert(dict)
            save_file(file_path, dict)
        elif option == 4:
            print("\t\t\t---SEARCH")
            search(dict)
        elif option == 5:
            print("\t\t\t SHOW DATA")
            print(dict)
        elif option == 6:
            print("\t\t\tDo you wanna close app!")
            exit()
        else:
            print("\t\t\tInvalid option. Please enter a number between 1 and 6.")
