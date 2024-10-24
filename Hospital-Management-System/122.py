from tkinter import *
import sqlite3
import tkinter
from tkinter.ttk import Separator
from tkinter import messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()
ids = []

class Application:
    def __init__(self, window):
        self.window = window
        self.v = IntVar()
        c.execute("SELECT * FROM appointments")
        self.alldata = c.fetchall()

        self.main = Frame(window, width=450, height=400, bg="lightblue")
        self.showdetailsframe = Frame(self.window)
        self.updateframe = Frame(self.window)
        self.deleteframe = Frame(self.window)

    def startpage(self):
        self.heading = Label(self.main, text="Hospital Management System", font=('Centaur 20 bold'), fg='black', bg="grey", relief=SUNKEN)
        self.heading.place(x=60, y=20)

        self.name = Label(self.main, text="Patients Name", font=('arial 12 bold'), bg="lightblue")
        self.name.place(x=0, y=110)

        self.age = Label(self.main, text="Age", font=('arial 12 bold'), bg="lightblue")
        self.age.place(x=0, y=155)

        Label(self.main, text="Gender", font=('arial 12 bold'), bg="lightblue").place(x=0, y=210)
        a = Radiobutton(self.main, text="Male", padx=20, font="ariel 10 bold", variable=self.v, value=1, bg="lightblue").place(x=130, y=210)
        b = Radiobutton(self.main, text="Female", padx=20, font="ariel 10 bold", variable=self.v, value=2, bg="lightblue").place(x=220, y=210)

        self.time = Label(self.main, text="Location", font=('arial 12 bold'), bg="lightblue")
        self.time.place(x=0, y=255)

        self.phone = Label(self.main, text="Contact Number", font=('arial 12 bold'), bg="lightblue")
        self.phone.place(x=0, y=300)

        # Entry fields
        self.name_ent = Entry(self.main, width=30)
        self.name_ent.place(x=140, y=115)

        self.age_ent = Entry(self.main, width=30)
        self.age_ent.place(x=140, y=160)

        self.location_ent = Entry(self.main, width=30)
        self.location_ent.place(x=140, y=258)

        self.phone_ent = Entry(self.main, width=30)
        self.phone_ent.place(x=140, y=310)

        self.submit = Button(self.main, text="Add Appointment", font="aried 12 bold", width=15, height=2, bg='lightgreen', command=self.add_appointment)
        self.submit.place(x=150, y=340)

        sql2 = "SELECT id FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        self.logs = Label(self.main, text="Total\n Appointments", font=('arial 10 bold'), fg='black', bg="lightblue")
        self.logs.place(x=340, y=320)
        self.logs = Label(self.main, text=" " + str(self.final_id), width=8, height=1, relief=SUNKEN).place(x=360, y=360)

        self.main.pack()

    def add_appointment(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        if self.v.get() == 1:
            self.val3 = "Male"
        elif self.v.get() == 2:
            self.val3 = "Female"
        else:
            self.val3 = "Not Specified"
        self.val4 = self.location_ent.get()
        self.val5 = self.phone_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO 'appointments' (name, age, gender, location, phone) VALUES(?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "\n Appointment for " + str(self.val1) + " has been created")
        self.main.destroy()
        self.__init__(self.window)
        self.startpage()

    # Placeholder method for 'Home' menu item
    def homee(self):
        messagebox.showinfo("Home", "This is the home page")

    # Placeholder method for 'Show details' menu item
    def showdetails(self):
        messagebox.showinfo("Show Details", "Showing appointment details")

    # Placeholder method for 'Update' menu item
    def updatee(self):
        messagebox.showinfo("Update", "Updating appointment details")

    # Placeholder method for 'Delete' menu item
    def deletee(self):
        messagebox.showinfo("Delete", "Deleting appointment details")


def menubar():
    main_menu = Menu(window)
    window.config(menu=main_menu)
    file_menu = Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Home", command=b.homee)
    file_menu.add_command(label="Show details", command=b.showdetails)
    file_menu.add_command(label="Update", command=b.updatee)
    file_menu.add_command(label="Delete", command=b.deletee)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

window = Tk()
b = Application(window)
b.startpage()
menubar()
window.title("Hospital Management")
window.iconbitmap(r'medkit.ico')
window.geometry("450x400")
window.resizable(False, False)

window.mainloop()
