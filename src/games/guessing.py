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
    if (kick < secret_number):
        print("you Lose, the secret number is bigger. ;)")
    elif (kick > secret_number):
        print("you Lose, the secret number is smaller. ;)")

print('{:=^50}'.format("> Game over <"))
