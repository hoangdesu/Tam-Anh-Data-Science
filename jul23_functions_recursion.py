# CLI: command-line interface

# GUI: Graphical-user interface

# Python: dynamically-typed language
# JS -> TS

# Statically-typed languages: C, C++, Java, TypeScript
# int a = 1;
# string name = "";

# type notation:
#     - optional
#     - mark a data type EXPECTED for a variable
#     - no strict enforce on the type like statically typed

# import typing

def count_vowels(name: str) -> int:
    # name.lower()
    # print(name)
    # return True
    
    # "in" keyword: return a boolen
    count = 0
    for char in name.lower():
        if char in ['a', 'i', 'u', 'e', 'o']:
            count += 1
        
        # count = count + 1 if char in ['a', 'i', 'u', 'e', 'o']
            
    return count
    
    
# print(count_vowels('Hoang Nguyen')) # -> 4
# print(count_vowels('Tam Anh')) # -> 2


# name = 'Tam Anh'
# print(name)

# fibonacci(length: int) -> list of ints
def fibonacci(length: int) -> list:
    a = 0
    b = 1
    
    # check edge cases
    if length == 0: 
        return []
    elif length == 1:
        return [a]
    elif length == 2:
        return [a, b]
    
    fib = [a, b]
    
    # excluding the first 2 values
    for i in range(length - 2):
        c = a + b
        a = b
        b = c
        fib.append(c)
        
    return fib

    
# print(fibonacci(10)) # -> [0 1 1 2 3 5 8 13 21 34]
# print(fibonacci(5)) # -> [0, 1, 1, 2, 3]

# a = 0
# b = 1
# c = 1

# a b c
#   a b c
#     a b c
#       a b c
# 0 1 1 2 3 5 8 13 21


def reverse_list(lst: list) -> list:
    # lst.reverse()
    # reversed_lst = []
    # for i in range(len(lst) - 1, -1, -1):
    #     reversed_lst.append(lst[i])
    # return reversed_lst
    
    # Using the two pointers method
    head = 0
    tail = len(lst) - 1
    
    # print(len(lst) // 2)
    
    for i in range(len(lst) // 2):
        # print(lst[head], lst[tail])
        tmp = lst[head]
        lst[head] = lst[tail]
        lst[tail] = tmp
        
        head += 1
        tail -= 1
        
    return lst


# print(reverse_list([1, 2, 3]))
# print(reverse_list([1, 2, 3, 4]))

# 1 2 3 4
# 4 2 3 1
# 4 3 2 1

# Two pointers


# def count_to(num: int):
#     if num == 2:
#         # early return
#         return
    
#     for i in range(100):
#         print(i)
#         if i == num:
#             return # similar to a break
        
# count_to(2)



# Recursion: đệ quy
    # - achiveve repetition similar to for and while loops
    # - a function calling itself
    

# def hello():
#     print('hi!!')
#     hello()
    
#     # Error: Stack overflow
    
#     # while True:
#     #     print('HI!')
    
# hello()


# def count(start: int, stop: int):
#     # base case
#     if start == stop + 1:
#         return
    
#     print(start)
#     count(start + 1, stop)
    
# count(1, 10)


# Iterative vs Recursion: repeat
# for/while vs recursive function

Challenge:
    - iterative_factorial(num)
    - recursive_factorial(num)
    

def iterative_factorial(num: int) -> int:
    ...
    
5! = 5 * 4 * 3 * 2 * 1 = 120
print(iterative_factorial(5)) # = 120



