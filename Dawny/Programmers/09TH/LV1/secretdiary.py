def solution(s, skip, index):
    dic = {a:b for b, a in enumerate([chr(c) for c in range(97, 123) if chr(c) not in skip])}
    reverse_dic = dict(map(reversed, dic.items()))
    ans = ''
    for i in s:
        tmp = dic[i] + index
        if tmp >= len(dic):
            tmp %= len(dic)
        ans += reverse_dic.get(tmp)
    return ans
