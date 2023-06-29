from collections import defaultdict

nums = [10, 2, -2, -20, 10]
k = -10
def countSubarrayswithSumK(a, K):
    n = len(a)
    hash = defaultdict(lambda: 0)
    count = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum == K:
            count += 1
        if (sum - K) in hash:
            count += hash[sum - K]
        hash[sum] += 1
    return count
print(countSubarrayswithSumK(nums,k))
def count2(a,k):
    h = {0:1}
    s = 0
    r = 0
    for i in a:
        s = s + i
        if s-k in h:
            r = r + h[s-k]
        if s not in h:
            h[s] = 1
        else:
            h[s] = h[s] + 1
    return r
#a = [1,1,1]
#k = 2
print(count2(nums,k))