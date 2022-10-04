alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# combine encode and decode functions in one
def caesar(user_choice, user_text, shift_amount):
	output_text = ""
	for letter in user_text:
		position = alphabet.index(letter)
# options to encode a message
		if user_choice == "encode":
			new_position = position + shift_amount
			if new_position > 25:
				new_position -= 26
			output_text += alphabet[new_position]
# options to decode a message
		elif user_choice == "decode":
			new_position = position - shift_amount
			output_text += alphabet[new_position]
	
  print(f"The {user_choice}d message is {output_text}")

caesar(user_choice=direction, user_text=text, shift_amount=shift)

#alternative solution
def caesar2(user_choice, user_text, shift_amount):
	output_text = ""
# for decode do eg 5* -1 = -5, position + -shift_amount == position - shift_amount
    if user_choice == "decode":
        shift_amount *= -1
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
			new_position -= 26
		output_text += alphabet[new_position]
    
     print(f"The {user_choice}d message is {output_text}")

caesar2(user_choice=direction, user_text=text, shift_amount=shift)
