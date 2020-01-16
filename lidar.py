from rplidar import RPLidar

def object_in_range(port, angle, distance):
    lidar = RPLidar(port)
    lidar.connect()

    for scan in lidar.iter_measurments():
        a = int(scan[2])
        d = int(scan[3] / 10)

        if ((a <= angle / 2) or (a >= 360 - angle / 2)):
            if ((d <= distance) and (d != 0)):
                break

    lidar.disconnect()
    return True