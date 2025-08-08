# Text files vs Binary files

with open('./data/FoodDatabase.csv', encoding='utf-8-sig') as food_file:
    # content = food_file.read() # return the content of the whole file as 1 big string
    # print(content)
    # food_list = content.split(' - ')
    # print(food_list)
    
    
    # lines = food_file.readlines() # return an array of lines (also include special chars e.g. \n)
    # print(lines)
    
    # line = food_file.readline()
    # print(line)
    
    # line = food_file.readline()
    # print(line)
    
    # line = food_file.readline()
    # print(line)
    
    # food_file.end
    
    
    # EOF: End of File
    
    # line = food_file.readline()
    # while line != '':
    #     print(line)
    #     line = food_file.readline()
    
    
    food_data = []
    for line in food_file:
        print('line', line)
        line = line.replace('\n', '')
        row = line.split(',')
        food_data.append(row)
        
    # food_data[0][0].replace('\ufeff', 'ID')
        
    print(food_data)
    
    for row in food_data:
        print(f'{row[0]}\t{row[1]}\t\t{row[2]}')
    
        
    lowest_rating = food_data[0][2]
    lowest_rated_food = food_data[0]
    for row in food_data:
        rating = row[2]
        if rating < lowest_rating:
            lowest_rating = rating
            lowest_rated_food = row
            
    print(lowest_rated_food)
    

# FILE MODES: 
#     'r': default -> read
#     'w': write, will create a new file or overwrite existing file
#     'a': append, continue where the file left off
    
with open('my_data.txt', 'a') as f:
    name = input('whats ur name: ')
    content = f'Hello {name}!'
    for i in range(10):
        f.write(f'{i+1}. {content}\n')
        
    # should close the file after use
    # f.close()