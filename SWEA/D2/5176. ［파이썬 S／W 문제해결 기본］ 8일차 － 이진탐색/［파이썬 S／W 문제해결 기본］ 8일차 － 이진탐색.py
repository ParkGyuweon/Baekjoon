from collections import defaultdict
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    answer_list = [i for i in range(1, N + 1)]
    graph, i, stack, current = defaultdict(list), 1, [], 1
    while i < N:
        graph[current].append(i + 1)
        stack.append(i + 1)
        i = i + 1
        if len(graph[current]) == 2:
            current = stack.pop(0)
    answer = [0] * N
    def search(num):
        if num not in graph:
            answer[num - 1] = answer_list.pop(0)
        elif len(graph[num]) == 2:
            search(graph[num][0])
            answer[num - 1] = answer_list.pop(0)
            search(graph[num][1])
        else:
            search(graph[num][0])
            answer[num - 1] = answer_list.pop(0)
    search(1)
    print(f'#{t} {answer[0]} {answer[N // 2 - 1]}')