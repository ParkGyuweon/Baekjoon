def solution(bandage, health, attacks):
    recover_time = 0
    max_health = health
    time_table = [0] * (attacks[-1][0] + 1)
    for attack in attacks:
        time_table[attack[0]] = attack[1]
        
    for t in range(attacks[-1][0] + 1):
        if time_table[t] != 0:
            health -= time_table[t]
            recover_time = 0
            if health <= 0:
                return - 1
        else:
            recover_time += 1
            health += bandage[1]
            if recover_time == bandage[0]:
                health += bandage[2]
                recover_time = 0
        if health > max_health:
            health = max_health
    return health