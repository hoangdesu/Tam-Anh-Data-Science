user_name = input('What is your name: ')

print('Hello ' + user_name)

# Simple calculator

a = int(input('Enter a: '))
b = int(input('Enter b: '))
# '1' + '2'

c = a + b
print('a + b = ' + str(c))
print(str(a) + ' + ' + str(b) + ' = ' + str(a + b))

# Type casting: converting between data types

# 3 + 5 = 8
print(a + b)

# String literal
print(f'{a} - {b} = {a-b}')

# String format
print('{} * {} = {}'.format(a, b, a * b))
print('{first} / {second} = {dividend}'.format(dividend=a/b, first=a, second=b))


# If-elif-else: Conditional (câu điều kiện)

is_raining = input('Is it raining? ') # yes / no

if is_raining == 'yes':
    print('Stay inside')
elif is_raining == 'no':
    print('Go touch grass')
else:
    print('Invalid input. Please type "yes" or "no"')
    
# DRY: don't repeat yourself

nationality = input('Where are you from: ').lower()

if nationality == 'vietnam':
    print('Xin chào!')
elif nationality == 'japan':
    print('こんにちは！　＾０＾')
elif nationality == 'france':
    print('Bonjour!')
else:
    print('Hello!')
    
# Vietnam
# VIETNAM
# VietNam
# => "vietnam"

# "vietnam".

# String methods: actions you can perform on a string

name = 'Tam Anh'
print('Tam Anh'.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.isnumeric())
print('123'.isnumeric())
print(name.count('a'))
print(name.swapcase())
print(name.replace('Tam', 'Tâm'))

# >
# <
# >=
# <=
# ==
# != not equal

amount = int(input('How much you have in your bank account: '))
ferrari = 1_000_000

if amount >= ferrari:
    print('You can buy one')
elif amount < ferrari:
    print('Youre broke')
else:
    print('Just enough')
    
    
# Vertical spacing: doesnt really matter
# Indentation: important
    
    
# HW: BMI calculator

# Challenge 1: Implement the calculator

# Challenge 2: Recommendation system
# How much weight to gain or lose
