"""
Your module description - Lab 111: Working with Lists, Tuples, Dictionaries
"""

#representation of Lists data type
myFruitList = ["Apple",  "Banana", "Cherry"]
print(myFruitList)
print(type(myFruitList))

#representation of indexing in Lists
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#mutability of Lists
myFruitList[1] = "Orange"
print(myFruitList)

#representation of Tuples data type
myFinalAnswerTuple = ("Apple", "Banana", "Pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#mutability of Tuples
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#representation of Dictionaries data type
myFavoriteFruitDictionary = {
    "Akua" : "Apple",
    "Saanvi" : "Banana",
    "Paulo" : "Pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#accessing  Dictionary values through keys
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])