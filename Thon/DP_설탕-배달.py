n = int(input())

def sugar(n):
    
    if n == 4 or n == 7:
        return -1
    
    mok15, nam15 = divmod(n, 15)
    
    if nam15 == 7:
        return (mok15 - 1) * 3 + 6
    elif nam15 == 1:
        return (mok15 - 1) * 3 + 4
    elif nam15 == 2 or nam15 == 4:
        return (mok15 - 1) * 3 + 5
    
    else:    
        mok5, nam5 = divmod(nam15, 5) 
        if nam5 == 1:
            return (mok5 - 1) + 2 + mok15 * 3
        elif nam5 == 2:
            return (mok5 - 2) + 4 + mok15 * 3
        elif nam5 == 3:
            return mok5 + 1 + mok15 * 3
        elif nam5 == 4:
            return (mok5 - 1) + 3 + mok15 * 3
        else:
            return mok5 + mok15 * 3
        
print(sugar(n))