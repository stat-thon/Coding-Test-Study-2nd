def solution(stones, k):
    start = 1
    end = max(stones)
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                break
        if cnt < k:
            start = mid + 1
        else:
            dab = mid
            end = mid - 1

    return dab
