import random

class RewardSys:
    def __init__(self, agent=None):
        self.agent = agent
        self.direction = [0,1]

    def setDirection(self, agentPosition=[2, 3]):
        self.direction = agentPosition[1] - agentPosition[0]
    
    def getDirection(self):
        return self.direction

    def setTarget(self, temperatureArray=[0, 2, 4], agentPosition=[2, 3]):
        self.agentDirection = agentPosition[1] - agentPosition[0]