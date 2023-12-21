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

# Ai
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

![Ai Diagram](https://github.com/KevMP/smart-home-automation/assets/100045145/e37b8a81-a3e7-478f-8c74-651d062369be)
