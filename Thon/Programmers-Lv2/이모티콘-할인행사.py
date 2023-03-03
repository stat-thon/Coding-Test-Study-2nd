from itertools import product

def solution(users, emoticons):
    rates = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    n = len(emoticons)
    
    MAX_user, MAX_rev = 0, 0
    
    for rate in product(rates, repeat = n):
        
        emo_plus, rev = 0, 0
        
        for user_rate, user_limit in users:
                user_sum = 0
                
                # 각 emoticon * 개별 할인율 반영한 결과 계산
                for i in range(n):
                    
                    # 사용자 할인율 이상일 때만 계산
                    if rate[i] >= user_rate:
                        user_sum += emoticons[i] * rates[rate[i]]
                
                # 계산된 합이 유저 가격한계 이상이면 이모티콘 플러스 구매
                if user_sum >= user_limit:
                    emo_plus += 1
                
                # 가격한계 미만이면 수익에 합
                else:
                    rev += user_sum
        
        # rate 조합을 MAX 값들과 비교
        if MAX_user < emo_plus:
            MAX_user = emo_plus
            MAX_rev = rev
        
        elif MAX_user == emo_plus:
            MAX_rev = max(MAX_rev, rev)
        
    return [MAX_user, MAX_rev]