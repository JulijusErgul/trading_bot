import schedule
import time
from api import get_historical_data, save_data_to_db
from strategy import analyze
from database import init_db
from datetime import datetime
from config import SYMBOL
from dashboard import display_signal
from logger import log_event

init_db()

def run_bot():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n[{timestamp}] Kör strategi för {SYMBOL}...")
    df = get_historical_data()
    if df is not None:
        save_data_to_db(df)
        signal = analyze(df)
        display_signal(df, signal)
        log_event(timestamp, SYMBOL, signal)
    else:
        print("Ingen data att analysera.")

# Schemalagd körning varje dag kl 15:30
schedule.every().day.at("11:03").do(run_bot)

print("Tradingboten är igång. Väntar på schemalagd körning...")
while True:
    schedule.run_pending()
    time.sleep(1)
