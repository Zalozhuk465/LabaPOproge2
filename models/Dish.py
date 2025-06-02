from models.MenuItem import MenuItem

class Dish(MenuItem):
    def __init__(self, name, price, preparation_time, is_vegetarian=False):
        super().__init__(name, price, preparation_time)
        self.__is_vegetarian = is_vegetarian

    @property
    def is_vegetarian(self):
        return self.__is_vegetarian

    def __str__(self):
        return f'Type: Dish, Name: {self.name}, Price: {self.price}$, Preparation: {self.preparation_time} mins, Vegetarian: {"Yes" if self.is_vegetarian else "No"}'