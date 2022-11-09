def solution(n):
    answer = 0
    f1 = 0
    f2 = 1
    f = 1
    for i in range(2, n+1):
        f = f1 + f2
        f1 = f2
        f2 = f
    answer = f%1234567
    return answer