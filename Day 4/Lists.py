#in python lists always starts/ends with a square bracket with elements inside it with a comma 

#storing all the names of states of india in a list

# name1="Delhi"
# name2="Jharkhand"
# name3="Tamil Nadu"

#instead of storing them in separate variables for each, we can create a list for all
import random

states_of_india = ["Delhi","Jharkhand","Tamil Nadu"]

index=random.randint(0,2)

print(states_of_india[index])

#using positive index value starts counting the data inside the list from the starting 

#similarly using the negative index value , it starts from the end of the list

# example

print(states_of_india[-2]) #this will print the data = "Tamil Nadu" (end of the list)


#TO Add some data into the list , you can use the .append() function

states_of_india.append("ChandanLand") #using .append() function adds the data to the end of the list
print(states_of_india[-1])


# TO add another list at the end of one list , you can use the .extend() function
# Example

states_of_india.extend(["RajuLand","MummiJiKaMahal","PapaKaMahal"])
print(states_of_india)


# Don't remember everything , just read and remember that it is possible, search google for these methods

#index out of range error if the given index value is greater than the size of list
# print(states_of_india[50])

length=len(states_of_india)
print(states_of_india[length-1])


