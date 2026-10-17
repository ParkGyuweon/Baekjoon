def solution(players, callings):
    player_dict = {}
    for idx in range(len(players)):
        player_dict[players[idx]] = idx
        
    for calling in callings:
        first_num = player_dict[calling]
        second_num = first_num - 1
        
        first_player = calling
        second_player = players[second_num]
        
        player_dict[calling] = second_num
        player_dict[second_player] = first_num
        
        players[first_num] = second_player
        players[second_num] = first_player
        
    return players