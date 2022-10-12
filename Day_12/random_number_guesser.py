import random
from art import *

def number_to_guess():
	"""Computer stores a number for the user to guess"""
	return int(random.random()*100)

def difficulty_choice():
	"""Player chooses a difficulty: hard or easy"""
	valid_choice = False
	while not valid_choice:
		difficulty = input("Choose a difficulty: hard or easy\n")
		if difficulty == "hard" or difficulty == "easy":
			valid_choice = True
			return difficulty
		else:
			print("Please choose a valid difficulty: hard or easy\n")

#user enters a guess
def user_guess():
	"""Player chooses a number to guess"""
	valid_guess = False
	while not valid_guess:
		the_guess = input("Choose a number between 0 and 100\n")
		if type(the_guess) is int and 0 < the_guess < 100:
			return the_guess
		else:
			print("Please enter a valid number")

#hot or cold for how close they are to the number
def hot_or_cold(the_guess, computer_number):
	"""Hot or cold depending on how close the user is to the number"""
	if -5 < (the_guess - computer_number) < 5:
		print("Very Hot!")
	elif -10 < (the_guess - computer_number) < 10:
		print("Hot!")
	elif -20 < (the_guess - computer_number) < 20:
		print("Warm!")
	elif -30 < (the_guess - computer_number) < 30:
		print("Lukewarm!")
	elif -40 < (the_guess - computer_number) < 40:
		print("Cold!")
	else:
		(print("Freezing!"))

## Guesses left artwork stored in a list and extracted with user guesses
def art_guesses_left(user_guesses):
	"""Art from art.py for guesses left"""
	artwork = [number_0, number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9, number_10]
	print(artwork[user_guesses])

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
		while are_you_playing != "y" and are_you_playing != "n":
			are_you_playing = input("Would you like to play again? y/n ")
			if are_you_playing == "y":
				os.system("clear")
			elif are_you_playing == "n":
				print("Thank you for playing!")
				keep_playing = False
			else:
				print("Please enter a valid response.")



guess_the_number()
