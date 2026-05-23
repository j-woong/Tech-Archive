import sys
from collections import deque
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())

def solution(n):
    queue = deque([i for i in range(1,n+1)])

    while len(queue) > 1:
        discard = queue.popleft()
        queue.append(queue.popleft())
    
    return queue[0]

print(solution(n))