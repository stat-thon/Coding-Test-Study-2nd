def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    node = set([costs[0][0], costs[0][1]])
    cost = costs[0][2]
    while len(node) != n:
        for n1, n2, dist in costs:
            if n1 in node and n2 in node:
                continue

            elif n1 in node or n2 in node:
                node.update([n1, n2])
                cost += dist
                break
                
    return cost
