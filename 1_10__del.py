class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self, start_pt, end_pt, color):
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color
fig1 = Figure((10, 5), (100, 20), 'blue')

# print(getattr(fig1, 'start_pt', 'no_such_attribute'))
# print(getattr(fig1, 'end_pt', 'no_such_attribute'))
# print(getattr(fig1, 'type_fig', 'no_such_attribute'))
# print(getattr(fig1, 'color', 'no_such_attribute'))
#
# delattr(Figure, 'color')
delattr(fig1, 'color')
# print(Figure.__dict__)
print(*(fig1.__dict__))