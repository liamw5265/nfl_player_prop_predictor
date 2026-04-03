import pandas as pd
from load_initial_data import load_weekly_individual_offense_players_stats, load_usage_stats, load_depth_chart

POSITION_LIST = ['QB', 'RB', 'WR', 'TE', 'K']

# REFACTOR THIS MESS
# FIX OUTPUT MESSAGES AND DOCSTRING

def clean_and_download_weekly_individual_offense_players_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    Cleans the raw dataframe of weekly individual offense players stats

    Args
        seasons: Season(s) to load using the nflreadpy library
            int: single season to load
            list[int]: list of seasons to load
            None: current/latest season

    Returns: Cleaned Pandas dataframe of weekly individual offensive player stats from [seasons] seasons
    '''

    if seasons is None:
        raw_dataframe = load_weekly_individual_offense_players_stats()
    elif seasons:
        raw_dataframe = load_weekly_individual_offense_players_stats(seasons)

    # Testing
    # raw_dataframe.to_csv('raw_player_stats.csv', index = False)

    cleaned_dataframe = raw_dataframe[['player_display_name', 'position', 'season', 'week', 'team', 'opponent_team', 
                                   'attempts', 'completions', 'passing_yards', 'passing_tds', 'passing_interceptions', 
                                   'carries', 'rushing_yards', 'rushing_tds', 
                                   'targets', 'receptions', 'receiving_yards', 'receiving_tds', 
                                   'sacks_suffered',
                                   'fg_att', 'fg_made', 
                                   'fg_made_0_19', 'fg_made_20_29', 'fg_made_30_39', 'fg_made_40_49', 'fg_made_50_59', 'fg_made_60_', 
                                   'pat_att', 'pat_made']]
    
    cleaned_dataframe = cleaned_dataframe[cleaned_dataframe['position'].isin(POSITION_LIST)]

    # Testing
    # cleaned_dataframe.to_csv('cleaned_player_stats.csv', index = False)

    return cleaned_dataframe

def clean_and_download_weekly_usage_offense_player_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    
    '''

    if seasons is None:
        raw_dataframe = load_usage_stats()
    elif seasons:
        raw_dataframe = load_usage_stats(seasons)

    # Testing
    # raw_dataframe.to_csv('raw_usage_stats.csv', index = False)

    cleaned_dataframe = raw_dataframe[['season', 'week', 'player', 'team', 'position', 
                                   'offense_snaps', 'offense_pct', 
                                   'defense_snaps', 'defense_pct', 
                                   'st_snaps', 'st_pct']]
    
    cleaned_dataframe = cleaned_dataframe[cleaned_dataframe['position'].isin(POSITION_LIST)]

    # Testing
    # cleaned_dataframe.to_csv('cleaned_usage_stats.csv', index = False)

    return cleaned_dataframe

def clean_and_download_weekly_offensive_depth_chart(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    
    '''

    rank_limits = {
    'QB': 2,
    'WR': 4,
    'RB': 3,
    'TE': 2
}

    if seasons is None:
        raw_dataframe = load_depth_chart()
    elif seasons:
        raw_dataframe = load_depth_chart(seasons)

    raw_dataframe.to_csv('raw_depth_stats.csv', index = False)

    raw_dataframe['dt'] = pd.to_datetime(raw_dataframe['dt'])

    latest_dt = raw_dataframe['dt'].max()
    raw_dataframe = raw_dataframe[raw_dataframe['dt'] == latest_dt]

    cleaned_dataframe = raw_dataframe[['player_name', 'team', 'pos_abb', 'pos_rank']]

    cleaned_dataframe = cleaned_dataframe[cleaned_dataframe['pos_rank'] <= cleaned_dataframe['pos_abb'].map(rank_limits)]

    cleaned_dataframe = cleaned_dataframe[cleaned_dataframe['pos_abb'].isin(POSITION_LIST)]

    cleaned_dataframe.to_csv('cleaned_depth_stats.csv', index = False)

    return cleaned_dataframe




if __name__ == '__main__':
    clean_and_download_weekly_offensive_depth_chart(2025)