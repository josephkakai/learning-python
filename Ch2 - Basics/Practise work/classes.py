class vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def ride(self, speed):
        self.mode = "riding"
        self.speed = speed

class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("car")
        self.doors = 4
        self.wheels = 4
        self.engine = enginetype
            
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my ", self.engine, "car at ", self.speed)

class motorcycle(vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:            
            self.wheels = 2
        self.doors = 0
        self.engine = enginetype

    def ride(self, speed):
        super().ride(speed)
        print("Riding my ", self.engine, "motorcycle at", self.speed)

car1 = car("gas") 
car2 = car("electric")
mc1 = motorcycle("gas", True)
mc2 = motorcycle("electric", False)

print(car1.wheels)
print(car1.engine)
print(car1.doors)
print(car2.wheels)
print(car2.engine)
print(car2.doors)
print(mc1.wheels)
print(mc1.engine)
print(mc1.doors)
print(mc2.doors)
print(mc2.engine)
print(mc2.wheels)


car1.drive(f"{30} Km/h")
car2.drive(f"{40} Km/h")
mc1.ride(f"{50} Km/h")
mc2.ride(f"{60} Km/h")
