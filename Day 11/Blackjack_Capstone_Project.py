import random
from art import logo
print(logo)

def play_game():
    def deal_card():
        """Returns a random card from the deck."""
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card=random.choice(cards)
        return card


    user_cards=[]
    comp_cards=[]


    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())


    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        
        # if 11 in cards and 10 in cards and len(cards)==2:
        # 	return f"BLACKJACK"
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


    def compare(user_score,comp_score):
        if user_score==comp_score:
            print("It's a draw")
        elif comp_score==0:
            print("You lose")
        elif user_score==0:
            print("You win")
        elif user_score>21:
            print("You lose")
        elif comp_score>21:
            print("You win")
        else:
            if max(user_score,comp_score) == user_score:
                print("You win")
            else:
                print("You lose")

    is_game_over=False

    while not is_game_over:

        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score==0 or comp_score==0 or user_score>21:
            is_game_over=True
        else:
            if input("Type 'y' to draw another card or 'n' to pass : ") == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    compare(user_score,comp_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()