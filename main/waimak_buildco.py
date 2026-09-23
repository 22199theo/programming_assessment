import tkinter as tk
from tkinter import messagebox


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


def main_screen():
    while True: 
        try:
            print("Welcome to Waimak BuildCo!")

            navigation = input(
                f''' What would you like to do?
                '''
            )

        except ValueError:
            print("This isn't a valid input.")
    