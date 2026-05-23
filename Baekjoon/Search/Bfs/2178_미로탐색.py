import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

n,m = map(int,sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 북:0 동:1 남:2 서:3
dr = [-1,0,1,0] # 행에 대한 이동 
dc = [0,1,0,-1] # 열에 대한 이동 

def bfs(start_r, start_c):
    queue = deque([(start_r,start_c)])

    while queue:
        r,c = queue.popleft()

        if r == n-1 and c == m-1:
            return grid[r][c]
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))

print(bfs(0,0))