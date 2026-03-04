from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
zero_cnt = belt.count(0)
robot = deque([0] * N)
turn = 0
while zero_cnt < K:
    turn += 1
    belt.rotate(1)
    robot.rotate(1)
    if robot[-1] == 1:
        robot[-1] -= 1
    for i in range(N - 1, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            robot[i], robot[i + 1] = robot[i + 1], robot[i]
            belt[i + 1] -= 1
            if robot[-1] == 1:
                robot[-1] -= 1
            if belt[i + 1] == 0:
                zero_cnt += 1
                if zero_cnt >= K:
                    break
    else:
        if belt[0] >= 1:
            robot[0] = 1
            belt[0] -= 1
            if belt[0] == 0:
                zero_cnt += 1

print(turn)