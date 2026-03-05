class cars:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model =model
    def get_brand(self):
        return self.__brand

 
my_car =cars("lembo","ghost")

my_car.model="dont know"
# print(my_car.__brand)
print(my_car.model)
print(my_car.get_brand())