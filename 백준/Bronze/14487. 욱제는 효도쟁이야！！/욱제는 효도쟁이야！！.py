N = int(input())
distances = list(map(int, input().split()))
print(sum(distances) - max(distances))