def encrypt(plaintext: str, key: int) -> str:
    cipher = ''
    for c in plaintext:
        is_upper = 65 <= ord(c) <= 90
        is_lower = 97 <= ord(c) <= 122
        encrypted_ascii = ord(c)
        if is_upper:
            lower_bound = 65
            upper_bound = 90
            encrypted_ascii = (ord(c) + key - lower_bound) % (upper_bound - lower_bound + 1) + lower_bound;
            # encrypted_ascii = (ord(c) + key) % 90
        elif is_lower:
            # encrypted_ascii = (ord(c) + key) % 122
            encrypted_ascii = (ord(c) + key - 97) % (122 - 97 + 1) + 97;

        cipher += chr(encrypted_ascii)
    
    return cipher
            
            
    
    
print(encrypt('aByZ c', 3)) # -> 'dEbC f'

msg = 'Congratulations, you have successfully encrypted this meaningless message ehehe!'
print(encrypt(msg, 8))



# def decrypt(cipher: str, key: int) -> str:
#     ...

# decrypt('dEbC f', 3) -> 'aByZ c'


# Challenge:
    
# def brute_force(cipher: str) -> list[str]:
#     ...
