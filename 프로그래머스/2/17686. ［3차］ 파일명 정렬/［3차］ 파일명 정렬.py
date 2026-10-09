def solution(files):
    new_files, answer = [], []
    for file_idx in range(len(files)):
        new_file = files[file_idx].lower()
        number = ''
        end = len(new_file) - 1
        for idx in range(len(new_file)):
            if not number and new_file[idx].isnumeric():
                start = idx
            if number and not new_file[idx].isnumeric():
                end = idx
                break
            if new_file[idx].isnumeric():
                number += new_file[idx]
        new_files.append([file_idx, new_file[0:start], '0' * (100 - len(number)) + number, new_file[end:]])
    
    new_files.sort(key=lambda x:(x[1], x[2], x[0]))
    for new_file in new_files:
        answer.append(files[new_file[0]])
    return answer