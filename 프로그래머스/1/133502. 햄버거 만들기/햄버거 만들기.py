def solution(ingredients):
    stack = []
    answer = 0
    for ingredient in ingredients:
        stack.append(ingredient)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer