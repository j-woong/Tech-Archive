import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,k = map(int,sys.stdin.readline().split())

def solution(n,k):
    queue = deque(range(1,n+1))
    ans = []
    
    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())        
        ans.append(str(queue.popleft()))
    return ans

result = solution(n,k)

print(f"<{', '.join(result)}>")