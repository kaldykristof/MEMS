from lidar import object_in_range
from database import Database

if(object_in_range("COM3", 10, 30)):
    print("Objektum a mérési határon belül!")

db = Database(host="remotemysql.com", username="NB8WskrWz5", password="iN23mdSang", database="NB8WskrWz5")

car = "ABC-123"

if (db.contains(car)):
	# AUTÓ KIJÖN
    time_delta = db.remove(car)
	print("Bent töltött idő: {0}".format(time_delta))
else:
	# AUTÓ BEMEGY
    db.insert(car)

db.close_connection()