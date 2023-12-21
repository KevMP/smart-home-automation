# Database Schema

,------------------. ,------------------------------.
|Profile | ,---------------------. |Gui |
|------------------| |Sensor | |------------------------------|
|+ name: String | |---------------------| |+ timestamp: DateTime |
|+ min_temp: Double| |+ id: String | |+ current_profile: String |
|+ max_temp: Double| |+ timestamp: DateTime| |+ change_in_thermostat: Double|
------------------' ---------------------' `------------------------------'

,---------------------. ,--------------------------------.
|Airconditioner | |TemperatureModel |
|---------------------| |--------------------------------|
|+ id: String | |+ timestamp: DateTime |
|+ timestamp: DateTime| |+ airconditioner_command: String|
|+ command: String | --------------------------------' ---------------------'


# Database Backup
* This file "database_backup.py" will backup our database every hour each day, it will have to be run as its own process on the same machine that the database will be stored.

# Ai
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

![Ai Diagram](https://github.com/KevMP/smart-home-automation/assets/100045145/e37b8a81-a3e7-478f-8c74-651d062369be)
