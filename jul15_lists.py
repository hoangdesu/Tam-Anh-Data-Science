# List can also contain list
# Nested lists, 2D array

# 1D list
# names = ['a', 'b', 'c']
# ---------------------->

phonepad = [
   # 0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

print(phonepad[1][2])

print(phonepad) # on a single line: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# for i in range(len(phonepad)):
#     for j in range(len(phonepad[i])):
#         # print(phonepad[i][j], end=" ")
#         # print(i, j)
        
#         # can directly modify the values
#         # phonepad[i][j] *= 2
#     print()


for row in phonepad:
    for el in row:
        print(el, end=" ")
    print()


print(phonepad)

items = [
    ['iphone', 1, 20],
    ['macbook', 2, 50]
]


for row in items:
    for cell in row:
        print(cell, end="\t")
    print()

invoice = []

while True:
    name = input('\nname: ')
    if name == '': 
        break
    
    qtn = int(input('quantity: '))
    price = float(input('price: '))
    
    item = [name, qtn, price]
    invoice.append(item)
    

print('Name\tQtn\tPrice')
for row in invoice:
    for cell in row:
        print(cell, end="\t")
    print()

for i in range(len(invoice)):
    print(f'{invoice[i][0]}\t{invoice[i][1]}\t{invoice[i][2]}')
    
