import sqlite3
import os
from flask import g

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
    def get_connection():
        if 'db' not in g:
            g.db = sqlite3.connect('databases/SHAS.db')
        return g.db

    @staticmethod
    def close_connection():
        db = g.pop('db', None)
        if db is not None:
            db.close()

    ## The following will be to select all data from each table.
    ## I will be creating separate functions for each respective
    ## table, systemData, userData, etc.

    def create_select_all_from_table_query(self, table_name_as_string):
        self.select_all_query = f'''SELECT * FROM {table_name_as_string}'''
        return self.select_all_query

    @staticmethod
    def select_all_system_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_system_data_query = SMAH().create_select_all_from_table_query(SMAH.ac_system_data_table)
        sql_cursor.execute(select_all_system_data_query)

        database_connection.commit()
        sql_cursor.close()
        database_connection.close()

    @staticmethod
    def select_all_sensor_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_sensor_data_query = SMAH().create_select_all_from_table_query(SMAH.sensor_data_table)
        sql_cursor.execute(select_all_sensor_data_query)

        database_connection.commit()
        sql_cursor.close()
        database_connection.close()

    @staticmethod
    def select_all_user_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_user_data_query = SMAH().create_select_all_from_table_query(SMAH.user_data_table)
        sql_cursor.execute(select_all_user_data_query)

        database_connection.commit()
        sql_cursor.close()
        database_connection.close()

    @staticmethod
    def select_all_user_account_data():
        database_connection = SMAH.get_connection()
        sql_cursor = database_connection.cursor()
        
        select_all_user_account_data_query = SMAH().create_select_all_from_table_query(SMAH.user_account_data_table)
        sql_cursor.execute(select_all_user_account_data_query)

        database_connection.commit()
        sql_cursor.close()
        database_connection.close()

    def select_all_data(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        result = [cursor.execute(f"SELECT * FROM {column}") for column in self.table_columns]
        result = cursor.fetchall()

        cursor.close()
        return result

    def print_all_data(self):
        data = self.select_all_data()
        print(data)
        
    def populate_with_fake_data(self):
        pass
        
    def deletes_all_data(self):
        pass
    
    ## The following function will create insert queries for the user account
    ## data table. It needs to be passed the column name of the table, and then
    ## the data to insert.

    def create_user_account_table_insert_query(self, column_name, data):
        self.user_name_query = f'''INSERT INTO {SMAH.user_account_data_table} ({column_name})
                                   VALUES ({data});'''
        return self.user_name_query

    @staticmethod
    def insert_user_name(user_identification):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('user_id', {user_identification}))

        database_conection.commit()
        sql_cursor.close()
        database_conection.close()
    
    @staticmethod
    def insert_email(email):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('email', email))

        database_conection.commit()
        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_password(password):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('password', password))
        
        database_conection.commit()
        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_first_name(first_name):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('first_name', first_name))

        sql_cursor.close()
        database_conection.close()

    @staticmethod
    def insert_last_name(last_name):
        database_conection = SMAH.get_connection()
        sql_cursor = database_conection.cursor()

        sql_cursor.execute(SMAH.create_user_account_table_insert_query('last_name', last_name))

        sql_cursor.close()
        database_conection.close()

    def get_user(self, email):
        pass

    def populate_with_fake_users(self):
        pass