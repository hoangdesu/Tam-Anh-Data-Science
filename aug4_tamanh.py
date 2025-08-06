# def encrypt(plaintext: str, key: int) -> str:
#     res = ''
#     lst = []
    
#     for i in range(65, 91):
#         lst.append(i)

#     for char in plaintext:
#         for i in range(len(lst)):
#             if ord(char) == lst[i]:
#                 num = lst[i] + key
#                 if num <= lst[len(lst) - 1]:
#                     decipher = num
#                 else:
#                     def turn_around(a: int, key: int) -> int:
#                         print(a)
#                         if a <= 90:
#                             return a
#                         turn_around(a - key, key)
#                     turn_around(num, key)
#                     decipher = turn_around(num, key)
#             res += chr(decipher)
#     return res
    
# print(encrypt('aByZ c', 3))  #-> 'dEbC f'




# def decrypt(cipher: str, key: int) -> str:
    # ...

# decrypt('dEbC f', 3) #-> 'aByZ c'

def loop(num: int, char: str, encryption_type):
    encrypt_num = -26 if encryption_type == 'encrypt' else 26
    if encryption_type == 'encrypt':
        char_ascii = 90 if char.isupper() else 122
        if num <= char_ascii:
            return num
    else:
        char_ascii = 65 if char.isupper() else 97
        if num >= char_ascii:
            return num
    return loop(num + encrypt_num, char, encryption_type)


def encrypt(plaintext: str, key: int) -> str:
    res = ''
    #
    for char in plaintext:
        if char.isalpha() and 65 <= ord(char) <= 90:
            if ord(char) + key <= 90:
                en = ord(char) + key
            else:
                # def loop(num):
                #     if num <= 90:
                #         return num
                #     return loop(num - 26)
                en = loop(ord(char) + key, char, 'encrypt')
            res += chr(en)
                
        elif char.isalpha() and 97 <= ord(char) <= 122:
            if ord(char) + key <= 122:
                en = ord(char) + key
            else:
                # def loop(num):
                #     if num <= 122:
                #         return num
                #     return loop(num - 26)

                en = loop(ord(char) + key, char, 'encrypt')
            res += chr(en) 
        else:
            res += char
    return res

encrypted = encrypt('aByZ c', 3)
print(encrypted)
# key = 0
# for i in range(1000):
def decrypt(cipher: str, key: int) -> str:
    res = '' 
    for char in cipher:
        if char.isalpha() and 65 <= ord(char) <= 90:
            if ord(char) - key >= 65:
                decipher = ord(char) - key
            else:
                # def loop(num):
                #     if num >= 65:
                #         return num
                #     return loop(num + 26)
                decipher = loop(ord(char) - key, char, 'decrypt')
            res += chr(decipher)
                
        elif char.isalpha() and 97 <= ord(char) <= 122:
            if ord(char) - key >= 97:
                decipher = ord(char) - key
            else:
                # def loop(num):
                #     if num >= 97:
                #         return num
                #     return loop(num + 26)
                decipher = loop(ord(char) - key, char, 'decrypt')
            res += chr(decipher)

        else:
            res += char
    return res
# print(decrypt('dEbC f', 3)) # -> 'aByZ c'
# key += 1

decrypted = decrypt(encrypted, 3)
print(decrypted)
# print(decrypt('dEbC f', key)) # -> 'aByZ c'