# Nested loops

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for row in range(1, 6):
    for element in range(1, row+1):
        print(element, end=" ")
    print()
    
print('Tam', end=" ")
print('Anh')

import time

for hour in range(12):
    for minute in range(60):
        for second in range(60):
            print(f'{hour}:{minute}:{second}')
            time.sleep(1)


# Enter height: 4

# *
# **
# ***
# ****

#    *
#   ***
#  *****
# *******

#    *
#   **
#  ***
# ****

# space = row - 1
# after every loop: space = space - 1

height = int(input('Height: '))

for row in range(1, height + 1):
    # print the spaces before the stars
    for _ in range(height - row):
        print(' ', end="")
        
    # print the stars
    for _ in range(1, row + 1):
        print('*', end="")
        
    print()


#    *
#   ***
#  *****
# *******


# row     stars   spaces
# 1       1       3
# 2       3       2
# 3       5       1
# 4       7       0

# row = 28  -> stars = 55 (stars = row * 2 - 1)

height = int(input('Enter pyramid height: '))
char = input('Enter a character: ')
stars = 1
spaces = height - 1

for row in range(1, height+1):
    for _ in range(spaces):
        print(' ', end="")
        
    for _ in range(stars):
        print(char, end="")

    # update the new counters for spaces & stars
    # stars = stars + 2
    stars += 2
    spaces -= 1
    
    print()


# Challenge: print diamond

# Row: only accept odd numbers

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

print(10 % 2)
print(11 % 2)

height = int(input('Enter height (only odd number): '))

while height % 2 != 1:
    height = int(input('No. Enter height (only odd number): '))
    
print('printing diamond...')
