"""def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings,key=lambda s:s[n])
    
    return answer
"""
def solution(s,n):
    return sorted(s,key= lambda s: (s[n],s))