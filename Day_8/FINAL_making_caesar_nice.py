from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift_amount, user_choice):

	output_text = ""
# accounts for shifts >26 by using the remainder as the shift amount
	shift_amount = shift_amount % 26

# changes shift to a negative for decoding
	if user_choice == "decode":
		shift_amount *= -1
		
	for letter in user_text:
# to account for special characters or spaces
		if letter not in alphabet:
			output_text += letter
# if it is a letter
		else:
			position = alphabet.index(letter)
			new_position = position + shift_amount
			output_text += alphabet[new_position]
	
	print(f"The {user_choice}d message is {output_text}")


print(logo)
keep_playing = True
while keep_playing == True:
# user inputs to call caesar()
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
# call caesar()
	caesar(user_text=text, shift_amount=shift, user_choice=direction)
# after caesar output, ask if want to carry on
	carry_on = input("Do you want to keep playing? y/n ")
	if carry_on == "n":
		keep_playing = False
