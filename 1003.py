import sys
before_one=0
for _ in range(int(sys.stdin.readline())):
    zero=1
    one=1
    N=int(sys.stdin.readline())
    if N==0:
        print("1 0")
        continue
    elif N==1:
        print("0 1")
        continue
    for i in range(2,N):
        before_one=zero
        zero=one
        one=before_one+zero
    print(zero,one)
    
    
