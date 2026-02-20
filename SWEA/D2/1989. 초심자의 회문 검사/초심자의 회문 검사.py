from collections import deque

T = int(input())
for t in range(1, T + 1):
    subject = deque(input())
    while len(subject) > 1 and subject.popleft() == subject.pop():
        if len(subject) <= 1:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')