"""
문제: 기능개발 (구현)
날짜: 2026-04-16
난이도: 골드5
풀이 포인트:
1. 알고리즘이나 자료구조를 어떤걸 사용할지 결정
2. 로봇이 실제로 움직이는 것 처럼 시뮬레이션 코드 작성
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
n,m = map(int,sys.stdin.readline().split())

start_r,start_c,Dir = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 0: 청소안된방 1: 벽 2: 청소된 방
def solve(r,c,d):
    ans = 0
    while True:
        if grid[r][c] == 0:
            grid[r][c] = 2
            ans += 1
        
        is_blank = False

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 0:
                    is_blank = True

        # 빈칸이 없다면
        if not is_blank:
            back_r,back_c = r - dr[d], c - dc[d]
            if 0 <= back_r < n and 0 <= back_c < m and grid[back_r][back_c] != 1:
                r,c = back_r, back_c
            else:
                return ans
        
        else:
            d = (d + 3) % 4
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                r,c = nr,nc
            
print(solve(start_r,start_c,Dir))
