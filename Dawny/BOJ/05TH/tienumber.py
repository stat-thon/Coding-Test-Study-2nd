# input
n = int(input())
arraylist = []
for _ in range(n):
    arraylist.append(int(input()))

# value
positive = []
negative = []
zero = 0
hap = 0
a, b = [0, 0]
# sort value
question = sorted(arraylist, key=lambda x: abs(x), reverse=True)

# greedy
for i in question:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        zero = 1

    if len(positive) == 2:
        a = positive.pop()
        b = positive.pop()
        if a == 1 or b == 1:
            hap += a + b
        else:
            hap += a * b

    if len(negative) == 2:
        a = negative.pop()
        b = negative.pop()
        hap += a * b

if positive:
    hap += positive[0]

if negative and zero == 0:
    hap += negative[0]

print(hap)
