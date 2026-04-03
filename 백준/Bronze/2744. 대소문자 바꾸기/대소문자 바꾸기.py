S = input()
answer = ''
for item in S:
    if item.isupper():
        answer += item.lower()
    else:
        answer += item.upper()
        
print(answer)