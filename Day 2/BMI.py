height=float(input("ENTER YOUR HEIGHT \n"))
weight=float(input("ENTER YOUR WEIGHT \n"))
bmi=(int(weight)/float(height) ** 2)
print(int(bmi))
if(bmi<18.5):
    print("UNDERWEIGHT")
elif(bmi>18.5 and bmi<25):
    print("normal weight")
elif(bmi>25 and bmi<35):
    print("overweight")
else:
    print("Obese")
#THANKYOU