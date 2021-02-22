class Order:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self._quantity = quantity

    @property
    def quantity(self):
        print('--> check on property')
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        print('--> check on quantity.setter')
        if value < 0:
            raise ValueError('Cannot be negative.')
        self._quantity = value

    def total(self):
        return self.price * self._quantity


order = Order('Banana', 5, 10)
order.quantity = -10
total = order.total()
print(total)