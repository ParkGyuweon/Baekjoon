import heapq

def solution(n, costs):
    
    def make(n):
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        return parent, rank
    
    def find(n, parent, rank):
        if parent[n] == n:
            return n
        parent[n] = find(parent[n], parent, rank)
        return parent[n]
    
    def union(one, two, parent, rank):
        ref1 = find(one, parent, rank)
        ref2 = find(two, parent, rank)
        if ref1 == ref2:
            return False
        
        if rank[ref1] < rank[ref2]:
            rank[ref1] += 1
            parent[ref1] = ref2
        else:
            rank[ref2] += 1
            parent[ref2] = ref1
            
        return True
    
    bridges = []
    count = 0
    total_cost = 0
    parent, rank = make(n)
    for cost in costs:
        heapq.heappush(bridges, (cost[2], cost[0], cost[1]))
        
    while count < n - 1:
        cur_cost, cur_one, cur_two = heapq.heappop(bridges)
        if union(cur_one, cur_two, parent, rank):
            total_cost += cur_cost
            count += 1
            
    return total_cost