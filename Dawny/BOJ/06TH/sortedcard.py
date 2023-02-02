# module
import heapq

# input
n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

tmp = 0
hap = 0
while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    tmp = first + second
    hap += tmp
    heapq.heappush(card, tmp)

print(hap)
