# HERE WE ARE GOING TO MAKE A TOOL TO ENCRYPT OR DECRYPT 
# A MESSAGE.

# STEP 1 - 
# WE WILL CREATE A LIST CONTAINING THE 2 CHOICES
# ENCODE AND DECODE
# TAKE ONE STRING INPUT FROM THE USER AND COMPARE 
# WITH THE LIST ITEM
# AND THEN DO THE NECESSARY PROCESSING 

from art import logo
print(logo)




# THIS IS MY PRECIOUS CODE USING THE ASCII

# list=['encode', 'decode']
# user_choice=input("Type 'encode' to encrypt, type 'decode' to decrypt :\n")
# new_message=""
# once_again=False
# while not once_again:
#     if user_choice in list:
#         message=input("Type your message :\n")
#         shift_number=int(input("Type the shift number :\n"))
#         if user_choice=='encode':
#             for i in message:
#                 dup=ord(i)
#                 dup+=shift_number
#                 dup=chr(dup)
#                 new_message+=dup
#             print(f"Your encoded message is : {new_message}")
#         else:
#             for i in message:
#                 dup=ord(i)
#                 dup-=shift_number
#                 dup=chr(dup)
#                 new_message+=dup
#             print(f"Your decoded message is : {new_message}")
#     else:
#         print("Invalid choice")
#     take=input("Type 'Yes' if you want to go again OR Type 'No' if you don't :\n")
#     if(take=='Yes'):
#         once_again=False
#     else:
#         once_again=True





# THIS IS THE TEACHERS CODE USING LIST

# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction=input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
# text=input("Type your message : \n").lower()
# shift=int(input("Type the shift number : \n"))

# shift=shift % 26


# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         position+=shift_amount
#         cipher_text+=alphabet[position]
#     print(f"The encoded text is : {cipher_text}")

# def decrypt(cipher_text,shift_amount):
#     decipher_text=""
#     for new_letter in cipher_text:
#         new_position=alphabet.index(new_letter)
#         new_position-=shift_amount
#         decipher_text+=alphabet[new_position]
#     print(f"The decoded text is : {decipher_text}")

# if direction=='encode':
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=='decode': 
#     decrypt(shift_amount=shift,cipher_text=text)


# NOW COMBINE BOTH THE ENCRYPT AND DECRYPT FUNCTION TO MAKE A SINGLE FUNCTION CALLED CEASAR() FUNCTION


def caesar(text,shift,direction):
    new_text=""
    if direction == 'decode':
            shift*=-1
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)

            # if direction == 'encode':
            #     position+=shift
            #     new_text+=alphabet[position]
            # else:
            #     position-=shift
            #     new_text+=alphabet[position]
            
            # DO THIS INSTEAD 

            position+=shift
            new_text+=alphabet[position]
        else:
            new_text+=letter
    print(f"The {direction}d text is : {new_text}")




message=False

while not message:

    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text=input("Type your message : \n").lower()
    shift=int(input("Type the shift number : \n"))

    shift=shift % 26
    caesar(text,shift,direction)
    take=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if take=='no':
        message=True
        print("Goodbye")