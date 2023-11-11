from database import Database
from controller import Controller
import time
import random

class AiModel:
    def __init__(self):
        self.profile = 0
        self.min = 90
        self.max = 120
        self.actionMatrix = [0, 0, 0]

    def setProfile(self):
        self.profile = Database().getCurrentProfile()
        self.min = Database().getMinimumPreferredTemperature(self.profile)
        self.max = Database().getMaximumPreferredTemperature(self.profile)

    def learnDirection(self, state: float):
        if state < self.min:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 1
        elif state > self.max:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = -1
        else:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 0

if __name__ == "__main__":
    model = AiModel()
    model.setProfile()
    currentTemperature = Controller().getTargetTemperature()
    
    while True:
        time.sleep(1)
        print(model.actionMatrix)
        print(model.min)
        print(model.max)
        print(currentTemperature)
        action = random.choice(model.actionMatrix)
        if action == 1:
            Controller().setTargetTemperature(currentTemperature + 1)
        elif action == -1:
            Controller().setTargetTemperature(currentTemperature - 1)
        model.learnDirection(currentTemperature)
        currentTemperature = Controller().getTargetTemperature()