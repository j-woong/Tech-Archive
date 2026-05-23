import sys
sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
MAX_R = 1000
grid = [[0] * MAX_R for _ in range(MAX_R)]
ans = 0
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())

    if y > 0 and y < 90 and x > 0 and x < 90:
        for i in range(y,y+10):
            for j in range(x,x+10):
                grid[i][j] = 1
                ans += 1

print(ans)