from datetime import datetime

def log(message):
    time = datetime.now().replace(microsecond=0)
    with open("log.txt", "a+") as f:
        f.write("[{0}] {1}\n".format(time, message))
    f.close()