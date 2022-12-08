#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict ={key: val for key, val in test_dict.item() if key != a_dictionary}
    print("The dictionary after remove is : " + str(new_dict))
