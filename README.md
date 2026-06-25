# Football Moneyball: Data Pipeline

A simple ETL data pipeline project built to scout young, high-potential football players who are still affordable (the *Moneyball* approach). 

This project extracts data from two different sources, merges them together, does a bit of feature engineering, and loads the clean data into a database so it's ready for analysis.

## Tech Stack
- **Language:** Python 3
- **Data Manipulation:** Pandas
- **API Requests:** Requests
- **Database:** SQLite3
- **Environment:** python-dotenv

## Extract, Transform, Load
1. **Extract:** - Reads raw player data from a local CSV dataset (Transfermarkt).
   - Pulls additional dynamic data (like proposed market value and unique IDs) straight from the SofaScore API. This is done using automated looping with a built-in delay so the server doesn't block.
   
2. **Transform:** - Performs feature engineering to accurately calculate the players' ages based on the `date_of_birth` column.
   - Applies the *Moneyball* filter: I only keep players who are 25 or younger with a market value strictly under €5,000,000.
   - Merges the CSV and JSON (API) data based on the player's name.
   
3. **Load:** - Saves the final, cleaned data as a `.csv` file inside the `processed` folder.
   - Dumps the data into the `scouting_players` table in an SQLite database (`football_moneyball.db`) so it's locked, loaded, and ready to be queried anytime.
