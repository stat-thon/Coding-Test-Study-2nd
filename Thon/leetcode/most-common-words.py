# 파이썬 알고리즘 인터뷰 6장 4번 문제
# https://leetcode.com/problems/most-common-word/

class Solution:
    # My solution
    def mostCommonWord(self, paragraph, banned):
        from collections import Counter
        temp = ''
        words = []
        for letter in paragraph + '.':
            if letter.isalnum():
                temp += letter.lower()
            else:
                words.append(temp)
                temp = ''
        word_count = Counter(words)


        banned.append('')
        for ban in banned:
            del word_count[ban]

        return word_count.most_common(1)[0][0]

    # Solution
    def solution(self, paragraph, banned):
        import re
        from collections import Counter
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph) # 정규 표현식으로 전처리한 셈
        .lower().split() if word not in banned]

        counts = Counter(words)
        return counts.most_common(1)[0][0]
