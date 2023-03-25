class Item:
    def __init__(self, name, price, quantity):
        self.name = name.title()
        self.price = price
        self.quantity = quantity
        self.total = price * quantity
    def total_sum(self):
        return self.price * self.quantity
item = Item("книга", 500, 10)
print(item.name)
print(item.total)
print(item.total_sum())