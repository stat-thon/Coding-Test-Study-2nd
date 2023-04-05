n, *target = map(int, open(0))
target = target[::-1]

number = [i for i in range(n, 0, -1)]
result, stack = [], []

while number or stack:
    
    if stack and stack[-1] == target[-1]:
        stack.pop()
        target.pop()
        result.append('-')
    
    elif number:
        stack.append(number.pop())
        result.append('+')
    
    else:
        break

if not stack:
    print('\n'.join(result))
else:
    print('NO')