import random
from game_data import data
from art import logo, vs
import os

	

## choose random selection from data
def choose():
	random_choice = random.randint(0, len(data)-1)
	return data[random_choice]

## play the game
def player_choice():
	print(logo)
	correct = True
	guesses = 0
	while correct:		
		
## initial comparison generated
		if guesses == 0:
			stats_A = choose()
			stats_B = choose()
			check_same(stats_A, stats_B)
		else:

## checks if A or B should be kept, moves to A, random generation for B
			if player_guess == "B":
				stats_A = stats_B
				stats_B = choose()
				check_same(stats_A, stats_B)
			else:
				stats_B = choose()
				check_same(stats_A, stats_B)

## comparison print and ask for guess
		print(f"Compare A: {stats_A['name']}, a {stats_A['description']} from {stats_A['country']}.")
		print(vs)
		print(f"With B: {stats_B['name']}, a {stats_B['description']} from {stats_B['country']}.\n")
		player_guess = guess()
		guesses += 1
		if player_guess == "A":
			print(f"\nYour guess is that {stats_A['name']} has more followers.\n")
		else:
			print(f"\nYour guess is that {stats_B['name']} has more followers.\n")

## check if correct
		if player_guess == "A" and stats_A['follower_count'] > stats_B['follower_count']:
			print(f"Correct! {stats_A['name']} has more followers.")
			print(f"Your score is {guesses}.\n")
		elif player_guess == "B" and stats_A['follower_count'] < stats_B['follower_count']:
			print(f"Correct! {stats_B['name']} has more followers.")
			print(f"Your score is {guesses}.\n")
		else:
			final_score = guesses -1
			print(f"Incorrect guess! Your final score is {final_score}")
			play_option = play_again()
			if play_option == "N":
				print("Thanks for playing!")
				correct = False
				return
			elif play_option == "Y":
				os.system('clear')
				player_choice()
			else:
				return
				
			
		
## player guess		
def guess():
	valid_guess = False
	while not valid_guess:
		the_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
		if the_guess == "A" or the_guess == "B":
			return the_guess			
		else:
			print("Please enter a valid guess: 'A' or 'B': ")

## play again
def play_again():
	valid_answer = False
	while not valid_answer:
		play_again = input("Would you like to play again? Y or N: ").upper()
		if play_again == "Y" or play_again == "N":
			return play_again
		else:
			print("Please enter a valid answer: 'Y' or 'N': ")

## check whether stats_A and stats_B are the same 
def check_same(stats_A, stats_B):
	while stats_A['name'] == stats_B['name']:
		print("same array")
		stats_B = choose()
			


			
#choose()
player_choice()
#check_same({'name': 'cat'},{'name':'cat'})
#play_again()
