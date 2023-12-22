# CREATE A FUNCTION CALLED GREET().
# WRITE 3 PRINT STATEMENTS INSIDE IT.
# CALL THE GREET FUNCTION AND RUN YOUR CODE.

# def greet():
#     print("Hello There")
#     print("This is Chandan")
#     print("Thankyou , Saiyonaara")

# greet()


# NOW PASSING VALUES INTO THE FUNCTION 

# def greet(user):
#     print(f"Hello {user}")
#     print(f"Nice to meet you {user}, It's Zephyrus-001")
#     print(f"Thankyou {user} for visiting, Saiyonaara")

# # user=""
# greet("chandan")


# NOW FUNCTION WITH MORE THAN ONE INPUTS
# PARAMETERS WILL BE(NAME,LOCATION)

def greet(user,location):
    print(f"Hello {user}")
    print(f"Nice to meet you {user}, It's Zephyrus-001")
    print(f"so your location is {location}")
    print(f"Thankyou {user} for visiting, Saiyonaara")

greet("chandan", "Jamshedpur")
# greet("Jamshedpur", "chandan") #POSITIONAL ARGUMENT

# TO AVOID MIS-POSITIONING THE ARGUMENTS , WE USE KEYWORD ARGUMENTS (NAMING THE VALUES)
# EXAMPLE :
greet(location="Jamshedpur", user="chandan")