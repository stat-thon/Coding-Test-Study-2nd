{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 7 7 -1 "
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "arr = list(map(int, input().split()))\n",
    "result = [-1] * n\n",
    "stack = []\n",
    "\n",
    "for i in range(n):\n",
    "    while stack and arr[stack[-1]] < arr[i]:\n",
    "        result[stack.pop()] = arr[i]\n",
    "    \n",
    "    stack.append(i)\n",
    "\n",
    "print(*result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 7 7 -1\n"
     ]
    }
   ],
   "source": [
    "print(*result)"
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
