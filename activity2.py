# Base class
class Vehicle:
    def move(self):
        pass  # This will be overridden

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
