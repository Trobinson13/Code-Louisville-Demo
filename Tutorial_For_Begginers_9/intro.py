# Below are a few exmaples on how to import the module along with how to call its "find_index" function

#import my_module
#index = my_module.find_index(courses, "Physics")

#import my_module as mm
#index = mm.find_index(courses, "Physics")

import sys
sys.path.append(
    "/Users/tre.robinson/Documents/GitHub/Code-Louisville-Demo/Test_Dir_For_TFB9/")

from my_module import find_index, test

courses = ["History", "Math", "Physics", "CompSci"]
index = find_index(courses, "Physics")
print(index)
print(test)
