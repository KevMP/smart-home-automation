# Setup : How to run
Depending on the amount of clients you may want to modify the clients that are accepted in the ```database_client_handler.py``` file. 

Additionally, modifying the IPv4 and the PORT number to the local LAN must be configured to accept clients.
```
database_client_handler.py file

def main():
    database = Database()

    server = Server("128.0.0.1", 5000)           ## Modify the IPv4 and PORT number to the local LAN address of the machine.
    server.bindServer()
    connected_clients = acceptClients(1, server) ## Modify the first argument to add more clients.

```
After configuring the client handler we can start the file, start the ```database_client_handler.py```

## Running the Sensor clients
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

# Database Schema
<details><summary>SHOW IMAGE SCHEMA</summary>

![database](https://github.com/KevMP/smart-home-automation/assets/100045145/46788cd0-9f58-401e-a2ac-2d669e2e6a58)

</details>

## Database Schema (written)
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
# Database Backup
* This file "database_backup.py" will backup our database every hour each day, it will have to be run as its own process on the same machine that the database will be stored.

# Client Server Network Diagram
<details><summary>SHOW DIAGRAM</summary>

![database network](https://github.com/KevMP/smart-home-automation/assets/100045145/5d55062b-8aab-47e7-b180-b555de59a255)
![smart-home-network](https://github.com/KevMP/smart-home-automation/assets/100045145/9f96d366-54b0-42b4-aff5-ccb2a754330b)

</details>

# Ai
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

![model-client](https://github.com/KevMP/smart-home-automation/assets/100045145/e615fe35-8acb-4aad-80aa-c2fed90dd479)
