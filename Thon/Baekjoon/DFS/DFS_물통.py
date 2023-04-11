import sys
sys.setrecursionlimit(10 ** 6)

limit1, limit2, limit3 = map(int, input().split())
limits = (limit1, limit2, limit3)

# 각 노드에서 뻗어나갈 간선은 6가지 경우의 수 존재
moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

visit = []
result = []

# 출발 노드 기록
visit.append((0, 0, limit3))

# 기본적인 결과 기록
result.append(limit3)

# dfs 정의
def dfs(bottle1, bottle2, bottle3):

    # 세 물통의 현재 상태
    now = (bottle1, bottle2, bottle3)
    
    for move in moves:
        will = [now[0], now[1], now[2]] # 일종의 후보, 업데이트는 for문 안에서 해야만 문제가 안 생김
        move_from, move_to = move
        
        # 물을 끌어다 쓸 물통이 현재 0리터가 아니면 물을 옮길 수 있음 (0리터는 패스)
        if now[move_from] != 0:

            # 옮겨질 물통이 수용 가능한 용량과 옮길 물통 안의 물 중 더 적은 양만 옮길 수 있음
            water_to_be_moved = min(limits[move_to] - now[move_to], now[move_from])

            # 물 이동 후 용량 계산
            will[move_from] -= water_to_be_moved
            will[move_to] += water_to_be_moved

            # 지금 만들어진 조합이 이미 기록된 조합이면 for문의 다음 move로 넘어갈 것
            if tuple(will) in visit:
                continue
            
            # 기록된 적 없는 조합이면 visit 기록하고, 첫번째 물통이 0리터이면 결과도 추가
            else:

                # visit을 append하는 효율이 안 좋을 줄 알았는데 빠르게 통과됨. visit에 기록된 노드가 많지 않아서 가능한 일인 것으로 추정됨
                visit.append(tuple(will))

                # 결과로 추가할 조건 -> 물통 1의 현재 물이 0리터인 경우
                if will[0] == 0:
                    result.append(will[2])
                
                # 재귀
                dfs(will[0], will[1], will[2])

dfs(0, 0, limit3)
print(*sorted(result))