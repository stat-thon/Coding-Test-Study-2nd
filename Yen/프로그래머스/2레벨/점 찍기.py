def solution(k, d):
    answer = 0
    x=0
    while (k*x <=d) :
        a=(d**2-(k*x)**2)**(1/2)
        x+=1
        answer += ((a//k)+1)
    return answer
