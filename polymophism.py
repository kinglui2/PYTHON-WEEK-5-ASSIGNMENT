# Animal classes with different move methods
class Dog:
    def move(self):
        return "Running 🐕"

class Cat:
    def move(self):
        return "Walking 🐈"

class Bird:
    def move(self):
        return "Flying 🦅"

# Vehicle classes with different move methods
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"

# Instantiate objects
dog = Dog()
cat = Cat()
bird = Bird()
car = Car()
plane = Plane()
boat = Boat()

# Calling the move method on each object
print(dog.move())
print(cat.move())
print(bird.move())
print(car.move())
print(plane.move())
print(boat.move())
