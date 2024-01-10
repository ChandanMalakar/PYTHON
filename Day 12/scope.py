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

def potion_drinking():
    print(health_max)

potion_drinking()


# local variables are those which are defined inside the function
# global variables are those which are defined outside the function


# this concept applies not only to 
# variables but also to functions and also this concept applies
# to anything you name


