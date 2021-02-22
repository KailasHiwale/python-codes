class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

order = Order('banana', 1, 5)
order.quantity = -5
print(order.total())