def solution(numbers, hand):
    keypad = [[1, 4, 7, '*'],
              [2, 5, 8, 0],
              [3, 6, 9, '#']]
    
    result = ''
    temp_left, temp_right = '*', '#'
    for num in numbers:
        
        # 무조건 왼손
        if num in keypad[0]:
            result += 'L'
            temp_left = num
        
        # 무조건 오른손
        elif num in keypad[2]:
            result += 'R'
            temp_right = num
        
        # 양손 판별
        else:
            
            for i in range(3):
                for j in range(4):
                    if keypad[i][j] == temp_left:
                        left_ind = (i, j)
                    
                    if keypad[i][j] == num:
                        num_ind = (i, j)
                    
                    if keypad[i][j] == temp_right:
                        right_ind = (i, j)
                    
            left_dist = abs(left_ind[0] - num_ind[0]) + abs(left_ind[1] - num_ind[1])
            right_dist = abs(right_ind[0] - num_ind[0]) + abs(right_ind[1] - num_ind[1])
            
            if left_dist < right_dist:
                result += 'L'
                temp_left = num
            
            elif left_dist > right_dist:
                result += 'R'
                temp_right = num
            
            else:
                if hand == 'left':
                    result += 'L'
                    temp_left = num
                else:
                    result += 'R'
                    temp_right = num
                    
    return result