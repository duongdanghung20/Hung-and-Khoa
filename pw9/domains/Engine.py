# import pickle
from input import *
from output import *
# import curses
from domains.BackgroundThread import BackgroundThread
# import zipfile
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import os


class Engine:
    # List students to store student objects
    students = []
    # List students_id to store students id, so that we can fetch id more easily afterwards
    students_id = []
    # List courses to store course objects
    courses = []
    # List courses_id to store courses id
    courses_id = []
    # List marks to store mark objects that are the marks of courses and students
    marks = []

    number_of_students = 0
    number_of_courses = 0
    list_of_numbers = []

    def __init__(self):
        self.__input = Input()
        self.__output = Output()

    def get_input(self):
        return self.__input

    def get_output(self):
        return self.__output

    # Define a method to create a background thread and run it
    def create_background_thread(self, mode, pickled_file, dumped_obj=None, loaded_array=None):
        bt = BackgroundThread(mode, pickled_file, dumped_obj, loaded_array)
        bt.start()
        bt.join()

    # Function to be called when only courses have been input, no students yet
    def cancel_in_phase_1(self, window, event=None):
        if self.number_of_courses != 0 and self.number_of_students == 0:
            messagebox.showinfo(message="Good bye!")
            window.destroy()
            with open('students.dat', 'wb') as new_zip2:
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.students))
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.courses))
                for course in self.courses:
                    self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                                  dumped_obj=course)
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.marks))
            exit()
        elif self.number_of_courses == 0 and self.number_of_students != 0:
            messagebox.showinfo(message="Good bye!")
            window.destroy()
            with open('students.dat', 'wb') as new_zip2:
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.students))
                for student in self.students:
                    self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                                  dumped_obj=student)
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.courses))
                self.create_background_thread(mode="dump", pickled_file=new_zip2,
                                              dumped_obj=len(self.marks))
            exit()
        elif self.number_of_courses == 0 and self.number_of_students == 0:
            messagebox.showinfo(message="Good bye!")
            window.destroy()
            exit()

    # Function to be called to input number of students, then input students information
    def engine_input_number_of_students_and_student_information(self, window, event=None):
        self.__input.input_number_of_students(self, window)
        for i in range(self.number_of_students):
            self.__input.input_student_information(self, window, (i + 1))
        if len(self.courses) > 0:
            window.destroy()

    # Function to be called to input number of courses, then input courses information
    def engine_input_number_of_courses_and_course_information(self, window, event=None):
        self.__input.input_number_of_courses(self, window)
        for i in range(self.number_of_courses):
            # print(f"Course #{i + 1}:")
            self.__input.input_course_information(self, window, (i + 1))
        if len(self.students) > 0:
            window.destroy()

    # Function to be called to input mark for a course
    def engine_input_mark_for_a_course(self, window, event=None):
        self.__input.input_mark(self, window)
        if len(self.marks) == len(self.students) * len(self.courses):
            window.destroy()

    # Cancel when
    def cancel_in_phase_2_and_3(self, window, event=None):
        messagebox.showinfo(message="Good bye!")
        window.destroy()
        with open('students.dat', 'wb') as new_zip:
            # pickle.dump(len(self.students), new_zip)
            self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.students))
            for student in self.students:
                # pickle.dump(student, new_zip)
                self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=student)
            # pickle.dump(len(self.courses), new_zip)
            self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.courses))
            for course in self.courses:
                # pickle.dump(course, new_zip)
                self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=course)
            # pickle.dump(len(self.marks), new_zip)
            self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.marks))
            for mark in self.marks:
                # pickle.dump(mark, new_zip)
                self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=mark)
        exit()

    #
    # def cancel_in_phase_3(self, window):
    #     messagebox.showinfo(message="Good bye!")
    #     window.destroy()
    #     with open('students.dat', 'wb') as new_zip:
    #         # pickle.dump(len(self.students), new_zip)
    #         self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.students))
    #         for student in self.students:
    #             # pickle.dump(student, new_zip)
    #             self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=student)
    #         # pickle.dump(len(self.courses), new_zip)
    #         self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.courses))
    #         for course in self.courses:
    #             # pickle.dump(course, new_zip)
    #             self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=course)
    #         # pickle.dump(len(self.marks), new_zip)
    #         self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=len(self.marks))
    #         for mark in self.marks:
    #             # pickle.dump(mark, new_zip)
    #             self.create_background_thread(mode="dump", pickled_file=new_zip, dumped_obj=mark)
    #     exit()

    # A method to start the program
    def start_engine(self):

        # print("Initializing engine...\n")
        # print("--- Student Manager ---\n")

        init_window = tk.Tk()
        init_window.title("Student Manager")
        init_window.resizable(height=False, width=False)
        init_window.eval('tk::PlaceWindow . center')
        init_lbl = tk.Label(text="Initializing engine: 0%", master=init_window)
        init_lbl.grid(row=0, column=0, padx=30, pady=10, sticky="s")
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='cyan2')
        bar = Progressbar(master=init_window, length=200, style='black.Horizontal.TProgressbar')
        bar['value'] = 0
        bar.grid(column=0, row=1, padx=30, pady=10, sticky="n")
        init_window.after(2000, lambda: init_window.destroy())

        def update_progressbar(value):
            bar['value'] = value

        def update_process(value):
            init_lbl['text'] = f"Initializing engine: {value}%"

        for i in range(100):
            init_window.after(20 * i, update_progressbar, i)
            init_window.after(20 * i, update_process, i + 1)
        init_window.mainloop()

        # Upon starting the program, check if students.dat exists
        if os.path.isfile('students.dat'):
            with open('students.dat', 'rb') as new_zip:
                # Check if there are data of students.
                #   If yes
                #       Load it into the Engine.
                #   Else
                #       Ask the user to input students data or exit.
                # self.number_of_students = pickle.load(new_zip)
                while True:
                    self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.list_of_numbers)
                    self.number_of_students = self.list_of_numbers[0]
                    if not self.number_of_students == 0:
                        for i in range(self.number_of_students):
                            # student = pickle.load(new_zip)
                            # self.students.append(student)
                            # self.students_id.append(student.get_sid())
                            self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.students)
                            self.students_id.append(self.students[i].get_sid())
                        break
                    else:
                        phase1_window = tk.Tk()
                        phase1_window.title("Student Manager")
                        phase1_window.resizable(height=False, width=False)
                        phase1_window.eval('tk::PlaceWindow . center')
                        logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase1_window)
                        logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                        btn1 = tk.Button(text="Input number of students and students information",
                                         command=lambda: self.engine_input_number_of_students_and_student_information(
                                             phase1_window), master=phase1_window)
                        btn2 = tk.Button(text="Cancel", command=lambda: self.cancel_in_phase_1(phase1_window),
                                         master=phase1_window)
                        btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                        btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                        phase1_window.mainloop()
                        break

                # Check if there are data of courses.
                #   If yes
                #       Load it into the Engine.
                #   Else
                #       Ask the user to input courses data or exit.
                # self.number_of_courses = pickle.load(new_zip)
                self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.list_of_numbers)
                self.number_of_courses = self.list_of_numbers[1]
                print(self.number_of_courses)
                if not self.number_of_courses == 0:
                    for i in range(self.number_of_courses):
                        self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.courses)
                        self.courses_id.append(self.courses[i].get_cid())
                    print(cid for cid in self.courses_id)
                else:
                    phase1_window = tk.Tk()
                    phase1_window.title("Student Manager")
                    phase1_window.resizable(height=False, width=False)
                    phase1_window.eval('tk::PlaceWindow . center')
                    logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase1_window)
                    logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                    btn1 = tk.Button(text="Input number of courses and courses information",
                                     command=lambda: self.engine_input_number_of_courses_and_course_information(
                                         phase1_window), master=phase1_window)
                    btn2 = tk.Button(text="Cancel", command=lambda: self.cancel_in_phase_1(phase1_window),
                                     master=phase1_window)
                    btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    phase1_window.mainloop()

                # Check if there are data of marks.
                #   If yes
                #       Load it into the Engine.
                #   Else
                #       Jump directly to choice 3 (Use the data from students.dat and skip the input students information and courses information part).
                # number_of_mark_objects = pickle.load(new_zip)
                self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.list_of_numbers)
                number_of_mark_objects = self.list_of_numbers[2]
                if not number_of_mark_objects == 0:
                    for i in range(number_of_mark_objects):
                        self.create_background_thread(mode="load", pickled_file=new_zip, loaded_array=self.marks)
                elif len(self.marks) < len(self.students) * len(self.courses):
                    phase2_window = tk.Tk()
                    phase2_window.title("Student Manager")
                    phase2_window.resizable(height=False, width=False)
                    phase2_window.eval('tk::PlaceWindow . center')
                    logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase2_window)
                    logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                    btn1 = tk.Button(text="Input mark for a course", master=phase2_window,
                                     command=lambda: self.engine_input_mark_for_a_course(phase2_window))
                    btn1.bind("<Return>", lambda: self.engine_input_mark_for_a_course(phase2_window))
                    btn2 = tk.Button(text="List students", master=phase2_window,
                                     command=lambda: self.get_output().list_students(self, phase2_window))
                    btn2.bind("<Return>", lambda: self.get_output().list_students(self, phase2_window))
                    btn3 = tk.Button(text="List courses", master=phase2_window,
                                     command=lambda: self.get_output().list_courses(self, phase2_window))
                    btn3.bind("<Return>", lambda: self.get_output().list_courses(self, phase2_window))
                    btn4 = tk.Button(text="Cancel", master=phase2_window,
                                     command=lambda: self.cancel_in_phase_2_and_3(phase2_window))
                    btn4.bind("<Return>", lambda: self.cancel_in_phase_2_and_3(phase2_window))
                    btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn4.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    phase2_window.mainloop()
                else:
                    # Jump directly to choice 4 (Use the data from students.dat and skip all the input parts)
                    phase3_window = tk.Tk()
                    phase3_window.title("Student Manager")
                    phase3_window.resizable(height=False, width=False)
                    phase3_window.eval('tk::PlaceWindow . center')
                    logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase3_window)
                    logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                    btn1 = tk.Button(text="List students", master=phase3_window,
                                     command=lambda: self.get_output().list_students(self, phase3_window))
                    btn1.bind("<Return>", lambda: self.get_output().list_students(self, phase3_window))
                    btn2 = tk.Button(text="List courses", master=phase3_window,
                                     command=lambda: self.get_output().list_courses(self, phase3_window))
                    btn2.bind("<Return>", lambda: self.get_output().list_courses(self, phase3_window))
                    btn3 = tk.Button(text="Show marks of a course", master=phase3_window,
                                     command=lambda: self.get_output().list_marks(self, phase3_window))
                    btn3.bind("<Return>", lambda: self.get_output().list_marks(self, phase3_window))
                    btn4 = tk.Button(text="Calculate GPA for a student", master=phase3_window,
                                     command=lambda: self.get_output().calculate_gpa(self, phase3_window))
                    btn4.bind("<Return>", lambda: self.get_output().calculate_gpa(self, phase3_window))
                    btn5 = tk.Button(text="Print a sorted student list by GPA descending", master=phase3_window,
                                     command=lambda: self.get_output().print_sorted_list(self, phase3_window))
                    btn5.bind("<Return>", lambda: self.get_output().print_sorted_list(self, phase3_window))
                    btn6 = tk.Button(text="Cancel", master=phase3_window,
                                     command=lambda: self.cancel_in_phase_2_and_3(phase3_window))
                    btn6.bind("<Return>", lambda: self.cancel_in_phase_2_and_3(phase3_window))
                    btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn4.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn5.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    btn6.grid(row=6, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                    phase3_window.mainloop()

        while True:
            if self.number_of_students == 0 or self.number_of_courses == 0:
                phase1_window = tk.Tk()
                phase1_window.title("Student Manager")
                phase1_window.resizable(height=False, width=False)
                phase1_window.eval('tk::PlaceWindow . center')
                logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase1_window)
                logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                btn1 = tk.Button(text="Input number of students and students information",
                                 command=lambda: self.engine_input_number_of_students_and_student_information(
                                     phase1_window),
                                 master=phase1_window)
                btn1.bind("<Return>", lambda: self.engine_input_number_of_students_and_student_information(
                    phase1_window))
                btn2 = tk.Button(text="Input number of courses and courses information",
                                 command=lambda: self.engine_input_number_of_courses_and_course_information(
                                     phase1_window),
                                 master=phase1_window)
                btn2.bind("<Return>", lambda: self.engine_input_number_of_courses_and_course_information(
                    phase1_window))
                btn3 = tk.Button(text="Cancel", master=phase1_window,
                                 command=lambda: self.cancel_in_phase_1(phase1_window))
                btn3.bind("<Return>", lambda: self.cancel_in_phase_1(phase1_window))
                btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                phase1_window.mainloop()

            elif len(self.marks) < len(self.students) * len(self.courses):
                phase2_window = tk.Tk()
                phase2_window.title("Student Manager")
                phase2_window.resizable(height=False, width=False)
                phase2_window.eval('tk::PlaceWindow . center')
                logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase2_window)
                logo_lbl.grid(row=0, column=0, padx=30, pady=30)
                btn1 = tk.Button(text="Input mark for a course", master=phase2_window,
                                 command=lambda: self.engine_input_mark_for_a_course(phase2_window))
                btn1.bind("<Return>", lambda: self.engine_input_mark_for_a_course(phase2_window))
                btn2 = tk.Button(text="List students", master=phase2_window,
                                 command=lambda: self.get_output().list_students(self, phase2_window))
                btn2.bind("<Return>", lambda: self.get_output().list_students(self, phase2_window))
                btn3 = tk.Button(text="List courses", master=phase2_window,
                                 command=lambda: self.get_output().list_courses(self, phase2_window))
                btn3.bind("<Return>", lambda: self.get_output().list_courses(self, phase2_window))
                btn4 = tk.Button(text="Cancel", master=phase2_window,
                                 command=lambda: self.cancel_in_phase_2_and_3(phase2_window))
                btn4.bind("<Return>", lambda: self.cancel_in_phase_2_and_3(phase2_window))
                btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                btn4.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
                phase2_window.mainloop()
            else:
                break
        phase3_window = tk.Tk()
        phase3_window.title("Student Manager")
        phase3_window.resizable(height=False, width=False)
        phase3_window.eval('tk::PlaceWindow . center')
        logo_lbl = tk.Label(text="Student Manager", font="Fixedsys 30 bold", master=phase3_window)
        logo_lbl.grid(row=0, column=0, padx=30, pady=30)
        btn1 = tk.Button(text="List students", master=phase3_window,
                         command=lambda: self.get_output().list_students(self, phase3_window))
        btn1.bind("<Return>", lambda: self.get_output().list_students(self, phase3_window))
        btn2 = tk.Button(text="List courses", master=phase3_window,
                         command=lambda: self.get_output().list_courses(self, phase3_window))
        btn2.bind("<Return>", lambda: self.get_output().list_courses(self, phase3_window))
        btn3 = tk.Button(text="Show marks of a course", master=phase3_window,
                         command=lambda: self.get_output().list_marks(self, phase3_window))
        btn3.bind("<Return>", lambda: self.get_output().list_marks(self, phase3_window))
        btn4 = tk.Button(text="Calculate GPA for a student", master=phase3_window,
                         command=lambda: self.get_output().calculate_gpa(self, phase3_window))
        btn4.bind("<Return>", lambda: self.get_output().calculate_gpa(self, phase3_window))
        btn5 = tk.Button(text="Print a sorted student list by GPA descending", master=phase3_window,
                         command=lambda: self.get_output().print_sorted_list(self, phase3_window))
        btn5.bind("<Return>", lambda: self.get_output().print_sorted_list(self, phase3_window))
        btn6 = tk.Button(text="Cancel", master=phase3_window,
                         command=lambda: self.cancel_in_phase_2_and_3(phase3_window))
        btn6.bind("<Return>", lambda: self.cancel_in_phase_2_and_3(phase3_window))
        btn1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        btn2.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        btn3.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        btn4.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        btn5.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        btn6.grid(row=6, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        phase3_window.mainloop()
