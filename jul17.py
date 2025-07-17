# Ctrl + click: var, module, function
# Bring u to definition

import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 100))
    
print(nums)

index = 0
found = False
n = int(input('Enter a num: '))

for num in nums:
    if n == num:
        found = True
        break
    index += 1
    
if found:
    print(index)
else:
    print('not found')



# List comprehensions

# 1->10
nums = [i for i in range(10, 21)]

for i in range(1, 11):
    nums.append(i)
    
print(nums)

even_nums = [x for x in range(10, 101) if x % 2 == 0] # one-liner => Pythonic
print(even_nums)



# Ternary: short-hand if-else
age = int(input('Enter your age: '))

ticket = 'adult' if age >= 18 else 'baby' if age <= 3 else 'teenager'

print(f'You have {ticket} ticket')


# Data Mapping
day = int(input('enter a day in the week (1-7): '))

# mapping: Connect a data in 1 column to data in another column
# 1: Monday
# 2: Tuesday
# ...

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 1 => Monday = days_of_week[0]
# 2 => Tuesday = days_of_week[1]
# 3 => Wednesday = days_of_week[2]

if day >= 1 and day <= len(days_of_week):
    print(days_of_week[day - 1])
else:
    print('Invalid day (1-7)')


# Match-case
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case _: # default case
        print('Invalid day (1-7)')



# Rock-paper-scissors

# Individual imports: more optimized, faster
from random import randint 

moves = ['keo', 'bua', 'bao']

# print(computer_move)

# if player_move == 'bua' and computer_move == 'bua':
#     print('Draw')
# elif player_move == 'bua' and computer_move == 'bao':
#     print('Computer wins')

player_score = 0
computer_score = 0

while True:
    random_index = randint(0, len(moves) - 1)
    computer_move = moves[random_index]

    player_move = input('Enter a move (keo, bua, bao): ')
    
    if player_move == 'quit':
        break
    
    # Ensure the player move is valid before continue
    # found = False
    # for move in moves:
    #     if player_move == move:
    #         found = True
    #         break
    
    # if not found:
    #     while
    
    while player_move not in moves:
        print('Invalid move!')
        player_move = input('Enter a move (keo, bua, bao): ')
        
    winner = '' # 'player' | 'computer' | 'draw'
    
    print(f'Player: {player_move} | Computer: {computer_move}')

    if player_move == 'bua':
        if computer_move == 'keo':
            winner = 'player'
        elif computer_move == 'bua':
            winner = 'draw'
        elif computer_move == 'bao':
            winner = 'computer'
    elif player_move == 'keo':
        if computer_move == 'keo':
            winner = 'draw'
        elif computer_move == 'bua':
            winner = 'computer'
        elif computer_move == 'bao':
            winner = 'player'
    elif player_move == 'bao':
        if computer_move == 'keo':
            winner = 'computer'
        elif computer_move == 'bua':
            winner = 'player'
        elif computer_move == 'bao':
            winner = 'draw'
    
    match winner:
        case 'computer':
            print('Computer wins!')
            computer_score += 1
        case 'player':
            print('Player wins!')
            player_score += 1
        case 'draw':
            print('Draw')
            
    print(f'Player score: {player_score} | Computer score: {computer_score}\n')
    
print('Thanks for playing!')
