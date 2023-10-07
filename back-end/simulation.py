import random

class Simulation():
    def chooseDirection(self, command):
        if command == True:
            return 1
        else:
            return -1
            
    def environment(self, command):
        self.ac_status = command

        for self.generation in range(100):
            pass

        return self.reward