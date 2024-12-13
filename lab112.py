"""
Your module description - Lab112: Categorizing Values
"""

#representation of Lists having capable of multiple data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog in on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
    