import random

class Simulation():
    def returnCommand(self, command):
        match command:
            case 0:
                Simulation().aircondtionerOn()
                return True
            case 1:
                Simulation().aircondtionerOff()
                return False
            
    def environment(self, command):
        self.ac_status = self.returnCommand(command)

        for self.generation in range(100):
            pass

        return self.reward