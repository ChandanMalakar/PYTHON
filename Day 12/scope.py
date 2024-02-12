# outsider=12

# def access():
#     outsider=14
#     print(f"inside function {outsider}")

# print(f"outside function {outsider}")
# access()

# Local Scope
# any variable value which is inside 
# a function
# can't be accessed from outside
# this is known as local scope

def potion_drinking():
    potion_maker=12
    print(potion_maker)

potion_drinking()
# print(potion_maker) # error

# Global Scope

# even if a varibale is defined
# outside the function, its value can be 
# accessed from the outside of the function

health_max=10

def game():
    def potion_drinking():
        print(health_max)

    potion_drinking()

# local variables are those which are defined inside the function
# global variables are those which are defined outside the function

# this concept applies not only to 
# variables but also to functions and also this concept applies
# to anything you name

# anything you give a name to , it may be functions,variables,etc has a
# namespace.

# there is no block scope means there is no use of curly braces to express
# a certain block of code , instead indentation works in python.
    
# if you create a variable within a function, then its only available within
# that function only.

# Modifying Global Scope
    
# all the changes made in global variable won't affect the local one
# it is the same for the local variable.

# there is no block scope in python
    
# only local scope is there in functions and classes
    
# not in if statements

game_level=3
# def create_enemy():
enemies=["Skeleton","Zombie","Alien"]
if game_level<5:
    new_enemy=enemies[0]
    
print(new_enemy)

enemies=1

def increase_enemies():
    enemies+=1
    print(f"enemies inside function {enemies}")

increase_enemies()
print(f"enemies outside function {enemies}")


# Global Constants

# constants are those variables whose value never changes
# they are written in capital letters
# and are separated by underscores

PI=3.14159
URL="https://www.google.com"


