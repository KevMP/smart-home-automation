## profiles.py

class Profile:
    def __init__(self, min_preferred_temperature: int, max_preferred_temperature: int, identification: str):
        self.preferred_temperatures = [min_preferred_temperature, max_preferred_temperature]
        self.identification = identification
    
    def getLowerBound(self):
        self.lower_bound = self.preferred_temperatures[0]
        return self.lower_bound
    
    def getUpperBound(self):
        self.upper_bound = self.preferred_temperatures[1]
        return self.upper_bound

    def getPreferredTemperature(self):
        return self.preferred_temperatures
