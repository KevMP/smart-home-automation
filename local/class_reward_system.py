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
    
    """
    **********************************************************************************
    Overwrites the previous reward value with the current one and writes the current
    reward value with the value that is passed in.
            PREVIOUS REWARD = CURRENT
            CURRENT REWARD = NEW VALUE
    **********************************************************************************
    """
    def overwriteReward(self, value:float):
        self.previous_reward = self.current_reward
        self.current_reward = value