import sys

# sys.stdin = open('C:\\Users\izrec\Desktop\input.txt', 'r', encoding='utf-8')
lst_in = list(map(str.strip, sys.stdin.readlines()))
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        # self.a = a
        # # self.b = b
        return db.lst_data[a:b+1]

    def insert(self, data):
        self.lst_in = data
        for i in range(len(data)):
            db.lst_data.append({})

        flatten_lst_in = []
        sp_lst_in = [i.split() for i in data]

        for i in sp_lst_in:
            flatten_lst_in += i
        lst_in = flatten_lst_in

        lst_in_id = 0

        for i in db.lst_data:
            for j in db.FIELDS:
                i[j] = lst_in[lst_in_id]
                lst_in_id += 1



db = DataBase()
db.insert(lst_in)
# print(db.select(1, 3))
