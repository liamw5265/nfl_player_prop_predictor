import json
import requests

import pandas as pd
import nflreadpy as nfl

from bs4 import BeautifulSoup
from termcolor import colored
from typing import Dict, Tuple
from weather_api import get_request

STADIUM_INFO: Dict[str, Tuple[float, float, str, str]] = { # Tuple(Lat, Long, grass_turf, covered_open_retract)
    'NE' : (42.09, -71.26, 'Turf', 'Outside'), 
    'BUF': (42.77, 78.78, 'Turf', 'Outside'), 
    'MIA': (25.96, 80.24, 'Grasf', 'Outside'), 
    'NYJ': (40.81, -74.07, 'Turf', 'Outside'),
    'PIT': (40.45, 80.02, 'Grasf', 'Outside'), 
    'BAL': (39.28, 76.62, 'Grasf', 'Outside'), 
    'CIN': (39.09, 84.51, 'Turf', 'Outside'), 
    'CLE': (41.50, 81.69, 'Grasf', 'Outside'),
    'JAX': (30.32, 81.63, 'Grasf', 'Outside'), 
    'HOU': (29.68, -95.41, 'Turf', 'Retract'), 
    'IND': (39.76, 86.16, 'Turf', 'Retract'), 
    'TEN': (36.17, 86.77, 'Turf', 'Outside'),
    'DEN': (39.74, 105.02, 'Grasf', 'Outside'), 
    'LAC': (33.95, 118.33, 'Turf', 'Dome'), 
    'KC':  (39.04, 94.48, 'Grasf', 'Outside'), 
    'LV':  (36.09, 115.18, 'Grass', 'Dome'),
    'PHI': (39.90, -75.16, 'Grasf', 'Outside'), 
    'DAL': (32.74, 97.09, 'Turf', 'Retract'), 
    'WSH': (38.90, -7686, 'Grasf', 'Outside'), 
    'NYG': (40.81, -74.07, 'Turf', 'Outside'),
    'CHI': (41.86, 87.61, 'Grasf', 'Outside'), 
    'GB':  (44.50, 88.06, 'Grasf', 'Outside'), 
    'MIN': (44.97, 93.26, 'Turf', 'Dome'), 
    'DET': (42.34, 83.04, 'Turf', 'Retract'),
    'CAR': (35.22, 80.85, 'Turf', 'Outside'), 
    'TB':  (27.98, 82.50, 'Grasf', 'Outside'), 
    'ATL': (33.75, -84.40, 'Turf', 'Retract'), 
    'NO':  (29.95, 90.08, 'Turf', 'Dome'),
    'SEA': (47.60, 122.33, 'Turf', 'Outside'), 
    'LAR': (33.95, 118.33, 'Turf', 'Dome'), 
    'SF':  (37.40, 121.96, 'Grasf', 'Outside'), 
    'ARI': (33.52, 112.26, 'Grass', 'Retract')
}
SKILL_POSITIONS = ['QB', 'RB', 'WR', 'TE', 'K']


# REFACTOR THIS MESS
# FIX OUTPUT MESSAGES AND DOCSTRING
# READ THE OPENSTAX THREAD TO SCRAPE PRIZEPICKS

def load_weekly_individual_offense_players_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    Load weekly individual offensive player stats

    Args:
        seasons: Season(s) to load using the nflreadpy library
            int: single season to load
            list[int]: list of seasons to load
            None: current/latest season

    Return: Pandas dataframe of weekly individual offensive player stats from [seasons] seasons
    '''

    if seasons is None:
        player_stats = nfl.load_player_stats()
    elif seasons:
        player_stats = nfl.load_player_stats(seasons)
    else:
        print(colored('Invalid arguments'), 'red')
        return -1

    print(colored(f'Weekly individual stats for season(s) {seasons} loaded', 'green'))
    return player_stats.to_pandas()

def load_usage_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    Load weekly individual player usage stats

    Args:
        seasons: Season(s) to load using the nflreadpy library
            int: single season to load
            list[int]: list of seasons to load
            None: current/latest season

    Return: Pandas dataframe of weekly player usage stats from [seasons] seasons
    '''

    if seasons is None:
        player_usage_stats = nfl.load_snap_counts()
    elif seasons:
        player_usage_stats = nfl.load_snap_counts(seasons)
    else:
         print(colored('Invalid arguments'), 'red')
         return -1

    print(colored(f'Weekly usage stats for season(s) {seasons} loaded', 'green'))
    return player_usage_stats.to_pandas()

