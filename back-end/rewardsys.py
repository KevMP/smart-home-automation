import random

class RewardSys:
    def __init__(self, agent):
        self.agent = agent

    def setTarget(self, temperatureArray=[0, 2, 4], agentPosition=[2, 3]):
        self.agentDirection = agentPosition[1] - agentPosition[0]