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
            

# toyota = Car('Toyota', 5000)

# toyota.wheels = 8
# print('Toyota:', toyota.wheels)

# print('Toyota:', toyota.vehicle_type)

# toyota.price = toyota.price * 0.9
# print(f'{toyota.brand} is priced at ${toyota.price}')
# toyota.drive()


# mercedes = Car('Mercedes', 90000)
# print('Mercedes:', mercedes.wheels)
# print('Mercedes:', mercedes.vehicle_type)
# print(f'{mercedes.brand} is priced at ${mercedes.price}')
# mercedes.drive()


# ferrari = Car('Ferrari', 2_000_000)
# print('Ferrari:', ferrari.wheels)
# print('Ferrari:', ferrari.vehicle_type)
# print(f'{ferrari.brand} is priced at ${ferrari.price}')
# ferrari.drive()



# 4 concepts of OOP:
#     1. Inheritance: tính kế thừa
#     2. Encapsulation: tính đóng gói
#     3. Polymorpshim: tính đa hình
#     4. Abstraction: tính trừu tượng


# Truck is a child class of Car
class Truck(Car):
    # wheels = 10
    # vehicle_type = 'truck'
    
    # if not defined, it will use the default constructor
    def __init__(self, brand, price, wheels, type_of_vehicle, engine):
        self.brand = brand
        self.price = price
        self.wheels = wheels
        self.vehicle_type = type_of_vehicle
        self.engine = engine
        
    
    # override existing methods
    def drive(self):
        print(f'{self.brand} goes 🚛💨')
        
        
class ElectricTruck(Truck):
    ...
    

class DieselTruck(Truck):
    ...
    
    
volvo = Truck("Volvo", 1000, 12, 'it is a truck', 'diesel')
print(volvo.wheels, volvo.registered)
print(volvo.brand, volvo.price, volvo.vehicle_type)
volvo.drive()


tesla = ElectricTruck('Tesla', 20000, 8, 'tesla truck', 'electric')
print(tesla.engine)
tesla.drive()