import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard' : ")


guess=random.randint(1,100)


if level=='easy':
    no_of_attempts=10
    print(f"You have {no_of_attempts} attempts remaining to guess the number ")
else:
    no_of_attempts=5
    print(f"You have {no_of_attempts} attempts remaining to guess the number ")

run_until=False

while not run_until:
    my_guess=int(input("Make a guess: "))

    if my_guess>guess:
        print("Too high.")
        print("Guess again.")
        no_of_attempts-=1
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    elif my_guess<guess:
        print("Too Low.")
        print("Guess again.")
        no_of_attempts-=1
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    elif my_guess==guess:
        print("Correct Guess! You win!")
        run_until=True
    
    if no_of_attempts==0:
        print("You've run out of guesses, you lose.")
        run_until=True
    
print("The number was ",guess)