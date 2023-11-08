import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []  # store (state, action, reward, next_state, done)
        self.gamma = 0.9  # discount rate
        self.epsilon = 1.
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = learning_rate
        self.q_network = self._build_q_network()

    def _build_q_network(self):
        model = Sequential()
        model.add(Dense(32, input_dim=self.state_size, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
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
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.q_network.predict(next_state)[0]))
            target_f = self.q_network.predict(state)
            target_f[0][action] = target
            self.q_network.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

def train_dqn_agent():
    state_size = 3  # occupancy, temperature, humidity
    action_size = 3  # TURN_ON_AC, TURN_OFF_AC, SET_TEMP
    agent = DQNAgent(state_size, action_size)
    environment = SmartACEnvironment()

    episodes = 10
    max_steps = 10

    for episode in range(episodes):
        state = np.array([environment.get_current_state()])
        total_reward = 0
        
        for step in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = environment.step(action)
            next_state = np.array([next_state])
            agent.remember(state, action, reward, next_state, done)
            agent.replay()
            state = next_state
            total_reward += reward
            if done:
                break

    return agent