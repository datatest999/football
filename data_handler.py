import requests
import pandas as pd
import os 
from tqdm import tqdm

# Class to fetch data from Football API
class DataHandler:

    def __init__(self, config: dict):
        self._config = config

    def fetch_data_api(self) -> list:
        # Access configuration values
        seasons = self._config['seasons']

        data = []
        for season in tqdm(seasons):
            json_data = self.get_api_json(season)
            matches = json_data.get("matches", [])
            for match in matches:
                if isinstance(match, dict):
                    homeTeam = match.get("homeTeam", {}).get("name", "")
                    awayTeam = match.get("awayTeam", {}).get("name", "")
                    score = match.get("score", {})
                    matchScore = score.get("winner",
                                           "") if score is not None else ""
                    matchDuration = score.get("duration",
                                              "") if score is not None else ""
                    goalsHome = score.get("fullTime", {}).get(
                        "home", "") if score is not None else ""
                    goalsAway = score.get("fullTime", {}).get(
                        "away", "") if score is not None else ""
                    # Determine Winner , Loser , Drawn
                    winnerName = ""
                    loserName = ""
                    matchScore = score.get("winner", "")
                    if matchScore == "HOME_TEAM":
                        winnerName = homeTeam
                        loserName = awayTeam
                    elif matchScore == "AWAY_TEAM":
                        winnerName = awayTeam
                        loserName = homeTeam
                    elif matchScore == "DRAW":
                        winnerName = "Draw"
                        loserName = "Draw"

                    data.append({
                        "season": season,
                        "homeTeam": homeTeam,
                        "awayTeam": awayTeam,
                        "winnerName": winnerName,
                        "loserName": loserName,
                        "matchScore": matchScore,
                        "goalsHome": goalsHome,
                        "goalsAway": goalsAway,
                        "matchDuration": matchDuration
                    })
                else:
                    print("Warning: Invalid match object:", match)
        return data

    def get_url(self, season: str):
        base_url = self._config['base_url']
        league_id = self._config['league_id']
        
        url = f"{base_url}/competitions/{league_id}/matches?season={season}"
        return url 
        

    def get_api_json(self, season: str):
        api_token = self._config['api_token']
        headers = {"X-Auth-Token": api_token}
        url = self.get_url(season)
                
        response = requests.get(url, headers=headers)
        return response.json()

    def transform_data_to_csv(self, data: list) -> None:
        assert len(data) > 0
        csv_filename = self._config['csv_filename']
        df = pd.DataFrame(data)
        df.to_csv(csv_filename, index=False)

    def get_data_frame(self) -> pd.DataFrame:
        csv_filename = self._config['csv_filename']
        assert os.path.exists(csv_filename)
        return pd.read_csv(csv_filename)
            