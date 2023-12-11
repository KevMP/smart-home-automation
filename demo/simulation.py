from model import Model
import time

class Simulation:
    def __init__(self):
        self.current_temperature = 0
        self.previous_temperature = self.current_temperature
        self.preferred_temperatures = [70, 71]
    
    def getCurrentTemperature(self):
        return self.current_temperature

    def setCurrentTemperature(self, action: int):
        self.previous_temperature = self.current_temperature
        if action == 1:
            self.current_temperature += 1
        elif action == -1:
            self.current_temperature -= 1
    
    def getDirection(self):
        return self.current_temperature - self.previous_temperature
    
    def isAiGettingCloserToTarget(self):
        if self.current_temperature > self.preferred_temperatures[0] and self.current_temperature < self.preferred_temperatures[1]:
            if self.getDirection() == 0:
                return 1
            else:
                return -1
        elif self.current_temperature < self.preferred_temperatures[0]:
            if self.getDirection() == 1:
                return 1
            else:
                return -1
        elif self.current_temperature > self.preferred_temperatures[1]:
            if self.getDirection() == -1:
                return 1
            else:
                return -1
    
def main():
    ai = Model()
    environment = Simulation()
    CYCLE_SPEED = 1 / 100

    while True:
        time.sleep(CYCLE_SPEED)
        print(environment.current_temperature, environment.getDirection(), ai.action_matrix, ai.reward_index, ai.reward_choices)
        action = ai.getAction()
        environment.setCurrentTemperature(action)
        ai.reward(environment.isAiGettingCloserToTarget())

main()