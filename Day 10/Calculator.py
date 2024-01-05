from art import logo


# num1=float(input("What's the first number? : "))
# print('+\n''-\n''*\n''/\n')



# def calculation(num1):
#     operation=input("Pick an operation : ")
#     num2=float(input("What's the next number? : "))
#     if operation=='+':
#         res=num1+num2
#         print(f"{num1} {operation} {num2} = {res}")
#         ask(res)
#     elif operation=='-':
#         res=num1-num2
#         print(f"{num1} {operation} {num2} = {res}")
#         ask(res)
#     elif operation=='*':
#         res=num1*num2
#         print(f"{num1} {operation} {num2} = {res}")
#         ask(res)
#     elif operation=='/':
#         res=num1/num2
#         print(f"{num1} {operation} {num2} = {res}")
#         ask(res)
#     else:
#         print("Invalid Choice")

# def ask(result):
#     case=input(f"Type 'y' to continue calculating with {result} , or type 'n' to stat a new calculation : ")
#     if case=='y':
#         calculation(result)

# calculation(num1)



def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2


operation={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1=float(input("What's the first number ? "))

    for symbol in operation:
        print(symbol)

    should_continue=True

    while should_continue:
        operation_symbol=input("Pick an operation : ")
        working_function=operation[operation_symbol]
        num2=float(input("What's the next number? : "))
        calculate=working_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {calculate}")
        if input(f"Type 'y' to continue calculating with {calculate} , or type 'n' to stat a new calculation : ")=='y':
            num1=calculate
        else:
            should_continue=False
            calculator()

calculator()
