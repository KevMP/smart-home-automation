# Database Schema
![database](https://github.com/KevMP/smart-home-automation/assets/100045145/46788cd0-9f58-401e-a2ac-2d669e2e6a58)

## Database Schema (written)
Profile
* name
* min_temp
* max_temp

Sensor
* id
* timestamp

Gui
* timestamp
* current_profile
* change_in_thermostat

Airconditioner
* id
* timestamp
* command

TemperatureModel
* timestamp
* airconditioner_command

# Database Backup
* This file "database_backup.py" will backup our database every hour each day, it will have to be run as its own process on the same machine that the database will be stored.

# Client Server Network Diagram
![database network](https://github.com/KevMP/smart-home-automation/assets/100045145/5d55062b-8aab-47e7-b180-b555de59a255)
![smart-home-network](https://github.com/KevMP/smart-home-automation/assets/100045145/9f96d366-54b0-42b4-aff5-ccb2a754330b)

clients need to connect to the same ip and port number as the main database server.
and the amount of clients that the server will receive will also have to be configured intitially.

# Ai
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

![model-client](https://github.com/KevMP/smart-home-automation/assets/100045145/e615fe35-8acb-4aad-80aa-c2fed90dd479)
