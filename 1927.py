import sys
import copy
def swap(a,b):
    tmp=a
    a=b
    b=tmp
    return a,b

N=int(sys.stdin.readline())
ar=[0]
deep=1
for i in range(N):
    deep=0
    x=int(sys.stdin.readline())
    if x !=0:
        ar.append(x)
        ap_loc=len(ar)-1
        key=int(ap_loc/2)
        
        while(key!=0):
            if ar[ap_loc]<ar[key]: # 부모노드 값이 자식노드보다 클경우 교
                ar[ap_loc],ar[key]=swap(ar[ap_loc],ar[key])
                ap_loc=key
            key=int(key/2)
    else:# 0 입력시
        if len(ar)==1:
            print(0)
        else:
            ap_loc=len(ar)-1
            ar[1],ar[ap_loc]=swap(ar[1],ar[ap_loc])
            print(ar.pop())
            ap_loc-=1
            target=1
            key=2
            while(key<ap_loc):
                if ar[key]<=ar[key+1]:
                    if ar[key]<ar[target]:
                        ar[target],ar[key]=swap(ar[target],ar[key])
                        target=key
                    else:
                        break
                else:
                    if ar[key+1]<ar[target]:
                        ar[target],ar[key+1]=swap(ar[target],ar[key+1])
                        target=key+1
                    else:
                        break
                key=target*2
            if key==ap_loc and ar[target]>ar[key]:
                ar[target],ar[key]=swap(ar[target],ar[key])


