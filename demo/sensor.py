class Sensor:
    def __init__(self, distance_from_temperature_source: float):
        self.distance_from_temperature_source = distance_from_temperature_source
        self.temperature = 0
        self.temperature_modifier = 0
    
    def setTemperatureModifier(self, modifier):
        self.temperature_modifier = modifier