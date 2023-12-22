from class_network_client import *
from class_sensor import *
## import Adafruit_DHT (read documentation.txt for installation instructions)
def getSensorData(gpio_pin):
    """
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PINOUT = gpio_pin
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PINOUT)
    return humidity, temperature
    """
    return None, None

def main():
    client = Client()
    client.setIp()
    client.setPort()
    client.connectToServer()
    server_data = client.getData()

    sensor0 = Sensor(0, 21)
    sensor1 = Sensor(1, 22)
    sensor2 = Sensor(2, 23)

    list_of_sensors = [sensor0, sensor1, sensor2]
    """
    **********************************************************************************
    The following is going to be sending data from multiple
    sensors, the list above is so that we can expand how many
    sensors we are sending to the database.

    However sensor specific data still needs to be built, currently
    it is only capturing sensor data from one sensor, or however
    the getTemperature and getHumidity functions are made.
    **********************************************************************************
    """
    while True:
        for sensor in list_of_sensors:
            while server_data != "CONTINUE":
                print("GETTING SERVER DATA")
                server_data = client.getData()
                print(server_data)
            server_data = ''

            humidity, temperature = getSensorData(sensor.sensor_pinout)
            while humidity is None and temperature is None:
                print("GETTING SENSOR DATA")
                humidity, temperature = getSensorData(sensor.sensor_pinout)
                print(humidity, temperature)
            
            sensor.setHumidity(humidity)
            sensor.setTemperature(temperature)
            client.sendData(f"[{sensor.sensor_id}, {sensor.temperature}, {sensor.humidity}]")
            print("DATA SENT")

if __name__ == "__main__":
    main()