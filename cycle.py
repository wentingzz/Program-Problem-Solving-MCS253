import sys
from collections import deque, defaultdict

n,edges = eval(sys.argv[1]),eval(sys.argv[2])

def getCycleNodes():
    parent = [i for i in range(n)]
    
    def getParent(node):
        if node != parent[node]:
            parent[node] = getParent(parent[node])
        return parent[node]
    def getCycle(u,v):
        pU, pV = getParent(u), getParent(v)
        if pU == pV:
            return True
        else:
            if pU > pV:
                pU, pV = pV, pU
            parent[pV] = pU
            return False
    res = deque()
    for u,v in edges:
        if getCycle(u,v):
            cycleParent = getParent(u)
            for i in range(n):
                if getParent(i) == cycleParent:
                    res.append((i,0))
            break
    return res

def adjacentList():
    dic = defaultdict(list)
    for u,v in edges:
        dic[u].append(v)
        dic[v].append(u)
    return dic

queue = getCycleNodes()
adj = adjacentList()
res = [float("inf")] * n

while queue:
    node, level = queue.popleft()
    for neighbor in adj[node]:
        if res[neighbor] > level + 1:
            queue.append((neighbor, level+1))
    res[node] = min(res[node], level)
print(res)
