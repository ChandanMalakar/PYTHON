

#using sub-scripting
num=input("Enter a two digit number : ")
num1=num[0]
num2=num[1]
res=int(num1)+int(num2)
print(res)

#using type conversion
num=int(input("Enter a two digit number : "))
num1=int(num%10)
num2=int(num/10)
print(num1+num2)