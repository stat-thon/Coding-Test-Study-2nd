import heapq

def solution(k, score):
    answer = []
    four = []
    for i in score:
        if len(four) < k:
            heapq.heappush(four, i)
        elif four[0] < i:
            heapq.heappop(four)
            heapq.heappush(four, i)
        answer.append(min(four))
    return answer
