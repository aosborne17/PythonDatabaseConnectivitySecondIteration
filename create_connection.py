import pyodbc
import secret_file
"""
This file is much better than the database connections file
because we have certain methods that are carrying out ONE function.

However, the other file has many functionalities all over the place
"""

"""
Creating a class that will
"""


class database_OOP:
    server = secret_file.server
    database = secret_file.database
    username = secret_file.username
    password = secret_file.password

    # this method is specifically for establishing a connection
    def establish_connection(self):
        connections = ('DRIVER={ODBC Driver 17 for SQL Server};'
                                     'SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection Successful")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("Connection Timed Out")
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface")
        else:
            cursor = connection.cursor()
            return cursor


