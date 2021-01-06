n , k = map(int, input().strip().split())
arr = [0] + list(map(int, input().strip().split()))
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
prefix = [0] * (n + 1)
suffix = [0] * (n + 1)
for i in range(k, len(arr)):
    prefix[i] = max(prefix[i-1], arr[i] - arr[i-k])
suffix[len(arr) - k] = arr[n] - arr[n-k]

for i in range(len(arr) - k - 1, 0, -1):
    #print(i)
    suffix[i] = max(suffix[i+1], arr[i + k - 1] - arr[i - 1])
#print(prefix)
#print(suffix)
result = int(1e18)
for i in range(k, len(arr)):
    pre = i - k
    suf = i + 1
    maxharray = 0
    if (pre >= k):
        maxharray = max(maxharray, prefix[pre])
    if (suf <= n - k + 1):
        maxharray = max(maxharray, suffix[suf])
    #print(test)
    result = min(result, maxharray)
    #print(i, maxharray)
print(result)
    
