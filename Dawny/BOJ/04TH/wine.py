# input
stairs = int(input())

score = [0]
for i in range(stairs):
    score.append(int(input()))

# dp
if stairs < 2:
    print(sum(score))
else:
    s = [0, score[1], score[1]+score[2]]
    for j in range(3, stairs + 1):
        s.append(max(s[j - 3] + score[j - 1] + score[j], s[j - 2] + score[j], s[j - 1]))
    print(s[stairs])
