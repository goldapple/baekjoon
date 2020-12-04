import sys
N=int(sys.stdin.readline())

M=list(map(int,sys.stdin.readline().split()))
M.sort()
M_Sum=0
for i in range(1,N+1):
    for j in range(i):
        M_Sum+=M[0+j]
print(M_Sum)
