def solution(s, skip, index):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
               'r','s','t','u','v','w','x','y','z']
    
    for i in skip:
        alphabet.remove(i)
    L = len(alphabet)
    answer=''    
    for j in s:
        i = alphabet.index(j) + index 
        
        if i>=L:
            i = i - 22
        print(i)
        answer+=alphabet[i]
    return answer
