def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col-1],-x[0]))
    b=[]
    for i in range(row_begin,row_end+1):
        c=0
        for j in data[i-1]:
            c += j % i
        b.append(c)
    answer =b[0]
    for k in range(1,len(b)):
        answer = answer ^ b[k]
        
    return answer
