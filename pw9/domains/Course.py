class Course:
    # A constructor to create a Student object and store it to courses[] list
    def __init__(self, engine, cid, name, credit):
        self.__cid = cid
        self.__name = name
        self.__credit = credit
        engine.courses.append(self)
        engine.courses_id.append(self.__cid)

    # return the cid of self
    def get_cid(self):
        return self.__cid

    # return the name of self
    def get_name(self):
        return self.__name

    # return the number of credits of self
    def get_credit(self):
        return self.__credit
