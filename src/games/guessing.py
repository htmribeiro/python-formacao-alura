print("*"*30)
print("Welcome to the Guessing Game!")
print("*"*30)

secret_number = 42

kick_str = input("Type your number: ")
print("You type: ", kick_str)
kick = int(kick_str)

if (secret_number == kick):
	print("You Win!!! :)")
else:
	print("you Lose, who knows the next time. ;)")

print('{:=^50}'.format("> Game over <"))