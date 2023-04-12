{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', ' ', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "a = 'ab cd'\n",
    "print(list(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', ' ', 'c', 'd', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "a = list(a)\n",
    "a += [1, 2, 3]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<ab cd>fe hg<ij kl>\n"
     ]
    }
   ],
   "source": [
    "from collections import deque\n",
    "dq = deque(input())\n",
    "stack = []\n",
    "result = []\n",
    "\n",
    "while dq:\n",
    "    q = dq.popleft()\n",
    "    \n",
    "    if q == '<':\n",
    "        result += stack[::-1]\n",
    "        stack = []\n",
    "        stack.append(q)\n",
    "        \n",
    "        while True:\n",
    "            nq = dq.popleft()\n",
    "            stack.append(nq)\n",
    "            if nq == '>':\n",
    "                result += stack\n",
    "                stack = []\n",
    "                break\n",
    "                \n",
    "    elif q == ' ':\n",
    "        result += stack[::-1]\n",
    "        result.append(' ')\n",
    "        stack = []\n",
    "        \n",
    "    else:\n",
    "        stack.append(q)\n",
    "\n",
    "result += stack[::-1]\n",
    "\n",
    "print(''.join(result))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
