class Printer:
    def print_document(self):
        print("Printing document...")

class Office:
    def __init__(self, printer):
        self.printer = printer

    def print_file(self):
        self.printer.print_document()

# Delegation in action
printer = Printer()
office = Office(printer)
office.print_file()


#Delegation involves having one class make use of another class’s methods. Instead of inheritance, an 
# object delegates behavior to another class.
#