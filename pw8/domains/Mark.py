class Mark:
    # A constructor to create a Mark object and store it to marks[] list
    def __init__(self, engine, sid, cid, value):
        self.__sid = sid
        self.__cid = cid
        self.__value = value
        engine.marks.append(self)

    def get_sid(self):
        return self.__sid

    def get_cid(self):
        return self.__cid

    def get_value(self):
        return self.__value
