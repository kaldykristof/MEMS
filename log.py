from datetime import datetime

def log(msg):
    time = datetime.now().replace(microsecond=0)
    with open("log.txt", 'a') as f:
        f.write("{0} {1}\n".format(time, msg))