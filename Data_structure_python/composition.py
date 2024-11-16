class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        super().__init__(self, engine)
        self.engine = engine

    def drive(self):
        #.start()
        print("Car is driving.")

# Composition in action
engine = Engine()
car = Car(engine)
car.drive()
car.start()




#Composition means that a class contains other classes as part of its data. 
# It allows code reuse without inheritance.
#