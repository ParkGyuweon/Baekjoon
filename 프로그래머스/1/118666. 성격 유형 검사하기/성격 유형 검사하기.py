def solution(survey, choices):
    score = {'A' : 0, 'N' : 0, 'R' : 0, 'T' : 0, 'C' : 0, 'F': 0, 'J' : 0, 'M' : 0}
    for idx in range(len(survey)):
        if choices[idx] == 7:
            score[survey[idx][1]] += 3
        elif choices[idx] == 6:
            score[survey[idx][1]] += 2
        elif choices[idx] == 5:
            score[survey[idx][1]] += 1
        elif choices[idx] == 3:
            score[survey[idx][0]] += 1
        elif choices[idx] == 2:
            score[survey[idx][0]] += 2
        elif choices[idx] == 1:
            score[survey[idx][0]] += 3
    
    answer = ''
    if score['T'] > score['R']:
        answer += 'T'
    else:
        answer += 'R'
        
    if score['C'] < score['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if score['J'] < score['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if score['A'] < score['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer