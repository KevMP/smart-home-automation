class Simulation():

    def aircondtionerOn(self):
        pass

    def aircondtionerOff(self):
        pass

    def parseCommand(self, command):
        match command:
            case 0:
                Simulation().aircondtionerOn()
                return 'Aircondtioner Off'
            case 1:
                Simulation().aircondtionerOff()
                return 'Airconditioner On'
            
    def environment(self, command):
        self.reward = 0

        ## if the ac is getting closer to our
        ## expected temperature
        self.reward = self.reward + 5

        ## if the ac is not getting further from our
        ## expected temperature
        self.reward = self.reward - 5 ## we could also choose not to punish
                                      ## the model whatsoever.

        ## what we want to get back is the
        ## value of our reward, if it is
        ## greater than the previous value,
        ## we update the model. If not, we
        ## don't update it whatsoever.

        return self.reward