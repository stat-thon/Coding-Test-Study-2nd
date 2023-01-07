######################################
# 숫자의 합
n = input()
print(eval('+'.join(input())))

######################################
# OX 퀴즈
def cal_score(rep_num):
    score = 0
    for num in range(rep_num + 1):
        score += num
    return score

from collections import deque

def whole_score(OX):
    dq = deque([ox for ox in OX + 'X'])
    result = 0
    rep_O = 0
    
    while dq:
        q = dq.popleft()
    
        if q == 'O':
            rep_O += 1
    
        else:
            result += cal_score(rep_O)
            rep_O = 0
    
    return result


n = int(input())
OX_list = []

for _ in range(n):
    OX_list.append(str(input()))

for OX in OX_list:
    print(whole_score(OX))

######################################
# 알파벳 찾기
word = str(input())

result = []
import string

for alpha in string.ascii_lowercase:
    try:
        result.append(word.index(alpha))
    
    except:
        result.append(-1)
        
for i in result:
    print(i, end = ' ')

######################################
# 단어의 개수
print(len(input().split()))

######################################
# 문자열 반복
n = int(input())

request = []
for _ in range(n):
    request.append(str(input()))
    
for req in request:
    rep, word = int(req.split()[0]), req.split()[1]
    
    result = ''
    for s in word:
        result += s * rep
    
    print(result)

######################################
# 단어 공부
from collections import Counter
letter_count = Counter(str(input()).upper())
if Counter(letter_count.values())[max(Counter(letter_count.values()))] != 1:
    print('?')
else:
    print(letter_count.most_common(1)[0][0])

######################################
# 그룹 단어 체커
n = int(input())

word_list = []
for _ in range(n):
    word_list.append(str(input()))
    
def group_word(word):
    
    if len(set(word)) == len(word):
        return True
    
    temp = ''
    temp_set = set()
    for s in word + '1':
        if s != temp:
            if temp in temp_set:
                return False
            else:
                temp_set = temp_set | {temp}
                temp = s
                
        else:
            pass
        
    return True

result = 0
for word in word_list:
    result += group_word(word)
print(result)

######################################
# 괄호
n = int(input())

test_list = []
for _ in range(n):
    test_list.append(str(input()))

def check(test):
    
    if test.count('(') != test.count(')'):
        return 'NO'
    
    cnt_l, cnt_r = 0, 0
    for s in test:
        if s == '(':
            cnt_l += 1
        else:
            cnt_r += 1
            
        if cnt_r > cnt_l:
            return 'NO'
        
    return 'YES'


for test in test_list:
    print(check(test))

######################################
# 크로아티아 알파벳
word = str(input())

special_case = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for case in special_case:
    try:
        word = word.replace(case, 'a')
    except:
        pass

print(len(word))

######################################
# 단어 정렬
n = int(input())

word_list = []
for _ in range(n):
    word_list.append(str(input()))
    
result = sorted(set(word_list), key = lambda x: (len(x), x))
for word in result:
    print(word)