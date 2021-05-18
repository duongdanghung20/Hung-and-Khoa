import math
# import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *
import tkinter as tk
from tkinter import messagebox


# A function to directly input a student object
def input_student(engine, sid, name, dob):
    Student(engine, sid, name, dob)


# A function to directly input a course object
def input_course(engine, sid, name, dob):
    Course(engine, sid, name, dob)


# A function to directly input a mark object
def input_mark(engine, sid, cid, value):
    Mark(engine, sid, cid, value)


class Input:
    # Function to ask user to input number of student.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_students(self, engine, window):
        sub = tk.Toplevel(master=window)
        sub.title("Number of students")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        lbl = tk.Label(text="Enter number of students:", master=frm1)
        number_of_students_var = tk.StringVar()
        ent = tk.Entry(width=3, master=frm1, textvariable=number_of_students_var)
        ent.focus_set()
        lbl.grid(row=0, column=0, padx=5)
        ent.grid(row=0, column=1, padx=5)
        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(event=None):
            try:
                number_of_students = int(number_of_students_var.get())
                if number_of_students < 0:
                    messagebox.showerror(message="Error: number of students must be non-negative")
                    ent.delete(-1, tk.END)
                else:
                    engine.number_of_students = number_of_students
                    sub.destroy()
            except:
                messagebox.showerror(message="Invalid number of students")
        sub.bind("<Return>", ok)
        ok_btn = tk.Button(text="OK", master=frm2, command=ok)
        ok_btn.bind("<Return>", ok)
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)


    # Function to ask user to input number of courses.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_courses(self, engine, window):
        sub = tk.Toplevel(master=window)
        sub.title("Number of courses")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        lbl = tk.Label(text="Enter number of courses:", master=frm1)
        number_of_courses_var = tk.StringVar()
        ent = tk.Entry(width=3, master=frm1, textvariable=number_of_courses_var)
        ent.focus_set()
        lbl.grid(row=0, column=0, padx=5)
        ent.grid(row=0, column=1, padx=5)
        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(event=None):
            try:
                number_of_courses = int(number_of_courses_var.get())
                if number_of_courses < 0:
                    messagebox.showerror(message="Error: number of courses must be non-negative")
                    ent.delete(-1, tk.END)
                else:
                    engine.number_of_courses = number_of_courses
                    sub.destroy()
            except:
                messagebox.showerror(message="Invalid number of courses")

        sub.bind("<Return>", ok)
        ok_btn = tk.Button(text="OK", master=frm2, command=ok)
        ok_btn.bind("<Return>", ok)
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)

    # Function to input a student object information. Force the user to re-input if wrong data is given
    def input_student_information(self, engine, window, student_order):
        sub = tk.Toplevel(master=window)
        sub.title(f"Student #{student_order}")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        sid_lbl = tk.Label(text="Enter student ID:", master=frm1)
        sid_var = tk.StringVar()
        sid_ent = tk.Entry(width=30, master=frm1, textvariable=sid_var)
        sid_ent.focus_set()
        sid_lbl.grid(row=0, column=0, padx=5, sticky="e")
        sid_ent.grid(row=0, column=1, padx=5, sticky="w")
        name_lbl = tk.Label(text="Enter student name:", master=frm1)
        name_var = tk.StringVar()
        name_ent = tk.Entry(width=30, master=frm1, textvariable=name_var)
        name_lbl.grid(row=1, column=0, padx=5, sticky="e")
        name_ent.grid(row=1, column=1, padx=5, sticky="w")
        dob_lbl = tk.Label(text="Enter student date of birth:", master=frm1)
        dob_frm = tk.Frame(master=frm1)
        date_var = tk.StringVar()
        date_ent = tk.Entry(width=2, master=dob_frm, textvariable=date_var)
        dash_lbl_1 = tk.Label(text="/", master=dob_frm)
        month_var = tk.StringVar()
        month_ent = tk.Entry(width=2, master=dob_frm, textvariable=month_var)
        dash_lbl_2 = tk.Label(text="/", master=dob_frm)
        year_var = tk.StringVar()
        year_ent = tk.Entry(width=4, master=dob_frm, textvariable=year_var)
        dob_lbl.grid(row=2, column=0, padx=5, sticky="e")
        date_ent.grid(row=0, column=0)
        dash_lbl_1.grid(row=0, column=1)
        month_ent.grid(row=0, column=2)
        dash_lbl_2.grid(row=0, column=3)
        year_ent.grid(row=0, column=4)
        dob_frm.grid(row=2, column=1, padx=5, sticky="w")

        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(event=None):
            sid = sid_var.get().strip()
            name = name_var.get()
            date = date_var.get()
            month = month_var.get()
            year = year_var.get()
            month_31 = [1, 3, 5, 7, 8, 10, 12]
            month_30 = [4, 6, 9, 11]
            if len(sid) == 0 or sid is None:
                messagebox.showerror(message="Error: Student ID cannot be empty")
            elif sid in engine.students_id:
                messagebox.showerror(message="Error: Student ID existed")
                sid_ent.delete(-1, tk.END)
            elif len(name) == 0 or name is None:
                messagebox.showerror(message="Error: Student name cannot be empty")
            elif len(date) == 0 or date is None or len(month) == 0 or month is None or len(year) == 0 or year is None:
                messagebox.showerror(message="Error: Student date of birth cannot be empty")
            elif int(month) < 1 or int(month) > 12:
                messagebox.showerror(message="Error: Invalid date of birth")
                date_ent.delete(-1, tk.END)
                month_ent.delete(-1, tk.END)
                year_ent.delete(-1, tk.END)
            elif int(month) == 2 and (int(date) < 1 or int(date) > 29):
                messagebox.showerror(message="Error: Invalid date of birth")
                date_ent.delete(-1, tk.END)
                month_ent.delete(-1, tk.END)
                year_ent.delete(-1, tk.END)
            elif int(month) in month_31 and (int(date) < 1 or int(date) > 31):
                messagebox.showerror(message="Error: Invalid date of birth")
                date_ent.delete(-1, tk.END)
                month_ent.delete(-1, tk.END)
                year_ent.delete(-1, tk.END)
            elif int(month) in month_30 and (int(date) < 1 or int(date) > 30):
                messagebox.showerror(message="Error: Invalid date of birth")
                date_ent.delete(-1, tk.END)
                month_ent.delete(-1, tk.END)
                year_ent.delete(-1, tk.END)
            else:
                dob = f"{date}/{month}/{year}"
                Student(engine, sid, name, dob)
                sub.destroy()

        sub.bind("<Return>", ok)
        ok_btn = tk.Button(text="OK", master=frm2, command=ok)
        ok_btn.bind("<Return>", ok)
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)

    # Function to input a course object information. Force the user to re-input if wrong data is given
    def input_course_information(self, engine, window, course_order):
        sub = tk.Toplevel(master=window)
        sub.title(f"Course #{course_order}")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        cid_lbl = tk.Label(text="Enter course ID:", master=frm1)
        cid_var = tk.StringVar()
        cid_ent = tk.Entry(width=30, master=frm1, textvariable=cid_var)
        cid_ent.focus_set()
        cid_lbl.grid(row=0, column=0, padx=5, sticky="e")
        cid_ent.grid(row=0, column=1, padx=5, sticky="w")
        name_lbl = tk.Label(text="Enter course name:", master=frm1)
        name_var = tk.StringVar()
        name_ent = tk.Entry(width=30, master=frm1, textvariable=name_var)
        name_lbl.grid(row=1, column=0, padx=5, sticky="e")
        name_ent.grid(row=1, column=1, padx=5, sticky="w")
        credits_lbl = tk.Label(text="Enter course credits:", master=frm1)
        credits_var = tk.StringVar()
        credits_ent = tk.Entry(width=3, master=frm1, textvariable=credits_var)
        credits_lbl.grid(row=2, column=0, padx=5, sticky="e")
        credits_ent.grid(row=2, column=1, padx=5, sticky="w")

        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(event=None):
            cid = cid_var.get()
            name = name_var.get()
            course_credits = credits_var.get()
            if len(cid) == 0 or cid is None:
                messagebox.showerror(message="Error: Course ID cannot be empty")
            elif cid in engine.courses_id:
                messagebox.showerror(message="Error: Course ID existed")
                cid_ent.delete(-1, tk.END)
            elif len(name) == 0 or name is None:
                messagebox.showerror(message="Error: Course name cannot be empty")
            elif len(course_credits) == 0 or credits is None:
                messagebox.showerror(message="Error: Course credits cannot be empty")
            elif int(course_credits) < 0:
                messagebox.showerror(message="Error: Course credits must be non-negative")
                credits_ent.delete(-1, tk.END)
            else:
                Course(engine, cid, name, int(course_credits))
                sub.destroy()

        sub.bind("<Return>", ok)
        ok_btn = tk.Button(text="OK", master=frm2, command=ok)
        ok_btn.bind("<Return>", ok)
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)

    # Function to input a mark object information. Force the user to re-input if wrong data is given
    def input_course_mark(self, engine, cid, window):
        for student in engine.students:
            sid = student.get_sid()
            sub = tk.Toplevel(master=window)
            sub.title(f"Student #{engine.students.index(student)}")
            sub.resizable(height=False, width=False)
            window.eval(f'tk::PlaceWindow {str(sub)} center')
            frm1 = tk.Frame(master=sub)
            frm1.grid(row=0, column=0, padx=10, pady=10)
            value_lbl = tk.Label(text=f"Enter mark for {student.get_name()}:", master=frm1)
            value_var = tk.StringVar()
            value_ent = tk.Entry(width=4, master=frm1, textvariable=value_var)
            value_ent.focus_set()
            value_lbl.grid(row=0, column=0, padx=5)
            value_ent.grid(row=0, column=1, padx=5)

            frm2 = tk.Frame(master=sub)
            frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

            def ok(event=None):
                value = math.floor(float(value_var.get()) * 10) / 10.0
                if value < 0:
                    messagebox.showerror(message="Error: Mark must be non-negative")
                    value_ent.delete(-1, tk.END)
                else:
                    Mark(engine, sid, cid, value)
                    sub.destroy()

            sub.bind("<Return>", ok)
            ok_btn = tk.Button(text="OK", master=frm2, command=ok)
            ok_btn.bind("<Return>", ok)
            ok_btn.pack(ipadx=5)
            sub.wait_window(sub)

    # Ask the user for the course ID whose mark should be input, then invoke the input_course_mark() function
    def input_mark(self, engine, window):
        sub = tk.Toplevel(master=window)
        sub.title(f"Input mark")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        cid_lbl = tk.Label(text=f"Enter the course ID you want to input mark:", master=frm1)
        cid_var = tk.StringVar()
        cid_ent = tk.Entry(width=10, master=frm1, textvariable=cid_var)
        cid_ent.focus_set()
        cid_lbl.grid(row=0, column=0, padx=5)
        cid_ent.grid(row=0, column=1, padx=5)

        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(input_obj, event=None):
            cid = cid_var.get()
            if len(cid) == 0 or cid is None:
                messagebox.showerror(message="Error: Course ID cannot be empty.")
            elif cid not in engine.courses_id:
                messagebox.showerror(message="Error: There exist no course with that ID.")
                cid_ent.delete(-1, tk.END)
            else:
                if len(engine.marks) > 0:
                    existed = False
                    for mark in engine.marks:
                        if mark.get_cid() == cid:
                            messagebox.showerror(message="Error: You've already input mark for this course.")
                            existed = True
                            break
                    if not existed:
                        input_obj.input_course_mark(engine, cid, window)
                else:
                    input_obj.input_course_mark(engine, cid, window)
                sub.destroy()

        sub.bind("<Return>", lambda: ok(self))
        ok_btn = tk.Button(text="OK", master=frm2, command=lambda: ok(self))
        ok_btn.bind("<Return>", lambda: ok(self))
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)
