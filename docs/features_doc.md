# Feature Documentation

## Player Metadata

- 'season'<br>
   Type: int <br>
   Description: NFL season year <br>

- 'player_name'<br>
   Type: string<br>
   Description: Name of player<br>

- 'position'<br>
   Type: string ('QB', 'RB', 'WR', 'TE')<br>
   Description: Position of player<br>

- 'team'<br>
   Type: string <br>
   Description: Team player is on <br>

- 'is_rookie'<br>
   Type: binary (1 or 0)<br>
   Description: If player is rookie (Adjust for lack of stats)<br>

- 'draft_pos'<br>
   Type: int
   Description: If player is rookie their draft position in used since they have no stats for week 1

- 'experience_years'<br>
   Type: int<br>
   Description: Total years player has been in the NFL<br>

## Team Depth

- 'starter'<br>
   Type: Binary (1 or 0)<br>
   Description: Indicates whether the player is the listed starter for their position<br>

- 'depth_chart_position'<br>
   Type: int (1, 2, or 3)<br>
   Description: Position in the depth chart<br>

- 'missing_qb1'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their QB1<br>

- 'missing_rb1'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their RB1<br>

- 'missing_rb2'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their RB2<br>

- 'missing_wr1'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their WR1<br>

- 'missing_wr2'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their WR2<br>

- 'missing_te1'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their TE1<br>

- 'missing_te2'<br>
   Type: Binary (1 or 0)<br>
   Description: If player's team is missing their TE2<br>

- 'rest_days'<br>
   Type: int<br>
   Description: Total days after last game<br>

## Game Conditions

- 'game_date'
   Type: string (yyyy-mm-dd)
   Description: Day the game took place

- 'game_time_hour'
   Type: int (24 hour format)
   Description: Time in hours the game took place

- 'game_type'
   Type: string (pre, reg, post)
   Description: What type of game, preseasion, regular season, or post season

- 'home_away'<br>
   Type: string (home or away)<br>
   Description: If player's team is playing at home or away<br>

- 'week_number'<br>
   Type: int<br>
   Description: Game week<br>

- 'opponent_team'<br>
   Type: string<br>
   Description: Opponent team name<br>

- 'team_score'<br>
   Type: int<br>
   Description: Score of player's team<br>

- 'opponent_score'<br>
   Type: int<br>
   Description: Score of opponent's team<br>

- 'overtime'<br>
   Type: boolean<br>
   Description: If game went to overtime<br>

- 'w_l'<br>
   Type: char<br>
   Description: If player's team won or lose the game

- 'game_temp'<br>
   Type: int<br>
   Description: Temperature in Fareheit during the game<br>

- 'game_wind_speed'<br>
   Type: int<br>
   Description: Wind speed in miles per hour during the game<br>

- 'game_wind_direction'<br>
   Type: string (N, NE, E, SE, S, SW, W, NW)<br>
   Description: Cardinal wind direction during the game <br>

- 'forecast'<br>
   Type: string (sunny, raining, snowing)<br>
   Description: weather of the game<br>

- 'stadium_type'<br>
   Type: string (outside, dome, retractable)<br>
   Description: Type of stadium<br>

- 'grass_turf'<br>
   Type: string (grass or turf)<br>
   Description: If the stadium has grass or astroturf<br>

## Team Offense Stats

- 'team_rushing_rank_last3'<br>
   Type: float<br>
   Description: Average rushing rank of the last 3 games<br>

- 'team_passing_rank_last3'<br>
   Type: float<br>
   Description: Average passing rank of the last 3 games<br>

-  'team_rushing_rank_last5'<br>
   Type: float<br>
   Description: Average rushing rank of the last 5 games <br>

- 'team_passing_rank_last5'<br>
   Type: float<br>
   Description: Average passing rank of the last 5 games<br>

## Player Individual Stats

- 'player_passing_attempts_last3'<br>
   Type: int<br>
   Description: Total player passing attempts of the last 3 games<br>

- 'player_passing_completions_last3'<br>
   Type: int<br>
   Description: Total player passing completions of the last 3 games<br>

- 'player_passing_yards_last3'<br>
   Type: int<br>
   Description: Total player passing yards of the last 3 games<br>

