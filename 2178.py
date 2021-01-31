import sys
from collections import deque

def bfs(ary,N,M,visited):
    count=1
    visited[0][0]=True
    Xqueue=deque([0])
    Yqueue=deque([0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    x=0
    y=0
    queue_size=1
    while True:
        for i in range(0,queue_size):
            x=int(Xqueue.popleft())
            y=int(Yqueue.popleft())
            
            for j in range(4):
                tdx=x+dx[j]
                tdy=y+dy[j]
                if 0<=tdx<N and 0<=tdy<M and not visited[tdx][tdy] and ary[tdx][tdy]==1:
                    Xqueue.append(tdx)
                    Yqueue.append(tdy)
                    visited[tdx][tdy]=True
            if (x+1==(N-1) and y==(M-1)) or (x==(N-1) and y+1==(M-1)) :
                return count+1
                    
        queue_size=len(Xqueue)
        count+=1
        
    
N,M = map(int, sys.stdin.readline().split())
ary=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

print(bfs(ary,N,M,visited))
