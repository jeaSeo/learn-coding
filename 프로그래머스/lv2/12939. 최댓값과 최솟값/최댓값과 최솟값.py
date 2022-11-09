def solution(s):
    nums = list(map(int, s.split()))
    nums.sort()
    a,b = nums[0], nums[-1]
    return f'{a} {b}'