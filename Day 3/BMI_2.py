height=float(input("Please enter your height in m: "))
weight=int(input("Please enter your weight in kg: "))
bmi=round(weight/height**2)

if bmi<18.5:
    print(f"Your BMI is : {bmi} , You're Underweight")
elif bmi<25:
    print(f"Your BMI is : {bmi} , You're normal weight")
elif bmi<30:
    print(f"Your BMI is : {bmi} , You're overweight")
elif bmi<35:
    print(f"Your BMI is : {bmi} , You're obese")
else:
    print(f"Your BMI is : {bmi} , You're clinically obese")

#THANKYOU