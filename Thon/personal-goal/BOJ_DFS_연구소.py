# 다시 풀어봤는데 시간초과를 해결 못해서 시현이 코드 다시 봄ㅠㅠ

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append([int(x) for x in input().split()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# count safe region
def count_safe_region(graph):
    safe_cnt = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safe_cnt += 1
    return safe_cnt

# make wall (bfs)
from collections import deque

MAX_cnt = 0
def make_wall(level):
    
    global MAX_cnt
    
    if level == 3:
        
        # spread virus
        temp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    
                    dq = deque()
                    dq.append((i, j))
                    while dq:

                        qx, qy = dq.popleft()

                        for d in range(4):
                            nx = qx + dx[d]
                            ny = qy + dy[d]

                            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                                temp[nx][ny] = 2
                                dq.append((nx, ny))

        cnt = count_safe_region(temp)
        
        MAX_cnt = max(MAX_cnt, cnt)
        return
        
    else:
        # make fence
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    make_wall(level + 1)
                    graph[i][j] = 0

# Output
MAX_cnt = 0
make_wall(0)

print(MAX_cnt)

########################
## 시간 효율성 높이는 풀이

from itertools import combinations
N,M = map(int,input().split())
org_box = [list(map(int,input().split())) for _ in range(N)]

# 울타리 세울 수 있는 곳 찾기 (graph == 0) #### 시간 효율성 확보 방법1
def get_zero_pos(v_map):
    zero_pos_list = []
    for i in range(N):
        for j in range(M):
            if v_map[i][j] == 0:
                zero_pos_list.append((i,j))
    return zero_pos_list

def use_stack(N,M,org_box) :
    space = get_zero_pos(org_box)
    virus = [(n, m) for n in range(N) for m in range(M) if org_box[n][m] == 2]
    S = len(space)

    result = -1
    #ct = 0 # 필요한가?

    # 콤비네이션으로 접근 (가능한 0개수 중 3개 뽑기)
    #### 시간 효율성 확보 방법2
    for pair in combinations(range(S), 3): # 그런데 숫자의 조합으로 구해서 인덱스를 사용해 효율적인듯
        #ct += 1
        box = [b[:] for b in org_box] # deepcopy 역할로 일시적인 그래프 생성
        
        # 벽 세 개 세우기
        for d in pair: # d는 space에 저장된 울타리로 가능한 인덱스임
            y, x = space[d] # 울타리 좌표
            box[y][x] = 1 # 벽으로 설정
        
        # 바이러스로 가능한 출발 위치
        stack = [(n, m) for n, m in virus]
        count = S - 3 # 세개 벽으로 세웠으니 빼줌

        # 바이러스 위치만 반복, 최단경로 기록이 목적이 아니라서 굳이 데크를 안 써도 됨.
        while stack:
            y, x = stack.pop()
            
            # 여기서도 cutedge로 시간 효율성 확보 #### 시간 효율성 확보 방법3
            if count < result:
                break
            
            for n, m in (0, 1), (-1, 0), (0, -1), (1, 0):
                if 0 <= y + n < N and 0 <= x + m < M and not box[y + n][x + m]:
                    box[y + n][x + m] = 2 # 바이러스 퍼뜨림
                    count -= 1 # count를 하나씩 뺌으로써 남은 0의 개수를 쉽게 파악 함수 사용없이 가능
                    stack.append((y + n, x + m))

        result = max(result, count)

    return result

print(use_stack(N,M,org_box))

# 결론: 이렇게 생각하려면 머리 아파서 난 못하겠던데..
# 다들 한번에 떠올리지는 않았겠지만 만약에 한번에 떠올렸다면 증말 대단하다.