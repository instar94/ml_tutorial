import random


class Car :
    def __init__(self,n="fire car",c="red",s=200):
        self.name=n
        self.color=c
        self.speed=s
        self.distance=0

    def printCarInfo(self):
        print(f"name {self.name}")
        print(f"color {self.color}")
        print(f"speed {self.speed}")

    def controlSpeed(self):
        return random.randint(0,self.speed)


    def getDistanceForHour(self):
        return self.controlSpeed()*1



