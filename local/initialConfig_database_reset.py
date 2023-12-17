from database_table import Table
import os
import time

def deleteDatabase():
    print("REMOVING FILE")
    time.sleep(2)
    os.remove("local/database.db")
    print("FILE REMOVED")
    
def createDatabase():
    print("CREATING DATABASE")
    time.sleep(1)
    file = open("local/database.db", 'w')
    file.close()
    print("DATABASE CREATED")

if __name__ == "__main__":
    deleteDatabase()
    createDatabase()
    Profile = Table("Profile")
    Profile.addField("name", str, True)
    Profile.addField("min_temp", int)
    Profile.addField("max_temp", int)
    Profile.createTable()

    Sensor = Table("Sensor")
    Sensor.addField("id", int)
    Sensor.addField("timestamp", 'timestamp', False, True)
    Sensor.addField("temperature", float)
    Sensor.addField("humidity", float)
    Sensor.createTable()

    Airconditioner = Table("Airconditioner")
    Airconditioner.addField("id", int)
    Airconditioner.addField("timestamp", 'timestamp', False, True)
    Airconditioner.addField("command", str)
    Airconditioner.createTable()

    Gui = Table("Gui")
    """
    Gui.addField("timestamp", 'timestamp', False, True)
    
    Note that setting the UNIQUE to false would mean
    that if two people set the temperature at the same time there
    could be a discrepancy for the ai.
    """
    Gui.addField("timestamp", 'timestamp', False, True)
    Gui.addField("current_profile", str)
    Gui.addField("change_in_thermostat", str)
    Gui.createTable()

    TemperatureModel = Table("TemperatureModel")
    TemperatureModel.addField("timestamp", 'timestamp', False, True)
    TemperatureModel.addField("airconditioner_command", str)
    TemperatureModel.createTable()