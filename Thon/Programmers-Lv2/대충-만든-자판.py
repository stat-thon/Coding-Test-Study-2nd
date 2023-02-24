def solution(keymap, targets):
    
    # make dict
    alpha_push = {chr(i): 1000 for i in range(65, 91)}
    
    for key in keymap:
        for i in range(len(key)):
            alpha_push[key[i]] = min(alpha_push[key[i]], i + 1)
    
    # result
    result = []
    for target in targets:
        push = 0
        for i in range(len(target)):
            if alpha_push[target[i]] == 1000:
                push = -1
                break
            else:
                push += alpha_push[target[i]]
        result.append(push)
    
    return result