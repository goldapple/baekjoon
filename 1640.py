import sys
N,M=map(int,sys.stdin.readline().split())#세로 N 가로 M
array = [[0]*M for _ in range(N)]
for i in range(N):
    k=sys.stdin.readline().rstrip()
    for j in range(len(k)):
        array[i][j]=int(k[j])
row_sum=[0 for i in range(N)]
col_sum=[0 for i in range(M)]
row_odd=0
col_odd=0
count=0
for i in range(N):
    for j in range(M):
        row_sum[i]+=array[i][j]
    if row_sum[i]%2==1:
        row_odd+=1
for i in range(M):
    for j in range(N):
        col_sum[i]+=array[j][i]
    if col_sum[i]%2==1:
        col_odd+=1
if row_odd%2==0 & col_odd%2==0:#행,열 모두 홀수가 짝수개인 경우
        print(min(N+M-row_odd-col_odd,row_odd+col_odd))
elif row_odd%2==1 & col_odd%2==1: #행,열 모두 홀수가 홀수개인 경우
        print(min(N-row_odd+col_odd,row_odd+M-col_odd))
else:
    print('-1')
