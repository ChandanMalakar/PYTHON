import random

programming_dictionary={"Chandan":"I am a good person"}
print(programming_dictionary["Chandan"])

pydict={"one":"chandan is a good person",
        "two":"raju is too a good person , but a little bit arrogant",
        "three": "mummy and papa ka mahal i will make"
        }

ran=random.randint(0,2)
print(pydict["three"])

programming_dictionary["Loop"]="hello ! looping structures"
print(programming_dictionary)

# Looping through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

programming_dictionary={}
print(programming_dictionary)

