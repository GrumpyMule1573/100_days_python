alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
	to_encrypt = text
	to_encrypt_index = []
	shift = int(shift)
	encrypted = []

# grab alphabet indices of the word
	for letter in to_encrypt:
		for letter2 in alphabet:
			if letter == letter2:
				to_encrypt_index.append(alphabet.index(letter2))

# create the shifted index - if > 25, -26 to get back to index[0]
	for new_index in to_encrypt_index:
		plus_shift = int(new_index) + shift
		if plus_shift > 25:
			plus_shift -= 26
		encrypted.append(alphabet[plus_shift])
	
	print(encrypted)
    
encrypt("hello",5)
