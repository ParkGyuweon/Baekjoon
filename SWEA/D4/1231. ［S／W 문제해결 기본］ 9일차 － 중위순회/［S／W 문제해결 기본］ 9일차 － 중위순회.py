for t in range(1, 11):
    N = int(input())
    character = [0] * N
    graph = {}
    for i in range(N):
        one_line = list(input().split())
        graph[int(one_line[0])] = list(sorted(map(int, one_line[2:])))
        character[int(one_line[0]) - 1] = one_line[1]
    answer = ''
    def search(num):
        if graph[num] == []:
            return character[num - 1]
        elif len(graph[num]) == 2:
            return search(graph[num][0]) + character[num - 1] + search(graph[num][1])
        else:
            return search(graph[num][0]) + character[num - 1]

    print(f'#{t} {search(1)}')