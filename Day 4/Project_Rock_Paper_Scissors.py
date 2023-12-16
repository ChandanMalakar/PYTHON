import random

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

list_of_game_elements=['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''', '''
   s _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']

print("YOUR CHOICE : \n")
if choice>=3 or choice<0:
    print("INVALID CHOICE ... YOU LOSE ....")
else:
    print(list_of_game_elements[choice])

    computers_choice=random.randint(0,2)
    print(list_of_game_elements[computers_choice])
    print(f"COMPUTER'S CHOICE : {computers_choice}\n")

    if computers_choice==choice:
        print("TIE")
    elif computers_choice==1 and choice==0 or computers_choice==2 and choice==1 or computers_choice==0 and choice==2 :
        print("YOU LOOSE")
    elif choice==0 and computers_choice==2 or choice==2 and computers_choice==1 or choice==1 and computers_choice==0:
        print("YOU WIN")
    else:
        print("INVALID CHOICE")

    print("GAME OVER...!")