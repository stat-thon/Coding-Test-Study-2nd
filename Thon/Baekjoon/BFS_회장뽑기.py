from collections import defaultdict, deque

# input
n = int(input())
graph = defaultdict(list)

while True:
    m0, m1 = map(int, input().split())
    if m0 == -1:
        break
    
    graph[m0].append(m1)
    graph[m1].append(m0)

# bfs
def bfs(x):
    dq = deque()
    dq.append((x, 0))
    
    visited = [0] * n
    visited[x - 1] = 1
    
    while dq:
        m, point = dq.popleft()
        
        for member in graph[m]:
            if visited[member - 1] == 0:
                visited[member - 1] = 1
                dq.append((member, point + 1))
                
    result_dict[x] = point
    return point

# result
result_dict = {i:0 for i in range(1, n + 1)}
min_point = 1e9

for x in range(1, n + 1):
    point = bfs(x)
    min_point = min(min_point, point)
    
result = [key for key in result_dict.keys() if result_dict[key] == min_point]

# print output
print(min_point, len(result))
for i in result:
    print(i, end = ' ')