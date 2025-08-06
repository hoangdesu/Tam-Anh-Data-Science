# - OOP: Object-Oriented Programming
# - Paradigm: common pattern

# drink = 'caphe sua da'

# print(drink.)

# # drink: str -> methods
# print(drink[1])

# glasses = 2
# # print(glasses[3])

# Object: container for attributes and methods

# Python's built-in data types: object

# int, str, float, bool

# is_raining = True

# print(is_raining.bit_count)

# a = 15

# print(a.to_bytes())

# 1 byte = 8 bits


# Custom Data type

# Class: blueprint for objects
# 1 class can create multiple objects

# Class: shared design
class Car:
    # Shared attributes
    wheels = 4
    vehicle_type = 'consumer car'
    registered = True
    
    # Constructor: special function to build different objects
    # Initialize
    def __init__(self, brand, price):
        # Individual attributes
        self.brand = brand
        self.price = price
    
    # Methods
    def drive(self):
        if self.brand == 'Ferrari':
            print('🏎️💨')
        else:
            print(f'{self.brand} goes 🚙💨')
    
    
# Objects: created from the same class
toyota = Car('Toyota', 5000)
print('Toyota:', toyota.wheels)
print('Toyota:', toyota.vehicle_type)
print(f'{toyota.brand} is priced at ${toyota.price}')
toyota.drive()


mercedes = Car('Mercedes', 90000)
print('Mercedes:', mercedes.wheels)
print('Mercedes:', mercedes.vehicle_type)
print(f'{mercedes.brand} is priced at ${mercedes.price}')
mercedes.drive()


ferrari = Car('Ferrari', 2_000_000)
print('Ferrari:', ferrari.wheels)
print('Ferrari:', ferrari.vehicle_type)
print(f'{ferrari.brand} is priced at ${ferrari.price}')
ferrari.drive()

