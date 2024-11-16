#An implementation of the Laptop class is given. Implement a method in
 #the Laptop class called dispiay_private_attrs( ) that displays the names of all
 #private attributes of the instance. 

class Laptop:
    def __init__(self, brand, model,code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)

    def display_non_private_attrs(self):
        for attr in self.__dict__:
            # Check for public and protected attributes
            if not attr.startswith(f'_{self.__class__.__name__}__'):
                print(f"Non-private attribute: {attr}")

Acer = Laptop("Acer", "Predator", "AC-111", 5490, 0.2)
Acer.display_non_private_attrs()
Acer.display_private_attrs()