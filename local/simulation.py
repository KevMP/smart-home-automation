from database import Database
from controller import Controller
import random

class AiModel:
    def __init__(self):
        self.profile = 0
        self.min = 70
        self.max = 75
        self.actionMatrix = [0, 0, 0]

    def setProfile(self):
        self.profile = Database().getCurrentProfile()
        self.min = Database().getMinimumPreferredTemperature(self.profile)
        self.max = Database().getMaximumPreferredTemperature(self.profile)

    def learnDirection(self, state):
        if state < self.min:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 1
        elif state > self.max:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = -1
        else:
            self.actionMatrix[random.randint(0, len(self.actionMatrix) - 1)] = 0

if __name__ == "__main__":
    model = AiModel()
    model.setProfile()
    
    while True:
        action = random.choice(model.actionMatrix)
        if action == 1:
            Controller().increaseTemperature()
        elif action == -1:
            Controller().decreaseTemperature()