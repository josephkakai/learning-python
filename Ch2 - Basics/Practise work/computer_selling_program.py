from ctypes.wintypes import HDC  #AUTHORED BY: Joseph Kakai


class Computer:
    def __init__(self, model):
        self.model = model

    def selling_price(self, price):
        self.using = "User frienldy enviroment"
        self.price = price


class Portable(Computer):
    def __init__(self, processortype):
        super().__init__("Portable")
        self.display = "16 inch"
        self.ram = "4GB"
        self.processor = processortype


    def selling_price(self, price):
        super().selling_price(price)
        print("Get good user friendly", self.processor, "portable computer @", self.price)

class Desktop(Computer):
    def __init__(self, towermodel, processortype ):
        super().__init__("Desktop")
        if (towermodel):
            self.ram = "16 GB"
        else:
            self.ram = "8 GB"
        self.display = "42 inch"
        self.processor = processortype
        
    def selling_price(self, price):
        super().selling_price(price)
        print("Get good user friendly", self.processor, "desktop computer @", self.price)

Pcomp1 = Portable("Pentium dual 2GHZ x 2")
Pcomp2 = Portable("intel I core 7 2GHZ X 7")
Dcomp1 = Desktop(True, "AMD Ryzen.7 5800X")
Dcomp2 = Desktop(False, "Intel Celeron Pentium II PE")


print(Pcomp1.display)
print(Pcomp1.ram)
print(Pcomp1.model)
print(Pcomp1.processor)
print(Pcomp2.display)
print(Pcomp2.ram)
print(Pcomp2.model)
print(Pcomp2.processor)
print(Dcomp1.display)
print(Dcomp1.ram)
print(Dcomp1.model)
print(Dcomp1.processor)
print(Dcomp2.display)
print(Dcomp2.ram)
print(Dcomp2.model)
print(Dcomp2.processor)
    
Pcomp1.selling_price(f"{4} KES")
Pcomp2.selling_price(f"{14} KES")
Dcomp1.selling_price(f"{7} KES")
Dcomp2.selling_price(f"{2} KES") 