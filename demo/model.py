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

ai = Model()