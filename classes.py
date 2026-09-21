class Dog:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'The dog named {self.name} is {self.age} years old.'

# Instantiate a Dog object
ruby = Dog('Ruby', 3)

print(ruby)
print(ruby.name, ruby.age)

ruby.bark()


# Create another Dog object using the default age
liam = Dog('Liam')

print(liam.name, liam.age)


# Create a list
nums = [1, 2, 3]
# Use the dir() function to list all attributes and methods of the list
# print(dir(nums))


print(dir(ruby))

# vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print("Starting up!")

    def stop(self):
        self.running = False
        print("Turning off.")

    def __str__(self):
        return f"The vehicle is a {self.make} {self.model}."


# Create a vehicle
car = Vehicle("Toyota", "RAV4")

print(car)
print(car.running)

car.start()

print(car.running)

car.stop()

print(car.running)

