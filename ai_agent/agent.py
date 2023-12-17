import random
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam, SGD, RMSprop, Adagrad, Adadelta, Adamax, Nadam, Ftrl
import numpy as np
import os
import platform
import logging
import json

logging.basicConfig(level=logging.INFO)

feature_order = ['temperature', 'humidity', 'target_temperature']

def extract_features(data_dict):
    return np.array([data_dict[key] for key in feature_order])

class DQNAgent:
    def __init__(self, state_size=3, action_size=3, learning_rate=0.01, gamma=0.09, epsilon=1, epsilon_min=0.01, epsilon_decay=0.995):
        logging.info("Initializing agent...")
        self.state_size = state_size
        self.action_size = action_size # raise / lower / do nothing
        self.learning_rate = learning_rate

        self.model_identification = None
    
        self.memory = []  # store (state, action, reward, next_state, done)
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.optimizer = 'Adam'
        self.q_network = self._build_q_network()

        self.load()

    def build_dense_layer(self, neurons, activation_func, state_size):
        return Dense(neurons, activation=activation_func, input_shape=(state_size,))

    def build_compiler(self, model, learning_rate, optimizer):
        if optimizer == 'Adam':
            model.compile(loss='mse', optimizer=Adam(learning_rate=learning_rate))
        elif optimizer == 'SGD':
            model.compile(loss='mse', optimizer=SGD(learning_rate=learning_rate))
        elif optimizer == 'RMSprop':
            model.compile(loss='mse', optimizer=RMSprop(learning_rate=learning_rate))
        elif optimizer == 'Adagrad':
            model.compile(loss='mse', optimizer=Adagrad(learning_rate=learning_rate))
        elif optimizer == 'Adadelta':
            model.compile(loss='mse', optimizer=Adadelta(learning_rate=learning_rate))
        elif optimizer == 'Adamax':
            model.compile(loss='mse', optimizer=Adamax(learning_rate=learning_rate))
        elif optimizer == 'Nadam':
            model.compile(loss='mse', optimizer=Nadam(learning_rate=learning_rate))
        elif optimizer == 'Ftrl':
            model.compile(loss='mse', optimizer=Ftrl(learning_rate=learning_rate))

    def _build_q_network(self, neurons=64, entrance_layer='relu', output_layer='linear'):
        model = Sequential()
        model.add(Dense(neurons, activation=entrance_layer, input_shape=(self.state_size,)))
        model.add(Dense(self.action_size, activation=output_layer))

        # if platform.system() == 'Darwin':
        #     model.compile(loss='mse', optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=self.learning_rate))
        # else:
        #     model.compile(loss='mse', optimizer=Adam(learning_rater=self.learning_rate))
        
        self.build_compiler(model, self.learning_rate, self.optimizer)
        
        return model

    def get_layers(self):
        return self.q_network.layers

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

    async def train_agent_fixed(self, environment, episodes=10, max_steps=10, save_interval=10, websocket=None):
        for episode in range(episodes):
            state_dict = environment.get_status()
            state = extract_features(state_dict).reshape(1, -1)
            total_reward = 0

            for step in range(max_steps):
                logging.info({'episode': episode+1, 'step': step+1})
                await websocket.send(json.dumps({'episode': episode+1, 'step': step+1}))
                
                action = self.choose_action(state)
                next_state_dict, reward, done = environment.step(action)
                next_state = extract_features(next_state_dict).reshape(1, -1)
                self.remember(state_dict, action, reward, next_state_dict, done)

                self.replay()

                state = next_state
                total_reward += reward

                if done:
                    break

            # if episode % save_interval == 0:
            #     self.save()

        return {
            'total_reward': total_reward,
            'episodes': episode + 1,
            'last_state': state.tolist()
        }

    def get_model_identifier(self):
        if self.is_default_parameters():
            return "default"
        else:
            layer_descriptions = []
            for layer in self.q_network.layers:
                # Example: Dense layer with 32 units and relu activation becomes "D32relu"
                desc = f"{layer.__class__.__name__[0]}{layer.output_shape[-1]}{layer.activation.__name__}"
                layer_descriptions.append(desc)

            layers_str = "_".join(layer_descriptions)

            return (f"lr{self.learning_rate}_gamma{self.gamma}_eps{self.epsilon}_epsmin{self.epsilon_min}_"
                    f"epsdecay{self.epsilon_decay}_layers{layers_str}_statesize{self.state_size}_actionsize{self.action_size}")

    def list_model_files(self, directory="ai_agent/saved_model", file_extension='.h5'):
        logging.info("Looking for model files...")
        model_files = []
        logging.info(directory)
        for file in os.listdir(directory):
            if file.endswith(file_extension):
                model_files.append(file)
        return model_files

    def update_hyperparameters(self, params):
        logging.info(params)

        self.learning_rate = params['learning_rate']
        self.gamma = params['gamma']
        self.epsilon = params['epsilon']
        self.epsilon_min = params['epsilon_min']
        self.epsilon_decay = params['epsilon_decay']
        self.action_size = params['action_size']
        self.learning_rate = params['learning_rate']
        self.state_size = params['state_size']
        
        model = Sequential()
        
        for layer in params['layers']:
            model.add(self.build_dense_layer(layer['neurons'], layer['activation'], layer['input_shape']))
        
        self.build_compiler(model, params['learning_rate'], params['optimizer'])
        
        self.save()
        
    def select_model(self, model_name):
        filename = f"dqn_{model_name}.keras"
        self.model_identification = filename
        if os.path.exists(os.path.join("ai_agent/saved_model", filename)):
            logging.info(f"Selecting model {model_name}...")
            self.q_network = load_model(os.path.join("ai_agent/saved_model", filename))
        logging.info("Agent listening...")

    def get_hyperparameters(self):
        return {
            'learning_rate': self.learning_rate,
            'gamma': self.gamma,
            'epsilon': self.epsilon,
            'epsilon_min': self.epsilon_min,
            'epsilon_decay': self.epsilon_decay,
            'state_size': self.state_size,
            'action_size': self.action_size,
            'layers': [
                        {'neurons': dense_layer.units,
                        'activation': dense_layer.activation.__name__,
                        'input_shape': dense_layer.input_shape[1]} 
                        for dense_layer in self.get_layers()
                        ],
            'models': self.list_model_files(),
            'optimizer': self.optimizer,
            'model_identification': self.model_identification
        }

    def is_default_parameters(self):
        default = [{'activation': 'relu', 'input_shape': 5, 'neurons': 64}, 
         {'activation': 'linear', 'input_shape': 64, 'neurons': 3}]
        
        
        return (self.learning_rate == 0.01 and self.gamma == 0.09 and 
                self.epsilon == 1 and self.epsilon_min == 0.01 and self.epsilon_decay == 0.995 and self.state_size == 5 and 
                self.action_size == 3 and self.optimizer == 'Adam' and sorted([
                        {'neurons': dense_layer.units,
                        'activation': dense_layer.activation.__name__,
                        'input_shape': dense_layer.input_shape[1]} 
                        for dense_layer in self.get_layers()], 
                        key=lambda d: d['neurons']) == sorted(default, key=lambda d: d['neurons']))

    def save(self, directory="ai_agent/saved_model"):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        identifier = self.get_model_identifier()
        filename = f"dqn_{identifier}.keras"
        self.q_network.save(os.path.join(directory, filename))

    def load(self, directory="ai_agent/saved_model"):
        identifier = self.get_model_identifier()
        filename = f"dqn_{identifier}.keras"
        
        self.model_identification = filename

        if os.path.exists(os.path.join(directory, filename)):
            logging.info("Loading existing q_network...")
            self.q_network = load_model(os.path.join(directory, filename))
        else:
            logging.info("Building new q_network...")
            self.save()

    def load_current_profile(self):
        with open('profile', 'r') as f:
            loaded_state = json.load(f)
            
    def dump_current_profile(self):
        with open('profile', 'r') as f:
            loaded_state = json.load(f)
