# HERE WE ARE GOING TO MAKE A TOOL TO ENCRYPT OR DECRYPT 
# A MESSAGE.

# STEP 1 - 
# WE WILL CREATE A LIST CONTAINING THE 2 CHOICES
# ENCODE AND DECODE
# TAKE ONE STRING INPUT FROM THE USER AND COMPARE 
# WITH THE LIST ITEM
# AND THEN DO THE NECESSARY PROCESSING 


print(''' ██████╗ █████╗ ███████╗███████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
██║     ██║██████╔╝███████║█████╗  ██████╔╝     
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ''')

list=['encode', 'decode']
user_choice=input("Type 'encode' to encrypt, type 'decode' to decrypt :\n")
new_message=""
once_again=False
while not once_again:
    if user_choice in list:
        message=input("Type your message :\n")
        shift_number=int(input("Type the shift number :\n"))
        if user_choice=='encode':
            for i in message:
                dup=ord(i)
                dup+=shift_number
                dup=chr(dup)
                new_message+=dup
            print(f"Your encoded message is : {new_message}")
        else:
            for i in message:
                dup=ord(i)
                dup-=shift_number
                dup=chr(dup)
                new_message+=dup
            print(f"Your decoded message is : {new_message}")
    else:
        print("Invalid choice")
    take=input("Type 'Yes' if you want to go again OR Type 'No' if you don't :\n")
    if(take=='Yes'):
        once_again=False
    else:
        once_again=True
