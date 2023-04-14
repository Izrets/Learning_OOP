import sys
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            self.id, self.title, self.pages = lst_values
            return True#, id, title, pages
        else:
            return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = [1, 2, 3]
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        # StreamData().create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
print(result, data.__dict__)
#
# sr = StreamReader()
# sr.readlines()
# d = StreamData
#
# print(d.__dict__)