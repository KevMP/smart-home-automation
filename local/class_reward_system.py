class Reward:
    def __init__(self, model):
        self.current_reward = 0
        self.previous_reward = 0
        self.model = model

    def rewardOrPunishModel(self):
        if self.current_reward > self.previous_reward:
            return True
        else:
            return False