def solution(array, commands):
    answer = []
    numlist = []
    for cmd in commands:
        i, j, k = cmd
        numlist += sorted(array[i-1:j])
        answer.append(numlist[k-1])
        numlist = []
    return answer