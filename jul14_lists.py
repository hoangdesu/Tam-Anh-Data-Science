scores = [8.5, 7.2, 6.6, 9.1, 7.8]

# scores[i]: direct access -> allow modify
scores[0] = 6.0

# s is just a copied value of scores[1] -> cannot modify list values
s = scores[1]
s = 9.9

# for i in range(len(scores)):
#     # s = scores[i]
#     # print('s =', s)
#     scores[i] -= 1
    

# Short hand for loop
# for score in scores:
#     score -= 2
#     print('score =', score)


# for i in range(len(scores)):
#     scores[i] *= 2
#     print('score =', scores[i])

# print(scores)


# Calculate the average score
# total = 0

# for score in scores:
#     total += score

# avg = total / len(scores)
# print(f'Average = {avg:.2f}')


# Find max and min
# Max = 9.1
# Min = 6.0

# max vs min: reserved keywords of Python -> avoid using

# temporarily store the first num as the max
max_num = scores[0]
min_num = scores[0]

for num in scores:
    # replace the current num if it's even larger than the max_num
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
        
print(f'Max = {max_num}')
print(f'Min = {min_num}')


# Code conventions:
#     - use vertical lines to separate code
#     - use comments to take note & explain


# Variable naming conventions:
#     - snake_case: this_is_a_very_long_variable_name (-> Python)
#     - camelCase: thisIsAVeryLongVariableName
#     - PascalCase: ThisIsAVeryLongVariableName
#     - var name cannot start with a number or special characters (only _ is OK)

# avoid using stuff like __name__

# Challenge:
a = 1
b = 2

# TODO: swap the values of a and b
...

print('a =', a) # 2
print('b =', b) # 1
