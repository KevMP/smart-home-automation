from database_root import *

class Updater(Database):
    def __init__(self):
        super().__init__()
        self.change_in_thermostat = ''
        self.current_profile = 'DEFAULT'
        self.profile_maximum_temperature = 0
        self.profile_minimum_temperature = 0
    
    def getGuiChangeFromThermostat(self):
        if not self.database_connection:
            print("Cannot fetch data. Database connection not available.")
            return None

        try:
            query = """
                SELECT change_in_thermostat
                FROM Gui
                ORDER BY timestamp DESC
                LIMIT 1;
            """

            result = self.cursor.execute(query).fetchone()
            if result:
                self.change_in_thermostat = result[0]

        except sql.Error as e:
            print(f"Error fetching data: {e}")

    def getCurrentProfileFromGui(self):
        if not self.database_connection:
            print("Cannot fetch data. Database connection not available.")
            return None

        try:
            query = """
                SELECT current_profile
                FROM Gui
                ORDER BY timestamp DESC
            """

            result = self.cursor.execute(query).fetchone()
            if result:
                self.current_profile = result[0]

        except sql.Error as e:
            print(f"Error fetching profile: {e}")

    def getMinimumPreferredTemperatureFromProfile(self):
        if not self.database_connection or not self.current_profile:
            print("Cannot fetch data. Database connection not available or current_profile not set.")
            return None

        try:
            query = """
                SELECT min_temp
                FROM Profile
                WHERE name = ?;
            """

            result = self.cursor.execute(query, (self.current_profile,)).fetchone()
            if result:
                self.profile_minimum_temp = result[0]

        except sql.Error as e:
            print(f"Error fetching profile minimum temperature: {e}")

    def getMaximumPreferredTemperatureFromProfile(self):
        if not self.database_connection or not self.current_profile:
            print("Cannot fetch data. Database connection not available or current_profile not set.")
            return None

        try:
            query = """
                SELECT max_temp
                FROM Profile
                WHERE name = ?;
            """

            result = self.cursor.execute(query, (self.current_profile,)).fetchone()
            if result:
                self.profile_maximum_temp = result[0]

        except sql.Error as e:
            print(f"Error fetching profile maximum temperature: {e}")

    def increaseProfileTemperaturePreference(self):
        if not self.database_connection:
            print("Cannot update profile preference. Database connection not available.")
            return

        try:
            query = """
                UPDATE Profile
                SET min_temp = min_temp + 1, max_temp = max_temp + 1
                WHERE name = ?;
            """

            self.cursor.execute(query, (self.current_profile,))
            self.database_connection.commit()

        except sql.Error as e:
            print(f"Error updating profile preference: {e}")

    def decreaseProfilePreference(self):
        if not self.database_connection:
            print("Cannot update profile preference. Database connection not available.")
            return

        try:
            query = """
                UPDATE Profile
                SET min_temp = min_temp - 1, max_temp = max_temp - 1
                WHERE name = ?;
            """

            self.cursor.execute(query, (self.current_profile,))
            self.database_connection.commit()

        except sql.Error as e:
            print(f"Error updating profile preference: {e}")

    """
    If the user modifies the thermostat by either increasing it
    or decreasing it, that action will be logged by the Gui and
    written to the database in the field (change_in_thermostat)
    """
    def increaseOrDecreaseProfilePreference(self):
        if self.change_in_thermostat == 'increase':
            self.increaseProfileTemperaturePreference()
        elif self.change_in_thermostat == 'decrease':
            self.decreaseProfilePreference()

def main():
    profile_updater = Updater()
    while True:
        print("CHECKING FOR UPDATE IN PROFILE")
        profile_updater.getCurrentProfileFromGui()
        profile_updater.getGuiChangeFromThermostat()
        profile_updater.increaseOrDecreaseProfilePreference()

if __name__ == "__main__":
    main()