from database_root import *

class Profile(Database):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.min_temp = 0
        self.max_temp = 0
    
    def setMinTemp(self, temperature: int):
        self.min_temp = temperature
    def setMaxTemp(self, temperature: int):
        self.max_temp = temperature
    
    def getProfileName(self):
        return self.name
    def getMinTemp(self):
        return self.min_temp
    def getMaxTemp(self):
        return self.max_temp

    def updateDatabase(self):
        if not self.database_connection:
            print("Cannot update database. Database connection not available.")
            return None

        """
        **********************************************************************************
        The following query is going to try and create a new profile if it does not exist,
        with the preferred temperature range of the user.

        If the profile exists, this will update the preferrences of the user.
        **********************************************************************************
        """
        update_query = """
            INSERT INTO Profile (name, min_temp, max_temp)
            VALUES (?, ?, ?)
            ON CONFLICT(name) DO UPDATE
            SET min_temp = ?, max_temp = ?;
        """

        self.cursor.execute(update_query, (self.getProfileName(), self.getMinTemp(), self.getMaxTemp(), self.getMinTemp(), self.getMaxTemp()))
        self.database_connection.commit()
        self.closeConnection()