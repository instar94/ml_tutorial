class Robot:
    def __init__(self,c,h,w):
        self.color=c
        self.height=h
        self.weight=w

    def fire(self):
        print("Fire in the hole")

    def printRobotInfo(self):
        print(f"self.color : {self.color}")
        print(f"self.height : {self.height}")
        print(f"self.weight : {self.weight}")

class NewRobot(Robot):
    def __init__(self,c,h,w):
        super().__init__(c,h,w)

    ### fire 함수 오버 라이딩
    def fire(self):
        print("You got the fire")

myrobot=NewRobot("Red",200,300)
myrobot.fire()