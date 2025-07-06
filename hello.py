import math

print('hello Python')

# Workflow:
#     1. write code
#     2. save the code
#     3. run the code

# this is a comment, ignored by computer
# for taking notes, temporarily disable a block of code
# shortcut: ctrl + /

print(3 * 5)
print('3 * 5')

# Data types:
#     - string (str): chuỗi ký tự, 'single quotes', "double quotes"
#     - integer (int): whole numbers, e.g.: 3, 0, -9
#     - float: floating point number e.g. 3.14, 0.0
#     - boolean (bool): True / False (1/0 Yes/No)
#     - extras: char: 1 ký tự 'a', '0', bytes, double (float)

# 1010:
# 8421: 8 + 2 = 10
# 8 bits = 1 byte

print('1' + '2')
print(1 + 2)

if False:
    print('1 > 2')
else:
    print('1 < 2')
    

# Variables: biến
# container for data
# Hello + name

name = 'Tam Anh'
print('Hello ' + name)

# Re-assign: overwrite old value
name = 'Brian'
print('Hello ' + name)

# Can assign a different data type
name = 1
print('Hello ', name)

name = True
print('Hello ', name)


first_name = 'Anh'
middle_name = 'Ngoc Tam'
last_name = 'Nguyen'

full_name = last_name + ' ' + middle_name + ' ' + first_name
print('My fullname is: ' + full_name)


# Arithmetic
a = 50
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b) # int / int = float
print(a // b) # integer division
print(a % b) # modulus: get remainder
print(a ** 3) # a ^ 3
print(int(math.pow(a, 3))) # a ^ 3 -> float
print(int(math.sqrt(a)))

# output -> 0101
# pow -> 111000

