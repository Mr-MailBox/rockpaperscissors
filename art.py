import random

items = ['rock', 'paper', 'scissors']
cpu = random.choice(items)
player = input("rock, paper, or scissors")
    
if player == 'rock' and cpu == 'paper':
    print('haha stupid baby')
if player == 'paper' and cpu == 'scissors':
    print('haha stupid baby')
if player == 'scissors' and cpu == 'rock':
    print('haha stupid baby')

if cpu == 'rock' and player == 'paper':
    print('you win')
if cpu == 'paper' and player == 'scissors':
    print('you win')
if cpu == 'scissors' and player == 'rock':
    print('you win')
