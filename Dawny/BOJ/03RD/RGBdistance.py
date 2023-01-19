# count house
house = int(input())
mindmap = []

for i in range(house):
    mindmap.append(list(map(int, input().split(' '))))

for j in range(1, house):
    mindmap[j][0] = min(mindmap[j - 1][1], mindmap[j - 1][2]) + mindmap[j][0]
    mindmap[j][1] = min(mindmap[j - 1][0], mindmap[j - 1][2]) + mindmap[j][1]
    mindmap[j][2] = min(mindmap[j - 1][0], mindmap[j - 1][1]) + mindmap[j][2]

print(min(mindmap[house - 1]))
