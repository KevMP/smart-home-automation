import sqlite3
import os
from flask import g

class Insert():
    backend_folder = 'back-end'
    database_folder = os.path.join(backend_folder, 'databases')
    database_file = os.path.join(database_folder, 'SHAS.db')

    system_table = 'acSystemData'
    sensor_table = 'sensorData'
    user_table = 'userData'

    ## The following functions will create a sql query that will be executed
    ## by the cursor in our main function for this class.
    
    ## Note, that when we are generating fake data we can use these functions
    ## to create that faked data.

    def create_insert_ac_system_data_query(self, running_time, time_stamp, user_identification):
        self.sql_query = f'''INSERT INTO {self.system_table} (runningTime, timeStamp, userId)
                             VALUES ({running_time}, {time_stamp}, {user_identification});'''
        return self.sql_query

    def create_insert_sensor_data_query(self, temperature, user_identification, time_stamp):
        self.sql_query = f'''INSERT INTO {self.sensor_table} (temperature, userId, timestamp)
                             VALUES ({temperature}, {user_identification}, {time_stamp});'''
        return self.sql_query
    
    def create_insert_user_data_query(self, preferred_temperature, number_of_residents):
        self.sql_query = f'''INSERT INTO {self.user_table} (preferredTemperature, numberOfResidents)
                             VALUES ({preferred_temperature}, {number_of_residents});'''
        return self.sql_query

    ## The cursor object will be executing all sql statements,
    ## note that a database connection must be made before executing
    ## the sql code.

    def create_connection(self, database_path):
        self.database_connection = sqlite3.connect(database_path)
        return self.database_connection
    
    ## The following function will insert the data generated from the queries
    ## above as separate function calls.

    def insert_ac_system_data(self, running_time, time_stamp, user_identification):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        self.insert_query = self.create_insert_ac_system_data_query(running_time, time_stamp, user_identification)
        self.sql_cursor.execute(self.insert_query)

        self.database_connection.commit()
        self.sql_cursor.close()
        self.database_connection.close()

    def insert_sensor_data(self, temperature, user_identification, time_stamp):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        self.insert_query = self.create_insert_sensor_data_query(temperature, user_identification, time_stamp)
        self.sql_cursor.execute(self.insert_query)
        
        self.database_connection.commit()
        self.sql_cursor.close()
        self.database_connection.close()

    def insert_user_data(self, preferred_temperature, number_of_residents):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        self.insert_query = self.create_insert_user_data_query(preferred_temperature, number_of_residents)
        self.sql_cursor.execute(self.insert_query)
        
        self.database_connection.commit()
        self.sql_cursor.close()
        self.database_connection.close()

    def insert_all_data(self):
        self.database_connection = self.create_connection(self.database_file)
        self.sql_cursor = self.database_connection.cursor()

        ## An example of how to execute a sql cursor for inserting
        ## data to the tables is shown below.

        self.sql_cursor.execute(self.insert_user_data("72", 2))
        self.database_connection.commit()

        self.sql_cursor.close()
        self.database_connection.close()

