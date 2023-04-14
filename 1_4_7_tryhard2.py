import sys

sys.stdin = open('C:\\Users\izrec\Desktop\input.txt', 'r', encoding='utf-8')
lst_in = list(map(str.strip, sys.stdin.readlines()))

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return db.lst_data[a, b]

    def insert(self, data):
        self.lst_data = {i for i from self.FIELDS }
        # db.lst_data.append(dict.fromkeys(DataBase.FIELDS))


db = DataBase()
db.insert(lst_in)
print(db.lst_data)