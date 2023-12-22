# WE ARE GOING TO MAKE A PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT

# THIS ONE IS MY METHOD

# def prime(number):
#     k=0
#     for i in range(2,number):
#         if number%i==0:
#             k=k+1
#     if k>0:
#         print("Not a prime number ")
#     else:
#         print("Prime number")

# THIS ONE IS TEACHER'S METHOD

def prime(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


n=int(input("Enter a number : "))
prime(number=n)