def load_depth_chart(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    Load weekly team depth charts

    Args:
        seasons: Season(s) to load using the nflreadpy library
            int: single season to load
            list[int]: list of seasons to load
            None: current/latest season

    Return: Pandas dataframe of weekly team depth charts for [seasons] seasons
    '''

    if seasons is None:
        team_depth_chart = nfl.load_depth_charts()
    elif seasons:
        team_depth_chart = nfl.load_depth_charts(seasons)
    else:
        print(colored('Invalid arguments'), 'red')
        return -1

    print(colored(f'Weekly depth chart stats from season(s) {seasons} loaded', 'green'))
    return team_depth_chart.to_pandas()

# Load Schdule data
def load_schedule_data(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    '''
    if seasons is None:
        schedule_data = nfl.load_schedules()
    elif seasons:
        schedule_data = nfl.load_schedules(seasons)
    else:
        print(colored('Invalid arguments'), 'red')
        return -1

    print(colored(f'Weekly schedule data for season(s) {seasons} loaded', 'green'))
    return schedule_data.to_pandas()

# Injury Report (Scrape every Wednesday & Satuday)
def load_weekly_injury_data(seasons: int | list[int] | None) -> pd.DataFrame: 
    '''
    Load weekly injury reports for nfl regular and post season games 

    Args:
    seasons: Season(s) to load using the nflreadpy library
            int: single season to load
            list[int]: list of seasons to load
            None: current/latest season

    Returns: Dataframe of all weekly injury reports for [seasons] seasons 
    '''
    file = 'test_injury_2.csv'
    weeks: Dict[int, str] = {
        1: 'reg1',
        2: 'reg2',
        3: 'reg3',
        4: 'reg4',
        5: 'reg5',
        6: 'reg6',
        7: 'reg7',
        8: 'reg8',
        9: 'reg9',
        10: 'reg10',
        11: 'reg11',
        12: 'reg12',
        13: 'reg13',
        14: 'reg14',
        15: 'reg15',
        16: 'reg16',
        17: 'reg17',
        18: 'reg18',
        19: 'post1',
        20: 'post2',
        21: 'post3',
        22: 'post4'
    }

    if seasons is None:
        return pd.DataFrame()

    if isinstance(seasons, int):
        seasons = [seasons]

    
    with open(file, 'w') as file:
        file.write('year,week,team,player,position,game_status\n')
        for year in seasons:
            for week_num, game in weeks.items():
                url = f'https://www.nfl.com/injuries/league/{year}/{game}'
                response = requests.get(url)

                if response.status_code != 200:
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')

                teams = soup.find_all(class_ = 'd3-o-section-sub-title')
                tables = soup.find_all('table')

                for team, table in zip(teams, tables):
                    team_name = team.get_text(strip = True)

                    for tr in table.find_all('tr')[1:]: 
                        data = f'{str(year)},{str(week_num)},{team_name},'
                        cols = [td.get_text(strip = True) for td in tr.find_all('td')]

                        player_name = cols[0]
                        pos = cols[1]
                        game_status = cols[-1]

                        data += f'"{player_name}",{pos},"{game_status}"' + '\n'
                        file.write(data)

    return pd.read_csv(file)
    


# Team Defense & Offense Stats
def load_team_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    
    '''

    if seasons is None:
        team_stats = nfl.load_team_stats()
    elif seasons:
        team_stats = nfl.load_team_stats(seasons)
    else:
        print(colored('Invalid arguments'), 'red')
        return -1

    print(colored(f'Team stats for season(s) {seasons} loaded', 'green'))
    return team_stats.to_pandas()

# Game Weather Data
def load_weather_data(date: str, time_hour: int, home_team: str) -> Tuple[float, float, str, str]:
    '''
    Uses the weather_api to get weather api from a specific stadium, date, and time

    Args
        date: Day of game
        time_hour: Nearest hour before the game
        home_team: What home stadium to search weather data for

    Returns: tuple of weather date
        float: Temp in F
        float: Wind speed in miles per hour
        str: Cardinal direction of wind
        str: Weather forecast
    '''

    temp, wind_speed, wind_direction, forecast = 0.0, 0.0, '', ''

    info = STADIUM_INFO[home_team]
    lat, long = info[0], info[1]

    json_output = get_request(date, time_hour, lat, long)

    hours = json_output["days"][0]["hours"]

    target_time = f"{time_hour:02d}:00:00"

    hour_data = None
    for hour in hours:
        if hour["datetime"] == target_time:
            hour_data = hour
            break

    if hour_data is None:
        print(colored(f'No temperature date found for hour {time_hour} on {date}', 'red'))

    temp = float(hour_data["temp"])
    wind_speed = float(hour_data["windspeed"])
    wind_direction = degrees_to_cardinal(hour_data["winddir"])
    forecast = hour_data["conditions"]


    return Tuple([temp, wind_speed, wind_direction, forecast])

def degrees_to_cardinal(degrees: float) -> str:
    '''
    Helper function to calculate degrees to cardinal direction

    Args
        degrees: wind direction in degrees from the json output from the api call
    '''
    directions = [
        "N", "NE", "E", "SE",
        "S", "SW", "W", "NW"
    ]
    index = round(degrees / 45) % 8
    return directions[index]

# Player Props

