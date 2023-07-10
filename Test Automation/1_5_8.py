class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()

cart.add(TV('Huilips', 10000))
cart.add(TV('drowiba', 11000))
cart.add(Table('rotang', 1000))
cart.add(Notebook('abser', 20000))
cart.add(Notebook('anus', 21000))
cart.add(Cup('2g1c', 300))

