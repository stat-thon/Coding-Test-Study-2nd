# input
s = input()
a = 2
cnt = -1
for i in s:
    if a != i:
        cnt += 1
    a = i
print(cnt // 2 + 1 if cnt % 2 != 0 else cnt // 2)
