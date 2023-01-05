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