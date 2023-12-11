class Sensor:
    def __init__(self, distanceFromTemperatureSource: float):
        self.distanceFromTemperatureSource = distanceFromTemperatureSource
        self.temperature = 0
    
    def setTemperature(self, cycles: int, temperatureModifier: int):
        if cycles % self.distanceFromTemperatureSource == 0:
            self.temperature += temperatureModifier