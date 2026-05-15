from collections import Counter
def solution(s):
    s = s.lower()
    counter = Counter(s)
    
    if counter['p'] == counter['y']:
        return True
    else:
        return False