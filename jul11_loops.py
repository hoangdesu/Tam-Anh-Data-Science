# Totaling

total = 0

for _ in range(3):
    num = int(input('Enter a number: '))
    total += num

print(f'Total = {total}')


# Counting

i = 1
count = 0

while i <= 100:
    if i % 7 == 0 or i % 4 == 0:
        print(i)
        count += 1
    i += 1

print(f'There are {count} numbers that are divisible by 7')
    

# Combine conditions -> LOGICAL EXPRESSION
#     - and
#     - or
#     - not
#     - xor, nor, nand
#     - nand = not and, not or


# Interest rate calculator

# in: 1_000_000
# rate: 4.4% / year ⬆️
# after 1 year: 1_044_000

# in: 1_044_000
# rate: 4.4% / year ⬆️
# after 2 years: 1_089_936

deposit = float(input('Enter your deposit amount: '))
rate = 1.044 # 4.4%
years = int(input('How many years: '))

total = deposit

for yr in range(years):
    interest = deposit * rate - deposit
    total += interest
    print(f'Year {yr}: {total:.1f}')

print(f'Total after {years} years = {total:.1f}')

increase = total / deposit

print(f'Your money has increased {increase:.1f} times')

# 1 2 4 8 16 32 64


# Alternating

# flowers = random

# love = True

# for ...:
    
# love
# no love
# love
# no love
# ..
# love

import random
flowers = random.randint(1, 15)
love = True

for i in range(flowers):
    # if love:
    #     print('Love')
    # elif not love:
    #     print('No love')
    
    print('Love') if love else print('No love')
        
    # toggle the boolean
    love = not love
