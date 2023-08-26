import os
import time
import sqlite3

class Read():
    def read_all_data(self):
        pass

    def get_timestamp(self, cursor_object, table_name):
        self.timestamp_query = f'''SELECT timeStamp FROM {table_name}
                                   WHERE timeStamp = '''
        cursor_object.execute(self.timestamp_query)
        return cursor_object[0]