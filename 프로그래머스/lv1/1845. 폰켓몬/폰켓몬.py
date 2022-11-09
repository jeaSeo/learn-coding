def solution(nums):
    s = len(nums) / 2
    nums = set(nums)
    if len(nums) == s or len(nums) > s:
        return s
    elif len(nums) < s:
        return len(nums)
        