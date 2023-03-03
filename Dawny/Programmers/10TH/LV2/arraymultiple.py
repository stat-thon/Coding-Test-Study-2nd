# 넘파이 개사기
# import numpy as np
# solution = lambda arr1, arr2: (np.array(arr1) @ np.array(arr2)).tolist()

def solution(A, B):
    
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
