import random

class RewardSys:
    def __init__(self, agent=None):
        self.agent = agent
        self.direction = [1,0]

    def setDirection(self, agentPosition=[2, 3]):
        self.direction = agentPosition[1] - agentPosition[0]
    def getDirection(self):
        return self.direction[1] - self.direction[0]

    def setTarget(self, temperatureArray=[0, 2, 4]):
        self.newTarget = temperatureArray[random.randint(0, len(temperatureArray) - 1)]
        return self.newTarget
    def getTargetBasedOnDirection(self, temperatureArray=[0, 2, 4], agentPosition=[1, 0]):
        self.agentDirection = self.getDirection()
        self.newTarget = self.setTarget(temperatureArray)
        match self.agentDirection:
            case -1:
                while self.newTarget <= agentPosition[1]:
                    self.newTarget = self.setTarget(temperatureArray)
            case 0:
                while self.newTarget == agentPosition[1]:
                    self.newTarget = self.setTarget(temperatureArray)
            case 1:
                while self.newTarget >= agentPosition[1]:
                    self.newTarget = self.setTarget(temperatureArray)
        return self.newTarget