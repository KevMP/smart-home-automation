## model.py

import random

class Model:
    def __init__(self):
        self.action_matrix = [-1, 0, 1]
        self.reward_choices = [-1, 0, 1]
        self.reward_index = 0
    
    def reward(self, reward_value: int):
        # The reward mechanism updates the action matrix based on the received reward.
        # If the reward is -1, the action matrix is rotated to the next reward choice.
        if reward_value == -1:
            if self.reward_index == 2:
                self.reward_index = 0
            else:
                self.reward_index += 1
        # Select a random action from the updated action matrix.
        self.action_matrix[random.choice([0, 1, 2])] = self.reward_choices[self.reward_index]

    def getAction(self):
        return random.choice(self.action_matrix)