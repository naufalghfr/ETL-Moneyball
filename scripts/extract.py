import os
import json
import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


load_dotenv(BASE_DIR / ".env")
API_KEY = os.getenv("RAPIDAPI_KEY")
URL = os.getenv("URL")

def extract_transfermarkt_csv():
    csv_path = RAW_DATA_DIR / "players.csv"
    df = pd.read_csv(csv_path)
    return df

def extract_sportapi_player_stats():
    url = URL
    headers = {"X-RapidAPI-Key": API_KEY,"X-RapidAPI-Host": "sportapi7.p.rapidapi.com"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            data = response.json()

            output_path = RAW_DATA_DIR / "sportapi_player_750.json"
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return data
    else:
        print(response.status_code)
        return None

if __name__ == "__main__":
    extract_transfermarkt_csv()
    extract_sportapi_player_stats()
