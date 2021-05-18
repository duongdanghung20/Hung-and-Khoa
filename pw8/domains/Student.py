class Student:
    # A constructor to create a Student object and store it to students[] list
    def __init__(self, engine, sid, name, dob, gpa=0):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = gpa
        engine.students.append(self)
        engine.students_id.append(self.__sid)

    # return the sid of self
    def get_sid(self):
        return self.__sid

    # return the name of self
    def get_name(self):
        return self.__name

    # return the dob of self
    def get_dob(self):
        return self.__dob

    # set the gpa of self
    def set_gpa(self, gpa):
        self.__gpa = gpa

    # return the gpa of self
    def get_gpa(self):
        return self.__gpa