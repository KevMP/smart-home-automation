import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential

# Hyperparameters
BATCH_SIZE = 32
GAMMA = 0.99
EPSILON = 0.1
LEARNING_RATE = 0.001
MODEL_PATH = 'temperature_agent_model.h5'

class Agent:
    def __init__(self):
        self.model = self.create_model()
        self.memory = []

    def create_model(self):
        model = Sequential([
            tf.keras.layers.Dense(2, activation='relu', input_shape=(2, )),
            tf.keras.layers.Dense(3, activation='relu'),
            tf.keras.layers.Dense(2)
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(LEARNING_RATE), loss='mse')
        return model

    def act(self, state):
        if random.random() < EPSILON:
            return random.randint(0, 1)
        q_values = self.model.predict(np.array([state]))
        return np.argmax(q_values[0])

    def remember(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))
        
    def train_batch(self):
        if len(self.memory) < BATCH_SIZE:
            return
        
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, next_state in batch:
            q_update = reward
            if next_state is not None:
                q_update = (reward + GAMMA * np.amax(self.model.predict(np.array([next_state]))[0]))
            q_values = self.model.predict(np.array([state]))
            q_values[0][action] = q_update
            self.model.train_on_batch(np.array([state]), q_values)

    def save_model(self):
        self.model.save(MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")

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

# agent = Agent()
# sim = Simulation(agent)

# for episode in range(100):
#     reward = sim.run()
#     print(f"Episode: {episode + 1}, Reward: {reward}")
#     agent.save_model()
