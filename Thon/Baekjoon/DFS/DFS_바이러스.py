# input
num_com = int(input())
n = int(input())

graph = [[0] * num_com for _ in range(num_com)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# dfs
def dfs(x):
    
    global cnt
    
    for i in range(num_com):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)
            
visited = [0] * num_com
visited[0] = 1
cnt = 0
dfs(0)                
print(cnt)