class Simulation():
    def getReward(self):
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
            
    def environment(self, command):

        ## what we want to get back is the
        ## value of our reward, if it is
        ## greater than the previous value,
        ## we update the model. If not, we
        ## don't update it whatsoever.

        self.reward = self.getReward()
        return self.reward