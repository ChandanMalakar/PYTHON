# THIS IS A ROLLER COASTER RIDE ELIGIBILITY CHECKING PROGRAM


height=float(input("Enter your height in cm: "))
if height>=120:
    print("You can ride the roller coaster")
    age=int(input("Enter your age : "))
    if age<12:
        print("Please pay $5")
    elif age>=12 and age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12") 
else:
    print("You cannot ride the roller coaster")

