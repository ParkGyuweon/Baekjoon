N = int(input())
people = list(sorted(list(map(int, input().split()))))
people_list = [False] * N

for i in range(1, N):
    people[i] = people[i] + people[i - 1]
print(sum(people))