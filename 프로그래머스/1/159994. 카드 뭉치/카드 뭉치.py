def solution(cards1, cards2, goal):
    card1_position = 0
    card2_position = 0
    answer = []
    while True:
        if answer == goal:
            return 'Yes'
        if len(cards1) > card1_position and cards1[card1_position] == goal[len(answer)]:
            answer.append(cards1[card1_position])
            card1_position += 1
        elif len(cards2) > card2_position and cards2[card2_position] == goal[len(answer)]:
            answer.append(cards2[card2_position])
            card2_position += 1
        else:
            return 'No'