class AirConditioner:
    def __init__(self, average_of_all_sensors):
        self.real_temperature = average_of_all_sensors
        self.airConditioner_status = 0
    
    def raise_temperature(self):
        self.airConditioner_status = 1
    
    def lower_temperature(self):
        self.airConditioner_status = -1
    
    def do_nothing_to_temperature(self):
        self.airConditioner_status = 0