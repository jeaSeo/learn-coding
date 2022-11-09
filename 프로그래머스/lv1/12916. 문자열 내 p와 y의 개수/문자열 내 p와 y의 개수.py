def solution(s):
    answer = True
    innp, inny = 0, 0
    for i,d in enumerate(list(s)):
        if d.upper() == 'P':
            innp += 1
        elif d.upper() == 'Y':
            inny += 1
    if (innp!=inny):
        answer = False
    else:
        pass
    return answer