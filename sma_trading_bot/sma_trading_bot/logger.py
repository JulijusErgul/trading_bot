import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "tradingbot.log")

os.makedirs(LOG_DIR, exist_ok=True)

def log_event(timestamp, symbol, signal):
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {symbol} | Signal: {signal}\n")