class SMAH():
    ac_system_data_table = 'acSystemData'
    sensor_data_table = 'sensorData'
    user_data_table = 'userData'
    user_account_data_table = 'userAccount'
    """
    user_id: primary key, text, unique
    email: text, unique
    password: text
    first_name: text
    last_name: text
    """

    table_columns = [ac_system_data_table, sensor_data_table, user_data_table]

    @staticmethod
    def connect():
        server = sqlite3.connect('databases/SHAS.db')
        return server

    ## The following will be to select all data from each table.
    ## I will be creating separate functions for each respective
    ## table, systemData, userData, etc.

    def create_select_all_from_table_query(self, table_name_as_string):
        self.select_all_query = f'''SELECT * FROM {table_name_as_string}'''
        return self.select_all_query

    @staticmethod
    def select_all_system_data():
        database_connection = SMAH().start_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_system_data_query = SMAH().create_select_all_from_table_query(SMAH.ac_system_data_table)
        system_data = sql_cursor.execute(select_all_system_data_query)
        database_connection.commit()
        return system_data

    @staticmethod
    def select_all_sensor_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_sensor_data_query = SMAH().create_select_all_from_table_query(SMAH.sensor_data_table)
        sensor_data = sql_cursor.execute(select_all_sensor_data_query)
        database_connection.commit()

        sql_cursor.close()
        database_connection.close()
        return sensor_data

    @staticmethod
    def select_all_user_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_user_data_query = SMAH().create_select_all_from_table_query(SMAH.user_data_table)
        user_data = sql_cursor.execute(select_all_user_data_query)
        database_connection.commit()

        sql_cursor.close()
        database_connection.close()
        return user_data

    @staticmethod
    def select_all_user_account_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_user_account_data_query = SMAH().create_select_all_from_table_query(SMAH.user_account_data_table)
        user_account_data = sql_cursor.execute(select_all_user_account_data_query)
        database_connection.commit()

        sql_cursor.close()
        database_connection.close()
        return user_account_data
    
    ## The following function will create insert queries for the user account
    ## data table. It needs to be passed the column name of the table, and then
    ## the data to insert.

    @staticmethod
    def create_user_account_table_insert_query(column_name, data):
        insert_query = f'''INSERT INTO {SMAH.user_account_data_table} ({column_name})
                                   VALUES ({data});'''
        return insert_query

    @staticmethod
    def create_user_account_specific_table_query(column_name, data, user_identification):
        insert_query = f'''INSERT INTO {SMAH.user_account_data_table} ({column_name})
                                VALUES ({data})
                                WHERE user_id = '{user_identification}';'''
        return insert_query

    @staticmethod
    def insert_user_identification(user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('user_id', {user_identification}))
        database_conection.commit()

        sql_cursor.close()
        database_conection.close()
    
    @staticmethod
    def insert_email(email, user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_specific_table_query('email', email, user_identification))
        database_conection.commit()

        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_password(password, user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_specific_table_query('password', password, user_identification))
        database_conection.commit()
        
        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_first_name(first_name, user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_specific_table_query('first_name', first_name, user_identification))
        database_conection.commit()

        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_last_name(last_name, user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_specific_table_query('last_name', last_name, user_identification))
        database_conection.commit()

        sql_cursor.close()
        database_conection.close()
    
    ## The following functions will be used to verify if the user exists.
    ## We could first confirm if a email already exists, if so the user
    ## when registering would have to create a new email.
    ## We could also check if the user has inputted the correct username
    ## or password and return the user identification number as a True
    ## flag, else we return a FALSE flag that could be used to print
    ## out an error in the login page.

    def get_email_column_data(self):
        self.get_data_query = '''SELECT email FROM userAccount;'''

        self.database_connection = Insert().create_connection(Insert.database_file)
        self.database_connection.row_factory = lambda cursor, row: row[0]
        self.sql_cursor = self.database_connection.cursor()

        self.email_data = self.sql_cursor.execute(self.get_data_query).fetchall()
        self.database_connection.commit()

        self.sql_cursor.close()
        self.database_connection.close()
        
        return self.email_data

    def check_email(self, email):
        self.email_data = self.get_email_column_data()
        if email in self.email_data:
            return True
        else:
            return False

    @staticmethod
    def check_if_user_email_exists(email):
        return SMAH().check_email(email)

    def get_user_id_from_email_and_password(self, email, password):
        self.get_data_query = f'''SELECT user_id FROM userAccount
                                 WHERE email = '{email}'
                                 AND password = '{password}';'''

        self.database_connection = Insert().create_connection(Insert.database_file)
        self.database_connection.row_factory = lambda cursor, row: row[0]
        self.sql_cursor = self.database_connection.cursor()

        self.user_identification = self.sql_cursor.execute(self.get_data_query).fetchall()
        self.database_connection.commit()

        self.sql_cursor.close()
        self.database_connection.close()
        
        return self.user_identification

    def check_email_and_password(self, email, password):
        self.user_id = SMAH().get_user_id_from_email_and_password(email, password)
        if len(self.user_id) > 2: ## Since '[]' are two characters, we need to check if the length of user_data is greater than 2,
            return self.user_id   ##  to be able to tell if the user exists at all.
        else:
            return False
    
    @staticmethod
    def check_if_user_exists_from_email_and_password(email, password):
        return SMAH().check_email_and_password(email, password)

    @staticmethod
    def return_one():
        return '1'