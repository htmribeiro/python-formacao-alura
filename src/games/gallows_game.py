def play():
  print("{}".format("*"*50))
  print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
  print("{}".format("*"*50))

  secret_word = "banana"
  letter_right = ['-', '-', '-', '-', '-', '-']
  print(letter_right)

  right = False
  gallows = False

  while(not right and not gallows):
    kick = input("Type a letter: ")
    kick = kick.strip()

    index = 0
    for letter in secret_word:
      if(kick.upper() == letter.upper()):
        letter_right[index] = letter
      index += 1

    print(letter_right)
    print("Playing...")

  print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
  play()
