def solution(arr1, arr2):
    m, n = len(arr1), len(arr2[0])
    
    col_arr = []
    for j in range(len(arr2[0])):
        col_arr.append([])
        for i in range(len(arr2)):
            col_arr[j].append(arr2[i][j])
        
    result = []
    for i in range(m):
        
        result.append([])
        
        for j in range(n):
            
            row = arr1[i]
            col = col_arr[j]
            rc_sum = 0
            
            for r, c in zip(row, col):
                rc_sum += r * c
            
            result[i].append(rc_sum)
            
    return result