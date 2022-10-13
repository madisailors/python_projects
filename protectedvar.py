
class Protect:
    def __init__(self):
        self.__private1 = 10
        self._protect1 = 5

    def getPrivate(self):
        print(self.__private1) #private double under score


    def getProtect(self):
        print(self._protect1) #protected single underscore

   


ob = Protect()
ob.getPrivate()
ob.getProtect()
