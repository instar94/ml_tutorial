class Car:
    def __init__(self,col,len):
        self.color=col
        self.length=len

    def doStop(self):
        print("Stop")

    def soStart(self):
        print("Start")

    def printCarInfo(self):
        print(f"self.color : {self.color}")
        print(f"self.length : {self.length}")

car1 = Car("Red",200)
car2 = Car("Blue",500)

car1.printCarInfo()
car2.printCarInfo()