print("*"*30)
print("Welcome to the Guessing Game!")
print("*"*30)

secret_number = 42
total_shots = 3
rounds = 1

while(rounds <= total_shots):
    print("Tentativa {} de {}".format(rounds, total_shots))
    kick_str = input("Type your number: ")
    print("You type: ", kick_str)
    kick = int(kick_str)

    goal    = kick == secret_number
    bigger  = kick < secret_number
    smaller = kick > secret_number

    if (goal):
        print("You Win!!! :)")
    else:
        if (bigger):
            print("you Lose, the secret number is bigger. ;)")
        elif (smaller):
            print("you Lose, the secret number is smaller. ;)")
    
    rounds = rounds + 1

print('{:=^50}'.format("> Game over <"))
