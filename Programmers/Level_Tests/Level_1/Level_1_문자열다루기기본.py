def solution(s):
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if not c.isdigit():
                return False
        return True
    else:
        return False
    
"""
*** 더 파이써닉한 코드***
def solution(s):
    return len(s) in (4,6) and s.isdigit():
"""