import random

print("*"*30)
print("Welcome to the Guessing Game!")
print("*"*30)

secret_number = random.randrange(1, 101)
total_shots = 3
rounds = 1

for rounds in range(1, total_shots + 1):
    print("Tentativa {} de {}".format(rounds, total_shots))
    kick_str = input("Type a number between 1 and 100: ")
    print("You type: ", kick_str)
    kick = int(kick_str)

    if (kick < 1 or kick > 100):
        print("You must type a number between 1 and 100!")
        continue

    goal    = kick == secret_number
    bigger  = kick < secret_number
    smaller = kick > secret_number

    if (goal):
        print("You Win!!! :)")
        break
    else:
        if (bigger):
            print("you Lose, the secret number is bigger. ;)")
        elif (smaller):
            print("you Lose, the secret number is smaller. ;)")
    
print('{:=^50}'.format("> Game over <"))
