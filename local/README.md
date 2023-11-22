note, depending on how you imported the database module to your specific python file. 
You may need to call it with the class prefix, for example, Database().getAllProfilesAsArray()

# Creating a profile:
### Function names in red.
![instructions_creation](https://github.com/KevMP/smart-home-automation/assets/100045145/b66f3226-2fb5-42a1-b03b-be401ddc881a)


in case you want to just copy/paste the functions,
* setCurrentProfile(identification_number)
* setMinimumPreferredTemperature(identification_number, value)
* setMaximumPreferredTemperature(identification_number, value)


# Getting the profile to the Local GUI:
### Function names in red.
![gettinguserprofiles](https://github.com/KevMP/smart-home-automation/assets/100045145/3320cec5-8461-4792-809f-1567410e41ab)


in case you want to just copy/paste the functions,
* getAllProfilesAsArray()
* getMinimumPreferredTemperature(identification_number)
* getMaximumPreferredTemperature(identification_number)

# EMBEDDED_PLAN
* Feeding the temperature/humidity data to the main controller:
    * temperature and humidity sensors could be taped to a breadboard, which can then be placed on a flat wall-surface.
    * wiring it could be done by holes in the walls tracing around the back, that is then led to a master controller? or a separate controller that is then fed via wireless communication. the problem would be space from the other sensors, having the master controller also connected to the touchscreen.
    * there's another matter of also connecting/hacking the air condtioner. making it so that it can be controlled by the thermostat/raspberrypi.
    * the smart vents would also be another issue, some concerns about if the ventilation is closed while the air conditioner is on could be a concern. Therefore at least one vent, or at minimum, one path would have to remain open.
    * assuming that there is 4 sensors, one ventilation controller, two air conditioners, then there must be a minimum of 8 GPIO pins available for the raspberry pi. Assuming that there is enough headspace for the controller. A "solution" to this problem could be wireless communication between each controller (Besides the touchscreen).