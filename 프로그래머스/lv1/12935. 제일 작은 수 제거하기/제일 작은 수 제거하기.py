def solution(arr):
    answer=[]
    if len(arr) in (0,1):
        answer.append(-1)
    else: 
        answer = arr[:] 
        arr.sort()
        i = arr[0]
        answer.remove(i)
    return answer