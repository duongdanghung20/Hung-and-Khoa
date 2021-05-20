import tkinter as tk
from sqlite3 import Error
import sqlite3
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tkinter.font as font


class Household:
    def __init__(self, id, name, address, area, payment_status=0, monthly_consumption=0):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__payment_status = payment_status
        self.__area = area
        self.__monthly_consumption = monthly_consumption

    def get_hid(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_payment_status(self):
        return self.__payment_status

    def get_area(self):
        return self.__area

    def get_monthly_consumption(self):
        return self.__monthly_consumption

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status

    def set_area(self, area):
        self.__area = area

    def set_monthly_consumption(self, monthly_consumption):
        self.__monthly_consumption = monthly_consumption


class Meter:
    def __init__(self, id, hid, register_year, register_month):
        self.__id = id
        self.__hid = hid
        self.__measurements = [(register_year, register_month, 0)]
        self.__total_months = 0
        self.__total_values = 0

    def get_id(self):
        return self.__id

    def get_hid(self):
        return self.__hid

    def get_total_months(self):
        return self.__total_months

    def get_total_values(self):
        return self.__total_values

    def add_measurements(self, year, month, value):
        self.__measurements.append((year, month, value))
        if self.__measurements[-1][0] == self.__measurements[-2][0]:
            self.__total_months += self.__measurements[-1][1] - self.__measurements[-2][1]
        elif self.__measurements[-1][0] > self.__measurements[-2][0]:
            self.__total_months += self.__measurements[-1][1] + (12 - self.__measurements[-2][1])
        else:
            print("The updated time must be later than the previous one")
        self.__total_values += value

    def get_measurements(self):
        return self.__measurements


class Area:
    def __init__(self, id, price):
        self.__id = id
        self.__price = price

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


class Engine:
    number_of_areas = 0
    number_of_households = 0

    # Create the database electric.db (if not existed) or connect to it (if existed)
    conn = sqlite3.connect('electric.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    # Create tables
    create_households_table = """
    CREATE TABLE IF NOT EXISTS households (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        owner_name VARCHAR (30),
        address VARCHAR (100),
        phone_number INTEGER,
        payment_status INTEGER,
        area_id INTEGER,
        monthly_consumption FLOAT,
        FOREIGN KEY (area_id) 
            REFERENCES areas (id)
                ON DELETE CASCADE 
                ON UPDATE NO ACTION 
    )
    """

    create_areas_table = """
    CREATE TABLE IF NOT EXISTS areas (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        price INTEGER
    )
    """
    create_meters_table = """
    CREATE TABLE IF NOT EXISTS meters (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        household_id VARCHAR (10) , 
        `month` INTEGER,
        `year` INTEGER,
        `value` INTEGER,
        FOREIGN KEY (household_id)
            REFERENCES households (id)
                ON DELETE CASCADE 
                ON UPDATE NO ACTION 
    )
    """

    def input_areas(self, parent):
        try:
            sub = tk.Toplevel(master=parent)
            sub.title("Input Areas")
            sub.resizable(height=False, width=False)

            # Create text entries
            price_ent = tk.Entry(sub, width=30)
            price_ent.grid(row=1, column=1, padx=20)

            # Create text labels
            id_lbl = tk.Label(sub, text=f"Area {self.number_of_areas + 1}: ")
            id_lbl.grid(row=0, column=0, columnspan=2)
            price_lbl = tk.Label(sub, text="Corresponding price: ")
            price_lbl.grid(row=1, column=0)

            # Create Submit Function for Database:
            def submit():
                try:
                    # Create the electric.db or connect to it
                    conn = sqlite3.connect('electric.db')
                    # Create cursor
                    c = conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    # Insert into table
                    c.execute(
                        """INSERT INTO areas (price) VALUES (:price)""",
                        {
                            'price': price_ent.get()
                        }
                    )
                    self.number_of_areas += 1
                    id_lbl["text"] = f"Area {self.number_of_areas + 1}: "
                    # Clear the entries
                    price_ent.delete(0, tk.END)
                    # Commit changes
                    conn.commit()
                    c.execute("""SELECT * FROM areas""")
                    results = c.fetchall()
                    for result in results:
                        print(result)
                    # Close connection
                    conn.close()
                except Error as e:
                    return e

            # Create Submit Button
            submit_btn = tk.Button(sub, text="Add Record to Database", command=submit)
            submit_btn.grid(row=2, column=0, columnspan=2, ipadx=5, ipady=5, pady=5, padx=5)
        except Error as e:
            return e

    def input_households(self, parent):
        try:
            sub = tk.Toplevel(master=parent)
            sub.title("Input Households")
            sub.resizable(height=False, width=False)

            # Create text entries
            name_ent = tk.Entry(sub, width=30)
            name_ent.grid(row=1, column=1, padx=20)
            address_ent = tk.Entry(sub, width=30)
            address_ent.grid(row=2, column=1, padx=20)
            phone_number_ent = tk.Entry(sub, width=30)
            phone_number_ent.grid(row=3, column=1, padx=20)
            area_ent = tk.Entry(sub, width=30)
            area_ent.grid(row=4, column=1, padx=20)

            # Create text labels
            id_lbl = tk.Label(sub, text=f"Household {self.number_of_areas + 1}: ")
            id_lbl.grid(row=0, column=0, columnspan=2)
            name_lbl = tk.Label(sub, text="Owner's name: ")
            name_lbl.grid(row=1, column=0)
            address_lbl = tk.Label(sub, text="Address: ")
            address_lbl.grid(row=2, column=0)
            phone_number_lbl = tk.Label(sub, text="Phone number: ")
            phone_number_lbl.grid(row=3, column=0)
            area_lbl = tk.Label(sub, text="Area: ")
            area_lbl.grid(row=4, column=0)

            # Create Submit Function for Database:
            def submit():
                try:
                    # Create the electric.db or connect to it
                    conn = sqlite3.connect('electric.db')
                    # Create cursor
                    c = conn.cursor()
                    c.execute("PRAGMA foreign_keys = ON")
                    # Check if area_id exist:
                    c.execute("""SELECT id FROM areas""")
                    results = c.fetchall()
                    area_ids = []
                    for result in results:
                        area_ids.append(result[0])
                    while 
                    if area_ent.get() not in area_ids:
                        messagebox.showerror(message="Area ID does not exist")
                        area_ent.delete(0, tk.END)
                    # Insert into table
                    c.execute(
                        """INSERT INTO households (owner_name, address, phone_number, payment_status, area_id, monthly_consumption) VALUES (:owner_name, :address, :phone_number, :payment_status, :area_id, :monthly_consumption)""",
                        {
                            'owner_name': name_ent.get(),
                            'address': address_ent.get(),
                            'phone_number': phone_number_ent.get(),
                            'payment_status': 0,
                            'area_id': area_ent.get(),
                            'monthly_consumption': 0
                        }
                    )
                    self.number_of_households += 1
                    id_lbl["text"] = f"Household {self.number_of_areas + 1}: "
                    # Clear the entries
                    name_ent.delete(0, tk.END)
                    phone_number_ent.delete(0, tk.END)
                    address_ent.delete(0, tk.END)
                    area_ent.delete(0, tk.END)
                    # Commit changes
                    conn.commit()
                    c.execute("""SELECT * FROM households""")
                    results = c.fetchall()
                    for result in results:
                        print(result)
                    # Close connection
                    conn.close()
                except Error as e:
                    return e

            # Create Submit Button
            submit_btn = tk.Button(sub, text="Add Record to Database", command=submit)
            submit_btn.grid(row=5, column=0, columnspan=2, ipadx=5, ipady=5, pady=5, padx=5)
        except Error as e:
            return e

    def update_household_information_with_id(self, hid):
        for household in self.households:
            if hid == household.get_hid():
                print("Enter again all the household's information:")
                household.set_hid(input("Enter household ID: "))
                household.set_name(input("Enter house owner's name: "))
                household.set_address(input("Enter household's address: "))
                household.set_area(input("Enter household's area: "))

    def exist(self, hid):
        for household in self.households:
            if hid == household.get_hid():
                return True
        return False

    def update_household_information(self):
        hid = input("Enter ID of the household requires updating: ")
        if not self.exist(hid):
            print("There exist no household with that ID")
        else:
            self.update_household_information_with_id(hid)

    def delete_household_with_id(self, hid):
        for household in self.households:
            if hid == household.get_hid():
                self.households.remove(household)

    def delete_meter_with_id(self, hid):
        for meter in self.meters:
            if hid == meter.get_hid():
                self.households.remove(meter)

    def delete_household(self):
        hid = input("Enter ID of the household requires deleting: ")
        if not self.exist(hid):
            print("There exist no household with that ID")
        else:
            self.delete_household_with_id(hid)
            self.delete_meter_with_id(hid)

    def list_households(self):
        for household in self.households:
            print(
                household.get_hid() + "-" + household.get_name() + "-" + household.get_address() + "-" + str(
                    household.get_area()) + "-" + str(household.get_payment_status()) + "-" + str(
                    household.get_monthly_consumption()))

    def update_meter_information_with_id(self, hid):
        new_monthly_consumption = 0
        for meter in self.meters:
            if meter.get_hid() == hid:
                year = int(input("Enter the updated year: "))
                month = int(input("Enter the updated month: "))
                value = int(input("Enter the updated value: "))
                meter.add_measurements(year, month, value)
                new_monthly_consumption = meter.get_total_values() / meter.get_total_months()
        for household in self.households:
            if household.get_hid() == hid:
                household.set_monthly_consumption(new_monthly_consumption)

    def update_meter_information(self):
        hid = input("Enter ID of the household meter requires updating: ")
        if not self.exist(hid):
            print("There exist no household with that ID")
        else:
            self.update_meter_information_with_id(hid)

    def update_payment_status_with_id(self, hid):
        for household in self.households:
            if household.get_hid() == hid:
                household.set_payment_status(int(input("Enter updated payment status (an integer from 0 to 2): ")))

    def update_payment_status(self):
        hid = input("Enter ID of the household whose payment status requires updating: ")
        if not self.exist(hid):
            print("There exist no household with that ID")
        else:
            self.update_payment_status_with_id(hid)

    def input_types_of_price(self):
        number_of_types = int(input("Enter number of areas: "))
        for i in range(number_of_types):
            self.prices.append((i + 1, int(input(f"Enter price for area {i + 1} (VND/kWh): "))))

    def auto_increase_payment_status(self):
        for household in self.households:
            household.set_payment_status(household.get_payment_status() + 1)
            if household.get_payment_status() > 2:
                self.delete_household_with_id(household.get_hid())

    def display_household_information(self, hid):
        if not self.exist(hid):
            print("There exist no household with that ID")
        else:
            for household in self.households:
                if household.get_hid() == hid:
                    print(
                        household.get_hid() + "-" + household.get_name() + "-" + household.get_address() + "-" + str(
                            household.get_area()) + "-" + str(household.get_payment_status()) + "-" + str(
                            household.get_monthly_consumption()))

    def display_historical_record_with_id(self, hid):
        for meter in self.meters:
            if meter.get_hid() == hid:
                area = 0
                for household in self.households:
                    if household.get_hid() == hid:
                        area = household.get_area()
                price_value = 0
                for price in self.prices:
                    if price[0] == area:
                        price_value = price[1]
                for measurement in meter.get_measurements():
                    print(f"Year {measurement[0]} - Month {measurement[1]} - Payment: {measurement[2] * price_value}")

    def clear_window(self, window):
        widgets = window.winfo_children()
        for widget in widgets:
            widget.destroy()

    def start_engine(self):

        # init_window = tk.Tk()
        # init_window.title("EIMS")
        # init_window.resizable(height=False, width=False)
        # init_window.eval('tk::PlaceWindow . center')
        # init_lbl = tk.Label(text="Initializing engine: 0%", master=init_window)
        # init_lbl.grid(row=0, column=0, padx=30, pady=10, sticky="s")
        # style = ttk.Style()
        # style.theme_use('default')
        # style.configure("black.Horizontal.TProgressbar", background='cornflower blue')
        # bar = Progressbar(master=init_window, length=200, style='black.Horizontal.TProgressbar')
        # bar['value'] = 0
        # bar.grid(column=0, row=1, padx=30, pady=10, sticky="n")
        # init_window.after(2000, lambda: init_window.destroy())
        #
        # def update_progressbar(value):
        #     bar['value'] = value
        #
        # def update_process(value):
        #     init_lbl['text'] = f"Initializing engine: {value}%"
        #
        # for i in range(100):
        #     init_window.after(20 * i, update_progressbar, i)
        #     init_window.after(20 * i, update_process, i + 1)
        # init_window.mainloop()
        #
        self.c.execute(self.create_areas_table)
        self.c.execute(self.create_households_table)
        self.c.execute(self.create_meters_table)
        #
        # root = tk.Tk()
        # root.title("EIMS")
        # root.resizable(width=False, height=False)
        # root.geometry("400x709")
        # background_img = tk.PhotoImage(file='new_background_img.png')
        # background_label = tk.Label(master=root, image=background_img)
        # background_label.place(relwidth=1, relheight=1)
        # logo_lbl = tk.Label(text="EIMS", font="Fixedsys 60 bold", master=root, fg="white", bg="cornflower blue")
        # logo_lbl.pack(pady=30, fill=tk.X)
        # btn1 = tk.Button(text="Input data", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn2 = tk.Button(text="Delete data", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn3 = tk.Button(text="Update data", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn4 = tk.Button(text="Display data", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn5 = tk.Button(text="Plot figures", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn6 = tk.Button(text="Print bill", font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn7 = tk.Button(text="Exit", master=root, font=("Arial", 16, "bold"), borderwidth=5, width=10, fg="black", bg="light yellow")
        # btn1.pack(pady=10, ipadx=5, ipady=5)
        # btn2.pack(pady=10, ipadx=5, ipady=5)
        # btn3.pack(pady=10, ipadx=5, ipady=5)
        # btn4.pack(pady=10, ipadx=5, ipady=5)
        # btn5.pack(pady=10, ipadx=5, ipady=5)
        # btn6.pack(pady=10, ipadx=5, ipady=5)
        # btn7.pack(pady=10, ipadx=5, ipady=5)
        # root.mainloop()
        root = tk.Tk()
        # self.input_areas(root)
        self.input_households(root)
        root.mainloop()


if __name__ == '__main__':
    e = Engine()
    e.start_engine()
