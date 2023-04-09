n=int(input())
arr=[]
for _ in range(n) :
    i=int(input())
    if i != 0:
        arr.append(i)
    else:
        arr.pop()
print(sum(arr))
