import sys

class Translator:
    data = {}

    def add(self, eng, rus):
        Translator.data[eng] = rus


    def remove(self, eng):
        del Translator.data[eng]


    def translate(self, eng):

        print(Translator.data[eng])

tr = Translator()
tr.add('eng', 'rus')
tr.translate(input())