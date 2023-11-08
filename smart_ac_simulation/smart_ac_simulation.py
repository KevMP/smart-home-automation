import json
import os
import random

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

class SmartThermostat:
    def __init__(self):
        self.ac_status = None
        self.temperature = None
        self.humidity = None
        self.occupancy = None
        self.is_celsius = True

    def turn_on_ac(self):
        self.ac_status = True

    def turn_off_ac(self):
        self.ac_status = False

    def set_temperature(self, temperature):
        self.temperature = temperature
    
    def set_humidity(self, humiditiy):
        self.humidity = humiditiy

    def set_occupancy(self, occupancy):
        self.humidity = occupancy

    def get_status(self):
        return {
            "temperature": self.temperature,
            "occupancy": self.occupancy,
            "humiditiy": self.humidity,
            "ac_status": self.ac_status
        }

class SmartACEnvironment:
    def __init__(self, state_file='smart_ac_simulation/ac_state.json'):
        os.makedirs(os.path.dirname(state_file), exist_ok=True)
        self.state_file = state_file

        self.occupancy_sensor = OccupancySensor()
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.smart_thermostat = SmartThermostat()

        self.smart_thermostat.turn_on_ac()
        self.smart_thermostat.set_humidity(self.humidity_sensor.read_humidity())
        self.smart_thermostat.set_temperature(self.temperature_sensor.read_temperature())
        self.smart_thermostat.set_occupancy(self.occupancy_sensor.detect_occupancy())
        
        if os.path.exists(self.state_file):
            self.load_state()
        else:
            self.initialize_state()

    def initialize_state(self):
        self.state = {
            'occupancy': self.occupancy_sensor.detect_occupancy(),
            'temperature': self.temperature_sensor.read_temperature(),
            'humidity': self.humidity_sensor.read_humidity(),
            'ac_status': self.smart_thermostat.ac_status,
            
            'min_humidity': self.humidity_sensor.min_humidity,
            'max_humidity': self.humidity_sensor.max_humidity,
            'min_temp': self.temperature_sensor.min_temp,
            'max_temp': self.temperature_sensor.max_temp,
            'max_occupancy': self.occupancy_sensor.max_occupancy
        }
        self.save_state()

    def load_state(self):
        with open(self.state_file, 'r') as f:
            loaded_state = json.load(f)
        self.smart_thermostat.set_occupancy(loaded_state['occupancy'])
        self.smart_thermostat.set_temperature(loaded_state['temperature'])
        self.smart_thermostat.set_humidity(loaded_state['humidity'])

        if loaded_state['ac_status']:
            self.smart_thermostat.turn_on_ac()
        else:
            self.smart_thermostat.turn_off_ac()

        self.temperature_sensor.set_range(loaded_state['min_temp'], loaded_state['max_temp'])
        self.humidity_sensor.set_range(loaded_state['min_humidity'], loaded_state['max_humidity'])
        self.occupancy_sensor.set_range(loaded_state['max_occupancy'])

        self.state = loaded_state

    def save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def get_current_state(self):
        return self.state

    def step(self, action):
        if action not in [0, 1, 2]:
            raise ValueError("Invalid action. Must be 0 (turn on AC), 1 (turn off AC), or 2 (set temperature).")
        
        if action == 0:
            self.smart_thermostat.turn_on_ac()
        elif action == 1:
            self.smart_thermostat.turn_off_ac()
        elif action == 2:
            new_temp = random.randint(self.temperature_sensor.min_temp, self.temperature_sensor.max_temp)
            self.smart_thermostat.set_temperature(new_temp)

        self.state['occupancy'] = self.occupancy_sensor.detect_occupancy()
        self.state['temperature'] = self.temperature_sensor.read_temperature()
        self.state['humidity'] = self.humidity_sensor.read_humidity()
        self.state['ac_status'] = self.smart_thermostat.ac_status
        self.state['temperature_setting'] = self.smart_thermostat.temperature_setting

        self.save_state()

        reward = self.calculate_reward()
        done = self.check_done()

        return self.get_current_state(), reward, done

    def calculate_reward(self):
        reward = 0
        temperature_difference = abs(self.state['temperature_setting'] - self.state['temperature'])
        if self.state['occupancy'] and self.state['ac_status']:
            reward += max(0, 10 - temperature_difference)
        if not self.state['ac_status'] and not self.state['occupancy']:
            reward += 5
        return reward

    def check_done(self):
        return self.state['temperature'] in range(22, 26)

# Test the environment
# env = SmartACEnvironment()
# print("Initial State:", env.get_current_state())

# env.occupancy_sensor.set_range(1)
# env.temperature_sensor.set_range(30, 100)
# env.save_state()

# new_env = SmartACEnvironment()
# print("Reloaded State:", new_env.get_current_state())
