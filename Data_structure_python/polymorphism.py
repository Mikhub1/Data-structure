class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.sound())

# Polymorphism in action
animal_sound(Dog())  # Output: Woof!
animal_sound(Cat())  # Output: Meow!
