import random

class Simulation():
    def chooseDirection(self, command):
        if command == True:
            return 1
        else:
            return -1
            
    def environment(self, agent):
        self.ac_status = command
        self.reward = 0
        self.temperature_array = [0, 20, 40, 70, 75, 80, 81, 100]

        self.current_temperature = self.temperature_array[random.randint(0, 8)]
        self.target_temperature = self.temperature_array[random.randint(0, 8)]

        for self.generation in range(100):
            if self.current_temperature == self.target_temperature:
                self.target_temperature = self.temperature_array[random.randint(0, 8)]
            else:
                pass

        return self.reward