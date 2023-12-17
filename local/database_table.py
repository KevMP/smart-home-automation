from database_root import *
"""
**********************************************************************************
Example on creating a table.
Profile = Table("Profile")
Profile.addField("username", str)
Profile.addField("password", str)
Profile.addField("min_temp", int)
Profile.addField("max_temp", int)
Profile.createTable()

Special Note, to use this functionality, it needs to be called
outside of its dbms folder. This is due to how the module is imported,
note that this file was made for the reset_database.py file.
**********************************************************************************
"""

class Table(Database):
    def __init__(self, table_name: str):
        super().__init__()
        self.name = table_name
        self.fields = []

    def addField(self, field_name: str, data_type, unique=False):
        self.data_conversion = {
            str: 'TEXT',
            int: 'INTEGER',
            float: 'REAL',
            'timestamp': 'TIMESTAMP'
        }
        field_declaration = f"{field_name} {self.data_conversion[data_type]}"
        if unique:
            field_declaration += " UNIQUE"

        self.fields.append(field_declaration)

    """
    **********************************************************************************
    Assuming that the connection to the database is valid, the following
    will create a table for the database.db file.
    Note that to do so, there needs to be a field in the fields list.
    **********************************************************************************
    """
    def createTable(self):
        if not self.database_connection:
            print("Cannot create table. Database connection not available.")
            return None

        if not self.fields:
            print("No fields added. Cannot create an empty table.")
            return None

        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.name} ("
        create_table_query += ', '.join(self.fields)
        create_table_query += ");"

        self.cursor.execute(create_table_query)
        self.database_connection.commit()
        self.closeConnection()