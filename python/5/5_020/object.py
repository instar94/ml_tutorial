class Robot:
    def __init__(self, color, height, weight):
        self.color=color
        self.height=height
        self.weight=weight

    def printInfo(self):
        print(f"self.color {self.color}")
        print(f"self.height {self.height}")
        print(f"self.weight {self.weight}")

rb1 =Robot("red",200,200)
rb2 =Robot("blue",230,500)
### 객체의 속성을 복사한 것이 아니라 객체의 주소값만 복사함
rb3 =rb1

rb1.printInfo()
rb2.printInfo()
rb3.printInfo()

rb1.color="green"
rb1.printInfo()
rb2.printInfo()
rb3.printInfo()
