def solution(X, Y):
    X_list = sorted(list(str(X)))
    Y_list = sorted(list(str(Y)))
    X_idx, Y_idx = 0, 0
    common = []
    while X_idx < len(X_list) and Y_idx < len(Y_list):
        if X_list[X_idx] == Y_list[Y_idx]:
            common.append(int(X_list[X_idx]))
            X_idx += 1
            Y_idx += 1
        elif X_list[X_idx] < Y_list[Y_idx]:
            X_idx += 1
        elif X_list[X_idx] > Y_list[Y_idx]:
            Y_idx += 1
    if not common:
        return "-1"
    if sum(common) == 0:
        return "0"
    else:
        return ''.join(map(str, sorted(common, reverse=True)))