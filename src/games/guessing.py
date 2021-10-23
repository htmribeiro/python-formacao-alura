print("*"*30)
print("Welcome to the Guessing Game!")
print("*"*30)

secret_number = 42

kick_str = input("Type your number: ")
print("You type: ", kick_str)
kick = int(kick_str)

goal = kick == secret_number
bigger = kick < secret_number
smaller = kick > secret_number

if (goal):
	print("You Win!!! :)")
else:
    if (bigger):
        print("you Lose, the secret number is bigger. ;)")
    elif (smaller):
        print("you Lose, the secret number is smaller. ;)")

print('{:=^50}'.format("> Game over <"))
