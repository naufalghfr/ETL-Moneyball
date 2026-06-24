import sys
import os
from pathlib import Path
from scripts.extract import extract_transfermarkt_csv, extract_sportapi_player_stats
from scripts.transform import transform_players_data
from scripts.load import load_data_to_sqlite

BASE_DIR = Path(__file__).resolve().parent

def run_pipeline():
    extract_transfermarkt_csv()
    extract_sportapi_player_stats()
    
    transform_players_data()
    
    load_data_to_sqlite()


if __name__ == "__main__":
    os.chdir(BASE_DIR)
    run_pipeline()