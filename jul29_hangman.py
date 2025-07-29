def print_answer_list(lst: list[str]):
    print()
    for c in lst:
        print(c, end=" ")
    print('\n')

description = 'mon nay dung de an vat, va no cay'
key = 'banh trang'
lives = 5

# TODO: later
# database = [
#     ['banh trang', 'mon nay dung de an vat, va no cay'], # 0
#     ['bun dau mam tom', 'mon nay kho an'], # 1
#     ['bun mam', 'mon nay kha pho bien o mien tay'] # 2
# ]

# hint: 'mon nay dung de an vat, va no cay'
# so ky tu: 9

# _ _ _ _ _ _ _ _ _

# enter your guess: 'a'

# _ a _ _ _ a _ _ _

format_key = ''
for c in key:
    if c.isalpha():
        format_key += c.lower()
        
# print(format_key)
# 'banhtrang'

answer = []
for c in format_key:
    answer.append('_')
        

# Game loop
while True:
    print()
    print('Description: ' + description)
    print(f'{len(format_key)} characters')
    print(f'Lives: ', end="")
    for live in range(lives):
        print('❤️ ', end="")
    
    print_answer_list(answer)
    
    guess = input('Enter your guess: ')
    
    # only allow 1 character
    while len(guess) > 1:
        print('Please enter 1 character only!')
        guess = input('Enter your guess: ')
        

    # Do not allow duplicated characters
    for c in answer:
        if guess == c:
            print(f'You have already guessed {guess}')
            guess = input('Enter your guess: ')

    
    # Linear search
    matches = 0
    for i in range(len(format_key)):
        if format_key[i] == guess:
            answer[i] = guess
            matches += 1
        
    print(f'There {'are' if matches > 1 else 'is'} {matches} {'letters' if matches > 1 else 'letter'} {guess}')

    # Check lose condition: deduct lives
    if matches == 0:
        lives -= 1
        print('You lost 1 live')
        
    if lives == 0:
        print(f'Sorry you lost the game :( The answer is {key}')
        break


    # Check win condition: no more underscore
    win = True
    for c in answer:
        if c == '_':
            win = False
            break
    
    if win:
        print_answer_list(answer)
        print(f'Congratulations, you won!! The answer is {key}')
        break
    
