import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

HOUSE_OPTIONS = {
    "company": "Waimak BuildCo",
    "bathroom": {
        "Tiles, spa bath, shower and tapware": 2500
    },
    "kitchen": [
        {"Upgrades units and worktop": 2000},
        {"As a plus induction hob": 3500},
        {"As a plus Deluxe appliance pack": 6000}
    ],
    "living_room": [
        {"Tv point plus roof mounted aerial": 250},
        {"Tv point plus satellite dish": 250},
        {"4.5 KW Heat pump": 2500}
    ],
    "bedroom": [
        {"2.5 KW Heat pump": 1800}
    ],
    "electrical_sockets": [
        {"1G sockets": 40},
        {"2G sockets": 50}
    ],
    "network_points": [
        {"price": 50, "network switch": 100, "minimum": 2, "maximum": 8}
    ]
}

class Customer:
    def __init__(self, name, address, delivery_address, customer_type):
        self.name = name
        self.address = address
        self.delivery_address = delivery_address
        self.customer_type = customer_type

    def customer_discount(self):
        if self.customer_type == "trade customer":
            return 0.1
        else:
            return 0

class House:
    def __init__(self):
        self.bathroom = None
        self.kitchen = None
        self.living_room = None
        self.bedroom = None



customers = []

def customer():
    name = name_entry.get()
    address = address_entry.get()
    delivery_address = delivery_address_entry.get()
    customer_type = customer_type_entry.get()

    customer = Customer(name, address, delivery_address, customer_type)

    customers.append(customer)

    for x in customers:
        print (x.name, x.address)

    messagebox.showinfo("Success", "Customer added")


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


window = tk.Tk()
window.title("Waimak BuildCo Customer Screen")
window.geometry("720x640")

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Address").pack()
address_entry = tk.Entry(window)
address_entry.pack()

tk.Label(window, text="Delivery Address").pack()
delivery_address_entry = tk.Entry(window)
delivery_address_entry.pack()

tk.Label(window, text="Customer Type").pack()
customer_type_entry = ttk.Combobox(window, 
                                   values=["retail customer", "trade customer"],
                                   state="readonly")
customer_type_entry.set("retail customer")
customer_type_entry.pack()

tk.Label(window, text="test").pack()

tk.Button(window, text="Test", command=customer).pack()




window.mainloop()
