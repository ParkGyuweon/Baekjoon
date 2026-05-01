def solution(str1, str2):
    twochar1 = set()
    twochar2 = set()
    for idx in range(len(str1) - 1):
        num = 0
        cur_char = str1[idx].upper() + str1[idx + 1].upper()
        if str1[idx].isalpha() and str1[idx + 1].isalpha():
            while cur_char + str(num) in twochar1:
                num += 1
            twochar1.add(cur_char + str(num))
            
    for idx in range(len(str2) - 1):
        num = 0
        cur_char = str2[idx].upper() + str2[idx + 1].upper()
        if str2[idx].isalpha() and str2[idx + 1].isalpha():
            while cur_char + str(num) in twochar2:
                num += 1
            twochar2.add(cur_char + str(num))
    if len(twochar1) == 0 and len(twochar2) == 0:
        return 65536
    else:
        return int((len(twochar1 & twochar2)) / len(twochar1 | twochar2) * 65536)
    