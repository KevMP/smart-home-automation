from database_root import *
"""
Get ai command from the table in the database.
keep it in the init variable.

Functions that this class needs to do.

* Get the command from the ai table in the database.db file.
* Save the command from the ai into a variable inside the class.
* Write the command to the air conditioner class table.
"""

class Airconditioner(Database):
    def __init__(self, name: str):
        super().__init__()
    
    """
    to close the data base connection,
    call this function:
    self.closeConnection()
    """