def solution(n):
    m = (n ** (1/2)) +1
    if (int(m)**2 == int(m**2)):
        answer = int(m**2)
    else:
        answer = -1
    return answer