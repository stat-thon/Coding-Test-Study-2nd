from collections import deque

def solution(arr):
    # 답
    a = [0, 0]
    
    q = deque([[arr, len(arr)]])
    while q:
        tree, l = q.popleft()
        if l > 1:
            if sum(sum(tree,[])) == 0:
                a[0] += 1
            elif sum(sum(tree,[])) == len(tree)**2:
                a[1] += 1
            else:
                l //= 2
                q.append([[c[:l] for c in tree[:l]], l])
                q.append([[c[:l] for c in tree[l:]], l])
                q.append([[c[l:] for c in tree[:l]], l])
                q.append([[c[l:] for c in tree[l:]], l])
        else:
            a[sum(sum(tree,[]))] += 1
        
    return a
