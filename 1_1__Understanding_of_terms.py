class Tutorial:
    title = "Class Attribute"

    def __init__(self, color):
        self.color = color #local attrib

t = Tutorial("lesson1")
print(t.__dict__) #print out local attributes of the class
print(Tutorial.__dict__) #prib  nt out Class Attributes