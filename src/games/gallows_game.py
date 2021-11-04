from random import randrange

def play():
	welcome_msg()
	
	secret_word = load_secret_word()
	
	correct_letters = init_correct_letters(secret_word)

	right = False
	gallows = False
	missed = len(secret_word)

	print(correct_letters)
	
	while(not right and not gallows):
		kick = input("Type a letter: ")
		kick = kick.strip().upper()

		if(kick in secret_word):
			index = 0
			for letter in secret_word:
				if(kick == letter):
					correct_letters[index] = letter
				index += 1

			letter_left = correct_letters.count('_')  # Hamilton
			print(correct_letters)
			print('Still left to hit {} letters.\n'.format(letter_left))  # Hamilton

			if(letter_left != 0):  # Hamilton
				print("Playing...\n")
		else:
			missed -= 1 # Hamilton
			print(correct_letters)
			print("{} attempts remain.\n".format(missed))  # Hamilton

		if(missed < len(secret_word)):
			# -aqui-Criar uma lista das letras missed e apresentar a cada rodada
			print("missed")
		
		gallows = missed == 0
		right = '_' not in correct_letters

		# print(correct_letters) # Mudar de posição para dentro do for letra in secret_word

	if(right):
		print("YOU WIN :) CONGRATULATION!")
	else:
		print("YOU LOSE :( SORRY!")
		print(secret_word)

	print()
	print("{:*^50}".format('<<<  Game Over  >>>'))

""" Function that prints the game presentation message """
def welcome_msg():
	print("{}".format("*"*50))
	print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
	print("{}".format("*"*50))

""" Function that reads the file and initializes the secret word """
def load_secret_word():
		words = []

		with open("others\words.txt", "r") as file:
			for line in file:
					line = line.strip()
					words.append(line)

		number = randrange(0, len(words))
		secret_word = words[number].upper()

		return secret_word

""" Function that initializes the list of correct letters """
def init_correct_letters(word):
	return ['_' for letter in word]

if (__name__ == "__main__"):
	play()
