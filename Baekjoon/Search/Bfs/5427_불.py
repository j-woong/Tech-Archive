import sys
from collections import deque

# sys.stdin = open("input.txt","r")

t = int(sys.stdin.readline())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(h)]

    sang = deque()
    fire = deque()
    sang_dist = [[-1] * w for _ in range(h)]
    fire_dist = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                sang.append((i, j))
                sang_dist[i][j] = 0
            elif grid[i][j] == '*':
                fire.append((i, j))
                fire_dist[i][j] = 0

    while fire:
        r, c = fire.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if grid[nr][nc] != '#' and fire_dist[nr][nc] == -1:
                    fire_dist[nr][nc] = fire_dist[r][c] + 1
                    fire.append((nr, nc))

    result = -1
    while sang:
        r, c = sang.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                result = sang_dist[r][c] + 1
                break

            if grid[nr][nc] != '#' and sang_dist[nr][nc] == -1:
                if fire_dist[nr][nc] == -1 or sang_dist[r][c] + 1 < fire_dist[nr][nc]:
                    sang_dist[nr][nc] = sang_dist[r][c] + 1
                    sang.append((nr, nc))
        
        if result != -1:
            break
    
    print(result if result != -1 else 'IMPOSSIBLE')