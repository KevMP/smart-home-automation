import random
import tkinter as tk

# Occupancy Sensor
class OccupancySensor:
    def detect_occupancy(self):
        return random.choice([0, 1])

# Temperature Sensor
class TemperatureSensor:
    def read_temperature(self):
        return random.randint(18, 30)

# Humidity Sensor
class HumiditySensor:
    def read_humidity(self):
        return random.randint(30, 60)

# Smart Thermostat
class SmartThermostat:
    def __init__(self):
        self.ac_status = "OFF"
        self.temperature_setting = 22  # Default temperature setting

    def turn_on_ac(self):
        self.ac_status = "ON"

    def turn_off_ac(self):
        self.ac_status = "OFF"

    def set_temperature(self, temperature):
        self.temperature_setting = temperature

    def get_status(self):
        return {
            "Temperature Setting": self.temperature_setting,
            "AC Status": self.ac_status
        }

class SmartACEnvironment:
    def __init__(self):
        self.occupancy_sensor = OccupancySensor()
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.smart_thermostat = SmartThermostat()
        self.state = self.get_current_state()

    def get_current_state(self):
        return (self.occupancy_sensor.detect_occupancy(), self.temperature_sensor.read_temperature(), self.humidity_sensor.read_humidity())

    def step(self, action):
        if action == "TURN_ON_AC":
            self.smart_thermostat.turn_on_ac()
        elif action == "TURN_OFF_AC":
            self.smart_thermostat.turn_off_ac()
        elif action.startswith("SET_TEMP_"):
            temperature = int(action.split("_")[-1])
            self.smart_thermostat.set_temperature(temperature)

        occupancy, temperature, _ = self.state
        reward = 0
        if occupancy == 1 and temperature > self.smart_thermostat.temperature_setting:
            reward += 10
        if self.smart_thermostat.ac_status == "OFF":
            reward += 5
        
        next_state = self.get_current_state()
        done = True
        
        return next_state, reward, done