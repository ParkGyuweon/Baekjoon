T = int(input())

def back(turn, current, visited):
    global max_val
    if turn == change:
        max_val = max(max_val, int(''.join(map(str, current))))
        return
    visited.append((int(''.join(map(str, current))), turn))
    for first in range(len(number)):
        for second in range(first + 1, len(number)):
            current[first], current[second] = current[second], current[first]
            if (int(''.join(map(str, current))), turn + 1) not in visited:
                back(turn + 1, current, visited)
            current[first], current[second] = current[second], current[first]

for t in range(1, T + 1):
    number, change = map(int, input().split())
    number = list(map(int, list(str(number))))
    max_val = 0
    back(0, number, [(0, 0)])
    print(f'#{t} {max_val}')