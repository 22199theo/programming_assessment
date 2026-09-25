import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

customers = []

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

def gui():

    window = tk.Tk()
    window.title("Waimak BuildCo Customer Screen")
    window.geometry("720x640")

    customer_viewing = True

    checkbuttons = {
        "TS" : tk.BooleanVar(value=False),
        "UW" : tk.BooleanVar(value=False),
        "IH" : tk.BooleanVar(value=False),
        "DA" : tk.BooleanVar(value=False),
        "MA" : tk.BooleanVar(value=False),
        "SD" : tk.BooleanVar(value=False),
        "LH" : tk.BooleanVar(value=False),
        "BH" : tk.BooleanVar(value=False)
    }

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

    def update_kitchen():
        if not checkbuttons["UW"].get():
            ih_entry.config(state="disabled")
            da_entry.config(state="disabled")
            return

        if checkbuttons["IH"].get():
            da_entry.config(state="disabled")
        else:
            da_entry.config(state="normal")

        if checkbuttons["DA"].get():
            ih_entry.config(state="disabled")
        else:
            ih_entry.config(state="normal")

    # creating a frame so when user selects a different room 
    # we can delete the old selected room function and shows the new one selected
    room_frame = tk.Frame(window)
    room_frame.pack()

    # all room functions
    def bathroom():
            tk.Label(room_frame, text="Bathroom").pack()
            ts_entry = ttk.Checkbutton(room_frame, 
                                       text="Tiles, spa bath, shower and tapware - $2500", 
                                       variable=checkbuttons["TS"])
            ts_entry.pack()

    def kitchen():
            tk.Label(room_frame, text="Kitchen").pack()

            uw_entry = ttk.Checkbutton(room_frame, 
                                    text="Upgrades units and worktop - $2000", 
                                    variable=checkbuttons["UW"],
                                    command=update_kitchen)
            uw_entry.pack()

            ih_entry = ttk.Checkbutton(room_frame, 
                                    text="As A plus induction hob - $3500", 
                                    variable=checkbuttons["IH"],
                                    command=update_kitchen)
            ih_entry.pack()

            da_entry = ttk.Checkbutton(room_frame, 
                                    text="As A plus Deluxe appliance pack - $6000", 
                                    variable=checkbuttons["DA"],
                                    command=update_kitchen)
            da_entry.pack()

            da_entry.config(state="disabled")
            ih_entry.config(state="disabled")

    def living_room():
            tk.Label(room_frame, text="Living Room").pack()

            ma_entry = ttk.Checkbutton(room_frame, 
                                    text="Tv point plus roof mounted aerial - $250", 
                                    variable=checkbuttons["MA"])
            ma_entry.pack()

            sd_entry = ttk.Checkbutton(room_frame, 
                                    text="Tv point plus satellite dish - $250", 
                                    variable=checkbuttons["SD"])
            sd_entry.pack()

            lh_entry = ttk.Checkbutton(room_frame, 
                                    text="4.5 KW Heat pump - $2500", 
                                    variable=checkbuttons["LH"])
            lh_entry.pack()

    def bedroom():
            tk.Label(room_frame, text="Bedroom").pack()
            bh_entry = ttk.Checkbutton(room_frame, 
                                    text="2.5 KW Heat pump - $1800", 
                                    variable=checkbuttons["BH"])
            bh_entry.pack()

    # the function uses event to get the information from the change in combobox 
    def get_room(event):
        nonlocal room_frame 

        room_frame.destroy()

        room_frame = tk.Frame(window)
        room_frame.pack()

        function_rooms = {
            "Bathroom": bathroom,
            "Kitchen": kitchen,
            "Living Room": living_room,
            "Bedroom": bedroom
        }

        room = room_entry.get()
        function_rooms[room]()

    #customer information
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

    #rooms

    tk.Label(window, text="Room").pack()
    room_entry = ttk.Combobox(window,
                              values=["Bathroom", "Kitchen", "Living Room", "Bedroom"], 
                              state="readonly",)
    bathroom()
    room_entry.set("Bathroom")
    #here bind is used to send the information to the get_room function 
    #and <<comboboxselected>> is the event that gets triggered when a user selects something from the combobox
    room_entry.bind("<<ComboboxSelected>>", get_room)
    room_entry.pack()

    tk.Button(window, text="Submit", command=customer).pack()

    window.mainloop()

gui()