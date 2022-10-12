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
		if player_total == 21 and len(player_cards) == 2:
			print(f"You drew cards {player_cards} totalling {player_total}. BlackJack!")
			return player_total, player_cards
		elif player_total == 21:
			print(f"You have {player_total}, stop drawing cards!")
			return player_total, player_cards
		else:
			another_card = input("Would you like to chose another card? y/n ")
			if another_card == "y":
				player_cards.append(pick_card())
				player_total = sum(player_cards)
	# adjust aces from 11 to 1 if total > 21
				if 11 in player_cards and player_total > 21:
					ace_index = player_cards.index(11)
					player_cards[ace_index] = 1
					player_total = sum(player_cards)
					print(f"You drew cards {player_cards} totalling {player_total}.")
	# bust if >21 and no aces, return total
				elif player_total > 21:
					print(f"You drew cards {player_cards} totalling {player_total}. You are bust!")
					return player_total, player_cards
				else:
					print(f"You drew cards {player_cards} totalling {player_total}.")
	# return final player total when not bust
			elif another_card == "n":
				return player_total, player_cards
			else:
				print("Please choose y/n")
			
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


def guess_the_number():
	"""Player guesses the number"""
	keep_playing = True
	while keep_playing:
		print(logo)
		computer_number = number_to_guess()
		difficulty = difficulty_choice()
		user_guesses = 0	
	## set number of guesses
		if difficulty == "hard":
			user_guesses = 5
			print(hard_choice)
			art_guesses_left(user_guesses)
		else:
			user_guesses = 10
			print(easy_choice)
			art_guesses_left(user_guesses)
	
		the_guess = user_guess()		
	## assess how close user is to number
		while user_guesses > 1:
			if the_guess < computer_number:
				user_guesses -= 1			
				print("Too low! Guess again.")
				hot_or_cold(the_guess, computer_number)
				art_guesses_left(user_guesses)
				the_guess = user_guess()
			elif the_guess > computer_number:
				user_guesses -= 1
				print("Too high! Guess again.")
				hot_or_cold(the_guess, computer_number)
				art_guesses_left(user_guesses)
				the_guess = user_guess()
			else:
				user_guesses = 0
				print(winner)
				print(f"You guessed the number {the_guess} correctly! You win!")
		if computer_number != the_guess:
			print(loser)
			print(f"You ran out of guesses! The computer number was {computer_number}")
		else:
			print(winner)
			print(f"You guessed the number {the_guess} correctly! You win!")
		are_you_playing = ""
	## ask if the player wants to play again
		while are_you_playing != "y" and are_you_playing != "n":
			are_you_playing = input("Would you like to play again? y/n ")
			if are_you_playing == "y":
				os.system("clear")
			elif are_you_playing == "n":
				print("Thank you for playing!")
				keep_playing = False
			else:
				print("Please enter a valid response.")

who_wins()
