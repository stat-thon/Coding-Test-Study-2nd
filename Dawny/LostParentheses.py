# input
str = input()

# check this num
if str.count('-') == 0:
    print(sum(list(map(int, str.split('+')))))

else:
    # place minus
    p = str.find('-')
    
    # split str
    front = str[0:p]
    back = str[(p+1):]
    
    # change - for +
    for i in range(len(back)):
        if back[i] == '-':
            back = back[0:i] + '+' + back[(i+1):]
    
    # calculate value
    backnum = list(map(int, back.replace('-', '+').split('+')))
    frontnum = list(map(int, front.split('+')))
    
    print(sum(frontnum) - sum(backnum))

    
##### check this memory
# my memory and time
# 30748KB 36ms
# first grade memory and time
# 30616KB 36ms
