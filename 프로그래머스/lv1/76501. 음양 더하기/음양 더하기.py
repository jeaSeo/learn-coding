def solution(absolutes, signs):
    answer = 0
    for i,d in enumerate(signs):
        if d:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer