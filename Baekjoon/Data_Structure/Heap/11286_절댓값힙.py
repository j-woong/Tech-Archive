import sys
import heapq
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
ans = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(ans,(abs(x),x))
    else:
        if len(ans):
            print(heapq.heappop(ans)[1])
        else:
            print(0)