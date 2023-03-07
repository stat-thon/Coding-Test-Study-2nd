def solution(number, k):
    num = [int(i) for i in number]
    stack = []
    remove = 0
    
    for i in range(len(num)):
        
        while stack and num[stack[-1]] < num[i] and remove < k:
                stack.pop()
                remove += 1
            
        stack.append(i)
    
    answer = ''
    for i in stack:
        answer += str(num[i])
    
    if len(answer) > len(number) - k:
        answer = answer[:len(number) - k]
    
    return answer