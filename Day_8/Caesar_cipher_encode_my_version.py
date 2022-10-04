alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
	to_encrypt_index = []
	encrypted = ""

# grab alphabet indices of the word
# this matches the given word letter with the letter in alphabet and appends index number
	for letter in plain_text:
		to_encrypt_index.append(alphabet.index(letter))

# create the shifted index - if > 25, -26 to get back to index[0]
# appends the letter found at the new index to encrypted
	for new_index in to_encrypt_index:
		plus_shift = new_index + shift_amount
		if plus_shift > 25:
			plus_shift -= 26
		encrypted += alphabet[plus_shift]
	
	print(f"The encrypted message is {encrypted}")
    
encrypt(plain_text=text, shift_amount=shift)
