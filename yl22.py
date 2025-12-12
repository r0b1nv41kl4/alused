import random

playAgain = None

while playAgain != 'n':
    userChoice = input('Rock, paper, scissors! ')

    list = ['rock', 'paper', 'scissors']
    botChoice = random.choice(list)

    if userChoice == botChoice:
        print("It's a tie!")
    elif (userChoice == 'rock' and botChoice == 'scissors') or \
         (userChoice == 'paper' and botChoice == 'rock') or \
         (userChoice == 'scissors' and botChoice == 'paper'):
        print('You win,', userChoice, 'beats', botChoice)
    else:
        print('You lose,', botChoice, 'beats', userChoice)

    playAgain = input('Do you want to play again? (y/n) ')