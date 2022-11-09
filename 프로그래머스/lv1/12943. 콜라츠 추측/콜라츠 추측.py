def solution(num):
    answer = 0
    while not(num==1):
        if (num%2):
            num = num*3+1
        else:
            num *= 0.5
        answer += 1
        if answer>500:
            answer=-1
            break
    return answer