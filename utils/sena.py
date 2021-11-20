import random

sena = []

step = 0
while step < 6:
    number = random.randrange(0, 61)
    sena.append(number)
    
    step += 1

print(sena)
