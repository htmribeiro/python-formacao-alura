def main():
  print('*'*50)
  print('*{:^48}*'.format(' Age Group '))
  print('*'*50)

  age_str = input('Type your age: ')
  age = int(age_str)

  legal_age = age >= 18
  child     = age < 12
  teenager  = age >= 12

  if (legal_age):
    print('You are of legal age.')
  else:
    if (child):
      print('You are a child.')
    elif (teenager):
      print('You are a teenager')
main()
