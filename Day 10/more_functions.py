# def my_function():
#     result=2*3
#     return result

# print(my_function())


def format_name(str1,str2):
    new_str=str1+" "+str2
    new_str=new_str.title()
    return new_str


fname=input("Enter your first name : ")
lname=input("Enter your last name : ")
print(format_name(fname,lname))