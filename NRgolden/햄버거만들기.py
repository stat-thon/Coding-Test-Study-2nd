def solution(ingredient):
    ingredient_str = ''.join(map(str,ingredient))
    if '1231' not in ingredient_str:
        return 0
    answer=0
    i=0
    while i<len(ingredient)-3:
        if ingredient[i] == 1:
            if [1,2,3,1] == ingredient[i:i+4]:
                answer+=1
                del ingredient[i:i+4]
                i=i-3
                continue

        i+=1
        
    return answer
