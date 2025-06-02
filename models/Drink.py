from models.MenuItem import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, preparation_time, is_alcoholic=False):
        super().__init__(name, price, preparation_time)
        self.__is_alcoholic = is_alcoholic

    @property
    def is_alcoholic(self):
        return self.__is_alcoholic

    def __str__(self):
        return f"Type: Drink, Name: {self.name}, Price: {self.price}$, Preparation: {self.preparation_time} mins, Alcoholic: {'Yes' if self.is_alcoholic else 'No'}"