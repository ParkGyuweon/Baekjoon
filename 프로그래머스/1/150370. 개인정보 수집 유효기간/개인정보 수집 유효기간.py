def solution(today, terms, privacies):
    cur_year, cur_month, cur_day = map(int, today.split('.'))
    month_dict = {}
    for term in terms:
        kind, month = term.split()
        month_dict[kind] = int(month)
    
    answer = []
    for idx in range(len(privacies)):
        privacy = privacies[idx]
        date, kind = privacy.split()
        year, month, day = map(int, date.split('.'))
        expire_date = [year, month + month_dict[kind], day]
        if expire_date[2] == 1:
            expire_date[2] = 28
            expire_date[1] -= 1
        else:
            expire_date[2] -= 1
            
        if expire_date[1] > 12:
            while expire_date[1] > 12:
                expire_date[0] += 1
                expire_date[1] -= 12
        
        if cur_year > expire_date[0]:
            answer.append(idx + 1)
        elif cur_year == expire_date[0] and cur_month > expire_date[1]:
            answer.append(idx + 1)
        elif cur_year == expire_date[0] and cur_month == expire_date[1] and cur_day > expire_date[2]:
            answer.append(idx + 1)
        
    return answer