from database_table import Table

if __name__ == "__main__":
    Profile = Table("Profile")
    Profile.addField("name", str, True)
    Profile.addField("min_temp", int)
    Profile.addField("max_temp", int)
    Profile.createTable()

    Sensor = Table("Sensor")
    Sensor.addField("id", int)
    Sensor.addField("timestamp", 'timestamp')
    Sensor.addField("temperature", float)
    Sensor.addField("humidity", float)
    Sensor.createTable()

    Airconditioner = Table("Airconditioner")
    Airconditioner.addField("id", int)
    Airconditioner.addField("timestamp", 'timestamp')
    Airconditioner.addField("command", str)
    Airconditioner.createTable()

    TemperatureModel = Table("TemperatureModel")
    TemperatureModel.addField("timestamp", 'timestamp')
    TemperatureModel.addField("airconditioner_command", str)
    TemperatureModel.createTable()