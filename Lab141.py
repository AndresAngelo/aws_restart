"""
Your module description - Challenge Lab: Python Scripting Exercise
"""

### Student Name: Angelo E. Andres
### Class Code: PHMAN 26 - Evening Class
### Date & Time: January 9, 2024 Thursday 4:00am
### project description: This is a simple coding project that outputs all prime numbers between 1 to 250
        
        
### a side function to determine whether a number passed here (x) is a prime number      
def isPrime(x):
    ### halved variable came to existence to ensure that we reduce the runtime of the for loop inside this function, as the upper part of the given number always produces a false return (0)
    halved = x/2
    ### an explicit condition to remove 1 in the for loop equation because it considers number 1 as divisible to itself AND has no other positive divisors, but it is not a prime number.
    if(x == 1):
        return 0
    ### this for loop equation considers the range starting from 2, to the integer version of the halved variable but its upper limit.
    for y in range(2, int(halved+1)):
        ### this condition makes x (the given number from the for loop 1 - 250) and y(the given number starting in 2 to halved of x) be divided,
        ### then passes through is_integer function to check whether the result is an integer number or without decimal or a fraction of a number.
        ### It then asks whether the result in is_integer is true or not.
        if (x/y).is_integer() == True:
            ### It will then proceed looping back if the result is True that this passed parameter number (x) has a divisible postive number lower than itself.
            return 0
    ### It will return 1 if all iterations have been tested and will now be considered as a prime number by isPrime function.
    return 1

### The main function. This function starts with a for loop of the numbers 2 - 250.
for x in range (1, 250):
    #This condition is just here to simplify whether the isPrime function produces a true or false return, giving us a filtration to print only prime numbers
    if isPrime(x):
        print(x)
    