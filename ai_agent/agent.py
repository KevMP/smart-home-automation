import random
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np
import os
import platform
import logging

logging.basicConfig(level=logging.INFO)

feature_order = ['temperature', 'humidity', 'occupancy', 'ac_status', 'target_temperature']

def extract_features(data_dict):
    return np.array([data_dict[key] for key in feature_order])

class DQNAgent:
    def __init__(self, state_size = 5, action_size = 3, learning_rate=0.01, gamma=0.09, epsilon=1, epsilon_min=0.01, epsilon_decay=0.995):
        logging.info("Initializing agent...")
        self.state_size = state_size # temperature, humidity, status
        self.action_size = action_size
        self.learning_rate = learning_rate

        self.memory = []  # store (state, action, reward, next_state, done)
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.load()

    def _build_q_network(self, neurons=64, activation='relu'):
        model = Sequential()
        model.add(Dense(units=neurons, activation=activation, input_shape=(self.state_size,)))
        model.add(Dense(self.action_size, activation='linear'))

        if platform.system() == 'Darwin':
            model.compile(loss='mse', optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=self.learning_rate))
        else:
            model.compile(loss='mse', optimizer=Adam(learning_rater=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def choose_action(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        q_values = self.q_network.predict(state)
        return np.argmax(q_values[0])

    def replay(self, batch_size=32):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)
        for state_dict, action, reward, next_state_dict, done in minibatch:

            state = extract_features(state_dict).reshape(1, -1)
            next_state = extract_features(next_state_dict).reshape(1, -1)

            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.q_network.predict(next_state)[0]))

            target_f = self.q_network.predict(state)
            target_f[0][action] = target
            self.q_network.fit(state, target_f, epochs=1, verbose=0)

            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

    def train_agent_fixed(self, environment, episodes=10, max_steps=10, save_interval=10):
        for episode in range(episodes):
            state_dict = environment.get_status()
            state = extract_features(state_dict).reshape(1, -1)
            total_reward = 0

            for step in range(max_steps):
                action = self.choose_action(state)
                next_state_dict, reward, done = environment.step(action)
                next_state = extract_features(next_state_dict).reshape(1, -1)
                self.remember(state_dict, action, reward, next_state_dict, done)

                self.replay()

                state = next_state
                total_reward += reward

                if done:
                    break

            if episode % save_interval == 0:
                self.save()

        return {
            'total_reward': total_reward,
            'episodes': episode + 1,
            'last_state': state.tolist()
        }

    def save(self, directory="ai_agent/saved_model"):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.q_network.save(os.path.join(directory, 'dqn_model.h5'))

    def load(self, directory="ai_agent/saved_model"):
        model_path = os.path.join(directory, 'dqn_model.h5')
        if os.path.exists(model_path):
            logging.info("Loading existing q_network...")
            self.q_network = load_model(model_path)
        else:
            logging.info("Building new q_network...")
            self.q_network = self._build_q_network()
    
