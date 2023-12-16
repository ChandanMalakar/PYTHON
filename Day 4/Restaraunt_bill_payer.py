import random


name_string=input("Enter the names of your colleagues separated with commas and space : ")
names=name_string.split(", ") #this function is used to convert the string elements to individual list elements
#the .split() function divides the string based on the given parameter (here , it is a comma with a space)
# it identifies the separator given as parameters and seperates the string as a part of list
print(names)
length=len(names) #used to find total number of items in the list
index=random.randint(0,length-1)

print(f"The Payment will be done by {names[index]} for the meal today")


#We can use random.choice() function to automatically choose one item from the list and display it

#example:

payer=random.choice(names)
print(f"THe payment will be done by {payer}")