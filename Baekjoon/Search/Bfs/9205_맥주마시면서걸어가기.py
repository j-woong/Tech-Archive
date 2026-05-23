import sys
from collections import deque
# sys.stdin = open("input.txt","r")
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    places = []

    for _ in range(n+2):
        x,y = map(int,sys.stdin.readline().split())
        places.append((x,y))

    # BFS
    visited = [False] * (n+2)
    visited[0] = True
    queue = deque([0])
    
    found = False
    while queue:
        cur = queue.popleft()
        
        if cur == n + 1:
            found = True
            break

        for i in range(n+2):
            if not visited[i]:
                dist = abs(places[cur][0] - places[i][0]) + abs(places[cur][1] - places[i][1])
                if dist <= 1000:
                    visited[i] = True
                    queue.append(i)

    print('happy' if found else 'sad')