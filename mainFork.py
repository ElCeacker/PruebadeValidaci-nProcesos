import os
import time
from datetime import datetime

def padre():
    for x in range(10):
        newPid = os.fork()
        if newPid == 0:
            hijo()
        time.sleep(10)

def hijo():
    date = datetime.now()
    print("Iniciando el proceso: %d" % os.getpid(), "creado a las", date.hour, ":" , date.minute, ":" , date.second)
    time.sleep(3)
    print("Terminando el proceso con PID: %d" % os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()