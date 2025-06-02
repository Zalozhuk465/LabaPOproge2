from models.MenuItem import MenuItem

class Dessert(MenuItem):
    def __init__(self, name, price, preparation_time, contains_gluten=True):
        super().__init__(name, price, preparation_time)
        self.__contains_gluten = contains_gluten

    @property
    def contains_gluten(self):
        return self.__contains_gluten

    def __str__(self):
        return f"Type: Dessert, Name: {self.name}, Price: {self.price}$, Preparation: {self.preparation_time} mins, Gluten: {'Yes' if self.contains_gluten else 'No'}"