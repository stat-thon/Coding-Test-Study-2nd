def solution(s):
    c = ''
    cnt = 0
    ans = 0
    for i in s:
        if c == '':
            c = i
            cnt += 1 
        else:
            if i == c:
                cnt += 1
            else:
                cnt -= 1
        if cnt == 0:
            ans += 1
            c = ''
    return ans if c == '' else ans + 1
