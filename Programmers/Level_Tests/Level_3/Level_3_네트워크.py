"""
문제: 네트워크 (DFS/BFS)
난이도: Level 3

[오늘의 삽질 포인트]
1. 변수의 관리 실패:
   - 처음에 dfs함수 내에서 네트워크 갯수를 관리하고 return 하려다보니, 로직에서 answer 변수가 덮어 씌워지는 오류가 발생함.
   - 해결: dfs 함수를 돌면서 바깥에서 dfs함수가 실행되는 횟수를 관리하는 것이 필요함을 깨달음
2. 개선점:
   - computers 배열 자체가 인접 행렬이기 때문에, 별도의 adj 리스트를 만드는 것은 메모리를 낭비하는 것.

[핵심 로직]
- 모든 컴퓨터를 순회하며 방문하지 않은 시작점을 찾는다.
- 새로운 시작점을 발견하면 answer += 1을 하고 DFS를 시작한다.
- DFS는 해당 컴퓨터와 연결된 모든 컴퓨터를 방문처리하여, 이후 메인루프에서 중복으로 세어지지 않게 한다.
"""

def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    adj[i].append(j)

    def dfs(now):
        visited[now] = True
        
        for next_com in adj[now]:
            if not visited[next_com]:
                dfs(next_com)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

"""
개선한 코드
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(now):
        visited[now] = True
        for next_com in range(n):
            # 연결되어 있고 + 아직 방문 안 했고 + 자기 자신이 아닐 때
            if computers[now][next_com] == 1 and not visited[next_com]:
                dfs(next_com)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
"""
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
#  print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))