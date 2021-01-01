import sys
import copy

def dfs(array,sPoint,aSize,count,cCheck):
    
    for i in range(aSize):

        if array[sPoint][i]==1 and cCheck[i]==0: # 해당 지점에 연결된 요소들 중 더 큰수가 있다면
            cCheck[i]=1
            count=dfs(array,i,aSize,count,cCheck)
    return count+1

cSize=int(sys.stdin.readline().rstrip())
cList=[[0]*(cSize+1) for i in range(cSize+1)]
global cCheck
cCheck=[0 for i in range(cSize+1)]
cCheck[1]=1
cPair=int(sys.stdin.readline().rstrip())

for i in range(cPair):
    o,t=map(int,sys.stdin.readline().split())
    cList[o][t]=1
    cList[t][o]=1

print(dfs(cList,1,cSize+1,0,cCheck)-1)
