import sys
from collections import deque

# sys.stdin = open("input.txt","r")
r,c = map(int,sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

fire_dist = [[-1] * c for _ in range(r)]
jh_dist = [[-1] * c for _ in range(r)]

jh = deque()
fire = deque()

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'F':
            fire.append((i,j))
            fire_dist[i][j] = 0
        elif grid[i][j] == 'J':
            jh.append((i,j))
            jh_dist[i][j] = 0

# 불이 각 칸에 도달하는 최소시간을 먼저 구함
while fire:
    cur_r,cur_c = fire.popleft()
    for i in range(4):
        nr, nc = cur_r + dr[i], cur_c + dc[i]

        if 0 <= nr < r and 0 <= nc < c:
            if grid[nr][nc] != '#' and fire_dist[nr][nc] == -1:
                fire_dist[nr][nc] = fire_dist[cur_r][cur_c] + 1
                fire.append((nr,nc))


while jh:
    cur_r,cur_c = jh.popleft()
    for i in range(4):
        nr, nc = cur_r + dr[i], cur_c + dc[i]

        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            print(jh_dist[cur_r][cur_c] + 1)
            exit()
        

        if grid[nr][nc] == '.' and jh_dist[nr][nc] == -1:
            if fire_dist[nr][nc] == -1 or jh_dist[cur_r][cur_c] + 1 < fire_dist[nr][nc]:
                jh_dist[nr][nc] = jh_dist[cur_r][cur_c] + 1
                jh.append((nr,nc))
                
print('IMPOSSIBLE')
