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
		print(f"With B: {stats_B['name']}, a {stats_B['description']} from {stats_B['country']}.")
		player_guess = guess()
		guesses += 1
		if player_guess == "A":
			print(f"Your guess is that {stats_A['name']} has more followers.")
		else:
			print(f"Your guess is that {stats_B['name']} has more followers.")

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
			play_option = play_again().upper()
			if play_option == "N":
				print("Thanks for playing!")
				correct = False
				print(correct)
				break
			elif play_option == "Y":
				os.system('clear')
				player_choice()
			else:
				print("i am printing when I shouldn't")
				break
				correct = False
