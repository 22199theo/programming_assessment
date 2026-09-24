import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

HOUSE_OPTIONS = {
    "company": "Waimak BuildCo",
    "bathroom": {
        "code": "TS", "name": "Tiles, spa bath, shower and tapware", "price": 2500
    },
    "kitchen": [
        {"code": "UW", "name": "Upgrades units and worktop", "price": 2000},
        {"code": "IH", "name": "As A plus induction hob", "price": 3500},
        {"code": "DA", "name": "As A plus Deluxe appliance pack", "price": 6000}
    ],
    "living_room": [
        {"code": "MA", "name": "Tv point plus roof mounted aerial", "price": 250},
        {"code": "SD", "name": "Tv point plus satellite dish", "price": 250},
        {"code": "LH", "name": "4.5 KW Heat pump", "price": 2500}
    ],
    "bedroom": [
        {"code": "BH", "name": "2.5 KW Heat pump", "price": 1800}
    ],
    "electrical_sockets": [
        {"code": "1G", "name": "1G sockets", "price": 40},
        {"code": "2G", "name": "2G sockets", "price": 50}
    ],
    "network_points": [
        {"code": "NP", "name": "Network point", "price": 50},
        {"code": "NS", "name": "Network switch", "price": 100}
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
        self.bathroom = []
        self.kitchen = []
        self.living_room = []
        self.bedroom = []

        self.electrical_sockets = {
            "bathroom": {"1G": 0, "2G": 0},
            "kitchen": {"1G": 0, "2G": 0},
            "living_room": {"1G": 0, "2G": 0},
            "bedroom1": {"1G": 0, "2G": 0},
            "bedroom2": {"1G": 0, "2G": 0}
        }

    def electrical_socket_validation(self):
        total_sockets = 0

        for room, sockets in self.electrical_sockets.items():

            room_sockets = sum(sockets.values())

            if room_sockets >4:
                messagebox.showerror("Error", f"Too many sockets in {room}, the maximum is 4.")
                return
            
            total_sockets +=room_sockets 

            if total_sockets > 12:
                messagebox.showerror("Error", "Too many sockets in the house, the maximum is 12.")
                return

    def total_price(self):
        total_price = 0

        #if self.bathroom: 
            
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

tk.Label(window, text="Bathroom").pack()
ts_entry = ttk.Checkbutton(window, text="Tiles, spa bath, shower and tapware - $2500")
ts_entry.pack()


tk.Button(window, text="Test", command=customer).pack()

window.mainloop()
