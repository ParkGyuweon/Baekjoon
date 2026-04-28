def solution(citations):
    answer = 0
    citation_list = [0] * 10001
    for paper in citations:
        citation_list[paper] += 1
    for idx in range(len(citation_list) - 1, 0, -1):
        citation_list[idx - 1] += citation_list[idx]
        
    for idx in range(len(citation_list) - 1, -1, -1):
        if citation_list[idx] >= idx:
            answer = idx
            break
    return answer