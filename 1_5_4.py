import  random
class Line:
    sp = ()
    ep = ()
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    sp = ()
    ep = ()
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    sp = ()
    ep = ()
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = (a, b)
        self.ep = (c, d)

figures = [Line, Rect, Ellipse]

elements = [random.choice(figures)(random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100))
            for i in range(217)]

for i in elements:
    if 'Line' in str(i):
        i.sp = (0, 0)
        i.ep = (0, 0)

print(elements[2].sp)