- 'player_passing_touchdowns_last3'<br>
   Type: int<br>
   Description: Total player passing touchdowns of the last 3 games<br>

- 'player_passing_interceptions_last3'<br>
   Type: int<br>
   Description: Total player passing interceptions of the last 3 games<br>

- 'player_rushing_attempts_last3'<br>
   Type: int<br>
   Description: Total player rushing attempts of the last 3 games<br><br>

- 'player_rushing_yards_last3'<br>
   Type: int<br>
   Description: Total player rushing yards of the last 3 games<br>

- 'player_rushing_touchdowns_last3'<br>
   Type: int<br>
   Description: Total player rushing touchdowns of the last 3 games<br>

- 'player_targets_last3'<br>
   Type: int<br>
   Description: Total player passing targets of the last 3 games<br>

- 'player_receptions_last3'<br>
   Type: int<br>
   Description: Total player receptions of the last 3 games<br>

- 'player_receiving_yards_last3'<br>
   Type: int<br>
   Description: Total player receiving yards of the last 3 games<br>

- 'player_receiving_touchdowns_last3'<br>
   Type: int<br>
   Description: Total player receiving touchdowns of the last 3 games<br>

- 'player_passing_attempts_last5'<br>
   Type: int<br>
   Description: Total player passing attempts of the last 5 games<br>

- 'player_passing_completions_last5'<br>
   Type: int<br>
   Description: Total player passing completions of the last 5 games<br>

- 'player_passing_yards_last5'<br>
   Type: int<br>
   Description: Total player passing yards of the last 5 games<br>

- 'player_passing_touchdowns_last5'<br>
   Type: int<br>
   Description: Total player passing touchdowns of the last 5 games<br>

- 'player_passing_interceptions_last5'<br>
   Type: int<br>
   Description: Total player passing interceptions of the last 5 games<br>

- 'player_rushing_attempts_last5'<br>
   Type: int<br>
   Description: Total player rushing attempts of the last 5 games<br><br>

- 'player_rushing_yards_last5'<br>
   Type: int<br>
   Description: Total player rushing yards of the last 5 games<br>

- 'player_rushing_touchdowns_last5'<br>
   Type: int<br>
   Description: Total player rushing touchdowns of the last 5 games<br>

- 'player_targets_last5'<br>
   Type: int<br>
   Description: Total player passing targets of the last 5 games<br>

- 'player_receptions_last5'<br>
   Type: int<br>
   Description: Total player receptions of the last 5 games<br>

- 'player_receiving_yards_last5'<br>
   Type: int<br>
   Description: Total player receiving yards of the last 5 games<br>

- 'player_receiving_touchdowns_last5'<br>
   Type: int<br>
   Description: Total player receiving touchdowns of the last 5 games<br>

## Opponents Team Stats

- 'opp_run_defense_rank_last3'<br>
   Type: float<br>
   Description: Average opponents run defense rank of the last 3 games<br>

- 'opp_pass_defense_rank_last3'<br>
   Type: float<br>
   Description: Average opponents pass defense rank of the last 3 games<br>

- 'opp_sacks_last3'<br>
   Type: int<br>
   Description: Total opponents sacks of the last 3 games<br>

- 'opp_interceptions_last3'<br>
   Type: int<br>
   Description: Total opponents interceptions of the last 3 games<br>

- 'opp_forced_fumbles_last3'<br>
   Type: int<br>
   Description: Total opponents forced fumbles of the last 3 games<br>

- 'opp_touchdowns_allowed_last3'<br>
   Type: int<br>
   Description: Total opponents allowed touchdowns of the last 3 games<br>

- 'opp_rushing_attempts_allowed_last3'<br>
   Type: int<br>
   Description: Total opponents allowed rushing attempts of the last 3 games<br>

- 'opp_passing_attempts_allowed_last3'<br>
   Type: int<br>
   Description: Total opponents allowed passing attempts of the last 3 games<br>

- 'opp_rushing_yards_allowed_last3'<br>
   Type: int<br>
   Description: Total opponents allowed rushing yards of the last 3 games<br>

