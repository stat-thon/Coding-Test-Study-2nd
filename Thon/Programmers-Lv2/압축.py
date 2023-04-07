def solution(msg):
    
    a_dict = {chr(i): i - 64 for i in range(65, 91)}
    result = []
    ind = 0
    char = msg[0]

    while ind < len(msg):
        
        # 사전에 있는 단어인 경우
        if char in a_dict:
            
            # 현재 인덱스가 마지막 인덱스가 아니면
            if ind != len(msg) - 1:
                ind += 1
            
            # 마지막 인덱스이면
            else:
                result.append(a_dict[char]) # (색인값)을 결과에 추가하고 break
                break
            
            # 이게 핵심. 사전에 있으면 단어를 업데이트 해줌으로써 ind 초기화 할 필요 없음
            char += msg[ind]
        
        # 사전에 없는 단어인 경우
        else:
            a_dict[char] = len(a_dict) + 1 # 단어 추가
            result.append(a_dict[char[:-1]]) # 사전에서 단어 찾아서 결과에 색인값 추가
            char = msg[ind] # 사전에 없는 단어 찾았으면, 단어 초기화
            
    return result