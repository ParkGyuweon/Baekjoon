def solution(progresses, speeds):
    release_date = []
    for progress in range(len(progresses)):
        if (100 - progresses[progress]) / speeds[progress] == (100 - progresses[progress]) // speeds[progress]:
            release_date.append((100 - progresses[progress]) // speeds[progress])
        else:
            release_date.append((100 - progresses[progress]) // speeds[progress] + 1)
            
    release_dict = {}
    for item in release_date:
        if not release_dict:
            release_dict[item] = 1
        elif max(release_dict) >= item:
            release_dict[max(release_dict)] += 1
        else:
            release_dict[item] = 1
    return list(release_dict.values())