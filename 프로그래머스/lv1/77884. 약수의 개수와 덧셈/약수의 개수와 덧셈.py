def solution(left, right):
    answer = 0
    curr=[]
    for i in [x for x in range(left, right+1)]:
        for j in range(1, i+1):
            if int(i%j) == 0:
                curr.append(j)
        if curr:
            if len(curr)%2 == 0:
                answer += i
            else:
                answer -= i
        curr = []
    return answer