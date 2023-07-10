import sys

class Translator:
    data = {}

    def add(self, eng, rus):
        if eng not in tr.data:
            self.data[eng] = [rus]
        else:
            if rus not in tr.data[eng]:
                self.data[eng].append(rus)
            else:
                pass


    def remove(self, eng):
        del self.data[eng]


    def translate(self, eng):
        return self.data[eng]

tr = Translator()
tr.add("digits", "1")
tr.add("digits", "2")
tr.add("digits", "2")

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.add("digits", "1")
tr.add("digits", "2")
tr.add("digits", "2")

tr.remove('car')
# print(*(tr.translate('go')))
print(tr.data)
assert tr.translate('digits') == ['1', '2']