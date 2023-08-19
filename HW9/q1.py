import random
import numpy as np

def lcs_length(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = np.zeros((m+1, n+1), dtype=int)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]

def estimate_gamma(k, n, num_trials):
    lcs_lengths = []
    for i in range(num_trials):
        s1 = ''.join(str(random.choice(range(k))) for _ in range(n))
        s2 = ''.join(str(random.choice(range(k))) for _ in range(n))
        lcs_lengths.append(lcs_length(s1, s2))
    return sum(lcs_lengths) / num_trials / n

def find_smallest_k(target_gamma, n, num_trials):
    k = 2
    while True:
        gamma_k = estimate_gamma(k, n, num_trials)
        print(f"Estimated gamma_{k} = {gamma_k}")
        if gamma_k < target_gamma:
            return k
        k += 1


target_gamma = 2/5
n = 100
num_trials = 1000

smallest_k = find_smallest_k(target_gamma, n, num_trials)
print(f"Smallest k such that gamma_k < {target_gamma} is {smallest_k}")