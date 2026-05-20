from collections import deque
def solution(maps):
    r = len(maps)
    c = len(maps[0])
    visited = [[False] * c for _ in range(r)]
    
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    
    def bfs(i,j):
        queue = deque([(i,j)])
        visited[i][j] = True
        
        while queue:
            cur_r,cur_c = queue.popleft()
            
            for i in range(4):
                nr,nc = cur_r + dr[i] , cur_c + dc[i]
                if 0 <= nr < r and 0 <= nc < c:
                    if not visited[nr][nc] and maps[nr][nc] == 1:
                        queue.append((nr,nc))
                        maps[nr][nc] = maps[cur_r][cur_c] + 1
                        
    bfs(0,0)
    if maps[r-1][c-1] == 1:
        return -1
    else:
        return maps[r-1][c-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))