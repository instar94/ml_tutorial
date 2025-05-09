import carrace as cr
import racing as rc

myCarGame=rc.CarRacing()

car01=cr.Car("car01","red",100)
car02=cr.Car("car02","blue",200)
car03=cr.Car("car03","gray",300)
car04=cr.Car("car04","white",400)
car05=cr.Car("car05","black",500)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.startRacing()