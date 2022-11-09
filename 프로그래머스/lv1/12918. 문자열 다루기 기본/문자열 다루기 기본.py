def solution(s):
    numbers = set(['0','1','2','3','4','5','6','7','8','9'])
    x = set(s)|numbers
    if len(s) == 4 or len(s) == 6:
        if len(x) >10:
            return False
        else:
            pass
    else: 
        return False
    return True