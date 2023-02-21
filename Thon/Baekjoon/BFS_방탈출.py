n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([int(i) for i in input().split()])


from collections import deque

# 시작점 정해주면 그 점에서 가장 먼 최단경로거리와 양쪽 합 구해주는 함수
def bfs(start_x, start_y):

    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1
    
    dq = deque()
    dq.append((start_x, start_y, 0, 0)) # 시작 x, 시작 y, 거리, 패스워드

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start_num = graph[start_x][start_y]

    # 흔한 bfs 경로 찾는 문제인데 break없이 제일 먼 좌표까지 가도록 둠
    # 그래야 시작점으로부터 가장 길이가 긴 최단경로에 해당하는 끝점 찾을 수 있음
    while dq:
        
        x, y, dist, password = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] != 0:
                        visited[nx][ny] = 1
                        dq.append((nx, ny, dist + 1, start_num + graph[nx][ny]))
        
    return dist, password

# 출발 가능한 시작점 좌표만 저장
coor_list = [(i, j) for i in range(n) for j in range(m) if graph[i][j] != 0]

# 출발 가능한 시작점에 대한 실험 시작
MAX_dist = 0
password = 0

for coor in coor_list:
    start_x, start_y = coor
    dist, pw = bfs(start_x, start_y)
    
    # 지금 최단거리가 이전에 계산된 최단거리보다 길면 패스워드 갱신
    if dist > MAX_dist:
        MAX_dist = max(dist, MAX_dist)
        password = pw

    # 최단거리 동점이면 -> 패스워드끼리 비교해서 더 큰 패스워드를 저장
    elif dist == MAX_dist and dist != 0:
        password = max(pw, password)

print(password)