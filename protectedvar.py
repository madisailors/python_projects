
class Protect:
    def __init__(self):
        self.__private1 = 10

    def getPrivate(self):
        print(self.__private1)

    def setPrivate(self, private):
        self.__private1 = private


ob = Protect()
ob.getPrivate()
ob.setPrivate(23)
ob.getPrivate()
