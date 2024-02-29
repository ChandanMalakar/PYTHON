from art import logo,vs
from game_data import list_of_dict

import random

print(logo)

# list_of_dict=[
#     {'name':'chandan','dept':'cse','reg':526,'pop':1000},
#     {'name':'harika','dept':'cse','reg':535,'pop':656},
#     {'name':'arsh','dept':'cse','reg':516,'pop':856},
#     {'name':'madhav','dept':'cse','reg':556,'pop':756}
#     ]
score=0
length_dict=len(list_of_dict)
ran1=random.randint(0,length_dict-1)

def random_list(ran1,length_dict,score):
    # print(length_dict)
    ran2=random.randint(0,length_dict-1)
    if(ran1==ran2):
        random_list(ran1,length_dict,score)
    if ran1>length_dict or ran2>length_dict:
        random_list(ran1,length_dict,score)
    # print(random_number)
    main(ran1,ran2,score)

 
  
def main(ran1,ran2,score):
    print(f"compare A : {list_of_dict[ran1]['name']} a {list_of_dict[ran1]['description']} from {list_of_dict[ran1]['country']}")
    print(vs)
    print(f"with B : {list_of_dict[ran2]['name']} a {list_of_dict[ran2]['description']} from {list_of_dict[ran2]['country']}")
    choice=input("Type A or B : ")
    if choice=='A' and list_of_dict[ran1]['follower_count']>list_of_dict[ran2]['follower_count']:
        score+=1
        print(f"Correct choice , you're score is {score}")
        random_list(ran1,length_dict,score)
    elif choice=='B' and list_of_dict[ran2]['follower_count']>list_of_dict[ran1]['follower_count']:
        score+=1
        print(f"Correct choice , you're score is {score}")
        ran1=ran2
        random_list(ran1,length_dict,score)
    else:
        print(f"Wrong answer , you're score is {score}")
    
random_list(ran1,length_dict,score)




