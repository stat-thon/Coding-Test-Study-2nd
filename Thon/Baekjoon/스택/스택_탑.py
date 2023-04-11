n = int(input())
tower = list(map(int, input().split()))
result = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    
    while stack and tower[stack[-1]] < tower[i]:
        result[stack.pop()] = i + 1
    
    stack.append(i)
    
print(*result)