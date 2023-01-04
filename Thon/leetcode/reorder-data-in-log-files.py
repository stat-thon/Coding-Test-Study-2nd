# 파이썬 알고리즘 인터뷰 6장 3번문제
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:

    # My solution
    def reorderLogFiles(self, logs):
        
        str_list = []
        num_list = []

        for log in logs:
            alnum = ''.join(log.split()[1:])
            if alnum.isalpha():
                str_list.append(log)
            else:
                num_list.append(log)
        
        # key 안에 정렬 순서 2가지 두는 법 까먹어서 교재 봐버림. 튜플로 하는 거였음
        return sorted(str_list, key = lambda x: (x.split()[1:], x.split()[0])) + num_list
    
    # Solution
    def solution(self, logs):
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits