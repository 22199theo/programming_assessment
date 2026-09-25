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
    "bedroom_1": [
        {"code": "BO", "name": "2.5 KW Heat pump", "price": 1800}
    ],
    "bedroom_2": [
        {"code": "BT", "name": "2.5 KW Heat pump", "price": 1800}
    ],
    "electrical_sockets": [
        {"code": "OG", "name": "1G sockets", "price": 40},
        {"code": "TG", "name": "2G sockets", "price": 50}
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
        self.bedroom_1 = []
        self.bedroom_2 = []

        self.electrical_sockets = {
            "bathroom": {"OG": 0, "TG": 0},
            "kitchen": {"OG": 0, "TG": 0},
            "living_room": {"OG": 0, "TG": 0},
            "bedroom_1": {"OG": 0, "TG": 0},
            "bedroom_2": {"OG": 0, "TG": 0}
        }

        self.network_points = {
            "bathroom": 0,
            "kitchen": 0,
            "living_room": 0,
            "bedroom_1": 0,
            "bedroom_2": 0
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

    checkbuttons = {
        "TS" : tk.BooleanVar(value=False),
        "UW" : tk.BooleanVar(value=False),
        "IH" : tk.BooleanVar(value=False),
        "DA" : tk.BooleanVar(value=False),
        "MA" : tk.BooleanVar(value=False),
        "SD" : tk.BooleanVar(value=False),
        "LH" : tk.BooleanVar(value=False),
        "BO" : tk.BooleanVar(value=False),
        "BT" : tk.BooleanVar(value=False),

        "additional_entry" : tk.BooleanVar(value=False),
        "loft_mount_entry" : tk.BooleanVar(value=False)
    }

    sockets_value = {
    "bathroom": {"OG": 0, "TG": 0},
    "kitchen": {"OG": 0, "TG": 0},
    "living_room": {"OG": 0, "TG": 0},
    "bedroom_1": {"OG": 0, "TG": 0},
    "bedroom_2": {"OG": 0, "TG": 0}
    }   

    network_points_value = {
    "bathroom": 0,
    "kitchen": 0,
    "living_room": 0,
    "bedroom_1": 0,
    "bedroom_2": 0       
    }

    #function once user submits their order
    def submit_order():
        name = name_entry.get()
        address = address_entry.get()
        delivery_address = delivery_address_entry.get()
        customer_type = customer_type_entry.get()

        customer = Customer(name, address, delivery_address, customer_type)

        house = House()

        if checkbuttons["TS"].get():
            house.bathroom.append("TS")

        if checkbuttons["UW"].get():
            house.kitchen.append("UW")

        if checkbuttons["IH"].get():
            house.kitchen.append("IH")

        if checkbuttons["DA"].get():
            house.kitchen.append("DA")

        if checkbuttons["MA"].get():
            house.living_room.append("MA")

        if checkbuttons["SD"].get():
            house.living_room.append("SD")

        if checkbuttons["LH"].get():
            house.living_room.append("LH")

        if checkbuttons["BO"].get():
            house.bedroom_1.append("BO")

        if checkbuttons["BT"].get():
            house.bedroom_2.append("BT")

        #copies the network_points_value dictionary to the network_points dictionary
        house.network_points = network_points_value.copy()

        for room in sockets_value:
            house.electrical_sockets[room]["OG"] = sockets_value[room]["OG"]
            house.electrical_sockets[room]["TG"] = sockets_value[room]["TG"]

        print (house.bathroom)
        print (house.kitchen)
        print (house.living_room)
        print (house.bedroom_1)
        print (house.bedroom_2)

        for x in customers:
            print (x.name, x.address)


        messagebox.showinfo("Success", "Customer added")

    #electrical sockets 
    def electrical_sockets(room):

        def save_sockets(event):
            sockets_value[room]["OG"] = int(OG_entry.get())
            sockets_value[room]["TG"] = int(TG_entry.get())

        tk.Label(room_frame, text="Additional Electrical Sockets (1G) - $40").pack()
        OG_entry = ttk.Combobox(room_frame, 
                                values=[0, 1, 2, 3, 4],
                                state="readonly")
        OG_entry.set(sockets_value[room]["OG"])
        OG_entry.pack()

        tk.Label(room_frame, text="Additional Electrical Sockets (2G) - $50").pack()
        TG_entry = ttk.Combobox(room_frame, 
                                values=[0, 1, 2, 3, 4],
                                state="readonly")
        TG_entry.set(sockets_value[room]["TG"])
        TG_entry.pack()

        OG_entry.bind("<<ComboboxSelected>>", save_sockets)
        TG_entry.bind("<<ComboboxSelected>>", save_sockets)

    #network points
    def network_points(room):
        def save_network_points(event):
            network_points_value[room] = int(additional_entry.get())

            total = sum(network_points_value.values())
                
            if total == 0:
                checkbuttons["loft_mount_entry"].set(False)
            else:
                checkbuttons["loft_mount_entry"].set(True)

        tk.Label(room_frame, text="Network Points").pack()
        additional_entry = ttk.Combobox(room_frame,
                                values=[0, 1, 2, 3, 4, 5, 6, 7, 8], )
        additional_entry.set(network_points_value[room])
        #here bind is used to send the information to the loft_mount function 
        #and <<comboboxselected>> is the event that gets triggered when a user selects something from the combobox
        additional_entry.bind("<<ComboboxSelected>>", save_network_points)
        additional_entry.pack()

        loft_mount_entry = ttk.Checkbutton(room_frame,
                                        text="loft mounted 8 port 10/100/1000 network switch - $100",
                                        state="disabled",
                                        variable=checkbuttons["loft_mount_entry"])
        loft_mount_entry.pack()

    # all room functions
    def bathroom():
            ts_entry = ttk.Checkbutton(room_frame, 
                                       text="Tiles, spa bath, shower and tapware - $2500", 
                                       variable=checkbuttons["TS"])
            ts_entry.pack()

            electrical_sockets("bathroom")
            network_points("bathroom")

    def kitchen():
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

        electrical_sockets("kitchen")
        network_points("kitchen")

        da_entry.config(state="disabled")
        ih_entry.config(state="disabled")

    def living_room():
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

            electrical_sockets("living_room")
            network_points("living_room")

    def bedroom_1():
            b1_entry = ttk.Checkbutton(room_frame, 
                                    text="2.5 KW Heat pump - $1800", 
                                    variable=checkbuttons["BO"])
            b1_entry.pack()

            electrical_sockets("bedroom_1")
            network_points("bedroom_1")

    def bedroom_2():
            b2_entry = ttk.Checkbutton(room_frame, 
                                    text="2.5 KW Heat pump - $1800", 
                                    variable=checkbuttons["BT"])
            b2_entry.pack()

            electrical_sockets("bedroom_2")
            network_points("bedroom_2")

    # the function uses event to get the information from the change in combobox 
    def get_room(event):

        #this for loop is used to remove everything currently in room_frame
        #winfo_children identifies each widget in the room_frame
        #and then by using a for loop it will go through each widget and remove it
        for widget in room_frame.winfo_children():
            widget.destroy()

        function_rooms = {
            "Bathroom": bathroom,
            "Kitchen": kitchen,
            "Living Room": living_room,
            "Bedroom 1": bedroom_1,
            "Bedroom 2": bedroom_2
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
                              values=["Bathroom", "Kitchen", "Living Room", "Bedroom 1", "Bedroom 2"], 
                              state="readonly",)
    room_entry.set("Bathroom")
    #here bind is used to send the information to the get_room function 
    #and <<comboboxselected>> is the event that gets triggered when a user selects something from the combobox
    room_entry.bind("<<ComboboxSelected>>", get_room)
    room_entry.pack()
    # creating a frame so when user selects a different room 
    # we can delete the old selected room function and shows the new one selected
    room_frame = tk.Frame(window)
    room_frame.pack()
    bathroom()

    tk.Button(window, text="Submit", command=submit_order).pack()

    window.mainloop()

gui()