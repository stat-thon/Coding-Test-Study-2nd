{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yxz\n"
     ]
    }
   ],
   "source": [
    "from collections import deque\n",
    "rq = deque()\n",
    "lq = deque(input())\n",
    "n = int(input())\n",
    "\n",
    "def move_left(lq, rq):\n",
    "    if lq: rq.appendleft(lq.pop())\n",
    "\n",
    "def move_right(lq, rq):\n",
    "    if rq: lq.append(rq.popleft())\n",
    "\n",
    "def backspace(lq):\n",
    "    if lq: lq.pop()\n",
    "\n",
    "def plus(lq, char):\n",
    "    lq.append(char)\n",
    "\n",
    "for _ in range(n):\n",
    "    \n",
    "    comm = input()\n",
    "    \n",
    "    if comm[0] == 'L':\n",
    "        move_left(lq, rq)\n",
    "    elif comm[0] == 'D':\n",
    "        move_right(lq, rq)\n",
    "    elif comm[0] == 'B':\n",
    "        backspace(lq)\n",
    "    elif comm[0] == 'P':\n",
    "        plus(lq, comm.split()[1])\n",
    "\n",
    "print(''.join(lq + rq))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P x\n"
     ]
    }
   ],
   "source": [
    "a = input()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a[0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "thon",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
