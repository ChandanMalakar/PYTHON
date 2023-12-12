# THIS IS A ROLLER COASTER RIDE ELIGIBILITY CHECKING PROGRAM


height=float(input("Enter your height in cm: "))
if height>=120:
    print("You can ride the roller coaster")
    age=int(input("Enter your age : "))
    bill=0
    if age<12:
        bill=5
        print("Child tickets are $5")
    elif age<=18:
        bill=7
        print("Youth tickets are $7")
    else:
        bill=12
        print("adult tickets are $12") 
    message=input("Do you want a photo taken? Y or N: ")
    if message=="Y":
        bill+=3
        print("Photo is $3")
    
    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the roller coaster")


