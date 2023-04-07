def solution(want, number, discount):
    
    from collections import Counter
    
    want_dict = {w:n for w, n in zip(want, number)}
    result = 0
    for i in range(len(discount) - 9):
        counter = Counter(discount[i: i + 10])
        if counter == want_dict:
            result += 1

    return result