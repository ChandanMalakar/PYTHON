import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']



new_list=letters+numbers+symbols

# print(new_list)

print("Welcome to the PyPassword Generator")
nr_letters=int(input("How many letters would you like in your password? \n"))
nr_symbols=int(input("How many symbols would you like? \n"))
nr_numbers=int(input("How many numbers would you like? \n"))

#EASY LEVEL (LETTERS, SYMBOLS, NUMBERS, IN SEQUENCE)
# fhghgd!$^^5646

# HARD LEVEL (ALL IN RANDOM NO SEQUENCE)
# fsmhgfsyr3278462@%^#&*#^$kr342

#EASY METHOD

password=""
# random_letters="" THIS ONE IS USED
for i in range(0,nr_letters):
    # rn_letter=random.randint(0,len(letters)-1) DON'T WRITE THESE 2 LINES
    # random_letters+=letters[rn_letter] NOT THIS ONE TOO
    
    # rn_letter=random.choice(letters) DON'T WRITE THESE 2 LINES EITHER
    # random_letters+=rn_letter
    password+=random.choice(letters)

# print(random_letters)


# random_numbers="" THIS ONE IS USED
for i in range(0,nr_numbers):
    # rn_number=random.randint(0,len(numbers)-1)
    # random_numbers+=numbers[rn_number]
    # rn_number=random.choice(numbers)
    # random_numbers+=rn_number
    password+=random.choice(numbers)
# print(random_numbers)

# random_symbols="" THIS ONE IS USED
for i in range(0,nr_symbols):
    # rn_symbols=random.randint(0,len(symbols)-1)
    # random_symbols+=symbols[rn_symbols]
    # rn_symbols=random.choice(symbols)
    # random_symbols+=rn_symbols
    password+=random.choice(symbols)
# print(random_symbols)
print("BY EASY METHOD : ")
print(f"The most suitable password would be : {password}")
# print(f"Your suitable password will be : {random_letters+random_symbols+random_numbers}")

# nf_letters=random.sample(letters,nr_letters)
# print(nf_letters)
# nf_symbols=random.sample(symbols,nr_symbols)
# print(nf_symbols)
# nf_numbers=random.sample(numbers,nr_numbers)
# print(nf_numbers)





# HARD METHOD

# length2=len(new_list)
total_elements=nr_letters+nr_numbers+nr_symbols
new_string=""
for i in range(0,total_elements):
    # new_letter=random.randint(0,length2-1)
    # new_string+=new_list[new_letter]
    new_string+=random.choice(new_list)
print("BY HARD METHOD : BY ME")
print(f"The most suitable password would be : {new_string}")



# HARD METHOD BY TUTORIAL

password_list=[]
# random_letters="" THIS ONE IS USED
for i in range(0,nr_letters):
    password_list+=random.choice(letters)

for i in range(0,nr_symbols):
    password_list+=random.choice(symbols)

for i in range(0,nr_numbers):
    password_list+=random.choice(numbers)
print('HARD METHOD BY TEACHER : ')
# print(password_list)
random.shuffle(password_list) # The shuffle() function is used to shuffle the list
# print(password_list)
password=""
for i in password_list:
    password+=i
print(f"The most suitable pas sword would be : {password}")