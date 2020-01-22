from time import sleep
from sense_hat import SenseHat

red     = (255,   0,   0)
green   = (  0, 255,   0)
white   = (255, 255, 255)
nothing = (  0,   0,   0)

R = red
G = green
W = white
_ = nothing

check_mark = [
    _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, _, _,
    _, _, _, _, _, _, G, _,
    _, _, _, _, _, G, _, _,
    _, _, _, _, G, _, _, _,
    _, G, _, G, _, _, _, _,
    _, _, G, _, _, _, _, _,
    _, _, _, _, _, _, _, _
]

x = [
    _, _, _, _, _, _, _, _,
    _, R, _, _, _, _, R, _,
    _, _, R, _, _, R, _, _,
    _, _, _, R, R, _, _, _,
    _, _, _, R, R, _, _, _,
    _, _, R, _, _, R, _, _,
    _, R, _, _, _, _, R, _,
    _, _, _, _, _, _, _, _
]

flash = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W
]

rainbow = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

class MySenseHat(object):
    def __init__(self):
        self.sensehat = SenseHat()
        self.sensehat.set_pixels(rainbow)
        sleep(1)
        self.sensehat.clear()
    
    def clear(self):
        self.sensehat.clear()
    
    def show_CM(self):
        self.clear()
        self.sensehat.set_pixels(check_mark)
        sleep(1)
        self.clear()

    def show_X(self):
        self.clear()
        self.sensehat.set_pixels(x)
        sleep(1)
        self.clear()

    def flash(self):
        self.clear()
        self.sensehat.set_pixels(flash)
        sleep(0.1)
        self.clear()

    def display(self, message):
        self.clear()
        self.sensehat.show_message(message, white)
        self.clear()