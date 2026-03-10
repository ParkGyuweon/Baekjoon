T = int(input())

def check(weights, capacities):
    weight_idx = 0
    capacities_idx = 0
    current_sum = 0

    while weight_idx < N and capacities_idx < M:
        if weights[weight_idx] <= capacities[capacities_idx]:
            current_sum += weights[weight_idx]
            weight_idx += 1
            capacities_idx += 1
        else:
            weight_idx += 1

    return current_sum

for t in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(sorted(list(map(int, input().split())), reverse=True))
    capacities = list(sorted(list(map(int, input().split())), reverse=True))
    print(f'#{t} {check(weights, capacities)}')