def play():
  print("{}".format("*"*50))
  print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
  print("{}".format("*"*50))

  secret_word = "banana".upper()
  letter_right = ['_', '_', '_', '_', '_', '_']

  right = False
  gallows = False
  missed = 6

  print(letter_right)
  
  while(not right and not gallows):
    kick = input("Type a letter: ")
    kick = kick.strip().upper()

    if(kick in secret_word):
      index = 0
      for letter in secret_word:
        if(kick == letter):
          letter_right[index] = letter
        index += 1

      letter_left = letter_right.count('_')  # Hamilton
      print('Still left to hit {} letters.'.format(letter_left))  # Hamilton

      if(letter_left != 0):  # Hamilton
        print("Playing...")
    else:
      missed -= 1
      # Hamilton - implementar aviso de quantas tentativas faltam
      print("{} attempts remain.".format(missed))

    gallows = missed == 0
    right = '_' not in letter_right
    

    print(letter_right)

  if(right):
    print("YOU WIN :) CONGRATULATION!")
  else:
    print("YOU LOSE :( SORRY!")

  print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
  play()
