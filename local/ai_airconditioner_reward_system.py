from class_reward_system import Reward

class AirconditionerReward(Reward):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.real_temperature = 0.0
    
    def getTemperatureFromDatabase():
        pass
    def getHumidityFromDatabase():
        pass

    def calculateRealTemperature():
        pass