def play():
  print("{}".format("*"*50))
  print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
  print("{}".format("*"*50))

  secret_word = "banana"
  letter_right = ['_', '_', '_', '_', '_', '_']

  right = False
  gallows = False

  print(letter_right)
  
  while(not right and not gallows):
    kick = input("Type a letter: ")
    kick = kick.strip()

    index = 0
    for letter in secret_word:
      if(kick.upper() == letter.upper()):
        letter_right[index] = letter
      index += 1

    print(letter_right)
    letter_left = letter_right.count('_')
    print('Still left to hit {} letters.'.format(letter_left))
    print("Playing...")

  print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
  play()
