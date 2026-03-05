class cars ():
    def __init__(self,brand,model):
        self.brand = brand
        self.model =model


    def full_name(self):
        return self.brand+self.model


my_car =cars("toyota","corella")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
 
 

