{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 1, 0, 1)\n",
      "(3, 1, 0, 1)\n",
      "(2, 0, 0, 1)\n",
      "(2, 2, 0, 1)\n",
      "(0, 1, 0, 2)\n",
      "(1, 0, 0, 2)\n",
      "(1, 2, 0, 2)\n",
      "(4, 1, 0, 2)\n",
      "(3, 0, 0, 2)\n",
      "(3, 2, 0, 2)\n",
      "(0, 0, 0, 3)\n",
      "(0, 2, 0, 3)\n",
      "(4, 0, 0, 3)\n",
      "(4, 2, 0, 3)\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "m, n, h = map(int, sys.stdin.readline().split())\n",
    "\n",
    "graph = []\n",
    "for _ in range(h):\n",
    "    co = []\n",
    "    for _ in range(n):\n",
    "        co.append(list(map(int, input().split())))\n",
    "    graph.append(co)\n",
    "    \n",
    "# prepare for bfs\n",
    "dx = [-1, 1, 0, 0, 0, 0]\n",
    "dy = [0, 0, -1, 1, 0, 0]\n",
    "dz = [0, 0, 0, 0, -1, 1]\n",
    "\n",
    "# find points\n",
    "from collections import deque\n",
    "dq = deque()\n",
    "num_space = h * n * m\n",
    "num_nothing = 0\n",
    "num_grown = 0\n",
    "\n",
    "for z in range(h):\n",
    "    for y in range(n):\n",
    "        for x in range(m):\n",
    "            \n",
    "            # 익은 tomato\n",
    "            if graph[z][y][x] == 1:\n",
    "                num_grown += 1\n",
    "                dq.append((x, y, z, 0))\n",
    "                \n",
    "            # 아무것도 없는 곳\n",
    "            elif graph[z][y][x] == -1:\n",
    "                num_nothing += 1\n",
    "\n",
    "# bfs\n",
    "def bfs(dq):\n",
    "\n",
    "    global num_grown\n",
    "\n",
    "    while dq:\n",
    "    \n",
    "        x, y, z, day = dq.popleft()\n",
    "    \n",
    "        for d in range(6):\n",
    "            nx = x + dx[d]\n",
    "            ny = y + dy[d]\n",
    "            nz = z + dz[d]\n",
    "        \n",
    "            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:\n",
    "                graph[nz][ny][nx] = 1\n",
    "                num_grown += 1\n",
    "                dq.append((nx, ny, nz, day + 1))\n",
    "            \n",
    "    if num_nothing + num_grown != num_space:\n",
    "        return -1\n",
    "    else:\n",
    "        return day\n",
    "\n",
    "if num_nothing + num_grown == num_space:\n",
    "    print(0)\n",
    "else:\n",
    "    print(bfs(dq))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "graph"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.11"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
