# String: a list of characters

name = 'Tam anh'

# print(name[0])

# String characters are IMMUTABLE
# name[4] = 'A'

name = 'Tam anh'

print(name)

# String methods: functions that operate on a string

print(name.upper())

name = name.replace('anh', 'Anh')

print('name.isdigit:', name.isdigit())

print(name)

# 2 types of method: mutating & non-mutating

# String concatenation: build a string

for i in range(10):
    name += 'h'
    
print(name)


def is_palindrome(s: str) -> bool:
    head = 0 
    tail = len(s) - 1
    
    for i in range(len(s) // 2):
        # print(f'i={i}, head={s[head]}, tail={s[tail]}')
        if s[head] != s[tail]:
            return False
        
        head += 1
        tail -= 1
        
    return True

    
print(is_palindrome('radar')) # -> True
print(is_palindrome('radbcxyzdar')) # -> False


def is_sentence_palindrome(sentence: str) -> bool:
    sentence = sentence.lower()
    head = 0
    tail = len(sentence) - 1
    
    i = 0
    while head <= tail:
        # print(f'i={i}, head={sentence[head]}, tail={sentence[tail]}')
        
        # skipping the head and tail chars until we reach an alphabet character
        while not sentence[head].isalpha():
            head += 1
            
        while not sentence[tail].isalpha():
            tail -= 1
            
        # right here, we got a pair of alphabet chars that can be compared
        print('comparing: ', sentence[head], sentence[tail])
        if sentence[head] != sentence[tail]:
            return False
        
        # move the pointers to the next char
        head += 1
        tail -= 1
        
        # i += 1
    
    return True
    


# print(is_sentence_palindrome('A Santa at NASA')) # True
#                             #    t h 

# print(is_sentence_palindrome('A   #$%^&*  Santa  $%^&* at NAASA =)))')) # True
                        # h               ht                    t
                        
# print('$'.isalpha())
                        
                        
def two_sum(nums: list[int], target: int) -> list[int]:
    

two_sum([2,7,11,15], 9) -> [0, 1]

two_sum([2,7,11,15], 99) -> []

two_sum([2,7,11,15], 4) -> [0, 0]

