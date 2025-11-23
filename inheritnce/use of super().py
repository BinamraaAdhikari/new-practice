class Vehicle():
    
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
         
    def vehicle_info(self):
        print(f"This is a {self.brand} made in {self.year}")
    
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand,year)
        self.doors=doors  
                     
    def car_info(self):
        print(f"This {self.brand} has {self.doors} doors")
    
class Bike(Vehicle):
    def __init__(self,brand,year, type_motor):
        super().__init__(brand,year,)
        self.type_motor=type_motor
        
    def bike_info(self):
        print(f"This {self.brand} is a {self.type_motor} motorcycle")
        
a=Vehicle("Toyota",1998)
c=Car("Toyota",1998,4)
b=Bike("Suzuki",1998,"Cruiser")
a.vehicle_info()
c.car_info()
b.bike_info()    
