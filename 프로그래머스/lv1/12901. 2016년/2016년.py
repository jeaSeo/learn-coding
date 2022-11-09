def solution(a, b):
    m = 0
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    months = [31, 29, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
    for i in range(1,a):
        m += months[i-1]

    return week[(m+b+4)%7]