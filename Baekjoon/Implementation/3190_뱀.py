import sys
from collections import deque
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
grid = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    r,c = map(int,sys.stdin.readline().split())
    grid[r][c] = 2

l = int(sys.stdin.readline())
times = {}
for _ in range(l):
    x,c = sys.stdin.readline().split()
    times[int(x)] = c

direction = 0 # 우:0 하:1 좌:2 상:3
dr = [0,1,0,-1]
dc = [1,0,-1,0]
time = 0
r,c = 1,1
grid[r][c] = 1
snake = deque([(r,c)])

while True:
    time += 1
    nr, nc = r + dr[direction], c + dc[direction]

    if not (1 <= nr <= n and 1 <= nc <= n):
        break

    if grid[nr][nc] == 1:
        break

    if grid[nr][nc] == 2:
        grid[nr][nc] = 1
        snake.append((nr,nc))
    else:
        grid[nr][nc] = 1
        snake.append((nr,nc))
        delr, delc = snake.popleft()
        grid[delr][delc] = 0

    r,c = nr,nc

    if time in times:
        if times[time] == 'D':
            direction = (direction + 1) % 4
        elif times[time] == 'L':
            direction = (direction - 1) % 4


print(time)