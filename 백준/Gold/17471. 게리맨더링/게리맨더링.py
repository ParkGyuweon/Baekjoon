from collections import defaultdict
N = int(input())
people = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(N):
    for item in list(map(int, input().split()))[1:]:
        graph[i + 1].append(item)
flag = False
min_val = 10E10

partial = []
for i in range(1, 1 << N - 1):
    current = []
    for j in range(N):
        if i & (1 << j):
            current.append(j + 1)
    partial.append(current)

total = set(range(1, N + 1))

def possible(party):
    stack = [party[0]]
    stack_people = [people[party[0] - 1]]
    visited = [party[0]]
    while stack:
        current = stack.pop(0)
        party.remove(current)
        for item in graph[current]:
            if item in party and item not in visited:
                stack.append(item)
                stack_people.append(people[item - 1])
                visited.append(item)
    if not party:
        return sum(stack_people)
    return False

for item in partial:
    first = possible(list(item))
    second = possible(list(total - set(item)))
    if first and second:
        flag = True
        min_val = min(min_val, abs(second - first))

if not flag:
    print(-1)
else:
    print(min_val)