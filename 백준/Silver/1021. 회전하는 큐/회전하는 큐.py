from collections import deque

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque([num for num in range(1, N + 1)])
turn = 0

for number in numbers:
    if queue[0] == number:
        queue.popleft()
    else:
        if len(queue) - queue.index(number) < queue.index(number):
            while queue[0] != number:
                queue.rotate(1)
                turn += 1
            queue.popleft()
        else:
            while queue[0] != number:
                queue.rotate(-1)
                turn += 1
            queue.popleft()

print(turn)