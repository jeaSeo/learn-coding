def solution(phone_number):
    answer = []
    phone_number.split()
    for i,d in enumerate(phone_number):
        if i < len(phone_number) - 4:
            answer.append('*')
        else: 
            answer.append(d)
    return ''.join(answer)