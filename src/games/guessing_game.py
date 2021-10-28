import random

print("*"*50)
print("*{:^48}*".format(" Welcome To The Guessing Game! "))
print("*"*50)

secret_number = random.randrange(1, 101)
total_shots = 0
rounds = 1
points = 1000
lost_points = 0
print(secret_number)
print("(1) Easy (2) Moderate (3) Hard")
level = int(input("Define your level: "))

if (level == 1):
    total_shots = 7
elif (level == 2):
    total_shots = 5
else:
    total_shots = 3

for rounds in range(1, total_shots + 1):
    print("Tentativa {} de {}".format(rounds, total_shots))
    kick_str = input("Type a number between 1 and 100: ")
    print("you type: ", kick_str)
    kick = int(kick_str)

    if (kick < 1 or kick > 100):
        print("You must type a number between 1 and 100!")
        continue

    goal    = kick == secret_number
    bigger  = kick < secret_number
    smaller = kick > secret_number

    if (goal):
        print("You Win!!! :)\nYou Scored {} Points.".format(points))
        break
    else:
        lost_points = abs(secret_number - kick)
        points -= lost_points
        if (bigger):
            print("You Lose, the secret number is Bigger. ;)")
            if (rounds == total_shots):
                print("The secret number was {}.\nYou Scored {} Points.".format(secret_number, points))
        elif (smaller):
            print("You Lose, the secret number is Smaller. ;)")
            if (rounds == total_shots):
                print("The secret number was {}.\nYou Scored {} Points.".format(
                    secret_number, points))

print('{:=^50}'.format("> Game over <"))
