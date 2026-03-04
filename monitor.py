import os
import time
import logging
from datetime import datetime
from config import HOST, CHECK_INTERVAL, LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_internet(host):
    response = os.system(f"ping -n 1 {host} > nul")
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
