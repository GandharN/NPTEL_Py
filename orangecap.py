def orangecap(match_details):
    players_data = {}
    for k, v in match_details.items():
        for player_name, score in v.items():
            prev_player = player_name
            if prev_player == player_name:
                score = players_data.get(player_name, 0) + score
            players_data[player_name] = score
    high_score_player = max(players_data, key=lambda i: players_data[i])
    print (high_score_player, players_data[high_score_player])
