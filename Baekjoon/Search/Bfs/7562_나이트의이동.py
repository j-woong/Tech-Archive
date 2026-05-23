import sys
from collections import deque
sys.stdin = open("input.txt","r")
t = int(sys.stdin.readline())
dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]
for _ in range(t):
    l = int(sys.stdin.readline())
    grid = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    cur_r , cur_c = map(int,sys.stdin.readline().split())
    res_r , res_c = map(int,sys.stdin.readline().split())

    if cur_r == res_r and cur_c == res_c:
        print(0)
        continue

    queue = deque([(cur_r,cur_c)])
    visited[cur_r][cur_c] = True

    while queue:
        r,c = queue.popleft()

        if r == res_r and c == res_c:
            print(grid[r][c])
            break

        for i in range(8):
            nr,nc = r + dr[i], c + dc[i]
            if 0 <= nr < l and 0 <= nc < l:
                if grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))

    