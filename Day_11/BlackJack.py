import random
from art import logo

# card list
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card():
	return card_list[int(random.random()*len(card_list))]


def player_pick():
	player_continue = True
	player_cards = []
	player_cards.append(pick_card())
	player_cards.append(pick_card())
	player_total = sum(player_cards)
	if player_cards[0] == 11 and player_cards[1] == 11:
		player_cards[0] = 1
		player_total = sum(player_cards)
	print(f"Your cards are {player_cards[0]} and {player_cards[1]} totalling {player_total}.")
	while player_continue:
		if player_total == 21:
			print(f"You drew cards {player_cards} totalling {player_total}. BlackJack!")
			return player_total, player_cards
		elif input("Would you like to chose another card? y/n ") == "y":
			player_cards.append(pick_card())
			player_total = sum(player_cards)
# adjust aces from 11 to 1 if total > 21
			if 11 in player_cards and player_total > 21:
				ace_index = player_cards.index(11)
				player_cards[ace_index] = 1
				player_total = sum(player_cards)
				if player_cards[-1] == 11 and player_total > 21:
					player_cards[-1] = 1
					player_total = sum(player_cards)
					print(f"You drew cards {player_cards} totalling {player_total}.")
				else:
					print(f"You drew cards {player_cards} totalling {player_total}.")
# bust if >21 and no aces, return total
			elif player_total > 21:
				print(f"You drew cards {player_cards} totalling {player_total}. You are bust!")
				return player_total, player_cards
			else:
				print(f"You drew cards {player_cards} totalling {player_total}.")
# return final player total when not bust
		else:
			return player_total, player_cards
			
# print statements only needed for testing
def dealer_pick():
	dealer_continue = True
	dealer_cards = []
	dealer_cards.append(pick_card())
	dealer_cards.append(pick_card())
	dealer_total = sum(dealer_cards)
	if dealer_cards[0] == 11 and dealer_cards[1] == 11:
		dealer_cards[0] = 1
		dealer_total = sum(dealer_cards)
	while dealer_continue:
		if dealer_total == 21:
#			print(f"Dealer drew cards {dealer_cards} totalling {dealer_total}. They have BlackJack! 1")
			return dealer_total, dealer_cards
## dealer continues to draw if <17
		elif dealer_total < 17:
			dealer_cards.append(pick_card())
			dealer_total = sum(dealer_cards)
## adjust aces from 11 to 1 if total > 21
		elif 11 in dealer_cards and dealer_total > 21:
			ace_index = dealer_cards.index(11)
			dealer_cards[ace_index] = 1
			dealer_total = sum(dealer_cards)
			if dealer_cards[-1] == 11 and dealer_total > 21:
				dealer_cards[-1] = 1
				dealer_total = sum(dealer_cards)
#				print(f"Dealer drew cards {dealer_cards} totalling {dealer_total}. 2")
#			else:
#				print(f"Dealer drew cards {dealer_cards} totalling {dealer_total}. 3")
## bust if >21 and no aces, return total
		elif dealer_total > 21:
#			print(f"Dealer drew cards {dealer_cards} totalling {dealer_total}. They are bust! 4")
			return dealer_total, dealer_cards

## return final dealer total when not bust
		else:
			return dealer_total, dealer_cards


def who_wins():
	print(logo)
	keep_playing = True
	while keep_playing:
		dealer_details = dealer_pick()
		print(f"Dealer's first card is {dealer_details[1][0]}.")
		player_details = player_pick()
		if player_details[0] > 21:
			if dealer_details[0] > 21:
				print(f"You are bust with {player_details[0]} and dealer is bust with {dealer_details[0]}, it's a draw.")
			else:
				print(f"You are bust with a score of {player_details[0]} and dealer score is {dealer_details[0]}, dealer wins.")
		elif dealer_details[0] > 21:
			print(f"Your score is {player_details[0]} and dealer is bust with {dealer_details[0]}, you win!")
		elif player_details[0] > dealer_details[0]:
			print(f"Your score is {player_details[0]} and dealer score is {dealer_details[0]}, you win!")
		elif player_details[0] == dealer_details[0]:
			print(f"Your score is {player_details[0]} and dealer score is {dealer_details[0]}, it's a draw.")
		else:
			print(f"Your score is {player_details[0]} and dealer score is {dealer_details[0]}, dealer wins.")
		if input("Would you like to play again? y/n ") == "y":
			print("\nNEW GAME!!!\n")
		else:
			print("\nThanks for playing!")
			keep_playing = False

who_wins()
