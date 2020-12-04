import sys
N=int(sys.stdin.readline())
arr=[0 for i in range(N)]
dp=[0 for i in range(N)]
for i in range(N):
    arr[i]=int(sys.stdin.readline().rstrip())

# dp[n] = dp[i-2] + arr[i]                // 마지막계단과 전전계단까지의 최댓값
# dp[n] = dp[i-3] + arr[i-1] + arr[i]     // 마지막계단과 전계단, 전전전계단까지의 최댓값
dp[0]=arr[0]
if N==1:
    print(dp[0])
elif N==2:
    dp[1]=max(arr[0]+arr[1],arr[1])
    print(dp[1])
else:
    dp[1]=max(arr[0]+arr[1],arr[1])
    dp[2]=max(arr[0]+arr[2],arr[1]+arr[2])

    for i in range(3,N):
        dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
    print(dp[N-1])
