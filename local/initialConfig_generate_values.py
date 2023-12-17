from class_profile import Profile
from class_sensor import Sensor

def fakeSensorData():
    sensor0 = Sensor(0)
    sensor0.setHumidity(60.54)
    sensor0.setTemperature(74.02)
    sensor0.updateDatabase()

    sensor1 = Sensor(1)
    sensor1.setHumidity(60.42)
    sensor1.setTemperature(72.48)
    sensor1.updateDatabase()

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
    pass

fakeSensorData()
fakeProfileData()