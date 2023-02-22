import heapq
def time_laps(X):
    t = []
    for i in range(2):
        a = X[i].split(":")
        t.append(int(a[0])*60 + int(a[1]))
    return t


def solution(book_time):
    time = sorted(list(map(time_laps, book_time)), key = lambda x : (x[0], x[1]), reverse = True)
    tmp = time.pop()
    hq = [tmp[1]]
    while time:
        a = time.pop()
        if (hq[0] + 10) <= a[0]:
            heapq.heappop(hq)
            heapq.heappush(hq, a[1])
        else:
            heapq.heappush(hq,a[1])
    return len(hq)
