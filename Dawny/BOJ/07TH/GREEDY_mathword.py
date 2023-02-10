# module
from collections import deque

# input
n = int(input())
alphabet = {}
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if word[i] in alphabet:
            alphabet[word[i]] += 10 ** (len(word)-i-1)
        else:
            alphabet[word[i]] = 10 ** (len(word)-i-1)

kkk = deque(sorted(alphabet.values(), reverse=True))
result = 0
num = 9
while kkk:
    result += kkk.popleft() * num
    num -= 1
print(result)
