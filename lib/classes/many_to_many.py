class Coffee:

    all = []

    def __init__(self, name):
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) >= 3):
            if self._name == name:
                self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        
        unique_customers = []

        for order in self.orders():
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)

        return unique_customers
    
    def num_orders(self):
        counter = 0

        for a in self.orders():
            if a.coffee == self:
                counter+=1
            else:
                pass
        return counter
    
    def average_price(self):
        a = Coffee.orders(self)
        total = 0
        for i in a:
            total+=i.price
        return (total/len(a))

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_list = []
        for order in self.orders():
            if order.coffee not in unique_list:
                unique_list.append(order.coffee)
        
        return unique_list
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if (type(price) == float) and (1.0 <= price <= 10.0):
            if self._price == price:
                self._price = price