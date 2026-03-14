import heapq, sys
input = sys.stdin.readline

N = int(input().strip())
heap = []
for i in range(N):
    number = int(input().strip())
    if number == 0:
        if not heap:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, number)