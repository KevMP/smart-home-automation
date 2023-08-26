"""
_summary_

Returns:
    _type_: _description_
"""
import sqlite3
import os

class Database():
    """
    _summary_

    Returns:
        _type_: _description_
    """
    connection = None

    # Tables
    ac_system_data_table = 'acSystemData'
    sensor_data_table = 'sensorData'
    user_data_table = 'userData'

    table_columns = [ac_system_data_table, sensor_data_table, user_data_table]

    def __init__(self) -> None:
        """
        _summary_

        Args:
            database_file (_type_): _description_

        Returns:
            _type_: _description_
        """
        database_file = os.path.join(r'\databases', 'SHAS.db')
        self.connection = sqlite3.connect(os.getcwd() + database_file)

    def select_all_data(self):
        """
        Fetches all records from a given table in the database.

        Args:
            table_name (str): Name of the table to fetch records from.

        Returns:
            List[Tuple]: List of records from the table.
        """
        cursor = self.connection.cursor()

        result = [cursor.execute(f"SELECT * FROM {column}") for column in self.table_columns]
        result = cursor.fetchall()

        cursor.close()
        return result

    def print_all_data(self):
        """
        _summary_

        Args:
            table_name (_type_): _description_
        """
        data = self.select_all_data()
        print(data)

    def insert(self, data_object):
        """
        _summary_

        Args:
            data_object (_type_): _description_
        """
        