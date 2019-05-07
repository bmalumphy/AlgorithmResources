import collections

def topKFrequent(nums, k):
    result = []
    n = len(nums)
    counts_bucket = [[] for _ in range(n)]

    for x, c in collections.Counter(nums).items():
        counts_bucket[c - 1].append(x)
    print(collections.Counter(nums).items())
    print(counts_bucket)
    for i in range(n - 1, -1, -1):
        if not counts_bucket[i]: continue
        result += counts_bucket[i]
        if len(result) == k: break

    return result
print(topKFrequent([1,1,1,3,4,5,3,1,2,4,2,3,1,1], 2))