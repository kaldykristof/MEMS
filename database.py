from mysql.connector import connect, Error
from datetime import datetime

class Database(object):
    def __init__(self, host, username, password, database):
        try:
            self.connection = connect(host=host, user=username, password=password, database=database)
            self.cursor = self.connection.cursor()
            self.connection._open_connection()
        except Error as err:
            print("Hiba: {0}".format(err))

    def disconnect(self):
        return self.connection.disconnect()

    def contains(self, PLATE):
        self.cursor.execute('SELECT * FROM cars WHERE license_plate = "{0}"'.format(PLATE))
        result = self.cursor.fetchone()
        if (result is None):
            return False
        else:
            return True

    def insert(self, PLATE):
        current_datetime = datetime.now()
        self.cursor.execute('INSERT INTO cars (license_plate, arrival_time) VALUE ("{0}", "{1}")'.format(PLATE, current_datetime))
        self.connection.commit()

    def remove(self, PLATE):
        self.cursor.execute('SELECT arrival_time FROM cars WHERE license_plate="{0}";'.format(PLATE))
        arrival_time = self.cursor.fetchone()
        self.cursor.execute('DELETE FROM cars WHERE license_plate="{0}";'.format(PLATE))
        self.connection.commit()

        current_time = datetime.now()
        time_delta = current_time - arrival_time[0]

        return time_delta.seconds