from sense_hat import SenseHat

sense = SenseHat()

sense.clear() #clearing out panel
sense.set_rotation(270)

g = (0, 255, 0)
b = (255, 0, 0)
z = (0, 0, 0)

def validation_good():
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
    
print("Kérem az inputot: ")
choice = input()
if (choice == '1'):
    validation_good()
elif (choice == '2'):
    validation_bad()
else:
    print("Rossz input!")
    sense.clear()