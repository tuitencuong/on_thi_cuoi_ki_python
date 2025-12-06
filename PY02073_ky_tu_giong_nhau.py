INF = 10**9

t = int(input().strip())
for _ in range(t):
    N = int(input().strip())
    X, Y, Z = map(int, input().split())
    
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        # 1) Insert từ i-1
        dp[i] = dp[i - 1] + X
        
        # 2) Dùng copy từ j
        for j in range(1, i + 1):
            if 2 * j == i:
                dp[i] = min(dp[i], dp[j] + Z)
            elif 2 * j > i:
                dp[i] = min(dp[i], dp[j] + Z + (2 * j - i) * Y)
    
    print(dp[N])