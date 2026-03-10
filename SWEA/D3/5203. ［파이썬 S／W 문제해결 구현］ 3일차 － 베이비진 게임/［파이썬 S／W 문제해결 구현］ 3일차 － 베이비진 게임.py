T = int(input())

def baby_jin(player):
    current = list(player)
    number_cnt = [0] * 10
    for item in current:
        number_cnt[item] += 1
    for item in number_cnt:
        if item >= 3:
            return True
    for i in range(8):
        if number_cnt[i] >= 1 and number_cnt[i + 1] >= 1 and number_cnt[i + 2] >= 1:
            return True

for t in range(1, T + 1):
    number_line = list(map(int, input().split()))
    first_player = []
    second_player = []
    while True:
        first_player.append(number_line.pop(0))
        second_player.append(number_line.pop(0))
        if baby_jin(first_player):
            print(f'#{t} 1')
            break
        if baby_jin(second_player):
            print(f'#{t} 2')
            break
        if not number_line:
            print(f'#{t} 0')
            break