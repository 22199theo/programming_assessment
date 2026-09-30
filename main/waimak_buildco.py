import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#quotes list for quotes, while current_quote 
#is also a list with the intial value set to None
quotes = []
current_quote = [None]

#this dictionary has nest lists and dictionarys as values later used for 
#storing and getting information for house options
HOUSE_OPTIONS = {
    "company": "Waimak BuildCo",
    "bathroom": [{
        "code": "TS", "name": "Tiles, spa bath, shower and tapware", "price": 2500
    }],
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

#This class is used for customer objects, it also has methods such as 
#finding the customer discount and seeing if the customer information is valid 
class Customer:
    def __init__(self, name, address, delivery_address, customer_type):
        self.name = name
        self.address = address
        self.delivery_address = delivery_address
        self.customer_type = customer_type

    #This function sees if a customer is suitable for a discount, 
    #with a trade customer being allowed to have a discount of 0.1 or 10%
    def customer_discount(self):
        if self.customer_type == "trade customer":
            return 0.1
        else:
            return 0

    #This function checks if the customer information submitted is valid, 
    #for example it checks if the name contains strange values such as $ or # 
    #where it will return false if the customer enters a value that is not allowed
    #and will return true if the customer enters a value that is allowed
    def customer_validation(self):
        if not self.name:
            messagebox.showinfo("Error", "Please Enter a Name.")
            return False
        elif len(self.name) > 30:
            messagebox.showinfo("Error", "Your name is too long.")
            return False
        elif not self.name.replace(" ", "").isalpha():
            messagebox.showinfo("Error", "Please only enter letters.")
            return False

        if not self.address:
            messagebox.showinfo("Error", "Please Enter an Address.")
            return False
        elif len(self.address) > 50:
            messagebox.showinfo("Error", "Your address is too long.")
            return False

        if not self.delivery_address:
            messagebox.showinfo("Error", "Please Enter a delivery address.")
            return False
        elif len(self.delivery_address) > 50:
            messagebox.showinfo("Error", "Your delivery address is too long.")
            return False
        
        return True

#This class is used for house objects, which includes all the information for
#the house, such as rooms, electrical sockets etc, it also includes methods
#for validating the house inputs, and calculating the price of the house with the
#addition of the users inputs
class House:
    def __init__(self):

        #This dictionary is used to get all the options the user selects and storing
        #them by the relevant room in a list as the value of the dictionary
        self.rooms = {
            "bathroom": [],
            "kitchen": [],
            "living_room": [],
            "bedroom_1": [],
            "bedroom_2": []
        }

        #This dictionary stores the room names with a nested dictionary in values which
        #stores the amount of electrical sockets per room
        self.electrical_sockets = {
            "bathroom": {"OG": 0, "TG": 0},
            "kitchen": {"OG": 0, "TG": 0},
            "living_room": {"OG": 0, "TG": 0},
            "bedroom_1": {"OG": 0, "TG": 0},
            "bedroom_2": {"OG": 0, "TG": 0}
        }

        #This dictionary stores the room names with the amount of network points the customer
        #selects per room
        self.network_points = {
            "bathroom": 0,
            "kitchen": 0,
            "living_room": 0,
            "bedroom_1": 0,
            "bedroom_2": 0
        }

    #This function checks if the house input is valid, specifically for the amount of 
    #electrical sockets and network sockets the user selects
    def house_validation(self):
        total_sockets = 0

        #electrical socket validation
        #a for loop to go through every item in self.electrical sockets
        for room, sockets in self.electrical_sockets.items():

            #This counts the number of sockets in a room
            room_sockets = sum(sockets.values())

            #if that number exceeds 4 it will return false so the code will not submit the order
            if room_sockets >4:
                messagebox.showerror("Error", f"Too many sockets in {room}, the maximum is 4.")
                return False

            total_sockets += room_sockets 

            #this checks if the total number of sockets exceeds 12, and if it does it will 
            #return false so the code will not submit the order
            if total_sockets > 12:
                messagebox.showerror("Error", "Too many sockets in the house, the maximum is 12.")
                return False

        #network point validation
        total_networks = 0
        #for loop to see the amount of network points in self.network_points
        for network_points in self.network_points.values():
            if network_points != 0:
                total_networks += 1

        #if total_networks is equal to 1 it means the user has only selected one network point which
        #is not allowed and so will return false
        if total_networks == 1:
            messagebox.showerror("Error", "Must have network points in 2 or more rooms")
            return False
            
        #a case boundary value where the code will return false if the amount of network points is smaller then 2
        #or greater then 8, (with the code allowing 0)
        if not 2 <= sum(self.network_points.values()) <= 8 and not sum(self.network_points.values()) == 0:
            messagebox.showerror("Error", "Too many network points in the house, the maximum is 8 (minimum of 2)")
            return False

        return True

    #This function calculates the total cost of all the options the user adds
    def quote_price(self):
        quote_price = 75000

        #calculation for rooms
        #for loop to go through all items in self.rooms
        for rooms, values in self.rooms.items():
            if values:
                #this for loop is used to go through each value in House_options with the key being the room
                #if the code in the house_options[rooms] is in values it will use that indexed value to add the 
                #price of that item to the total
                for value in (HOUSE_OPTIONS[rooms]):
                    if value["code"] in values:
                        quote_price += value["price"]

        #calculation for sockets
        #this for loop goes through all the self.electrical_sockets values
        for sockets in self.electrical_sockets.values():
            #this for loop goes through the one g and two g dictionary in the nested dictionary, sockets
            for socket_type, socket_number in sockets.items():
                #this for loop will compare the socket code of the dictionary to house_options 
                #and will calculate accordingly
                for socket_option in HOUSE_OPTIONS["electrical_sockets"]:
                    if socket_type == socket_option["code"]:
                        quote_price += (socket_option["price"] * socket_number)

        #calculation for network points
        total_network_points = sum(self.network_points.values())
        #this if statement checks if network points were selected, ie. not 1, 
        #and will add the price of the network switch to the total value
        if total_network_points != 0:
            quote_price += (100 + (total_network_points * 50))

        return quote_price

#This class is used for quote objects where it stores the customer and houses, 
#and uses methods to calculate the quote costs, apply discounts and gst, and 
#generates the quote as information that can be saved or displayed 
class Quote:
    def __init__(self, customer):
        self.customer = customer
        self.houses = []

        self.quote_number = len(quotes) + 1

    #This function appneds the added houses to the self.houses list
    def add_house(self, house):
        self.houses.append(house)

    #The next 6 functions are for calculations for the quote text display
    #with original price calculating the original price of the houses
    #with discount_amount calculating the disconut the customer receives
    #with total_discount_price being the total price after the discount
    #with options_price being the price of the options of all houses
    #with gst_amount being the cost of the gst for all options
    #with total_price being the final price of the houses
    def original_price(self):
        original_price = 0

        for house in self.houses:
            original_price += house.quote_price()

        return original_price

    def discount_amount(self):
        discount_amount = self.original_price() * (self.customer.customer_discount())
        return discount_amount

    def total_discount_price(self):
        total_discount_price = self.original_price() - self.discount_amount()
        return total_discount_price

    def options_price(self):
        options_price = self.original_price() - (75000 * len(self.houses))
        return options_price

    def gst_amount(self):
        gst_amount = self.options_price() * 0.15
        return gst_amount

    def total_price(self):
        total_price = self.gst_amount() + self.total_discount_price()
        return total_price

    #This function generates the quote_text, which is used to display the quote
    def quote_text(self):

        network_switch = 0

        quote_text = f'''QUOTE NUMBER: {self.quote_number}
'''
        
        quote_text += f'''CUSTOMER INFORMATION
--------------------------------------------
Customer: {(self.customer.name).capitalize()}
Address: {self.customer.address}
Delivery Address: {self.customer.delivery_address}
Customer Type: {self.customer.customer_type.capitalize()}

'''
        #this for loop uses enumerate to get the index of the house
        #and display it as eg. House 1
        for number, house in enumerate(self.houses, 1):
            quote_text += f'''
HOUSE {number}
--------------------------------------------
'''
            #This for loop gets the items in the house.rooms 
            #The code inside this for loop displays all the information for 
            #each individual room selected and all the options selected for that room
            for rooms, values in house.rooms.items():
                room_selected = False
                total_room_price = 0

                #This if statement checks if the room had any upgrades selected
                if (values or 
                    house.electrical_sockets[rooms]["OG"] or 
                    house.electrical_sockets[rooms]["TG"] or 
                    house.network_points[rooms]):
                        
                        room_selected = True
                        quote_text += f"{rooms.replace('_', ' ').upper()}:\n"

                #This if statement displays the options selected for the
                #relevant room and the price
                if values:
                    for value in (HOUSE_OPTIONS[rooms]):
                        if value["code"] in values:
                            quote_text += f"{value['name']} - ${value['price']}\n"
                            total_room_price += value["price"]

                #This if statement displays any one g sockets selected
                if house.electrical_sockets[rooms]["OG"]:
                    quote_text += (f"1G Electrical Sockets x{house.electrical_sockets[rooms]['OG']} - "
                                f"${(house.electrical_sockets[rooms]["OG"]) * 40}\n")

                #This if statement displays any two g sockets selected
                if house.electrical_sockets[rooms]["TG"]:
                    quote_text += (f"2G Electrical Sockets x{house.electrical_sockets[rooms]['TG']} - "
                                f"${(house.electrical_sockets[rooms]["TG"]) * 50}\n")

                #This if statment displays any network points selected
                if house.network_points[rooms]:
                    network_switch += 1
                    quote_text += (f"Network Point x{house.network_points[rooms]}"
                                f" - ${house.network_points[rooms] * 50}\n")

                #This if statmement will display the total cost of all options, including 
                #electrical and network for the relevant room
                if room_selected:
                    total_room_cost = (
                    total_room_price
                    + (house.network_points[rooms] * 50)
                    + (house.electrical_sockets[rooms]["TG"] * 50)
                    + (house.electrical_sockets[rooms]["OG"] * 40))

                    quote_text += (f"{rooms.replace('_', ' ').capitalize()} total cost - "
                                f"${total_room_cost}\n\n")

        #This if statement checks if the network points were selected
        #and if so it will add the price of the network switch (of all network
        #points selected for each house) eg. if the user selected 3 houses but only
        #two of them have additional network points it will calculate 100 * 2
        if network_switch:
              quote_text += f'''ADDITIONAL COST:
Network Switch - ${100 * network_switch}

'''

        #This section uses all the calculation functions in this class to display
        #the costs of the order
        quote_text += f'''PRICE SUMMARY 
--------------------------------------------
TOTAL ORIGINAL HOUSE(s) COST - ${75000 * len(self.houses)}
TOTAL EXTRA COSTS - ${(self.options_price())}
TOTAL COST (gst exclusive) - ${self.original_price()}
'''

        if self.customer.customer_discount():
            quote_text += f'''DISCOUNT RATE - %{(self.customer.customer_discount() * 100):.0f}
DISCOUNT VALUE - ${self.discount_amount()}
NEW DISCOUNTED COST - ${self.total_discount_price()}
'''
        quote_text += f'''GST COST - ${self.gst_amount()}
TOTAL COST (gst inclusive) - ${self.total_price()}'''

        quote_text += '''

--------------------------------------------
WAIMAK BUILD CO LTD
Unit 3, 93 McKenzie Street, Rangiora, North Canterbury
Tel: 03 1234567
Email: Office@wbc.co.nz
'''
        return quote_text

    #This function actually saves the final users order as a quote to QuoteHistory.txt
    def save_quote(self):
        #This opens QuoteHistory.txt in appnd mode so new quotes are added to the existing file 
        with open("QuoteHistory.txt", "a") as file:
            #this sections writes the relevant quote_text and adds two lines so each quote is displayed nicely
            file.write(self.quote_text())
            file.write("\n\n")

#This Function is used to display the GUI of the whole order, by using tkinter and 
#other methods such as functions and quotes to accurately display, make the gui
#responsive and have boundary cases, and be able to create, cancel, save quotes, read
#them etc. 
def gui():
    #using tkniter here a window is created, with dimensions 700x780
    window = tk.Tk()
    window.title("Waimak BuildCo Customer Screen")
    window.geometry("700x780")

    #This dictionary contains all codes for room options with booleanvar
    #objects as values. These are set to False, and when the customer
    #selects the relevant option, it will switch to True
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

    #dictionary for sockets
    sockets_value = {
    "bathroom": {"OG": 0, "TG": 0},
    "kitchen": {"OG": 0, "TG": 0},
    "living_room": {"OG": 0, "TG": 0},
    "bedroom_1": {"OG": 0, "TG": 0},
    "bedroom_2": {"OG": 0, "TG": 0}
    }   

    #dictionary for network points
    network_points_value = {
    "bathroom": 0,
    "kitchen": 0,
    "living_room": 0,
    "bedroom_1": 0,
    "bedroom_2": 0       
    }

    #this function is used for when a user submits their order
    #it uses multiple functions and methods such as check validation to see if the user input is valid
    #and if it is it then submits it
    def submit_order():
        #yes or no question before submits
        submit_quote = messagebox.askyesno("Submit Quote", "Are you sure you want submit?")
        if submit_quote:
            #customer details submitting 
            name = name_entry.get()
            address = address_entry.get()
            delivery_address = delivery_address_entry.get()
            customer_type = customer_type_entry.get()

            customer = Customer(name, address, delivery_address, customer_type)

            if not customer.customer_validation():
                        return

            house = House()

            #house details submitting and verification

            #here a for loop is used to check all the checkbuttons and then appends them
            #it checks it by using .get() and then uses append to append them to the relevant house
            for codes in checkbuttons.keys():
                if len(codes) == 2:
                    if checkbuttons[codes].get():
                        for rooms, values in HOUSE_OPTIONS.items():
                            #here isinstance checks if the value is a list (to remove company)
                            if isinstance(values, list):
                                for dictionary in values:
                                    if dictionary["code"] == codes:
                                        house.rooms[rooms].append(codes)

            #if checkbuttons["TS"].get():
                #house.rooms["bathroom"].append("TS")

            #if checkbuttons["UW"].get():
                #house.rooms["kitchen"].append("UW")

            #if checkbuttons["IH"].get():
                #house.rooms["kitchen"].append("IH")

            #if checkbuttons["DA"].get():
                #house.rooms["kitchen"].append("DA")

            #if checkbuttons["MA"].get():
                #house.rooms["living_room"].append("MA")

            #if checkbuttons["SD"].get():
                #house.rooms["living_room"].append("SD")

            #if checkbuttons["LH"].get():
                #house.rooms["living_room"].append("LH")

            #if checkbuttons["BO"].get():
                #house.rooms["bedroom_1"].append("BO")

            #if checkbuttons["BT"].get():
                #house.rooms["bedroom_2"].append("BT")

            #copies the network_points_value dictionary to the network_points dictionary
            house.network_points = network_points_value.copy()

            #this for loop is used to check every electrical socket and appends them to the object
            for room in sockets_value:
                house.electrical_sockets[room]["OG"] = sockets_value[room]["OG"]
                house.electrical_sockets[room]["TG"] = sockets_value[room]["TG"]

            if not house.house_validation():
                return
            
            #checks if the current quote list has anything in it
            if current_quote[0] is None:
                #if not it will create the quote with the customer information
                current_quote[0] = Quote(customer)
                quotes.append(current_quote[0])

            #then it will add each house the customer adds to that list
            current_quote[0].add_house(house)

            #allows the display to be edited
            quote_display.config(state="normal")
            #clears the quote before
            quote_display.delete("1.0", "end")
            #shows the new quote
            quote_display.insert("1.0", current_quote[0].quote_text())
            #stops the user from changing the new quote
            quote_display.config(state="disabled")

            reset_quote()

            messagebox.showinfo("Success", "Order added")
        else:
            return

    #This function is used to create a new order by saving or clearing 
    #the current order and resetting customer and house info
    def new_order():
        #this if statement checks if there is currently and order with 
        #at least one house
        if current_quote[0] is not None and current_quote[0].houses:

            save = messagebox.askyesno("Save Order", "Save this order before creating a new one?")

            #if the user chooses yes it saves the current quote to 
            #QuoteHistory.txt
            if save:
                current_quote[0].save_quote()

            #remoes the current quote so a new order can be created
            current_quote[0] = None

        # clear all customer information from input fields
        name_entry.delete(0, "end")
        address_entry.delete(0, "end")
        delivery_address_entry.delete(0, "end")
        customer_type_entry.set("retail customer")
        
        reset_quote()

        #Here the quote display allowed to be edited so it can be deleted
        #then it clears the previous quote and makes the display read only again
        quote_display.config(state="normal")
        quote_display.delete("1.0", "end")
        quote_display.config(state="disabled")

    #this function resets the quote by setting each checkbutton to false
    #clearing all sockets and setting them to zero
    #and setting all networkpoint values to 0
    def reset_quote():
            for key in checkbuttons:
                checkbuttons[key].set(False)

            for room in sockets_value:
                sockets_value[room]["OG"] = 0
                sockets_value[room]["TG"] = 0

            for room in network_points_value:
                network_points_value[room] = 0

    #This function exits the order by saving the current quote, if the user wants to save the quote
    #and using window.destroy() to end the tkniter window
    def exit_order():
        exit_order = messagebox.askyesno("Exit Order", "Are you sure you want to exit the program?")
        if exit_order:
            if current_quote[0] is not None and current_quote[0].houses:
                save = messagebox.askyesno("Save Order", "Save this order before exiting?")

                if save:
                    current_quote[0].save_quote()

            window.destroy()
        else: return

    #allows the customer to cancel the current order by removing the
    #current quote in the quotes list and resetting the quote display
    def cancel_order():
        #this if statement checks if there is currently and order with 
        #at least one house
        if current_quote[0] is None or not current_quote[0].houses:
            messagebox.showinfo("Cancel Order", "There is no order to cancel.")
            return

        cancel = messagebox.askyesno(
            "Cancel Order",
            "Are you sure you want to cancel this order?"
        )

        if cancel:
            #removes the current quote from quote and clears the current
            #quote so a new order can be made
            quotes.remove(current_quote[0])
            current_quote[0] = None

            reset_quote()

            quote_display.config(state="normal")
            quote_display.delete("1.0", "end")
            quote_display.config(state="disabled")

            messagebox.showinfo("Cancelled", "Order cancelled.")

    
    #electrical sockets function display
    def electrical_sockets(room):

        #this functino updates the displayed socket value by getting the users entry
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

    #network points function dislpay
    def network_points(room):

        #this function also updates the displayed by changing it to what the user
        #set the network points as and also updates whether the switch is displayed or not
        def save_network_points(event):
            network_points_value[room] = int(additional_entry.get())

            total = sum(network_points_value.values())
                
            if total == 0:
                checkbuttons["loft_mount_entry"].set(False)
            else:
                checkbuttons["loft_mount_entry"].set(True)

        tk.Label(room_frame, text="Network Points").pack()
        additional_entry = ttk.Combobox(room_frame,
                                values=[0, 1, 2, 3, 4, 5, 6, 7, 8], 
                                state="readonly")
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
        #this function is used to set the ih and da checkbuttons to state disabled(not showing up)
        #if the uw is not checked
        def update_kitchen():
            if not checkbuttons["UW"].get():
                ih_entry.config(state="disabled")
                da_entry.config(state="disabled")

                checkbuttons["IH"].set(False)
                checkbuttons["DA"].set(False)
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

    tk.Button(window, text="Submit Order", command=submit_order).pack()
    tk.Button(window, text="Cancel Order", command=cancel_order).pack()
    tk.Button(window, text="Reset Current Inputs", command=reset_quote).pack()
    tk.Button(window, text="Save / New Order", command=new_order).pack()
    tk.Button(window, text="Save / Exit Program", command=exit_order).pack()

    #this extra display is used to where the quote text is displayed
    quote_display = tk.Text(window, height=15, width=80, state="disabled")
    quote_display.pack()

    window.mainloop()

gui()