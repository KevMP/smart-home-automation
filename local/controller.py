from database import *

class Controller():
    def __init__(self, db_name='local/data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def increaseTemperature(self):
        pass

    def decreaseTemperature(self):
        pass