def solution(n):
    n = list(str(n))
    n=''.join(sorted(n, reverse=True))
    answer = int(n)
    return answer
