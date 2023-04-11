# 1st
def solution(n, words):
    for i, j in enumerate(zip(words[:-1],words[1:])):
        print(i , j)
        if not j[0][-1]==j[1][0] or not words[:i+2].count(j[1]) == 1:
            p, q = divmod(i+1,n)
            return [q+1,p+1]
    return [0,0]
  
# 2nd
from collections import deque

def solution(n, words):
    q = deque(words)
    dic = deque([words[0][0]])
    player = [j+1 for j in range(n)]
    c = 0
    while q:
        turn, number = divmod(c, n)
        word = q.popleft()
        if word in dic or dic[0] and dic[-1][-1] != word[0]:
            return [number+1, turn+1]
        dic.append(word)
        c += 1
    return [0, 0]
# 기존에 풀었던 전략과 유사한 풀이를 도출할 수 있었음.
