def solution(diffs, times, limit):
    visited = [0] * (max(diffs) + 1)
    left, right = min(diffs), max(diffs)
    cur_level, answer = (left + right) // 2, right
    time_reduction = [0] * len(times)
    for idx in range(1, len(times)):
        time_reduction[idx] = times[idx] + times[idx - 1]
    stack = [(left, right, cur_level)]
    visited[cur_level] = 1
    while stack:
        cur_left, cur_right, cur_level = stack.pop()
        cur_time = 0
        for idx in range(len(diffs)):
            fail_count = diffs[idx] - cur_level
            if fail_count <= 0:
                cur_time += times[idx]
            else:
                cur_time += time_reduction[idx] * fail_count + times[idx]
        if cur_time <= limit:
            answer = min(answer, cur_level)
        if cur_time == limit:
            break
        elif cur_time < limit and visited[(cur_left + cur_level) // 2] == 0:
            stack.append((cur_left, cur_level, (cur_left + cur_level) // 2))
            visited[(cur_left + cur_level) // 2] = 1
        else:
            if visited[(cur_level + cur_right) // 2] == 0:
                visited[(cur_level + cur_right) // 2] = 1
                stack.append((cur_level + 1, cur_right, (cur_level + cur_right) // 2))
    return answer