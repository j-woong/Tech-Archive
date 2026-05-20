def solution(s):
    answer = True
    S = []
    if s[0] == ')' or not s:
        return False
    
    for char in s:
        if char == '(':
            S.append(char)
        else:
            if len(S) == 0:
                return False
            else:
                S.pop()
        
    if len(S) == 0:
        return True
    else:
        return False
