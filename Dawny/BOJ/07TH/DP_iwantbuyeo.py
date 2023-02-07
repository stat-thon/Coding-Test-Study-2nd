# packages
import sys

# input
cnt = int(sys.stdin.readline())

# DP
people = [[i for i in range(1, 15)]] + [[1]+[0]*13 for _ in range(1, 15)]

for i in range(1, 15):
    for j in range(1, 14):
        people[i][j] = people[i][j-1] + people[i-1][j]

a = []
b = []
for q in range(cnt):
    a.append(int(sys.stdin.readline()))
    b.append(int(sys.stdin.readline()))
    print(people[a[q]][b[q]-1])

################## reupload ####################
