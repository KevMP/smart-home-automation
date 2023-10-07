"""
_summary_

Returns:
    _type_: _description_
"""
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np
from simulation import Simulation

class DQNAgent:
    def __init__(self):
        self.model = self.create_model()
    
    def create_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(2, activation='relu', input_shape=(2,)),
            tf.keras.layers.Dense(3, activation='relu'),
            tf.keras.layers.Dense(2, activation='softmax')
        ])

        model.compile(optimizer='adam', loss='categorical_crossentropy')

        return model

    def train(self):
        simulation = Simulation(self.model)

        reward = simulation.run()
        print(reward)
       
       
agent = DQNAgent()
agent.train()