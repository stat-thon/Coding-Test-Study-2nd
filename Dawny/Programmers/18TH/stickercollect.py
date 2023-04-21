def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    one = [0] + sticker[:len(sticker)-1]
    two = [0] + sticker[1:]
    
    onedp = [0 for _ in range(len(one))]
    twodp = [0 for _ in range(len(one))]
    
    onedp[1] = one[1]
    twodp[1] = two[1]
    
    for i in range(2, len(one)):
        onedp[i] = max(onedp[i-1], onedp[i-2]+one[i])
        twodp[i] = max(twodp[i-1], twodp[i-2]+two[i])
        
    return max(onedp[-1], twodp[-1])
