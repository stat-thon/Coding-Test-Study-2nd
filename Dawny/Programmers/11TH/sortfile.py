def solution(files):
    word = []
    for a in files:
        head = ""
        number = ""
        tail = ""
        alpha = 0
        digit = 0
        for i in a:
            if (i.isalpha() or i in ['.', '-', ' '] )and alpha == 0:
                head += i
            elif i.isdigit() and digit == 0:
                alpha = 1
                number += str(i)
            else:
                digit = 1
                tail += i
        word.append([head, number, tail])
        
    return list(map(lambda y: ''.join(y), sorted(word, key = lambda x: (x[0].lower(), int(x[1])))))
