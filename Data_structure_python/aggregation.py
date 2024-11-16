class CPU:
    def process(self):
        print("CPU is processing.")

class Computer:
    def __init__(self, cpu):
        self.cpu = cpu
    
    def run(self):
        self.cpu.process()
        print("Computer is running.")

# Aggregation in action
cpu = CPU()
computer = Computer(cpu)
computer.run()
