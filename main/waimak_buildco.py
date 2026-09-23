class Customer:
    def __init__(self, name, address, delivery_address, customer_type):
        self.name = name
        self.phone = address
        self.delivery_address = delivery_address
        self.customer_type = customer_type

    def customer_discount(self):
        if self.customer_type == "trade_customer":
            return 0.1
        else:
            return 0


    