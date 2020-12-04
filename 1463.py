import sys
N=int(sys.stdin.readline())
Array_list=list(range(1000001))
Array_list[1]=0
Array_list[2]=1
Array_list[3]=1
for i in range(3,N+1):
    if i%6==0:
        Array_list[i]=min(Array_list[int(i/3)],Array_list[int(i/2)],Array_list[i-1])+1
    elif i%3==0:
        Array_list[i]=min(Array_list[int(i/3)],Array_list[i-1])+1
    else:
        if i%2==0:#짝수일때
            Array_list[i]=min(Array_list[i-1],Array_list[int(i/2)])+1
        else: # 홀수일때
            Array_list[i]=Array_list[i-1]+1
        


print(Array_list[N])

