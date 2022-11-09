def solution(x):
    answer = sum(list(map(int, str(x))))
    if (x % answer):
        answer = False
    else:
        answer = True
    return answer