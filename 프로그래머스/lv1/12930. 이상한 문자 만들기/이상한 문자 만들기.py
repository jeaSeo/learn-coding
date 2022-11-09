def solution(s):
    answer = ''
    for word in s.split(' '):
        for i, p in enumerate(word):
            if i % 2:
                answer += p.lower()
            else: 
                answer += p.upper()
        answer += ' '
    return answer[:-1]