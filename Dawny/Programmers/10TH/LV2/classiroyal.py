import heapq
def solution(n, k, enemy):
    r = []
    for lev, alien in enumerate(enemy+[10000000000000]):
        if n - alien >= 0:
            heapq.heappush(r, -alien)
            n -= alien
        elif k > 0:
            k -= 1
            n -= alien
            n -= heapq.heappushpop(r, -alien)
        else:
            break
    return lev
