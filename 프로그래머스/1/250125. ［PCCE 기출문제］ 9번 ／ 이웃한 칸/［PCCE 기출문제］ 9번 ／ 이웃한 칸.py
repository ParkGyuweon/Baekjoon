def solution(board, h, w):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    answer = 0
    if len(board) == 1:
        return 0
    if 0 < h < len(board) - 1 and 0 < w < len(board) - 1:
        for x, y in direction:
            if board[h + y][w + x] == board[h][w]:
                answer += 1
    elif 0 < h < len(board) - 1:
        if board[h + 1][w] == board[h][w]:
            answer += 1
        if board[h - 1][w] == board[h][w]:
            answer += 1
        if w == 0:
            if board[h][w + 1] == board[h][w]:
                answer += 1
        elif w == len(board) - 1:
            if board[h][w - 1] == board[h][w]:
                answer += 1
    elif 0 < w < len(board) - 1:
        if board[h][w + 1] == board[h][w]:
            answer += 1
        if board[h][w - 1] == board[h][w]:
            answer += 1
        if h == 0:
            if board[h + 1][w] == board[h][w]:
                answer += 1
        elif h == len(board) - 1:
            if board[h - 1][w] == board[h][w]:
                answer += 1
    elif h == 0 and w == 0:
        if board[h + 1][w] == board[h][w]:
            answer += 1
        if board[h][w + 1] == board[h][w]:
            answer += 1
    elif h == len(board) - 1 and w == 0:
        if board[h - 1][w] == board[h][w]:
            answer += 1
        if board[h][w + 1] == board[h][w]:
            answer += 1
    elif h == 0 and w == len(board) - 1: 
        if board[h + 1][w] == board[h][w]:
            answer += 1
        if board[h][w - 1] == board[h][w]:
            answer += 1
    elif h == len(board) - 1 and w == len(board) - 1:
        if board[h - 1][w] == board[h][w]:
            answer += 1
        if board[h][w - 1] == board[h][w]:
            answer += 1
    return answer