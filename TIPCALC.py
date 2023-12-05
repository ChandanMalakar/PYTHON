print("Welcome to the Tip Calculator")
total=float(input("What is the total bill amount ? $"))
num=float(input("How many people to split the bill? "))
tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))

amt=float(total+(total*(tip/100)))
new_amt=(amt/num)
print("Each person should pay : $"+str(new_amt))
