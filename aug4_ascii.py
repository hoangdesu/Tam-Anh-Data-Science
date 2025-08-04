# ASCII

print(ord('a')) # 97
print(ord(' ')) # 32
print(ord('A'))

def is_alphabet_character(c: str) -> bool:
    is_upper = 65 <= ord(c) <= 90
    is_lower = 97 <= ord(c) <= 122
    if is_upper or is_lower:
        return True
    return False


print(is_alphabet_character('a'))
print(is_alphabet_character('Z'))
print(is_alphabet_character('*'))


def to_upper_case(s: str) -> str:
    res = ''

    difference = 32
    
    for c in s:
        is_lower_char = 97 <= ord(c) <= 122
        if is_lower_char:
            # convert lower to upper case
            upper_ascii = ord(c) - difference
            upper_char = chr(upper_ascii)
            res += upper_char
        else:
            res += c
    
    return res


print(to_upper_case('taM aNh nEeEeee'))

# Hex color:
# #00ffaa

# #RRGGBB
# '0-9,A-F'

from random import randint
# def generate_random_hex_color() -> str:
#     chars = '0123456789ABCDEF'
#     color = '#'
#     for i in range(6):
#         rand_index = randint(0, len(chars) - 1)
#         color += chars[rand_index]
#     return color

def generate_random_hex_color() -> str:
    # group 0: digits
    # group 1: chars A-F
    
    color = '#'
    for i in range(6):
        group = randint(0, 1)
        ascii = 0
        if group == 0:
            ascii = randint(48, 57)
        elif group == 1:
            ascii = randint(65, 70)
        color += chr(ascii)
        
    return color
    

for i in range(10):
    print(generate_random_hex_color()) # -> '#AF9D71'


# Challenge: encrypt and decrypt functions
# - preserve cases and spaces

def encrypt(plaintext: str, key: int) -> str:
    ...
    
    
encrypt('aByZ c', 3) -> 'dEbC f'



def decrypt(cipher: str, key: int) -> str:
    ...

decrypt('dEbC f', 3) -> 'aByZ c'

