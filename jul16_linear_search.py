# Linear search: tìm kiếm tuyến tính

menu = ['pho', 'com tam', 'bun mam', 'bun cha']

order = input('what u want to order: ') # pho

# # flag: đặt cờ
found = False

for i in range(len(menu)):
    # if order == menu[i]:
    #     print(f'your {order} is on the way!')
    # else:
    #     print(f'your {order} is not in our menu')
    
    if order == menu[i]:
        found = True
        break # ignore the rest of the list
        

# conclude after finish searching
if found:
    print(f'your {order} is on the way!')
else:
    print(f'sorry, {order} is not in our menu :(')


# # ensure the element exists before finding the index
# print(menu.index('pizza'))


Challenge:
1. give me a list of 10 random numbers


2. allow user to enter an int


3. if found: tell the user WHERE (what index) that number appears in the list
if not found, let the user know

[3, 2, 9, 5, 4]

5
5 appears at index 3 in the list

8
8 appears not to be in the list

