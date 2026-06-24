from pandas._libs.tslibs import nattype
import pandas as pd
import sqlite3
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def load_data_to_sqlite():
    csv_path = PROCESSED_DATA_DIR / "clean_players.csv"
    db_path = BASE_DIR / "football_moneyball.db"

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)

    df.to_sql("scouting_players", conn, if_exists="replace", index=False)

    conn.close()

if __name__ == "__main__":
    load_data_to_sqlite()

