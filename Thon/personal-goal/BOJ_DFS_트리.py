import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
parents = list(map(int, input().split()))
node_removed = int(input())

# make tree
tree = {i:[] for i in range(n)}
for child, parent in enumerate(parents):
    if parent != -1 and child != node_removed:
        tree[parent].append(child)

root_node = parents.index(-1)

del tree[node_removed]


# dfs
def dfs(node):
    global cnt
    
    if node == node_removed:
        return
    
    if tree[node]:
        for child in tree[node]:
            dfs(child)
            if child == node_removed:
                cnt += 1
    else:
        cnt += 1

cnt = 0
dfs(root_node)
print(cnt)