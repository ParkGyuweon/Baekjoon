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
            if heap[0][1] == 0:
                print(-1 * heap[0][0])
                heapq.heappop(heap)
            else:
                print(heap[0][0])
                heapq.heappop(heap)
    else:
        if number > 0:
            heapq.heappush(heap, (number, 1))
        else:
            heapq.heappush(heap, (-1 * number, 0))