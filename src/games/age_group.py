def main():
  print('*'*50)
  print('*{:^48}*'.format(' Age Group '))
  print('*'*50)

  age_str = input('Type your age: ')
  age = int(age_str)

  if (age >= 18):
    print('You are of legal age.')
  else:
    if (age < 12):
      print('You are a child.')
    elif (age >= 12):
      print('You are a teenager')
main()