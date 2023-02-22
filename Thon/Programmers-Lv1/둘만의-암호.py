def solution(s, skip, index):
    alpha = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    result = ''
    for a in s:
        result += alpha[((''.join(alpha).find(a)) + index) % len(alpha)]
    return result