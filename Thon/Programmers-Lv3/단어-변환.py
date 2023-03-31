def solution(begin, target, words):
    
    # to compare 2 words
    def one_letter(word, new_word):
        n = len(word)
        cnt = 0
        for i in range(n):
            if word[i] != new_word[i]:
                cnt += 1
            
            if cnt > 1:
                return False
        
        return True
    
    # graph
    graph = {word:[] for word in words}
    graph[begin] = []
    for word in graph.keys():
        for new_word in words:
            if one_letter(word, new_word) and word != new_word:
                graph[word].append(new_word)
            
    # bfs
    from collections import deque
    dq = deque()
    dq.append((begin, 0))
    visited = set()
    
    while dq:
        
        q, cnt = dq.popleft()
        
        if q == target:
            return cnt
        
        for word in graph[q]:
            if word not in visited:
                visited.add(word)
                dq.append((word, cnt + 1))
      
    return 0