def solution(picks, minerals):
    
    # 필요한거
    cnt = 0
    time = []
    
    # 광물 5개씩 묶기
    mine = [minerals[5*c: 5*c + 5] for c in range(len(minerals)//5 + 1)]
    
    # 광물캐기
    for mineral in sorted(mine[:sum(picks)]):

        # 최대 피로도가 125이므로 그 이상값
        method1, method2, method3 = 126, 126, 126
        
        # 다이아곡괭이로 캠
        if picks[0] > 0:
            method1 = len(mineral)
        
        # 이온 곡괭이로 캠
        if picks[1] > 0:
            d = mineral.count("diamond")
            method2 = d*5 + len(mineral)-d
        
        # 스톤 곡괭이로 캠
        if picks[2] > 0:
            d = mineral.count("diamond")
            ir = mineral.count("iron")
            method3 = d * 25 + ir * 5 + len(mineral) - d - ir
        
        # 캐는 방법 묶어서 저장하기
        time.append([method1, method2, method3])
    
    # 돌곡괭이로 캤을때 가장 큰것부터 나열
    info = sorted(time, key = lambda x: (x[2], x[1], x[0]))
    
    # 제일 크게 소모되는 피로도를 줄여라
    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                cnt += info.pop()[idx]
            else:
                # 곡괭이가 먼저 끝나면 여기서 종료
                return cnt
    
    # 광물이 먼저 끝나면 여기서 종료
    return cnt
