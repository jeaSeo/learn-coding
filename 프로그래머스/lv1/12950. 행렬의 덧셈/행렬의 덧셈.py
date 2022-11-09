def solution(arr1, arr2):
    answer = []
    z = []

    for i, x in enumerate(arr1):
        for j, y in enumerate(x):
            a = y + arr2[i][j]
            z.append(a)
        answer.append(z)
        z = []
    return answer