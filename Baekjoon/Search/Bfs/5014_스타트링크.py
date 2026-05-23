import sys
from collections import deque
# sys.stdin = open("input.txt","r")
f,s,g,u,d = map(int,sys.stdin.readline().split())
visited = [False] * (f+1)
stairs = [0] * (f+1)

visited[s] = True
queue = deque([s])
while queue:
    cur_stair = queue.popleft()
    
    if cur_stair == g:
        print(stairs[cur_stair])
        exit()    

    for next_stair in (cur_stair + u, cur_stair - d):
        if next_stair <= f and next_stair > 0:
            if not visited[next_stair]:
                queue.append((next_stair))
                visited[next_stair] = True
                stairs[next_stair] = stairs[cur_stair] + 1
            

print('use the stairs')