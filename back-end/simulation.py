import random

class Simulation():
    def chooseDirection(self, command):
        if command == True:
            return 1
        else:
            return -1
            
    def environment(self, command):
        self.ac_status = command
        self.temperatuer_array = [0, 20, 40, 70, 75, 80, 81, 100]
        for self.generation in range(100):
            pass

        return self.reward