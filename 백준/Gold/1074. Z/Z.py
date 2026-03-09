N, r, c = map(int, input().split())
total_visited = []

def search(start_x, start_y, end_x, end_y, turn, start_num, end_num):
    size = (2 ** turn) * (2 ** turn)
    if start_x <= c <= start_x + 2 ** turn - 1 and start_y <= r <= start_y + 2 ** turn - 1:
        if size == 1:
            print(start_num)
            exit()
        search(start_x, start_y, start_x + 2 ** turn - 1, start_y + 2 ** turn - 1, turn - 1, start_num + 0, start_num + size - 1)
    elif start_x + 2 ** turn <= c <= end_x and start_y <= r <= start_y + 2 ** turn - 1:
        if size == 1:
            print(start_num + size * 1)
            exit()
        search(start_x + 2 ** turn, start_y, end_x, start_y + 2 ** turn - 1, turn - 1, start_num + size, start_num + size * 2 - 1)
    elif start_x <= c <= start_x + 2 ** turn - 1 and start_y + 2 ** turn <= r <= end_y:
        if size == 1:
            print(start_num + size * 2)
            exit()
        search(start_x, start_y + 2 ** turn, start_x + 2 ** turn - 1, end_y, turn - 1, start_num + size * 2, start_num + size * 3 - 1)
    elif start_x + 2 ** turn <= c <= end_x and start_y + 2 ** turn <= r <= end_y:
        if size == 1:
            print(start_num + size * 3)
            exit()
        search(start_x + 2 ** turn, start_y + 2 ** turn, end_x, end_y, turn - 1, start_num + size * 3, start_num + size * 4 - 1)

search(0, 0, 2 ** N - 1, 2 ** N - 1, N - 1, 0, (2 ** N) ** 2 - 1)
