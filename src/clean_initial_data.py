import pandas as pd
from load_initial_data import load_weekly_individual_offense_players_stats, load_usage_stats, load_depth_chart, load_team_stats

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

def clean_and_download_weekly_team_stats(seasons: int | list[int] | None) -> pd.DataFrame:
    '''
    
    '''
    if seasons is None:
        all_stats = load_team_stats()
    elif seasons:
        all_stats = load_team_stats(seasons)

    passing_stats = (
        all_stats[ 
        ['team', 'opponent_team', 'week', 'passing_yards', 'sack_yards_lost']]
        .copy())
    passing_stats = passing_stats.sort_values(['team', 'week'])
    passing_stats['net_passing_yards'] = (
        passing_stats['passing_yards'] + passing_stats['sack_yards_lost'])
    passing_stats['total_net_passing_yards'] = (
        passing_stats.groupby('team')['net_passing_yards'].cumsum())
    passing_stats['net_passing_yards_per_game'] = (
        passing_stats['total_net_passing_yards'] / passing_stats['week'])
    passing_stats['passing_rank'] = (
        passing_stats.groupby('week')['net_passing_yards_per_game']
        .rank(ascending = False, method = 'min')
        .astype(int))


    rushing_stats = (
        all_stats[
        ['team', 'opponent_team', 'week', 'rushing_yards']]
        .copy())
    rushing_stats = rushing_stats.sort_values(['team', 'week'])
    rushing_stats['total_rushing_yards'] = (
        rushing_stats.groupby('team')['rushing_yards'].cumsum()) 
    rushing_stats['net_rushing_yards_per_game'] = (
        rushing_stats['total_rushing_yards'] / rushing_stats['week'])
    rushing_stats['rushing_rank'] = (
        rushing_stats.groupby('week')['net_rushing_yards_per_game']
        .rank(ascending = False, method = 'min')
        .astype(int))


    passing_yards_allowed = (
        passing_stats[['week', 'team', 'net_passing_yards']]
        .copy())
    passing_yards_allowed = (
        passing_yards_allowed.rename(columns = {
            'team': 'opponent_team_lookup', 
            'net_passing_yards': 'net_passing_yards_allowed'}))
    passing_yards_allowed['passing_allowed_rank'] = (
        passing_yards_allowed.groupby('week')['net_passing_yards_allowed']
        .rank(ascending = True, method = 'min').astype(int))


    rushing_yards_allowed = (
        rushing_stats[['week', 'team', 'rushing_yards']]
        .copy())
    rushing_yards_allowed = (
        rushing_yards_allowed.rename(columns = {
            'team': 'opponent_team_lookup', 
            'rushing_yards': 'rushing_yards_allowed'}))
    rushing_yards_allowed['rushing_allowed_rank'] = (
        rushing_yards_allowed.groupby('week')['rushing_yards_allowed']
        .rank(ascending = True, method = 'min').astype(int))


    passing_stats = (
        passing_stats.merge(passing_yards_allowed, 
        left_on = ['week', 'opponent_team'], 
        right_on = ['week', 'opponent_team_lookup'], 
        how = 'left').drop(columns = ['opponent_team_lookup']))

    rushing_stats = (
        rushing_stats.merge(rushing_yards_allowed, 
        left_on = ['week', 'opponent_team'], 
        right_on = ['week', 'opponent_team_lookup'], 
        how = 'left').drop(columns = ['opponent_team_lookup']))

    final = (
        passing_stats.merge(rushing_stats[
        ['team', 'week', 'rushing_yards', 'total_rushing_yards', 
        'net_rushing_yards_per_game', 'rushing_rank', 
        'rushing_yards_allowed', 'rushing_allowed_rank']], 
        on = ['team', 'week'], how = 'left'))


    final = final.round(2)
    final = final.sort_values(['week', 'team'])

    final = (
        final[
        ['week', 'team', 'opponent_team', 
        'passing_yards', 'sack_yards_lost', 
        'net_passing_yards', 'total_net_passing_yards', 
        'rushing_yards', 'total_rushing_yards', 
        'net_passing_yards_per_game', 'passing_rank', 
        'net_rushing_yards_per_game', 'rushing_rank', 
        'net_passing_yards_allowed', 'passing_allowed_rank', 
        'rushing_yards_allowed', 'rushing_allowed_rank']])
    

    final.to_csv('testtesttesttesttest.csv', index = False)
    return final


if __name__ == '__main__':
    clean_and_download_weekly_team_stats(2025)