import logo

print(logo.art)

print("Welcome to the secret auction program.")

# name , bid_price, 



bids={}			
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=''
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while not bidding_finished:
	new_dict={}
	name=input("What is your name ? ")
	bid_price=int(input("What is your bid price $"))
	new_dict[name]=bid_price
	bids.update(new_dict)
	case=input("Are there any other bidders? 'yes' or 'no'.")
	if case=='no':
		bidding_finished=True
find_highest_bidder(bids)