import random

class Model:
    def __init__(self):
        self.action_matrix = [-1, 0, 1]
        self.reward_choices = [-1, 0, 1]
        self.reward_index = 0
    
    def reward(self, reward_value: int):
        if reward_value == -1:
            if self.reward_index == 2:
                self.reward_index = 0
            else:
                self.reward_index += 1
            self.action_matrix[random.randint(0, 2)] = self.reward_choices[self.reward_index]
        elif reward_value == 1:
            self.action_matrix[random.randint(0, 2)] = self.reward_choices[self.reward_index]
    
    def getAction(self):
        return random.choice(self.action_matrix)

'''
example usage;

ai = Model()
while true:
    action = ai.getAction()
    if action did bad thing:
        ai.reward(-1)
    if action did good thing:
        ai.reward(1)
'''