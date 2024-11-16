class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

# Method overriding in action
animal = Animal()
dog = Dog()
print(animal.sound())  # Output: Some sound
print(dog.sound())     # Output: Woof!
