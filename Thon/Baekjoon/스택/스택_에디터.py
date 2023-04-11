from collections import deque
import sys
rq = deque()
lq = deque(input())
n = int(input())

def move_left(lq, rq):
    if lq: rq.appendleft(lq.pop())

def move_right(lq, rq):
    if rq: lq.append(rq.popleft())

def backspace(lq):
    if lq: lq.pop()

def plus(lq, char):
    lq.append(char)

for _ in range(n):
    
    comm = sys.stdin.readline()
    
    if comm[0] == 'L':
        move_left(lq, rq)
    elif comm[0] == 'D':
        move_right(lq, rq)
    elif comm[0] == 'B':
        backspace(lq)
    elif comm[0] == 'P':
        plus(lq, comm.split()[1])

print(''.join(lq + rq))