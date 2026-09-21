class Dog:
    next_id = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog #{self.id} named {self.name} is {self.age} years old.'

    @classmethod
    def get_total_dogs(cls):
        return cls.next_id - 1


class ShowDog(Dog):
    def __init__(self, name, age=0, total_earnings=0):
        Dog.__init__(self, name, age)
        self.total_earnings = total_earnings

    def add_prize_money(self, amount):
        self.total_earnings += amount
        print(f'{self.name}\'s new total earnings are ${self.total_earnings}')


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




# Create dogs
harry = Dog('Harry', 2)
print(harry)

maggie = Dog('Maggie')
print(maggie)

spot = Dog('Spot', 2)
diogee = Dog('Diogee')

# Call the class method
print(Dog.get_total_dogs())



# Create a ShowDog
winky = ShowDog('Winky', 3, 1000)

print(winky)

winky.bark()

print(winky.total_earnings)

winky.add_prize_money(500)

print(winky.total_earnings)