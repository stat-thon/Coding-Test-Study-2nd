
def dfs(stack,tickets,visited,answer):
    if len(stack)==len(tickets)+1:
        a = [stack[i] for i in range(len(tickets)+1)]
        answer.append(a)
    
    for i in range(len(tickets)):
        if visited[i]==0 and stack[-1]==tickets[i][0]:
            visited[i]=1
            stack.append(tickets[i][1])
            dfs(stack,tickets,visited,answer)
            visited[i] = 0
            stack.pop()


def solution(tickets):
    tickets=sorted(tickets,key=lambda x : x[1])
    answer=[]

    for i in range(len(tickets)):
        stack=[]
        visited= [0] * len(tickets)
        if tickets[i][0]=='ICN':
            stack.append(tickets[i][0])
            stack.append(tickets[i][1])
            visited[i]=1
            dfs(stack,tickets,visited,answer)
    return answer[0]
