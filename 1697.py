import sys
from collections import deque

def bfs(n,k):
    if n>k:
        return n-k
    elif n==k:
        return 0
    cnt=0
    ary=[9999999 for _ in range(200000)]
    visited=[False for i in range(200000)]
    que=deque([n])
    que_size=1
    while True:
        for i in range(que_size):
            key=que.popleft()
            if key>100001 or key<0:
                continue
            if not visited[key]:
                visited[key]=True
                
                if cnt<ary[key]:
                    ary[key]=cnt
                else:
                    cnt=ary[key]
                    
                if key+1==k or key-1==k or key*2==k:
                    return ary[key]+1
                que.append(key+1)
                que.append(key-1)
                que.append(key*2)
                
                if cnt+1<ary[key+1]:
                    ary[key+1]=cnt+1
                if cnt+1<ary[key-1]:
                    ary[key-1]=cnt+1
                if key*2<100000:
                    if cnt+1<ary[key*2]:
                        ary[key*2]=cnt+1
        que_size=len(que)
        cnt+=1
    
N,K=map(int,sys.stdin.readline().split())
print(bfs(N,K))
