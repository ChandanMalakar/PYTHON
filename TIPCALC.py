print("Welcome to the Tip Calculator")
total=float(input("What is the total bill amount ? $"))
num=int(input("How many people to split the bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
amt=float((total/num)*(12/100))
print("Each person should pay : $ {amt}")
