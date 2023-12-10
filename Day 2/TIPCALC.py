# print("Welcome to the Tip Calculator")
# total=float(input("What is the total bill amount ? $"))
# num=float(input("How many people to split the bill? "))
# tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# amt=float(total+(total*(tip/100)))
# new_amt=round(amt/num,2)
# print("Each person should pay : $"+str(new_amt))

#OR

print("Welcome to the Tip Calculator")
total=float(input("What is the total bill amount ? $"))
num=int(input("How many people to split the bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
new_tip=(tip/100+1.0)
amt=round(((total*new_tip)/num),2)
print(f"Each person should pay : ${amt}")
