# Introduction : Why this way
This program is meant to serve as separated processes, which we will call clients, all being controlled by one central process, which we will call the client handler.

As the name suggests it will be handling which clients read/write data to the database. Due to some constraints from the SQLite3 library, only one connection can be made at a time to the Database, so to get around this blocker for parallel reading/writing from multiple computers/clients, the Client Handler was made.

# Setup : How to run
## Setup : Configuring the Client Handler
Depending on the amount of clients you may want to modify the clients that are accepted in the ```database_client_handler.py``` file. 

Additionally, modifying the IPv4 and the PORT number to the LAN must be configured to accept clients.
```
database_client_handler.py file

def main():
    database = Database()

    server = Server("128.0.0.1", 5000)           ## Modify the IPv4 and PORT number to the local LAN address of the machine.
    server.bindServer()
    connected_clients = acceptClients(1, server) ## Modify the first argument to add more clients.

```
After configuring the client handler we can start the file, start the ```database_client_handler.py```

<details><summary>SHOW DIAGRAM</summary>

![database network](https://github.com/KevMP/smart-home-automation/assets/100045145/5d55062b-8aab-47e7-b180-b555de59a255)
![smart-home-network](https://github.com/KevMP/smart-home-automation/assets/100045145/9f96d366-54b0-42b4-aff5-ccb2a754330b)

</details>

<details><summary>HOW THE CLIENT HANDLER WORKS</summary>

The Client Handler doesn't allow for parallel computing, it's still one connection to the Database, what it does do however is allow for a Round Robin algorithm to go through each client, ask them whether they want to read/write, and either give them back that information(read) or write information to a table(write). This configuration allows us to add more and more computers, expanding horizontally infinitely.

</details>

## Setup : Running the Sensor clients

<details><summary>DEPENDENCIES</summary>

The Adafruit_DHT library is required for getting our sensor data, therefore run the following command.
```pip3 install Adafruit_DHT```

it can be imported as,
```import Adafruit_DHT```

</details>

Once the ```sensor_client.py``` is configured to their own sensor hardware, 
we can run each file on their after first starting up the client handler.

Note that our current default values are configured to run on the same local machine, 
to configure the client to connect to the respective ip/port addresses of the client_handler, 
we'd need to declare the network client object with those arguments (IPv4 address followed by the PORT number).

```
sensor_client.py

def main():
    sensor = Sensor(0)                 ## The 0 is the identifier of the hardware sensor, must be configured to the different sensors we are collecting data from.

    client = Client("128.0.4.1", 5000) ## Note that 128.0.4.1 is just an example IPv4 address, we'd need to figure out exactly what address the client handler will be running on, same deal with the port number.

```

## Setup : Running the Ai Model
Just like the previous step, we need to make sure that the ```database_client_handler.py``` is configured to secure a connection for our model.

After that step is done, we need to configure the ```ai_airconditioner_model.py``` client code.

Our Client() object call needs to have the IPv4 address and the PORT number that our ```database_client_handler.py``` is using.

<details><summary>SHOW WHERE TO CONFIGURE</summary>

```
ai_airconditioner_model.py

def main():
    temperature_model = AirconditionerModel()
    print(temperature_model.current_profile)
    client = Client() ## Configure the IPv4 address and PORT number to the Client Handler.
    client.connectToServer()
```

</details>

## Setup : Working with the Airconditioner
Just like the previous step, we need to make sure that the ```database_client_handler.py``` is configured to secure a connection for our airconditioner.

The ```database_airconditioner_scanner.py``` sole purpose is to check what command the Ai is outputting, note that this step can be completely bypassed and instead we could just read from the Ai Table (Would be faster this way and reduce the cycles that our Client Handler would have to move through).

But for the sake of clarification, there is a seperate table that can be used to read the commands dedicated to run our airconditioner hardware.

Note that configuring the IPv4 and the PORT number is still required to connect to the Client Handler.

<details><summary>SHOW WHERE TO CONFIGURE</summary>

```
def database_airconditioner_scanner():
    airconditioner_object = Airconditioner(0)
    client = Client() ## Configure the IPv4 address and PORT number to the Client Handler.
    client.connectToServer()
```

</details>

# Database : SQL
## Database : Schema (written)
<details><summary>SHOW WRITTEN SCHEMA</summary>

```
"Profile" Table

| name  | min_temp | max_temp |
===============================
| "bob" | 73       | 75       |

"Sensor" Table

| id | timestamp | temperature | humidity |
===========================================
| 0 | 12:00:44   | 75          | 40       |

"Gui" Table

| timestamp | current_profile | change_in_thermostat |
======================================================
| 12:00:44  | "bob"           | "increase"           |

"Airconditioner" Table
| id | timestamp | command    |
===============================
| 0  | 12:00:44  | "increase" |

"TemperatureModel" Table
| timestamp | airconditioner_command |
======================================
| 12:00:44  | "increase"             |

```

</details>

## Database : Automatic Backups
* This file ```database_backup.py``` will backup our database every hour each day, it will have to be run as its own process on the same machine that the database will be stored.

# Artificial Intelligence : About
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

<details><summary>SHOW AI DIAGRAM</summary>

![model-client](https://github.com/KevMP/smart-home-automation/assets/100045145/e615fe35-8acb-4aad-80aa-c2fed90dd479)

</details>
