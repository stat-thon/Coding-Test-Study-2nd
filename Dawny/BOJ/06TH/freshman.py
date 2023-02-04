# input
t = int(input())

# greedy
for _ in range(t):
    n = int(input())
    score = []
    for _ in range(n):
        a = list(map(int, input().split()))
        score.append(a)

    score.sort(reverse=True)
    cri = [score.pop()]
    while score:
        d = score.pop()
        if d[1] < cri[-1][1]:
            cri.append(d)

    print(len(cri))
