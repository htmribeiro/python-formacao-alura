from random import randrange

def play():
	welcome_msg()
	
	secret_word = load_secret_word()
	
	correct_letters = init_correct_letters(secret_word)
	print(correct_letters)

	right = False
	gallows = False
	missed = 0
	
	while(not right and not gallows):
		kick = player_kick()

		if(kick in secret_word):
			hit_kick(secret_word, kick, correct_letters)
		else:
			missed += 1
		
		gallows = missed == 7
		right = '_' not in correct_letters
		print(correct_letters)

		if(missed > 0):
			draw_gallows(missed)
			# -aqui- Criar uma lista das letras missed e apresentar a cada rodada
			# print("wrong letters\n")
		
	if(right):
		game_winner()
	else:
		game_loser(secret_word)

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

""" Function that asks for the player's kick """
def player_kick():
	kick = input("Type a letter: ")
	kick = kick.strip().upper()

	return kick

""" Function that puts the player's kick in the correct position on the list """
def hit_kick(secret_word, kick, correct_letters):
	index = 0
	for letter in secret_word:
		if(kick == letter):
			correct_letters[index] = letter
		index += 1
	
	letter_left = correct_letters.count('_')  # Hamilton
	print(correct_letters)
	print('Still left to hit {} letters.\n'.format(letter_left))  # Hamilton

	if(letter_left != 0):
		print("Playing...\n") # Hamilton

""" Function that prints the game's winner and loser messages """
def game_winner():
	print("PARABÉNS, VOCÊ GANHOU!!!")
	print("       ___________      ")
	print("      '._==_==_=_.'     ")
	print("      .-\\:      /-.    ")
	print("     | (|:.     |) |    ")
	print("      '-|:.     |-'     ")
	print("        \\::.    /      ")
	print("         '::. .'        ")
	print("           ) (          ")
	print("         _.' '._        ")
	print("        '-------'       ")

def game_loser(secret_word):
	print("Ahhh...VOCÊ FOI ENFORCADO!!!")
	print(f"A palavra era {secret_word}")
	print("    _______________         ")
	print("   /               \        ")
	print("  /                 \       ")
	print("//   ~~~~     ~~~~   \/\    ")
	print("\|   xxxx     xxxx   | /    ")
	print(" |    xx       xx    |/     ")
	print(" |   xxxx     xxxx   |      ")
	print(" |                   |      ")
	print(" \__      xxx      __/      ")
	print("   |\      x      /|        ")
	print("   | |    xxx    | |        ")
	print("   |               |        ")
	print("   | I I I I I I I |        ")
	print("   \_   I I I I   _/        ")
	print("     \_         _/          ")
	print("       \_______/            ")


def draw_gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
	play()
