import random

#STEP 1

# word_list=["neko", "rabbits", "calfs"]

# TAKE A RANDOM WORD FROM THE WORDLIST.
# ASSIGN IT TO A VARIABLE 'CHOSEN_WORD'. 

# ASK THE USER TO GUESS A LETTER , AND ASSIGN THEIR 
# ANSWER TO A VARIABLE 'GUESS' AND MAKE IT LOWERCASE.

# CHECK IF THE GUESSED LETTER IS THERE IN THE CHOSEN WORD.

# import hangman_words # OR USE THIS 
from hangman_words import word_list

chosen_word=random.choice(word_list)
# print(chosen_word)


# guess=input("Guess a letter : \n")
# guess.lower();

# for i in range(0,len(chosen_word)):
#     if chosen_word[i]==guess:
#         print("Right")
#     else:
#         print("Wrong")

# NOW
        
# Create an empty list called display.
# for each letter in the chosen word add a space "_"      
# to 'display'.

display=[];
for i in range(0,len(chosen_word)):
    display+="_"
# print(display)


# STEP 2
# loop through each position in the chosen word.
# If the letter at that position matches 'guess' then 
# reveal that letter in the display at that position

# chances=5
# while(chances>=0):
# for i in range(0,len(chosen_word)):
#     if(chosen_word[i]==guess):
#         display[i]=guess

# use a while loop to let the user guess again.            
# this loop shall stop when all the letters have been guessed
        
# now writing all the above code together

# import hangman_ascii_art # OR USE THIS
from hangman_ascii_art import logo, stages

print(logo)

end_of_game=False



chances=len(stages)
life=0
print()
while not end_of_game and chances!=0:    
    
    guess=input("Guess a letter : \n")
    guess.lower();

    if guess in display:
        print("you've already guessed it in the guessed letter")

    for i in range(0,len(chosen_word)):
        if(chosen_word[i]==guess):
            display[i]=guess
    print(display)
    if guess not in display:
        chances-=1
        print("Wrong guess")
        print(f"You have {chances} left")
        print(stages[life])
        life+=1
        
    elif "_" not in display:
        end_of_game=True
        print("You Win...!")
if chances==0:
    print("You Lose...LOSER")
    print(f"Psst....the word was {chosen_word}")
