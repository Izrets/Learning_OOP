class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
pt = Point(110, 11)
print(pt.__dict__)