# Data structures & Algorithms

# List: 
# - collection of similar items
# - contiguous blocks of memory
# - allowed duplicated elements
# - Array: chuỗi

# food1 = 'pizza'
# food2 = 'fried chicken'
# food3 = 'ramen'

# print('These are my favorite dishes:')
# print(food1)
# print(food2)
# print(food3)

foods = ['pizza', 'fried chicken', 'ramen', 'sushi', 'jajangmyeon', 'takoyaki']
print(foods)

# Elements all have a position (index) starting from 0
# print('Tam Anh likes ' + foods[1])


# List methods: actions you can perform on a list

# add the element to the END of the list
foods.append('bun dau mam tom')
foods.append('bun cha ha noi')

# add at the beginning
foods.insert(0, 'burrito')

# insert in the middle
foods.insert(3, 'yoghurt')

# remove: make sure the element exists, else cause Error
foods.remove('sushi')


# extends or add another list 
quang_ninh_foods = ['cha muc', 'be be', 'be be', 'be be', 'sua chua tran chau ha long']
foods.extend(quang_ninh_foods)

hanoi_foods = ['pho', 'bun thang', 'banh xeo']
foods += hanoi_foods

# Search for an item
print('index of be be:', foods.index('be be')) # element exists
# print('index of bun mam:', foods.index('bun mam')) # element does not exist => Error

# pop: remove the last element
removed_food = foods.pop()
print('removed food:', removed_food)

# remove by index
removed_food = foods.pop(foods.index('jajangmyeon')) # similar to foods.remove('jajangmyeon')
print('removed food:', removed_food)

# foods.clear()

# List + For loop
print('I like ' + str(len(foods)) + ' foods:')
for i in range(len(foods)):
    print('- I like ' + foods[i])

print('Brian likes ' + foods[3]) # IndexError: list index out of range

# Avoid using "magic numbers"

print('count be be:', foods.count('be be'))


print('last element in foods:', foods[len(foods) - 1])
print('last element in foods using NEGATIVE index:', foods[-1], foods[-2])


# list can have different types of data
# list should have the same data type

brian = ['Brian', 'Nguyen', 30, False, 99.500, 123.456]
print(brian)


# List of integers

nums = [12, 50, 9.9, 2.1, 11]

total = 0
for i in range(len(nums)):
    total += nums[i]
    
print(f'total = {total}')


# INVOICE APP

items = [] # str
item_prices = [] # floats

item = input('Enter item name: ')
amount = float(input('Enter amount: '))

while amount != 0:
    # add items and their prices to the corresponding list
    items.append(item)
    item_prices.append(amount)

    # update new values for item and price
    item = input('Enter item name: ')
    if item == '': break
    amount = float(input('Enter amount: '))

total = 0
for i in range(len(item_prices)):
    total += item_prices[i]

print('\n---------- INVOICE ----------')
print('No\tName\t\tPrice')

for i in range(len(items)):
    print(f'{i+1}\t{items[i]}\t\t{item_prices[i]}')
    
print('-----------------------------')
print(f'Total\t\t\t${total}')



# \: Escape character (backward slash)
# \t: tab character
# \n: new line character
# \'
# \"
# \\
# \r

# print('\\^o^/')
# print('\ta\n\n\n\t\tb')

print("My name is \"Tam Anh\"")
print('My name is \'Brian\'')


Challenge: improve on the Invoice app
    
---------------------- INVOICE ------------------------
No      Name            Quantity    Item Price    Total
1       cafe            2           $10.0         $20.0
2       pho             3           $20.0         $60.0
-------------------------------------------------------
Total                                             $80.0
