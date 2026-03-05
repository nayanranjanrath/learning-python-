class cars ():
    def __init__(self,brand,model):
        self.brand = brand
        self.model =model


    def full_name(self):
        return self.brand+self.model


class e_cars(cars):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

my_car =cars("toyota","corella")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
 
my_ev =e_cars("tesla","model s","85 Kwh")
print(my_ev.brand,my_ev.model,my_ev.full_name())
 

