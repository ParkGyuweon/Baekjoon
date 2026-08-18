from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    while truck_weights or (not truck_weights and sum(bridge) != 0):
        if bridge[0] != 0:
            bridge[0] = 0
        if truck_weights and sum(bridge) + truck_weights[0] <= weight and bridge[0] == 0:
            bridge[0] = truck_weights.popleft()
        bridge.rotate(1)
        answer += 1
    return answer