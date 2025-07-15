
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
        
print(board)
        
        

# game loop
while True:
    # 1. display the board
    print()
    for row in board:
        for num in row:
            print(num, end=" ")
        print()
    
    
    # 2. get user input
    move = int(input('x move: '))
    
    
    # 3. check valid move
    while move < 1 or move > 9:
        move = int(input(f'{move} is an invalid move. Please enter a number 1-9: '))
    
    
    # 4. record move into the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = 'x'
                
    
    # 5. check win condition