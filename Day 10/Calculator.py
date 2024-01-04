print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")


num1=float(input("What's the first number? : "))
print('+\n''-\n''*\n''/\n')



def calculation(num1):
    operation=input("Pick an operation : ")
    num2=float(input("What's the next number? : "))
    if operation=='+':
        res=num1+num2
        print(f"{num1} {operation} {num2} = {res}")
        ask(res)
    elif operation=='-':
        res=num1-num2
        print(f"{num1} {operation} {num2} = {res}")
        ask(res)
    elif operation=='*':
        res=num1*num2
        print(f"{num1} {operation} {num2} = {res}")
        ask(res)
    elif operation=='/':
        res=num1/num2
        print(f"{num1} {operation} {num2} = {res}")
        ask(res)
    else:
        print("Invalid Choice")

def ask(result):
    case=input(f"Type 'y' to continue calculating with {result} , or type 'n' to stat a new calculation : ")
    if case=='y':
        calculation(result)

calculation(num1)



