import requests
import pandas as pd
from config import API_KEY, API_SECRET, BASE_URL, SYMBOL
from database import Session, PriceData
from datetime import datetime

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": API_SECRET
}

def get_historical_data(symbol=SYMBOL, limit=100):
    url = f"{BASE_URL}/v2/stocks/{symbol}/bars?timeframe=1Day&limit={limit}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    bars = response.json().get("bars", [])
    df = pd.DataFrame(bars)
    if df.empty:
        print("Inga data tillgängliga.")
        return None
    df["t"] = pd.to_datetime(df["t"])
    return df

def save_data_to_db(df):
    session = Session()
    for _, row in df.iterrows():
        data = PriceData(
            symbol=SYMBOL,
            timestamp=row["t"],
            open=row["o"],
            high=row["h"],
            low=row["l"],
            close=row["c"],
            volume=row["v"]
        )
        session.merge(data)
    session.commit()
    session.close()
    print(f"{len(df)} datapunkter sparade till databasen.")
