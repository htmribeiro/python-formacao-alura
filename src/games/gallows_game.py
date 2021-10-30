def play():
  print("{}".format("*"*50))
  print('{:*^50}'.format(' >>>  Welcome To The Gallows Game!  <<< '))
  print("{}".format("*"*50))

  secret_word = "banana"
  right = False
  gallows = False

  while(not right and not gallows):
    print("Playing...")

  print("{:*^50}".format('<<<  Game Over  >>>'))

if (__name__ == "__main__"):
  play()
