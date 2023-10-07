import tensorflow as tf
import random

class Simulation():
    def chooseDirection(self, command):
        if command == True:
            return 1
        else:
            return -1
            
    def environment(self, agent):
        self.reward = 0
        self.temperature_array = [0, 20, 40, 70, 75, 80, 81, 100]

        self.current_temperature = self.temperature_array[random.randint(0, 8)]
        self.target_temperature = self.temperature_array[random.randint(0, 8)]

        for self.generation in range(100):
            self.command = self.getCommand(agent)
            ## if the ai/agent reaches the target temperature,
            ## we choose a new target temperature, and reward our
            ## agent.
            if self.current_temperature == self.target_temperature:
                self.target_temperature = self.temperature_array[random.randint(0, 8)]
                self.reward += 8
            else:
                self.current_temperature += self.chooseDirection(self.command)
                self.reward -= 1
        
        return self.reward