from collections import deque

def solution(n, wires):
    answer = n
    wires = deque(wires)
    for _ in range(len(wires)):
        cut_wire = wires.popleft()
        stack = deque([1])
        visited = [0] * (n + 1)
        visited[1] = 1
        while stack:
            cur_wire = stack.popleft()
            for wire in wires:
                if wire[0] == cur_wire and visited[wire[1]] == 0:
                    stack.append(wire[1])
                    visited[wire[1]] = 1
                if wire[1] == cur_wire and visited[wire[0]] == 0:
                    stack.append(wire[0])
                    visited[wire[0]] = 1
        answer = min(answer, abs(sum(visited) - (n - sum(visited))))
        wires.append(cut_wire)
    return answer