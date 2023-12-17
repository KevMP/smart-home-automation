from database_table import Table
import os
import time

def deleteDatabase():
    print("REMOVING FILE")
    os.remove("local/database.db")
    time.sleep(2)

def createDatabase():
    print("CREATING DATABASE")
    file = open("local/database.db", 'w')
    file.close()

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

    TemperatureModel = Table("TemperatureModel")
    TemperatureModel.addField("timestamp", 'timestamp', False, True)
    TemperatureModel.addField("airconditioner_command", str)
    TemperatureModel.createTable()