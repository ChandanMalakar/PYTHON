print("RANDOM NUMBERS")
#THANKYOU

import random

random_number=random.randint(1,10)

print(random_number)


#importing the created module {module_creation.py} in this program

import module_creation

print(module_creation.pi) #this is how you use variables from another program using the module

#printing random floating point numbers

random_float=random.random()
print(random_float)

#printing floating point numbers between 0 and 5

random_float=random.random()*5
print(random_float)