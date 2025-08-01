# Data structure
# Dictionary: key-value pair
# - hashmap / hashtable
# - hash function: one-way function
# - can only extract values from keys, not vice versa

world = {
    'vietnam': 'hue',
    'japan': 'tokyo',
    'france': 'paris',
    'indonesia': 'jakarta',
    'philippines': 'manila'
}

print(world['vietnam']) # must ensure that the key exists
print(world.get('france'))

# print(world['china']) # KeyError
print(world.get('korea')) # None => safer to use

# update current value
world['vietnam'] = 'hanoi'
print(world.get('vietnam'))

# capital_of_vietnam = 'hue'
# capital_of_vietnam = 'hanoi'

# Add new record
world['china'] = 'beijing'

# remove a pair
print('pop: ' + world.pop('indonesia'))

# print(world)

# get all keys
for key in world.keys():
    print('city: ' + key, end="")
    print(' : ' + world[key])
    
# get all values
for val in world.values():
    print('capital: ' + val)
    
for key, val in world.items():
    print(f'key={key} value={val}')
    
    
# object: me :D
brian = {
    'name': {
      'first': 'Brian',
      'last': 'Nguyen'  
    },
    'birth_year': 1995,
    'is_hungry': False,
    'account_balance': 10.5,
    'hobbies': ['piano', 'coding', 'gaming', 'coffee']
}

# key: str, val: can be any data type

print(brian)

# print(world['japan']) -> 'tokyo'

# Big-O notation
# Look-up time:
#     - List: O(n)
#     - Dictionary: O(1)
    
# Add time:
#     - List: Append = O(1), Insert = O(n)
#     - Dictionary: O(1)
    

def phone_word(word: str) -> str:
    # 'a' or 'b' or 'c' -> '2'
    mapped_word = ''

    # print(word.lower())
    
    for c in word.lower():
        match c:
            case 'a' | 'b' | 'c':
                mapped_word += '2'
                # print(c, mapped_word)
            case 'd' | 'e' | 'f':
                mapped_word += '3'
            case 'g' | 'h' | 'i':
                mapped_word += '4'
            case 'j' | 'k' | 'l':
                mapped_word += '5'
            case 'm' | 'n' | 'o':
                mapped_word += '6'
            case 'p' | 'q' | 'r' | 's':
                mapped_word += '7'    
            case 't' | 'u' | 'v':
                mapped_word += '8'
            case 'w' | 'x' | 'y' | 'z':
                mapped_word += '9'
            case _: 
                mapped_word += c
    
    return mapped_word


print(phone_word('1800-APPLE')) # -> '1800-27753'
print(phone_word('1900-SAMSUNG')) # -> '1800-7267864'



Challenge 1: Implement the phone_word() function using Dictionary


Challenge 2: Find frequency (number of appearance) of all characters in a string

def char_frequency(s: str) -> dict:
    ...
    
e.g char_frequency('Tam Anh ne') will return a dictionary like this:
    
    {
        't': 1,
        'a': 2,
        'm': 1,
        'n': 2,
        'h': 1,
        'e': 1
    }

    