import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth_people = set(list(map(int, input().split()))[1:])
party_list = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
prev_len, new_len = len(truth_people), 0

if not truth_people:
    print(len(party_list))
else:
    while prev_len != new_len or prev_len + new_len == len(truth_people):
        prev_len = new_len
        for party in party_list:
            if len(party & truth_people) != 0 and len(party & truth_people) != len(party):
                truth_people = truth_people | party
        new_len = len(truth_people)

    answer_party = 0

    for party in party_list:
        if len(party & truth_people) == 0:
            answer_party += 1

    print(answer_party)

