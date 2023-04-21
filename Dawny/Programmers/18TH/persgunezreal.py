def solution(sequence):
    dp = [0] * (len(sequence)+1)
    for i in range(len(sequence)):
        dp[i] = dp[i-1] + sequence[i] * (-1) ** (i)
    return max(dp) - min(dp)
