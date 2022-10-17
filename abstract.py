from abc import ABC, abstractmethod
class card(ABC):
    def receipt(self, amount):
        print("Amount: ",amount)
        @abstractmethod #function tells us to pass in an argument but not
        #what type of data it will be
        def payment(self, amount):
            pass #w/ abstract method you have to include 'pass' or
                    #you'll recieve an error

class cardPayment(card): #child class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit".format(amount))

    
ob = cardPayment()
ob.receipt("$1200")
ob.payment("$1200")


