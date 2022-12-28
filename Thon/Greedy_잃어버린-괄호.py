eq = input()

temp = ''
eq_list = []

for i in eq:
    if i.isnumeric():
        temp += i
    else:
        while temp.startswith('0'):
            temp = temp[1:]
        eq_list.append(temp)
        eq_list.append(i)
        temp = ''
while temp.startswith('0'):
    temp = temp[1:]
eq_list.append(temp)

if '-' in eq_list: print(eval(''.join(['-' if i > eq_list.index('-') and s == '+' else s for i, s in enumerate(eq_list)])))
else: print(eval(''.join(eq_list)))
