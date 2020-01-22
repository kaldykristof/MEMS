import cv2
import tkinter as tk
import time
import os
#-SAJÁT-MODULOK-----------------------
from log import log
from sensehat import MySenseHat
from lidar import object_in_range
from camera import take_picture
from ocr import ocr, validator
from database import Database

FREE_PARKING_SPOTS = 50 # a parkolóház férőhelyeinek száma
FREE_TIME = 10          # az ingyenesen bent tölthető idő mértéke
TARIFF = 100            # egy időegység után fizetendő pénz mennyisége

sH = MySenseHat()

while (True):
    if(object_in_range(port="COM3", angle=10, distance=30)):
        print("Objektum észlelve...")
        log("Objektum ertekhataron belul")

        while(True):
            print("Kép készítése...")
            log("Kep keszitese folyamatban")
            sH.flash()
            image = take_picture(cam_ID=0)

            print("OCR folyamatban...")
            log("Karakterfelismeres folyamatban")
            license_plate = ocr(api_key="69e586ed1d88957", file_name=image)
            log('Kapott ertek: "{0}"'.format(license_plate))

            if (validator(license_plate) == True):
                log("A kapott ertek megfelelo")
                sH.show_CM()
                break
            else:
                log("A kapott ertek nem megfelelo")
                os.remove("images/{0}.png".format(image))
                sH.show_X()
                
                for i in range(5, 0, -1):
                    print("Hiba! Művelet újrapróbálása {0} másodperc múlva!".format(i))
                    time.sleep(1)

    print("Rendszám: {0}".format(license_plate))

    print("Kapcsolat felvétele az adatbázissal...")
    log("Adatbaziskapcsolat letrehozasa")

    db = Database(host="remotemysql.com", username="NB8WskrWz5", password="iN23mdSang", database="NB8WskrWz5")

    log("Adatbaziskapcsolat letre jott")

    if (db.contains(license_plate)):
        # AUTÓ KIJÖN: bent töltött idő, fizetendő pénz kiszámítása, parkolóhely felszabadítása
        time_delta = db.remove(license_plate)
        log("Rekord eltavolitva az adatbazisbol")

        FREE_PARKING_SPOTS += 1
        payment = (time_delta - FREE_TIME) * TARIFF if (time_delta > FREE_TIME) else 0

        window = tk.Tk()
        window.title("Parkolóház")

        tk.Label(window, text="Rendszám: {0}".format(license_plate), font=(None, 50)).pack()
        tk.Label(window, text="Bent töltött idő: {0} mp".format(time_delta), font=(None, 50)).pack()
        tk.Label(window, text="Fizetendő: {0} Ft".format(payment), font=(None, 50)).pack()
        tk.Button(window, text="Kilépés", command=window.destroy, height=10, width=50).pack()

        window.mainloop()
    else:
        # AUTÓ BEMEGY: rendszám, aktuális idő elmentése, parkolóhely lefoglalása
        db.insert(license_plate)
        log("Rekord hozzaadva az adatbazishoz")
        
        FREE_PARKING_SPOTS -= 1

    db.disconnect()