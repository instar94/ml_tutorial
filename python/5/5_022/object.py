class NormalCar:
    def drive(self):
        print("[NormalCar] drive() called")
    def back(self):
        print("[NormalCar] back() called")


### 상속받는 클래스를 ()안에 넣음
class Turbocar(NormalCar):
    def turbo(self):
        print("[Turbocar] turbo() called")

myTurboCar =Turbocar()
myTurboCar.drive()
myTurboCar.back()
myTurboCar.turbo()
