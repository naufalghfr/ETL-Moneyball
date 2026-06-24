import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def transform_players_data():
    csv_path = RAW_DATA_DIR / "players.csv"
    df_csv = pd.read_csv(csv_path) 
    
    df_csv['date_of_birth'] = pd.to_datetime(df_csv['date_of_birth'], errors='coerce')
    df_csv['age'] = (pd.Timestamp.now() - df_csv['date_of_birth']).dt.days // 365

    df_filtered = df_csv[(df_csv['age'] <= 25) & (df_csv['market_value_in_eur'] <= 5000000) & (df_csv['market_value_in_eur'] > 0)].copy()
    
    columns_to_keep = [
        'player_id', 'name', 'age', 'current_club_name', 
        'position', 'sub_position', 'market_value_in_eur'
    ]
    df_csv_clean = df_filtered[columns_to_keep]
    
    json_path = RAW_DATA_DIR / "sportapi_player_750.json"
    with open(json_path, "r", encoding="utf-8") as f:
        api_data = json.load(f)
        player_info = api_data.get("player", {})
        api_dict = {
            "name": player_info.get("name"),
            "api_market_value": player_info.get("proposedMarketValue"), 
            "sofascore_id": player_info.get("sofascoreId")
        }
        df_api = pd.DataFrame([api_dict])
        
    df_final = pd.merge(df_csv_clean, df_api, on="name", how="left").sort_values(by='market_value_in_eur', ascending=True)
    
    output_path = PROCESSED_DATA_DIR / "clean_players.csv"
    df_final.to_csv(output_path, index=False)
    
    return df_final

if __name__ == "__main__":
    df_result = transform_players_data()
    print(df_result.info()) 
