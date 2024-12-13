"""
Your module description - Lab 110: Working with String Data Type
"""

#representation of a string variable
myString = "This is a string."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type " + str(type(myString)))

#representation of concatenation
firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#basic input function
name = input("What is your name?: ")
print(name)

#basic outputting inputted variables
color = input("What is your favorite color?: ")
animal = input("What is your favorite animal?: ")
print("{}, you like a {} {}!".format(name, color, animal))