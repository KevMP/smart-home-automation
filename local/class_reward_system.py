class Reward:
    def __init__(self, model):
        self.current_reward = 0
        self.previous_reward = 0
        self.model = model

    