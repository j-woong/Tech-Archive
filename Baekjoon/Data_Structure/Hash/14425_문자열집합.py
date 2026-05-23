import sys
sys.stdin = open("input.txt","r")
n,m = map(int,sys.stdin.readline().split())

s = set()
for _ in range(n):
    s.add(sys.stdin.readline().strip())

cnt = 0
for _ in range(m):
    word = sys.stdin.readline().strip()
    
    if word in s:
        cnt += 1

print(cnt)