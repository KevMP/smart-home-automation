# Database Schema

```plantuml
@startuml

class Profile {
  + name: String
  + min_temp: Double
  + max_temp: Double
}

class Sensor {
  + id: String
  + timestamp: DateTime
}

class Gui {
  + timestamp: DateTime
  + current_profile: String
  + change_in_thermostat: Double
}

class Airconditioner {
  + id: String
  + timestamp: DateTime
  + command: String
}

class TemperatureModel {
  + timestamp: DateTime
  + airconditioner_command: String
}

@enduml


# Database Backup
* This file "database_backup.py" will backup our database every hour each day, it will have to be run as its own process on the same machine that the database will be stored.

# Ai
* The ai will receive various pieces of information such as the current profile preferences that is informed by the Gui, and the profile data inside our profile table.
* Additionally we're also getting the temperature and humidity data so that we can calculate the "Feels Like" temperature.
* The feels like temperature will be used to dictate whether or not our model is making the correct decisions and will be punished or rewarded accordingly.

![Ai Diagram](https://github.com/KevMP/smart-home-automation/assets/100045145/e37b8a81-a3e7-478f-8c74-651d062369be)
