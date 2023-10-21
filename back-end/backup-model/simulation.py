import tensorflow as tf
import random

class Simulation:
    def __init__(self, agent):
        self.agent = agent

    def run(self):
        total_reward = 0
        temperature_array = [0, 20, 40, 70, 75, 80, 81, 100]

        current_temperature = random.choice(temperature_array)
        target_temperature = random.choice(temperature_array)
        
        for _ in range(100):
            state = [current_temperature, target_temperature]
            action = self.agent.act(state)
            next_temperature = current_temperature + (1 if action == 0 else -1)
            next_state = [next_temperature, target_temperature]
            
            # Reward logic
            if next_temperature == target_temperature:
                reward = 2
                target_temperature = random.choice(temperature_array)
            else:
                reward = -abs(next_temperature - target_temperature) / 100

            self.agent.remember(state, action, reward, next_state)
            self.agent.train_batch()

            current_temperature = next_temperature
            total_reward += reward
            
        return total_reward