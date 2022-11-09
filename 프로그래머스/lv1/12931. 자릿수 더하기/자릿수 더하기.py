def solution(n):
    answer = 0
    n = [int(x) for x in list(str(n))]
    for i in n:
        answer += i
    return answer