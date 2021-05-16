import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import font
from domains.Course import Course


phase1_window = tk.Tk()
phase1_window.title("Student Manager")
phase1_window.resizable(height=False, width=False)
phase1_window.eval('tk::PlaceWindow . center')
logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase1_window)
logo_lbl.grid(row=0, column=0, padx=30, pady=30)
btn1 = tk.Button(text="Input number of students and students information",
                 command=exit,
                 master=phase1_window)
btn2 = tk.Button(text="Input number of courses and courses information",
                 command=exit,
                 master=phase1_window)
btn3 = tk.Button(text="Cancel", command=exit, master=phase1_window)
btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
phase1_window.mainloop()

