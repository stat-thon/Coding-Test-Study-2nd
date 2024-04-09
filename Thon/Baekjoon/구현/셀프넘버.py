### 셀프넘버
# 고민: 6분
# 코딩: 15분

def d(n):
    
    s = str(n)

    cnt = n
    for i in s:

        cnt += int(i)

    return cnt


allset = set(i for i in range(1, 10001))

nonself_set = set()
for i in range(1, 10001):
    nonself_set.add(d(i))


for i in sorted(list(allset - nonself_set)):
    print(i)