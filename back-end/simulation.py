## Inputs for the ai:
## 1.
## 2.
## 3.
## 4.
## 5.

class Simulation():
    def getReward(self):
        pass

    def getTemperature(self):
        pass

    def getHumiditiy(self):
        pass

    def setTemperature(self):
        pass

    def acOn(self):
        pass

    def acOff(self):
        pass

    def parseCommand(self, command):
        match command:
            case 0:
                Simulation().acOn()
                return 'Aircondtioner Off'
            case 1:
                Simulation().acOff()
                return 'Airconditioner On'