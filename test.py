def maximumLikes(prediction):
    MOD = 10**9 + 7
    
    if not prediction:
        return 0
    
    max_val = max(prediction)
    
    # Build frequency array
    freq = [0] * (max_val + 1)
    for val in prediction:
        freq[val] += 1
    
    # dp[i] will hold the max likes using popularities up to i
    dp = [0] * (max_val + 1)
    dp[1] = freq[1] * 1
    
    for i in range(2, max_val + 1):
        # Either skip i or take i
        dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])
    
    return dp[max_val] % MOD

def main():
    # Hard-coded example input
    prediction = [1,3]
    
    # Compute the result
    result = maximumLikes(prediction)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
