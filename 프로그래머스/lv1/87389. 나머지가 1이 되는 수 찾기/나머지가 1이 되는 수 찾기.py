def solution(n):
    i=1
    while True:
        if n%i == 1:
            answer = i
            break
        else:
            i += 1
    return answer