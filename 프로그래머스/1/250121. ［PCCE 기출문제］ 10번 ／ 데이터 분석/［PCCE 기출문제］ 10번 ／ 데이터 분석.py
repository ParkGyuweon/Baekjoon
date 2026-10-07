def solution(data, ext, val_ext, sort_by):
    new_list = []
    line_dict = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    for each in data:
        if each[line_dict[ext]] < val_ext:
            new_list.append(each)
    
    new_list.sort(key = lambda x:x[line_dict[sort_by]])
    return new_list