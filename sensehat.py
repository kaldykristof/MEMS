from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

#clearing out panel
sense.clear()

#changes in orientation
sense.set_rotation(270)

g = (0, 255, 0)
hg = (0, 115, 0)
hg2 = (0, 75, 0)
b = (255, 0, 0)
z = (0, 0, 0)

def validation_good():
    #changes in orientation
    sense.set_rotation(270)
    sense.clear()
    validation_good = [
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, g, z,
        z, z, z, z, z, g, z, z,
        z, z, z, z, g, z, z, z,
        z, g, z, g, z, z, z, z,
        z, z, g, z, z, z, z, z,
        z, z, z, z, z, z, z, z
        ]
    sense.set_pixels(validation_good)

def validation_bad():
    #changes in orientation
    sense.set_rotation(270)
    sense.clear()
    validation_bad = [
        z, z, z, z, z, z, z, z,
        z, b, z, z, z, z, b, z,
        z, z, b, z, z, b, z, z,
        z, z, z, b, b, z, z, z,
        z, z, z, b, b, z, z, z,
        z, z, b, z, z, b, z, z,
        z, b, z, z, z, z, b, z,
        z, z, z, z, z, z, z, z
        ]
    sense.set_pixels(validation_bad)
    
def loading_anim():
    #changes in orientation
    sense.set_rotation(180)
    sense.clear()
    for j in range(1, 5):
        for i in range(3,7):
            sense.set_pixel(3, i-2, g)
            sense.set_pixel(4, i-2, g)
            sleep(0.4)
            sense.set_pixel(3, i-1, hg)
            sense.set_pixel(4, i-1, hg)
            sleep(0.4)
            sense.set_pixel(3, i, hg2)
            sense.set_pixel(4, i, hg2)
            sleep(0.4)
        sense.clear()
        
print("Kérem az inputot: ")
choice = input()
if (choice == '1'):
    validation_good()
elif (choice == '2'):
    validation_bad()
elif (choice == '3'):
    loading_anim()
else:
    print("Rossz input!")
    sense.clear()