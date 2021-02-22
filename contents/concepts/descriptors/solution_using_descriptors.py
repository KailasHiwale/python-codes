class NonNegative:
    def __init__(self, name):
        self.name = name  # (4)
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]  # (5)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value  # (6)


class Order:
    price = NonNegative('price')  # (3)
    quantity = NonNegative('quantity')

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

order = Order('apple', 1, 10)
order.total()
# 10
order.price = -10
# ValueError: Cannot be negative
order.quantity = -10
# ValueError: Cannot be negative