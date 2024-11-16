class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Instantiation
dog1 = Dog("Buddy")
dog1.bark()
