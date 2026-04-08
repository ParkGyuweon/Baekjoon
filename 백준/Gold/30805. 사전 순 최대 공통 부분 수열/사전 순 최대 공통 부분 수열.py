N = int(input())
numbers_a = list(map(int, input().split()))
M = int(input())
numbers_b = list(map(int, input().split()))

def solution(numbers_a, numbers_b, answer):
    if (not numbers_a) or (not numbers_b):
        return answer

    a_max, b_max = max(numbers_a), max(numbers_b)
    a_idx, b_idx = numbers_a.index(a_max), numbers_b.index(b_max)

    if a_max == b_max:
        answer.append(a_max)
        return solution(numbers_a[a_idx + 1:], numbers_b[b_idx + 1:], answer)
    elif a_max > b_max:
        numbers_a.pop(a_idx)
        return solution(numbers_a, numbers_b, answer)
    elif b_max > a_max:
        numbers_b.pop(b_idx)
        return solution(numbers_a, numbers_b, answer)

answer = solution(numbers_a, numbers_b, [])
if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(' '.join(map(str, answer)))