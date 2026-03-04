import os
import time
import logging
from datetime import datetime
from config import HOST, CHECK_INTERVAL, LOG_FILE
import platform

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_internet(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {host}"
    response = os.system(command)
    return response == 0

def main():
    print("Internet monitor started...")

    while True:
        status = check_internet(HOST)

        if status:
            message = "Internet connection OK"
            logging.info(message)
            print(message)

        else:
            message = "Internet connection DOWN"
            logging.error(message)
            print(message)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
