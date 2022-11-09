def solution(s):
    answer = ''
    slist = list(s)
    
    for i, d in enumerate(slist):
        d = d.lower()
        if i == 0 or slist[i-1] == ' ':
            d = d.upper()
            answer += d
        else:
            answer += d
    return answer