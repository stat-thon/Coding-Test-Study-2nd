from collections import deque

def bfs(x,y,n,arr):
    q=deque()
    arr[x]=1        
    q.append(x)
    while q :
        x=q.popleft()
        if 0<= x+n <=1000000 and arr[x+n]==0 :
            arr[x+n]=arr[x]+1
            q.append(x+n)
        if 0 <= x*2<=1000000 and arr[x*2]==0:
            arr[x*2]=arr[x]+1
            q.append(x*2)
        if 0 <= x*3 <=1000000 and arr[x*3]==0 :
            arr[x*3]=arr[x]+1
            q.append(x*3)


def solution(x, y, n):
    arr=[0]*1000001
    bfs(x,y,n,arr)
    return arr[y]-1
