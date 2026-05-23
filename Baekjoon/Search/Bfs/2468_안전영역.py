import sys
from collections import deque
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
building_h = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(r,c,h,visited):
    queue = deque([(r,c)])
    visited[r][c] = True

    while queue:
        cur_r , cur_c = queue.popleft()

        for i in range(4):
            nr , nc = cur_r + dr[i] , cur_c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if building_h[nr][nc] > h and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr,nc))
                    
result = 0             
for h in range(0,101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
            for j in range(n):
                if building_h[i][j] > h and not visited[i][j]:
                    bfs(i,j,h,visited)
                    cnt += 1
                    
    result = max(result,cnt)
print(result)        