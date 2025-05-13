from time import sleep
class CarRacing:
    def __init__(self):
        self.cars=[]
        self.ranking=[]

    def startRacing(self):
        for i in range(10):
            print(f"racing : {i+1} 바퀴")
            for car in self.cars:
                car.distance += car.getDistanceForHour()
            sleep(1)
            self.printCurrentCarDistance()

    def printCurrentCarDistance(self):
        for car in self.cars:
            print(f"{car.name} : {car.distance} \t\t", end=" ")
        print()

    def addCar(self,c):
        self.cars.append(c)