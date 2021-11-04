from random import randrange

def play():
	print("{}".format("*"*50))
	print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
	print("{}".format("*"*50))

	file = open("others\words.txt", "r")
	words = []

	for line in file:
  		line = line.strip()
  		words.append(line)

	file.close()

	number = randrange(0, len(words))
	secret_word = words[number].upper()
	letter_right = ['_' for letter in secret_word]

	right = False
	gallows = False
	missed = len(secret_word)

	print(letter_right)
	
	while(not right and not gallows):
		kick = input("Type a letter: ")
		kick = kick.strip().upper()

		if(kick in secret_word):
			index = 0
			for letter in secret_word:
				if(kick == letter):
					letter_right[index] = letter
				index += 1

			letter_left = letter_right.count('_')  # Hamilton
			print(letter_right)
			print('Still left to hit {} letters.\n'.format(letter_left))  # Hamilton

			if(letter_left != 0):  # Hamilton
				print("Playing...\n")
		else:
			missed -= 1 # Hamilton
			print(letter_right)
			print("{} attempts remain.\n".format(missed))  # Hamilton

		gallows = missed == 0
		right = '_' not in letter_right

		# print(letter_right) # Mudar de posição para dentro do for letra in secret_word

	if(right):
		print("YOU WIN :) CONGRATULATION!")
	else:
		print("YOU LOSE :( SORRY!")

	print()
	print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
	play()
