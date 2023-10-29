import random

class OccupancySensor:
    def detect_occupancy(self):
        return random.choice([0, 1])
class TemperatureSensor:
    def read_temperature(self):
        return random.randint(18, 30)
class HumiditySensor:
    def read_humidity(self):
        return random.randint(30, 60)

class SmartThermostat:
    def __init__(self):
        self.ac_status = False
        self.temperature_setting = 22

    def turn_on_ac(self):
        self.ac_status = True

    def turn_off_ac(self):
        self.ac_status = False

    def set_temperature(self, temperature):
        self.temperature_setting = temperature

    def get_status(self):
        return {
            "temp": self.temperature_setting,
            "ac_status": self.ac_status
        }

class SmartACEnvironment:
    def __init__(self):
        self.occupancy_sensor = OccupancySensor()
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.smart_thermostat = SmartThermostat()
        self.state = self.get_current_state()
    def get_ac_status(self):
        return self.smart_thermostat.get_status()

    def get_current_state(self):
        return (self.occupancy_sensor.detect_occupancy(), self.temperature_sensor.read_temperature(), self.humidity_sensor.read_humidity())

    def step(self, action):
        if action == 0:
            self.smart_thermostat.turn_on_ac()
        elif action == 1:
            self.smart_thermostat.turn_off_ac()
        elif action == 2:
            temperature = random.randint(18, 30)
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