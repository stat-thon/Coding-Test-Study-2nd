def solution(s):
    num_dict = {'zero': 0, 'one': 1, 'two': 2,
                'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    result = ''
    temp = ''
    for i in s:
        if i.isnumeric():
            result += str(i)
        else:
            temp += str(i)
            
            if temp in num_dict.keys():
                result += str(num_dict[temp])
                temp = ''
    return int(result)