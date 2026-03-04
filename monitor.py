import os
import time
import logging
import platform
from config import HOST, CHECK_INTERVAL, LOG_FILE


# Налаштування логування
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_internet(host):
    """
    Перевірка інтернету через ping.
    Працює на Windows і Linux.
    """

    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {host}"

    response = os.system(command)

    return response == 0


def main():

    print("🚀 Internet monitor started")
    logging.info("Internet monitor started")

    while True:

        status = check_internet(HOST)

        if status:

            message = f"Internet connection OK ({HOST})"

            print(message)
            logging.info(message)

        else:

            message = f"Internet connection DOWN ({HOST})"

            print(message)
            logging.error(message)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
