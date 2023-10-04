"""
_summary_

Returns:
    _type_: _description_
"""
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

class DQNAgent:
    """
    _summary_
    """
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
        """
        _summary_

        Returns:
            _type_: _description_
        """
        model = Sequential()
        model.add(Dense(32, input_dim=self.state_size, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        """
        _summary_

        Args:
            state (_type_): _description_
            action (_type_): _description_
            reward (_type_): _description_
            next_state (_type_): _description_
            done (function): _description_
        """
        self.memory.append((state, action, reward, next_state, done))

    def choose_action(self, state):
        """
        _summary_

        Args:
            state (_type_): _description_

        Returns:
            _type_: _description_
        """
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        q_values = self.q_network.predict(state)
        return np.argmax(q_values[0])

    def replay(self, batch_size=32):
        """
        _summary_

        Args:
            batch_size (int, optional): _description_. Defaults to 32.
        """
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

