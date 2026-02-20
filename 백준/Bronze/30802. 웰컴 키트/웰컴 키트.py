N = int(input())
people = list(map(int, input().split()))
T, P = map(int, input().split())
shirt, pen, each = 0, 0, 0

for item in people:
    if item / T == int(item / T):
        shirt = shirt + item // T
    else:
        shirt = shirt + item // T + 1
pen, each = sum(people) // P, sum(people) % P
print(f'{shirt}\n{pen} {each}')