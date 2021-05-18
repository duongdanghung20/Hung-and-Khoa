# import main
# import curses
import numpy as np
import math
import tkinter as tk
from tkinter import messagebox


class Output:
    # List all the courses
    def list_courses(self, engine, window):
        # print("Courses existing:")
        # for course in engine.courses:
        #     print("\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
        sub = tk.Toplevel(master=window)
        sub.title(f"Input mark")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        lbl1 = tk.Label(text="Course existing:", master=sub)
        lbl1.grid(row=0, column=0)
        for course in engine.courses:
            course_lbl = tk.Label(
                text="[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()),
                master=sub)
            course_lbl.grid(row=(engine.courses.index(course) + 1), column=0)

    # List all the students
    def list_students(self, engine, window):
        # print("Students in class:")
        # for student in engine.students:
        #     print("\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
        sub = tk.Toplevel(master=window)
        sub.title("Input mark")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        lbl1 = tk.Label(text="Students in class:", master=sub)
        lbl1.grid(row=0, column=0)
        for student in engine.students:
            student_lbl = tk.Label(
                text="[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()), master=sub)
            student_lbl.grid(row=(engine.students.index(student) + 1), column=0)

    # List all students with their marks for a specific course
    def list_course_marks(self, engine, cid, window):
        # for mark in engine.marks:
        #     if mark.get_cid() == cid:
        #         sid = mark.get_sid()
        #         for student in engine.students:
        #             if student.get_sid() == sid:
        #                 print(f"\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(),
        #                                                                  mark.get_value()))
        sub = tk.Toplevel(master=window)
        sub.title(f"Marks of course {cid}")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        lbl1 = tk.Label(text=f"Marks of course {cid}:", master=sub)
        lbl1.grid(row=0, column=0)
        for mark in engine.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in engine.students:
                    if student.get_sid() == sid:
                        mark_lbl = tk.Label(
                            text=f"[%s]    %-20s%s" % (student.get_sid(), student.get_name(), mark.get_value()),
                            master=sub)
                        mark_lbl.grid(row=(engine.students.index(student) + 1), column=0)

    # Ask the user for the course ID whose mark should be listed, then invoke the list_course_marks() function
    def list_marks(self, engine, window):
        # while True:
        #     cid = input("- Enter the course ID you want to list marks: ")
        #     if len(cid) == 0 or cid is None:
        #         print("Error: Course ID cannot be empty")
        #     else:
        #         break
        # if cid in engine.courses_id:
        #     self.list_course_marks(engine, cid)
        # else:
        #     print("Error: There exist no course with that ID.")
        #     return -1
        sub = tk.Toplevel(master=window)
        sub.title(f"List marks")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        cid_lbl = tk.Label(text=f"Enter the course ID you want to list marks:", master=frm1)
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
                messagebox.showinfo(message="Error: Course ID cannot be empty.")
            elif cid not in engine.courses_id:
                messagebox.showinfo(message="Error: There exist no course with that ID.")
                cid_ent.delete(-1, tk.END)
            else:
                input_obj.list_course_marks(engine, cid, window)
                sub.destroy()

        sub.bind("<Return>", lambda: ok(self))
        ok_btn = tk.Button(text="OK", master=frm2, command=lambda: ok(self))
        ok_btn.bind("<Return>", lambda: ok(self))
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)

    # A function to calculate average GPA for a specific student
    def calculate_student_gpa(self, engine, sid):
        mark_values = np.array([])
        course_credits = np.array([])
        for mark in engine.marks:
            if mark.get_sid() == sid:
                for course in engine.courses:
                    if course.get_cid() == mark.get_cid():
                        mark_values = np.append(mark_values, mark.get_value())
                        course_credits = np.append(course_credits, course.get_credit())
        gpa = np.dot(mark_values, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0
        # Add the value of attribute gpa for the student with ID specified
        for student in engine.students:
            if student.get_sid() == sid:
                student.set_gpa(rounded_gpa)

    # Ask the user for the student ID whose GPA should be calculated, then invoke the calculate_student_gpa() function
    def calculate_gpa(self, engine, window):
        # while True:
        #     sid = input("- Enter student ID that requires GPA calculating: ")
        #     if len(sid) == 0 or sid is None:
        #         print("Error: Student ID cannot be empty")
        #     elif sid not in engine.students_id:
        #         print("Error: Student does not exist")
        #     else:
        #         break
        # for student in engine.students:
        #     if student.get_sid() == sid:
        #         self.calculate_student_gpa(engine, sid)
        #         print("\n\t\t%s's GPA:    %-20.1f" % (student.get_name(), student.get_gpa()))
        #         break
        sub = tk.Toplevel(master=window)
        sub.title(f"Calculate GPA")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        frm1 = tk.Frame(master=sub)
        frm1.grid(row=0, column=0, padx=10, pady=10)
        sid_lbl = tk.Label(text=f"Enter student ID that requires GPA calculating:", master=frm1)
        sid_var = tk.StringVar()
        sid_ent = tk.Entry(width=10, master=frm1, textvariable=sid_var)
        sid_ent.focus_set()
        sid_lbl.grid(row=0, column=0, padx=5)
        sid_ent.grid(row=0, column=1, padx=5)

        frm2 = tk.Frame(master=sub)
        frm2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        def ok(input_obj, event=None):
            sid = sid_var.get()
            if len(sid) == 0 or sid is None:
                messagebox.showinfo(message="Error: Student ID cannot be empty.")
            elif sid not in engine.students_id:
                messagebox.showinfo(message="Error: There exist no student with that ID.")
                sid_ent.delete(-1, tk.END)
            else:
                gpa = 0
                name = ""
                input_obj.calculate_student_gpa(engine, sid)
                for student in engine.students:
                    if student.get_sid() == sid:
                        gpa = student.get_gpa()
                        name = student.get_name()
                messagebox.showinfo(message=f"GPA of {name} is {gpa}")
                sub.destroy()

        sub.bind("<Return>", ok)
        ok_btn = tk.Button(text="OK", master=frm2, command=lambda: ok(self))
        ok_btn.bind("<Return>", lambda: ok(self))
        ok_btn.pack(ipadx=5)
        sub.wait_window(sub)

    # A function to print a sorted student list by GPA descending
    def print_sorted_list(self, engine, window):
        # Automatically calculate GPA for all students before printing a sorted list
        new_student_list = []
        for student in engine.students:
            self.calculate_student_gpa(engine, student.get_sid())
            new_student = (student.get_sid(), student.get_name(), student.get_gpa())
            new_student_list.append(new_student)
        # Make a copy of the student list using type numpy.array
        dtype = [('sid', 'S10'), ('name', 'S30'), ('gpa', float)]
        np_student_list = np.array(new_student_list, dtype=dtype)
        # Sort the student list in ascending order and then reverse it
        sorted_student_list = np.sort(np_student_list, order='gpa')[::-1]
        # Make a copy of the sorted student list with attributes type bytes converted back to type str
        new_sorted_student_list = []
        for student in sorted_student_list:
            decoded_student = (student[0].decode(), student[1].decode(), student[2])
            new_sorted_student_list.append(decoded_student)
        # Print the final sorted student list
        sub = tk.Toplevel(master=window)
        sub.title("Sorted Student List")
        sub.resizable(height=False, width=False)
        window.eval(f'tk::PlaceWindow {str(sub)} center')
        lbl1 = tk.Label(text="Student list (sorted by GPA in descending order):", master=sub)
        lbl1.grid(row=0, column=0)
        for student in new_sorted_student_list:
            # print("\t\t[%s]    %-20sGPA: %s\n" % (student[0], student[1], student[2]))
            student_lbl = tk.Label(text="[%s]    %-20sGPA: %s" % (student[0], student[1], student[2]), master=sub)
            student_lbl.grid(row=(new_sorted_student_list.index(student) + 1), column=0)
