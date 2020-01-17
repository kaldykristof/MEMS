import cv2
import tkinter as tk
import time
#-SAJÁT-MODULOK-----------------------
from lidar import object_in_range
from camera import take_picture
from database import Database

FREE_PARKING_SPOTS = 50 # a parkolóház férőhelyeinek száma
FREE_TIME = 10          # az ingyenesen bent tölthető idő mértéke
TARIFF = 100            # egy időegység után fizetendő pénz mennyisége

if(object_in_range(port="COM3", angle=10, distance=30)):
    while(True):
        try:
            picture = take_picture(cam_ID=0)
            break
        except:
            for i in range(5, 0, -1):
                print("Hiba! Művelet újrapróbálása {0} másodperc múlva!".format(i))
                time.sleep(1)

cv2.imshow("Image", picture)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: karakterfelismerés a készített fotón

car = "ABC-123"

db = Database(host="remotemysql.com", username="NB8WskrWz5", password="iN23mdSang", database="NB8WskrWz5")

if (db.contains(car)):
    # AUTÓ KIJÖN: bent töltött idő, fizetendő pénz kiszámítása, parkolóhely felszabadítása
    time_delta = db.remove(car)
    FREE_PARKING_SPOTS +=1
    
    payment = (time_delta - FREE_TIME) * TARIFF if (time_delta > FREE_TIME) else 0

    window = tk.Tk()
    window.title("Parkolóház")

    tk.Label(window, text="Rendszám: {0}".format(car), font=(None, 50)).pack()
    tk.Label(window, text="Bent töltött idő: {0} mp".format(time_delta), font=(None, 50)).pack()
    tk.Label(window, text="Fizetendő: {0} Ft".format(payment), font=(None, 50)).pack()
    tk.Button(window, text="Kilépés", command=window.destroy, height=10, width=50).pack()

    window.mainloop()
else:
    # AUTÓ BEMEGY: rendszám, aktuális idő elmentése, parkolóhely lefoglalása
    db.insert(car)
    FREE_PARKING_SPOTS -= 1

db.disconnect()
