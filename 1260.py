import sys
from collections import deque
def dfs(graph,target,visit):
    visit[target]=True
    dfsAry=[target]
    graph[target].sort()
    for i in graph[target]:
        if not visit[i]:
            dfsAry+=dfs(graph,i,visit)
    return dfsAry
        
def bfs(graph,target,visit):
    queue=deque([target])
    visit[target]=True
    bfsAry=[target]
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if not visit[i]:
                bfsAry.append(i)
                queue.append(i)
                visit[i]=True
    return bfsAry
    

    
N,M,V=map(int,sys.stdin.readline().split())
array=[[] for i in range(N+1)]
visit=[False]*(N+1)
for i in list(range(M)):
    A,B=map(int,sys.stdin.readline().split())
    array[A].append(B)
    array[B].append(A)
a=dfs(array,V,visit)
for i in a:
    print(i,end=' ')
visit=[False]*(N+1)
b=bfs(array,V,visit)
print()
for i in b:
    print(i,end=' ')
