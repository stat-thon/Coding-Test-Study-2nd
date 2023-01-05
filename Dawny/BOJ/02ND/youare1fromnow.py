# input
x = int(input())

# value
d = [0] * (x+1)

# DP
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[x])

########################################################
############# my first sol ##############
### 오답 ### 

# input
k = input()

# dynamic programming

cnt = [0]
n = [1]
a, b, c = [0, 0, 0]
num = 0

for i in range(1, int(k)+1):
    if int(k) in n:
        print(cnt[n.index(int(k))])
        break

    a = i + 1
    b = i * 2
    c = i * 3
    num = cnt[n.index(i)]
    if a not in n:
        cnt.append(num+1)
        n.append(a)
    if b not in n:
        cnt.append(num+1)
        n.append(b)
    if c not in n:
        cnt.append(num+1)
        n.append(c)
