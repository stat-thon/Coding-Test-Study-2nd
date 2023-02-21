def solution(lottos, win_nums):
    
    same = 0
    num_zero = 0
    for my_num in lottos:
        if my_num == 0:
                num_zero += 1
                
        for win_num in win_nums:
            if my_num == win_num:
                same += 1
                
    lowest = lambda x: 6 if x < 2 else 7 - x
    return [lowest((same + num_zero)), lowest(same)]