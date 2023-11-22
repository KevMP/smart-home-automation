from database import *
from datetime import datetime

class Controller():
    def __init__(self, db_name='local/data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    ## Need to rewrite this to send signals to the controllers.
    ## Currently it is used for simulation purposes.
    def increaseTemperature(self):
        current_temperature = Database().getMedianTemperature()
        current_temperature += 1
        ## Hours, Minutes, Seconds, Milliseconds
        Database().setTargetTemperature(datetime.now().strftime("%H:%M:%S.%f")[:-3], current_temperature)

    def decreaseTemperature(self):
        current_temperature = Database().getMedianTemperature()
        current_temperature -= 1
        ## Hours, Minutes, Seconds, Milliseconds
        Database().setTargetTemperature(datetime.now().strftime("%H:%M:%S.%f")[:-3], current_temperature)
    
    def getTargetTemperature(self):
        return Database().getTargetTemperature()

    def setTargetTemperature(self, target_temp: float):
        Database().setTargetTemperature(datetime.now().strftime("%H:%M:%S.%f")[:-3], target_temp)