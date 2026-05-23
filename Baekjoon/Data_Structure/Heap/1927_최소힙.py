import sys
import heapq
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(ans,x)
    else:
        if ans:
            print(heapq.heappop(ans))
        else:
            print(0)
