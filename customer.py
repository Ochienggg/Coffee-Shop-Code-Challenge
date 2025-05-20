class Customer:
    def __init__(self, name):
        self.name = name  # This will call the name setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    @property
    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order  # Assuming you have an Order class in the order module
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)  # Adding the order to the coffee's orders

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        return max(customers, key=lambda c: sum(o.price for o in c.orders if o.coffee == coffee))
