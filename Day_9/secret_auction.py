from replit import clear
from art import logo

def secret_auction():
	print(logo)
	continue_bidding = True
	bids = {}
	winning_bid = 0
	winner = ""
	while continue_bidding:
		name = input("What is your name? ")
		bid = int(input("What is your bid? "))
		bids[name] = bid
		more_bids = input("Are there any more bids? Y/N ")
		if more_bids.upper() == "Y":
			clear()
		else:
			continue_bidding = False
			clear()
	for person in bids:
		if bids[person] > winning_bid:
			winning_bid = bids[person]
			winner = person
	print(f"{winner.capitalize()} is the winner of the auction with a bid of {winning_bid}.")

secret_auction()
