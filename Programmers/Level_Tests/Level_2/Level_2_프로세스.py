"""

"""
# 재풀이
from collections import deque
def solution(priorities, location):
    sorted_p = sorted(priorities,reverse=True)
    
    queue = deque((idx,p) for idx,p in enumerate(priorities))
    
    answer = 0
    while queue:
        idx,p = queue.popleft()
        if p == sorted_p[0]:
            answer += 1  
            sorted_p.pop(0)
            
            if idx == location:
                return answer 
            
        else:
            queue.append((idx,p))
        
    return answer
        
"""
from collections import deque
def solution(priorities, location):
    answer = 0
    Q = deque([(p,i) for i,p in enumerate(priorities)])
    
    while Q:
        cur = Q.popleft()

        if any(cur[0] < next[0] for next in Q):
            Q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer
            
"""