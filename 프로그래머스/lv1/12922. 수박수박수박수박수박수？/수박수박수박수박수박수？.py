def solution(n):
    answer = ''
    for r in range(n):
        if (r%2):
            answer += '박'
        else:
            answer += '수'
    return answer