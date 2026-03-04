# internet-monitor
Python DevOps tool for monitoring internet connectivity
# Internet Monitor

Simple DevOps tool for monitoring internet connectivity.

## Features

- Checks internet connection periodically
- Logs connection status
- Detects outages
- Lightweight monitoring tool

## Technologies

- Python
- Logging
- Ping

## Usage

Run the monitor:

python monitor.py

## Configuration

Edit `config.py`:

HOST = "1.1.1.1"
CHECK_INTERVAL = 30

## Example log

2026-03-04 12:01:01 - INFO - Internet connection OK
2026-03-04 12:01:31 - ERROR - Internet connection DOWN
