## simulation.py

from model import Model
from sensor import Sensor
from airconditioner import AirConditioner
from profiles import Profile
import random

class Simulation:
    def __init__(self, num_sensors=9):  # Increase the number of sensors
        self.lower_bound = 70 - 2
        self.upper_bound = 71 + 2
        self.current_temperature = self.lower_bound
        self.previous_temperature = self.current_temperature
        self.preferred_temperatures = [70, 71]
        self.sensors = [Sensor(distance_from_temperature_source=2.0) for _ in range(num_sensors)]
        self.air_conditioner = AirConditioner(self.current_temperature)
        self.profile = Profile(min_preferred_temperature=70, max_preferred_temperature=75, identification="Default")
        self.cycles = 0

    def getSensorTemperatureByIndex(self, index):
        if 0 <= index < len(self.sensors):
            return self.sensors[index].temperature
        return None

    def getCurrentTemperature(self):
        return self.current_temperature

    def setCurrentTemperature(self, action: int):
        self.previous_temperature = self.current_temperature

        # Update the temperature based on the air conditioner status
        if action == 1:
            self.air_conditioner.raise_temperature()
            self.current_temperature += 1
        elif action == -1:
            self.air_conditioner.lower_temperature()
            self.current_temperature -= 1
        else:
            self.air_conditioner.do_nothing_to_temperature()

        # Ensure the temperature stays within bounds
        self.current_temperature = max(self.lower_bound, min(self.current_temperature, self.upper_bound))

    def getDirection(self):
        return self.current_temperature - self.previous_temperature

    def isAiGettingCloserToTarget(self):
        preferred_temperature_range = self.profile.getPreferredTemperature()
        if self.current_temperature > preferred_temperature_range[0] and self.current_temperature < preferred_temperature_range[1]:
            if self.getDirection() == 0:
                return 1
            else:
                return -1
        elif self.current_temperature < preferred_temperature_range[0]:
            if self.getDirection() == 1:
                return 1
            else:
                return -1
        elif self.current_temperature > preferred_temperature_range[1]:
            if self.getDirection() == -1:
                return 1
            else:
                return -1

    def updateSensors(self):
        for sensor in self.sensors:
            if self.cycles % sensor.distance_from_temperature_source == 0:
                temperature_modifier = random.uniform(-1, 1)
                sensor.setTemperatureModifier(temperature_modifier)
                sensor.temperature += temperature_modifier
                sensor.temperature = max(self.lower_bound, min(sensor.temperature, self.upper_bound))

    def getSensorTemperatures(self):
        return [sensor.temperature for sensor in self.sensors]

    def increasePreferredTemperature(self):
        self.profile.preferred_temperatures = [temp + 1 for temp in self.profile.preferred_temperatures]
        self.lower_bound = self.profile.getLowerBound() - 2
        self.upper_bound = self.profile.getUpperBound() + 2

    def decreasePreferredTemperature(self):
        self.profile.preferred_temperatures = [temp - 1 for temp in self.profile.preferred_temperatures]
        self.lower_bound = self.profile.getLowerBound() - 2
        self.upper_bound = self.profile.getUpperBound() + 2

    def incrementCycles(self):
        self.cycles += 1
