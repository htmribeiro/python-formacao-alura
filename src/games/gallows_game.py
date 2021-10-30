def play():
  print("{}".format("*"*50))
  print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
  print("{}".format("*"*50))

  secret_word = "banana"
  right = False
  gallows = False

  while(not right and not gallows):
    kick = input("Type a letter: ")

    index = 0
    for letter in secret_word:
      if(kick == letter):
        print("The letter '{}' is in position {}".format(letter, index))
      index += 1

    print("Playing...")

  print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
  play()
