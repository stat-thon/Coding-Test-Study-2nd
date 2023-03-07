def solution(arr1, arr2):
    answer = []
    for i in arr1:
        a=[]
        for k in range(len(arr2[0])):
            b=0
            l=0
            for j in arr2:
                b+= i[l]* j[k]
                l+=1
            a.append(b)
        answer.append(a)
    return answer
