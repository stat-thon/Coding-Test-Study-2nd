# 답 봄
def solution(numbers):
    
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        
        while stack and numbers[stack[-1]] < numbers[i]:
            q = stack.pop()
            answer[q] = numbers[i]
            
        stack.append(i)
        
    return answer