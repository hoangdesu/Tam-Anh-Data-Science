
# Tic tac toe

# 1 2 3
# 4 5 6
# 7 8 9

# # players: x / o

# player x move: 5

# 1 2 3
# 4 x 6
# 7 8 9

# player o move: 10

# 10 is an invalid move. please enter a number 1-9: 5

# 5 is already used. please select another number: 6

# 1 2 3
# 4 x o
# 7 8 9

# 9: i=2, j=2

# player x move: 2

# 1 x 3
# 4 x o
# 7 8 9

board = [] # 3x3

# Populate data
count = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(count)
        count += 1
    board.append(row)
        
# print(board)

# starting player is always x
player = 'x'

game_continue = True

print()
for row in board:
    for num in row:
        print(num, end=" ")
    print()

# game loop
while game_continue:

    # 1. get user input
    move = int(input(f'\nplayer {player} move: '))
    
    
    # 2. check valid move
    while move < 1 or move > 9:
        move = int(input(f'{move} is an invalid move. Please enter a number 1-9: '))
            
 
    # 3. record move into the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = player
    
    
    # 4. check win condition
    # 1 2 3 or 456 or 789
    
    # horizontal match -> check all rows equal
    # row[i][0] == row[i][1] == row[i][2]
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            print(f'Player {player} wins!')
            game_continue = False
        # for 

    
    # # vertical match -> check all columns equal
    # row[0][i] == row[1][i] == row[2][i]

    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            print(f'Player {player} wins!')
            game_continue = False
    
    
    # diagonal match        
    # board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         if i == j: ...

    # if left to right or right to left match
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        print(f'Player {player} wins!')
        game_continue = False

    
    
    # 5. display the updated board
    print()
    for row in board:
        for num in row:
            print(num, end=" ")
        print()
        
        
    # 6. toggle the player after 1 round
    if player == 'x':
        player = 'o'
    elif player == 'o':
        player = 'x'
    
    
print('Thanks for playing ^o^')

# Tech debt
# Software Developement Cycle => Dont go for perfection

# Naive approach vs Optimal approach