- 'opp_passing_yards_allowed_last3'<br>
   Type: int<br>
   Description: Total opponents allowed passing yards of the last 3 games<br>

- 'opp_qb_pressure_pct_last3'<br>
   Type: float<br>
   Description: Average % of opponent defensive plays that generated quarterback pressure of the last 3 games<br>

- 'opp_pass_coverage_rating_last3'<br>
   Type: float<br>
   Description: Average opponent pass coverage rating of the lkast 3 games<br>

- 'opp_run_defense_rank_last5'<br>
   Type: float<br>
   Description: Average opponents run defense rank of the last 5 games<br>

- 'opp_pass_defense_rank_last5'<br>
   Type: float<br>
   Description: Average opponents pass defense rank of the last 5 games<br>

- 'opp_sacks_last5'<br>
   Type: int<br>
   Description: Total opponents sacks of the last 5 games<br>

- 'opp_interceptions_last5'<br>
   Type: int<br>
   Description: Total opponents interceptions of the last 5 games<br>

- 'opp_forced_fumbles_last5'<br>
   Type: int<br>
   Description: Total opponents forced fumbles of the last 5 games<br>

- 'opp_touchdowns_allowed_last5'<br>
   Type: int<br>
   Description: Total opponents allowed touchdowns of the last 5 games<br>

- 'opp_rushing_attempts_allowed_last5'<br>
   Type: int<br>
   Description: Total opponents allowed rushing attempts of the last 5 games<br>

- 'opp_passing_attempts_allowed_last5'<br>
   Type: int<br>
   Description: Total opponents allowed passing attempts of the last 5 games<br>

- 'opp_rushing_yards_allowed_last5'<br>
   Type: int<br>
   Description: Total opponents allowed rushing yards of the last 5 games<br>

- 'opp_passing_yards_allowed_last5'<br>
   Type: int<br>
   Description: Total opponents allowed passing yards of the last 5 games<br>

- 'opp_qb_pressure_pct_last5'<br>
   Type: float<br>
   Description: Average % of opponent defensive plays that generated quarterback pressure of the last 5 games<br>

- 'opp_pass_coverage_rating_last5'<br>
   Type: float<br>
   Description: Average opponent pass coverage rating of the lkast 5 games<br>

## Usage Metrics

- 'target_share_last3'<br>
   Type: float<br>
   Description: Average passing target share of the last 3 games<br>

- 'snap_share_last3'<br>
   Type: float<br>
   Description: Average snap percent of the last 3 games<br>

- 'touch_share_last3'<br>
   Type: float<br>
   Description: Average carries + receptions share of the last 3 games<br>

- 'redzone_targets_last3'<br>
   Type: int<br>
   Description: Total redzone targets of the last 3 games<br>

- 'redzone_touches_last3'<br>
   Type: int<br>
   Description: Total redzone carries + recpetions of the last 3 games<br>

- 'target_share_last5'<br>
   Type: float<br>
   Description: Average passing target share of the last 5 games<br>

- 'snap_share_last5'<br>
   Type: float<br>
   Description: Average snap percent of the last 5 games<br>

- 'touch_share_last5'<br>
   Type: float<br>
   Description: Average carries + receptions share of the last 5 games<br>

- 'redzone_targets_last5'<br>
   Type: int<br>
   Description: Total redzone targets of the last 5 games<br>

- 'redzone_touches_last5'<br>
   Type: int<br>
   Description: Total redzone carries + recpetions of the last 5 games<br>

## Offensive Kicking Stats

- 'extra_point_last3'<br>
   Type: int<br>
   Description: Total player xp scored of the last 3 games<br>

- 'field_goal_20_29_last3'<br>
   Type: int<br>
   Description: Total player field goals scored from 20 to 29 yards of the last 3 games<br>

- 'field_goal_30_39_last3'<br>
   Type: int<br>
   Description: Total player field goals scored from 30 to 39 yards of the last 3 games<br>

- 'field_goal_40_49_last3'<br>
   Type: int<br>
   Description: Total player field goals scored from 40 to 49 yards of the last 3 games<br>

- 'field_goal_50_plus_last3'<br>
   Type: int<br>
   Description: Total player field goals scored from 50+ yards of the last 3 games<br>

