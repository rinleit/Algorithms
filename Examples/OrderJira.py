import time


class Order:
    def __init__(self, data):
        self.data = data
        self.order_created = time.gmtime()
        self.order_completed = None
        self.order_served = None

    def update_completed(self):
        self.order_completed = time.gmtime()

    def update_served(self):
        self.order_completed = time.gmtime()


class Orders:
    def __init__(self):
        self.orders = []

    def add(self, order):
        if order is not None:
            self.orders.append(order)

    def remove(self, order):
        if order is not None:
            self.orders.remove(order)

    def get_order(self, number):
        for order in self.orders:
            if order.data == number:
                return order

    def orders(self):
        len(self.orders)


class OrderSystem:
    def __init__(self):
        self.orders_in_progress = Orders()
        self.orders_complete = Orders()
        self.order_num = 1

    def add_order(self):
        self.orders_in_progress.add(Order(self.order_num))
        self.order_num += 1

    def remove_incomplete_order(self, order_num):
        self.orders_in_progress.remove(self.orders_in_progress.get_order(order_num))

    # Remove from in progress queue and add to complete queue
    def complete_order(self, order_num):
        order = self.orders_in_progress.get_order(order_num)
        self.orders_in_progress.remove(order)
        order.update_completed()
        self.orders_complete.add(order)

    def serve_order(self, order_num):
        order = self.orders_complete.get_order(order_num)
        order.update_served()
        self.orders_complete.remove(order)

    def remove_order(self, order_num):
        self.orders_complete.remove(self.orders_complete.get_order(order_num))