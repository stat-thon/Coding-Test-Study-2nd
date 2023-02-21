from collections import Counter

def solution(p, c):
    
    p_dict, c_dict = Counter(p), Counter(c)
    
    for p_key, p_value in p_dict.items():
        if c_dict[p_key] != p_value:
            return p_key 