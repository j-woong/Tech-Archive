def solution(s):
    answer = 0
    len_x = 0
    len_not_x = 0
    curr = s[0]
    
    for c in s:
        if len_x == 0:
            curr = c
            len_x += 1
            continue
        
        if c == curr:
            len_x += 1
        else:
            len_not_x += 1
        
        if len_x == len_not_x:
            answer += 1
            len_x = 0
            len_not_x = 0
            
    if len_x > 0:
        answer += 1
    return answer