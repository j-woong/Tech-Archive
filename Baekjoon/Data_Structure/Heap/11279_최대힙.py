import sys
import heapq
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(ans, x * (-1))
    else:
        if ans:
            print(heapq.heappop(ans) * (-1))
        else:
            print(0)
"""
튜플을 이용한 최대 힙 구현

ans = []
# (우선순위, 실제값) 형태로 넣기
heapq.heappush(ans, (-x, x)) 

# 꺼낼 때
max_val = heapq.heappop(ans)[1]
"""


"""
매우 안좋은 코드
for _ in range(n):
    heap = []
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(ans,x)
    
    else:
        if ans:
            for i in ans:
                heapq.heappush(heap,-i)
            print(-heapq.heappop(heap))
            ans = [ -i for i in heap]
        else:
            print(0)
"""