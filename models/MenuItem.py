class MenuItem:
    def __init__(self, name, price, preparation_time):
        self.__name = name
        self.__price = price
        self.__preparation_time = preparation_time

    @property
    def name(self):
        return self.__name
        
    @property
    def price(self):
        return self.__price

    @property
    def preparation_time(self):
        return self.__preparation_time

    def __str__(self):
        raise NotImplementedError()