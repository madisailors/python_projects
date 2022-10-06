
#parent class
class Electronic:
    device = "Unknown"
    brand = "Unknown"
    size = " "
    memory = "64 Gygabites"

    def information(self): 
        msg = "\nDevice Type: {}\nBrand: {}\nSize: {}\nMemory: {}".format(self.device,self.brand,self.size,self.memory)
        return msg

#child class
def Laptop(Electronic):
    device = "Macbook Pro"
    brand = "Apple"
    size = "15.6 inch"

#child class
def Tablet(Electronic):
    device = "HP Chromebook X2 11"
    brand = "Google"
    size = "11 inch"


if __name__ == "__main__":
    laptop = Laptop()
    print(laptop.information())

    tablet = Tablet()
    print(tablet.information())
    
    
    
