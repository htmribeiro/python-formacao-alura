import gallows_game
import guessing_game

print("{}".format('*'*50))
print("{:*^50}".format(" >>>  Choose Your Game!  <<< "))
print("{}".format('*'*50))

print("(1) Gallows (2) Gessing")

choice = int(input("Type you choice: "))

if (choice == 1):
  print("Start Gallows Game!")
  gallows_game.play()

elif (choice == 2):
  print("Start Gessing Game!")
  guessing_game.play()
