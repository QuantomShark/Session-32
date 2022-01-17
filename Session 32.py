class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print("Details:",self.name,self.color,self.price)

    def max_speed(self):
        print("Vehicle's Max Speed is 180km/hr")

    def change_gear(self):
        print("Vehicle can change upto 6 gears")

class Car (Vehicle):
    def max_speed(self):
        print("Car's Maximum Speed is 240 km/hr")

    def change_gear(self):
        print("Car can change upto 7 gears")


car = Car("Car X1","Red",200000)
car.show()
car.max_speed()
car.change_gear()

print("\n")
vehicle = Vehicle("Truck X1","Grey",100000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()
        
