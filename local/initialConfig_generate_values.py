from class_profile import Profile
from database_root import *

def fakeProfileData():
    bob = Profile("default")
    bob.setMinTemp(72)
    bob.setMaxTemp(75)
    bob.updateDatabase()

    away = Profile("away")
    away.setMinTemp(68)
    away.setMaxTemp(74)
    away.updateDatabase()

    cat = Profile("cat")
    cat.setMinTemp(74)
    cat.setMaxTemp(74)
    cat.updateDatabase()

def fakeGuiData():
    db = Database()
    if not db.database_connection:
        print("Cannot update database. Database connection not available.")
        return

    gui_data = [
        {"current_profile": "default", "change_in_thermostat": "increase"},
        # Add more entries as needed
    ]

    for data in gui_data:
        current_profile = data["current_profile"]
        change_in_thermostat = data["change_in_thermostat"]
        
        # Construct the query
        query = f"INSERT INTO Gui (current_profile, change_in_thermostat) VALUES ('{current_profile}', '{change_in_thermostat}');"
        db.writeToDatabase(query)

    db.closeConnection()

def fakeSensorData():
    db = Database()
    if not db.database_connection:
        print("Cannot update database. Database connection not available.")
        return

    sensor_data = [
        {"id": 0, "temperature": 75, "humidity": 40},
        # Add more entries as needed
    ]

    for data in sensor_data:
        sensor_id = data["id"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        
        # Construct the query
        query = f"INSERT INTO Sensor (id, temperature, humidity) VALUES ({sensor_id}, {temperature}, {humidity});"
        db.writeToDatabase(query)

    db.closeConnection()

fakeSensorData()
fakeGuiData()
fakeProfileData()