- 'extra_point_last5'<br>
   Type: int<br>
   Description: Total player xp scored of the last 5 games<br>

- 'field_goal_20_29_last5'<br>
   Type: int<br>
   Description: Total player field goals scored from 20 to 29 yards of the last 5 games<br>

- 'field_goal_30_39_last5'<br>
   Type: int<br>
   Description: Total player field goals scored from 30 to 39 yards of the last 5 games<br>

- 'field_goal_40_49_last5'<br>
   Type: int<br>
   Description: Total player field goals scored from 40 to 49 yards of the last 5 games<br>

- 'field_goal_50_plus_last5'<br>
   Type: int<br>
   Description: Total player field goals scored from 50+ yards of the last 5 games<br>

## Defensive Kicking Stats

- 'extra_point_allowed_last3'<br>
   Type: int<br>
   Description: Total extra points allowed of the last 3 games<br>

- 'field_goal_20_29_allowed_last3'<br>
   Type: int<br>
   Description: Total field goals allowed from 20 to 29 yards of the last 3 games<br>

- 'field_goal_30_39_allowed_last3'<br>
   Type: int<br>
   Description: Total field goals allowed from 30 to 39 yards of the last 3 games<br>

- 'field_goal_40_49_allowed_last3'<br>
   Type: int<br>
   Description: Total field goals allowed from 40 to 49 yards of the last 3 games<br>

- 'field_goal_50_plus_allowed_last3'<br>
   Type: int<br>
   Description: Total field goals allowed from 50+ yards of the last 3 games<br>

- 'extra_point_allowed_last5'<br>
   Type: int<br>
   Description: Total field goals allowed of the last 5 games<br>

- 'field_goal_20_29_allowed_last5'<br>
   Type: int<br>
   Description: Total field goals allowed from 20 to 29 yards of the last 5 games<br>

- 'field_goal_30_39_allowed_last5'<br>
   Type: int<br>
   Description: Total field goals allowed from 30 to 39 yards of the last 5 games<br>

- 'field_goal_40_49_allowed_last5'<br>
   Type: int<br>
   Description: Total field goals allowed from 40 to 49 yards of the last 5 games<br>

- 'field_goal_50_plus_allowed_last5'<br>
   Type: int<br>
   Description: Total field goals allowed from 50+ yards of the last 5 games<br>

## Offensive Pace of Game

- 'team_offensive_plays_per_game_last3'<br>
   Type: float<br>
   Description: Average number of offensive plays run by the player's team over the last 3 games.<br>

- 'team_offensive_plays_per_game_last5'<br>
   Type: float<br>
   Description: Average number of offensive plays run by the player's team over the last 5  games.<br>

## Defensive Pace of Game

- 'team_defensive_plays_allowed_per_game_last3'<br>
   Type: float<br>
   Description: Average number of offensive allowed by the opponet's team over the last 3 games.<br>

- 'team_defensive_plays_allowed_per_game_last5'<br>
   Type: float<br>
   Description: Average number of offensive allowed by the opponet's team over the last 5 games.<br>

## Las Vegas Odds

- 'prop_type'<br>
   Type: string<br>
   Description: Type of player prop<br>

- 'prop_line'<br>
   Type: float<br>
   Description: Line for the player prop<br>

- 'game_total'<br>
   Type: float<br>
   Description: Vegas projected total points for the game<br>

- 'team_implied_points'<br>
   Type: float<br>
   Description: Vegas implied points for the player's team<br>

- 'spread'<br>
   Type: float<br>
   Description: Point spread relative to the player's team<br>

- 'hit'<br>
   Type: Binary (1 or 0)<br>
   Description: If the player hit the prop<br>

## Post Game Results

- 'actual'<br>
   Type: int<br>
   Description: stat relative to prop_type feature<br>

## More Features Coming Soon

- ''<br>
   Type: <br>
   Description: <br>

- ''<br>
   Type: <br>
   Description: <br>

- ''<br>
   Type: <br>
   Description: <br>

- ''<br>
   Type: <br>
   Description: <br>

- ''<br>
   Type: <br>
   Description: <br>