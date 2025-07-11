# Randomization
# Loops + Iterations

# random: 10

# guess: 20
# => wrong. guess lower

# guess: 15
# => wrong. guess lower

# guess: 9
# => wrong. guess higher

# guess: 10
# => Correct!

# END!

import random

random_int = random.randint(1, 100) # inclusive

guess = int(input('Guess: '))
tries = 0

while guess != random_int:
    if guess > random_int:
        guess = int(input('Wrong, guess lower: '))
    elif guess < random_int:
        guess = int(input('Wrong, guess higher: '))
        
    tries = tries + 1
        
print(f'Correct! You guessed in {tries} tries.')
print('Random integer = ' + str(random_int))
    
# game finished

# Using binary search algorithm:
#     - log2(100) ~ 6.6
#     => maximum 6 times to search for a number


# Control flow
# 2 loops: 
#     - for loop: known range
#     - while loop: unknown range, loop using a condition

# convention: i = index

# range(stop): 0 -> stop-1
for i in range(10):
    print('i:', i)
    
# print()


# range(start, stop): start -> stop-1
for z in range(1, 10+1):
    print('z:', z)
    

# print()

# range(start, stop)
# default: step = +1

for x in range(9, 5-1, -1):
    print('x:', x)
    

for ev in range(1, 10+1, 2):
    print(ev)


# Parameters (params) / Arguments (args): inputs for a function


# While loop: manually update the loop condition

# while True:
#     print('hehe')
    
# Ctrl + C: interrupt infinite loop


i = 1
while i <= 10: # i = 1 < 10 => TRUE
    print(i, 'hello python')
    i = i + 1 # i = 10 + 1 => i = 11
    
print('i outside while:', i)

# 2 = 2 + 1
# = assignment operator

password = input('enter your password: ')

attempts = 3
while True:
    if password == 'hehe':
        print('Correct password!')
        break
    elif attempts == 1:
        print('Wrong password. Your accounts has been locked!')
        break
    else:
        password = input('Wrong password. Please enter again: ')
        attempts = attempts - 1


# Challenge: Login app:
#     - for loop
#     - user need to enter a username & a password

    
# bryan
# hehe

for attempts in range(3):
    username = input('Enter username: ')
    
    if username == 'brian':
        break
        

