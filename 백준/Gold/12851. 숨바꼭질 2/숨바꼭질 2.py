from collections import deque
N, K = map(int, input().split())
time_answer, case_answer, find_flag = 0, 0, False
visited = [-1] * 100001

stack = deque([N])
visited[N] = 0

if N == K:
    print(0)
    print(1)
else:
    while stack:
        cur_position = stack.popleft()

        if K < N:
            if 0 <= cur_position - 1 <= 100000 and (visited[cur_position - 1] == -1 or visited[cur_position - 1] == visited[cur_position] + 1):
                if not find_flag and cur_position - 1 == K:
                    find_flag = True
                    visited[cur_position - 1] = visited[cur_position] + 1
                    case_answer += 1
                elif find_flag and cur_position - 1 == K and visited[cur_position - 1] == visited[cur_position] + 1:
                    case_answer += 1
                else:
                    visited[cur_position - 1] = visited[cur_position] + 1
                    stack.append(cur_position - 1)
        else:
            if 0 <= cur_position * 2 <= 100000 and (
                    visited[cur_position * 2] == -1 or visited[cur_position * 2] == visited[cur_position] + 1):
                if not find_flag and cur_position * 2 == K:
                    find_flag = True
                    visited[cur_position * 2] = visited[cur_position] + 1
                    case_answer += 1
                elif find_flag and cur_position * 2 == K and visited[cur_position * 2] == visited[cur_position] + 1:
                    case_answer += 1
                else:
                    visited[cur_position * 2] = visited[cur_position] + 1
                    stack.append(cur_position * 2)

            if 0 <= cur_position + 1 <= 100000 and (visited[cur_position + 1] == -1 or visited[cur_position + 1] == visited[cur_position] + 1):
                if not find_flag and cur_position + 1 == K:
                    find_flag = True
                    visited[cur_position + 1] = visited[cur_position] + 1
                    case_answer += 1
                elif find_flag and cur_position + 1 == K and visited[cur_position + 1] == visited[cur_position] + 1:
                    case_answer += 1
                else:
                    visited[cur_position + 1] = visited[cur_position] + 1
                    stack.append(cur_position + 1)

            if 0 <= cur_position - 1 <= 100000 and (visited[cur_position - 1] == -1 or visited[cur_position - 1] == visited[cur_position] + 1):
                if not find_flag and cur_position - 1 == K:
                    find_flag = True
                    visited[cur_position - 1] = visited[cur_position] + 1
                    case_answer += 1
                elif find_flag and cur_position - 1 == K and visited[cur_position - 1] == visited[cur_position] + 1:
                    case_answer += 1
                else:
                    visited[cur_position - 1] = visited[cur_position] + 1
                    stack.append(cur_position - 1)

    print(visited[K])
    print(case_answer)