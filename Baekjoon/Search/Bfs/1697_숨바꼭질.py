import sys
from collections import deque
sys.stdin = open("input.txt","r")
n,k = map(int,sys.stdin.readline().split())
visited = [False] * 100001

def bfs(val,level):
    # 현재 값과 레벨
    queue = deque([(val,level)])
    visited[val] = True

    while queue:
        val,level = queue.popleft()

        if val == k:
            print(level)
            return 

        for next_val in (val+1, val*2, val-1):
            if 0 <= next_val <= 100000 and not visited[next_val]:
                visited[next_val] = True
                queue.append((next_val,level + 1))
        
bfs(n,0)