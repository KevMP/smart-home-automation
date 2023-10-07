import tensorflow as tf
import random

class Simulation():
    
    def __init__(self, agent):
        self.agent = agent

    def run(self):
        return self.environment()

    def chooseDirection(self, command):
        if command == 0:
            return 1
        else:
            return -1
    
    # current temperature, occupancy, humidity -> target temperature
    # target temperature, current temperature, occupancy, humidity -> most efficient


    # toggle, use AI or not
    
    # energy efficieny: the model will choose the most efficient path to reach the target temperature
    # adaptive learning: learns the habits of residents, so temp at specific times
    # occupancy-based control:
    

    def getCommand(self, model, array):
        predictions = model.predict([array])
        prediction = tf.argmax(predictions, axis=1).numpy()
        prediction = prediction[0]
        return prediction

    def environment(self):
        self.agent_reward = 0
        self.temperature_array = [0, 20, 40, 70, 75, 80, 81, 100]

        self.current_temperature = self.temperature_array[random.randint(0, 7)]
        self.target_temperature = self.temperature_array[random.randint(0, 7)]
        self.agent_input = [self.current_temperature, self.target_temperature]

        for self.generation in range(100):
            self.command = self.getCommand(self.agent, self.agent_input)
            if self.current_temperature == self.target_temperature:
                self.target_temperature = self.temperature_array[random.randint(0, 7)]
                self.agent_reward += 2
                self.agent_input = [self.current_temperature, self.target_temperature]
            else:
                self.current_temperature += self.chooseDirection(self.command)
                self.agent_reward -= 1
                self.agent_input = [self.current_temperature, self.target_temperature]

        return self.agent_reward