class Money:
    def __init__(self, money):
         self.money = money


my_money = Money(100)
your_money = Money(1000)
print(your_money.__dict__)