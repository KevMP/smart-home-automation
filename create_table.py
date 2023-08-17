import sqlite3

class Table():
    def drop_table(table):
        drop_table_query = f"DROP TABLE IF EXISTS {table}"
        cursor.execute(drop_table_query)
    
    def create_table(table_query, table_name):
        table_query.format(table_name)