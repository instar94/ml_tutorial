class NormalTV:
    def __init__(self,i=32, c="bk", r="fhd"):
        self.inch=i
        self.color=c
        self.resol=r
        self.smartTV="off"
        self.aiTV="off"

    def turnON(self):
        print("TV 켜짐")

    def turnOff(self):
        print("TV 꺼짐")

    def printTVInfo(self):
        print(f"inch={self.inch}")
        print(f"color={self.color}")
        print(f"resol={self.resol}")
        print(f"smartTV={self.smartTV}")
        print(f"aiTV={self.aiTV}")

class Tv4K(NormalTV):
    def __init__(self,i,c,r="4K"):
        super().__init__(i,c,r)

    def setSmartTv(self,s):
        self.smartTV=s


class Tv7K(NormalTV):
    def __init__(self, i, c, r="8K"):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTV = s

    def setAiTv(self, a):
        self.aiTV = a