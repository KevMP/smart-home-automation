import random

class Simulation():
    def getAcStatus(self, command):
        match command:
            case 0:
                Simulation().aircondtionerOn()
                return True
            case 1:
                Simulation().aircondtionerOff()
                return False
            
    def environment(self, command):
        pass