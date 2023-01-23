from collections import deque 

n=int(input())
arr=[[] for _ in range(n+1)]

while True :
  x, y = map(int, input().split())
  if x == -1 and y == -1:
    break
  arr[x].append(y)
  arr[y].append(x)



def bfs(x):
  visited = [-1] * (n+1)
  visited[x] = 0
  q = deque([x])
  while q:
    v = q.popleft()
    for w in arr[v]:
      if visited[w] == -1:
        visited[w] = visited[v] + 1
        q.append(w)
  return max(visited)

score = 50
m = []

for i in range(1, n+1):
    a= bfs(i)
    if a < score:
      score = a
      m = [i]
    elif a == score:
        m.append(i)
      
print(score, len(m))
for i in m :
  print(i,end=' ')
