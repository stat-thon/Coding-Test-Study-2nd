from itertools import product
from collections import deque

def solution(users, emoticons):
    
    # 할인율 경우의 수 구하기
    할인율 = list(product([0.9, 0.8, 0.7, 0.6], repeat = len(emoticons)))
    maxperson = 0
    maxmoney = 0
    
    # 삼중포문이 되네
    # 각 할인율 경우마다 가입자, 매출합 구하기
    for percent in 할인율:
        price = list(map(lambda x, y: [round(x * y), y], emoticons, percent))
        q = deque(users)
        person = 0
        money = 0
        
        # 전체 가입자 수와 매출액 구하기
        while q:
            a, b = q.popleft()
            onepersonbuy = 0
            a = 1 - a/100
            
            # 한 사람이 구매하려는 이모티콘 가격 구하기
            for i in price:
                if a >= i[1]:
                    onepersonbuy += i[0]
                    
            # 구매금액보다 크면 가입
            if onepersonbuy >= b:
                person += 1
            
            # 안하면 매출액 증가
            else:
                money += onepersonbuy
        
        # 최대 가입자 수보다 크면 사람수와 매출가격 전부 업데이트
        if maxperson < person:
            maxperson = person
            maxmoney = money
            
        # 최대 가입자 수와 같으면 매출액 비교하기
        elif maxperson == person and maxmoney < money:
            maxmoney = money
            
    return [maxperson, maxmoney]
