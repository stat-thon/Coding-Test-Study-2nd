# input
t = int(input())

# value
edge = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
    num = int(input())
    if len(edge) > num:
        print(edge[num])
    else:
        for j in range(len(edge), num + 1):
            edge.append(edge[-1]+edge[j-5])
        print(edge[num])
