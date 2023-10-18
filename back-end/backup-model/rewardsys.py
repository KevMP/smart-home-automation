import random

class RewardSys:
    def __init__(self, agent=None):
        self.agent = agent
        self.direction = 0
        self.agentPosition = [1, 0]

    def setAgentPosition(self, agentPosition):
        self.agentPosition = agentPosition
    def getAgentPosition(self):
        return self.agentPosition

    def setAgentDirection(self):
        self.direction = self.agentPosition[1] - self.agentPosition[0]
    def getAgentDirection(self):
        return self.direction

    def setTarget(self, temperatureArray=[0, 2, 4]):
        self.newTarget = temperatureArray[random.randint(0, len(temperatureArray) - 1)]
        return self.newTarget
    def getTargetBasedOnDirection(self, temperatureArray=[0, 2, 4]):
        self.newTarget = self.setTarget(temperatureArray)
        match self.getAgentDirection():
            case -1:
                while self.newTarget <= self.getAgentPosition()[1]:
                    self.newTarget = self.setTarget(temperatureArray)
            case 0:
                while self.newTarget == self.getAgentPosition()[1]:
                    self.newTarget = self.setTarget(temperatureArray)
            case 1:
                while self.newTarget >= self.getAgentPosition()[1]:
                    self.newTarget = self.setTarget(temperatureArray)
        return self.newTarget

# obj = RewardSys()
# print(obj.getTargetBasedOnDirection())