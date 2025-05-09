from abc import ABCMeta
from abc import abstractmethod

## 강제성을 띄게 하는 클래스에
# metaclass=ABCMeta
class AirPlane(metaclass=ABCMeta):

    #추상 클래스 표시
    @abstractmethod
    def flight(self):
        pass

    def forward(self):
        print("전진")

    def flight(self):
        print("후진")

class Airliner(AirPlane):
    def __init__(self,c):
        self.color=c

    def flight(self):
        print("시속 400km/h")

class filghterPlane(AirPlane):
    def __init__(self,c):
        self.color=c
    def flight(self):
        print("시속 800km/h")

al=Airliner("red")

