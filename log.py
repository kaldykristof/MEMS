from datetime import datetime
import codecs

def log(message):
    time = datetime.now().replace(microsecond=0)
    with codecs.open("log.txt", "a+", "UTF-8") as f:
        f.write("[{0}] {1}\n".format(time, message))
    f.close()
    print(message)