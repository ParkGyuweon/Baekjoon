from collections import deque
T = int(input())

def DSLR_bfs(A, B):
    stack = deque([(A, '')])
    while stack:
        cur_num, cur_commands = stack.popleft()
        for command in ('D', 'S', 'L', 'R'):
            if command == 'D' and num_visited[(cur_num * 2) % 10000] == 0:
                if (cur_num * 2) % 10000 == B:
                    return cur_commands + 'D'
                stack.append(((cur_num * 2) % 10000, cur_commands + 'D'))
                num_visited[(cur_num * 2) % 10000] = 1
            elif command == 'S':
                if cur_num == 0 and num_visited[9999] == 0:
                    if 9999 == B:
                        return cur_commands + 'S'
                    stack.append((9999, cur_commands + 'S'))
                    num_visited[9999] = 1
                elif cur_num != 0 and num_visited[cur_num - 1] == 0:
                    if cur_num - 1 == B:
                        return cur_commands + 'S'
                    stack.append((cur_num - 1, cur_commands + 'S'))
                    num_visited[cur_num - 1] = 1
            else:
                if command == 'L' and num_visited[(cur_num % 1000) * 10 + cur_num // 1000] == 0:
                    if (cur_num % 1000) * 10 + cur_num // 1000 == B:
                        return cur_commands + 'L'
                    stack.append(((cur_num % 1000) * 10 + cur_num // 1000, cur_commands + 'L'))
                    num_visited[(cur_num % 1000) * 10 + cur_num // 1000] = 1
                elif command == 'R' and num_visited[(cur_num % 10) * 1000 + cur_num // 10] == 0:
                    if (cur_num % 10) * 1000 + cur_num // 10 == B:
                        return cur_commands + 'R'
                    stack.append(((cur_num % 10) * 1000 + cur_num // 10, cur_commands + 'R'))
                    num_visited[(cur_num % 10) * 1000 + cur_num // 10] = 1

for t in range(1, T + 1):
    A, B = map(int, input().split())
    num_visited = [0] * 10000
    num_visited[A] = 1
    print(DSLR_bfs(A, B))