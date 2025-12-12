import random

num = random.randrange(0, 100)

guess = None

while guess != num:
    guess = float(input('Mis numbri arvuti välja mõtles? '))

    if guess > num:
        guess = print('Väiksem! ')
    elif guess < num: print('Suurem! ')
    else: print('Hästi tehtud!')