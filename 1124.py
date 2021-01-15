import sys

def prime_list(n):
    sieve=[True]*(n+1)
    a=list()
    for i in range(2,n+1):
        if sieve[i]==True:
            a.append(i)
            for j in range(i+i,n+1,i):
                sieve[j]=False
    # before return [i for i in range(2,n) if sieve[i]==True]
    return a

A,B=map(int,sys.stdin.readline().split())

prime_number=prime_list(B) # 소수 확보
cnt=0
answer=0

for i in range(A,B+1):
    cnt=0
    if i in prime_number:
        continue
    while i!=1:
        for j in prime_number: #소수리스트
            while i%j==0: # 소수리스트의 값으로 나눠지면 계속나누기
                i/=j
                cnt+=1
            if i==1: #다 나눠지면 탈출
                break;
    if cnt!=1:
        if cnt in prime_number:
            answer+=1
print(answer)
