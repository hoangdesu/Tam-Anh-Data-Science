# print()
# input()
# range()

# Function: hàm
# - re-usable block of code

# parameters / arguments: inputs for a function
# a function might have inputs and/or outputs


# 1. define a function
def intro():
    print(f'Hello nice to meet you!')
    

# # 2. call the function
intro()


def intro_with_name(name):
    print(f'Hello nice to meet you! My name is {name}')
    

intro_with_name('Tam Anh')
intro_with_name('Brian')


def full_intro(name, country, birthyear):
    print(f'Hi my name is {name}. I came from {country} and I am {2025-birthyear} years old!')
    

full_intro('Brian', 'Vietnam', 1995) # positional arguments
full_intro(country='Vietnam', birthyear=2007, name='Tam Anh') # named arguments


# A function can have a return value

def add(a, b):
    c = a + b
    return c
    # print(c)


# need to store the returned value from a function
print(add(1, 2) * 2)

# Return multiple values

x = 1
print('outside', x)

def get_window_dimension(device):
    x = 5
    print('inside', x)
    if device == 'laptop' or device == 'pc':
        width = 1920
        height = 1080
        return width, height
    elif device == 'mobile':
        return 1440, 3200

w, h = get_window_dimension('mobile')
print(f'{w} x {h}')

# Function scope: visibility of a variable with respect to its function

print('outside', x)


# Default params
from random import randint
def hello(name="world", lucky_number=randint(1, 10)):
    print(f'Hello {name}. My lucky number is {lucky_number}')
    
hello()
hello('Tam Anh')
hello('Brian', randint(1, 10))

# Function overloading: NOT supported in Python
# def hi():
#     print('hi')
    
# hi()
    
# this will overwrite the previous
# def hi(name):
#     print(f'hi {name}')
    
# def hi(name, age, pet):


# hi('Brian')
# hi() -> error!

# Variadic function is a function that can accept an arbitrary number of arguments
def sum_all(name, *nums):
    # nums = [all the numbers go here]
    print(name)
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all('brian', 1, 2, 6, 4))
sum1 = sum_all('tam anh', 1, 2, 6, 4, 9, 11, 29, 2, 44)
print(sum1)


def sum_scores(name, score_list):
    print(f'score of {name}:')
    total = 0
    for score in score_list:
        total += score
    return total


print(sum_scores('brian', [1, 2, 5, 7]))


# def reverse_list(lst):
    
# # num_list = [1, 2, 3]
# num_list_reversed = reverse_list(num_list)
# print(num_list_reversed) # [3, 2, 1]


def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count
    print('hẹ hẹ') # not gonna run
    
    
counter = count_even_numbers([1, 2, 3, 4, 5, 8, 9, 10])
print(f'Even numbers: {counter}')


# Challenge 1:

def count_vowels(string) -> int:
    ...
    
count_vowels('Hoang Nguyen') -> 4
count_vowels('Tam Anh') -> 2

# vowels: a, i, u, e, o

# String: a list of characters
name = 'Brian Nguyen'

for i in range(len(name)):
    print(i, name[i])


# Challenge 2: 
    # Fibonacci series

# input: int: length of the fib series
# output: a list containing the length of the series

fibonacci(10) -> [0 1 1 2 3 5 8 13 21 34]

fibonacci(3) -> [0, 1, 1]

fibonacci(length: int) -> list of ints

