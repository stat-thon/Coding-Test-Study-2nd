# 정답
def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for i in range(len(babbling)):
        for b in baby:
            if b * 2 in babbling[i]:
                babbling[i] = 'a'
                break
    
    for word in babbling:
        
        temp = 0
        word_list = [i for i in word]
        
        while word_list:
            
            temp -= 1
            if ''.join(word_list[temp:]) in baby:
                print(word_list[temp:])
                for _ in range(abs(temp)):
                    word_list.pop()
                
                temp = 0
            
            if temp < -3:
                break
            
        if word_list == []:
            result += 1
            
    return result

# 정답 2
def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for i in range(len(babbling)):
        for b in baby:
            if b * 2 in babbling[i]:
                babbling[i] = 'a'
                break
                
    print(babbling)
    for word in babbling:
        for b in baby:
            if b in word:
                word = word.replace(b, '1')
            
        if word.isnumeric():
            result += 1
        print(word)
    return result

# 왜 안되는지 모르겠다
# 차이점은 remove를 써서 중복인 옹알이를 babbling에서 제거한 것인데.. 이게 문제임

def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for word in babbling:
        for b in baby:
            if b * 2 in word:
                babbling.remove(word) # 유일한 차이
                break
    
    for word in babbling:
        
        temp = 0
        word_list = [i for i in word]
        
        while word_list:
            
            temp -= 1
            if ''.join(word_list[temp:]) in baby:
                print(word_list[temp:])
                for _ in range(abs(temp)):
                    word_list.pop()
                
                temp = 0
            
            if temp < -3:
                break
            
        if word_list == []:
            result += 1
            
    return result