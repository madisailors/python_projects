
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
class Laptop(Electronic):
    device = "Macbook Pro"
    brand = "Apple"
    size = "15.6 inch"

    def information(self):
        msg = "\nCongrats, you won a {} {} {} with {} of memory!".format(self.size,self.brand,self.device,self.memory)
        return msg

#child class
class Tablet(Electronic):
    device = "HP Chromebook X2 11"
    brand = "Google"
    size = "12 inch"

    def information(self):
        msg = "\nCongrats, you won a {} {} {} with {} of memory!".format(self.size,self.brand,self.device,self.memory)
        return msg


if __name__ == "__main__":
    laptop = Laptop()
    print(laptop.information())

    tablet = Tablet()
    print(tablet.information())
    
    
    
