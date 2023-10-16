import random
import time

class BasicAi:
    def __init__(self, agent=None):
        self.decisionTree = [-1] * 1444
        self.agentPositions = [0,1]

    def getDirection(self):
        self.direction = self.agentPositions[1] - self.agentPositions[0]
        return self.direction

    def rewardAgent(self, action):
        self.decisionTree[random.randint(0, len(self.decisionTree) - 1)] = action
    def punishAgent(self, action):
        self.decisionTree[random.randint(0, len(self.decisionTree) - 1)] = action * -1

    def createTarget(self, environment=[0, 20, 30, 70], agentPosition=0):
        self.target = environment[random.randint(0, len(environment) - 1)]
        while self.target == agentPosition:
            self.target = environment[random.randint(0, len(environment) - 1)]
        return self.target

    def simulation(self):
        self.environment = [0, 20, 30, 40, 60, 70]
        self.agentPositions[0] = self.environment[random.randint(0, len(self.environment) - 1)]
        self.target = self.createTarget(self.environment, self.agentPositions[0])
        self.revolutions = 0
        while True:
            self.action = self.decisionTree[random.randint(0, len(self.decisionTree) - 1)]
            if self.action == 1:
                self.agentPositions[1] = self.agentPositions[0] + 1
            if self.action == -1:
                self.agentPositions[1] = self.agentPositions[0] - 1
            self.revolutions += 1
            time.sleep(0.0001)
            if self.agentPositions[1] == self.target:
                self.rewardAgent(self.action)
                print(f'total moves it took to reach the target: {self.revolutions}, defficiency:{self.revolutions/len(self.decisionTree):.2f}')
                self.revolutions = 0
                self.target = self.createTarget(self.environment, self.agentPositions[1])
            if self.target < self.agentPositions[1]:
                if self.getDirection() == -1:
                    self.rewardAgent(self.action)
                else:
                    self.punishAgent(self.action)
            if self.target > self.agentPositions[1]:
                if self.getDirection() == 1:
                    self.rewardAgent(self.action)
                else:
                    self.punishAgent(self.action)
            self.agentPositions[0] = self.agentPositions[1]

agent1 = BasicAi()
agent1.simulation()