import json
import os
import random
from logging.handlers import RotatingFileHandler

feature_order = ['temperature', 'humidity', 'occupancy', 'ac_status', 'target_temperature']

log_folder = 'smart_ac_simulation/screenshot'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file_path = os.path.join(log_folder, 'state_log.json')
handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=5)

def log_state(state):
    state_json = json.dumps(state)

    if handler.shouldRollover(state_json):
        handler.doRollover()
    
    with open(handler.baseFilename, 'a') as log_file:
        log_file.write(state_json + '\n')

class OccupancySensor:
    def __init__(self, mx=1):
        self.max_occupancy = mx

    def detect_occupancy(self):
        return random.randint(0, self.max_occupancy)

    def set_range(self, mx):
        self.max_occupancy = mx

class TemperatureSensor:
    def __init__(self, min_temp=18, max_temp=30):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def read_temperature(self):
        return random.randint(self.min_temp, self.max_temp)

    def set_range(self, min_temp, max_temp):
        if min_temp >= max_temp:
            raise ValueError("min_temp must be less than max_temp")
        self.min_temp = min_temp
        self.max_temp = max_temp

class HumiditySensor:
    def __init__(self, min_humidity=30, max_humidity=60):
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

    def read_humidity(self):
        return random.randint(self.min_humidity, self.max_humidity)

    def set_range(self, min_humidity, max_humidity):
        if min_humidity >= max_humidity:
            raise ValueError("min_humidity must be less than max_humidity")
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

class SmartACEnvironment:
    def __init__(self, state_file='smart_ac_simulation/ac_state.json'):
        os.makedirs(os.path.dirname(state_file), exist_ok=True)
        self.state_file = state_file

        self.occupancy_sensor = OccupancySensor()
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        
        if os.path.exists(self.state_file):
            self.load_state()
        else:
            self.initialize_state()

    def initialize_state(self):
        self.state = {
            'max_occupancy': self.occupancy_sensor.max_occupancy,
            'occupancy': self.occupancy_sensor.detect_occupancy(),
            
            'ac_status': True,
            'is_celsius': True,
            'target_temperature': 20,

            'humidity': self.humidity_sensor.read_humidity(),
            'min_humidity': self.humidity_sensor.min_humidity,
            'max_humidity': self.humidity_sensor.max_humidity,
            
            'temperature': self.temperature_sensor.read_temperature(),
            'min_temp': self.temperature_sensor.min_temp,
            'max_temp': self.temperature_sensor.max_temp,
        }
        self.save_state()

    def load_state(self):
        with open(self.state_file, 'r') as f:
            loaded_state = json.load(f)

        self.temperature_sensor.set_range(loaded_state['min_temp'], loaded_state['max_temp'])
        self.humidity_sensor.set_range(loaded_state['min_humidity'], loaded_state['max_humidity'])
        self.occupancy_sensor.set_range(loaded_state['max_occupancy'])

        self.state = loaded_state

    def save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def get_status(self):
        if self.state['is_celsius']:
            return {
                "temperature": self.state['temperature'],
                "occupancy": self.state['occupancy'],
                "humidity": self.state['humidity'],
                "ac_status": self.state['ac_status'],
                "target_temperature": self.state['target_temperature']
            }
        else:
            return {
                "temperature": (((self.state['temperature'] - 32) * 5 ) / 9),
                "occupancy": self.state['occupancy'],
                "humidity": self.state['humidity'],
                "ac_status": self.state['ac_status'],
                "target_temperature": self.state['target_temperature']
            }

    def get_current_state(self):
        return self.state

    def step(self, action):
        if action not in [0, 1, 2]:
            raise ValueError("Invalid action. Must be 0 (turn on AC), 1 (turn off AC), or 2 (set temperature).")
        
        if action == 0:
            self.state['ac_status'] = True
        elif action == 1:
            self.state['ac_status'] = False
        elif action == 2:
            new_temp = random.randint(self.temperature_sensor.min_temp, self.temperature_sensor.max_temp)
            self.state['temperature'] = new_temp

        self.state['occupancy'] = self.occupancy_sensor.detect_occupancy()
        self.state['temperature'] = self.temperature_sensor.read_temperature()
        self.state['humidity'] = self.humidity_sensor.read_humidity()

        self.save_state()

        reward = self.calculate_reward()
        done = self.check_done()

        return self.get_current_state(), reward, done

    def calculate_reward(self):
        reward = 0
        temperature_difference = abs(self.state['target_temperature'] - self.state['temperature'])
        if self.state['occupancy'] and self.state['ac_status']:
            reward += max(0, 10 - temperature_difference)
        if not self.state['ac_status'] and not self.state['occupancy']:
            reward += 5
        return reward

    def check_done(self):
        return self.state['temperature'] == self.state['target_temperature']

# env = SmartACEnvironment()
# print("Initial State:", env.get_current_state())
# env.save_state()
